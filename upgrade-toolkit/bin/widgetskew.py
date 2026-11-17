#!/usr/bin/env python3
"""widgetskew.py: did a module update replace a widget whose styles belong to a module that stayed at its old version?

  widgetskew.py <app dir> --plan <plan.txt> [--cache DIR]

Why (cold CMM, 9.24.2 -> 10.24.28): Atlas_Web_Content 3.9.0 brought Datagrid 2.30.6 into widgets/ (was 2.2.2), while
DataWidgets, whose package ships that widget and whose themesource/datawidgets holds its styles, was kept (FILES-EDITED).
Every data grid page rendered as unstyled rows; afterwalk passed 23/23 (the data is on the page) and the screens rung
only said REVIEW on each one.

Reads .stepupdate/widgets.txt (the widgets each module step changed, written by stepupdate) and .stepupdate/kept.txt.
For each kept module that has a plan line ("<content id> <version> <module>"), the cached package <id>-<version>.mpk
lists the widgets its target version ships; a widget another step replaced is a skew:

  WIDGET-SKEW Datagrid 2.2.2 -> 2.30.6 (by Atlas_Web_Content 3.9.0) ships with DataWidgets 3.11.8; DataWidgets stays at
    the installed version, its theme styles do not match the new widget

Exit: 0 = no skew, 1 = a skew (update the kept module, or put the old widget back), 2 = input error.
A kept module without a cached package is named on a NOTE line and not counted.
"""
import argparse, os, re, sys, zipfile


def steps(app):
    """{widget file: (name, old, new, by)} from .stepupdate/widgets.txt (last step wins)."""
    out, p = {}, os.path.join(app, ".stepupdate", "widgets.txt")
    for line in open(p, encoding="utf-8") if os.path.isfile(p) else []:
        by, _, rest = line.strip().partition(": ")
        for part in rest.split("; "):
            m = re.match(r"(\S+\.mpk) (.+?) (\S+) -> (\S+)$", part.strip())
            if m:
                out[os.path.basename(m.group(1))] = (m.group(2), m.group(3), m.group(4), by)
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("app"); ap.add_argument("--plan", required=True)
    ap.add_argument("--cache", default=os.environ.get("UPG_CACHE") or os.path.expanduser("~/.cache/upgrade-toolkit/mpk"))
    a = ap.parse_args()
    if not os.path.isfile(a.plan):
        sys.exit(f"widgetskew: {a.plan}: not a file")
    kp = os.path.join(a.app, ".stepupdate", "kept.txt")
    kept = [l.split()[0] for l in open(kp, encoding="utf-8") if l.strip()] if os.path.isfile(kp) else []
    plan = {}
    for l in open(a.plan, encoding="utf-8"):
        f = l.split()
        if len(f) >= 3 and not l.lstrip().startswith("#"):
            plan[f[2]] = (f[0], f[1])
    changed, skew = steps(a.app), 0
    for mod in kept:
        if mod not in plan:
            continue
        cid, ver = plan[mod]
        mpk = os.path.join(a.cache, f"{cid}-{ver}.mpk")
        try:
            ships = {os.path.basename(n) for n in zipfile.ZipFile(mpk).namelist() if re.match(r"widgets/[^/]+\.mpk$", n)}
        except (OSError, zipfile.BadZipFile):
            print(f"NOTE {mod} {ver}: no cached package ({mpk}), its widgets not checked"); continue
        for w in sorted(ships & set(changed)):
            name, old, new, by = changed[w]
            if by.split()[0] == mod:
                continue
            skew += 1
            print(f"WIDGET-SKEW {name} {old} -> {new} (by {by}) ships with {mod} {ver}; {mod} stays at the installed version, "
                  f"its theme styles do not match the new widget")
    print(f"widgetskew: {len(kept)} kept module(s), {skew} widget(s) replaced under a kept module"
          + ("; repair: steps/repair.md row 32" if skew else ""))
    sys.exit(1 if skew else 0)


if __name__ == "__main__":
    main()
