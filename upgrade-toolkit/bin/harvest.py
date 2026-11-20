#!/usr/bin/env python3
"""harvest.py: draft the learnings of a finished upgrade run for the toolkit and the brain, no LLM.

A run teaches the toolkit things that evaporate when its work folder is deleted: a fix the agent made by hand, an error
code no step names, a script the agent wrote to get past a wall, an open item the gate gives the toolkit to fix. This
reads the run's own files and writes them as drafts, each marked for one of two places:

  toolkit   <toolkit>/contrib/inbox/<date>-<code>-harvest.md   generic lessons, scripts and table rows; goes to the
                                                               toolkit repo by PR (bin/submit-learnings.sh toolkit)
  brain     <brain>/inbox/<date>-<code>-upgrade.md             one note draft per lesson the brain has no note for, in
                                                               the brain's note format; goes to the brain repo
                                                               (bin/submit-learnings.sh brain). Internal tier.

What it reads in --work (recursively; a flat run folder and an examples/<app>/<rung>/steps folder both work):
  1. CHANGES.md     rows with by=agent, grouped per rule: a repair row of steps/repair.md, or a term (mx.logger,
                    getContext(), a CE code) that a toolkit file already names, is known and still done by hand;
                    the rest are fixes the toolkit does not know
  2. *.log, *.md    error codes (CE + 4 digits) that no file of steps/, playbooks/ or bin/ names
  3. grade-notes.tsv, gate-summary.md, AGENT-DECISIONS.md   items owned by the toolkit, WARNING lines, agent decisions
  4. *.py *.sh *.js *.mdl   files the agent wrote in the run that are not a copy of a toolkit file (candidate tools)

Brain lookup (--brain, default $UPG_BRAIN; skipped when the folder has no internal/): each error code and each new fix
is grepped in <brain>/internal/. The toolkit draft only says whether the brain has a note; it never copies brain text,
which is internal. Only lessons the brain does not hold get a brain draft.

Every draft is scrubbed (home folders, the run folder path) and then checked against the private denylist
(bin/private_names.sh). A hit writes nothing for that place and exits 1. Review every draft before you submit it.

usage: harvest.py --work DIR --code CODE [--brain DIR] [--to toolkit|brain|both] [--inbox DIR] [--brain-inbox DIR]
                  [--date YYYY-MM-DD]
  --code         the run's app code name (F1, FSM); a name that matches the denylist is refused
  --inbox        toolkit drafts go here instead of <toolkit>/contrib/inbox (a run-local folder in a pipeline)
  --brain-inbox  brain drafts go here instead of <brain>/inbox
Prints one summary line: 'harvest: R agent fixes (K known to the toolkit, N new), C new error codes, S scripts,
O toolkit items'. Exit 0 drafts written or nothing to harvest, 1 denylist hit (that place not written), 2 bad call.
"""
import argparse
import datetime
import hashlib
import os
import re
import subprocess
import sys
from pathlib import Path

TK = Path(__file__).resolve().parent.parent
CE = re.compile(r"\bCE\d{4}\b")
# distinctive terms of a fix: error codes, dotted names (mx.logger, Core.getRuntimeVersion), calls, flags, Module_Names
TERM = re.compile(r"\bCE\d{4}\b|\b[A-Za-z_]\w*\.[A-Za-z_]\w*(?:\(\))?|\b[A-Za-z_]\w*\(\)|(?<!\w)--[a-z][a-z-]+"
                  r"|\b[A-Z][A-Za-z0-9]*_[A-Za-z0-9_]+\b")
