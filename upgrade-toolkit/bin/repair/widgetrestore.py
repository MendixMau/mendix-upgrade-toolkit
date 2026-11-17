#!/usr/bin/env python3
"""widgetrestore.py: put back one pluggable widget as an earlier commit of the app saved it (repair row 33).

  widgetrestore.py <app dir|.mpr> --from <earlier .mpr> --doc Module.Doc --widget NAME [--apply]

Why (cold CMM): update-widgets ran under DataWidgets 2.2.1 and rewrote Administration 4.5.0's Roles filter on
Account_Overview to the 2.x definition; the association mode (baseType ref, refEntity over System.UserRoles) was gone,
and with DataWidgets 3.11.8 later the page showed "Unable to get filter store". widgetdrop.py now stops before that;
this repairs an app where it already happened. mxcli cannot write the 3.x filter's association mode.

The earlier .mpr is the app at a commit before the loss (`git show <commit>:<app>.mpr > old.mpr`). The widget's
whole subtree (its saved Type and its Object) is copied from it with fresh ids over the widget of the same name in the
same document; nothing else in the document changes. It prints each setting that comes back. Run `mx update-widgets`
and `mx check` after: the restored Type is the one the widget was saved with, update-widgets brings it to the
installed package and keeps every setting the package declares (widgetdrop.py says which it would not).

Refusals (exit 2): the document or the widget missing or not unique in either project, a different widget id, an MPR
whose document cannot be decoded. Dry run unless --apply; commit the app before --apply.
Exit: 0 = done (or the dry run shows it), 2 = refused.
"""
import argparse, copy, os, sqlite3, sys

import bson

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from copy_mappings import Mpr  # noqa: E402
from copydoc import new_ids  # noqa: E402
from widgetdrop import find, value  # noqa: E402


def die(msg):
    print(f"widgetrestore: REFUSED: {msg}")
    sys.exit(2)


def version(m):
    try:
        return m.con.execute("select _ProductVersion from _MetaData").fetchone()[0]
    except sqlite3.DatabaseError:
        return "?"


def widget(m, doc, name, label):
    uid = m.docs.get(doc)
    if uid is None:
        die(f"{label}: no document {doc}")
    d = m.decode(uid)
    if d is None:
        die(f"{label}: {doc} cannot be decoded")
    ws = list(find(d, lambda x: x.get("$Type") == "CustomWidgets$CustomWidget" and x.get("Name") == name))
    if len(ws) != 1:
        die(f"{label}: {len(ws)} pluggable widgets named {name} in {doc}, want 1")
    return uid, d, ws[0]


def settings(w):
    """{property key: set value} of a widget instance (nested objects too)."""
    keys = {repr(pt.get("$ID")): pt.get("PropertyKey")
            for pt in find(w.get("Type") or {}, lambda x: x.get("$Type") == "CustomWidgets$WidgetPropertyType")}
    out = {}
    for p in find(w.get("Object") or {}, lambda x: x.get("$Type") == "CustomWidgets$WidgetProperty"):
        k, v = keys.get(repr(p.get("TypePointer"))), value(p.get("Value"))
        if k and v:
            out.setdefault(k, v)
    return out


def replace(o, target, new):
    """Replace the dict object `target` (by identity) inside o with new; True when found."""
    if isinstance(o, dict):
        for k, v in o.items():
            if v is target:
                o[k] = new
                return True
            if replace(v, target, new):
                return True
    elif isinstance(o, list):
        for i, v in enumerate(o):
            if v is target:
                o[i] = new
                return True
            if replace(v, target, new):
                return True
    return False


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("project")
    ap.add_argument("--from", dest="old", required=True)
    ap.add_argument("--doc", required=True)
    ap.add_argument("--widget", required=True)
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    try:
        cur, old = Mpr(a.project), Mpr(a.old)
    except ValueError as e:
        die(str(e))
    uid, doc, w = widget(cur, a.doc, a.widget, "app")
    _, _, ow = widget(old, a.doc, a.widget, "earlier")
    wid, owid = (w.get("Type") or {}).get("WidgetId"), (ow.get("Type") or {}).get("WidgetId")
    if wid != owid:
        die(f"{a.widget} is {wid} in the app but {owid} in the earlier project")
    now, then = settings(w), settings(ow)
    back = sorted(k for k in then if now.get(k) != then[k])
    print(f"widgetrestore: {a.doc} {a.widget} ({wid}) from {os.path.basename(old.path)} (Mendix {version(old)}) "
          f"into {os.path.basename(cur.path)} (Mendix {version(cur)})")
    for k in back:
        print(f"  RESTORE {k}: {now.get(k, '(unset)')} -> {then[k]}")
    gone = sorted(k for k in now if k not in then)
    for k in gone:
        print(f"  UNSET   {k}: {now[k]} (the earlier widget has no value)")
    if not back and not gone:
        print("  nothing differs: no change")
        return 0
    if not a.apply:
        print("widgetrestore: dry run, rerun with --apply (commit the app first), then mx update-widgets and mx check")
        return 0
    new, _ = new_ids(copy.deepcopy(ow))
    new["Name"] = w.get("Name")
    if not replace(doc, w, new):
        die("the widget could not be located for the write")
    cur.write(uid, bson.encode(doc))
    print(f"widgetrestore: written, {len(back)} setting(s) back; now run mx update-widgets and mx check")
    return 0


if __name__ == "__main__":
    sys.exit(main())
