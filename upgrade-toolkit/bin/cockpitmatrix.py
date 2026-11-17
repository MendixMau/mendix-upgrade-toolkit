#!/usr/bin/env python3
"""cockpitmatrix.py: the matrix half of the upgrade cockpit page (called by cockpitpage.py, never run on its own).

One row per upgrade item, four stage columns (Triage, Plan, Upgrade, Test), a readiness strip, top tiles counted from the rows,
a proposed-solution box on every non-green cell, a "since you last looked" feed, and a side panel per stage and per cell.

It never decides. Every status, count and verdict is copied from a run file (gate-summary.md, PROPOSAL.md, heal.json, ...). A file that
is missing gives a grey "not yet", never a pass. Words for the owner come from one optional per-run file, work/cockpit-items.json
(schema in steps/report.md, "Cockpit page"); the generator merges it over the derived rows and chips.

  build(work, model) -> dict    rows, ready chips, tiles, feed, stage texts (embedded in the page as D.matrix)
  render(model, matrix) -> str  page content only (title, style, markup, script)
"""
import datetime, html, json, os, re

import cockpitpage as cp
import steps as stp

STAGES = ("triage", "plan", "upgrade", "test")
GROUPS = [("app", "App and platform"), ("setup", "How we prove it still works"), ("golive", "Go-live")]
STEP_GROUP = ("steps", "Steps of this run")   # added after "app" when work/steps.jsonl exists
STATUSES = ("ok", "wait", "bad", "none", "you")
LOOP = ("Found", "Proposed", "Trying", "Fixed")
V2S = {"PASS": "ok", "PASS*": "ok", "EXCEPT": "ok", "FAIL": "bad", "REVIEW": "wait", "INVALID": "wait"}
VWORD = {"PASS": "passed", "PASS*": "passed with accepted differences", "EXCEPT": "passed with an exception", "FAIL": "failed",
         "REVIEW": "needs a look", "INVALID": "not measured yet", "NOT RUN": "not run"}
STEP_PLAIN = {"fetch": "app unpacked", "triage": "triage", "baseline": "snapshot of the old app", "basewalk": "old app click-through",
              "propose": "plan written", "convert": "model converted", "update": "modules updated", "build": "build",
              "after": "new app started", "afterwalk": "new app click-through", "journeys": "journeys", "heal": "self-healing round",
              "diff": "old and new compared", "gate": "final checks"}
STEP_STAGE = {"fetch": "triage", "triage": "triage", "propose": "plan", "baseline": "upgrade", "convert": "upgrade", "update": "upgrade",
              "build": "upgrade"}
CHIPS = [("source", "App source and versions"), ("testdb", "Test database"), ("outside", "Outside systems"), ("login", "Login"),
         ("broker", "Brokers and messaging"), ("seed", "Seed data"), ("clicks", "Click paths"), ("unreadable", "Unreadable modules"),
         ("users", "Test users per role"), ("files", "Files and storage"), ("target", "Target environment"),
         ("backup", "Backup and way back")]


# ---- cells and rows ----
def cell(s, label, steps=None, tech=None, late=False, deploy=False, dec=None, d=""):
    """d: one short line under the label in the matrix (what was found or what the plan does), so a cell says more than its state."""
    return {"s": s, "l": label, "steps": list(steps or []), "tech": list(tech or []), "late": late, "deploy": deploy, "dec": dec, "d": d}


def notyet(what="No result file yet, so nothing is claimed."):
    return cell("none", "Not yet", [what])


def nowork(why="Nothing to do at this stage for this item."):
    return cell("none", "Not needed", [why])


def row(rid, name, sub, group, cells, tech=None, fix=None, regression=False, story=None):
    """story: {found, means, plan} lists of plain sentences, shown at the top of every drawer of the row (cold test WM1: a
    cell said "Found" or "Approved" and nobody could tell what was found or what the plan does about it)."""
    full = {k: cells.get(k) or nowork() for k in STAGES}
    return {"id": rid, "name": name, "sub": sub, "group": group, "cells": full, "tech": list(tech or []), "fix": fix,
            "regression": regression, "story": story or {}}


def fixd(problem="", proposal="", steps=None, loop=None, result="", help="", learn=""):
    return {"problem": problem, "proposal": proposal, "steps": list(steps or []), "loop": loop, "result": result, "help": help,
            "learn": learn}


def rungs_cell(g, names, labels=None):
    """One cell from gate rungs: statuses and words are the gate's own verdicts. No rung present: grey, not a pass."""
    rs = [r for n in names for r in g["rungs"] if r["rung"] == n]
    if not rs:
        return notyet("The final checks have not measured this yet.")
    st = [V2S.get(r["verdict"], "none") for r in rs]
    if "bad" in st:
        s = "bad"
    elif "wait" in st:
        s = "wait"
    elif "none" in st:
        s = "wait" if "ok" in st else "none"
    else:
        s = "ok"
    words = [VWORD.get(r["verdict"], "not run") for r in rs]
    if len(rs) == 1:
        label = words[0][:1].upper() + words[0][1:]
    elif s == "ok":
        acc = sum(1 for r in rs if r["verdict"] != "PASS")
        label = f"All {len(rs)} passed" + (f", {acc} with accepted differences" if acc else "")
    else:
        cnt = {}
        for w in words:
            cnt[w] = cnt.get(w, 0) + 1
        label = ", ".join(f"{n} {w}" for w, n in cnt.items())
        label = label[:1].upper() + label[1:]
    steps, tech = [], []
    for r in rs:
        nm = cp.RUNG_NAMES.get(r["rung"], r["rung"])
        if V2S.get(r["verdict"]) == "ok":
            steps.append(f"{nm}: {VWORD[r['verdict']]}.")
        else:
            steps.append(f"{nm}: {cp.gate_sentence(r, [], False, 0)}")
        tech.append(f"gate rung {r['rung']}: {r['verdict']} | " + re.sub(r"\b(PASS\*?|FAIL|INVALID|SKIPPED)\s+(\d+)", r"\1=\2", cp.short(r['detail'].replace(chr(92) + '|', '|'), 260)))
    return cell(s, label, steps, tech)


TRIAGE_FILES = ("findings.json", "release-impact.md", "localedits.json", "jarclash.md", "appshape.out")
PLAN_FILES = ("PROPOSAL.md", "DECISIONS.md", "NEEDS-JUDGMENT.md")


def _norm(s):
    return re.sub(r"[^a-z0-9]", "", str(s).lower())


def ad_text(work):
    return cp.rd(os.path.join(work, "AGENT-DECISIONS.md")) or cp.rd(os.path.join(os.path.dirname(os.path.abspath(work)), "AGENT-DECISIONS.md")) or ""


def ad_rows(work):
    """[(id, title, what, options, status)] from the agent decisions table."""
    out = []
    for ln in ad_text(work).splitlines():
        c = [x.strip() for x in ln.strip().strip("|").split("|")] if ln.startswith("|") else []
        m = re.match(r"^(D\d+[a-z]?)\b", c[0]) if c else None
        if m and len(c) >= 3:
            out.append((m.group(1), c[1], c[2], c[3] if len(c) > 3 else "", c[4] if len(c) > 4 else ""))
    return out


def seen_in(work, terms, files):
    ts = [x for x in (_norm(s) for s in terms) if len(x) >= 4]
    for f in files:
        txt = _norm(cp.rd(os.path.join(work, f)) or "")
        if txt and any(x in txt for x in ts):
            return f
    return None


def late_cells(work, terms):
    """Triage and plan cells for an item found late: what the run files say. The dashed Not flagged is only for an
    item no triage file mentions; an item triage saw is never called missed."""
    tf, pf = seen_in(work, terms, TRIAGE_FILES), seen_in(work, terms, PLAN_FILES)
    ts = [x for x in (_norm(s) for s in terms) if len(x) >= 4]
    ad = next((d for d in ad_rows(work) if any(x in _norm(" ".join(d[1:4])) for x in ts)), None)
    led = [l for l in (cp.rj(os.path.join(work, "decisions.json")) or []) if isinstance(l, dict) and any(x in _norm(l.get("item", "")) for x in ts)]
    tc = (cell("ok", "Seen in triage", ["Triage listed this item before the test."], [tf]) if tf
          else cell("none", "Not flagged", ["No triage file mentions this item."], late=True))
    if pf:
        pc = cell("ok", "In the plan", ["The plan or the questions file names this item."], [pf])
    elif led:
        pc = cell("ok", "Decided by you", [f"{led[-1].get('by', 'You')} answered this item."], ["decisions.json"])
    elif ad:
        pc = cell("ok" if "OPEN" not in ad[4] else "wait", "Decided during the run" if "OPEN" not in ad[4] else "Open, being worked",
                  [f"Recorded as {ad[0]}: {cp.short(ad[1], 90)}"], ["AGENT-DECISIONS.md " + ad[0]])
    elif tf:
        pc = cell("wait", "Not in the plan yet", ["Triage saw this item; the plan does not name it yet."])
    else:
        pc = cell("none", "Not flagged", ["The plan did not cover this item."], late=True)
    return tc, pc


def apis_cell(g, work):
    c = rungs_cell(g, ["apis"])
    r = next((x for x in g["rungs"] if x["rung"] == "apis"), None)
    if r and V2S.get(r["verdict"]) != "ok":
        m1, m2 = re.search(r"mocked (\d+)", r["detail"]), re.search(r"(\d+) MOCKED endpoints NOT EXERCISED", r["detail"])
        if m1 and m2:
            n, left = int(m1.group(1)), int(m2.group(1))
            c["s"] = "wait" if left else c["s"]
            c["l"] = f"{n - left} of {n} exercised"
            c["steps"] = [f"{n - left} of {n} stand-ins were called by the tests; {left} were not."] + c["steps"][1:]
            for d in ad_rows(work):
                m = re.search(r"requested: (\d+) before, (\d+) after", d[2])
                if m:
                    c["steps"].append(f"Last loop ({d[0]}): {m.group(1)} called before, {m.group(2)} after.")
    return c


def release_cell(g):
    c = rungs_cell(g, ["release"])
    r = next((x for x in g["rungs"] if x["rung"] == "release"), None)
    m = re.search(r"(\d+) of (\d+) rows handled or not relevant, (\d+) open", r["detail"]) if r else None
    if m and V2S.get(r["verdict"]) != "ok":
        c["s"] = "wait" if int(m.group(3)) else "ok"
        c["l"] = f"{m.group(1)} of {m.group(2)} handled, {m.group(3)} open"
        c["steps"] = [f"{m.group(1)} of {m.group(2)} release-note rows are handled or not relevant.", f"{m.group(3)} rows still need a person's answer."]
    return c


def worst(*cs):
    st = [c["s"] for c in cs]
    for s in ("bad", "wait", "you"):
        if s in st:
            return s
    return "ok" if "ok" in st else "none"