FILE_LIKE = re.compile(r"\.(html|js|java|md|jar|mpk|mpr|css|scss|json|log|txt|py|sh|xml|tsv)$", re.I)
SHA = re.compile(r"\s*\(`[0-9a-f]{7,40}`\)")
SCRIPT_EXT = {".py", ".sh", ".js", ".mdl"}
# folders the pipeline writes itself, never the agent: the patched journey engine copy (<work>/e2e-*/engine, run_journeys.py),
# editroute's replay MDL and localedits' saved edits. Their files differ from any toolkit file by design (cold CMM: 37 of
# them were listed as scripts the agent wrote), and the top-level run/ folder, the unpacked runtime of each walked app.
TOOLKIT_WRITTEN = {"replay", "saved-edits"}


def toolkit_written(rel):
    parts = Path(rel).parts
    # NL1: <work>/run/<old|new|oldwalk|...>/ is the unpacked deployment (minified web JS, login page strings, an absolute app path):
    # 40 of its files were listed as "scripts the agent wrote" and copied toward contrib/inbox/
    return parts[0] == "run" or any(p in TOOLKIT_WRITTEN for p in parts[:-1]) or any(
        p == "engine" and i > 0 and parts[i - 1].startswith("e2e-") for i, p in enumerate(parts[:-1]))
SKIP_DIRS = {".git", "node_modules", "__pycache__", "e2e", "playwright-report", "test-results", "vendor"}
TEXT_EXT = {".log", ".md", ".txt", ".out", ".tsv"}
MAX_TEXT = 5_000_000


def deny_pattern():
    out = subprocess.run(["bash", "-c", f'source "{TK}/bin/private_names.sh"; printf %s "$DENY"'],
                         capture_output=True, text=True)
    return out.stdout.strip()


def walk(root):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS and not d.startswith("."))
        for f in sorted(filenames):
            yield Path(dirpath) / f


def read(p):
    try:
        if p.stat().st_size > MAX_TEXT:
            return ""
        return p.read_text(errors="replace")
    except OSError:
        return ""


def table_rows(text):
    """Rows of the first markdown table with a header, as dicts keyed by lowercased header cells."""
    head, rows = None, []
    for line in text.splitlines():
        if not line.startswith("|"):
            if head and rows:
                break
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if head is None:
            head = [c.lower() for c in cells]
        elif set("".join(cells)) <= set("-: "):
            continue
        elif len(cells) == len(head):
            rows.append(dict(zip(head, cells)))
    return rows


def toolkit_docs():
    """(label, text) of every toolkit file that can already hold a lesson."""
    docs = []
    for sub in ("BACKLOG.md", "FEEDBACK.md", "SKILL.md", "READING-THE-VERDICT.md", "steps", "playbooks", "bin"):
        p = TK / sub
        files = [p] if p.is_file() else walk(p) if p.is_dir() else []
        docs += [(str(f.relative_to(TK)), read(f)) for f in files
                 if f.suffix in {".md", ".tsv", ".py", ".sh"} and f.name != "harvest.py"]
    return docs


def terms(text):
    return sorted({t for t in TERM.findall(SHA.sub("", text)) if not FILE_LIKE.search(t)})


def where_known(ts, docs):
    """Where the toolkit already holds the fix: 'BACKLOG.md #144', 'playbooks/x.md', or '' when any of its names is
    unknown. Every distinctive name must be known (a common module name alone proves nothing); a CE code is shared by
    many fixes, so it counts only when the fix has no other name. The place shown is the one of its rarest name."""
    names = [t for t in ts if not CE.fullmatch(t)] or ts
    if not names:
        return ""
    hits = {t: [(label, text) for label, text in docs if t in text] for t in names}
    if not all(hits.values()):
        return ""
    t = min(names, key=lambda n: len(hits[n]))
    label, text = hits[t][0]
    if label == "BACKLOG.md":
        for line in text.splitlines():
            m = re.match(r"\|\s*(\d+)\s*\|", line)
            if m and t in line:
                return f"BACKLOG.md #{m.group(1)}"
    return label


def repair_rows():
    rows = set()
    for line in read(TK / "steps" / "repair.md").splitlines():
        m = re.match(r"\|\s*(\d+)\s*\|", line)
        if m:
            rows.add(m.group(1))
    return rows


