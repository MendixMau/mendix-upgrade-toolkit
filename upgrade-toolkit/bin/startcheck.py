#!/usr/bin/env python3
"""startcheck.py: did the old app start CLEANLY? Read its start log before the baseline database is frozen (GM-A5).

  startcheck.py LOG [--allow allow.txt]

Why: bin/cloud/upgrade-pipeline.sh froze the baseline database once `app_up old` returned 0, which only means the
runtime came up. An after-startup microflow that threw (ERROR in the log, the runtime still started) froze a baseline
whose state the old app had half written, and every gate rung then compared against it. Reads the same Mendix runtime
log lines as logdiff.py (docker logs saved by runapp.py as logs/runtime-<name>.log), only the START window: first line to
"Mendix Runtime successfully started".

Verdicts (first line of output; exit code):
  CLEAN              0  no ERROR/CRITICAL line in the start window, "successfully started" present, after-startup ended.
  CLEAN-WITH-ERRORS  0  as CLEAN, but ERROR/CRITICAL lines are logged in the start window OUTSIDE the after-startup
                        section: listed, never a stop (lead's decision, GM-A5 review: many old apps log a benign ERROR at
                        start, and a stop on each would train people to allow-list blindly; the lines are the person's to read).
  UNCLEAN            1  the after-startup section began and never ended, there is no "successfully started" line, or an
                        ERROR/CRITICAL line is logged BETWEEN after-startup begin and end (a failed after-startup
                        microflow). Do NOT freeze.
  INVALID            2  the log is missing, empty or has no Mendix log lines. Nothing was read, so nothing is proven: the
                        caller stops (logdiff.py's convention: exit 2 on a log with no Mendix lines). Silence is not CLEAN.
Options: --allow FILE (one fnmatch pattern per line on "LEVEL Node: message", then " # reason", logdiff.py's format; an
allowed line is listed as accepted and counts as no problem, in or out of the after-startup section) and --list FILE
(writes every ERROR/CRITICAL line, "ERROR line N: ..." or "accepted: <pattern> # <reason>: ...", for the report).

Producer: upgrade-pipeline.sh step baseline (mandatory), reading logs/runtime-old.log that app_down/runapp.py saves.
"""
import fnmatch, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from logdiff import LINE, STARTED, AS_BEGIN, AS_END  # noqa: E402  (one log grammar for both tools)


def check(path, allow=()):
    """Returns (verdict, problems, accepted, nlines, errors). problems/accepted/errors: [(lineno, text)]."""
    try:
        lines = open(path, errors="replace").read().splitlines()
    except OSError as e:
        return "INVALID", [(0, f"cannot read {path}: {e.strerror or e}")], [], 0, []
    problems, accepted, errors = [], [], []
    seen_any = started = False
    in_as = False
    for i, raw in enumerate(lines, 1):
        m = LINE.match(raw)
        if not m:
            continue
        seen_any = True
        _, level, node, msg = m.groups()
        text = f"{node.strip()}: {msg}"
        if AS_BEGIN in text:
            in_as = True
        if AS_END in text:
            in_as = False
        if level in ("ERROR", "CRITICAL"):
            s = f"{level} {text}"
            hit = next(((p, w) for p, w in allow if fnmatch.fnmatch(s, p)), None)
            t = raw.strip()[:240]
            if hit:
                accepted.append((i, f"accepted: {hit[0]} # {hit[1]}: {t}"))
            elif in_as:
                problems.append((i, t + "  (inside the after-startup section)"))
            else:
                errors.append((i, t))
        if STARTED in text:
            started = True
            break
    if not seen_any:
        return "INVALID", [(0, f"no Mendix log lines in {path} ({len(lines)} lines): nothing was read")], [], len(lines), []
    if in_as:
        problems.append((0, "after-startup section began ('Running after-startup-action') and never ended"))
    if not started:
        problems.append((0, "no 'Mendix Runtime successfully started' line in the log"))
    return ("UNCLEAN" if problems else "CLEAN-WITH-ERRORS" if errors else "CLEAN"), problems, accepted, len(lines), errors


def main():
    args = sys.argv[1:]
    allow, listf = [], None
    for flag in ("--allow", "--list"):
        if flag in args:
            i = args.index(flag)
            if i + 1 >= len(args):
                print(f"startcheck: {flag} needs a value (usage: startcheck.py LOG [--allow FILE] [--list FILE])", file=sys.stderr); sys.exit(2)
            val = args[i + 1]
            del args[i:i + 2]
            if flag == "--list":
                listf = val
                continue
            try:
                for line in open(val):
                    if line.strip() and not line.lstrip().startswith("#"):
                        pat, _, why = line.partition("#")
                        allow.append((pat.strip(), why.strip() or "allowed"))
            except OSError as e:
                print(f"startcheck: INVALID, cannot read the allow file: {e}", file=sys.stderr); sys.exit(2)
    if len(args) != 1:
        print("usage: startcheck.py LOG [--allow FILE] [--list FILE]", file=sys.stderr); sys.exit(2)
    verdict, problems, accepted, n, errors = check(args[0], allow)
    print(f"startcheck: {verdict} ({args[0]}, {n} lines, {len(problems)} problem(s), {len(errors)} error line(s) logged, {len(accepted)} accepted)")
    for ln, t in problems:
        print(f"  {'line ' + str(ln) if ln else 'log'}: {t}")
    for ln, t in errors:
        print(f"  ERROR line {ln}: {t}")
    for ln, t in accepted:
        print(f"  line {ln}: {t}")
    if listf and verdict != "INVALID":
        with open(listf, "w") as f:
            for ln, t in problems + errors:
                if ln:
                    f.write(f"ERROR line {ln}: {t}\n")
            for ln, t in accepted:
                f.write(f"line {ln}: {t}\n")
    sys.exit({"CLEAN": 0, "CLEAN-WITH-ERRORS": 0, "UNCLEAN": 1}.get(verdict, 2))


if __name__ == "__main__":
    main()
