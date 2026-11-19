#!/usr/bin/env python3
"""exprparam_source.py: an expression text parameter that still carries a source variable (repair row 35, CE7005).

  exprparam_source.py <app dir|.mpr> [--apply]

Why (cold rfq, 9.24.10 -> 10.24.28): a page text had a template parameter given by an expression
(formatDateTime($X/Date)) that also kept a Forms$PageVariable from before, pointing at a SNIPPET parameter X (pasted from
a snippet). An expression names its variables itself; Studio Pro stores no source variable for it (the same text on a
sister page had none). 9.24 ignored the leftover, the 10.24 mx check after the convert reports CE7005 "No source variable
has been selected" on the text. Pointing the variable at the page parameter X did not clear it; removing it did.

For each page, snippet and layout, each Forms$ClientTemplateParameter with an Expression, no AttributeRef and a
SourceVariable: the SourceVariable is removed. Attribute parameters are left alone.
Dry run unless --apply; commit the app before --apply, then run mx check.
Exit: 0 = done (or nothing found), 2 = input error.
"""
import argparse, os, sys

import bson

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from copy_mappings import Mpr  # noqa: E402
from widgetdrop import find  # noqa: E402

FORMS = ("Forms$Page", "Forms$Snippet", "Forms$Layout")


def owner(d, target):
    """Name of the closest named widget around target (for the report)."""
    def walk(x, name):
        if x is target:
            return name
        if isinstance(x, dict):
            n = x.get("Name") if isinstance(x.get("Name"), str) else name
            vals = x.values()
        elif isinstance(x, list):
            n, vals = name, x
        else:
            return None
        for v in vals:
            r = walk(v, n)
            if r:
                return r
        return None
    return walk(d, "?") or "?"


def source(v):
    for k in ("PageParameter", "SnippetParameter", "LocalVariable", "Widget"):
        if v.get(k):
            return f"{k} {v[k]}"
    return "an empty source"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("project")
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    try:
        m = Mpr(a.project)
    except (ValueError, OSError) as e:
        print(f"exprparam_source: {e}")
        return 2
    n = 0
    for qn, uid in sorted(m.docs.items()):
        d = m.decode(uid)
        if not d or d.get("$Type") not in FORMS:
            continue
        hits = list(find(d, lambda x: x.get("$Type") == "Forms$ClientTemplateParameter" and x.get("Expression")
                         and not x.get("AttributeRef") and isinstance(x.get("SourceVariable"), dict)))
        for p in hits:
            print(f"FIX {qn} {owner(d, p)}: expression {p['Expression'][:60]!r} carries {source(p['SourceVariable'])}: removed")
            p["SourceVariable"] = None
            n += 1
        if hits and a.apply:
            m.write(uid, bson.encode(d))
    tail = ("written" if a.apply else "dry run, rerun with --apply (commit the app first), then mx check") if n else "nothing to write"
    print(f"exprparam_source: {n} fix(es); {tail}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
