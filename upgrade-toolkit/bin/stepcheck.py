#!/usr/bin/env python3
"""stepcheck.py: did one module update add model errors? The question after each step, before the step is committed.

  stepcheck.py BEFORE.log AFTER.log --module M --version V [--accepted FILE] [--fields] [--max N]

BEFORE.log and AFTER.log are `mx check` outputs of the app as it was before the update and as it is with the update applied.
Why (GM-23 / A-1, a community gamification app, 314 entities): stepupdate accepted a step on the data check alone, mx check ran
only at the build after every update, and steps that left 31 and 4 CE1613 were committed; the commit even went in a chained
command before the check was read. The error that the update caused was found many commits later, with the cause buried.

New errors = the error lines the AFTER log has more of than BEFORE, counted line by line (code, message and place), so an
update that fixes 3 errors and adds 3 others is still a finding. Lines that BEFORE already had are not the step's.
--accepted FILE holds earlier answers, one per line: `<Module> <CODE>[,<CODE>...]  # who and why`; errors of those codes are
left out for that module only.

Prints `NEW <code> <line>` rows, then a summary line. With --fields, for upgrade-pipeline.sh to turn into the stop
(nj_meta person ...), one field per line, tab separated, the shape bin/widgetfix.py uses:
  Q question   R recommended key   O key|label|what the reader notices   W key|file|line   B one line of the body
Exit: 0 = no new error, 1 = new errors, 2 = unreadable input, 3 = the AFTER check did not finish (a crash is no verdict).
"""
import argparse, collections, re, sys

LINE = re.compile(r"^\[error\]\s*\[(CE\d+)\]\s*(.*)$")
SUMMARY = re.compile(r"The app contains:\s*(\d+) errors")
# what a reader notices; only codes whose meaning is certain. Anything else is said with its code.
SAYS = {"CE1613": "something refers to an element that is gone",
        "CE0463": "a widget no longer matches the settings saved on its pages"}


def read(path):
    try:
        t = open(path, errors="replace").read()
    except OSError as e:
        print(f"stepcheck: {path}: {e}", file=sys.stderr)
        sys.exit(2)
    rows = [m.groups() for m in map(LINE.match, t.splitlines()) if m]
    died = any(l.startswith("[error] [MXCHECK]") for l in t.splitlines()) or (SUMMARY.search(t) is None and not rows)
    return rows, died


def new_errors(before, after, accepted):
    have = collections.Counter(before)
    out = []
    for r in after:
        if have[r] > 0:
            have[r] -= 1
        elif r[0] not in accepted:
            out.append(r)
    return out


def accepted_for(path, module):
    codes = set()
    if not path:
        return codes
    try:
        for line in open(path, errors="replace"):
            body = line.split("#", 1)[0].split()
            if len(body) >= 2 and body[0] == module:
                codes |= {c.strip().upper() for c in " ".join(body[1:]).replace(",", " ").split()}
    except OSError:
        pass
    return codes


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("before"); ap.add_argument("after")
    ap.add_argument("--module", required=True); ap.add_argument("--version", default="")
    ap.add_argument("--accepted"); ap.add_argument("--fields", action="store_true"); ap.add_argument("--max", type=int, default=8)
    a = ap.parse_args()
    (before, bdied), (after, adied) = read(a.before), read(a.after)
    if adied:
        print(f"stepcheck: the check after {a.module} did not finish (see {a.after}); a crash is not 0 errors", file=sys.stderr)
        return 3
    if bdied:
        print(f"stepcheck: the check before {a.module} did not finish (see {a.before}): no baseline to compare with", file=sys.stderr)
        return 3
    new = new_errors(before, after, accepted_for(a.accepted, a.module))
    if not new:
        print(f"stepcheck: {a.module} {a.version}: no new error ({len(before)} before, {len(after)} after)")
        return 0
    per = collections.Counter(c for c, _ in new)
    codes = ", ".join(f"{c} x{n}" for c, n in sorted(per.items()))
    for c, m in new[:a.max]:
        print(f"NEW {c} {m}")
    if len(new) > a.max:
        print(f"NEW ... {len(new) - a.max} more (the full list: {a.after})")
    print(f"stepcheck: {a.module} {a.version}: {len(new)} new error(s) ({codes}); {len(before)} before, {len(after)} after")
    if not a.fields:
        return 1
    mod, ver = a.module, a.version
    says = "; ".join(f"{c}: {SAYS[c]}" for c in sorted(per) if c in SAYS)
    q = (f"Updating {mod}{' to ' + ver if ver else ''} breaks the model: {len(new)} new error(s) ({codes}) that the app did not have "
         f"before this update{' (' + says + ')' if says else ''}. The app would not build until they are repaired. What should we do?")
    print(f"Q\t{q}")
    print("R\tkeep")
    print(f"O\tkeep|Keep {mod} at the installed version|The update is undone and {mod} stays as it is, so the app checks as clean as before; "
          f"modules that need the newer {mod} are listed as kept")
    print(f"O\taccept|Carry on with the update and repair these errors in the build step|The update stays, the app does not build until "
          f"each error is repaired (steps/repair.md), and these errors are listed there")
    print(f"O\thand|Stop here and look at the errors first|The update is undone and the run stays stopped; nothing else changes")
    print(f"W\tkeep|step-keep.txt|{mod}")
    print(f"W\taccept|stepcheck-accepted.txt|{mod} {','.join(sorted(per))}")
    print(f"B\tThe step was undone before anything was committed. The errors the update added:")
    for c, m in new[:a.max]:
        print(f"B\t  {c} {m}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