def toolkit_hashes(work):
    hs = set()
    for f in walk(TK):
        if "examples" in f.relative_to(TK).parts or work in f.parents:
            continue
        if f.suffix in SCRIPT_EXT:
            try:
                hs.add(hashlib.sha256(f.read_bytes()).hexdigest())
            except OSError:
                pass
    return hs


def brain_has(brain, ts):
    """True when one brain note names every distinctive term (CE codes count only when there is no other name, as in
    where_known), False when none does, None without a brain."""
    if not brain:
        return None
    names = [t for t in ts if not CE.fullmatch(t)] or ts
    notes = None
    for t in names:
        r = subprocess.run(["grep", "-rlF", "--include=*.md", "--", t, str(brain / "internal")],
                           capture_output=True, text=True)
        hit = {l for l in r.stdout.splitlines() if not l.endswith("/INDEX.md")}
        notes = hit if notes is None else notes & hit
        if not notes:
            return False
    return bool(notes)


def first_comment(p):
    for line in read(p).splitlines()[:30]:
        s = line.strip().lstrip("#/*-\"' ").strip()
        if len(s) > 12 and not s.startswith("!") and not s.startswith("usr/bin"):
            return s[:160]
    return "(no description line)"


def harvest(work, brain):
    found = {"fixes": [], "codes": {}, "items": [], "scripts": []}
    known_rows = repair_rows()
    docs = toolkit_docs()
    tk_hash = toolkit_hashes(work)
    groups = {}
    for f in walk(work):
        rel = str(f.relative_to(work))
        if f.name == "CHANGES.md":
            for r in table_rows(read(f)):
                if r.get("by") != "agent":
                    continue
                rule, why = r.get("rule", ""), SHA.sub("", r.get("why", ""))
                key = rule or why
                g = groups.setdefault(key, {"rule": rule, "kind": r.get("kind", ""), "whys": [], "src": rel})
                g["whys"].append(why)
        if f.suffix in TEXT_EXT:
            text = read(f)
            for line in text.splitlines():
                for c in set(CE.findall(line)):
                    e = found["codes"].setdefault(c, {"n": 0, "line": line.strip()[:200], "src": rel})
                    e["n"] += 1
            if f.name == "grade-notes.tsv":
                for line in text.splitlines():
                    cells = line.split("\t")
                    if len(cells) >= 4 and cells[2].strip() == "toolkit":
                        found["items"].append({"src": rel, "text": f"rung {cells[0]}: {cells[3].strip()}"})
            if f.name == "gate-summary.md":
                for line in text.splitlines():
                    if "WARNING:" in line:
                        t = line.split("WARNING:", 1)[1].strip().rstrip("| ").strip()
                        found["items"].append({"src": rel, "text": t[:240]})
            if f.name == "AGENT-DECISIONS.md":
                for r in table_rows(text):
                    if "agent" in r.get("#", ""):
                        found["items"].append({"src": rel, "text": f"agent decision: {r.get('decision', '')}: "
                                                                   f"{r.get('choice', '')} ({r.get('why', '')})"})
        if f.suffix in SCRIPT_EXT and not toolkit_written(rel):
            try:
                h = hashlib.sha256(f.read_bytes()).hexdigest()
            except OSError:
                continue
            if h not in tk_hash:
                found["scripts"].append({"src": rel, "lines": len(read(f).splitlines()), "what": first_comment(f)})
    for g in groups.values():
        m = re.fullmatch(r"repair-row-(\d+)", g["rule"])
        ts = terms(" ".join(g["whys"]))
        g["terms"] = ts
        g["status"] = "by-hand" if (m and m.group(1) in known_rows) else "known" if where_known(ts, docs) else "new"
        g["where"] = f"steps/repair.md row {m.group(1)}" if g["status"] == "by-hand" else where_known(ts, docs)
        g["brain"] = brain_has(brain, ts) if ts else (None if not brain else False)
        found["fixes"].append(g)
    alltext = "\n".join(t for _, t in docs)
    found["codes"] = {c: e for c, e in sorted(found["codes"].items()) if not re.search(r"\b" + c + r"\b", alltext)}
    for c, e in found["codes"].items():
        e["brain"] = brain_has(brain, [c])
    return found


