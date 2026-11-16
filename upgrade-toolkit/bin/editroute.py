#!/usr/bin/env python3
"""editroute.py: route each module the update refused to a way of updating it anyway, instead of keeping it at the old version.

Why (cold test WM1, 2026-11-16): seven Marketplace modules were "kept" because "local edits refuse the update", and the cockpit
recommended "keep old version" for all seven. The owner: an edit does not mean the module cannot be updated; most edits can be
carried over, and an old module misses fixes and may not run on the next Mendix version. Looking closer, Email_Connector's one
"changed" microflow differed only in where an arrow attached; Encryption's edit was its key constant; MendixSSO's update drops an
attribute nothing in the app reads. None of that is a reason to stay behind.

Routes, per refused module (the module is updated in all of them except HOLD):
  COSMETIC  every refused microflow/nanoflow/rule equals the installed package once diagram geometry (@position, @anchor, @curve,
            @size) is ignored: forced, nothing to replay
  REPLAY    pages, layouts, snippets, images and constants: the CHANGE is replayed onto the new version, not the old element
            (replay/<Module>.mdl): a three-way merge per element of `mxcli describe` (base = installed package, ours = the
            original app, theirs = the updated app), each result passed through `mxcli check` first; mixed with COSMETIC
            logic, only the UI elements are replayed. Why (cold test WM1, Atlas_Core): the saved whole element lost the
            layout's master-layout link (empty Atlas_Default, every page would lose the company design) and carried the old
            Sprintr widget's properties onto the new widget; replaying it was refused by mxcli (MDL081, MDL-WIDGET01)
  UNREAD    mxcli could not read some elements and localedits shows no domain or logic edit: forced, whatever it could save replayed
  FILES     theme/JavaScript files could not be compared (installed package unreadable): the saved copies under
            .stepupdate/saved/<Module>/ stay, the update may commit (accept-unsaved.txt)
  VENDOR    the new version drops an attribute or entity of its own module and nothing outside the module refers to it
            (mxcli refs): accepted in approved.txt with that reason
  XASSOC    the update drops associations ANOTHER module owns into this one (they hold app data): forced with --save-edits, each
            association replayed and its ORIGINAL GUID restored (replay/<Module>.guids), the step-only removal in approved-step.txt
  HOLD      a real logic edit, Java user code, a GUID change, a removal something still uses, a tool or network fault: it stays a
            card for a person, with the evidence. The recommendation there is still to update (move the edit to <Module>_Ext).

  A module the routed update kept again is routed again (the pipeline runs plan up to three times): routes add up per module
  (Email_Connector, WM1: COSMETIC, then XASSOC for the 3 associations the app's Email module owns into it). The same reason
  twice is a HOLD.

  editroute.py reset   --work W   first thing in the update step: an earlier routing's lines and files out of the way
  editroute.py score   --work W --app A --plan W/plan.txt [--ledger F]   did each route work: editroute-score.tsv, exit 1 when a
                       kept module did not end on the plan's version (held, replay failed, or kept again)
  editroute.py plan    --work W --app A --original W/original.mpr --plan W/plan.txt   writes the route files, prints ROUTE lines
  editroute.py collect --work W                                                       after the routed update: builds replay/
Files: W/edit-routes.json (one row per module), W/route-plan.txt (the plan lines of the routed modules, plan order), and
appends to W/force-ui.txt, W/accept-unsaved.txt, W/approved.txt, W/approved-step.txt. Exit 0 = something routed, 1 = nothing.
"""
import argparse, difflib, glob, json, os, re, subprocess, sys, time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import localedits  # noqa: E402  (MXCLI, CACHE, fetch_pkg)

UI_KINDS = {"PAGE", "LAYOUT", "SNIPPET", "IMAGE", "IMAGECOLLECTION", "CONSTANT"}
LOGIC_KINDS = {"MICROFLOW": "microflow", "NANOFLOW": "nanoflow", "RULE": "rule"}
GEOM = re.compile(r"^\s*@(position|anchor|curve|size)\b")
NOISE = re.compile(r"^(✓|Building|Loading|Connected|WARNING)")


