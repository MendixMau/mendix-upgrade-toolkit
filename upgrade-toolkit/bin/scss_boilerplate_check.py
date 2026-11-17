#!/usr/bin/env python3
"""scss_boilerplate_check.py: is an @import that reaches outside a themesource module Mendix's own stock
boilerplate, or a real app-specific edit a FILES route must carry forward?

Every Mendix-generated themesource/<module>/web/main.scss ships two lines by default, reaching three levels up
into the project's own top-level theme/ folder:

  @import "../../../theme/web/exclusion-variables";
  @import "../../../theme/web/custom-variables";

(WM1-style audits mistook these for a hand-edited vendor file at FILES-route risk on Atlas_Core: 46 of a real
app's themesource modules carried the identical line, including modules with zero other edits. An Atlas_Core
update regenerates this same boilerplate every time; it is not what an Atlas update wipes.)

A line that reaches outside the module by the SAME depth but imports something OTHER than those two stock
names is not boilerplate: it is an app edit, and the FILES route applies (move the imported content into the
app's own design module, so the single import-path line is the only thing replayed on every update).

  scss_boilerplate_check.py <module-dir> [<module-dir> ...]
        <module-dir> is a themesource/<module> directory containing web/main.scss.

Output: one line per outward-reaching import found:
  "BOILERPLATE <module> <line>: stock Mendix theme-folder import, not a FILES-route risk"
  "RISK <module> <line>: app-specific outward import, needs a FILES route (editroute.py FILES)"
then a summary: "scss_boilerplate_check: N boilerplate, M risk across K module(s)".
Exit 0 if no RISK lines found (including no outward imports at all), 1 if any RISK line was found, 2 on bad input
(a module dir with no web/main.scss).
"""
import os
import re
import sys

STOCK_NAMES = {"custom-variables", "exclusion-variables"}
# Mendix's generated main.scss reaches out with a "../"-only relative path (any depth) into theme/web/.
OUTWARD_RE = re.compile(r'@import\s+[\'"](\.\./[\./]*theme/web/([A-Za-z0-9_-]+))[\'"]\s*;?')


def check_module(module_dir):
    main_scss = os.path.join(module_dir, "web", "main.scss")
    if not os.path.isfile(main_scss):
        print(f"usage: no web/main.scss in {module_dir}", file=sys.stderr)
        return None
    module = os.path.basename(os.path.normpath(module_dir))
    boiler = risk = 0
    with open(main_scss, encoding="utf-8") as f:
        for line in f:
            m = OUTWARD_RE.search(line)
            if not m:
                continue
            name = m.group(2)
            stripped = line.strip()
            if name in STOCK_NAMES:
                boiler += 1
                print(f"BOILERPLATE {module} {stripped}: stock Mendix theme-folder import, not a FILES-route risk")
            else:
                risk += 1
                print(f"RISK {module} {stripped}: app-specific outward import, needs a FILES route (editroute.py FILES)")
    return boiler, risk


def main(argv):
    if not argv:
        print("usage: scss_boilerplate_check.py <module-dir> [<module-dir> ...]", file=sys.stderr)
        return 2
    total_boiler = total_risk = 0
    modules = 0
    for module_dir in argv:
        result = check_module(module_dir)
        if result is None:
            return 2
        b, r = result
        total_boiler += b
        total_risk += r
        modules += 1
    print(f"scss_boilerplate_check: {total_boiler} boilerplate, {total_risk} risk across {modules} module(s)")
    return 1 if total_risk else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
