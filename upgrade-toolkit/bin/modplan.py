#!/usr/bin/env python3
"""modplan.py: pick the target version of every installed Marketplace module and write the module plan (GA-4).

  modplan.py <localedits.json> --target 11.12.2 [--out plan.txt] [--jumps module-jumps.txt] [--app APP]
             [--versions-dir DIR] [--no-fetch] [--skip A,B] [--last X,Y] [--force]

Rule (steps/triage.md item 3, E6-5): for each module, the NEWEST plain release whose "min Mendix" is at or below
--target and that is newer than the installed version. This is the catalog rule only. It does not know whether a package
is importable on the target (planbuild.py reads the build version), which module a newer one drags in (absentmods.py),
or the per-module caps (atlascap.py); run those on the plan afterwards.

Input: localedits.json from localedits.py (name, cid, version per module). Versions come from `mxcli marketplace
versions <cid>` (UPG_MXCLI, as localedits.py). The raw table is kept per module as <versions-dir>/versions-<cid>.txt
(default: modvers/ beside localedits.json) and read from there first, so a rerun and an offline run need no network;
--no-fetch never calls mxcli. Nothing here names a version: every number comes from the arguments or those tables.

One line per module:
  PICK      Module 4.4.0 -> 4.5.0 (min Mendix 10.24.0)
  CURRENT   Module 4.5.0: no newer version fits 11.12.2 (newest that fits: 4.5.0)
  STRANDED  Module 3.0.0: no version at all has a min Mendix at or below 11.12.2 (list it in stranded.md, steps/triage.md)
  SKIP      Module: renamed / republished (renamed_modules.py) or named in --skip; not a version update
  NOT PICKED Module: <why>   no content id, versions not fetched, table unreadable: never a pass
Prereleases (a letter in the version) and rows whose version or min Mendix cannot be read are ignored and counted.

--out writes the plan ("<content id> <version> <Module>   # was <installed>"; refuses an existing file unless --force,
which keeps the old one as <out>.pre-modplan, .1, .2 ...). --jumps writes "<Module> <installed> -> <new> <content id>", the form diff.py --module-jumps, proposal.py and
release_impact.py --plan read. Order: the lines keep the module order of localedits.json,
--last moves the named modules to the end, and --app (an app folder or .mpr) puts the target of a cross-module
association before its owner, planorder.py's rule (PV-2), whose CYCLE and NOTE lines are printed too.
Widget providers (field run RKT, 10.5 -> 11.12): a module whose new package uses a pluggable widget that another PLANNED module's
new package ships goes after that module. Administration 4.5.0 uses the Combo box widget that Atlas_Core 3.22.1 ships; listed
first, its step stopped with 7 CE0462 "could not find widget". Read from the packages themselves (<content id>-<version>.mpk in
--cache, default UPG_CACHE or ~/.cache/upgrade-toolkit/mpk; one that is not cached is downloaded like planbuild.py does, never
with --no-fetch): the widget ids on the pages of the package's project.mpr against the widgets/*.mpk the other packages hold.
Printed: `ORDER <Provider> before <User>: ...` per pair, and always one `widget order:` line with the denominator (packages read
of planned). A package that could not be read is named there and its widget needs are NOT in the order: never read as "needs
none". A cycle between providers is said (`CYCLE-WIDGET`) and the widget order is not applied.
While any module is NOT PICKED nothing is written (exit 3); --allow-unresolved writes the files with a
"# NOT PICKED <Module>: <why>" comment per module and still exits 3.
Exit: 0 every module resolved, 3 at least one NOT PICKED, 2 input error.
"""
import argparse, io, json, os, re, shutil, sys, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

VER = re.compile(r"^\d+(?:\.\d+){1,3}$")


def tup(s):
    t = tuple(int(x) for x in s.split("."))
    return t + (0,) * (4 - len(t))  # 4.5 == 4.5.0