def rd(p):
    try:
        with open(p, encoding="utf-8", errors="replace") as f:
            return f.read()
    except OSError:
        return ""


def mx(args):
    r = subprocess.run([localedits.MXCLI] + args, capture_output=True, text=True)
    return r.returncode, "\n".join(ln for ln in (r.stdout or "").splitlines() if not NOISE.match(ln))


def describe(mpr, kind, qn):
    rc, out = mx(["describe", "-p", mpr, kind, qn])
    return out if rc == 0 and out.strip() else None


def logic_body(text):
    return [ln.rstrip() for ln in text.splitlines() if not GEOM.match(ln)]


def refusal(log):
    """(rows [(KIND, name)], unread count) of the last refusal in an update log."""
    t = rd(log)
    rows = []
    for m in re.finditer(r"refusing to update:[^\n]*\n((?:\s{2,}\S[^\n]*\n)+)", t):
        rows = [tuple(ln.split(None, 1)) for ln in m.group(1).splitlines() if len(ln.split(None, 1)) == 2 and not ln.strip().startswith("-")]
    u = re.findall(r"(\d+) element\(s\) could not be read", t)
    return [(k, n.strip()) for k, n in rows], int(u[-1]) if u else 0


def red_rows(idc):
    return [m.groups() for m in re.finditer(r"^RED\s+(\w+)\s+(\w+)\s+([\w.]+)", rd(idc), re.M)]


def unused(original, kind, qn):
    rc, out = mx(["refs", "-p", original, qn])
    return rc == 0 and "no references found" in out


def route_module(mod, why, S, ledit, original, cache, mpr):
    """-> (route, reason, extra) for one kept module."""
    logs = sorted(glob.glob(os.path.join(S, f"step*-{mod}.log")), key=lambda p: int(re.search(r"step(\d+)-", p).group(1)))
    log = logs[-1] if logs else ""
    if re.search(r"NETWORK|update failed|Java user code|javasource", why):
        return "HOLD", why, {}
    if "idcheck REVIEW" in why:
        idc = log[:-4] + ".idcheck" if log else ""
        rows, own, xassoc, bad = red_rows(idc), [], [], []
        for finding, kind, qn in rows:
            if finding == "REMOVED" and kind in ("attribute", "entity") and qn.split(".")[0] == mod:
                (own if unused(original, kind, qn) else bad).append(qn)
            elif finding == "REMOVED" and kind == "association" and qn.split(".")[0] != mod:
                xassoc.append(qn)
            else:
                bad.append(f"{finding} {kind} {qn}")
        if bad or not rows:
            return "HOLD", "idcheck finding still used or not a removal: " + ", ".join(bad or ["no RED rows read"]), {}
        if xassoc:
            return "XASSOC", f"the update drops {len(xassoc)} association(s) other modules own into {mod}; replayed with their original ids", \
                {"assocs": xassoc, "vendor": own}
        return "VENDOR", f"the new version drops {', '.join(own)}; nothing outside {mod} refers to it", {"vendor": own}
    if "FILES-UNKNOWN" in why:
        return "FILES", f"files could not be compared with the installed package; the copies are kept under .stepupdate/saved/{mod}", {}
    rows, unread = refusal(log)
    if unread and not rows:
        e = ledit or {}
        if e and not e.get("domain") and not e.get("logic"):
            return "UNREAD", f"{unread} elements unreadable by mxcli; localedits shows no domain or logic edit", {}
        return "HOLD", f"{unread} elements unreadable and localedits shows domain or logic edits", {}
    if not rows:
        return "HOLD", why, {}
    pkg = None
    real, cosmetic, ui = [], [], []
    for kind, name in rows:
        if kind in UI_KINDS:
            ui.append(f"{kind.lower()} {name}")
        elif kind in LOGIC_KINDS:
            if pkg is None and ledit and ledit.get("cid") and ledit.get("version"):
                pkg, _, _ = localedits.fetch_pkg(ledit["cid"], ledit["version"], cache)
            a = describe(mpr, LOGIC_KINDS[kind], f"{mod}.{name}")
            b = describe(pkg, LOGIC_KINDS[kind], f"{mod}.{name}") if pkg else None
            (cosmetic if a and b and logic_body(a) == logic_body(b) else real).append(f"{kind.lower()} {name}")
        else:
            real.append(f"{kind.lower()} {name}")
    if real:
        return "HOLD", "real logic edit: " + ", ".join(real) + f" (move it to {mod}_Ext, then update)", {"cosmetic": cosmetic, "ui": ui}
    if ui:
        return "REPLAY", f"{len(ui)} UI element(s)/constant(s) saved and replayed onto the new version" + \
            (f"; {len(cosmetic)} diagram-only change(s) dropped" if cosmetic else ""), {"ui": ui, "cosmetic": cosmetic}
    return "COSMETIC", "only diagram layout differs (" + ", ".join(cosmetic) + "); the logic equals the Marketplace version", {"cosmetic": cosmetic}


