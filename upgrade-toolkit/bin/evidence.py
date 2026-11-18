#!/usr/bin/env python3
"""evidence.py: what exactly sits behind one plan item, from the files the run already wrote. A question card shows it, so a person
decides on the elements themselves and not on a label like "local edits refuse the update".

Why (cold test WM1, 2026-11-16): seven "What should the upgrade do with <module>?" cards said only "local edits refuse the update";
the owner asked how anyone can decide that. The run had the answer in its logs: Atlas_Core had 7 layouts and snippets edited,
Encryption only its EncryptionKey constant, Email_Connector one microflow, MendixSSO an attribute the new version drops.

  for_item(work, name, kind=None) -> {"what": [plain lines], "files": [paths relative to the run folder]}
  evidence.py --work W [--kind K] NAME       prints the lines and the files (a check by hand)

A plan item that is no module has its own source (cold CMM, 2026-11-17: the "Release notes" and "DataWidgets themesource
edits" cards were flagged ask-no-evidence on every run, because only module names were looked up):
  kind check, Release notes   W/release-impact.out (why the release-note check did not run)
  kind theme, "<M> themesource edits"   the theme and JavaScript file rows of <M> in W/localedits.json
A replacement card "R<n> <pattern>" (any kind) shows its row's evidence column in W/replacements.md, one line per hit, and a module
card also lists the file rows of the module in W/localedits.json (cold rfq, 2026-11-18: 14 "R18 Runtime Java API removals"-style
cards and the "SAPODataConnector (Java)" card, whose only edit is a Java file, were ask-no-evidence).

Sources, per module (app = state/app-dir, S = app/.stepupdate):
  S/step*-<M>.log        the elements mxcli refused to overwrite, or why it could not read the module
  S/step*-<M>.idcheck    data-bearing changes the update makes (RED rows) and a module deleted and imported again
  S/step*-<M>.files      theme, JavaScript and Java files the update replaced and that could not be proven unedited
  W/localedits.md        the local edits found in triage (UI, domain model, logic)
  W/apimock-inventory.json  the outside calls of the module, with their stand-in status
  W/edit-routes.json     how editroute.py carries the module's edits over (or why it holds them for a person)
"""
import argparse, glob, json, os, re, sys


def _rd(p):
    try:
        with open(p, encoding="utf-8", errors="replace") as f:
            return f.read()
    except OSError:
        return None


def _rel(work, p):
    run = os.path.dirname(os.path.abspath(work))
    return os.path.relpath(p, run)


KIND = {"LAYOUT": "layout", "SNIPPET": "snippet", "PAGE": "page", "MICROFLOW": "microflow", "NANOFLOW": "nanoflow",
        "CONSTANT": "constant", "ENTITY": "entity", "ENUMERATION": "enumeration", "JAVA_ACTION": "Java action"}


def _refused(text):
    m = re.search(r"refusing to update: (\d+) element\(s\) have been changed locally[^\n]*\n((?:\s{2,}\S[^\n]*\n)+)", text)
    if not m:
        return []
    out = []
    for ln in m.group(2).splitlines():
        f = ln.split(None, 1)
        if len(f) == 2 and not f[0].startswith("-"):
            out.append(f"{KIND.get(f[0], f[0].lower())} {f[1].strip()}: changed in this app; the update would overwrite it")
    return out


def _recipe(work, rid):
    """The evidence column of row rid in W/replacements.md, one line per hit (cells escape | as \\|)."""
    p = os.path.join(work, "replacements.md")
    for ln in (_rd(p) or "").splitlines():
        cells = [c.strip().replace("\\|", "|") for c in re.split(r"(?<!\\)\|", ln)]
        if len(cells) > 6 and cells[1] == rid:
            hits = [re.sub(r"^/.*?/ in ", "found in ", h.strip()) for h in re.split(r"; (?=\S)", cells[5]) if h.strip()]
            what = [f"replacements.md row {rid}: {cells[2]}"] + [h if len(h) <= 240 else h[:237] + "..." for h in hits[:6]]
            return {"what": what, "files": [_rel(work, p)]}
    return {"what": [], "files": []}


def _files(work, mod):
    """The file rows (theme, JavaScript, Java) of module mod in W/localedits.json."""
    try:
        rep = json.loads(_rd(os.path.join(work, "localedits.json")) or "[]")
    except ValueError:
        rep = []
    return [f"{f.get('path')}: {(f.get('change') or '').lower()} ({f.get('detail')})"
            for e in rep if isinstance(e, dict) and e.get("name") == mod for f in e.get("files") or []]


def _other(work, name, kind):
    r = re.match(r"R\d+(?= )", name)
    if r:
        return _recipe(work, r.group(0))
    if kind == "check" and name == "Release notes":
        p = os.path.join(work, "release-impact.out")
        what = [ln.strip() for ln in (_rd(p) or "").splitlines() if ln.strip()][:5]
        return {"what": what, "files": [_rel(work, p)] if what else []}
    if kind == "theme" and name.endswith(" themesource edits"):
        what = _files(work, name[:-len(" themesource edits")])
        return {"what": what, "files": [_rel(work, os.path.join(work, "localedits.json"))] if what else []}
    return None