# ---- derivation ----
def derive(work, model):
    P = cp.parse_proposal(cp.rd(os.path.join(work, "PROPOSAL.md")))
    dm = cp.parse_decisions_md(cp.rd(os.path.join(work, "DECISIONS.md")))
    gtext = cp.rd(os.path.join(work, "gate-summary.md")) or ""
    g = cp.parse_gate(gtext)
    mo = re.search(r"open regression (\d+)", gtext)
    g["open_reg"] = int(mo.group(1)) if mo else None
    mh = re.search(r"(\d+) real-regression", gtext)
    g["stale_reg"] = (g["open_reg"] == 0) or (mh is not None and int(mh.group(1)) == 0)
    g["closed_q"] = []
    pending_j = []
    heal = cp.rj(os.path.join(work, "heal.json")) or {}
    inv = (cp.rj(os.path.join(work, "apimock-inventory.json")) or {})
    finds = (cp.rj(os.path.join(work, "findings.json")) or {}).get("findings", [])
    ledit = cp.rj(os.path.join(work, "localedits.json"))
    ledger = cp.rj(os.path.join(work, "decisions.json")) or []
    done = {s: bool(cp.rd(os.path.join(work, "state", s + ".done"))) for s in cp.STEP_ORDER}
    commits = cp.app_commits(work)
    per = cp.run_minutes(work)
    vm = re.search(r"(\d+(?:\.\d+)+) → (\d+(?:\.\d+)+)", model.get("sub", ""))
    src, tgt = (vm.group(1), vm.group(2)) if vm else ("", "")
    signed = P["signed"]
    rows = []

    def commit_rows(pred):
        return [(h, s) for h, s in commits if pred(s)]

    # Mendix runtime
    t = (cell("ok", "Version read", [f"The app runs on Mendix {src}.", f"Mendix {tgt} is the target."], [f"PROPOSAL.md title: {P['title']}"])
         if done["triage"] and src else notyet("Triage has not run yet."))
    p = (cell("ok", "Plan written", ["The plan lists the module updates and the choices that need a person.",
                                     f"Signed by {signed[0]}." if signed else "Not signed yet."], ["PROPOSAL.md"])
         if done["propose"] and P["present"] else
         cell("wait", "Planned, not approved", ["The plan is written. Nothing changes in the app before you approve it."], ["PROPOSAL.md"]) if P["present"]
         else notyet("No plan yet."))
    if done["convert"]:
        u = (cell("ok", "Converted, build clean", [f"The model was converted to Mendix {tgt}.", "The build finished with 0 errors."])
             if done["build"] and any(r["rung"] == "build" and r["verdict"].startswith("PASS") for r in g["rungs"])
             else cell("wait", "Converted, build open", [f"The model was converted to Mendix {tgt}.", "The build is not clean yet."]))
        u["tech"] = [f"{h} {s}" for h, s in commit_rows(lambda s: s.startswith("convert"))]
    else:
        u = notyet("The model has not been converted yet.")
    if src:
        t["d"] = f"{src} → {tgt}"
        p["d"] = p["d"] or "convert, then build"
    rows.append(row("runtime", "Mendix runtime", f"{src} → {tgt}" if src else "", "app",
                    {"triage": t, "plan": p, "upgrade": u, "test": rungs_cell(g, ["build", "data"])},
                    story={"found": [f"The app runs on Mendix {src}; the target is Mendix {tgt}."] if src else [],
                           "means": ["The whole app model is converted to the new version. Pages, microflows and Java code must still build after that."],
                           "plan": ["Convert the model with the new Studio Pro, then build it. Every repair after the build is its own Git commit."]}))

    # Marketplace modules
    planned = []
    for it in P["sec2"]:
        m = re.match(r"module update (\S+) (\S+) -> (\S+)", it["text"])
        if m:
            planned.append((m.group(1), m.group(2), m.group(3)))
    names = sorted({n for n, _, _ in planned})
    stepc = commit_rows(lambda s: s.startswith("step"))
    got = [n for n in names if any(n in s for _, s in stepc)]
    if P["present"]:
        t = cell("ok", f"{len(names)} to update" if names else "None to update",
                 [f"{n}: {a} to {b}." for n, a, b in planned] or ["No Marketplace module needs an update."], ["PROPOSAL.md section 2"])
        p = cell("ok", f"{len(planned)} steps planned" if planned else "Nothing planned", ["Each update is its own step, with a data identity check after it."]) if done["propose"] else \
            cell("wait", "Planned, not approved", ["Each update is its own step, with a data identity check after it.",
                                                   "Nothing changes in the app before you approve the plan."], ["PROPOSAL.md section 2"])
    else:
        t, p = notyet("Triage has not written a proposal yet."), notyet("No plan yet.")
    if names and got:
        u = cell("ok" if len(got) == len(names) else "wait", "Updated" if len(got) == len(names) else f"{len(got)} of {len(names)} updated",
                 [f"{n}: {'updated' if n in got else 'not updated yet'}." for n in names], [f"{h} {s}" for h, s in stepc])
    elif names:
        u = cell("none", "Not started", ["No update step has been committed yet."])
    else:
        u = nowork("No module needed an update.") if P["present"] else notyet()
    kept = [i["name"] for i in P["sec3"] if i.get("id") and "keep" in (i["sub"].get("recommendation", "") + i["sub"].get("answer", "")).lower()]
    arrow = [f"{n} {a} → {b}" for n, a, b in planned]
    if planned:
        t["d"] = cp.short(", ".join(n for n, _, _ in planned[:3]) + (f" +{len(planned) - 3}" if len(planned) > 3 else ""), 60)
        p["d"] = cp.short(arrow[0] + (f" +{len(arrow) - 1} more" if len(arrow) > 1 else ""), 60)
    rows.append(row("modules", "Marketplace modules", f"{len(names)} updates" if names else "", "app",
                    {"triage": t, "plan": p, "upgrade": u, "test": rungs_cell(g, ["const", "logdiff"])},
                    story={"found": [f"{len(planned)} Marketplace modules have a newer version for the target." if planned else "No Marketplace module needs an update."]
                                    + ([f"Kept at the old version: {', '.join(kept)} (see Our own edits in modules)."] if kept else []),
                           "means": ["An update replaces the module with the vendor's new version. That brings the fixes for the new Mendix version, "
                                     "and it overwrites anything the app changed inside the module."],
                           "plan": [f"Update: {x}." for x in arrow[:12]] + ([f"... and {len(arrow) - 12} more."] if len(arrow) > 12 else [])
                                   + ["Why: the old versions are not built for the new Mendix version. Each update is its own step, with a data check after it."]}))

    # Own edits in Marketplace modules
    if ledit is None:
        rows.append(row("localedits", "Our own edits in modules", "", "app", {"triage": notyet("The edit check has not run yet.")}))
    else:
        edited, unread = [], []
        for m in ledit:
            kinds = [(k, len(m[k])) for k in ("domain", "ui", "logic", "files") if m.get(k)]
            if m.get("domain_error") or m.get("files_error"):
                unread.append(m["name"])
            if kinds:
                edited.append((m["name"], kinds))
        sec3 = [i for i in P["sec3"] if i.get("id") and i.get("kind") != "check"]   # a check that did not run has its own row
        open_choices = [i for i in sec3 if not (any(l.get("item") == i["id"] for l in ledger)
                                                or "CONFIRMED" in ((dm.get(i["id"]) or [""] * 6)[5:6] or [""])[0])]
        t = (cell("wait", f"{len(edited)} modules with edits", [f"{n}: " + ", ".join(f"{k} {c}" for k, c in ks) + "." for n, ks in edited],
                  ["localedits.json"]) if edited else cell("ok", "No edits found", ["No module has edits that an update would undo."], ["localedits.json"]))
        if not P["present"]:
            p = notyet("No plan yet.")
        elif not sec3:
            p = cell("ok", "Nothing to decide", ["Every edit can be saved and put back by the update."])
        else:
            p = cell("wait" if open_choices else "ok", f"{len(sec3)} choice" + ("" if len(sec3) == 1 else "s") + (f", {len(open_choices)} assumed" if open_choices else ""),
                     [f"{i['name']}: {cp.short(i['sub'].get('recommendation', ''), 110)}" for i in sec3], ["PROPOSAL.md section 3", "DECISIONS.md"])
        rep = commit_rows(lambda s: s.startswith("replay"))
        u = (cell("ok", f"{len(rep)} edit sets put back", [cp.short(s.partition(": ")[2], 110) for _, s in rep], [f"{h} {s}" for h, s in rep]) if rep
             else (cell("none", "Not started", ["No edit has been put back yet."]) if edited else nowork("There were no edits to put back.")))
        KW = {"domain": "entities", "ui": "pages", "logic": "microflows", "files": "files"}
        said = [f"{n}: " + ", ".join(f"{c} {KW.get(k, k)}" for k, c in ks) for n, ks in edited]
        if said:
            t["d"] = cp.short(said[0] + (f" +{len(said) - 1}" if len(said) > 1 else ""), 60)
        acts = [f"{i['name']}: " + re.sub(r"\s*\((?:DECIDED|CONFIRMED|ASSUMED)[^)]*\)\)?", "", plain(i['sub'].get('answer') or i['sub'].get('recommendation', '')).split(';')[0]) for i in sec3 if "check" not in i.get("kind", "")]
        if sec3 and acts:
            p["d"] = cp.short(acts[0], 60)
        rows.append(row("localedits", "Our own edits in modules", f"{len(edited)} modules", "app",
                        {"triage": t, "plan": p, "upgrade": u, "test": rungs_cell(g, ["idcheck"])},
                        story={"found": [f"The app changed {len(edited)} Marketplace modules itself." if edited else "No module has edits of its own."]
                                        + [x + "." for x in said[:6]],
                               "means": ["A Marketplace update overwrites the whole module. Edits the toolkit can save are put back after the update; "
                                         "edits it cannot put back (new entities hold data) need a choice."],
                               "plan": [x + "." for x in acts] or ["The toolkit saves each edit and puts it back after the update."]}))

    # Java libraries
    jc = cp.rd(os.path.join(work, "jarclash.md"))
    if jc is None:   # before the build only triage's own scan exists (cold test WM1: the cell said "Not yet" after triage scanned)
        jc = cp.rd(os.path.join(work, "jarclash-before.md"))
    jf = re.search(r"summary: (\d+) Java actions scanned, (\d+) assignments", cp.rd(os.path.join(work, "javafinal.md")) or "")
    if jc is None:
        t = notyet("The library check has not run yet.")
        nclash = None
    else:
        nclash = len(re.findall(r"^CLASH ", jc, re.M))
        libs = sorted({m.split(".")[1] if m.count(".") > 1 else m for m in re.findall(r"^CLASH \d+ classes in \d+ packages \(([\w.]+)", jc, re.M)})
        t = cell("ok", f"{nclash} libraries twice" if nclash else "No clashes",
                 ([f"{nclash} sets of classes are in two jar files ({', '.join(libs[:4])}). The upgrade keeps one copy of each."] if nclash else ["No library is present twice."])
                 + ([f"{jf.group(1)} Java actions scanned: {'no' if jf.group(2) == '0' else jf.group(2)} code that breaks on the new Java."] if jf else []),
                 ["jarclash.md" if os.path.exists(os.path.join(work, "jarclash.md")) else "jarclash-before.md"] + (["javafinal.md"] if jf else []))
    fixc = commit_rows(lambda s: re.search(r"jardedupe|java dependencies", s))
    u = (cell("ok", "Settled", ["One copy of each library is kept."], [f"{h} {s}" for h, s in fixc]) if fixc
         else (cell("wait", "Not settled", ["The duplicate libraries are not removed yet."]) if nclash else nowork() if jc is not None else notyet()))
    if nclash:
        t["d"] = cp.short(", ".join(libs[:3]) + " in two jars", 60)
    elif jf:
        t["d"] = f"{jf.group(1)} Java actions scanned"
    jp = cell("ok", "Keep one copy", ["The build step removes the second copy of each library."], d="remove the duplicate jars") if nclash else None
    rows.append(row("java", "Java libraries", f"{nclash} duplicates" if nclash else "", "app",
                    {"triage": t, "upgrade": u, "test": rungs_cell(g, ["build"]), **({"plan": jp} if jp else {})},
                    story={"found": t["steps"] if jc is not None else [],
                           "means": (["Two copies of the same classes can make the app load the wrong one after the upgrade, and fail at run time."] if nclash else [])
                                    + (["The app's own Java code uses nothing the new Java version removes."] if jf and jf.group(2) == "0" else []),
                           "plan": ["Keep one copy of each library (the newest), then build. The build proves the choice."] if nclash else
                                   ["Nothing to change; the build checks it again."] if jc is not None else []}))

    # Findings from the Mendix 11 catalog
    if not finds and not os.path.exists(os.path.join(work, "findings.json")) and tgt.startswith("10."):
        later = cell("none", "At the 10 → 11 step", ["The Mendix 11 catalog is checked when the run upgrades from Mendix 10 to 11, after this step."],
                     d="checked after Mendix 10")
        rows.append(row("findings", "Mendix 11 findings", "", "app", {"triage": later},
                        story={"found": ["Not checked yet: this step goes to Mendix 10."], "means": ["Mendix 11 changes are checked on the Mendix 10 model."],
                               "plan": ["The second step (10 → 11) scans the app with the Mendix 11 catalog and plans the fixes."]}))
    elif not finds and not os.path.exists(os.path.join(work, "findings.json")):
        rows.append(row("findings", "Mendix 11 findings", "", "app", {"triage": notyet("The scan has not run yet.")}))
    else:
        sev = {}
        for f in finds:
            sev.setdefault(f.get("severity"), {}).setdefault(f.get("catalog_id"), []).append(f)
        nb = sum(len(v) for v in sev.get("blocker", {}).values())
        top = [(s, cid, len(fl)) for s in ("blocker", "high") for cid, fl in sorted(sev.get(s, {}).items(), key=lambda kv: -len(kv[1]))]
        t = cell("ok", f"{len(finds)} findings" + (f", {nb} blocking" if nb else ""),
                 [f"{n} × {cid.replace('MX11-', '').replace('-', ' ').lower()} ({s})." for s, cid, n in top[:8]] or ["No blocking finding."], ["findings.json"])
        repairs = commit_rows(lambda s: not re.match(r"(step|convert|build|original|replay)", s))
        u = (cell("ok", f"{len(repairs)} fixes applied", [cp.short(re.sub(r"^\w+( D\d+\w*)?: ", "", s), 120) for _, s in repairs[:8]],
                  [f"{h} {s}" for h, s in repairs]) if repairs else nowork("No separate fix was committed."))
        if repairs:
            u["n"] = len(repairs)
        rows.append(row("findings", "Mendix 11 findings", f"{len(finds)} found", "app",
                        {"triage": t, "plan": cell("ok", "In the plan", ["Findings feed the plan sections."], ["PROPOSAL.md"]) if done["propose"] else notyet("No plan yet."),
                         "upgrade": u, "test": rungs_cell(g, ["smoke", "screens"])}))

    # Real regressions and open decisions, one row each, from the decision list
    stage_of = {"regression": "test", "signoff": "plan", "confirmgroup": "upgrade"}
    for it in model.get("items", []):
        if it.get("hidden"):
            continue
        k = it["kind"]
        stg = stage_of.get(k) or STEP_STAGE.get(it.get("step", ""), "test")
        isopen = not (it.get("decided") and k != "signoff") and bool(it.get("open", 1))
        if k == "judgment":
            rg = [r for r in g["rungs"] if r["rung"] == it.get("step")]
            shut = (V2S.get(rg[0]["verdict"]) == "ok") if rg else bool(g.get("stale_reg"))
            if shut:
                g["closed_q"].append(it["title"])
            elif isopen:
                pending_j.append(it)
            continue
        closed_by_gate = (g.get("stale_reg") and stg == "test" and k == "regression")
        kids_ = it.get("children") or []
        if closed_by_gate:
            c = cell("ok", "Fixed, passes on the latest gate", ["The latest gate reports no open regression, so the earlier question is closed."],
                     list(it.get("tech") or []))
        elif isopen:
            c = cell("you", "Needs your decision", [it["problem"]], list(it.get("tech") or []), dec=it["id"])
        else:
            c = cell("wait", "You decided, waiting for the pipeline", ["Your answer is recorded; the next step applies it."], dec=it["id"])
        if k == "regression" and not closed_by_gate:
            c["l"] = "Fails on the new app, you decide" if isopen else "Fails on the new app"
        if k == "confirmgroup" and kids_:
            nopen_ = int(it.get("open") or 0)
            c["l"] = f"{nopen_} of {len(kids_)} to confirm" if isopen else f"All {len(kids_)} confirmed"
            c["s"] = "you" if isopen else "wait"
        name = {"signoff": "Plan sign-off", "confirmgroup": "Changes the agent made"}.get(k, cp.short(it["title"], 70))
        if isopen and not closed_by_gate:
            c["steps"] = ([it["problem"]] if k == "regression" else []) + ["Pick one option in the decision box below.", "The pipeline applies your answer at its next step."]
        cells_ = {stg: c}
        if k in ("regression", "judgment") and stg == "test":
            cells_["triage"], cells_["plan"] = late_cells(work, [it["id"].split(":", 1)[-1]])
        rows.append(row(it["id"], name, it.get("meta", ""), "golive" if k == "signoff" else "app", cells_,
                        tech=[it["id"]] + list(it.get("tech") or [])[:6], regression=(k == "regression" and not closed_by_gate)))
    if P["present"] and signed:
        rows.append(row("signoff", "Plan sign-off", "", "golive", {"plan": cell("ok", f"Signed by {signed[0]}", [f"Signed on {signed[1]}."])}))

    # Outside systems
    eps = inv.get("endpoints", [])
    if not eps:
        rows.append(row("outside", "Outside systems", "", "setup", {"triage": notyet("No outside call list yet.")}))
    else:
        mocked = [e for e in eps if e.get("status") == "MOCKED"]
        unk = [e for e in eps if e.get("status") == "UNKNOWN"]
        t = cell("wait" if unk else "ok", f"{len(eps)} calls found" + (f", {len(unk)} unclear" if unk else ""),
                 [f"The app makes {len(eps)} outside calls.", f"{len(mocked)} can be answered by a stand-in.",
                  f"{len(unk)} get their address from data or are not classified." if unk else "All are classified."], ["apimock-inventory.json"])
        p = cell("ok" if mocked else "none", f"{len(mocked)} stand-ins" if mocked else "No stand-ins", ["Build a stand-in per call.", "Check the real systems before go-live."])
        t["d"] = f"{len(unk)} of {len(eps)} unclear" if unk else f"{len(eps)} calls"
        p["d"] = f"{len(mocked)} answered by stand-ins" if mocked else ""
        rows.append(row("outside", "Outside systems", f"{len(eps)} calls", "setup",
                        {"triage": t, "plan": p, "upgrade": nowork("Stand-ins are test side only; the app is unchanged."), "test": apis_cell(g, work)},
                        story={"found": t["steps"],
                               "means": ["The test must not call real outside systems. A call with no stand-in is not tested."],
                               "plan": [f"Answer {len(mocked)} calls with a stand-in during the test.",
                                        f"The other {len(eps) - len(mocked)} are checked on the real test systems by a person before go-live."]}))

    # Release notes
    ri = cp.rd(os.path.join(work, "release-impact.md"))
    rq = next((i for i in model.get("items", []) if i.get("title", "").startswith("Release notes") and i["kind"] == "plan-choice"), None)
    if ri is None and rq:
        why = "the company brain's version tables are not on this machine" if "version tables" in (rq.get("problem") or "") else "see the technical details"
        t = cell("bad", "Did not run", [f"The release-note check did not run: {why}.", "So nobody has checked what the new Mendix versions change for this app."],
                 [rq.get("problem") or "", "release-impact.out"], d="version tables missing")
        p = (cell("wait", "You decided, waiting for the pipeline", ["Your answer is recorded; the next step applies it."], dec=rq["id"]) if rq.get("decided")
             else cell("you", "Needs your decision", [rq.get("problem") or ""], dec=rq["id"], d="run it first, or go on without it"))
        rows.append(row("release", "Release notes", "check did not run", "app", {"triage": t, "plan": p},
                        story={"found": t["steps"][:1],
                               "means": ["A change in Mendix 10 or 11 that hits this app is found only at the build or the test, or after go-live."],
                               "plan": ["Recommended: give the run the company brain and rerun triage, so the plan covers the release notes.",
                                        "Or a named person reads the release notes for every version before go-live."]}))
    elif ri is None:
        rows.append(row("release", "Release notes", "", "app", {"triage": notyet("The release-note check has not run yet.")}))
    else:
        n = len([r for r in ri.splitlines() if re.match(r"^\| \d+ \|", r)])
        mm = re.search(r"This run: (\d+) auto, \d+ kept from a person, (\d+) open", ri)
        t = cell("ok", f"{n} rows listed", [f"{n} release-note rows were checked against the app."], ["release-impact.md"])
        p = (cell("ok", f"{mm.group(1)} handled automatically", [f"{mm.group(1)} rows are handled automatically.", f"{mm.group(2)} rows need a person's answer."]) if mm else notyet())
        rows.append(row("release", "Release notes", f"{n} rows", "app",
                        {"triage": t, "plan": p, "upgrade": nowork("Release notes are read, not applied."), "test": release_cell(g)}))

    # How we prove it still works: one row per kind of app part in test-inventory.md, with the gate rungs that measure it
    # (cold test WM1: 13 kinds of test sat in test-inventory.md and the matrix showed one row, "Click paths: Not needed")
    inv = {}
    for line in (cp.rd(os.path.join(work, "test-inventory.md")) or "").splitlines():
        c = [x.strip() for x in line.strip().strip("|").split("|")]
        if len(c) >= 4 and c[0] not in ("app part", "---"):
            inv[c[0]] = c
    js = cp.rd(os.path.join(work, "journey-scope.md")) or ""
    jb = cp.rd(os.path.join(work, "journeys-base.out")) or ""
    jo = cp.rd(os.path.join(work, "journeys.out")) or ""
    scope = re.search(r"journeys in scope: (\d+) reachable", js)
    nopath = re.search(r"(\d+) reachable actions have no click path", js)
    jbase = re.search(r"(\d+) journeys .*?(\d+) pass on baseline", jb)
    cov = re.search(r"coverage (\d+)/(\d+) \((\d+)%\)", jo)
    shots = len(os.listdir(os.path.join(work, "smoke-before-shots"))) if os.path.isdir(os.path.join(work, "smoke-before-shots")) else 0
    # (inventory key, row name, what we prove, how in plain words, gate rungs)
    TESTS = [("Persistent entities", "Data survives", "every table keeps its rows and values",
              "Count the rows and checksum every column of every table on a copy of the database, before and after.", ["data"]),
             ("Role home pages and menu", "Pages per role", "every role still lands on its home page and opens its menu",
              "Log in as each role, open the home page and every menu item, and compare the screens before and after.", ["smoke", "screens"]),
             (None, "Buttons and journeys", "the buttons and flows people use still work",
              "Click every reachable button and run the recorded journeys, on the old app first and then on the new one.", ["journeys"]),
             ("Published REST operations", "Published APIs", "other systems can still call this app",
              "Compare the API contract before and after, and call every safe read operation once.", ["apis"]),
             ("Scheduled events", "Scheduled jobs", "the background jobs still run on the same schedule",
              "Compare each job's schedule and on/off state before and after; trigger it once in the test.", []),
             ("Pluggable widgets", "Widgets", "every widget still renders",
              "Open each page that uses the widget, check for errors and compare the screen before and after.", ["smoke", "screens"]),
             ("Java actions", "Java code", "the app's own Java still compiles and runs",
              "The build proves it compiles; the journeys that use it prove it runs.", ["build"])]
    for key, name, what, how, rungs in TESTS:
        if key is None:
            if not (scope or jbase or cov):   # nothing measured yet: the row stays, grey (a missing file is never a pass)
                rows.append(row("t-buttons-and-journeys", name, "", "setup", {"test": rungs_cell(g, rungs)}))
                continue
            found = (f"{scope.group(1)} buttons in reach of a user" if scope else "") + (f"; {nopath.group(1)} have no click path yet" if nopath else "")
            auto = True
            sub = f"{scope.group(1)} buttons" if scope else ""
            pl = [how] + ([f"{jbase.group(2)} of {jbase.group(1)} journeys already pass on the old app."] if jbase else []) \
                 + ([f"{nopath.group(1)} buttons only show up with the right data; the test reaches them through their flow or a person checks them."] if nopath else [])
        else:
            c = inv.get(key)
            if not c or re.match(r"^0\b", c[1]):
                continue
            found, sub = c[1], c[1].split(" (")[0]
            auto = c[3].startswith("auto")
            pl = [how] + ([] if auto else [f"Part of it needs a person: {c[3]}."])
            if key == "Role home pages and menu" and shots:
                pl.append(f"{shots} screens of the old app are already taken as the reference.")
        t = cell("ok", "Found", [f"Found: {found}."], ["test-inventory.md"], d=found[:60])
        p = cell("ok" if auto else "wait", "Automatic" if auto else "Partly by a person", pl, d=how.split(",")[0][:60])
        ct = rungs_cell(g, rungs) if rungs else notyet("No automatic check measures this yet.")
        if name == "Buttons and journeys" and cov and ct["s"] != "none":
            ct["l"] = f"{cov.group(3)}% of buttons reached"
            ct["steps"].insert(0, f"{cov.group(1)} of {cov.group(2)} buttons have a test that clicks them.")
        rows.append(row("t-" + re.sub(r"\W+", "-", name.lower()), name, sub, "setup",
                        {"triage": t, "plan": p, "upgrade": nowork("Tests do not change the app."), "test": ct},
                        story={"found": [f"Found: {found}."], "means": [f"The test has to prove that {what}."], "plan": pl}))

    # Test repairs (self-healing)
    hr = heal.get("rows", [])
    if hr:
        by = {}
        for r in hr:
            by.setdefault(r.get("class"), []).append(r)
        opn = sum(1 for c, rs in by.items() if c != "real-regression" for r in rs if not str(r.get("result", "")).startswith("accepted"))
        steps = [f"{cp.CLASS_TEXT.get(c, (c, ''))[0]}: {len(rs)}. {cp.CLASS_TEXT.get(c, ('', ''))[1]}".strip() for c, rs in by.items() if c != "real-regression"]
        c = cell("wait" if opn else "ok", f"{opn} test rows open" if opn else "All test rows settled", steps, ["heal.json", "heal.md"])
        fx = (fixd(problem=f"{opn} test rows fail for reasons in the test, not in the app.", proposal="The agent repairs the test, never the app, and reruns it.",
                   loop=2, result=f"{opn} rows still open.", help="Nothing needed.") if opn else
              fixd(problem="Some test rows failed for reasons in the test.", proposal="The agent repaired the test and reran it.", loop=3,
                   result="All test rows are settled.", help="Nothing needed."))
        rows.append(row("heal", "Test repairs", f"{len(hr)} rows looked at", "setup", {"test": c}, fix=fx))
    # the gate counts an open regression that no heal row names: take it from an open REGRESSION line of the agent decisions
    nopen = sum(1 for r in rows if r["regression"])
    if g.get("open_reg") and g["open_reg"] > nopen:
        for did, title, what, opts, status in ad_rows(work):
            if "REGRESSION" in title.upper() and "OPEN" in status and nopen < g["open_reg"]:
                nm = re.sub(r"^[A-Z ]*REGRESSION:\s*", "", title, flags=re.I) or title
                terms = re.findall(r"[A-Z]{3,}[A-Za-z]*", nm)
                tc, pc = late_cells(work, terms + [nm])
                rw = row("regression:" + did, cp.short(nm, 60), "Real regression, " + did, "app",
                         {"triage": tc, "plan": pc, "upgrade": nowork(), "test": cell("bad", "Fails on the new app", [cp.short(what, 220), "The agent is isolating the cause; no decision is needed from you yet."], [did])},
                         tech=[did], regression=True,
                         fix=fixd(problem=cp.short(what, 400), proposal=cp.short(opts, 400), loop=1, result="Open, not fixed yet.",
                                  steps=[s.strip() for s in re.split(r"Option \d+:", opts) if s.strip()][:4]))
                rows.append(rw)
                nopen += 1
    # an open ledger question shows as a purple cell on the item it belongs to, never as its own row
    home = {"journeys": "t-buttons-and-journeys", "apis": "outside", "release": "release", "smoke": "findings", "screens": "findings"}
    for it in pending_j:
        tgt = next((r for r in rows if r["id"] == home.get(it.get("step"), "findings")), None) or rows[0]
        c = tgt["cells"]["test"]
        if c.get("s") == "you" and c.get("dec", "").startswith("stop:") and it["id"].startswith("stop:"):
            # several sections of one judgment stop on one row: list them all (the first one kept only its own title)
            n = c.get("nstop", 1) + 1
            c.update(nstop=n, l=f"{n} decisions needed", steps=c["steps"] + [it["title"]])
            continue
        was = c["l"]
        c.update(s="you", l="Needs your decision", dec=it["id"], steps=[it["title"], it["problem"], f"Before: {was}."][:3] if it["problem"] else [it["title"]])
    return rows, ready_chips(work, P, g, heal, inv, ledit, done), P, g, done, per, ledger


def ready_chips(work, P, g, heal, inv, ledit, done):
    def exists(n):
        return os.path.exists(os.path.join(work, n))
    out = {}
    out["source"] = ("ok", "App source and versions") if (done["fetch"] and exists("appshape.out")) else ("none", "App source and versions: not checked")
    dr = next((r for r in g["rungs"] if r["rung"] == "data"), None)
    out["testdb"] = (("ok" if dr and V2S.get(dr["verdict"]) == "ok" else "wait"), "Test database") if done["baseline"] else ("none", "Test database: not checked")
    eps = inv.get("endpoints", [])
    ar = next((r for r in g["rungs"] if r["rung"] == "apis"), None)
    if eps:
        nm = sum(1 for e in eps if e.get("status") == "MOCKED")
        out["outside"] = (V2S.get(ar["verdict"], "wait") if ar else "wait", f"Outside systems: {nm} stand-ins")
    else:
        out["outside"] = ("none", "Outside systems: not checked")
    ex = re.search(r"excluded (\d+) \(([^)]*)\)", ar["detail"]) if ar else None
    if inv.get("excludes") or ex:
        out["login"] = ("wait", "Login: excluded")
    elif exists("login-path.txt"):
        out["login"] = ("ok", "Login path known")
    else:
        out["login"] = ("none", "Login: not checked")
    out["broker"] = ("none", "Brokers and messaging: not checked")
    nodata = [r for r in heal.get("rows", []) if r.get("class") == "no-test-data"]
    out["seed"] = (("wait", f"Seed data: {len(nodata)} rows empty") if nodata else ("none", "Seed data: not checked"))
    jo = cp.rd(os.path.join(work, "journeys.out")) or ""
    cov = re.search(r"coverage \d+/\d+ \((\d+)%\)", jo)
    jr = next((r for r in g["rungs"] if r["rung"] == "journeys"), None)
    out["clicks"] = ((V2S.get(jr["verdict"], "wait") if jr else "wait"), f"Click paths: {cov.group(1)}%") if cov else ("none", "Click paths: not checked")
    if ledit is None:
        out["unreadable"] = ("none", "Unreadable modules: not checked")
    else:
        n = sum(1 for m in ledit if m.get("domain_error") or m.get("files_error"))
        out["unreadable"] = (("wait", f"{n} {'module' if n == 1 else 'modules'} unreadable") if n else ("ok", "All modules readable"))
    us = cp.rj(os.path.join(work, "users.json"))
    out["users"] = (("ok", f"Test users: {len(us)} roles") if isinstance(us, dict) and us else ("none", "Test users per role: not checked"))
    for k, label in (("files", "Files and storage"), ("target", "Target environment"), ("backup", "Backup and way back")):
        out[k] = ("none", f"{label}: not checked")
    return [{"id": k, "name": n, "s": out[k][0], "l": out[k][1], "fix": None, "row": None, "tech": []} for k, n in CHIPS]


# ---- items file ----
def loopnum(v):
    if isinstance(v, int) and 0 <= v <= 3:
        return v
    if isinstance(v, str) and v.strip().capitalize() in LOOP:
        return LOOP.index(v.strip().capitalize())
    return None


def apply_fix(target, ov):
    f = dict(target.get("fix") or fixd())
    for k in ("problem", "proposal", "result", "help", "learn"):
        if isinstance(ov.get(k), str):
            f[k] = ov[k]
    if isinstance(ov.get("steps"), list):
        f["steps"] = [str(x) for x in ov["steps"]]
    if loopnum(ov.get("loop")) is not None:
        f["loop"] = loopnum(ov["loop"])
    if any(k in ov for k in ("problem", "proposal", "steps", "result", "help", "learn", "loop")):
        target["fix"] = f


KINDS = ("upgrade", "testgap", "owner", "golive")
OWNER_IDS = ("release", "signoff")


def default_kind(x, row_kind=None):
    """upgrade | testgap | owner | golive. Rows: release and sign-off, then golive group, then setup, then a row whose only
    non-green cell is a you cell; the rest is upgrade. A chip with a row follows that row, a chip without one is a testing gap."""
    if "cells" not in x:
        return row_kind or "testgap"
    if x["id"] in OWNER_IDS:
        return "owner"
    if x["group"] == "golive":
        return "golive"
    if x["group"] == "setup":
        return "testgap"
    bad = [c["s"] for c in x["cells"].values() if c["s"] not in ("ok", "none")]
    if bad and all(s == "you" for s in bad):
        return "owner"
    return "upgrade"


def assign_kinds(rows, chips):
    for r in rows:
        if r.get("kind") not in KINDS:
            r["kind"] = default_kind(r)
    byid = {r["id"]: r for r in rows}
    for c in chips:
        if c.get("kind") not in KINDS:
            c["kind"] = default_kind(c, byid[c["row"]]["kind"] if c.get("row") in byid else None)


def merge_items(rows, chips, items, work=""):
    byid = {r["id"]: r for r in rows}
    derived = list(rows)
    declared = []
    for rid, ov in (items.get("items") or {}).items():
        if not isinstance(ov, dict):
            continue
        key = ov.get("key") or ov.get("matches")
        r = byid.get(key if isinstance(key, str) and key in byid else rid)
        if r is None:
            r = row(rid, ov.get("name") or rid, "", ov.get("group") if ov.get("group") in dict(GROUPS) else "app",
                    {k: notyet("Not checked yet.") for k in STAGES})
            rows.append(r)
            byid[rid] = r
        declared.append(r)
        for k in ("name", "sub"):
            if isinstance(ov.get(k), str):
                r[k] = ov[k]
        if ov.get("group") in dict(GROUPS):
            r["group"] = ov["group"]
        if ov.get("kind") in KINDS:
            r["kind"] = ov["kind"]
        for stg, co in (ov.get("cells") or {}).items():
            if stg not in STAGES or not isinstance(co, dict):
                continue
            c = r["cells"][stg]
            if co.get("status") in STATUSES:
                c["s"] = co["status"]
                if not isinstance(co.get("steps"), list):
                    c["steps"] = []
            if isinstance(co.get("label"), str):
                c["l"] = co["label"]
            if isinstance(co.get("steps"), list):
                c["steps"] = [str(x) for x in co["steps"]]
            for k in ("late", "deploy"):
                if k in co:
                    c[k] = bool(co[k])
        if isinstance(ov.get("decisions"), list):
            byad = {d[0]: d for d in ad_rows(work)}
            seen_d = [byad[x] for x in ov["decisions"] if x in byad]
            for d in seen_d[-2:]:
                r["cells"]["test"]["steps"].append(f"Latest, {d[0]}: {cp.short(d[1], 110)}")
                r["cells"]["test"]["tech"].append("AGENT-DECISIONS.md " + d[0])
        if ov.get("triage_missed"):
            key = ov.get("key") or ov.get("matches") or rid
            terms = [str(key).split(":", 1)[-1], rid.split(":", 1)[-1]] + [str(x) for x in (ov.get("seen_as") or [])]
            tc, pc = late_cells(work, terms)
            for stg, nc in (("triage", tc), ("plan", pc)):
                c = r["cells"][stg]
                if c["s"] == "none" and c["l"] in ("Not needed", "Not yet", "Not flagged") and not (isinstance(ov.get("cells"), dict) and stg in ov["cells"]):
                    r["cells"][stg] = nc
        apply_fix(r, ov)
    for cid, ov in (items.get("ready") or {}).items():
        ch = next((c for c in chips if c["id"] == cid), None)
        if ch is None or not isinstance(ov, dict):
            continue
        if ov.get("status") in STATUSES:
            ch["s"] = ov["status"]
        if isinstance(ov.get("label"), str):
            ch["l"] = ov["label"]
        if ov.get("kind") in KINDS:
            ch["kind"] = ov["kind"]
        if isinstance(ov.get("row"), str) and ov["row"] in byid:
            ch["row"] = ov["row"]
        apply_fix(ch, ov)
    # new rows keep the declared order: each goes right after the row declared before it
    rows[:] = derived
    prev = None
    for r in declared:
        if r not in derived:
            at = rows.index(prev) + 1 if prev is not None and prev["group"] == r["group"] else None
            if at is None:
                last = [i for i, x in enumerate(rows) if x["group"] == r["group"]]
                at = last[-1] + 1 if last else len(rows)
            rows.insert(at, r)
        prev = r
    order = {k: i for i, (k, _) in enumerate(GROUPS)}
    rows.sort(key=lambda r: order[r["group"]])