def append(path, lines):
    have = set(rd(path).splitlines())
    new = [ln for ln in lines if ln not in have]
    if new:
        with open(path, "a") as f:
            f.write("".join(ln + "\n" for ln in new))


def cmd_plan(a):
    W, app = os.path.abspath(a.work), os.path.abspath(a.app)
    S = os.path.join(app, ".stepupdate")
    kept = [ln.split(" ", 1) for ln in rd(os.path.join(S, "kept.txt")).splitlines() if ln.strip()]
    try:
        led = {x["name"]: x for x in json.load(open(a.localedits or os.path.join(W, "localedits.json"))) if isinstance(x, dict)}
    except (OSError, ValueError):
        led = {}
    cache = os.environ.get("UPG_CACHE") or localedits.CACHE
    mpr = os.path.join(app, next((f for f in os.listdir(app) if f.endswith(".mpr")), ""))
    try:   # an earlier pass of this rung: its rows stay, a module kept again adds its new route
        prev = {x["module"]: x for x in json.load(open(os.path.join(W, "edit-routes.json")))}
    except (OSError, ValueError):
        prev = {}
    rows, now = dict(prev), []
    for mod, why in kept:
        r, reason, extra = route_module(mod, why, S, led.get(mod), a.original, cache, mpr)
        p = prev.get(mod)
        if p and p.get("kept_because") == why and r != "HOLD":
            r, reason, extra = "HOLD", f"the routed update kept it again for the same reason: {why}", {}
        e = led.get(mod) or {}
        if r in ("REPLAY", "UNREAD") and e.get("cid") and e.get("version"):
            extra["pkg"] = localedits.fetch_pkg(e["cid"], e["version"], cache)[0]
        row = {"module": mod, "route": r, "reason": reason, "kept_because": why, "original": a.original, "app_mpr": mpr, **extra}
        row["brain"] = brain_for(mod, r, reason)
        if p and p["route"] != "HOLD" and r != "HOLD":
            for k in ("ui", "cosmetic", "assocs", "vendor"):
                row[k] = sorted(set(p.get(k, [])) | set(row.get(k, [])))
            row["pkg"] = row.get("pkg") or p.get("pkg")
            row["route"] = "+".join(dict.fromkeys(p["route"].split("+") + [r]))
            row["reason"] = p["reason"] + "; then " + reason
        rows[mod] = row
        now.append(row)
        print(f"ROUTE {mod} {r}: {reason}")
    json.dump(list(rows.values()), open(os.path.join(W, "edit-routes.json"), "w"), indent=1)
    rows = now
    go = {x["module"] for x in rows if x["route"] != "HOLD"}
    plan = [ln for ln in rd(a.plan).splitlines() if len(ln.split()) >= 3 and not ln.startswith("#") and ln.split()[2] in go]
    with open(os.path.join(W, "route-plan.txt"), "w") as f:
        f.write("# modules the update kept, routed by editroute.py (edit-routes.json)\n" + "".join(ln + "\n" for ln in plan))
    append(os.path.join(W, "force-ui.txt"), [f"{x['module']} # editroute {x['route']}" for x in rows
                                             if {"COSMETIC", "REPLAY", "UNREAD", "XASSOC"} & set(x["route"].split("+"))])
    append(os.path.join(W, "accept-unsaved.txt"), [f"{x['module']} # editroute FILES: saved copies under .stepupdate/saved/{x['module']}" for x in rows if "FILES" in x["route"].split("+")])
    append(os.path.join(W, "approved.txt"), [f"{qn} # editroute VENDOR: the new {x['module']} drops it, nothing outside the module refers to it"
                                             for x in rows for qn in x.get("vendor", [])])
    append(os.path.join(W, "approved-step.txt"), [f"{qn} # editroute XASSOC: removed by the {x['module']} update, replayed with its original id"
                                                  for x in rows for qn in x.get("assocs", [])])
    return 0 if go else 1


