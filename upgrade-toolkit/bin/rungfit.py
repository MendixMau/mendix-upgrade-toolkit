#!/usr/bin/env python3
"""rungfit.py: does every plan line install on the Mendix version the plan runs at? (WK-6, WKS and ERRH field runs 2026-11)

  rungfit.py <plan.txt> --at 10.24.13.86719 --modvers <work>/modvers

On a ladder (10.x below 10.24 -> 10.24 -> 11) each plan runs on one rung: plan-pre.txt before the convert, at the SOURCE
version; plan.txt after it, at the version the project then has. A pick made for the final target (Atlas_Core 4.7.1, min
Mendix 11.0.0) fails on the 10.24 rung with "requires Mendix 11.0.0, and the project is 10.24.13", and a 10.24 pick fails
before the convert at 10.21.1 the same way: every line KEPT, no cause named. This reads the MIN MENDIX of each line's
version from the table modplan.py caches ($WORK/modvers/versions-<content id>.txt) and names the lines that do not fit.

plan lines: "<content id> <version> <Module>" (# comments allowed). Output, one line per plan entry:
  FIT       Module 3.22.1: min Mendix 10.24.0, project 10.24.13
  MISFIT    Module 4.7.1: min Mendix 11.0.0 is above 10.24.13 (pick for this rung: modplan.py --target 10.24.13...)
  NOT CHECKED  Module 1.0.0: no version table for content id N / version not in it
Exit: 0 all fit (or not checked: counted on the last line), 1 a line misfits, 2 input error.
"""
import os, re, sys


def key(v):  # fixed length 4, like modplan.py tup: 10.24.0.0 == 10.24.0
    t = tuple(int(x) for x in re.findall(r"\d+", v)[:4])
    return t + (0,) * (4 - len(t))


def main(argv):
    if len(argv) < 2 or "--at" not in argv or "--modvers" not in argv:
        print(__doc__.split("\n\n")[0], file=sys.stderr)
        return 2
    plan = argv[1]
    at = argv[argv.index("--at") + 1]
    mv = argv[argv.index("--modvers") + 1]
    if not os.path.isfile(plan) or not at:
        print(f"rungfit: no plan {plan} or no version", file=sys.stderr)
        return 2
    bad = unk = n = 0
    for raw in open(plan, encoding="utf-8"):
        line = raw.split("#")[0].strip()
        if not line:
            continue
        p = line.split()
        if len(p) < 3:
            continue
        cid, ver, mod = p[0], p[1], p[2]
        n += 1
        t = os.path.join(mv, f"versions-{cid}.txt")
        mn = None
        if os.path.isfile(t):
            for r in open(t, encoding="utf-8"):
                c = r.split()
                if len(c) >= 2 and c[0] == ver:
                    mn = c[1]
        if mn is None:
            unk += 1
            print(f"NOT CHECKED  {mod} {ver}: no version table for content id {cid} or the version is not in it")
        elif key(mn) > key(at):
            bad += 1
            print(f"MISFIT    {mod} {ver}: min Mendix {mn} is above {at}: pick the newest version that fits this rung "
                  f"(modplan.py --target {at}), and keep the later pick in the next rung's plan")
        else:
            print(f"FIT       {mod} {ver}: min Mendix {mn}, project {at}")
    print(f"rungfit: {n} line(s), {bad} misfit, {unk} not checked")
    return 1 if bad else 0


sys.exit(main(sys.argv))