# ---- tiles, feed, stage texts ----
def tiles(rows, chips, open_reg=None):
    up = [r for r in rows if r["group"] != "golive" and r["cells"]["upgrade"]["s"] != "none"]
    t = [r for r in rows if r["cells"]["test"]["s"] != "none"]
    tested = sum(1 for r in t if r["cells"]["test"]["s"] == "ok")
    deploy = sum(1 for r in t if r["cells"]["test"]["s"] != "ok" and r["cells"]["test"]["deploy"])
    assign_kinds(rows, chips)
    units = [x for x in rows if x["fix"] or any(c["s"] in ("wait", "bad", "you") for c in x["cells"].values())]
    units += [c for c in chips if not c["row"] and (c["fix"] or c["s"] in ("wait", "bad", "you"))]

    def done(x):
        if x["fix"] and x["fix"]["loop"] == 3:
            return True
        return all(c["s"] == "ok" for c in x["cells"].values()) if "cells" in x else x["s"] == "ok"

    def per(k):
        u = [x for x in units if x["kind"] == k]
        return [sum(1 for x in u if done(x)), len(u)]
    measured = bool(any(r["id"] == "heal" or r["regression"] for r in rows)) or any(r["cells"]["test"]["s"] != "none" for r in rows if r["id"] == "t-buttons-and-journeys")
    return {"up": [sum(1 for r in up if r["cells"]["upgrade"]["s"] == "ok"), len(up)],
            "reg": open_reg if open_reg is not None else (sum(1 for r in rows if r["regression"]) if measured else None),
            "upg": per("upgrade"), "gap": per("testgap"), "own": per("owner")[1], "gol": per("golive")[1],
            "tested": [tested, deploy, len(t) - tested - deploy],
            "you": sum(1 for r in rows for c in r["cells"].values() if c["s"] == "you")}


def parse_iso(t):
    try:
        return datetime.datetime.strptime(t.strip(), "%Y-%m-%dT%H:%M:%SZ")
    except (ValueError, AttributeError):
        return None


def feed(work, model, ledger, items, closed=()):
    ev = []
    for s in cp.STEP_ORDER:
        d = parse_iso(cp.rd(os.path.join(work, "state", s + ".done")) or "")
        if d:
            ev.append((d, f"Step finished: {STEP_PLAIN.get(s, s)}."))
    title = {i["id"]: i["title"] for i in model.get("items", [])}
    for l in ledger:
        d = parse_iso(l.get("at", ""))
        if d:
            ev.append((d, f"{l.get('by', 'Someone')} answered: {cp.short(title.get(l.get('item'), 'a decision'), 80)}."))
    gm = os.path.join(work, "gate-summary.md")
    if closed and os.path.exists(gm):
        gd = datetime.datetime.fromtimestamp(os.path.getmtime(gm), datetime.timezone.utc).replace(tzinfo=None)
        for q in closed:
            ev.append((gd, f"Question closed by the latest gate: {cp.short(q, 80)}"))
    for f in (items.get("feed") or []):
        d = parse_iso(str(f.get("time", ""))) if isinstance(f, dict) else None
        if d and isinstance(f.get("text"), str):
            ev.append((d, f["text"]))
    ev.sort(key=lambda x: x[0], reverse=True)
    return [{"t": d.strftime("%Y-%m-%dT%H:%M:%SZ"), "text": x} for d, x in ev[:8]]


def stage_texts(rl, per):
    def run(steps, txt):
        v = sum(per[s] for s in steps if s in per)
        return txt + (f" It took about {cp.dur(v)} here." if v else "")
    return [
        {"key": "triage", "n": "1", "name": "Triage", "sub": "what changes · can we test it",
         "what": "We read the app without changing it. We list everything the upgrade touches, and check whether we can test each part.",
         "steps": ["Unpack the app and read its version, modules and widgets.", "Compare every module and widget with what the new Mendix version supports.",
                   f"Read the {rl or 'release-note'} release-note rows and mark which ones touch this app.",
                   "List outside systems, login, messaging and data, and check which ones we can reach.",
                   "Turn every gap into a row with a status, so nothing is a surprise later."],
         "run": run(("fetch", "triage"), "Runs on its own. Nothing in the app changes."), "you": "Nothing, unless an item needs a choice only you can make."},
        {"key": "plan", "n": "2", "name": "Plan", "sub": "what we do · how we test",
         "what": "For every row we choose a fix and a way to test it. Routine fixes are assumed. Only fixes with a big impact on the app come to you.",
         "steps": ["Pick a fix per row: upgrade, replace, keep or remove.", "Pick a test per row: build check, data compare, screen compare, click-through journey, or a stand-in.",
                   "For anything we cannot reach, plan a stand-in or a check at deploy.", "Mark the rows that need your choice.", "Write it all into one plan you sign once, on this page."],
         "run": run(("propose",), "Drafted by the agent from the triage rows."), "you": "Read the purple rows and sign the plan once."},
        {"key": "upgrade", "n": "3", "name": "Upgrade", "sub": "what we did · worked?",
         "what": "We make a safe copy, convert the app and apply the planned fixes. Every change is a separate commit you can undo.",
         "steps": ["Take a snapshot of the old app and its data as the baseline.", "Convert the model and update the modules.", "Apply the fixes from the plan, one commit each.",
                   "Build until it is clean. If a build fails, fix and retry, at most a few rounds.", "Record what worked, what did not, and anything new we found."],
         "run": run(("baseline", "convert", "update", "build"), "Runs on its own."), "you": "Nothing. Surprises with big app impact become a purple row."},
        {"key": "test", "n": "4", "name": "Test", "sub": "tested how · result",
         "what": "We run the old and the new app side by side and compare them. A failure only counts if the new app fails where the old one worked.",
         "steps": ["Start both apps on the same test data.", "Compare data, settings and logs between old and new.",
                   "Click through every page we have a path for, and take screenshots on both.",
                   "When a test itself is broken (missing data, missing system), the agent fixes the test, never the app, and reruns.",
                   "Anything we still cannot test gets a plan: a stand-in now, or a check at deploy."],
         "run": run(("basewalk", "after", "afterwalk", "journeys", "heal", "diff", "gate"), "Runs on its own and loops until nothing changes."),
         "you": "Look at visible changes and confirm they are fine."}]


def merge_trail(rows, trail):
    """Optional work/cockpit-trail.json: {"rows": {row id: [action, ...]}}. An action has name, sub, status and per stage
    (triage, plan, upgrade, test) the plain words (say, why, who, options, facts, results) and the proof behind them."""
    per = trail.get("rows") if isinstance(trail, dict) else None
    if not isinstance(per, dict):
        return
    for r in rows:
        acts = per.get(r["id"])
        if isinstance(acts, list) and acts:
            r["trail"] = acts


def plan_doc(text):
    """PROPOSAL.md as readable sections for the drawer: heading, intro lines, items with their sub-lines. Copied, never judged."""
    out, sec, cur = [], None, None
    for ln in (text or "").splitlines():
        if ln.startswith("<!--") or ln.startswith("# "):
            continue
        m = re.match(r"^(#{2,3}) (.*)$", ln)
        if m:
            sec = {"h": re.sub(r"^\d+\. ", "", m.group(2).strip()), "sub": len(m.group(1)) == 3, "intro": [], "items": []}
            out.append(sec)
            cur = None
            continue
        if sec is None or not ln.strip():
            continue
        t = ln.strip().replace("`", "")
        if ln.startswith("- "):
            cur = {"text": t[2:], "subs": []}
            mm = re.match(r"^\[(P-\d+)\] (\w+): (.*)$", cur["text"])
            if mm:
                cur.update(id=mm.group(1), kind=mm.group(2), name=mm.group(3).strip())
            sec["items"].append(cur)
        elif cur is not None and re.match(r"^\s+- ", ln):
            k, _, v = t[2:].partition(": ")
            cur["subs"].append([k, v] if _ else ["", t[2:]])
        else:
            sec["intro"].append(t)
            cur = None
    return out


# ---- step records (work/steps.jsonl, written by bin/steps.py): one row per step, the drawer reads the record ----
def _day(at):
    return (at or "")[:10]


def _answered(ap):
    """The day a person answered: the time on the page row when the approval came from the ledger, else the time it was written."""
    return _day((ap or {}).get("ledger_at") or (ap or {}).get("at"))


def _stage_ok(res):
    return res["verdict"] in ("PASS", "PASS*")