HINT = {"HOLD": "edited Marketplace module extension module local edits", "REPLAY": "layout page snippet edited in Marketplace module",
        "XASSOC": "module update drops associations another module owns data", "VENDOR": "module update removes attribute data loss",
        "FILES": "theme styling files edited in module overwritten by update", "UNREAD": "Marketplace module update local edits",
        "COSMETIC": "Marketplace module update local edits"}
_NOTES = None


def brain_for(mod, route, reason, k=2):
    """[{path, title}] of the company brain's notes for this route (brainnotes.py); [] without a brain on this machine."""
    global _NOTES
    try:
        import brainnotes
        if _NOTES is None:
            b = brainnotes.brain_dir(None)
            _NOTES = brainnotes.load(b) if b and os.path.isdir(os.path.join(b, "internal")) else []
        q = f"{mod.replace('_', ' ')} {HINT.get(route.split('+')[0], '')} {reason}"
        r = brainnotes.search(_NOTES, q, k) if _NOTES else []
        return [{"path": p, "title": t} for sc, p, t in r if sc >= 0.5 * r[0][0]]   # a far weaker second match is noise
    except Exception:
        return []


def norm(t):
    return [ln.rstrip() for ln in (t or "").splitlines() if ln.strip() and not ln.startswith("mdl ")]


def merge_element(kind, qn, base_mpr, orig, app_mpr, tmp):
    """-> (mdl or None, how): the app's change carried onto the updated element, per the REPLAY rules in the docstring."""
    ours = describe(orig, kind, qn)
    if not ours:
        return None, "unreadable in the original model"
    base = describe(base_mpr, kind, qn) if base_mpr else None
    if base is not None and norm(ours) == norm(base):
        return "", "no edit (equal to the installed package)"
    theirs = describe(app_mpr, kind, qn)
    if base is None:
        return ours, "added by the app: its version"
    if theirs is None or norm(theirs) == norm(base):
        return ours, "the vendor did not change it: the app's version"
    paths = []
    for n, t in (("ours", ours), ("base", base), ("theirs", theirs)):
        paths.append(os.path.join(tmp, f"{qn}.{n}"))
        with open(paths[-1], "w") as f:
            f.write("\n".join(norm(t)) + "\n")
    r = subprocess.run(["git", "merge-file", "-p", *paths], capture_output=True, text=True)
    if r.returncode == 0:
        return "mdl 1;\n" + r.stdout, "merged: the app's change on the new version"
    props = prop_patch(norm(base), norm(ours), norm(theirs))
    if props is not None:
        return "mdl 1;\n" + "\n".join(props) + "\n", "the app's property values set on the new version"
    b, o = set(norm(base)), norm(ours)
    if sum(1 for ln in o if ln in b) < 0.3 * max(len(b), 1):
        return ours, "the app rewrote the whole element: its version kept, the vendor's change to it dropped"
    return None, "the app's change and the vendor's change overlap (merge conflict)"


