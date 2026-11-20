#!/usr/bin/env python3
"""startcheck.py: did the old app start CLEANLY? Read its start log before the baseline database is frozen (GM-A5).

  startcheck.py LOG [--allow allow.txt]

Why: bin/cloud/upgrade-pipeline.sh froze the baseline database once `app_up old` returned 0, which only means the
runtime came up. An after-startup microflow that threw (ERROR in the log, the runtime still started) froze a baseline
whose state the old app had half written, and every gate rung then compared against it. Reads the same Mendix runtime
log lines as logdiff.py (docker logs saved by runapp.py as logs/runtime-<name>.log), only the START window: first line to
"Mendix Runtime successfully started".

Verdicts (first line of output; exit code):
  CLEAN    0  the start window has no ERROR/CRITICAL line, a "successfully started" line, and an after-startup
             section that ended. Freezing is allowed.
  UNCLEAN  1  ERROR/CRITICAL lines in the start window (each printed with its line number), or the after-startup
             section began and never ended, or the window has no "successfully started" line. Do NOT freeze.
  INVALID  2  the log is missing, empty or has no Mendix log lines. Nothing was read, so nothing is proven: the caller
             stops (same convention as logdiff.py, which exits 2 on a log with no Mendix lines). Silence is not CLEAN.
allow.txt (optional): one fnmatch pattern per line on "LEVEL Node: message", then " # reason" (logdiff.py's format).
An allowed line is listed as accepted and does not make the log UNCLEAN.

Producer: upgrade-pipeline.sh step baseline (mandatory), reading logs/runtime-old.log that app_down/runapp.py saves.
"""
import fnmatch, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from logdiff import LINE, STARTED, AS_BEGIN, AS_END  # noqa: E402  (one log grammar for both tools)


def check(path, allow=()):
    """Returns (verdict, problems, accepted, nlines). problems/accepted: [(lineno, text)]."""
    try:
        lines = open(path, errors="replace").read().splitlines()
    except OSError as e:
        return "INVALID", [(0, f"cannot read {path}: {e.strerror or e}")], [], 0
    problems, accepted = [], []
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
            why = next((w for p, w in allow if fnmatch.fnmatch(s, p)), None)
            (accepted if why else problems).append((i, raw.strip()[:240] + (f"  (accepted: {why})" if why else "")))
        if STARTED in text:
            started = True
            break
    if not seen_any:
        return "INVALID", [(0, f"no Mendix log lines in {path} ({len(lines)} lines): nothing was read")], [], len(lines)
    if in_as:
        problems.append((0, "after-startup section began ('Running after-startup-action') and never ended"))
    if not started:
        problems.append((0, "no 'Mendix Runtime successfully started' line in the log"))
    return ("UNCLEAN" if problems else "CLEAN"), problems, accepted, len(lines)


def main():
    args = sys.argv[1:]
    allow = []
    if "--allow" in args:
        i = args.index("--allow")
        if i + 1 >= len(args):
            sys.exit(__doc__)
        try:
            for line in open(args[i + 1]):
                if line.strip() and not line.lstrip().startswith("#"):
                    pat, _, why = line.partition("#")
                    allow.append((pat.strip(), why.strip() or "allowed"))
        except OSError as e:
            print(f"startcheck: INVALID, cannot read the allow file: {e}", file=sys.stderr); sys.exit(2)
        del args[i:i + 2]
    if len(args) != 1:
        sys.exit(__doc__)
    verdict, problems, accepted, n = check(args[0], allow)
    print(f"startcheck: {verdict} ({args[0]}, {n} lines, {len(problems)} problem(s), {len(accepted)} accepted)")
    for ln, t in problems:
        print(f"  {'line ' + str(ln) if ln else 'log'}: {t}")
    for ln, t in accepted:
        print(f"  line {ln}: {t}")
    sys.exit({"CLEAN": 0, "UNCLEAN": 1}.get(verdict, 2))


if __name__ == "__main__":
    main()