# ---- what a finding MEANS, per item (the owner, 2026-11-17: "not just what, but what it means"); built from the run's own files ----
def _json(work, name):
    try:
        with open(os.path.join(work or "", name), encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return None


def _edit_means(x):
    """What one localedits.json row means for the upgrade, in plain words."""
    k, ch, det = x.get("kind", ""), x.get("change", ""), x.get("detail") or ""
    if k == "layout" and ch == "CHANGED":
        return "The app restyled this shared layout. Every page on it, Marketplace pages too, takes its look from it. The update puts the plain layout back, so those pages lose the app's look unless they move to the app's own layout."
    if "removed by the update" in det:
        return "The app's own document inside a Marketplace module. The update deletes it; whatever uses it breaks unless it moves to a module of the app first."
    if k == "snippet":
        return "The update puts the package version of this snippet back. Screens that show it look like the package again."
    if k == "javascript":
        return "This JavaScript action differs from the package. The update overwrites it, so a local fix in it is lost."
    if k in ("entity", "attribute", "association") and ch == "ADDED" and x.get("data"):
        return "The app stores its own data here. A Marketplace update removes it, and the data stored in it with it."
    if "access rules" in det:
        return "The app changed who may see or edit this. The update puts the package rules back, so the app's access changes."
    if k in ("microflow", "nanoflow"):
        return "The app changed this logic. The update overwrites it, so the app behaves like the package again."
    return "The update overwrites this local change."


def _edit_name(x):
    return x.get("name") or x.get("path") or "?"


def found_detail(rec, work):
    """{"means": [sentences], "items": [[what, tag, tone, what it means]]} for the triage of one step, or {} when nothing is known.
    tone: ok (nothing lost), wait (a person looks), bad (lost or broken unless someone acts)."""
    t = rec.get("topic") or ""
    ev = [str(e) for e in (rec["found"].get("evidence") or [])]
    if t == "standins" or t.startswith("person:apis"):
        inv = _json(work, "apimock-inventory.json") or {}
        eps = inv.get("endpoints") or []
        if not eps:
            return {}
        items = []
        for e in eps:
            why = e.get("why") or ""
            if e.get("status") == "MOCKED":
                items.append([e["doc"], "stand-in ready", "ok", "The tests answer this call with a stand-in, so the screens that use it can be checked."])
            elif why.startswith("location from data"):
                fld = why.split(":")[0].replace("location from data", "").strip()
                items.append([e["doc"], "address from data", "wait", f"The address is read from the database ({fld}) while the app runs. The tests cannot know where it goes; a person names the real test system."])
            elif "computed by Java action" in why:
                items.append([e["doc"], "address built in Java", "wait", "A Java action builds the address while the app runs. The toolkit cannot see it, so a person says which system this is."])
            elif e.get("kind") == "const":
                items.append([e["doc"], "unused address?", "wait", "A web address setting that nothing in the model reads. Either it is unused, or a Java action reads it. A person checks."])
            else:
                items.append([e["doc"], e.get("status", "").lower() or "open", "wait", why])
        ok = sum(1 for i in items if i[2] == "ok")
        mods = sorted({e["doc"].split(".")[0] for e in eps if e.get("status") != "MOCKED"})
        return {"means": [f"{ok} of {len(items)} outside calls are covered in the tests.",
                          f"For the other {len(items) - ok}, a passing test only shows the screen works without the outside system. It says nothing about the real call.",
                          f"Before go-live, a person tests these against real test systems ({', '.join(mods)})."], "items": items}
    if t in ("modules", "module-edits"):
        edits = {m["name"]: m for m in (_json(work, "localedits.json") or []) if isinstance(m, dict)}
        items, clean, touched, unknown = [], 0, [], 0
        for e in ev:
            m = re.match(r"module update (\S+) (\S+) -> (\S+)", e)
            if not m:
                continue
            le = edits.get(m.group(1)) or {}
            rows = [x for k in ("domain", "ui", "logic", "files") for x in (le.get(k) or [])]
            if le.get("domain_error"):
                unknown += 1
                items.append([f"{m.group(1)} {m.group(2)} → {m.group(3)}", "not compared", "wait", "The toolkit could not compare this module with its Marketplace version, so local edits in it are not known."])
            elif rows:
                touched.append(m.group(1))
                items.append([f"{m.group(1)} {m.group(2)} → {m.group(3)}", f"{len(rows)} local edit" + ("" if len(rows) == 1 else "s"), "wait",
                              f"The app changed {', '.join(os.path.splitext(os.path.basename(x['path']))[0] if x.get('path') else _edit_name(x).split('.')[-1] for x in rows[:4])}{', ...' if len(rows) > 4 else ''}. "
                              + _edit_means(rows[0]) + " The toolkit carries the edit over; the Test step compares its screens on both apps."])
            else:
                clean += 1
                items.append([f"{m.group(1)} {m.group(2)} → {m.group(3)}", "no local edits", "ok", "The update swaps the whole module. Nothing of the app is lost."])
        if not items:
            return {}
        means = [f"{clean} of {len(items)} modules {'has' if clean == 1 else 'have'} no local edits: a clean swap."] if clean else []
        if touched:
            means.append(f"{len(touched)} {'carries' if len(touched) == 1 else 'carry'} edits by the app ({', '.join(touched)}). Not routine: the update replaces the whole module and the toolkit carries each edit back.")
            means.append("After the build, the screens that use these edits are compared on the old and the new app. The same: it goes ahead. A difference: a decision for you, with its case.")
        if unknown:
            means.append(f"{unknown} could not be compared, so nobody knows yet whether the app changed {'it' if unknown == 1 else 'them'}.")
        return {"means": means, "items": items}
    if t.startswith("module:"):
        mod = t.split(":", 1)[1]
        le = next((m for m in (_json(work, "localedits.json") or []) if isinstance(m, dict) and m.get("name") == mod), {}) or {}
        rows = [x for k in ("domain", "ui", "logic", "files") for x in (le.get(k) or [])]
        items = [[_edit_name(x), x.get("change", "").lower(), "bad" if x.get("data") else "wait", _edit_means(x)] for x in rows]
        if not items:
            items = [[e[:120], "to review", "wait", "The update step stopped at this module because stored data could be dropped or changed. A person accepts that with a reason, or keeps the old version."] for e in ev]
        data = sum(1 for x in rows if x.get("data"))
        means = [f"The app changed this Marketplace module in {len(rows)} place" + ("" if len(rows) == 1 else "s") + "." if rows else "The update would touch data this module stores."]
        if data:
            means.append(f"{data} of them {'holds' if data == 1 else 'hold'} the app's own data. A plain update deletes that data, so this cannot be routine.")
        means.append("A person picks the way: carry the edits over (recommended), move them out by hand, or keep the old version for now.")
        return {"means": means, "items": items}
    if t == "react":
        items = []
        for e in ev:
            m = re.search(r"(\d+) x (.+?) -> (.+)$", e)
            if m:
                items.append([f"{m.group(1)} × {m.group(2)}", "→ " + re.sub(r"\s*\(.*$", "", m.group(3)), "ok",
                              f"{m.group(2)} does not exist in the React client. The toolkit swaps each of the {m.group(1)} for {re.sub(r'\s*[(:].*$', '', m.group(3))}. The screen can look a bit different; the Test step checks it still works."])
        n = sum(int(i[0].split(" ")[0]) for i in items)
        return {"means": [f"{n} widgets in {len(items)} kind{'' if len(items) == 1 else 's'} move to their React successor.", "Nothing is lost: each swap keeps the data the widget showed. Screens can look a little different, which the screenshots in the Test step show."], "items": items} if items else {}
    if t == "convert":
        return {"means": ["Studio Pro's converter runs once. It moves the project to the new format and marks what it cannot convert.",
                          "Each mark becomes a build error that the toolkit fixes, and every fix is a change you can see in the Upgrade step."],
                "items": [[e, "convert", "ok", "A major version step; only the Mendix converter can make it."] for e in ev]}
    if t == "person:release-rows":
        return {"means": ["Mendix release notes between the two versions list changes that can affect an app.",
                          "The toolkit matched them to this app. A person marks each row handled or not relevant; until then, nobody has judged them."],
                "items": [[e, "open", "wait", "Each open row is a platform change nobody has checked against this app yet."] for e in ev]}
    return {}


def step_cells(rec):
    """The four cells and the drawer action of one step record. Every sentence is a template or the record's own plain text."""
    ap, pr, fd, gaps = rec.get("approval"), rec["proposed"], rec["found"], rec["gaps"]
    commits, results = rec["done"]["commits"], rec["tested"]["results"]
    state = (ap or {}).get("state")
    ev = [str(x) for x in (fd.get("evidence") or [])]
    # triage: what was found
    if fd.get("say"):
        triage = cell("ok", "Found", [fd["say"]], ev)
    else:
        triage = cell("none", "Not recorded", [gaps.get("found") or "No finding was written for this step."])
    # plan: what is proposed and who approved it
    who = {"approved": f"Approved by {(ap or {}).get('by', 'a person')} on {_answered(ap)}.",
           "assumed": "Assumed by the agent. It needs your OK.",
           "rejected": f"Rejected by {(ap or {}).get('by', 'a person')} on {_answered(ap)}."}.get(state, "No approval has been recorded yet.")
    if state in ("approved", "rejected") and (ap or {}).get("reason"):
        who += f" Reason: {ap['reason']}"
    lines = [x for x in (pr.get("say"), who if state == "assumed" else None) if x]   # why, options and approval are in the action below
    plan = {"approved": lambda: cell("ok", "Approved", lines), "assumed": lambda: cell("you", "Needs your OK", lines),
            "rejected": lambda: cell("bad", "Rejected", lines)}.get(state, lambda: cell("wait" if pr.get("say") else "none", "Not approved yet" if pr.get("say") else "Not proposed", lines or [gaps.get("proposed") or "Nothing was proposed for this step."]))()
    if (rec.get("topic") or "").startswith("person:"):   # cold test WM1: these showed as open approvals after the plan was approved
        plan = cell("none", "For a person", [pr.get("say") or "A person does this; the toolkit lists it so it is not forgotten."])
    # upgrade: the commits that did it
    n = len(commits)
    if n:
        upgrade = cell("ok", f"{n} change" + ("" if n == 1 else "s"), [c["say"] for c in commits], [c["sha"] for c in commits])
    elif gaps.get("done"):
        upgrade = cell("none", "Not needed", [gaps["done"]])
    elif state == "approved":
        upgrade = cell("wait", "Not done yet", ["The step is approved, and no change in the app names it yet."])
    elif state == "rejected":
        upgrade = cell("none", "Not needed", ["The step was rejected, so nothing was changed."])
    elif (rec.get("topic") or "").startswith("person:"):
        upgrade = cell("none", "Not needed", ["The toolkit changes nothing in the app for this."])
    else:
        upgrade = cell("none", "Not started", ["Nothing changes in the app before the step is approved."])
    # test: one line per rung the step closes by; a rung with no passing result is a gap, never a pass
    rungs = pr.get("closes_by") or []
    got = {r["rung"]: r for r in results}
    rows, lines_t, gapn = [], [], 0
    for rg in rungs or []:
        r = got.get(rg)
        nm = cp.RUNG_NAMES.get(rg, rg)
        if r and _stage_ok(r):
            rows.append([nm, "pass", r["say"]])
        elif r and r["verdict"] == "FAIL":
            rows.append([nm, "fail", r["say"]])
        else:
            gapn += 1
            rows.append([nm, "gap", (r or {}).get("say") or gaps.get("tested:" + rg) or "No result yet, so nothing tested this."])
    for r in results:
        if r["rung"] not in rungs and _stage_ok(r):
            rows.append([cp.RUNG_NAMES.get(r["rung"], r["rung"]), "pass", r["say"]])
    noted = False   # a written note that nothing is tied to a check (a routine note, or a run that predates step records) is not an open topic
    if not rungs and not any(_stage_ok(r) for r in results):
        note = gaps.get("tested")
        noted = bool(note) and note != stp.NO_CHECK
        gapn = 0 if noted else 1
        rows.append(["Linked checks", "none" if noted else "gap", note or "No check is linked to this step, so nothing tested it."])
    lines_t = [x[2] for x in rows]
    if noted and not any(x[1] == "fail" for x in rows):
        test = cell("none", "Not tied to a check", lines_t)
    elif any(x[1] == "fail" for x in rows):
        test = cell("bad", "Failed", lines_t)
    elif gapn and (rec.get("topic") or "").startswith("person:"):
        test = cell("none", "Later, by a person", lines_t)
    elif gapn:
        test = cell("wait", "Test gap", lines_t)
    elif rows:
        test = cell("ok", "Passed with accepted differences" if any(r["verdict"] == "PASS*" for r in results) else "Passed", lines_t)
    else:
        test = cell("none", "Not yet", ["The checks have not run yet."])
    test["tech"] = [str(p) for r in results for p in r.get("proof", [])]
    plain_opts = [o for i, o in enumerate(pr.get("options") or []) if i != pr.get("recommend")]
    proof_t = [{"kind": "text", "src": str(p), "how": "", "text": "", "imgs": []} for r in results for p in r.get("proof", [])]
    act = {"name": rec["title"], "sub": rec["topic"], "status": "done" if rec["status"] == "done" else "open", "stages": {
        "triage": {"say": fd.get("say") or "", "gap": not fd.get("say"),
                   "proof": [{"kind": "text", "src": e, "how": "", "text": "", "imgs": []} for e in ev]},
        "plan": {"say": pr.get("say") or "", "why": pr.get("why") or "", "who": who, "options": plain_opts, "gap": not pr.get("say"),
                 "proof": [{"kind": "text", "src": d, "how": "A decision the agent made on its own.", "text": "", "imgs": []} for d in pr.get("decisions") or []]},
        "upgrade": {"say": upgrade["l"] + "." if n else upgrade["steps"][0], "facts": [],
                    "proof": [{"kind": "commit", "h": c["sha"], "d": "", "s": c["say"]} for c in commits]},
        "test": {"say": test["l"] + "." if rows else test["steps"][0], "results": rows, "gap": bool(gapn), "proof": proof_t}}}
    return {"triage": triage, "plan": plan, "upgrade": upgrade, "test": test}, act


def step_row(rec, work=None):
    """One overview row for one step record."""
    cells, act = step_cells(rec)
    fd = found_detail(rec, work) if work else {}
    act["stages"]["triage"].update(means=fd.get("means") or [], items=fd.get("items") or [])
    r = row(rec["id"], rec["title"] or rec["id"], f"{rec['id']} · {rec['topic']}", STEP_GROUP[0], cells, rec["found"].get("evidence") or [])
    r["trail"] = [act]
    r["fromSteps"] = True
    r["story"] = {"found": [x for x in [rec["found"].get("say")] if x], "means": fd.get("means") or [],
                  "plan": [x for x in [rec["proposed"].get("say"), rec["proposed"].get("why")] if x]}
    if rec.get("phase"):   # a two-version upgrade: the version this step belongs to (steps.py UPG_PHASE)
        r["phase"] = rec["phase"]
    ap = rec.get("approval") or {}
    # slice 8: only a step that is still assumed (or has no approval) gets the buttons; an answered step shows who answered
    r["ask"] = ap.get("state") in (None, "assumed") and not (rec.get("topic") or "").startswith("person:")
    if ap.get("state") in ("approved", "rejected"):
        r["ans"] = {"state": ap["state"], "by": ap.get("by") or "", "day": _answered(ap), "reason": ap.get("reason") or ""}
    states = [c["s"] for c in cells.values() if c["s"] not in ("ok", "none")]
    r["kind"] = "owner" if "you" in states else "testgap" if states and all(s == "wait" for s in states) and cells["test"]["s"] == "wait" else "upgrade"
    return r


def run_base(work):
    """The work folder of rung 1: rung 2 works in <work>/rung2 and shares the run's ladder, steps and cockpit."""
    return os.path.dirname(work) if os.path.basename(os.path.normpath(work)) == "rung2" else work


def ladder(work):
    """The version route and how far each rung got: [{v, state}] with done, now or next (the first version is the start).
    [] without ladder.json (a run made before the version ladder)."""
    base = run_base(work)
    route = (cp.rj(os.path.join(base, "ladder.json")) or {}).get("route") or []
    if len(route) < 2:
        return []
    out = [{"v": route[0], "state": "done", "say": "start"}]
    for i, v in enumerate(route[1:]):
        w = base if i == 0 else os.path.join(base, "rung2")
        ov = cp.parse_gate(cp.rd(os.path.join(w, "gate-summary.md")) or "")["overall"]
        started = os.path.isdir(os.path.join(w, "state")) and any(n.endswith(".done") for n in os.listdir(os.path.join(w, "state")))
        st = "done" if ov == "PASS" else "now" if started or ov else "next"
        out.append({"v": v, "state": st, "say": {"done": "gate passed", "now": f"gate {ov}" if ov else "in progress", "next": "next"}[st]})
    return out


JLINE = re.compile(r"(\d+) PASS, (\d+) FAIL, (\d+) INVALID")
ALINE = re.compile(r"actions (\d+) found\D+(\d+) generated")


def health(work):
    """How the tests improved, per version: heal rounds from heal.json and the click path counts and action coverage of the gate.
    [] when no version has a heal or a gate yet."""
    base, out = run_base(work), []
    route = (cp.rj(os.path.join(base, "ladder.json")) or {}).get("route") or []
    for i, w in enumerate([base, os.path.join(base, "rung2")]):
        heal = cp.rj(os.path.join(w, "heal.json")) or {}
        g = {r["rung"]: r for r in cp.parse_gate(cp.rd(os.path.join(w, "gate-summary.md")) or "")["rungs"]}
        jd = (g.get("journeys") or {}).get("detail", "")
        jm, am = JLINE.search(jd), ALINE.search(jd)
        if not heal.get("rounds") and not jm:
            continue
        cls = {}
        for r in heal.get("rows", []):
            cls[r.get("class", "")] = cls.get(r.get("class", ""), 0) + 1
        out.append({"v": ".".join(route[i + 1].split(".")[:3]) if len(route) > i + 1 else "",
                    "rounds": [{"n": r.get("round"), "fixed": r.get("new_heals", 0), "left": r.get("rows", 0)} for r in heal.get("rounds", [])],
                    "paths": [int(x) for x in jm.groups()] if jm else None,
                    "actions": [int(x) for x in am.groups()] if am else None,
                    "real": cls.get("real-regression", 0), "setup": cls.get("test-setup", 0),
                    "noise": cls.get("startup-noise", 0), "nopath": cls.get("no-click-path", 0)})
    return out


def phases(rows):
    """The target versions of a two-version upgrade, oldest first; [] for a one-version upgrade (no filter is shown then)."""
    key = lambda v: [int(x) if x.isdigit() else 0 for x in re.split(r"[.-]", v)]
    return sorted({r["phase"] for r in rows if r.get("phase")}, key=key)


def merge_steps(rows, recs, item_keys=(), work=None):
    """Add one row per step after the derived rows of the group "app"; the rows keep step order. The same topic is the same step: a row
    that cockpit-items.json declared for a topic gives way to the step with that topic, so a topic never shows twice."""
    topics = {r["topic"] for r in recs}
    rows[:] = [r for r in rows if not (r["id"] in topics and r["id"] in item_keys and not r.get("fromSteps"))]
    rows.extend(step_row(r, work) for r in recs)
    order = {k: i for i, (k, _) in enumerate([GROUPS[0], STEP_GROUP] + GROUPS[1:])}
    rows.sort(key=lambda r: order[r["group"]])


def build(work, model):
    work = os.path.abspath(work)
    rows, chips, P, g, done, per, ledger = derive(work, model)
    items = cp.rj(os.path.join(work, "cockpit-items.json")) or {}
    if not isinstance(items, dict):
        items = {}
    merge_items(rows, chips, items, work)
    recs, err = stp.load(work)   # recs is None when steps.jsonl is missing or damaged: then the older inputs below are used as they were
    groups = list(GROUPS)
    if recs is not None:
        try:
            merge_steps(rows, recs, set(items.get("items") or {}), work)
            groups.insert(1, STEP_GROUP)
        except (KeyError, TypeError, AttributeError, ValueError):
            recs, err = None, "a step record is incomplete"
            rows[:] = [r for r in rows if not r.get("fromSteps")]
    if recs is None:
        merge_trail(rows, cp.rj(os.path.join(work, "cockpit-trail.json")) or {})
    kpi = items.get("kpi")
    if err:
        kpi = dict(kpi) if isinstance(kpi, dict) else {}
        kpi["open"] = list(kpi.get("open") or []) + [{"group": "To fix", "text": f"The step records are damaged ({err}), so this page shows the older inputs.", "owner": "agent"}]
    ri = cp.rd(os.path.join(work, "release-impact.md")) or ""
    rl = len([r for r in ri.splitlines() if re.match(r"^\| \d+ \|", r)])
    tl = tiles(rows, chips, g.get("open_reg"))
    return {"stages": stage_texts(rl, per), "groups": [{"key": k, "name": n} for k, n in groups], "rows": rows, "ready": chips,
            "tiles": tl, "feed": feed(work, model, ledger, items, g.get("closed_q") or []), "loop": list(LOOP),
            "band": band(model, rows, chips, g, tl, kpi),
            "generated": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "phases": phases(rows), "ladder": ladder(work), "health": health(work), "cases": cases(work, model),
            "itemsFile": os.path.exists(os.path.join(work, "cockpit-items.json")), "stepsFile": recs is not None,
            "plan": plan_doc(cp.rd(os.path.join(work, "PROPOSAL.md"))), "ran": test_runs(work)}


def _count_line(txt):
    """'FAIL 0 | REVIEW 2 | PASS* 1 | PASS 47' -> {'FAIL': 0, ...} from the first line that has it."""
    for ln in (txt or "").splitlines():
        m = re.findall(r"(PASS\*|[A-Z_]+) (\d+)(?: \||$)", ln)
        if len(m) >= 2 and ("PASS" in dict(m) or "FAIL" in dict(m)):
            return {k: int(v) for k, v in m}
    return None


# the page speaks plain words, never the gate's verdict names (control cockpit-words-no-plural-marker-pass)
RUN_WORD = {"PASS": "passed", "PASS*": "accepted with a reason", "FAIL": "failed", "INVALID": "could not be judged",
            "REVIEW": "to look at", "INFO": "listed only", "SKIPPED": "skipped, failed on the old app",
            "NOT CHECKED": "not checked", "NEW_ENDPOINT": "new endpoint", "UNREACHABLE": "unreachable",
            "CONTAMINATED": "could not be judged"}


def _word(v):
    return RUN_WORD.get(v, v.lower())


def _vc(vs):
    order = ("PASS", "PASS*", "FAIL", "INVALID", "SKIPPED", "INFO", "NOT CHECKED")
    c = {}
    for v in vs:
        c[v] = c.get(v, 0) + 1
    return ", ".join(f"{c[k]} {_word(k)}" for k in sorted(c, key=lambda k: (order.index(k) if k in order else 99, k)))


def test_runs(work):
    """What actually ran in the Test stage, on the old app and on the new one (the owner, 2026-11-17: "see which tests
    actually ran, on old and new"). rows: [check, old app, new app, compared]; lists: per check every test with both
    verdicts. Read from the stored results only; a side without a file says "not run"."""
    rows, lists = [], {}
    sm = {sd: cp.rj(os.path.join(work, f"smoke-{sd}.json")) for sd in ("before", "after")}
    if any(sm.values()):
        per = {}
        for i, sd in enumerate(("before", "after")):
            for r in (sm[sd] or {}).get("roles", []):
                for st in r.get("steps", []):
                    per.setdefault(f"{r['role']}: {st.get('caption')}", ["not run", "not run"])[i] = st.get("verdict", "?")
        side = lambda i: (cp.pl(sum(1 for v in per.values() if v[i] != 'not run'), "page") + ": " + _vc(v[i] for v in per.values() if v[i] != "not run")) if sm[("before", "after")[i]] else "not run"
        scr = _count_line(cp.rd(os.path.join(work, "screens.out")))
        rows.append(["Page walk", side(0), side(1), (f"{sum(scr.values())} screenshot pairs: " + ", ".join(f"{v} {_word(k)}" for k, v in scr.items() if v)) if scr else "screenshots not compared"])
        lists["Page walk"] = [[k] + [_word(x) if x != "not run" else x for x in v] for k, v in sorted(per.items())]
    js = {sd: cp.rj(os.path.join(work, f)) for sd, f in (("old", "e2e-before-picked/before-picked/summary.json"), ("new", "e2e-after/after/summary.json"))}
    if any(js.values()):
        ids = sorted(set().union(*[set((d or {}).get("journeys", {})) for d in js.values()]))
        vv = {sd: {j: x.get("verdict", "?") for j, x in ((d or {}).get("journeys") or {}).items()} for sd, d in js.items()}
        jf = {sd: os.path.join(work, f) for sd, f in (("old", "e2e-before-picked/before-picked/summary.json"), ("new", "e2e-after/after/summary.json"))}
        # WM1 2026-11-17: a rerun walks the old app first; the new app's file was still the one of the run before
        stale = js["old"] and js["new"] and os.path.getmtime(jf["new"]) < os.path.getmtime(jf["old"])
        if stale:
            js["new"], vv["new"] = None, {}
        side = lambda sd: (cp.pl(len(vv[sd]), "journey") + ": " + _vc(vv[sd].values())) if js[sd] else ("not run yet in this run" if sd == "new" and stale else "not run")
        both = sum(1 for j in ids if vv["old"].get(j) == "PASS" and vv["new"].get(j) == "PASS")
        lost = sum(1 for j in ids if vv["old"].get(j) == "PASS" and vv["new"].get(j) not in (None, "PASS"))
        rows.append(["Journeys", side("old"), side("new"), f"{both} pass on both, {lost} passed on the old app and not on the new one"
                     if js["old"] and js["new"] else "needs both apps"])
        lists["Journeys"] = [[j, _word(vv["old"][j]) if j in vv["old"] else "not run", _word(vv["new"][j]) if j in vv["new"] else "not run"] for j in ids]
    for f, nm in (("data.out", "Data compare"), ("logdiff.out", "Start log"), ("const.out", "Constants")):
        c = _count_line(cp.rd(os.path.join(work, f)))
        if c:
            rows.append([nm, "snapshot taken" if nm != "Start log" else "start log read", "snapshot taken" if nm != "Start log" else "start log read",
                         f"{sum(c.values())} checks: " + ", ".join(f"{v} {_word(k)}" for k, v in c.items() if v)])
    return {"rows": rows, "lists": lists}

# ---- the top band: what is closed, what is still to validate (generic, from rows and gate rungs) ----
def _rung_detail(g, name):
    r = next((x for x in g["rungs"] if x["rung"] == name), None)
    return (r["detail"].replace("\\|", "|") if r else ""), r


def _first(pat, text):
    m = re.search(pat, text or "")
    return int(m.group(1)) if m else 0


def closed_items(rows, g, tl):
    """Non-overlapping counts of things that are done. Every number is read from a row or a gate rung; a missing rung drops out."""
    out = [(tl["upg"][0], "upgrade problems solved"), (tl["gap"][0], "test gaps closed")]
    out.append((sum(c.get("n", 0) for r in rows for c in r["cells"].values() if c["s"] == "ok"), "fixes applied"))
    d, _ = _rung_detail(g, "release")
    out.append((_first(r"(\d+) of \d+ rows handled", d), "release notes handled"))
    d, _ = _rung_detail(g, "journeys")
    out.append((_first(r"journeys: (\d+) PASS(?!\*)", d), "journeys pass"))
    out.append((_first(r"(\d+) PASS\*", d), "journeys behave as on the old app"))
    rest = 0
    for name in ("apis", "rest"):
        d, _ = _rung_detail(g, name)
        rest = max(rest, _first(r"direct API test: PASS (\d+)", d), _first(r"(\d+) calls match", d))
    if not rest:   # a run that words it in a cell ("61 calls match") instead of in the gate row
        rest = max([_first(r"(\d+) calls match", c["l"]) for r in rows for c in r["cells"].values()] or [0])
    out.append((rest, "REST calls match the old app"))
    d, _ = _rung_detail(g, "const")
    out.append((_first(r"(?<![\w*])PASS (\d+)", d), "constants checked"))
    return [{"n": n, "label": t} for n, t in out if n > 0]


def open_items(rows, chips, g):
    """Open topics to validate, each with a group and an owner, derived from the matrix cells."""
    out, seen = [], {}

    def add(group, text, owner, ver=""):
        hit = seen.get((group, text))
        if hit is None:
            seen[(group, text)] = hit = {"group": group, "text": text, "owner": owner, "vers": []}
            out.append(hit)
        if ver and ver not in hit["vers"]:
            hit["vers"].append(ver)
    d, _ = _rung_detail(g, "release")
    nrel = _first(r"rows handled or not relevant, (\d+) open", d)
    if nrel:
        add("Your call", f"{nrel} release notes to review", "you")
    for r in rows:
        if r["id"] == "release" and nrel:
            continue
        cs = [(k, r["cells"][k]) for k in STAGES if r["cells"][k]["s"] in ("wait", "bad", "you")]
        if not cs:
            continue
        nm, ver = r["name"], r.get("phase") or ""   # a two-version upgrade: the same topic on both rungs is one line
        you = next(((k, c) for k, c in cs if c["s"] == "you"), None)
        dep = next(((k, c) for k, c in cs if c["deploy"]), None)
        tc = r["cells"]["test"]
        if you:
            add("Your call", f"{nm}: {you[1]['l']}", "you", ver)
        elif r["regression"]:
            add("Regression", f"{nm}: {tc['l']}", "agent", ver)
        elif any(c["s"] == "bad" for _, c in cs):
            add("To fix", f"{nm}: {next(c for _, c in cs if c['s'] == 'bad')['l']}", "agent", ver)
        elif dep or r["group"] == "golive":
            c = (dep or cs[-1])[1]
            add("At deploy", f"{nm}: {c['l']}", "you / customer", ver)
        else:
            add("Coverage", f"{nm}: {cs[-1][1]['l']}", "agent", ver)
    for c in chips:
        if c.get("row") or c["s"] == "ok":
            continue
        if c["s"] == "none" and c.get("kind") != "golive":
            continue
        add("Your call" if c.get("kind") == "golive" else "Coverage", c["l"], "you" if c.get("kind") == "golive" else "agent")
    for o in out:
        if o["group"] == "Your call":   # the group already says it needs you
            o["text"] = re.sub(r":\s*Needs your OK$", "", o["text"])
        vers = o.pop("vers")
        if vers:
            o["text"] += f" (Mendix {', '.join(vers)})"
    return out


def band(model, rows, chips, g, tl, kpi=None):
    """The summary on top: headline, regressions, closed total with chips, open topics. kpi (optional, from cockpit-items.json):
    {"closed": [{"n","label"}], "open": [{"group","text","owner"}], "hide": ["text part", ...]} adds, renames or hides entries."""
    kpi = kpi if isinstance(kpi, dict) else {}
    vm = re.search(r"(\d+(?:\.\d+)+) → (\d+(?:\.\d+)+)", model.get("sub", ""))
    tgt = vm.group(2) if vm else ""
    b = next((r for r in g["rungs"] if r["rung"] == "build"), None)
    reg = tl.get("reg")
    core = [r for r in g["rungs"] if r["rung"] in ("smoke", "data", "idcheck", "const", "logdiff") and r["verdict"] == "FAIL"]
    if b and b["verdict"].startswith("PASS") and core:
        names = ", ".join(cp.RUNG_NAMES.get(r["rung"], r["rung"]) for r in core)
        st, head = "warn", f"The app builds on Mendix {tgt}" if tgt else "The app builds on the new Mendix version"
        sub = f"Next step for the agent: fix {len(core)} final {'check' if len(core) == 1 else 'checks'} ({names})."
    elif b and b["verdict"].startswith("PASS"):
        st, head = "ok", f"The app runs on Mendix {tgt}" if tgt else "The app runs on the new Mendix version"
        sub = "" if reg is None else (f"{reg} regression" + ("" if reg == 1 else "s"))
    elif b and b["verdict"] == "FAIL":
        st, head, sub = "bad", "The build does not pass yet", "The agent is fixing it."
    else:
        st, head, sub = "neutral", (f"Upgrade to Mendix {tgt} in progress" if tgt else "Upgrade in progress"), "The build has not run yet."
    if model.get("stopped") and st != "ok":   # a judgment stop outranks "in progress": nothing moves until a person decides
        s = model["stopped"]
        st, head = "bad", f"Stopped at {s['step']}, waiting for you"
        n = len(open_questions(model)) or len(s["titles"])   # the cards in Blocked on you, not the stop file's older list
        sub = f"{n} {'item' if n == 1 else 'items'} to decide, then rerun (see the red bar)."
    closed =closed_items(rows, g, tl)
    for it in kpi.get("closed") or []:
        if isinstance(it, dict) and isinstance(it.get("label"), str) and isinstance(it.get("n"), int):
            hit = next((c for c in closed if c["label"].lower() == it["label"].lower()), None)
            if hit:
                hit["n"] = it["n"]
            elif it["n"] > 0:
                closed.append({"n": it["n"], "label": it["label"]})
    opens = open_items(rows, chips, g)
    for it in kpi.get("open") or []:
        if isinstance(it, dict) and isinstance(it.get("text"), str):
            opens.append({"group": str(it.get("group") or "Coverage"), "text": it["text"], "owner": str(it.get("owner") or "agent")})
    # every Blocked on you card is also in "for you now" (cold test WM1: 1 here, 7 there): add the ones the matrix did not list
    for i in open_questions(model):
        nm = re.sub(r"\s*\((module|widget|jar|java|check)\)$", "", i.get("title", ""))
        if i["kind"] != "signoff" and not any(nm and nm in o["text"] for o in opens if o["owner"] != "agent"):
            opens.append({"group": "Your call", "text": question_of(i), "owner": "you"})
    order = {"Regression": 0, "To fix": 1, "Your call": 2, "At deploy": 3, "Coverage": 4}
    opens.sort(key=lambda x: order.get(x["group"], 9))   # stable: same group keeps its order
    hide = [str(h).lower() for h in (kpi.get("hide") or []) if isinstance(h, str) and h]
    closed = [c for c in closed if not any(h in c["label"].lower() for h in hide)]
    opens = [o for o in opens if not any(h in (o["text"] + " " + o["group"]).lower() for h in hide)]
    return {"state": st, "head": head, "sub": sub, "reg": reg, "closed": {"n": sum(c["n"] for c in closed), "chips": closed},
            "open": {"n": len(opens), "items": opens}}


# ---- page ----
CSS = r"""
:root{
  --bg:#f3f5f7; --panel:#ffffff; --fg:#17212b; --muted:#5b6875; --line:#d9dfe5; --accent:#0f6e7a; --accentbg:#e3f1f3;
  --ok:#1f8a4c; --wait:#b7770f; --bad:#c23b2e; --none:#9aa5b1; --late:#c23b2e; --you:#5b4bc4; --youbg:#ece9fb;
  --okbg:#e6f4ec; --waitbg:#fbf1de; --badbg:#fbe7e4; --nonebg:#eef1f4; --shade:rgba(15,25,35,.28);
  --sans:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
  --mono:ui-monospace,Menlo,Consolas,monospace;
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
  --bg:#11171d; --panel:#18212a; --fg:#e4e9ee; --muted:#93a1ae; --line:#2b3742; --accent:#4fb8c4; --accentbg:#16323a;
  --ok:#4cc27e; --wait:#e0a43b; --bad:#ec6a5c; --none:#6c7a87; --late:#ec6a5c; --you:#a99cf5; --youbg:#29244a;
  --okbg:#183326; --waitbg:#342a14; --badbg:#3a1d1a; --nonebg:#1f2a34; --shade:rgba(0,0,0,.5); color-scheme:dark}}
:root[data-theme="dark"]{
  --bg:#11171d; --panel:#18212a; --fg:#e4e9ee; --muted:#93a1ae; --line:#2b3742; --accent:#4fb8c4; --accentbg:#16323a;
  --ok:#4cc27e; --wait:#e0a43b; --bad:#ec6a5c; --none:#6c7a87; --late:#ec6a5c; --you:#a99cf5; --youbg:#29244a;
  --okbg:#183326; --waitbg:#342a14; --badbg:#3a1d1a; --nonebg:#1f2a34; --shade:rgba(0,0,0,.5); color-scheme:dark}
*{box-sizing:border-box}
body{background:var(--bg);color:var(--fg);font-family:var(--sans);font-size:15px;line-height:1.45;margin:0}
.wrap{max-width:1440px;margin:0 auto;padding-block:28px 48px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));display:grid;gap:20px}
.eyebrow{font-family:var(--mono);font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--accent)}
h1{font-size:30px;margin:4px 0 6px;text-wrap:balance}
h2{font-size:17px;margin:0;text-wrap:balance}
.ver{font-family:var(--mono);font-size:13px;color:var(--muted)}
.head{display:flex;flex-wrap:wrap;justify-content:space-between;gap:16px;align-items:flex-end}
.tiles{display:flex;flex-wrap:wrap;gap:10px;width:100%}
.tile{background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:10px 14px;min-width:116px;font:inherit;color:inherit;text-align:left}
.tile b{display:block;font-size:24px;font-variant-numeric:tabular-nums}
.tile span{font-size:12px;color:var(--muted)}
.tile.warn b{color:var(--wait)} .tile.good b{color:var(--ok)} .tile.bad b{color:var(--bad)} .tile.you b{color:var(--you)}
.tile small{font-size:14px;color:var(--muted)}
button.tile{cursor:pointer} button.tile:hover{border-color:var(--you)}
.headline{display:flex;flex-wrap:wrap;gap:6px 34px;font-size:20px;color:var(--muted);width:100%}
.headline b{font-size:40px;color:var(--ok);font-variant-numeric:tabular-nums}
.headline .neutral b{color:var(--muted)} .headline .bad b{color:var(--bad)}
.tile.kind.neutral b{color:var(--fg)}
.tile.kind[aria-pressed=true]{border-color:var(--accent);background:var(--accentbg)}
.row.dim,.chip.dim{opacity:.25}
.row.kin{box-shadow:inset 4px 0 0 var(--accent)}
.chip.kin{outline:2px solid var(--accent);outline-offset:1px}
.legend{display:flex;flex-wrap:wrap;gap:14px;font-size:13px;color:var(--muted)}
.legend i{display:inline-block;width:10px;height:10px;border-radius:50%;margin-right:6px;vertical-align:-1px}
.card{background:var(--panel);border:1px solid var(--line);border-radius:10px}
.ready{padding:14px 16px;display:grid;gap:10px}
.ready .top{display:flex;justify-content:space-between;flex-wrap:wrap;gap:8px;align-items:baseline}
.ready .top span{font-size:13px;color:var(--muted)}
.rchips{display:flex;flex-wrap:wrap;gap:8px}
.ladder h2,.health h2{font-size:15px;margin:0 0 10px}
.lrow{display:flex;flex-wrap:wrap;align-items:center;gap:8px}
.lv{display:flex;flex-direction:column;padding:8px 14px;border-radius:8px;background:var(--nonebg);border-left:4px solid var(--none)}
.lv.ok{background:var(--okbg);border-color:var(--ok)} .lv.wait{background:var(--waitbg);border-color:var(--wait)}
.lv small{color:var(--muted);font-size:12px} .la{color:var(--muted);font-size:18px}
.hv{margin:6px 0 14px} .hv h3{font-size:13px;margin:0 0 6px;color:var(--muted)}
.hrow{display:grid;grid-template-columns:150px minmax(120px,320px) 1fr;gap:12px;align-items:center;padding:5px 0;font-size:13px;border-top:1px solid var(--line)}
.hrow em{font-style:normal;color:var(--muted)} .hrow .num b{font-size:18px;color:var(--ok);margin-right:4px}
.bar{display:flex;height:12px;border-radius:6px;overflow:hidden;background:var(--nonebg)}
.bar i.ok{background:var(--ok)} .bar i.bad{background:var(--bad)} .bar i.none{background:var(--none);opacity:.5}
@media (max-width:640px){.hrow{grid-template-columns:1fr}}
.pbar{display:flex;flex-wrap:wrap;align-items:center;gap:8px;padding:10px 12px 0}
.pbar .plbl{font-size:12px;color:var(--muted);margin-right:4px}
.pbar .chip{width:auto;flex:0 0 auto;background:var(--accentbg);padding:6px 12px}
.pbar .chip.on{outline:2px solid var(--accent);outline-offset:1px}
.rchips .chip{width:auto}
.rchips .chip+.chip{margin-top:0}
[hidden]{display:none!important}
#dBody{display:grid;gap:18px}
.scroll{overflow-x:auto}
.grid{min-width:940px}
.row{display:grid;grid-template-columns:200px repeat(4,1fr)}
.row+.row,.grp+.row{border-top:1px solid var(--line)}
.hd{border-bottom:1px solid var(--line)}
.stage{all:unset;box-sizing:border-box;cursor:pointer;padding:12px;font-size:13px;font-weight:700;display:flex;flex-direction:column;gap:2px;border-radius:8px 8px 0 0}
.stage:hover,.stage[aria-pressed="true"]{background:var(--accentbg)}
.stage:focus-visible{outline:2px solid var(--accent);outline-offset:-2px}
.stage small{font-weight:400;color:var(--muted);font-size:12px}
.stage .n{font-family:var(--mono);color:var(--accent);margin-right:6px}
.stage .more{font-weight:400;font-size:11.5px;color:var(--accent)}
.hcell{padding:12px;font-size:13px;font-weight:700}
.item{padding:12px;font-weight:700;font-size:14px;overflow-wrap:anywhere}
.item small{display:block;font-weight:400;color:var(--muted);font-size:12px;font-family:var(--mono)}
.cell{padding:8px 10px;min-width:0}
.cell.on{background:var(--accentbg)}
.chip small.cd{display:block;font-size:12px;color:var(--muted);font-weight:400;margin-top:2px}
.story{display:grid;gap:10px}.story section{border-left:3px solid var(--line);padding:2px 0 2px 12px}.story p{margin:0 0 4px}
.chip{all:unset;box-sizing:border-box;cursor:pointer;display:flex;gap:8px;align-items:flex-start;width:100%;font-size:13px;padding:6px 8px;border-radius:6px;line-height:1.35;overflow-wrap:anywhere}
.chip+.chip{margin-top:6px}
.chip:hover{filter:brightness(.97)}
.chip:focus-visible{outline:2px solid var(--accent);outline-offset:1px}
.chip::before{content:"";flex:none;width:9px;height:9px;border-radius:50%;margin-top:4px}
span.chip{cursor:default}
.ok{background:var(--okbg)} .ok::before{background:var(--ok)}
.wait{background:var(--waitbg)} .wait::before{background:var(--wait)}
.bad{background:var(--badbg)} .bad::before{background:var(--bad)}
.none{background:var(--nonebg);color:var(--muted)} .none::before{background:var(--none)}
.you{background:var(--youbg)} .you::before{background:var(--you)}
.grp{padding:8px 12px;font-family:var(--mono);font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);background:var(--bg);border-top:1px solid var(--line)}
.feed{padding:14px 16px;display:grid;gap:8px}
.feed ol{list-style:none;margin:0;padding:0;display:grid;gap:6px;font-size:14px}
.feed time{font-family:var(--mono);font-size:12px;color:var(--muted);margin-right:10px}
.feed .new{font-weight:700}
.note{font-size:12px;color:var(--muted)}
.shade{position:fixed;inset:0;background:var(--shade);z-index:20}
.drawer{position:fixed;top:0;right:0;bottom:0;width:min(max(520px,50vw),100%);background:var(--panel);border-left:1px solid var(--line);z-index:21;overflow-y:auto;
  padding:calc(20px + env(safe-area-inset-top,0px)) max(20px,env(safe-area-inset-right,0px)) calc(28px + env(safe-area-inset-bottom,0px)) 22px;display:grid;gap:16px;align-content:start}
details.kpi summary{cursor:pointer;list-style:none}details.kpi summary b{display:block}details.kpi summary span{font-size:13px;color:var(--muted)}.agentnote{margin:14px 2px 0;font-size:13px;color:var(--muted)}.drawer>*,.drawer *{min-width:0;overflow-wrap:anywhere}.drawer pre,.drawer code{white-space:pre-wrap}
.drawer .x{all:unset;cursor:pointer;position:absolute;top:calc(14px + env(safe-area-inset-top,0px));right:max(16px,env(safe-area-inset-right,0px));font-size:22px;color:var(--muted);padding:4px 8px;border-radius:6px}
.drawer .x:focus-visible{outline:2px solid var(--accent)}
.drawer h3{margin:0;font-size:21px;padding-right:36px;text-wrap:balance}
.drawer h4{margin:0 0 6px;font-size:12px;font-family:var(--mono);letter-spacing:.07em;text-transform:uppercase;color:var(--muted);font-weight:500}
.steps{margin:0;padding:0;list-style:none;counter-reset:n;display:grid;gap:10px}
.steps li{counter-increment:n;display:grid;grid-template-columns:28px 1fr;gap:10px;font-size:14.5px}
.steps li::before{content:counter(n);font-family:var(--mono);font-size:12px;width:24px;height:24px;border-radius:50%;background:var(--accentbg);color:var(--accent);display:grid;place-items:center}
.box{padding:12px 14px;border-radius:8px;background:var(--bg);font-size:14px}
.box.youbox{background:var(--youbg)}
.mini{display:grid;gap:6px}
.mini .chip{font-size:13px}
.nav{display:flex;align-items:center;gap:8px;flex-wrap:wrap;padding-right:40px}
.back{all:unset;cursor:pointer;font-size:13px;color:var(--accent);padding:4px 8px;border-radius:6px;border:1px solid var(--line)}
.back:hover{background:var(--accentbg)} .back:focus-visible,.tab:focus-visible,.step:focus-visible{outline:2px solid var(--accent)}
.crumb{font-family:var(--mono);font-size:12px;color:var(--muted);letter-spacing:.04em}
.tabs{display:grid;grid-template-columns:repeat(4,1fr);gap:6px}
.tab{all:unset;box-sizing:border-box;cursor:pointer;text-align:center;padding:7px 4px;border-radius:8px;border:1px solid var(--line);font-size:12.5px;display:flex;flex-direction:column;align-items:center;gap:3px}
.tab i{width:9px;height:9px;border-radius:50%}
.tab[aria-current="step"]{border-color:var(--accent);background:var(--accentbg);font-weight:700}
.pager{display:flex;justify-content:space-between;gap:8px}
.step{all:unset;cursor:pointer;font-size:13px;color:var(--accent);padding:6px 10px;border-radius:6px;border:1px solid var(--line);max-width:48%;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.step:hover{background:var(--accentbg)} .step[disabled]{visibility:hidden}
.mini .chip::after{content:"\2192";margin-left:auto;padding-left:8px;color:var(--muted)}
.loop{display:grid;grid-template-columns:repeat(4,1fr);gap:4px}
.loop span{font-size:12px;text-align:center;padding:6px 2px;border-radius:6px;background:var(--nonebg);color:var(--muted)}
.loop span.done{background:var(--okbg);color:var(--fg)}
.loop span.now{background:var(--waitbg);color:var(--fg);font-weight:700;outline:2px solid var(--wait);outline-offset:-2px}
.fixbox{border:1px solid var(--line);border-radius:10px;padding:14px;display:grid;gap:12px}
.fixbox h4{margin:0}
.fixbox .prob{font-size:14.5px}
.help{font-size:13.5px;color:var(--muted)}
.help b{color:var(--fg)}
.row.hl{box-shadow:inset 4px 0 0 var(--accent);background:var(--accentbg)}
.tech{font-size:13px;color:var(--muted)} .tech summary{cursor:pointer}
.trail{display:grid;grid-template-columns:minmax(0,1fr);gap:8px}
.act,.actb,.pf,.pfi{min-width:0;max-width:100%}
.facts{display:flex;flex-wrap:wrap;gap:6px;margin:2px 0 8px} .facts span{font-size:12.5px;padding:3px 9px;border-radius:999px;background:var(--bg);border:1px solid var(--line)}
h5.ch{margin:6px 0 4px;font-size:12px;color:var(--muted);font-weight:600;text-transform:uppercase;letter-spacing:.04em}
ol.chg{margin:0 0 8px;padding-left:20px;display:grid;gap:6px} ol.chg small{display:block;color:var(--muted);font-family:var(--mono);font-size:11.5px}
.planbtn{display:flex;justify-content:space-between;align-items:center;width:100%;text-align:left;padding:12px 14px;border:1px solid var(--accent);border-radius:10px;background:var(--panel);color:var(--fg);font:inherit;cursor:pointer}
.planbtn b{color:var(--accent)} .planbtn:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.plan{display:grid;grid-template-columns:minmax(0,1fr);gap:14px}
.plan section>p{margin:2px 0 6px;color:var(--muted);font-size:13.5px}
.plan ul.pl{margin:0;padding-left:18px;display:grid;gap:6px} .plan ul.pl small{display:block;color:var(--muted)}
.pcard{border:1px solid var(--line);border-radius:10px;padding:10px 12px;background:var(--panel);display:grid;gap:6px;margin-bottom:8px}
.pcard .tag{font-size:12px;color:var(--muted)} .pcard .asm{color:var(--wait);font-weight:600}
.trail>p{margin:0;color:var(--muted);font-size:13.5px}
.act{border:1px solid var(--line);border-radius:10px;background:var(--panel)}
.means{border-left:4px solid var(--accent);background:var(--bg);padding:8px 12px;margin:0 0 12px;border-radius:0 8px 8px 0}.means h5{margin:0 0 4px}.means p{margin:4px 0;font-size:15px}
table.fnd{width:100%;border-collapse:collapse;margin-bottom:10px}table.fnd td{padding:8px 6px;border-top:1px solid var(--line);vertical-align:top}table.fnd td:first-child{width:14px}
table.fnd i{display:block;width:9px;height:9px;border-radius:50%;margin-top:6px;background:var(--ok)}table.fnd tr.wait i{background:var(--wait)}table.fnd tr.bad i{background:var(--bad)}
table.fnd b{overflow-wrap:anywhere}table.fnd .tg{margin-left:8px;font-size:12px;padding:1px 7px;border-radius:9px;border:1px solid var(--line);color:var(--muted);white-space:nowrap}table.fnd div{color:var(--ink,inherit);margin-top:3px;font-size:14px}
.act>summary{list-style:none;cursor:pointer;display:grid;grid-template-columns:10px minmax(0,1fr) auto;gap:10px;align-items:start;padding:10px 12px}
.act>summary::-webkit-details-marker{display:none}
.act>summary:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.act>summary i{width:10px;height:10px;border-radius:50%;margin-top:5px}
.act>summary b{display:block}
.act>summary small{color:var(--muted);display:block;font-size:13px;margin-top:2px}
.act>summary .say{color:var(--fg);font-size:13.5px;margin-top:4px;display:block}
.act>summary em{font-style:normal;font-size:12px;color:var(--muted);white-space:nowrap}
.act[open]>summary{border-bottom:1px solid var(--line)}
.actb{padding:12px;display:grid;gap:10px;font-size:14px}
.actb dl{margin:0;display:grid;grid-template-columns:110px minmax(0,1fr);gap:6px 12px}
.actb dt{color:var(--muted);font-size:13px}
.actb dd{margin:0}
.actb ul{margin:0;padding-left:18px}
.res{width:100%;border-collapse:collapse;font-size:13.5px}
.ran{width:100%;border-collapse:collapse;font-size:13px;margin:4px 0 8px}.ran th{text-align:left;font-weight:600;color:var(--muted);padding:5px 8px}.ran td{padding:6px 8px;border-top:1px solid var(--line);vertical-align:top;overflow-wrap:normal;word-break:normal;hyphens:none}.ran td:first-child,.ran th{white-space:nowrap}.ran tr.lost td{background:color-mix(in srgb,var(--bad) 10%,transparent)}
details.ctx>summary{cursor:pointer;font-weight:600;color:var(--muted);margin-bottom:6px}
.res td{padding:7px 8px;border-top:1px solid var(--line);vertical-align:top}
.res td:first-child{width:22px;padding-right:0}
.res .v{font-weight:700;white-space:nowrap}
.v.pass{color:var(--ok)} .v.fail{color:var(--bad)} .v.partly{color:var(--wait)} .v.gap{color:var(--you)}
.nl{display:inline-block;font-size:12px;color:var(--you);background:var(--youbg);border-radius:4px;padding:1px 8px}
.pf{font-size:13px} .pf>summary{cursor:pointer;color:var(--accent)}
.pfi{margin-top:8px;border:1px solid var(--line);border-radius:8px;overflow:hidden}
.pfi h5{margin:0;padding:8px 10px 0;font-size:12px;color:var(--muted);font-weight:600}
.pfi p{margin:4px 10px 8px}
.pfi pre{margin:0;padding:8px 10px;font-family:var(--mono);font-size:11.5px;line-height:1.5;white-space:pre;overflow:auto;max-height:300px;background:var(--bg);border-top:1px solid var(--line)}
.shots{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:8px;padding:8px 10px 10px}
.shots figure{margin:0} .shots img{display:block;width:100%;border:1px solid var(--line);border-radius:4px}
.shots figcaption{font-size:12px;color:var(--muted);margin-top:3px}
.tech code,.tech li{font-family:var(--mono);font-size:12px;overflow-wrap:anywhere}
.btn{justify-self:start;border:0;background:var(--accent);color:var(--panel);font:700 13px var(--sans);padding:6px 14px;border-radius:6px;cursor:pointer}
.btn[disabled]{opacity:.5;cursor:default}
.btn.sm{padding:3px 10px;font-size:12.5px}
.btn.alt{background:transparent;color:var(--accent);border:1px solid var(--line)}
.opt{display:flex;gap:8px;align-items:flex-start;cursor:pointer;margin-bottom:6px}
.opt input{margin-top:4px}
.opt small{display:block;color:var(--muted);font-size:12.5px}
.kid{display:grid;gap:4px;padding:8px 0;border-top:1px solid var(--line)}
.kid:first-child{border-top:0}
.kid .k{display:flex;gap:8px;flex-wrap:wrap;align-items:center}
.done-note{color:var(--ok)}
.stepask{display:grid;gap:8px;margin-top:10px}.stepask .why{display:grid;gap:4px;font-size:13px;color:var(--muted)}.stepask .reason{font:inherit;padding:6px 8px;border:1px solid var(--line,#ccc);border-radius:6px;background:var(--bg,#fff);color:inherit}.stepask .acts{display:flex;gap:8px;align-items:center;flex-wrap:wrap}
.m{color:var(--muted);font-size:12.5px}
.dec{display:grid;gap:8px}
.wrap{grid-template-columns:minmax(0,1fr)}
.wrap>*{min-width:0}
.head,.legend{min-width:0;max-width:100%}
.ver{overflow-wrap:anywhere}
.card.scroll{overflow-x:auto;-webkit-overflow-scrolling:touch}
#feed,#feed *{overflow-wrap:anywhere}
.nowrun{display:flex;align-items:center;gap:12px;margin:0 0 14px;padding:10px 14px;border-radius:12px;background:var(--panel);border:1px solid var(--wait);font-size:14px}
.nowrun[hidden]{display:none}
.blocked{margin:0 0 14px;padding:12px 14px;border-radius:14px;background:var(--youbg);border:2px solid var(--you)}
.blocked h2{margin:0 0 4px;font-size:17px}.blocked p{margin:0 0 8px;font-size:13px;color:var(--muted)}
.blocked ol{margin:0;padding:0;list-style:none}.blocked li{display:flex;gap:8px;align-items:center;justify-content:space-between;padding:8px 0;border-top:1px solid var(--line);font-size:14px}
.resolve{font:inherit;font-size:13px;font-weight:600;white-space:nowrap;padding:6px 10px;border-radius:9px;border:0;background:var(--you);color:#fff;cursor:pointer}
.qdlg{max-width:640px;width:calc(100% - 32px);border:0;border-radius:16px;padding:0;background:var(--panel);color:var(--fg);box-shadow:0 20px 60px rgba(0,0,0,.35)}
.qdlg::backdrop{background:rgba(0,0,0,.4)}.qcard{padding:18px 20px}.qcard.done{opacity:.6}
.qk{font:12px var(--mono);color:var(--muted)}.qcard h3{margin:4px 0 10px;font-size:19px}.qcard p{margin:6px 0;font-size:14px;line-height:1.45}
.qev{margin:10px 0;padding:10px 12px;border:1px solid var(--line,#ddd);border-radius:8px}.qev ul{margin:6px 0 4px 18px;padding:0}.qev li{margin:2px 0}.qev small{opacity:.7}
.qrec{padding:8px 10px;border-radius:10px;background:var(--accentbg)}
.qdlg.wide{max-width:1100px;width:92vw}.chead{font-size:17px!important;font-weight:600}
.ctiles{display:flex;gap:10px;margin:10px 0}.ct{flex:1;border:1px solid var(--line);border-radius:10px;padding:8px 12px;text-align:center}.ct b{display:block;font-size:28px}.ct span{font-size:13px;color:var(--muted)}
.ct.ok b{color:var(--ok)}.ct.bad b{color:var(--bad)}.ct.wait b{color:var(--wait)}
.cshot{margin:10px 0;display:grid;grid-template-columns:1fr 1fr;gap:10px}.cshot div{border:1px solid var(--line);border-radius:10px;overflow:hidden}.cshot span{display:block;font:12px var(--mono);padding:4px 8px;color:var(--muted);border-bottom:1px solid var(--line)}
.cshot img{display:block;width:100%}.cshot i{display:block;padding:30px;color:var(--muted);text-align:center}.cshot figcaption{grid-column:1/-1;font-size:13px;color:var(--muted)}
.cwh{margin:12px 0 6px}.cwhy{counter-reset:w;list-style:none;padding:0;margin:0;display:flex;gap:8px;flex-wrap:wrap}.cwhy li{counter-increment:w;flex:1 1 200px;border:1px solid var(--line);border-radius:10px;padding:8px 10px 8px 34px;position:relative;font-size:14px}
.cwhy li::before{content:counter(w);position:absolute;left:8px;top:8px;width:20px;height:20px;border-radius:50%;background:var(--accent);color:#fff;font-size:12px;text-align:center;line-height:20px}
.cdet{margin-top:8px;font-size:13px}.qopts small.catch{color:var(--wait)}
@media (max-width:700px){.cshot{grid-template-columns:1fr}.ctiles{flex-wrap:wrap}}
.qopts{display:grid;gap:8px;margin-top:12px}
.qopts button{font:inherit;font-size:14px;text-align:left;padding:10px 12px;border-radius:10px;border:1px solid var(--line);background:var(--bg);color:var(--fg);cursor:pointer}
.qopts button.rec{border:2px solid var(--accent);background:var(--accentbg)}.qopts button em{margin-left:8px;font-size:12px;font-style:normal;color:var(--accent);font-weight:600}
.qopts button small{display:block;margin-top:3px;font-size:13px;color:var(--muted)}.qopts button:disabled{cursor:default;opacity:.7}
.qmsg{margin-top:8px;font-size:13px;font-weight:600}.qhint{font-size:12px!important;color:var(--muted)}
.qclose{font:inherit;font-size:13px;margin-top:6px;padding:6px 12px;border-radius:9px;border:1px solid var(--line);background:var(--bg);color:var(--fg);cursor:pointer}
.legend .gbreak{flex-basis:100%;height:0}.legend .gl b{color:var(--fg);font-weight:600}
.stopbar{margin:0 0 14px;padding:10px 14px;border-radius:12px;background:var(--badbg);border:1px solid var(--bad);font-size:14px}
.stopbar b{color:var(--bad)}.stopbar ul{margin:6px 0;padding-left:20px}.stopbar small{display:block;color:var(--muted,#6c7a87);overflow-wrap:anywhere}
.nowrun .pulse{flex:none;width:10px;height:10px;border-radius:50%;background:var(--wait);animation:nrp 1.4s ease-in-out infinite}
@keyframes nrp{0%,100%{opacity:1}50%{opacity:.25}}
@media (prefers-reduced-motion:reduce){.nowrun .pulse{animation:none}}
.nowrun b{font-weight:600}.nowrun small{display:block;color:var(--muted,#6c7a87);overflow-wrap:anywhere}
.hero{display:grid;gap:18px;padding:20px;border-radius:14px;background:var(--panel);border:1px solid var(--line)}
.hmsg{display:flex;gap:14px;align-items:center}
.hmsg .tick{flex:none;width:44px;height:44px;border-radius:50%;display:grid;place-items:center;background:var(--ok);color:#fff;font-size:24px;font-weight:700}
.hero.neutral .tick{background:var(--none)} .hero.warn .tick{background:var(--wait)} .hero.bad .tick{background:var(--bad)}
.hmsg b{display:block;font-size:22px;text-wrap:balance}
.hmsg .rg{display:block;color:var(--muted)} .hmsg .rg.bad{color:var(--bad);font-weight:700}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(280px,100%),1fr));gap:16px}
.kpi{display:grid;gap:6px;align-content:start;padding:16px;border-radius:12px;border:1px solid var(--line);min-width:0}
.kpi>b{font-size:44px;line-height:1;font-variant-numeric:tabular-nums}
.kpi>span{color:var(--muted)}
.kpi.good>b{color:var(--ok)} .kpi.open>b{color:var(--wait)}
.ccs{display:flex;flex-wrap:wrap;gap:6px;margin-top:8px}
.cc{font-size:13px;padding:4px 8px;border-radius:8px;background:var(--okbg)}
.cc b{margin-right:5px}
.ns{display:grid;grid-template-columns:90px 1fr auto;gap:10px;align-items:baseline;padding:7px 0;border-top:1px solid var(--line);font-size:14px;overflow-wrap:anywhere}
.ns b{font-size:12px;color:var(--muted);font-weight:600}
.ns em{font-style:normal;font-size:12px;color:var(--muted)}
.layout{display:grid;grid-template-columns:minmax(0,1fr) 340px;gap:20px;align-items:start}
.main{display:grid;gap:20px;min-width:0}
.side{position:sticky;top:16px;min-width:0;max-height:calc(100vh - 32px);overflow-y:auto}
.side .hero{gap:14px;padding:16px}
.side .hmsg b{font-size:18px}
.side .kpis{grid-template-columns:1fr;gap:12px}
.side .kpi{padding:12px}
.side .kpi>b{font-size:36px}
.side .ns{grid-template-columns:1fr auto;gap:2px 8px}
.side .ns span{grid-column:1/-1;order:3}
@media (max-width:1000px){.layout{grid-template-columns:minmax(0,1fr)}.side{position:static;max-height:none;order:-1}}
details.more{padding:10px 16px}
details.more>summary{cursor:pointer;font-size:13px;color:var(--muted)}
details.more[open]>summary{margin-bottom:10px}
@media (max-width:560px){
  h1{font-size:24px}
  .hero{padding:14px}
  .hmsg b{font-size:19px}
  .ns{grid-template-columns:1fr auto}
  .ns span{grid-column:1/-1;order:3}
  .ns em{white-space:nowrap}
}
@media (prefers-reduced-motion:no-preference){.drawer{animation:in .18s ease-out}@keyframes in{from{transform:translateX(24px);opacity:.6}}}
"""

JS = r"""
const M=D.matrix, STAGES=M.stages, ROWS=M.rows, READY=M.ready, GROUPS=Object.fromEntries(M.groups.map(g=>[g.key,g.name])), LOOP=M.loop;
const $=q=>document.querySelector(q), esc=s=>String(s==null?"":s).replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
const COL={ok:"var(--ok)",wait:"var(--wait)",bad:"var(--bad)",none:"var(--none)",you:"var(--you)"};
const NONGREEN=["wait","bad","you"];
const fmt=iso=>{try{return new Date(iso).toLocaleString([],{day:"numeric",month:"short",hour:"2-digit",minute:"2-digit"})}catch(_){return iso}};
let lastSeen=null;try{lastSeen=localStorage.getItem("cockpit-last-seen")}catch(_){}
$("#feed").innerHTML=M.feed.length?M.feed.map(f=>`<li><time>${esc(fmt(f.t))}</time>${lastSeen&&f.t>lastSeen?`<span class="new">${esc(f.text)}</span>`:esc(f.text)}</li>`).join(""):`<li>Nothing recorded yet.</li>`;
try{localStorage.setItem("cockpit-last-seen",M.generated)}catch(_){}

// tiles: computed by the generator from the rows, so they never disagree with the matrix
(function(){
  const T=M.tiles;
  const fx=[T.upg[0]+T.gap[0],T.upg[1]+T.gap[1]],ts=[T.tested[0],T.tested[0]+T.tested[2]];
  $("#headline").innerHTML=`<span><b>${fx[0]}</b> of ${fx[1]} fixed</span><span><b>${ts[0]}</b> of ${ts[1]} tested</span>`+(T.tested[1]?`<span class="neutral"><b>${T.tested[1]}</b> at deploy</span>`:"")+(T.reg===null?"":`<span class="${T.reg?"bad":""}"><b>${T.reg}</b> regressions</span>`);
  const KT=(k,v,t)=>{const n=Array.isArray(v),cls=n?(v[1]&&v[0]===v[1]?"good":"warn"):(k==="owner"&&T.you?"you":"neutral");return `<button class="tile kind ${cls}" type="button" data-kind="${k}" aria-pressed="false"><b>${n?v[0]+"/"+v[1]:v}</b><span>${t}${k==="owner"&&T.you?` · ${T.you} need you`:""}</span></button>`};
  $("#tiles").innerHTML=
   `<div class="tile ${T.up[1]&&T.up[0]===T.up[1]?"good":"warn"}"><b>${T.up[0]}/${T.up[1]}</b><span>upgrade items done</span></div>`+
   (T.reg===null?`<div class="tile"><b>not yet</b><span>regressions</span></div>`:`<div class="tile ${T.reg?"bad":"good"}"><b>${T.reg}</b><span>regressions</span></div>`)+
   KT("upgrade",T.upg,"upgrade problems solved")+KT("testgap",T.gap,"test gaps closed")+KT("owner",T.own,"your tasks")+KT("golive",T.gol,"at go-live");
})();

function fixBox(f,need){
  if(!f)return need?`<div class="fixbox"><h4>Proposed solution</h4><div class="box">No proposal yet.</div></div>`:"";
  const lp=f.loop===null||f.loop===undefined?-1:f.loop;
  return `<div class="fixbox"><h4>Proposed solution</h4>
   ${lp>=0?`<div class="loop" aria-label="Improvement loop">${LOOP.map((x,j)=>`<span class="${j<lp?"done":j===lp?"now":""}">${x}</span>`).join("")}</div>`:""}
   ${f.problem?`<div class="prob"><b>Problem:</b> ${esc(f.problem)}</div>`:""}
   ${f.proposal?`<div class="prob"><b>Proposal:</b> ${esc(f.proposal)}</div>`:`<div class="box">No proposal yet.</div>`}
   ${f.steps&&f.steps.length?ol(f.steps):""}
   ${f.result?`<div class="box">${esc(f.result)}</div>`:""}
   <div class="help"><b>How you can help:</b> ${esc(f.help||"Nothing needed.")}</div>
   ${f.learn?`<div class="help"><b>Toolkit learns:</b> ${esc(f.learn)}</div>`:""}</div>`;
}
const techBox=a=>a&&a.length?`<details class="tech"><summary>Technical details</summary><ul>${a.map(x=>`<li>${esc(x)}</li>`).join("")}</ul></details>`:`<details class="tech"><summary>Technical details</summary><p>No technical record for this cell.</p></details>`;

let pf=null, kf=null, active=null, hlRow=-1, hist=[], cur=null, lastFocus=null;
function render(){
  let h=`<div class="row hd"><div class="hcell">Item</div>`+STAGES.map(s=>`<button class="stage" type="button" data-stage="${s.key}" aria-pressed="${active===s.key}"><span><span class="n">${s.n}</span>${esc(s.name)}</span><small>${esc(s.sub)}</small><span class="more">How this stage works →</span></button>`).join("")+`</div>`;
  let g="";
  ROWS.forEach((it,i)=>{
    if(pf&&it.phase&&it.phase!==pf)return;   // a two-version upgrade: rows of the other version are hidden, rows of the whole run stay
    if(it.group!==g){g=it.group;h+=`<div class="grp">${esc(GROUPS[g])}</div>`;}
    h+=`<div class="row${hlRow===i?" hl":""}${kf?(it.kind===kf?" kin":" dim"):""}" id="r${i}"><div class="item">${esc(it.name)}<small>${esc(it.sub)}${it.phase&&!pf?` · Mendix ${esc(it.phase)}`:""}</small></div>`+
      STAGES.map(s=>{const c=it.cells[s.key];return `<div class="cell${active===s.key?" on":""}"><button class="chip ${c.s}" type="button" data-i="${i}" data-s="${s.key}"><span>${esc(c.l)}${c.d?`<small class="cd">${esc(c.d)}</small>`:""}</span></button></div>`}).join("")+`</div>`;
  });
  $("#matrix").innerHTML=h;
  const pb=$("#phases"); if(pb&&M.phases&&M.phases.length>1){const n=v=>ROWS.filter(r=>r.phase===v).length;
    pb.hidden=false;pb.innerHTML=`<span class="plbl">Version</span>`+[null,...M.phases].map(v=>`<button class="chip${pf===v?" on":""}" type="button" data-phase="${v||""}" aria-pressed="${pf===v}">${v?`Mendix ${esc(v)} <b>${n(v)}</b>`:"Both versions"}</button>`).join("");}
}
function renderReady(){const m=c=>kf?(c.kind===kf?" kin":" dim"):"";$("#ready").innerHTML=READY.map(c=>c.s==="ok"?`<span class="chip ok${m(c)}">${esc(c.l)}</span>`:`<button class="chip ${c.s}${m(c)}" type="button" data-ready="${esc(c.id)}">${esc(c.l)} →</button>`).join("");}
renderReady();
render();

const VIEW={stage:k=>stagePanel(k),cell:(i,k)=>cellPanel(i,k),you:()=>youPanel(),ready:id=>readyPanel(id),plan:i=>planPanel(i)};
const label=v=>v[0]==="stage"?STAGES.find(s=>s.key===v[1]).name+" stage":v[0]==="you"?"Needs you":v[0]==="ready"?"Readiness":v[0]==="plan"?(v[1]!=null&&ROWS[v[1]]?"Plan: "+ROWS[v[1]].name:"The proposed plan"):ROWS[v[1]].name;
function go(v,push=true){
  if(push&&!$("#drawer").hidden&&cur)hist.push(cur);
  cur=v; VIEW[v[0]](v[1],v[2]);
}
function navBar(crumb){
  const prev=hist[hist.length-1];
  return `<div class="nav">${prev?`<button class="back" type="button" data-back>← ${esc(label(prev))}</button>`:""}<span class="crumb">${crumb}</span></div>`;
}
function open(html){if($("#drawer").hidden)lastFocus=document.activeElement;$("#dBody").innerHTML=html;$("#drawer").hidden=false;$("#shade").hidden=false;$("#drawer").scrollTop=0;$("#dClose").focus();}
function close(){$("#drawer").hidden=true;$("#shade").hidden=true;active=null;hlRow=-1;hist=[];cur=null;render();lastFocus&&lastFocus.focus&&lastFocus.focus();}
const ol=a=>`<ol class="steps">${a.map(x=>`<li><span>${esc(x)}</span></li>`).join("")}</ol>`;
const cellChip=(it,i,k)=>{const c=it.cells[k];return `<button class="chip ${c.s}" type="button" data-i="${i}" data-s="${k}"><span><b>${esc(it.name)}</b> · ${esc(c.l)}</span></button>`};

function stagePanel(k){
  const s=STAGES.find(x=>x.key===k);active=k;hlRow=-1;render();
  const tabs=STAGES.map(x=>`<button class="tab" type="button" data-stage="${x.key}"${x.key===k?' aria-current="step"':''}>${x.n} ${esc(x.name)}</button>`).join("");
  open(`${navBar("How the stages work")}<div class="tabs">${tabs}</div><h3>Stage ${s.n}: ${esc(s.name)}</h3>
   <div class="box">${esc(s.what)}</div>
   <div><h4>Step by step</h4>${ol(s.steps)}</div>
   <div><h4>How we run it</h4><div class="box">${esc(s.run)}</div></div>
   <div><h4>Your part</h4><div class="box youbox">${esc(s.you)}</div></div>
   ${k==="test"?ranBox():""}
   <div><h4>Every item in this stage</h4><div class="mini">${ROWS.map((it,i)=>cellChip(it,i,k)).join("")}</div></div>`);
}
function decBox(di){
  if(!di)return "";
  return `<div class="box youbox dec"><div><b>${esc(di.title)}</b></div><div>${esc(di.problem||"")}</div>${di.kind==="confirmgroup"||!di.rec_text?"":`<div><b>Recommended:</b> ${esc(di.rec_text)}</div>`}<div id="c-${esc(di.id)}"></div></div>`;
}
const TSAY={triage:"What we found",plan:"What we proposed",upgrade:"What changed in the app",test:"How we checked it"};
const TCOL={done:"var(--ok)",kept:"var(--accent)",open:"var(--wait)"};
const TLBL={done:"done",kept:"kept on purpose",open:"open"};
const VW={pass:"PASS",fail:"FAIL",partly:"PARTLY",gap:"NOT LINKED"};
function pfItem(p){
  if(p.kind==="decision"){const c=p.cells||[];return `<div class="pfi"><h5>${esc(c[0])}, from AGENT-DECISIONS.md</h5><p><b>${esc(c[1])}</b></p>${c.slice(2).filter(Boolean).map(v=>`<p>${esc(v)}</p>`).join("")}</div>`;}
  if(p.kind==="quote")return `<div class="pfi"><h5>${esc(p.src)}</h5><pre>${esc(p.text)}</pre></div>`;
  if(p.kind==="commit")return `<div class="pfi"><h5>Commit ${esc(p.h)} · ${esc(p.d||"")}</h5><p><b>${esc(p.s)}</b></p>${p.body?`<p>${esc(p.body)}</p>`:""}${p.stat?`<pre>${esc(p.stat)}</pre>`:""}</div>`;
  return `<div class="pfi"><h5>${esc(p.src)}</h5>${p.how?`<p>${esc(p.how)}</p>`:""}${p.text?`<pre>${esc(p.text)}</pre>`:""}${(p.imgs||[]).length?`<div class="shots">${p.imgs.map(m=>`<figure><img ${"sr"+"c"}="${m.src}" alt="${esc(m.cap)}"><figcaption>${esc(m.cap)}</figcaption></figure>`).join("")}</div>`:""}</div>`;
}
function trailBox(it,k){
  if(!it.trail||!it.trail.length)return "";
  const acts=it.trail.map(a=>{const t=a.stages[k]||{};let b="";
    if(k==="plan"){b=`<dl>${t.why?`<dt>Why</dt><dd>${esc(t.why)}</dd>`:""}${t.who?`<dt>Who decided</dt><dd>${esc(t.who)}</dd>`:""}${(t.options||[]).length?`<dt>Other options</dt><dd><ul>${t.options.map(o=>`<li>${esc(o)}</li>`).join("")}</ul></dd>`:""}</dl>`;}
    if(k==="upgrade"){const cs=(t.proof||[]).filter(p=>p.kind==="commit");
      b=`${(t.facts||[]).length?`<div class="facts">${t.facts.map(f=>`<span>${esc(f)}</span>`).join("")}</div>`:""}${cs.length?`<h5 class="ch">Changes in the app (${cs.length})</h5><ol class="chg">${cs.map(c=>`<li><span>${esc(c.s.replace(/^[\w ./-]+?: /,""))}</span><small>${esc(c.h)}${c.d?" · "+esc(c.d):""}</small></li>`).join("")}</ol>`:""}`;}
    if(k==="triage"&&((t.means||[]).length||(t.items||[]).length)){const ni=(t.items||[]).filter(x=>x[2]!=="ok").length;
      b=`${(t.means||[]).length?`<div class="means"><h5>What it means</h5>${t.means.map(x=>`<p>${esc(x)}</p>`).join("")}</div>`:""}${(t.items||[]).length?`<h5 class="ch">What we found, item by item (${t.items.length}${ni?`, ${ni} to look at`:""})</h5><table class="fnd">${t.items.slice().sort((p,q)=>(p[2]==="ok")-(q[2]==="ok")).map(x=>`<tr class="${esc(x[2])}"><td><i></i></td><td><b>${esc(x[0])}</b><span class="tg">${esc(x[1])}</span><div>${esc(x[3])}</div></td></tr>`).join("")}</table>`:""}`;}
    if(k==="test"&&(t.results||[]).length)b=`<table class="res">${t.results.map(r=>`<tr><td><i style="display:block;width:8px;height:8px;margin-top:6px;border-radius:50%;background:${r[1]==="pass"?"var(--ok)":r[1]==="fail"?"var(--bad)":r[1]==="partly"?"var(--wait)":"var(--you)"}"></i></td><td>${esc(r[0])}<br><span style="color:var(--muted)">${esc(r[2])}</span></td><td class="v ${esc(r[1])}">${VW[r[1]]||esc(r[1])}</td></tr>`).join("")}</table>`;
    const pf=(t.proof||[]).length?`<details class="pf"><summary>Show the proof (${t.proof.length})</summary>${t.proof.map(pfItem).join("")}</details>`:`<p style="color:var(--muted);margin:0">No file in the run backs this up.</p>`;
    return `<details class="act"${it.fromSteps&&it.trail.length===1?" open":""}><summary><i style="background:${TCOL[a.status]||"var(--none)"}"></i><span><b>${esc(a.name)}</b><small>${esc(a.sub)}</small><span class="say">${esc(t.say||"")}${t.gap?' <span class="nl">not linked</span>':""}</span></span><em>${TLBL[a.status]||""}</em></summary><div class="actb">${b}${pf}</div></details>`;}).join("");
  return `<div class="trail"><h4>${TSAY[k]}, per action (${it.trail.length})</h4><p>Open an action for the reasons and the result. The proof is the record from the run itself.</p>${acts}</div>`;
}
const STORY=[["found","What we found"],["means","What it means for this app"],["plan","What the plan does, and why"]];
// the same context shows on every stage tab: one click hides it everywhere, and the page remembers it (the owner, 2026-11-17)
let ctxOpen=null;try{const v=localStorage.getItem("cockpit-ctx");if(v!==null)ctxOpen=v==="1";}catch(e){}
const storyBox=(it,k)=>{const s=it.story||{};const b=STORY.filter(([k])=>(s[k]||[]).length);
  const op=ctxOpen===null?k==="triage":ctxOpen;
  return b.length?`<details class="ctx"${op?" open":""}><summary>Context: ${b.map(([,h])=>h.toLowerCase()).join(", ")}</summary><div class="story">${b.map(([k,h])=>`<section><h4>${h}</h4>${s[k].map(t=>`<p>${esc(t)}</p>`).join("")}</section>`).join("")}</div></details>`:"";};
document.addEventListener("toggle",e=>{if(e.target.matches&&e.target.matches("details.ctx")){ctxOpen=e.target.open;try{localStorage.setItem("cockpit-ctx",ctxOpen?"1":"0");}catch(x){}}},true);
// what actually ran in the Test stage, on the old and on the new app (test_runs in cockpitmatrix.py)
function ranBox(){const R=M.ran||{rows:[],lists:{}};if(!R.rows.length)return "";
  const lost=r=>r[1]==="passed"&&r[2]!=="passed"&&r[2]!=="not run";
  const lst=Object.entries(R.lists).map(([k,l])=>{const nl=l.filter(lost).length;
    return `<details class="pf"><summary>Every ${esc(k.toLowerCase())} test, old and new (${l.length}${nl?`, ${nl} passed on the old app only`:""})</summary><table class="ran"><tr><th>Test</th><th>Old app</th><th>New app</th></tr>${l.slice().sort((a,b)=>lost(b)-lost(a)).map(r=>`<tr${lost(r)?' class="lost"':""}><td>${esc(r[0])}</td><td>${esc(r[1])}</td><td>${esc(r[2])}</td></tr>`).join("")}</table></details>`;}).join("");
  return `<div><h4>What ran, on the old and the new app</h4><table class="ran"><tr><th>Check</th><th>Old app</th><th>New app</th><th>Compared</th></tr>${R.rows.map(r=>`<tr><td><b>${esc(r[0])}</b></td><td>${esc(r[1])}</td><td>${esc(r[2])}</td><td>${esc(r[3])}</td></tr>`).join("")}</table>${lst}</div>`;}
const planBtn=i=>(M.plan||[]).length?`<button class="planbtn" type="button" data-plan="${i}"><span>The proposed plan for ${esc(ROWS[i].name)}<br><span style="color:var(--muted);font-size:13px">Each step that was proposed, why, who decided and the other options</span></span><b>Read →</b></button>`:"";
function topicPlan(it){
  const acts=(it.trail||[]).map(a=>{const t=a.stages.plan||{};
    return `<div class="pcard"><span class="tag">${esc(a.sub||"")}</span><b>${esc(a.name)}</b><div>${esc(t.say||"")}${t.gap?' <span class="nl">not linked</span>':""}</div>
     ${t.why?`<div><b>Why:</b> ${esc(t.why)}</div>`:""}${t.who?`<div><b>Who decided:</b> ${esc(t.who)}</div>`:""}
     ${(t.options||[]).length?`<details class="pf"><summary>Other options (${t.options.length})</summary><ul>${t.options.map(o=>`<li>${esc(o)}</li>`).join("")}</ul></details>`:""}
     ${(t.proof||[]).length?`<details class="pf"><summary>Show the proof (${t.proof.length})</summary>${t.proof.map(pfItem).join("")}</details>`:""}</div>`;}).join("");
  return `${propBox(it)}${acts?`<div><h4>Proposed steps (${it.trail.length})</h4>${acts}</div>`:""}`;
}
function planPanel(i){
  const it=i!=null?ROWS[i]:null;
  if(it){active="plan";hlRow=i;render();}else{active="plan";hlRow=-1;render();}
  active="plan";hlRow=-1;render();
  const sub=s=>s.map(([k,v])=>`<small>${k?esc(k)+": ":""}${esc(v)}</small>`).join("");
  const card=it=>{const g=Object.fromEntries(it.subs.filter(x=>x[0]));const ans=g.answer||"";const asm=/ASSUMED/.test(ans);
    return `<div class="pcard"><span class="tag">${esc(it.id)} · ${esc(it.kind)}</span><b>${esc(it.name)}</b>
     ${g.recommendation?`<div><b>Recommended:</b> ${esc(g.recommendation)}</div>`:""}
     ${ans?`<div><b>Answer:</b> ${esc(ans.replace(/\s*\(ASSUMED[^)]*\)\)?$/,""))} ${asm?'<span class="asm">· assumed by the agent, not yet confirmed by a person</span>':""}</div>`:""}
     ${g.options?`<details class="pf"><summary>Other options</summary><ul>${g.options.split(" | ").map(o=>`<li>${esc(o)}</li>`).join("")}</ul></details>`:""}
     ${g.evidence?`<details class="pf"><summary>Why this came up</summary><p>${esc(g.evidence)}</p></details>`:""}</div>`;};
  const secs=M.plan.map(s=>`<section>${s.sub?`<h4 style="font-size:13px">${esc(s.h)}</h4>`:`<h4>${esc(s.h)}</h4>`}${s.intro.map(t=>`<p>${esc(t)}</p>`).join("")}
    ${s.items.some(x=>x.id)?s.items.map(card).join(""):s.items.length?`<ul class="pl">${s.items.map(x=>`<li>${esc(x.text)}${sub(x.subs)}</li>`).join("")}</ul>`:""}</section>`).join("");
  const whole=`<div class="box">Written by the toolkit from triage, before anything in the app changed. This is the plan as it stands in PROPOSAL.md.</div><div class="plan">${secs}</div>`;
  if(it)open(`${navBar(esc(it.name)+" › Proposed plan")}<h3>The proposed plan for ${esc(it.name)}</h3><div class="plan">${topicPlan(it)}</div><details class="pf" style="margin-top:12px"><summary>The whole plan, all topics</summary>${whole}</details>`);
  else open(`${navBar("The proposed plan")}<h3>The proposed plan</h3>${whole}`);
}
function planFor(it){
  // the lines of PROPOSAL.md that are about this row: by row name, sub-line or the name of one of its actions
  const keys=[it.name].concat((it.trail||[]).map(a=>a.name)).map(x=>x.toLowerCase()).filter(x=>x.length>3);
  const hits=[];
  (M.plan||[]).forEach(s=>s.items.forEach(x=>{const t=(x.name||x.text).toLowerCase(),nm=(x.name||"").toLowerCase();if(keys.some(kk=>t.includes(kk)||(nm.length>3&&kk.split(/[\s:,]+/).includes(nm))))hits.push([s.h,x]);}));
  return hits;
}
function propBox(it){
  const sign=(M.plan||[]).find(s=>/sign-off/i.test(s.h)), st=sign?sign.intro.filter(t=>/^(Status:|Signed-off:)/.test(t)&&!t.includes("<")).pop()||"":"";
  const signed=/^Signed-off:/.test(st);
  const hits=it.id==="runtime"?(M.plan||[]).filter(s=>/summary/i.test(s.h)).flatMap(s=>s.items.map(x=>[s.h,x]))
    :it.id==="modules"?(M.plan||[]).flatMap(s=>s.items.filter(x=>/^module update /.test(x.text||"")).map(x=>[s.h,x])):planFor(it);
  const rows=hits.map(([h,x])=>{const g=Object.fromEntries(x.subs.filter(y=>y[0]));const asm=/ASSUMED/.test(g.answer||"");
    return `<li><span class="tag" style="font-size:12px;color:var(--muted)">${esc(h)}${x.id?" · "+esc(x.id):""}</span><br>${esc(x.name||x.text)}${g.recommendation?`<small style="display:block"><b>Recommended:</b> ${esc(g.recommendation)}</small>`:""}${g.answer?`<small style="display:block"><b>Answer:</b> ${esc(g.answer.replace(/\s*\(ASSUMED[^)]*\)\)?$/,""))}${asm?' <span class="asm" style="color:var(--wait);font-weight:600">· assumed by the agent</span>':""}</small>`:""}</li>`;}).join("");
  const who=signed?`Approved: ${esc(st.replace(/^Signed-off:\s*/,""))}`:`<span style="color:var(--wait);font-weight:600">Not approved yet.</span> The plan's sign-off line says "${esc(st||"no status")}".`;
  return `<div class="box youbox"><h4 style="margin-top:0">From the proposed plan</h4>${rows?`<ul class="pl" style="margin:0;padding-left:18px;display:grid;gap:6px">${rows}</ul>`:`<p style="margin:0">The plan has no line for this item. It was decided during the run, see the actions below.</p>`}<p style="margin:8px 0 0">${who}</p></div>`;
}
function cellPanel(i,k){
  const it=ROWS[i],s=STAGES.find(x=>x.key===k),c=it.cells[k];active=k;hlRow=i;render();
  const r=document.getElementById("r"+i); r&&r.scrollIntoView({block:"center",behavior:matchMedia("(prefers-reduced-motion:reduce)").matches?"auto":"smooth"});
  const tabs=STAGES.map(x=>`<button class="tab" type="button" data-i="${i}" data-s="${x.key}" data-swap${x.key===k?' aria-current="step"':''}><i style="background:${COL[it.cells[x.key].s]}"></i>${x.n} ${esc(x.name)}</button>`).join("");
  const p=ROWS[i-1],n=ROWS[i+1], di=c.dec&&D.items.find(x=>x.id===c.dec);
  open(`${navBar(esc(it.name)+" › "+esc(s.name))}
   <div class="tabs" aria-label="Stages of this item">${tabs}</div>
   <h3>${esc(c.l)}</h3>
   ${storyBox(it,k)}
   ${k==="plan"&&!it.fromSteps?propBox(it)+planBtn(i):""}
   ${k==="plan"&&it.fromSteps&&it.ask?`<div class="box youbox"><b>Needs your OK.</b> The agent chose this on its own while it worked. Nothing is final until a person approves it.<div class="stepask" id="sc-${esc(it.id)}"></div></div>`:""}
   ${k==="plan"&&it.fromSteps&&it.ans?`<div class="done-note">${it.ans.state==="approved"?"Approved":"Rejected"} by ${esc(who(it.ans.by))}${it.ans.day?" on "+esc(it.ans.day):""}.${it.ans.reason?" Reason: "+esc(it.ans.reason):""}</div>`:""}
   <div><h4>This stage, step by step</h4>${ol(c.steps.length?c.steps:["Nothing recorded for this cell."])}</div>
   ${k==="test"?ranBox():""}
   ${trailBox(it,k)}
   ${decBox(di)}
   ${it.trail&&it.trail.length||(it.story&&(it.story.plan||[]).length&&!it.fix)?"":fixBox(it.fix,NONGREEN.includes(c.s)&&!di)}
   ${c.late?`<div class="box">For the toolkit: triage did not flag this item. The new triage checks it from the start.</div>`:""}
   <div class="pager"><button class="step" type="button" data-i="${i-1}" data-s="${k}" data-swap ${p?"":"disabled"}>← ${p?esc(p.name):""}</button><button class="step" type="button" data-i="${i+1}" data-s="${k}" data-swap ${n?"":"disabled"}>${n?esc(n.name):""} →</button></div>
   ${techBox((it.tech||[]).concat(c.tech||[]))}`);
  if(di)ctrl(di);
  if(it.fromSteps&&it.ask)stepCtl(it);
}
function readyPanel(id){
  const c=READY.find(x=>x.id===id);
  if(c.row){const i=ROWS.findIndex(x=>x.id===c.row);const k=(STAGES.find(s=>NONGREEN.includes(ROWS[i].cells[s.key].s))||STAGES[3]).key;return cellPanel(i,k);}
  active=null;hlRow=-1;render();
  open(`${navBar("Readiness › "+esc(c.name))}<h3>${esc(c.l)}</h3>${fixBox(c.fix,true)}${techBox(c.tech)}`);
}
function youPanel(){
  active=null;hlRow=-1;render();
  const rows=ROWS.map((it,i)=>STAGES.filter(s=>it.cells[s.key].s==="you").map(s=>`<button class="chip you" type="button" data-i="${i}" data-s="${s.key}"><span><b>${esc(it.name)}</b> · ${esc(it.cells[s.key].l)}</span></button>`).join("")).join("");
  const n=M.tiles.you;
  open(`${navBar("Your part")}<h3>${n===0?"Nothing needs you":n===1?"1 thing needs you":n+" things need you"}</h3><div class="box">Everything else is assumed or fixed by the agent. Open one, then use ← to come back here.</div><div class="mini">${rows}</div>`);
}
document.addEventListener("click",e=>{
  const inDrawer=!!e.target.closest("#drawer");
  if(e.target.closest("button.btn")){const b=e.target.closest("button.btn");if(!b.disabled){if(b.dataset.sid)decideStep(b);else if(b.dataset.kid)decideKid(b);else{const it=NEED.find(i=>i.id===b.dataset.id);if(it)decide(it,b)}}return;}
  const pb=e.target.closest("[data-plan]"); if(pb){if(!inDrawer)hist=[];go(["plan",pb.dataset.plan===""?null:+pb.dataset.plan]);return;}
  if(e.target.closest("[data-back]")){const v=hist.pop();if(v)go(v,false);return;}
  const st=e.target.closest("[data-stage]"); if(st){if(!inDrawer)hist=[];go(["stage",st.dataset.stage],!st.matches(".tab"));return;}
  const ch=e.target.closest("[data-i]"); if(ch){if(!inDrawer)hist=[];go(["cell",+ch.dataset.i,ch.dataset.s],!ch.hasAttribute("data-swap"));return;}
  const ph=e.target.closest("[data-phase]"); if(ph){pf=ph.dataset.phase||null;render();return;}
  const kb=e.target.closest("[data-kind]");
  if(kb){kf=kf===kb.dataset.kind?null:kb.dataset.kind;document.querySelectorAll("[data-kind]").forEach(b=>b.setAttribute("aria-pressed",String(b.dataset.kind===kf)));renderReady();render();if(kf==="owner"&&M.tiles.you){hist=[];go(["you"]);return;}const f=document.querySelector(".row.kin,.chip.kin");if(f)f.scrollIntoView({block:"nearest"});return;}
  const rd=e.target.closest("[data-ready]"); if(rd){hist=[];go(["ready",rd.dataset.ready]);return;}
  if(e.target.id==="shade"||e.target.closest("#dClose"))close();
});
document.addEventListener("keydown",e=>{if(e.key==="Escape"&&!$("#drawer").hidden)close();});

// ---- decisions: the owner's answers go to the artifact db; the pipeline reads them at its next step ----
let db=null,user=null,me=null;
const decided={},signed={};   // item -> {choice,by,at,source}; user id -> {plan,at,source}
const NEED=D.items.filter(i=>!i.hidden);
function who(by){return me&&by===me?"you":by}
function kids(it){
  const can=db&&user&&me;
  return it.children.map(cid=>{
    const ch=D.items.find(x=>x.id===cid);if(!ch)return"";
    const d=decided[cid]||ch.decided;
    const t=`<div class="m">${(ch.tech||[]).map(esc).join("<br>")}</div>`;
    let act="";
    if(d)act=`<span class="done-note">${d.choice==="reject"?"Rejected":"Accepted"} by ${esc(who(d.by))}, waiting for the pipeline.</span>`;
    else if(can)act=`<button class="btn sm" data-kid="${esc(cid)}" data-choice="accept">Accept</button><button class="btn sm alt" data-kid="${esc(cid)}" data-choice="reject">Reject</button><span class="m" data-msg></span>`;
    return `<div class="kid"><div class="k"><b>${esc(ch.title)}</b>${act}</div>${t}</div>`}).join("")
    +(can?"":`<div>Sign in to this page to accept or reject.</div>`);
}
function ctrl(it){
  const el=$("#c-"+CSS.escape(it.id));if(!el)return;
  if(it.kind==="confirmgroup"){el.innerHTML=kids(it);return}
  const d=decided[it.id]||it.decided;
  const sg=it.kind==="signoff"?Object.values(signed).find(s=>s.plan===D.planHash)||(D.signed?{by:D.signed[0]}:null):null;
  if(sg){const nm=sg.by||(sg._id&&sg._id===me?"you":"");el.innerHTML=`<div class="done-note">Signed${nm?" by "+esc(nm):""}, waiting for the pipeline.</div>`;return}
  if(d&&it.kind!=="signoff"){el.innerHTML=`<div class="done-note">Decided by ${esc(who(d.by))} (${esc((it.options.find(o=>o.key===d.choice)||{label:d.choice}).label)}), waiting for the pipeline.</div>`;return}
  if(!db||!user||!me){el.innerHTML=`<div>${it.options.filter(o=>o.key!==it.rec).map(o=>`<div>Or: ${esc(o.label)}</div>`).join("")}</div><div>Sign in to this page to decide.</div>`;return}
  const name="o-"+it.id;
  el.innerHTML=(it.kind==="signoff"?"":it.options.map(o=>`<label class="opt"><input type="radio" name="${esc(name)}" value="${esc(o.key)}"${o.key===it.rec?" checked":""}><span>${esc(o.label)}${o.key===it.rec?" (recommended)":""}${o.causes?`<small>${esc(o.causes)}</small>`:""}</span></label>`).join(""))
    +`<button class="btn" data-id="${esc(it.id)}">${it.kind==="signoff"?"Read and sign":"Confirm"}</button><span class="m" data-msg></span>`;
}
function stepCtl(it){
  const el=document.getElementById("sc-"+it.id);if(!el)return;
  const d=decided[it.id];
  if(d&&(d.choice==="approve"||d.choice==="reject")){el.innerHTML=`<div class="done-note">${d.choice==="reject"?"Rejected":"Approved"} by ${esc(who(d.by))}${d.at?" on "+esc(d.at.slice(0,10)):""}${d.reason?". Reason: "+esc(d.reason):""}. Waiting for the pipeline.</div>`;return}
  const can=!!(window.UPG_LIVE||(db&&user&&me));   // the live cockpit saves through its own server (cockpitserve.py /decide)
  el.innerHTML=`<label class="why">Reason (optional)<input type="text" class="reason" maxlength="200" placeholder="Why you decided this"${can?"":" disabled"}></label><div class="acts"><button class="btn sm" type="button" data-sid="${esc(it.id)}" data-choice="approve"${can?"":" disabled"}>Approve</button><button class="btn sm alt" type="button" data-sid="${esc(it.id)}" data-choice="reject"${can?"":" disabled"}>Reject</button><span class="m" data-msg>${can?"":"Sign in to this page to answer."}</span></div>`;
}
async function decideStep(btn){
  const box=btn.closest(".stepask");const msg=box.querySelector("[data-msg]");box.querySelectorAll("button").forEach(b=>b.disabled=true);
  try{
    const why=box.querySelector(".reason").value.trim();
    if(window.UPG_LIVE){   // cold test WM1: the step buttons only knew the hosted page's database and stayed grey in the live cockpit
      const r=await fetch("decide",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(Object.assign({item:btn.dataset.sid,choice:btn.dataset.choice},why?{reason:why}:{}))});
      const t=await r.text();if(!r.ok)throw new Error(t||r.status);
      msg.textContent=t+" The agent picks it up within 15 seconds.";
      setTimeout(()=>location.reload(),1200);return;}   // the server rerendered the page before it answered; the item leaves Blocked on you
    const row={item:btn.dataset.sid,choice:btn.dataset.choice,by:await user.id(),at:new Date().toISOString(),source:"page"};
    if(why)row.reason=why;
    await db.collection("decisions").doc(row.item).set(row);
    msg.textContent="Saved.";
  }catch(e){box.querySelectorAll("button").forEach(b=>b.disabled=false);msg.textContent="Could not save: "+(e&&e.message?e.message:e)}
}
async function decideKid(btn){
  btn.disabled=true;const msg=btn.parentNode.querySelector("[data-msg]");
  try{
    await db.collection("decisions").doc(btn.dataset.kid).set({item:btn.dataset.kid,choice:btn.dataset.choice,by:await user.id(),at:new Date().toISOString(),source:"page"});
    if(msg)msg.textContent="Saved.";
  }catch(e){btn.disabled=false;if(msg)msg.textContent="Could not save: "+(e&&e.message?e.message:e)}
}
async function decide(it,btn){
  btn.disabled=true;const msg=btn.parentNode.querySelector("[data-msg]");
  try{
    const at=new Date().toISOString();
    if(it.kind==="signoff"){await db.collection("signoffs").doc(await user.id()).set({plan:D.planHash,at,source:"page"})}
    else{
      const r=btn.parentNode.querySelector("input:checked");const choice=r?r.value:it.rec;
      await db.collection("decisions").doc(it.id).set({item:it.id,choice,by:await user.id(),at,source:"page"});
    }
    if(msg)msg.textContent="Saved.";
  }catch(e){btn.disabled=false;if(msg)msg.textContent="Could not save: "+(e&&e.message?e.message:e)}
}
(async()=>{
  try{ if(window.claude&&claude.use){db=await claude.use("db");user=await claude.use("user")} }catch(_){db=null;user=null}
  if(!db||!user){NEED.forEach(ctrl);return}
  try{me=await user.id()}catch(_){me=null}
  if(!me){NEED.forEach(ctrl);return}
  NEED.forEach(ctrl);ROWS.forEach(r=>{if(r.fromSteps&&r.ask)stepCtl(r)});
  const err=()=>{};
  db.collection("decisions").onSnapshot(s=>{s.docs.forEach(d=>{const v=d.data();if(v&&v.item)decided[v.item]=v});NEED.forEach(ctrl);ROWS.forEach(r=>{if(r.fromSteps&&r.ask)stepCtl(r)})},err);
  db.collection("signoffs").onSnapshot(s=>{s.docs.forEach(d=>{const v=d.data();if(v)signed[d.id]=Object.assign({_id:d.id},v)});NEED.forEach(ctrl)},err);
})();
"""


# ---- static markup: the same HTML the script draws, so the page reads without JavaScript ----
E = html.escape
LEGEND = [("ok", "done / passed"), ("wait", "next step, owner named"), ("you", "needs you"), ("bad", "problem"), ("none", "not applicable or not checked")]


def h_ladder(L):
    """The version route as a row of version chips: done green, now amber, next grey."""
    if not L:
        return ""
    cls = {"done": "ok", "now": "wait", "next": "none"}
    parts = [f'<span class="lv {cls[x["state"]]}"><b>Mendix {E(".".join(x["v"].split(".")[:3]))}</b><small>{E(x["say"])}</small></span>' for x in L]
    return '<div class="ladder" aria-label="Version route"><div class="lrow">' + '<span class="la">→</span>'.join(parts) + "</div></div>"


def h_health(H):
    """How the tests improved: per version the heal rounds, the click paths judged and the actions covered."""
    if not H:
        return ""
    out = []
    for h in H:
        rows = []
        if h["paths"]:
            ok, bad, nj = h["paths"]
            tot = max(ok + bad + nj, 1)
            rows.append(f'<div class="hrow"><span>Click paths</span><div class="bar"><i class="ok" style="width:{100*ok/tot:.1f}%"></i><i class="bad" style="width:{100*bad/tot:.1f}%"></i><i class="none" style="width:{100*nj/tot:.1f}%"></i></div>'
                        f'<em>{ok} pass · {bad} fail · {nj} not judged yet</em></div>')
        for r in h["rounds"]:
            rows.append(f'<div class="hrow"><span>Heal round {r["n"]}</span><div class="num"><b>{r["fixed"]}</b> tests repaired</div><em>{r["left"]} findings still explained one by one</em></div>')
        if h["actions"]:
            f_, g_ = h["actions"]
            rows.append(f'<div class="hrow"><span>Test of the tests</span><div class="bar"><i class="ok" style="width:{100*g_/max(f_,1):.1f}%"></i></div><em>{g_} of {f_} actions have a generated click path</em></div>')
        why = [f"{h[k]} {t}" for k, t in (("real", "real problems on the new app"), ("setup", "test setup issues"),
                                            ("noise", "start noise, also on the old app"), ("nopath", "actions with no click path yet")) if h[k]]
        if why:
            rows.append(f'<div class="hrow"><span>Explained</span><div class="num"></div><em>{E(", ".join(why))}</em></div>')
        out.append(f'<div class="hv"><h3>{E("Mendix " + h["v"]) if h["v"] else "This run"}</h3>{"".join(rows)}</div>')
    return '<section class="card health" aria-label="How the tests improved"><h2>How the tests improved</h2>' + "".join(out) + "</section>"


def h_band(b):
    tick = {"ok": "✓", "bad": "!", "warn": "→"}.get(b["state"], "…")
    reg = ""
    if b["sub"]:
        bad = b["state"] == "ok" and b["reg"]
        reg = f'<span class="rg{" bad" if bad else ""}">{E(b["sub"])}</span>'
    chips = "".join(f'<span class="cc"><b>{c["n"]}</b>{E(c["label"])}</span>' for c in b["closed"]["chips"])
    # who closes each open topic, and when (cold test WM1: "16 open topics still to validate" and the owner asked "what should a
    # person do with this? validate when, by who?"; all 16 were the agent's, closed later in the run)
    WHEN = {"Regression": "now", "To fix": "during the upgrade", "Coverage": "at the test stage", "At deploy": "at deploy"}
    its = b["open"]["items"]
    mine = [o for o in its if o["owner"] != "agent" and o["group"] != "At deploy"]
    later = [o for o in its if o["group"] == "At deploy"]
    agent = [o for o in its if o not in mine and o not in later]

    def lst(xs, who):
        return "".join(f'<div class="ns"><b>{E(o["group"])}</b><span>{E(o["text"])}</span><em>{E(who or WHEN.get(o["group"], ""))}</em></div>' for o in xs)
    you = (f'<div class="kpi open"><b>{len(mine)}</b><span>for you now</span><div class="next">{lst(mine, "you")}</div></div>' if mine
           else '<div class="kpi good"><b>0</b><span>for you now: nothing to do, the agent goes on</span></div>')
    agentbox = (f'<details class="kpi"><summary><b>{len(agent)}</b><span>the agent closes these itself, later in the run (open to see when)</span></summary>'
                f'<div class="next">{lst(agent, "")}</div></details>' if agent else "")
    laterbox = (f'<details class="kpi"><summary><b>{len(later)}</b><span>for a person at deploy, not now</span></summary>'
                f'<div class="next">{lst(later, "")}</div></details>' if later else "")
    closed = (f'<div class="kpi good"><b>{b["closed"]["n"]}</b><span>items closed successfully</span><div class="ccs">{chips}</div></div>'
              if b["closed"]["n"] else "")
    return (f'<section class="hero {b["state"]}" aria-label="Progress">\n'
            f'<div class="hmsg"><span class="tick">{tick}</span><div><b>{E(b["head"])}</b>{reg}</div></div>\n'
            f'<div class="kpis">{you}{closed}{agentbox}{laterbox}</div></section>')


def h_tiles(M):
    T = M["tiles"]
    fx, ts = [T["upg"][0] + T["gap"][0], T["upg"][1] + T["gap"][1]], [T["tested"][0], T["tested"][0] + T["tested"][2]]
    head = (f'<span><b>{fx[0]}</b> of {fx[1]} fixed</span><span><b>{ts[0]}</b> of {ts[1]} tested</span>'
            + (f'<span class="neutral"><b>{T["tested"][1]}</b> at deploy</span>' if T["tested"][1] else "")
            + ("" if T["reg"] is None else f'<span class="{"bad" if T["reg"] else ""}"><b>{T["reg"]}</b> regressions</span>'))

    def kt(k, v, t):
        if isinstance(v, list):
            cls, val = ("good" if v[1] and v[0] == v[1] else "warn"), f"{v[0]}/{v[1]}"
        else:
            cls, val = ("you" if k == "owner" and T["you"] else "neutral"), str(v)
        more = f' · {T["you"]} need you' if k == "owner" and T["you"] else ""
        return f'<button class="tile kind {cls}" type="button" data-kind="{k}" aria-pressed="false"><b>{val}</b><span>{t}{more}</span></button>'
    up = T["up"]
    tiles_ = (f'<div class="tile {"good" if up[1] and up[0] == up[1] else "warn"}"><b>{up[0]}/{up[1]}</b><span>upgrade items done</span></div>'
              + ('<div class="tile"><b>not yet</b><span>regressions</span></div>' if T["reg"] is None
                 else f'<div class="tile {"bad" if T["reg"] else "good"}"><b>{T["reg"]}</b><span>regressions</span></div>')
              + kt("upgrade", T["upg"], "upgrade problems solved") + kt("testgap", T["gap"], "test gaps closed")
              + kt("owner", T["own"], "your tasks") + kt("golive", T["gol"], "at go-live"))
    return head, tiles_


def h_ready(M):
    return "".join(f'<span class="chip ok">{E(c["l"])}</span>' if c["s"] == "ok"
                   else f'<button class="chip {c["s"]}" type="button" data-ready="{E(c["id"])}">{E(c["l"])} →</button>' for c in M["ready"])


def h_matrix(M):
    h = '<div class="row hd"><div class="hcell">Item</div>' + "".join(
        f'<button class="stage" type="button" data-stage="{s["key"]}" aria-pressed="false"><span><span class="n">{s["n"]}</span>{E(s["name"])}</span>'
        f'<small>{E(s["sub"])}</small><span class="more">How this stage works →</span></button>' for s in M["stages"]) + "</div>"
    names, g = {x["key"]: x["name"] for x in M["groups"]}, None
    for i, it in enumerate(M["rows"]):
        if it["group"] != g:
            g = it["group"]
            h += f'<div class="grp">{E(names[g])}</div>'
        h += f'<div class="row" id="r{i}"><div class="item">{E(it["name"])}<small>{E(it["sub"])}</small></div>' + "".join(
            f'<div class="cell"><button class="chip {it["cells"][s["key"]]["s"]}" type="button" data-i="{i}" data-s="{s["key"]}">{E(it["cells"][s["key"]]["l"])}</button></div>'
            for s in M["stages"]) + "</div>"
    return h


def h_feed(M):
    def fmt(t):
        d = parse_iso(t)
        return d.strftime("%-d %b %H:%M UTC") if d else t
    return "".join(f'<li><time>{E(fmt(f["t"]))}</time>{E(f["text"])}</li>' for f in M["feed"]) or "<li>Nothing recorded yet.</li>"


GREY = [("Not yet", "the run has not reached this stage for the item"), ("Not started", "planned, waits for the plan approval"),
        ("Not needed", "this stage has nothing to do for the item")]


def h_legend(M):
    used = {c["s"] for r in M["rows"] for c in r["cells"].values()} | {c["s"] for c in M["ready"]}
    labels = {c["l"] for r in M["rows"] for c in r["cells"].values() if c["s"] == "none"}
    grey = "".join(f'<span class="gl"><b>{l}</b>: {t}</span>' for l, t in GREY if l in labels)
    return ("".join(f'<span><i style="background:var(--{k})"></i>{t}</span>' for k, t in LEGEND if k in used)
            + (f'<span class="gbreak"></span><span class="gl"><i style="background:var(--none)"></i>Grey cells:</span>{grey}' if grey else ""))


def h_running(r):
    """The step running now (cockpitpage.running): a bar under the header. Always present, hidden when idle, so the live
    page (cockpitserve.py /status) can fill it in place without a reload."""
    if not r:
        return '<div class="nowrun" id="nowrun" hidden aria-live="polite"><span class="pulse"></span><div><b></b><small></small></div></div>'
    what = " · ".join(x for x in [f'{r["mins"]} min' if r["mins"] else "just started",
                                  f'now in {r["tool"]}' if r["tool"] else "", r["said"]] if x)
    return (f'<div class="nowrun" id="nowrun" aria-live="polite"><span class="pulse"></span><div><b>Running now: {E(r["text"])} ({E(r["step"])})</b>'
            f'<small>{E(what)}</small></div></div>')


def h_stopped(s):
    """A judgment stop (NEEDS-JUDGMENT.md): a red bar under the header, so a run that waits for a person says so first."""
    if not s:
        return ""
    if str(s["code"]) in ("14", "15"):   # the plan waits for sign-off: the Decide now cards are the questions, no paths or commands
        return ('<div class="stopbar" role="alert"><b>The run stopped before changing anything: the plan waits for your answers and '
                'your approval.</b><small>Open <b>Blocked on you</b> on the right to answer. The run goes on after you approve.</small></div>')
    li = "".join(f"<li>{E(t)}</li>" for t in s["titles"])
    cmd = f'<small>Then rerun: <code>{E(s["rerun"])}</code></small>' if s["rerun"] else ""
    return (f'<div class="stopbar" role="alert"><b>The run stopped at {E(s["step"])} (exit {s["code"]}) and waits for you.</b>'
            f'{"<ul>" + li + "</ul>" if li else ""}<small>Answer under <b>Blocked on you</b> on the right. Details: NEEDS-JUDGMENT.md in the work folder.</small>{cmd}</div>')


def open_questions(model):
    """The items a person still has to answer, one question card each: plan choices and judgments first, the sign-off last."""
    qs = [i for i in model["items"] if i.get("options") and not i.get("decided") and i["kind"] != "confirmgroup"]
    return sorted(qs, key=lambda i: i["kind"] == "signoff")


def question_of(i):
    if i["title"].endswith("(check)"):   # a triage check that did not run (proposal.py, release notes)
        return f"The {i['title'][:-8].strip().lower()} check did not run. How do we go on?"
    t = re.sub(r"\s*\((module|widget|jar|java)\)$", "", i["title"])
    return {"plan-choice": f"What should the upgrade do with {t}?", "signoff": "Approve the plan and start the upgrade?",
            "confirm": f"Accept this change: {t}?"}.get(i["kind"], t)


def plain(t):
    """An option or recommendation without the file names and rule names behind it (they stay in the technical details)."""
    t = re.sub(r"\s*\((kept list|replacements\.tsv row|[a-z0-9_./ ]+\.(?:json|txt|tsv|md))\)", "", t or "")
    t = re.sub(r"\beffort ([SML])\b", lambda m: {"S": "small", "M": "medium", "L": "large"}[m.group(1)] + " effort", t)
    t = t.replace("a RED edit", "the app's own edit").replace("RED local edit", "the app's own edit")
    return "; ".join(x.strip() for x in t.split(";") if x.strip() and "stop rule" not in x).strip()


# what an option of a module plan choice does, in words, by the phrase the proposal uses for it
OPTION_SAYS = [("update to the latest", "Take the newest Marketplace version. The pipeline carries the app's edits over: diagram-only changes are dropped, pages, layouts and constants are replayed, and data the vendor drops is checked for use first."),
               ("update, move", "Take the newest version after a person moves the app's own logic into a module of its own (<Module>_Ext) that works with the Marketplace module."),
               ("keep old", "The module stays as it is now. It misses the Marketplace fixes and may not run on the next Mendix version: only with a reason and an end date."),
               ("replace", "Take the new Marketplace version. The app's own additions to the module are removed, and their data with them unless it is moved first."),
               ("rebuild", "Move the app's own additions into a module of its own, then take the clean Marketplace version. Most work, cleanest result."),
               ("hand to", "Park this one. The run waits until the named person answers.")]


def context_of(i):
    """Two or three plain sentences: what the item is and why it is asked."""
    if i["kind"] == "signoff":
        return ["The run has prepared the upgrade and changed nothing in the app yet.",
                "Approving starts the upgrade with your answers to the other questions, and with what the toolkit does on its own: the "
                "Marketplace module updates, the conversion to the new version and the stand-ins for outside systems (all listed in the matrix).",
                "Every change is a Git commit, so you can review or revert each one."]
    if i["kind"] == "plan-choice" and (i.get("problem") or "").startswith("the release-note check did not run"):
        return ["Before the plan, the toolkit reads what each Mendix version on the route changes (the release notes) and checks this app against it.",
                "That check did not run" + (": the company brain's version tables are not on this machine" if "version tables" in i["problem"] else "")
                + ". So nobody has checked yet what the new Mendix versions change for this app."]
    if i["kind"] == "plan-choice":
        ent = [x.split(".")[-1] for x in re.findall(r"ADDED entity ([\w.]+)", i.get("problem") or "")]
        more = re.search(r"\(\+(\d+)\)", i.get("problem") or "")
        if ent:
            n = len(ent) + (int(more.group(1)) if more else 0)
            name = re.sub(r"\s*\(.*\)$", "", i["title"])
            return [f"{name} is a Marketplace module, but this app changed it: it added {n} entities of its own ({', '.join(ent)}{', ...' if more else ''}).",
                    "A Marketplace update overwrites the whole module, so those additions, and the data stored in them, would be lost."]
    return [plain(i.get("problem") or "")] if i.get("problem") else []


CASE_DIR = "cases"


def case_id(item_id):
    """The file name of the case of one decision: work/cases/<id>.json, with every character outside [A-Za-z0-9._-] as _."""
    return re.sub(r"[^A-Za-z0-9._-]", "_", item_id) + ".json"


def _embed(work, c):
    """The case's screenshots (paths in the work folder) as data URIs, "" when missing."""
    import base64
    for sh in c.get("shots") or []:
        for k in ("old", "new"):
            pth = os.path.join(work, sh.get(k) or "")
            if sh.get(k) and os.path.isfile(pth) and pth.lower().endswith((".png", ".jpg", ".jpeg")):
                with open(pth, "rb") as fh:
                    sh[k] = ("data:image/png;base64," if pth.lower().endswith(".png") else "data:image/jpeg;base64,") + base64.b64encode(fh.read()).decode()
            else:
                sh[k] = ""
    return c


def cases(work, model=None):
    """The case files of the open decisions (the owner, 2026-11-17: "such a report per issue that needs a decision"). A case is what the
    agent that raised the decision found: {"headline", "tiles": [[number, label, tone]], "shots": [{"old", "new", "cap"}], "why": [steps],
    "options": {option key: {"does", "catch"}}, "details": [lines]}. Screenshots are paths in the work folder, embedded as data URIs,
    so the cockpit stays one file. A regression without a case file gets one built from the run's own files (auto_case); a broken
    case file is skipped."""
    out, d = {}, os.path.join(work, CASE_DIR)
    for f in sorted(os.listdir(d)) if os.path.isdir(d) else []:
        c = cp.rj(os.path.join(d, f)) if f.endswith(".json") else None
        if isinstance(c, dict):
            out[f] = _embed(work, c)
    for i in (model or {}).get("items") or []:
        if i.get("kind") == "regression" and case_id(i["id"]) not in out:
            c = auto_case(work, i)
            if c:
                out[case_id(i["id"])] = _embed(work, c)
    return out


def _shot_paths(work):
    """{file name: [paths relative to work]} of the walk screenshots."""
    got = {}
    for root, dirs, files in os.walk(work):
        dirs[:] = [x for x in dirs if x not in (CASE_DIR, "node_modules", ".git")]
        for f in files:
            if f.endswith(".png"):
                got.setdefault(f, []).append(os.path.relpath(os.path.join(root, f), work))
    return got


def auto_case(work, item):
    """The case of a regression nobody wrote one for, from the run's own files: how many actions broke, the first old and new
    screenshot of the same step, the module edits the update carried over (the first place to look), and the evidence lines."""
    heal = _json(work, "heal.json") or {}
    ids = item.get("tech") or []
    ev = {r.get("id"): r.get("evidence", "") for r in heal.get("rows", []) if r.get("class") == "real-regression"}
    lines = [ev[x] for x in ids if ev.get(x)]
    if not ids:
        return None
    pages = sorted({re.sub(r"^act-", "", x.split(":", 1)[-1]).rsplit(".", 1)[0] for x in ids})
    n = len(ids)
    shots, names = [], None
    for ln in lines:
        m = re.search(r"screenshot (\S+\.png)", ln)
        if m:
            names = names or _shot_paths(work)
            new = (names.get(m.group(1)) or [""])[0]
            oldn = re.sub(r"-[A-Z][A-Z-]*\.png$", ".png", m.group(1))
            olds = names.get(oldn) or []
            old = next((x for x in olds if "before" in x or "old" in x), olds[0] if olds else "")
            if new or old:
                step = re.search(r"-(step\d+)", m.group(1))
                shots.append({"old": old, "new": new, "cap": f"{pages[0]}, {step.group(1) if step else 'the step'} that fails: "
                              "the old app on the left, where the new app stopped on the right."})
                break
    # a vendor screen the app changed (not a page the app added to the module): the update carries it over
    carried = sorted({m["name"] for m in (_json(work, "localedits.json") or []) if isinstance(m, dict)
                      and any(x.get("change") == "CHANGED" for x in m.get("ui") or [])})
    reason = next((r.group(1) for ln in lines for r in [re.search(r"FAIL (.+?)(?: \u2014| \||$)", ln)] if r), "")
    why = [f"{n} action{'s' if n != 1 else ''} on {len(pages)} page{'s' if len(pages) != 1 else ''} pass on the old app and fail on the new one"
           + (f": {reason}." if reason else ".")]
    if carried:
        why.append(f"The update carried over the app's own screen edits in {', '.join(carried)}. A carried screen edit is the first place to look.")
    tiles = [[n, "pass on the old app, fail on the new", "bad"], [len(pages), "page" + ("s" if len(pages) != 1 else ""), "wait"]]
    if carried:
        tiles.append([len(carried), "modules with screen edits carried over", "wait"])
    return {"headline": f"{n} action{'s' if n != 1 else ''} that work on the old app fail on the new one ({', '.join(pages[:3])}{', ...' if len(pages) > 3 else ''}).",
            "tiles": tiles, "shots": shots, "why": why,
            "options": {"fix": {"does": "The agent finds the cause, fixes it in the toolkit or the app, and runs again from the step that broke. These actions must pass.",
                                "catch": "One more run of the tests."},
                        "accept": {"does": "Record these changes as intended, with your name and reason.",
                                   "catch": "Users can no longer do on the new app what these actions did on the old one."},
                        "old-wrong": {"does": "Record that the old app was wrong here.",
                                      "catch": "Only true when the old behaviour was a bug; the screenshots show what it did."}},
            "details": [cp.short(x, 300) for x in lines[:6]]}


def h_case(c):
    """The case block inside a question dialog: tiles, old and new screenshot, why in steps."""
    if not c:
        return ""
    tl = "".join(f'<div class="ct {E(str(t[2]) if len(t) > 2 else "")}"><b>{E(str(t[0]))}</b><span>{E(str(t[1]))}</span></div>' for t in c.get("tiles") or [] if len(t) > 1)
    def pane(src, lab):
        img = f'<img src="{src}" alt="{lab}">' if src else "<i>no screenshot</i>"
        return f"<div><span>{lab}</span>{img}</div>"
    sh = "".join(f'<figure class="cshot">{pane(x.get("old"), "Old app")}{pane(x.get("new"), "New app")}<figcaption>{E(x.get("cap") or "")}</figcaption></figure>'
                 for x in c.get("shots") or [])
    wy = "".join(f"<li>{E(w)}</li>" for w in c.get("why") or [])
    dt = "".join(f"<li>{E(x)}</li>" for x in c.get("details") or [])
    return ((f'<p class="chead">{E(c["headline"])}</p>' if c.get("headline") else "") + (f'<div class="ctiles">{tl}</div>' if tl else "") + sh
            + (f'<h4 class="cwh">Why it happened</h4><ol class="cwhy">{wy}</ol>' if wy else "")
            + (f'<details class="cdet"><summary>The evidence</summary><ul>{dt}</ul></details>' if dt else ""))


def h_questions(model, matrix=None, cases_=None):
    """The open questions: a "Blocked on you" list in the sidebar, each with a Resolve button that opens one question in a dialog
    with its context, one button per option and what each option does. The buttons post to the local server (cockpitserve.py
    /decide, live page only); on a static copy they stay off and the answer goes through chat."""
    qs = open_questions(model)
    # a choice the agent made on its own (a step with an assumed approval) blocks too; Resolve opens its plan cell, where its buttons are
    asks = [(n, r) for n, r in enumerate((matrix or {}).get("rows", [])) if r.get("fromSteps") and r.get("ask") and r["cells"]["plan"]["s"] == "you"]
    if not qs and not asks:
        return "", ""
    rows, dlgs = [], []
    for n, r in asks:
        rows.append(f'<li><span>The agent chose this on its own: {E(r["name"])}. OK?</span>'
                    f'<button type="button" class="resolve" data-i="{n}" data-s="plan">Resolve →</button></li>')
    for n, i in enumerate(qs, 1):
        rows.append(f'<li><span>{E(question_of(i))}</span><button type="button" class="resolve" data-q="q{n}">Resolve →</button></li>')
        btns = []
        cs = (cases_ or {}).get(case_id(i["id"])) or {}
        for o in i["options"]:
            lab = plain(o["label"]) or o["label"]
            co = (cs.get("options") or {}).get(o["key"]) or {}
            say = co.get("does") or (o.get("causes") or next((t for k, t in OPTION_SAYS if k in lab.lower()), "") if i["kind"] == "plan-choice" else "")
            if not say and ": " in lab:
                lab, say = lab.split(": ", 1)
                say = say[:1].upper() + say[1:] + "."
            if i["kind"] == "signoff":
                lab = "Approve and continue"
            rec = o["key"] == i.get("rec") and len(i["options"]) > 1
            btns.append(f'<button type="button" disabled data-choice="{E(o["key"])}" class="{"rec" if rec else ""}"><b>{E(lab)}</b>'
                        f'{"<em>Recommended</em>" if rec else ""}{"<small>" + E(say[:320]) + "</small>" if say else ""}'
                        f'{"<small class=" + chr(34) + "catch" + chr(34) + ">The catch: " + E(co["catch"]) + "</small>" if co.get("catch") else ""}</button>')
        ctx = "".join(f"<p>{E(t)}</p>" for t in context_of(i) if t)
        # what exactly is behind it, from the run's own files (cold test WM1: "how can a person ever decide without those details?")
        ev = i.get("evidence") or {}
        if ev.get("what"):
            ctx += ('<div class="qev"><b>What exactly</b><ul>' + "".join(f"<li>{E(w)}</li>" for w in ev["what"][:15])
                    + (f"<li>and {len(ev['what']) - 15} more</li>" if len(ev["what"]) > 15 else "") + "</ul>"
                    + f'<small>From: {E(", ".join(ev.get("files") or []))}</small></div>')
        why = plain(i.get("rec_text") or "")
        rl = plain(next((o["label"] for o in i["options"] if o["key"] == i.get("rec")), ""))
        if rl and why.startswith(rl) and why[len(rl):].startswith(";"):   # the option itself is the button; keep effort and risk
            why = why[len(rl) + 1:].strip()
            why = why[:1].upper() + why[1:]
        rec = f'<p class="qrec"><b>Why we recommend it:</b> {E(why)}</p>' if why and len(i["options"]) > 1 and not cs.get("options") else ""
        if cs:   # a case written by the agent replaces the generic context: the case says what is wrong, shows it, and why
            ctx = h_case(cs)
        dlgs.append(f'<dialog class="qdlg{" wide" if cs else ""}" id="q{n}"><div class="qcard" data-item="{E(i["id"])}"><div class="qk">Question {n} of {len(qs)} · '
                    f'blocks step {E(i.get("step") or "")}</div><h3>{E(question_of(i))}</h3>{ctx}{rec}<div class="qopts">{btns and "".join(btns)}</div>'
                    '<div class="qmsg" data-qmsg aria-live="polite"></div><p class="qhint">The buttons work in the live cockpit. On a copy, answer in chat.</p>'
                    '<button type="button" class="qclose">Close</button></div></dialog>')
    side = (f'<section class="blocked" aria-label="Blocked on you"><h2>Blocked on you: {len(qs) + len(asks)}</h2>'
            '<p>The run waits for these answers. Click Resolve for the full question.</p><ol>' + "".join(rows) + "</ol></section>")
    return side, "".join(dlgs)


def render(model, matrix):
    data = json.dumps(dict({k: model[k] for k in ("title", "sub", "state", "planHash", "signed", "phases", "items")}, matrix=matrix), ensure_ascii=False)
    data = data.replace("</", "<\\/").replace("<!--", "<\\!--")
    e = html.escape
    head_, tiles_ = h_tiles(matrix)
    cases_ = matrix.pop("cases", None) or {}   # kept out of the page data: the screenshots are embedded once, in the dialog
    qside, qdlgs = h_questions(model, matrix, cases_)
    return (f"<title>{e(model['title'])}</title>\n"
            '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
            '<meta name="claude:viewport-fit-sides" content="cover">\n'
            f"<style>{CSS}</style>\n"
            '<div class="wrap">\n  <header class="head">\n    <div>\n      <div class="eyebrow">Upgrade cockpit</div>\n'
            f"      <h1>{e(model['title'])}</h1>\n      <div class=\"ver\">{e(model['sub'])}</div>\n"
            "    </div>\n"
            f"    {h_ladder(matrix.get('ladder'))}\n  </header>\n"
            f"  {h_stopped(model.get('stopped'))}{h_running(model.get('running'))}\n"
            '  <div class="layout">\n  <div class="main">\n'
            '  <details class="card more"><summary>Counts by kind (tap one to mark its rows)</summary>\n'
            f'    <div class="headline" id="headline">{head_}</div>\n    <div class="tiles" id="tiles">{tiles_}</div>\n  </details>\n'
            '  <section class="card ready" aria-label="Readiness">\n'
            '    <div class="top"><h2>Do we have what we need to upgrade and test?</h2><span>Checked in triage. Each item that is not green opens its proposed solution.</span></div>\n'
            f'    <div class="rchips" id="ready">{h_ready(matrix)}</div>\n  </section>\n'
            f'  <div class="legend">{h_legend(matrix)}</div>\n'
            f'  <section class="card scroll" aria-label="Items per stage"><div class="pbar" id="phases" hidden></div><div class="grid" id="matrix">{h_matrix(matrix)}</div></section>\n'
            '  <p class="note">Click a stage name to see how that stage works. Click any cell for that item, step by step.</p>\n'
            f"  {h_health(matrix.get('health'))}\n"
            '  <section class="card feed" aria-label="Recent changes">\n    <h2>Since you last looked</h2>\n'
            f'    <ol id="feed">{h_feed(matrix)}</ol>\n  </section>\n  </div>\n'
            f'  <aside class="side">{qside}{h_band(matrix["band"])}'
            # the page can lag the run; the session that drives it always knows (cold test WM1)
            '<p class="agentnote">Page not up to date, or stuck? Talk to your agent in the chat. It is easier.</p>'
            f'</aside>\n  </div>\n</div>\n{qdlgs}\n'
            '<div class="shade" id="shade" hidden></div>\n'
            '<aside class="drawer" id="drawer" hidden role="dialog" aria-modal="true" aria-label="Details">\n'
            '  <button class="x" id="dClose" type="button" aria-label="Close">×</button>\n  <div id="dBody"></div>\n</aside>\n\n'
            f"<script>\nconst D={data};\n{JS}</script>\n")