PROP = re.compile(r"^(\s*)([\w.]+):\s")


def prop_patch(base, ours, theirs):
    """theirs with the app's changed property values, when every app change is a `key: value` line whose key also stands once
    in theirs (WM1 FeedbackWidget: only `sprintrapp` differed; the vendor rewrote the lines around it, so a line merge collides)."""
    sm = difflib.SequenceMatcher(None, base, ours, autojunk=False)
    sets = {}
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            continue
        if op != "replace" or i2 - i1 != j2 - j1:
            return None
        for bl, ol in zip(base[i1:i2], ours[j1:j2]):
            mb, mo = PROP.match(bl), PROP.match(ol)
            if not (mb and mo and mb.group(2) == mo.group(2)):
                return None
            sets[mo.group(2)] = ol
    out = list(theirs)
    for key, line in sets.items():
        hits = [i for i, ln in enumerate(out) if (m := PROP.match(ln)) and m.group(2) == key]
        if len(hits) != 1:
            return None
        comma = out[hits[0]].rstrip().endswith(",")
        out[hits[0]] = line.rstrip().rstrip(",") + ("," if comma else "")
    return out if sets else None


def checked(mdl, app_mpr, tmp, qn):
    p = os.path.join(tmp, f"{qn}.check.mdl")
    with open(p, "w") as f:
        f.write(mdl)
    rc, out = mx(["check", p, "-p", app_mpr])
    return rc == 0, " ".join(ln.strip() for ln in out.splitlines() if "✗" in ln or "error" in ln.lower())[:300]


def cmd_collect(a):
    W = os.path.abspath(a.work)
    try:
        allrows = json.load(open(os.path.join(W, "edit-routes.json")))
    except (OSError, ValueError):
        return 1
    os.makedirs(os.path.join(W, "replay"), exist_ok=True)
    tmp = os.path.join(W, "replay", ".merge")
    os.makedirs(tmp, exist_ok=True)
    n = 0
    for x in allrows:
        mod, routes = x["module"], set(x["route"].split("+"))
        d = os.path.join(W, "saved-edits", mod)
        parts, held = [], []
        if routes & {"REPLAY", "UNREAD"}:
            keep = {re.sub(r"\W", "", e.split(" ", 1)[1]).lower() for e in x.get("ui", [])}
            for f in sorted(glob.glob(os.path.join(d, "*.mdl"))):
                b = os.path.basename(f)[:-4]
                if b.startswith(("association-", "entity-", "microflow-", "nanoflow-")) or "-" not in b:
                    # a saved whole entity puts the vendor's widened attributes back (EmailTemplate: 5 of them String(2000)
                    # to String(200), data test 2026-11-16); logic goes to <Module>_Ext, never back into the vendor module
                    continue
                kind, name = b.split("-", 1)
                if "UNREAD" not in routes and re.sub(r"\W", "", name).lower() not in keep:
                    continue
                qn = f"{mod}.{name}"
                if kind in ("layout", "snippet", "page", "constant") and x.get("original") and x.get("app_mpr"):
                    mdl, how = merge_element(kind, qn, x.get("pkg"), x["original"], x["app_mpr"], tmp)
                else:
                    mdl, how = rd(f), "saved element (no describe for this kind)"
                if mdl is None:
                    held.append(f"{kind} {name}: {how}")
                    continue
                if not mdl.strip():
                    continue
                ok, why = checked(mdl, x["app_mpr"], tmp, qn) if x.get("app_mpr") else (True, "")
                if not ok:
                    held.append(f"{kind} {name}: mxcli check refuses the result: {why}")
                    continue
                parts.append((f"{kind} {name}: {how}", mdl))
        if "XASSOC" in routes:
            # from the ORIGINAL model, not save-edits: on WM1 the forced update wrote no association-*.mdl for the 4
            # associations the app's Email module owns into Email_Connector (data test 2026-11-16), so nothing was replayed
            owners = {}
            for q in x.get("assocs", []):
                f = os.path.join(d, f"association-{q.replace('.', '_')}.mdl")
                mdl = describe(x["original"], "association", q) if x.get("original") else None
                mdl = mdl or (rd(f) if os.path.exists(f) else None)
                if not mdl:
                    held.append(f"association {q}: not in the original model or the saved edits")
                    continue
                parts.append((f"association {q}: from the original model, original id restored after", mdl))
                m = re.search(r"\bfrom\s+([\w.]+)\s+to\b", mdl)
                if m:
                    owners.setdefault(m.group(1), []).append(q.split(".", 1)[1])
            # a re-created association has no member access (ReadWrite became None; a build error on a non-persistent
            # owner, data test 2026-11-16): the owner's grant lines that name it go in again
            for ent, names in owners.items():
                g = [ln.strip() for ln in (describe(x["original"], "entity", ent) or "").splitlines()
                     if ln.strip().startswith("grant ") and any(re.search(rf"\b{re.escape(n)}\b", ln) for n in names)]
                if g:
                    parts.append((f"member access on {ent} for {len(names)} association(s)", "\n".join(g)))
            with open(os.path.join(W, "replay", f"{mod}.guids"), "w") as g:
                g.write("".join(q + "\n" for q in x.get("assocs", [])))
        for h in held:
            print(f"HELD {mod} {h}")
        x["held"] = held
        if not parts:
            if routes & {"REPLAY", "UNREAD", "XASSOC"}:
                print(f"COLLECT {mod}: nothing to replay")
            continue
        with open(os.path.join(W, "replay", f"{mod}.mdl"), "w") as out:
            out.write(f"mdl 1;\n/* replay of {mod} (editroute {x['route']}) */\n")
            for label, mdl in parts:
                out.write(f"\n/* {label} */\n" + re.sub(r"^mdl 1;\s*", "", mdl.strip(), flags=re.M) + "\n")
        print(f"COLLECT {mod}: {len(parts)} element(s) -> replay/{mod}.mdl" + (f", {len(held)} held for a person" if held else ""))
        n += 1
    json.dump(allrows, open(os.path.join(W, "edit-routes.json"), "w"), indent=1)
    return 0 if n else 1