def for_item(work, name, kind=None):
    work = os.path.abspath(work)
    other = _other(work, name, kind)
    if other is not None:
        return other
    app = (_rd(os.path.join(work, "state", "app-dir")) or "").strip()
    S = os.path.join(app, ".stepupdate") if app else ""
    what, files = [], []
    for p in sorted(glob.glob(os.path.join(S, f"step*-{name}.log"))) if S else []:
        t = _rd(p) or ""
        rows = _refused(t)
        m = re.search(r"(\d+) element\(s\) could not be read", t)
        if m:
            rows.append(f"{m.group(1)} elements of the module could not be read by mxcli, so nobody can show yet whether they were edited")
        if rows:
            what += rows
            files.append(_rel(work, p))
    for p in sorted(glob.glob(os.path.join(S, f"step*-{name}.idcheck"))) if S else []:
        t = _rd(p) or ""
        rows = []
        for ln in t.splitlines():
            r = re.match(r"RED\s+(\w+)\s+(\w+)\s+([\w.]+)", ln)
            if r:
                rows.append(f"{r.group(2)} {r.group(3)}: {r.group(1).lower()} by the new version, its data is lost")
            elif ln.startswith("warn MODULE_RECREATED"):   # the info form (element identities kept) is no data row
                rows.append("the new version replaces the module as a whole (all ids new), pages that use it are rewritten too")
        if rows:
            what += rows
            files.append(_rel(work, p))
    for p in sorted(glob.glob(os.path.join(S, f"step*-{name}.files"))) if S else []:
        t = _rd(p) or ""
        rows = [ln.strip() for ln in t.splitlines() if ln.startswith("FILES-") and not ln.startswith("FILES-SAME")]
        nf = re.search(r"FILES NOT COMPARED \(([^)]*)\)", t)
        if nf:
            rows.insert(0, f"its files could not be compared with the Marketplace version ({nf.group(1).split(';')[0]})")
        if rows:
            what += [re.sub(r"^FILES-\w+ \S+: ", "", r) for r in rows]
            files.append(_rel(work, p))
    le = _rd(os.path.join(work, "localedits.md")) or ""
    sec = re.search(rf"^## {re.escape(name)} [^\n]*\n((?:  [^\n]*\n)*)", le, re.M)
    if sec:
        rows = []
        for ln in sec.group(1).splitlines():
            r = re.match(r"\s+(\w+)\s+(ADDED|CHANGED|REMOVED)\s+(\w+)\s+([\w.]+)\s+(.*)", ln)
            if r:
                rows.append(f"{r.group(3)} {r.group(4)}: {r.group(2).lower()} by this app ({r.group(5).split(';')[0]})")
        known = {re.split(r"[ :]", w)[1].split(".")[-1] for w in what if len(re.split(r"[ :]", w)) > 1}
        rows = [r for r in rows if r.split(" ")[1].rstrip(":").split(".")[-1] not in known]
        if rows:
            what += rows
            files.append(_rel(work, os.path.join(work, "localedits.md")))
    rows = [r for r in _files(work, name) if r.split(":")[0] not in " ".join(what)]
    if rows:
        what += rows
        files.append(_rel(work, os.path.join(work, "localedits.json")))
    inv = json.loads(_rd(os.path.join(work, "apimock-inventory.json")) or "{}").get("endpoints", [])
    rows = [f"outside call {e['doc']} ({(e.get('method') or '').strip()} {e.get('template') or ''}".rstrip() + f"): "
            + ("a stand-in answers it in the test" if e.get("status") == "MOCKED" else "no stand-in yet, " + (e.get("why") or "not classified"))
            for e in inv if e.get("module") == name]
    if rows:
        what += rows
        files.append(_rel(work, os.path.join(work, "apimock-inventory.json")))
    for x in json.loads(_rd(os.path.join(work, "edit-routes.json")) or "[]"):
        if x.get("module") == name:
            what.insert(0, ("held for a person: " if x["route"] == "HOLD" else f"the pipeline updates it anyway ({x['route']}): ") + x["reason"])
            what[1:1] = [f"company brain (internal): {b['title']} ({b['path']})" for b in x.get("brain") or []]
            files.insert(0, _rel(work, os.path.join(work, "edit-routes.json")))
    return {"what": what, "files": files}


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--work", required=True)
    ap.add_argument("--kind")
    ap.add_argument("name")
    a = ap.parse_args()
    ev = for_item(a.work, a.name, a.kind)
    print("\n".join("- " + w for w in ev["what"]) or "(no evidence found)")
    print("files: " + ", ".join(ev["files"]))
    return 0 if ev["what"] else 1


if __name__ == "__main__":
    sys.exit(main())
