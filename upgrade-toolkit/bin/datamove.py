#!/usr/bin/env python3
"""datamove.py: prove a run-once data move (scenario D) moved every value: count in the target = count in the baseline.

Why (data test 2026-11-16, scenario D; WM1 MendixSSO.AuthRequest.Nonce): data the app keeps in a vendor module must move
to <Module>_Ext before the update drops the column. However the move runs (RUN-ONCE-DESIGN.md: a deploy before the
update, or SQL), the gate needs the same proof: every non-null value in the source on the baseline is in the target after.

  datamove.py check --plan datamove.txt --before-psql "docker exec -i PG psql -U mendix -d BASE" --after-psql "... -d AFTER"

datamove.txt: one move per line, '#' comments:   Src.Entity.Attr -> Dst.Entity.Attr   [# reason]
Per line: MOVED (target >= source), LOST (target < source), or UNCOUNTED (a count failed). Exit 0 when every line is
MOVED, 1 on LOST or UNCOUNTED, 2 on a malformed plan.
"""
import argparse, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from platform_drops import count, sql_for

LINE = re.compile(r"^\s*([A-Za-z]\w*\.\w+\.\w+)\s*->\s*([A-Za-z]\w*\.\w+\.\w+)\s*(?:#.*)?$")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("check")
    c.add_argument("--plan", required=True); c.add_argument("--before-psql", required=True); c.add_argument("--after-psql", required=True)
    a = ap.parse_args()
    moves = []
    for n, ln in enumerate(open(a.plan), 1):
        if not ln.strip() or ln.lstrip().startswith("#"):
            continue
        m = LINE.match(ln)
        if not m:
            print(f"datamove: {a.plan}:{n}: not 'Src.Entity.Attr -> Dst.Entity.Attr': {ln.strip()}", file=sys.stderr)
            return 2
        moves.append(m.groups())
    bad = 0
    for src, dst in moves:
        nb, na = count(a.before_psql, sql_for(src)[0]), count(a.after_psql, sql_for(dst)[0])
        if nb is None or na is None:
            verdict, bad = "UNCOUNTED", bad + 1
        elif na < nb:
            verdict, bad = "LOST", bad + 1
        else:
            verdict = "MOVED"
        show = lambda x: "count failed" if x is None else str(x)
        print(f"{verdict} {src} -> {dst}: {show(nb)} before, {show(na)} after")
    print(f"datamove: {len(moves) - bad} of {len(moves)} moves proven")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