def brain_word(b):
    return {None: "brain not configured", True: "brain has a note", False: "brain has no note (drafted for the brain)"}[b]


def fix_line(g):
    n = f" ({len(g['whys'])}x)" if len(g["whys"]) > 1 else ""
    return f"- `{g['rule'] or 'no rule'}`{n} ({g['kind']}): " + "; ".join(g["whys"])


def toolkit_draft(f, code, date):
    by = {s: [g for g in f["fixes"] if g["status"] == s] for s in ("new", "known", "by-hand")}
    out = [f"**From:** upgrade run {code}", f"**Date:** {date}", "**Kind:** harvest (bin/harvest.py)",
           "**Status:** unreviewed. Triage moves each item to its real home (BACKLOG.md, FEEDBACK.md, steps/repair.md, "
           "playbooks/, bin/) and deletes this file in the same commit.", "", "---", ""]
    if by["new"]:
        out += ["## Fixes the agent made that the toolkit does not know", "",
                "Made by hand in the run; no toolkit file names their terms. Target: a row in steps/repair.md, a "
                "playbook row, or a script.", ""]
        out += [fix_line(g) + f" [{g['src']}; {brain_word(g['brain'])}]" for g in by["new"]]
        out.append("")
    if by["by-hand"] or by["known"]:
        out += ["## Known to the toolkit, still done by hand", "",
                "The toolkit has a recipe or an open item; the agent did the work. One more run that asks for a script.",
                ""]
        out += [fix_line(g) + f" [known: {g['where']}]" for g in by["by-hand"] + by["known"]]
        out.append("")
    if f["codes"]:
        out += ["## Error codes no step or playbook names", "",
                "Target: a row in steps/repair.md or playbooks/, with the fix the run used.", ""]
        out += [f"- {c} ({e['n']} line(s), first in {e['src']}; {brain_word(e['brain'])}): `{e['line']}`"
                for c, e in f["codes"].items()]
        out.append("")
    if f["items"]:
        out += ["## Open items the run gives the toolkit", "", "Target: BACKLOG.md (with a 'done when').", ""]
        out += [f"- {x['text']} [{x['src']}]" for x in f["items"]]
        out.append("")
    if f["scripts"]:
        out += ["## Scripts and recipes written in the run", "",
                "Not a copy of any toolkit file. A generic one becomes a bin/ script with a catch and a pass control; "
                "an app-specific one stays in the run.", ""]
        out += [f"- {x['src']} ({x['lines']} lines): {x['what']}" for x in f["scripts"]]
        out.append("")
    return "\n".join(out)


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:60] or "note"


def brain_draft(f, code, date):
    notes = [(g["whys"][0], g["terms"], g["whys"], g["src"]) for g in f["fixes"] if g["brain"] is False]
    notes += [(f"{c} seen in an upgrade run", [c], [e["line"]], e["src"])
              for c, e in f["codes"].items() if e["brain"] is False]
    if not notes:
        return ""
    out = [f"<!-- inbox draft from bin/harvest.py, upgrade run {code}, {date}. One note per section: move each to "
           "internal/upgrade/<slug>.md, fill in the root cause, check it, then delete this file. -->", ""]
    for title, ts, whys, src in notes:
        title = re.split(r"[:;(]", title, maxsplit=1)[0].strip() if len(title) > 90 else title
        kw = ", ".join(f'"{k}"' for k in ts) or '"(add keywords)"'
        out += ["---", f"title: {title[:100]}", "topic: upgrade", "kind: pitfall", "applies_to: mendix-general",
                'versions: ""', f"keywords: [{kw}]", "layer: internal", "sources:",
                f'  - {{title: "upgrade run {code}", url: "", author: "toolkit harvest", date: "{date}"}}',
                "confidentiality: internal", "status: draft-unreviewed", f"slug: {slug(title)}", "---",
                "**Symptom**"] + [f"- {w}" for w in whys] + [
                "", "**Root cause**", "- (to fill in)", "", "**Fix**", f"- What the run did: see {src}.", "",
                "**Status**", "- seen once; not checked on another app", ""]
    return "\n".join(out)