def cmd_reset(a):
    """A rerun of the update step starts as the first run did: editroute's own lines leave the decision files (a person's
    lines stay), the earlier routes and replays move aside. Why (WM1 rerun, 2026-11-16): the earlier run's 'Atlas_Core #
    editroute REPLAY' in force-ui.txt made the first update pass force Atlas_Core before any routing, so its edits were saved
    and never merged back: every page on the vendor layouts again."""
    W = os.path.abspath(a.work)
    n = 0
    for f in ("force-ui.txt", "accept-unsaved.txt", "approved.txt", "approved-step.txt"):
        p = os.path.join(W, f)
        lines = rd(p).splitlines(True)
        keep = [ln for ln in lines if "# editroute " not in ln]
        if len(keep) != len(lines):
            n += len(lines) - len(keep)
            with open(p, "w") as fh:
                fh.writelines(keep)
    old = os.path.join(W, ".editroute-prev-" + time.strftime("%Y%m%d%H%M%S"))
    moved = []
    for f in ("edit-routes.json", "replay", "editroute-score.tsv"):
        if os.path.exists(os.path.join(W, f)):
            os.makedirs(old, exist_ok=True)
            os.replace(os.path.join(W, f), os.path.join(old, f))
            moved.append(f)
    print(f"editroute-reset: {n} line(s) of an earlier routing removed from the decision files"
          + (f", {', '.join(moved)} moved to {os.path.basename(old)}" if moved else ""))
    return 0


