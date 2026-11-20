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
which keeps the old one as <out>.pre-modplan, .1, .2 ...). --jumps writes the same lines with the installed version as
a fourth field, the input of release_impact.py --plan. Order: the lines keep the module order of localedits.json,
--last moves the named modules to the end, and --app (an app folder or .mpr) puts the target of a cross-module
association before its owner, planorder.py's rule (PV-2), whose CYCLE and NOTE lines are printed too.
Exit: 0 every module resolved, 3 at least one NOT PICKED, 2 input error.
"""
import argparse, json, os, re, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

VER = re.compile(r"^\d+(?:\.\d+){1,3}$")


def tup(s):
    return tuple(int(x) for x in s.split("."))


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


def pick(installed, rows, target):
    """('PICK', version, min) | ('CURRENT', newest fitting) | ('STRANDED', None)."""
    fit = [r for r in rows if tup(r[1]) <= target]
    if not fit:
        return "STRANDED", None
    best = max(fit, key=lambda r: tup(r[0]))
    if VER.match(installed or "") and tup(best[0]) <= tup(installed):
        return "CURRENT", best[0]
    return "PICK", best


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("localedits"); ap.add_argument("--target", required=True)
    ap.add_argument("--out"); ap.add_argument("--jumps"); ap.add_argument("--app")
    ap.add_argument("--versions-dir"); ap.add_argument("--no-fetch", action="store_true")
    ap.add_argument("--skip", default=""); ap.add_argument("--last", default="")
    ap.add_argument("--force", action="store_true")
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
    plan, unresolved, ignored_total = [], 0, 0
    for m in mods:
        n, cid, inst = m["name"], m.get("cid"), m.get("version") or ""
        if n in skip or n in renamed:
            print(f"SKIP {n}: " + ("named in --skip" if n in skip else "renamed or republished (renamed_modules.py): not a version update"))
            continue
        if not cid:
            unresolved += 1
            print(f"NOT PICKED {n}: no content id in the MPR; give it with localedits.py --cid {n}=<id>")
            continue
        path = os.path.join(vdir, f"versions-{cid}.txt")
        if not os.path.isfile(path):
            ok, why = (False, "versions not cached and --no-fetch given") if a.no_fetch else fetch(cid, path)
            if not ok:
                unresolved += 1
                print(f"NOT PICKED {n}: {why}")
                continue
        rows, ign = parse_versions(open(path, encoding="utf-8", errors="replace").read())
        ignored_total += ign
        if not rows:
            unresolved += 1
            print(f"NOT PICKED {n}: {path} has no readable version rows")
            continue
        kind, v = pick(inst, rows, target)
        if kind == "STRANDED":
            print(f"STRANDED {n} {inst}: no version at all has a min Mendix at or below {a.target} (list it in stranded.md, steps/triage.md)")
        elif kind == "CURRENT":
            print(f"CURRENT {n} {inst}: no newer version fits {a.target} (newest that fits: {v})")
        else:
            plan.append((n, cid, v[0], inst))
            print(f"PICK {n} {inst or '?'} -> {v[0]} (min Mendix {v[1]})")
    plan.sort(key=lambda r: (r[0] in last, last.index(r[0]) if r[0] in last else 0))
    if a.app and plan:
        import idcheck, planorder
        try:
            dm, _ = idcheck.load(a.app)
            model = idcheck.build(dm)
        except (SystemExit, Exception) as ex:
            print(f"modplan: --app {a.app}: {ex}", file=sys.stderr); return 2
        names = [p[0] for p in plan]
        e = planorder.edges(model, set(names))
        new, cyc = planorder.order(names, e)
        for c in cyc:
            print(f"CYCLE {c} is part of a cross-module association cycle on the plan: cannot be ordered, reimport its owner after both")
        by = {p[0]: p for p in plan}
        plan = [by[x] for x in new]
        for (own, tgt), nm in sorted(planorder.kept_owner_notes(model, set(names)).items()):
            print(f"NOTE {tgt} is planned, its owner {own} is not (kept): the {tgt} update drops {len(nm)} association(s); "
                  f"replay route (steps/upgrade.md item 1) or keep {tgt}")
    print(f"modplan: {len(mods)} module(s): {len(plan)} to update, {unresolved} not picked"
          + (f"; {ignored_total} unreadable or prerelease row(s) ignored" if ignored_total else "")
          + ("; not picked is not a pass" if unresolved else ""))
    for path, with_old in ((a.out, False), (a.jumps, True)):
        if not path:
            continue
        if os.path.exists(path):
            if not a.force:
                print(f"modplan: {path} exists; --force keeps it as {path}.pre-modplan and writes the new one", file=sys.stderr)
                return 2
            bak, k = path + ".pre-modplan", 0
            while os.path.exists(bak):
                k += 1; bak = f"{path}.pre-modplan.{k}"
            shutil.copyfile(path, bak)
        body = "".join(f"{c} {v} {n}   # was {o or '?'}\n" if not with_old else f"{c} {v} {n} {o or '?'}\n"
                       for n, c, v, o in plan)
        tmp = path + ".tmp"
        with open(tmp, "w", encoding="utf-8") as fh:
            fh.write(body or "# no module update fits the target\n")
        os.replace(tmp, path)
        print(f"modplan: wrote {path} ({len(plan)} line(s))")
    return 3 if unresolved else 0


if __name__ == "__main__":
    sys.exit(main())