def parse_versions(text):
    """(rows [(version, min mendix)], ignored count) from `mxcli marketplace versions <id>` output.
    Rows are '<version> <min mendix> <date> <name...>' under a VERSION header; the version must be a plain release."""
    rows, ignored = [], 0
    for ln in text.splitlines():
        p = ln.split()
        if len(p) < 3 or p[0] == "VERSION" or not re.match(r"^\d", p[0]):
            continue
        if VER.match(p[0]) and VER.match(p[1]):
            rows.append((p[0], p[1]))
        else:
            ignored += 1
    return rows, ignored


def fetch(cid, path):
    """Run mxcli and keep the table. Returns (ok, why)."""
    import localedits  # late: it reads UPG_MXCLI at import
    if not (os.path.isfile(localedits.MXCLI) or shutil.which(localedits.MXCLI)):
        return False, "no table cached and no mxcli to fetch it (UPG_MXCLI)"
    r, net = localedits.run_retry([localedits.MXCLI, "marketplace", "versions", str(cid)], f"versions {cid}")
    if r.returncode != 0:
        return False, ("network error fetching versions" if net else
                       "mxcli marketplace versions failed: " + ((r.stderr or r.stdout).strip().splitlines() or ["?"])[-1][:80])
    if not parse_versions(r.stdout)[0]:
        return False, "mxcli listed no versions"
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(r.stdout)
    return True, ""


def pkg_widgets(cache, cid, ver, download):
    """(uses, provides, why): widget ids the package's own pages use (less its own), widget ids its widgets/*.mpk declare; why is
    the reason the package was not read (uses and provides are then None)."""
    import planbuild
    mpk, why = planbuild.package(cid, ver, cache, download)
    if not mpk:
        return None, None, why
    provides = set()
    xdir = mpk[:-4]
    xmpr = os.path.join(xdir, "project.mpr")  # the layout crosscalls.package_model extracts to
    try:
        with zipfile.ZipFile(mpk) as z:
            for n in z.namelist():
                if re.match(r"widgets/[^/]+\.mpk$", n):
                    try:
                        with zipfile.ZipFile(io.BytesIO(z.read(n))) as w:
                            for x in w.namelist():
                                if x.endswith(".xml"):
                                    provides.update(re.findall(r'<widget[^>]*\sid="([^"]+)"', w.read(x).decode("utf-8", "replace")))
                    except zipfile.BadZipFile:
                        pass
            if not os.path.exists(xmpr):
                names = [n for n in z.namelist() if n.endswith(".mpr")]
                if not names:
                    return None, None, "package holds no model (.mpr)"
                z.extract(names[0], xdir)
                if names[0] != "project.mpr":
                    os.rename(os.path.join(xdir, names[0]), xmpr)
    except (OSError, zipfile.BadZipFile) as ex:
        return None, None, f"package unreadable ({type(ex).__name__})"
    sys.path.insert(0, os.path.join(HERE, "repair"))
    import missing_deps
    uses = set()

    def walk(d):
        if isinstance(d, dict):
            if d.get("$Type") == "CustomWidgets$CustomWidgetType" and d.get("WidgetId"):
                uses.add(d["WidgetId"])
            for v in d.values():
                walk(v)
        elif isinstance(d, list):
            for v in d:
                walk(v)
    try:
        for d in missing_deps.units(xmpr):
            if d.get("Excluded") is not True:  # excluded documents are not built
                walk(d)
    except SystemExit:
        return None, None, "model not readable here (needs the bson module)"
    except Exception as ex:
        return None, None, f"model unreadable ({type(ex).__name__})"
    return uses - provides, provides, ""


def widget_edges(order, uses, provides):
    """{(user, provider): [widget ids]}: the user needs the provider first. A widget that a planned module already ahead of the
    user ships needs no pair; otherwise the first provider in the current order is the one."""
    pos = {m: i for i, m in enumerate(order)}
    e = {}
    for u in order:
        for w in sorted(uses.get(u) or ()):
            ps = [r for r in order if r != u and w in (provides.get(r) or ())]
            if ps and not any(pos[r] < pos[u] for r in ps):
                e.setdefault((u, ps[0]), []).append(w)
    return e