def scrub(text, work):
    text = text.replace(str(work), "<run>")
    text = re.sub(r"/Users/[^/\s`'\"]+", "/Users/<user>", text)
    return re.sub(r"/home/[^/\s`'\"]+", "/home/<user>", text)


def write(path, text, deny, label):
    hits = [l for l in text.splitlines() if deny and re.search(deny, l, re.I)]
    if hits:
        print(f"harvest: {label} draft names a private term, nothing written for the {label}:", file=sys.stderr)
        for h in hits[:10]:
            print(f"  {h[:200]}", file=sys.stderr)
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)
    print(f"  wrote {path}")
    return True


def main():
    ap = argparse.ArgumentParser(usage=__doc__.split("usage: ")[1].split("\n  --code")[0])
    ap.add_argument("--work", required=True)
    ap.add_argument("--code", required=True)
    ap.add_argument("--brain", default=os.environ.get("UPG_BRAIN", ""))
    ap.add_argument("--to", choices=["toolkit", "brain", "both"], default="both")
    ap.add_argument("--inbox", default=str(TK / "contrib" / "inbox"))
    ap.add_argument("--brain-inbox", default="")
    ap.add_argument("--date", default=datetime.date.today().isoformat())
    a = ap.parse_args()
    work = Path(a.work).resolve()
    if not work.is_dir():
        print(f"harvest: no run folder {a.work}", file=sys.stderr)
        return 2
    deny = deny_pattern()
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,23}", a.code) or (deny and re.search(deny, a.code, re.I)):
        print(f"harvest: --code must be a short code name (letters, digits, - _ .), not an app or customer name",
              file=sys.stderr)
        return 2
    brain = Path(a.brain).expanduser() if a.brain else None
    if brain and not (brain / "internal").is_dir():
        print(f"harvest: {brain} has no internal/ folder, brain lookup skipped")
        brain = None
    f = harvest(work, brain)
    new = sum(g["status"] == "new" for g in f["fixes"])
    print(f"harvest: {len(f['fixes'])} agent fixes ({len(f['fixes']) - new} known to the toolkit, {new} new), "
          f"{len(f['codes'])} new error codes, {len(f['scripts'])} scripts, {len(f['items'])} toolkit items")
    rc, wrote = 0, 0
    if a.to in ("toolkit", "both") and (f["fixes"] or f["codes"] or f["items"] or f["scripts"]):
        ok = write(Path(a.inbox) / f"{a.date}-{a.code}-harvest.md", scrub(toolkit_draft(f, a.code, a.date), work),
                   deny, "toolkit")
        rc, wrote = (rc, wrote + 1) if ok else (1, wrote)
    if a.to in ("brain", "both"):
        bd = brain_draft(f, a.code, a.date) if brain else ""
        if bd:
            target = Path(a.brain_inbox) if a.brain_inbox else brain / "inbox"
            ok = write(target / f"{a.date}-{a.code}-upgrade.md", scrub(bd, work), deny, "brain")
            rc, wrote = (rc, wrote + 1) if ok else (1, wrote)
        elif not brain:
            print("  brain: not configured (set UPG_BRAIN or --brain), no brain drafts")
    if wrote:
        print("Review every draft (names, paths, app detail), then: bin/submit-learnings.sh toolkit | brain")
    elif rc == 0:
        print("Nothing to harvest.")
    return rc


if __name__ == "__main__":
    sys.exit(main())
