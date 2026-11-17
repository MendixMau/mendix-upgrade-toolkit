#!/usr/bin/env python3
"""checkwhere.py: add the document of each error to an `mx check` log, from the JSON that `mx check -j` writes.

  checkwhere.py CHECK.json CHECK.log

The text output of mx check names only the element ("at Action button 'actionButton1'"), and a widget name like that
occurs on many pages (cold CMM: 4 CE0117 on actionButton1/2/4/7, which sat in two Mix_New_WizardStep1 pages, not in the
login templates that also have such buttons). The JSON has the module, document and property. Appends one line per
error location to the log:

  [where] CE0117 MaterialManagement / Page 'Mix_New_WizardStep1': Property 'Dynamic classes expression' of action button 'actionButton1'

The [error] lines and the summary stay as they are, so checkdiff.py and the error count read the log as before.
Exit: 0 = lines added (or none to add), 2 = the JSON is unreadable (the log is left alone).
"""
import json, sys


def where(d):
    for e in d.get("errors") or []:
        for loc in e.get("locations") or [{}]:
            yield (f"[where] {e.get('code', '?')} {loc.get('module-name', '?')} / {loc.get('document-name', '?')}: "
                   f"{loc.get('element-name', '?')}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    try:
        d = json.load(open(sys.argv[1]))
    except (OSError, ValueError) as e:
        print(f"checkwhere: {sys.argv[1]}: {e}", file=sys.stderr); sys.exit(2)
    lines = list(where(d))
    if lines:
        with open(sys.argv[2], "a") as f:
            f.write("Where (mx check -j):\n" + "\n".join(lines) + "\n")