def pick(installed, rows, target):
    """('PICK', version, min) | ('CURRENT', newest fitting) | ('STRANDED', None)."""
    fit = [r for r in rows if tup(r[1]) <= target]
    if not fit:
        return "STRANDED", None
    best = max(fit, key=lambda r: tup(r[0]))
    if tup(best[0]) <= tup(installed):
        return "CURRENT", best[0]
    return "PICK", best


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("localedits"); ap.add_argument("--target", required=True)
    ap.add_argument("--out"); ap.add_argument("--jumps"); ap.add_argument("--app")
    ap.add_argument("--versions-dir"); ap.add_argument("--no-fetch", action="store_true")
    ap.add_argument("--skip", default=""); ap.add_argument("--last", default="")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--allow-unresolved", action="store_true")
    ap.add_argument("--cache", default=os.environ.get("UPG_CACHE") or os.path.expanduser("~/.cache/upgrade-toolkit/mpk"))
    a = ap.parse_args()
    if not VER.match(a.target):
        print(f"modplan: --target {a.target}: not a Mendix version", file=sys.stderr); return 2
    try:
        mods = json.load(open(a.localedits, encoding="utf-8"))
        assert isinstance(mods, list) and all(isinstance(m, dict) and m.get("name") for m in mods)
    except (OSError, ValueError, AssertionError):
        print(f"modplan: {a.localedits}: not a localedits.json (a list of modules with name, cid, version)", file=sys.stderr)
        return 2
    target = tup(a.target)
    vdir = a.versions_dir or os.path.join(os.path.dirname(os.path.abspath(a.localedits)), "modvers")
    skip = {x for x in a.skip.split(",") if x}
    last = [x for x in a.last.split(",") if x]
    import renamed_modules
    renamed = set()
    try:
        renamed = {r["module"] for r in renamed_modules.find(mods)}
    except Exception:  # a table problem must not stop the plan: the proposal still lists the rename
        pass
    plan, unresolved, ignored_total, notes = [], 0, 0, []

    def not_picked(n, why):
        nonlocal unresolved
        unresolved += 1
        notes.append(f"# NOT PICKED {n}: {why}")
        print(f"NOT PICKED {n}: {why}")
    for m in mods:
        n, cid, inst = m["name"], m.get("cid"), m.get("version") or ""
        if n in skip or n in renamed:
            print(f"SKIP {n}: " + ("named in --skip" if n in skip else "renamed or republished (renamed_modules.py): not a version update"))
            continue
        if not cid:
            not_picked(n, f"no content id in the MPR; give it with localedits.py --cid {n}=<id>")
            continue
        if not VER.match(inst):
            not_picked(n, f"installed version not comparable ({inst or 'none'!r}): not a plain release, so no newer one can be told from a downgrade")
            continue
        path = os.path.join(vdir, f"versions-{cid}.txt")
        cached = os.path.isfile(path)
        if not cached:
            ok, why = (False, "versions not cached and --no-fetch given") if a.no_fetch else fetch(cid, path)
            if not ok:
                not_picked(n, why)
                continue
        rows, ign = parse_versions(open(path, encoding="utf-8", errors="replace").read())
        ignored_total += ign
        if not rows:
            not_picked(n, f"{path} has no readable version rows")
            continue
        kind, v = pick(inst, rows, target)
        if kind == "STRANDED":
            print(f"STRANDED {n} {inst}: no version at all has a min Mendix at or below {a.target} (list it in stranded.md, steps/triage.md)")
        elif kind == "CURRENT":
            print(f"CURRENT {n} {inst}: no newer version fits {a.target} (newest that fits: {v})" + (" (cached)" if cached else ""))
        else:
            plan.append((n, cid, v[0], inst))
            print(f"PICK {n} {inst} -> {v[0]} (min Mendix {v[1]})" + (" (cached)" if cached else ""))
    plan.sort(key=lambda r: (r[0] in last, last.index(r[0]) if r[0] in last else 0))
    names = [p[0] for p in plan]
    e_assoc, model = {}, None
    if a.app and plan:
        import idcheck, planorder
        try:
            dm, _ = idcheck.load(a.app)
            model = idcheck.build(dm)
        except (SystemExit, Exception) as ex:
            print(f"modplan: --app {a.app}: {ex}", file=sys.stderr); return 2
        e_assoc = planorder.edges(model, set(names))
    uses, provides, unread, e_widget = {}, {}, [], {}
    if len(plan) > 1:
        for n, cid, v, _ in plan:
            u, pr, why = pkg_widgets(a.cache, cid, v, not a.no_fetch)
            if pr is None:
                unread.append(f"{n} {v} ({why})")
            else:
                uses[n], provides[n] = u, pr
        e_widget = widget_edges(names, uses, provides)
        print(f"widget order: {len(uses)} of {len(plan)} planned package(s) read"
              + (f"; NOT read, their widget needs are not in the order: {'; '.join(unread)}" if unread else "")
              + (f"; {len(e_widget)} provider-before-user pair(s)" if e_widget else ""))
    if model is not None or e_widget:
        import planorder
        new, cyc = planorder.order(names, {**e_widget, **e_assoc})
        if cyc and e_widget:  # a cycle through the widget pairs: say so, keep the association rule alone
            print(f"CYCLE-WIDGET {', '.join(cyc)}: they use each other's widgets, no widget provider order exists on the plan; "
                  "the widget order is NOT applied")
            e_widget = {}
            new, cyc = planorder.order(names, e_assoc)
        for c in cyc:
            print(f"CYCLE {c} is part of a cross-module association cycle on the plan: cannot be ordered, reimport its owner after both")
        ver = {p[0]: p[2] for p in plan}
        for (u, r), ws in sorted(e_widget.items()):
            print(f"ORDER {r} before {u}: {u} {ver[u]} uses the widget {ws[0].rsplit('.', 1)[-1]} ({ws[0]}"
                  f"{', +%d more' % (len(ws) - 1) if len(ws) > 1 else ''}), which {r} {ver[r]} ships; "
                  f"install/update {r} first, or the {u} step stops with CE0462 (could not find widget)")
        by = {p[0]: p for p in plan}
        plan = [by[x] for x in new]
        if model is not None:
            for (own, tgt), nm in sorted(planorder.kept_owner_notes(model, set(names)).items()):
                print(f"NOTE {tgt} is planned, its owner {own} is not (kept): the {tgt} update drops {len(nm)} association(s); "
                      f"replay route (steps/upgrade.md item 1) or keep {tgt}")
    print(f"modplan: {len(mods)} module(s): {len(plan)} to update, {unresolved} not picked"
          + (f"; {ignored_total} unreadable or prerelease row(s) ignored" if ignored_total else "")
          + ("; not picked is not a pass" if unresolved else ""))
    outs = [(p, k) for p, k in ((a.out, "plan"), (a.jumps, "jumps")) if p]
    if unresolved and outs and not a.allow_unresolved:
        print(f"modplan: {unresolved} module(s) NOT PICKED: nothing written (a plan without them would drop them silently); "
              "fix the cause, or --allow-unresolved writes the files with a '# NOT PICKED' comment per module", file=sys.stderr)
        return 3
    for path, _ in outs:  # both paths are checked before either is written
        if os.path.exists(path) and not a.force:
            print(f"modplan: {path} exists; --force keeps it as {path}.pre-modplan and writes the new one", file=sys.stderr)
            return 2
    for path, kind in outs:
        if os.path.exists(path):
            bak, k = path + ".pre-modplan", 0
            while os.path.exists(bak):
                k += 1; bak = f"{path}.pre-modplan.{k}"
            shutil.copyfile(path, bak)
        if kind == "plan":
            body = "".join(f"{c} {v} {n}   # was {o}\n" for n, c, v, o in plan)
        else:  # "<Module> <old> -> <new> <cid>": the form diff.py, proposal.py and release_impact.py read
            body = "".join(f"{n} {o} -> {v} {c}\n" for n, c, v, o in plan)
        body = "".join(x + "\n" for x in notes) + body
        tmp = path + ".tmp"
        with open(tmp, "w", encoding="utf-8") as fh:
            fh.write(body if plan or notes else "# no module update fits the target\n")
        os.replace(tmp, path)
        print(f"modplan: wrote {path} ({len(plan)} line(s))")
    return 3 if unresolved else 0


if __name__ == "__main__":
    sys.exit(main())