def cmd_score(a):
    """Did each route work? One row per module the update kept, judged on the app's own git log and the run's files."""
    W, app = os.path.abspath(a.work), os.path.abspath(a.app)
    try:
        rows = json.load(open(os.path.join(W, "edit-routes.json")))
    except (OSError, ValueError):
        print("editroute-score: no edit-routes.json, nothing was routed")
        return 0
    r = subprocess.run(["git", "-C", app, "log", "--format=%s"], capture_output=True, text=True)
    log = r.stdout.splitlines() if r.returncode == 0 else []
    want = {}
    for ln in rd(a.plan).splitlines() if a.plan else []:
        f = ln.split()
        if len(f) >= 3 and f[0].isdigit():
            want[f[2]] = f[1]
    kept = {ln.split(" ", 1)[0] for ln in rd(os.path.join(app, ".stepupdate", "kept.txt")).splitlines() if ln.strip()}
    out, tot = [], {"modules": 0, "routed": 0, "on_target": 0, "held_modules": 0, "held_elements": 0, "replay_failed": 0}
    for x in rows:
        mod = x["module"]
        got = next((m.group(1) for ln in log if (m := re.match(rf"step: {re.escape(mod)} (\S+) \(stepupdate, idcheck PASS", ln))), "")
        replayed = any(ln.startswith(f"replay: {mod}") for ln in log)
        rp = os.path.join(W, "replay", f"{mod}.mdl")
        failed = os.path.exists(rp) and not replayed and os.path.exists(os.path.join(W, f"replay-{mod}.out"))
        on = bool(got) and mod not in kept and (not want.get(mod) or got == want[mod])
        held = len(x.get("held") or [])
        verdict = ("HOLD" if x["route"] == "HOLD" else "REPLAY FAILED" if failed else "ON TARGET" if on
                   else "KEPT" if mod in kept else "OFF TARGET")
        tot["modules"] += 1; tot["routed"] += x["route"] != "HOLD"; tot["on_target"] += on
        tot["held_modules"] += x["route"] == "HOLD"; tot["held_elements"] += held; tot["replay_failed"] += failed
        out.append([mod, x["route"], got or "-", want.get(mod, "-"), "yes" if replayed else "no" if os.path.exists(rp) else "-",
                    str(held), verdict, x.get("reason", "")[:160]])
    head = ["module", "route", "installed", "plan_target", "replayed", "held_elements", "verdict", "reason"]
    with open(os.path.join(W, "editroute-score.tsv"), "w") as f:
        f.write("\t".join(head) + "\n" + "".join("\t".join(o) + "\n" for o in out))
    if a.ledger:   # one line per module per run, across apps: the route that was chosen and whether it worked
        new = not os.path.exists(a.ledger)
        with open(a.ledger, "a") as f:
            if new:
                f.write("\t".join(["date", "app", "work"] + head) + "\n")
            for o in out:
                f.write("\t".join([time.strftime("%Y-%m-%d"), a.label or os.path.basename(app), W] + o) + "\n")
    for o in out:
        print(f"SCORE {o[0]} {o[1]} -> {o[6]} (installed {o[2]}, plan {o[3]}, held {o[5]})")
    print(f"editroute-score: {tot['on_target']}/{tot['modules']} kept module(s) ended on the plan's version, "
          f"{tot['held_modules']} held, {tot['held_elements']} element(s) held, {tot['replay_failed']} replay(s) failed")
    return 0 if tot["on_target"] == tot["modules"] else 1


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("plan")
    p.add_argument("--work", required=True); p.add_argument("--app", required=True)
    p.add_argument("--original", required=True); p.add_argument("--plan", required=True); p.add_argument("--localedits")
    c = sp.add_parser("collect")
    c.add_argument("--work", required=True)
    s = sp.add_parser("score")
    s.add_argument("--work", required=True); s.add_argument("--app", required=True); s.add_argument("--plan")
    s.add_argument("--ledger", help="append the rows here too (cross-run: UPG_ROUTE_LEDGER)"); s.add_argument("--label")
    r = sp.add_parser("reset")
    r.add_argument("--work", required=True)
    a = ap.parse_args()
    return {"plan": cmd_plan, "collect": cmd_collect, "score": cmd_score, "reset": cmd_reset}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
