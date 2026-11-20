#!/usr/bin/env python3
"""planbuild.py: which plan lines name a package Mendix 11 cannot import? (GM-17)

  planbuild.py <plan.txt> --target 11.12.2 [--cache DIR] [--no-download] [--write]

Mendix 11 refuses every module package built with Studio Pro before 10.21 (exit 117, "range from 10.21.0 to
10.24.99"). "Min Mendix" in the catalog is not the build version: BizzomateDevTools 2.0.2 and 3.0.0 were planned
and the run-time SKIP in stepupdate.sh found out only mid-batch. This reads the build version from each planned
package up front: _MetaData._ProductVersion of the project.mpr inside the .mpk, through mxversion.py (the same
reader the add-on check uses; below() is the shared "older than 10.21" test).

plan.txt lines are "<content id> <version> <Module>" (# comments allowed). The package is the cached
<content id>-<version>.mpk (UPG_CACHE, the localedits.py cache); one that is not cached is downloaded with
`mxcli marketplace download` the way localedits does, unless --no-download. One line per plan entry:

  KEEP         Module 3.1.0: built with 10.24.1.1, importable on 11
  DROPPED      Module 2.0.2: built with 10.5.0.1, 11 needs >= 10.21 (belongs in plan-pre.txt, before the convert, or stays out)
  NOT CHECKED  Module 3.0.0: <why>: build version unknown; the run-time SKIP in stepupdate.sh is the only guard left

Not checked is never a pass: it is counted on the last line and exit 3 says so. A target below 11 checks nothing
(prints one line, exit 0). --write rewrites plan.txt with each DROPPED line turned into a "# dropped: ..." comment
(the old file is kept as plan.txt.pre-gm17); NOT CHECKED lines stay.
Exit: 0 every line checked and none dropped (or target < 11), 1 a line dropped, 3 none dropped but a line not
checked, 2 input error. A dropped line wins over not checked.
"""
import argparse, os, re, shutil, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mxversion import below, mxmodule_version  # noqa: E402

MIN_MAJOR, MIN_MINOR = 10, 21


def package(cid, ver, cache, download):
    """(path or None, why not)."""
    mpk = os.path.join(cache, f"{cid}-{ver}.mpk")
    if os.path.isfile(mpk):
        return mpk, ""
    if not download:
        return None, "package not cached"
    try:
        import localedits  # imported late: it reads UPG_MXCLI at import
        if not (os.path.exists(localedits.MXCLI) or shutil.which(localedits.MXCLI)):
            return None, "package not cached and no mxcli to download it"
        _mpr, err, net = localedits.fetch_pkg(cid, ver, cache)
    except Exception as e:  # a plan-time look must never crash the triage
        return None, f"download failed ({type(e).__name__})"
    if err:
        return None, ("network error on download" if net else "download failed: " + " ".join(err)[:80])
    return (mpk, "") if os.path.isfile(mpk) else (None, "download failed")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("plan"); ap.add_argument("--target", required=True)
    ap.add_argument("--cache", default=os.environ.get("UPG_CACHE") or os.path.expanduser("~/.cache/upgrade-toolkit/mpk"))
    ap.add_argument("--no-download", action="store_true"); ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    if not os.path.isfile(a.plan):
        print(f"planbuild: {a.plan}: not a file", file=sys.stderr); sys.exit(2)
    m = re.match(r"^(\d+)", a.target)
    if not m:
        print(f"planbuild: --target {a.target}: not a Mendix version", file=sys.stderr); sys.exit(2)
    if int(m.group(1)) < 11:
        print(f"planbuild: target {a.target} is below 11, no package is refused for its build version; nothing checked"); return
    kept = dropped = unchecked = 0
    out = []
    for l in open(a.plan, encoding="utf-8").read().splitlines():
        f = l.split()
        if len(f) < 3 or l.lstrip().startswith("#"):
            out.append(l); continue
        cid, ver, mod = f[0], f[1], f[2]
        mpk, why = package(cid, ver, a.cache, not a.no_download)
        built = mxmodule_version(mpk) if mpk else None
        if mpk and not built:
            why = "package has no readable project.mpr"
        if not built:
            unchecked += 1; out.append(l)
            print(f"NOT CHECKED {mod} {ver}: {why}: build version unknown; the run-time SKIP in stepupdate.sh is the only guard left")
        elif below(built, MIN_MAJOR, MIN_MINOR):
            dropped += 1; out.append(f"# dropped: {mod} {ver} built with {built}, 11 needs >= {MIN_MAJOR}.{MIN_MINOR} (was: {l.strip()})")
            print(f"DROPPED {mod} {ver}: built with {built}, 11 needs >= {MIN_MAJOR}.{MIN_MINOR} "
                  f"(belongs in plan-pre.txt, before the convert, or stays out)")
        else:
            kept += 1; out.append(l)
            print(f"KEEP {mod} {ver}: built with {built}, importable on 11")
    print(f"planbuild: {kept + dropped + unchecked} plan line(s): {kept} kept, {dropped} dropped, {unchecked} not checked"
          + ("; not checked is not a pass" if unchecked else ""))
    if a.write and dropped:
        shutil.copyfile(a.plan, a.plan + ".pre-gm17")
        open(a.plan, "w", encoding="utf-8").write("\n".join(out) + "\n")
        print(f"planbuild: wrote {a.plan} (old file kept as {a.plan}.pre-gm17)")
    sys.exit(1 if dropped else 3 if unchecked else 0)


if __name__ == "__main__":
    main()
