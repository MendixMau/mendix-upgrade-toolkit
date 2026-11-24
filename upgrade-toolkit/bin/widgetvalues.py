#!/usr/bin/env python3
"""widgetvalues.py: did a step reset the settings of a pluggable widget the app had configured? (GF-44)

  widgetvalues.py <old project dir|.mpr> <new project dir|.mpr> [--changed FILE]

Why (a field run, GF): two `update-widgets` passes during an upgrade step silently put a widget's configured settings
(two microflow references, two URL values) back to the package defaults. `mx check` only named the two properties that
had become required, and no rung compared property VALUES: widgetdiff.py names package versions, idcheck.py data.

Reads both models with mprmodel.py (Page, Snippet and Layout documents, v1 and v2), pairs each CustomWidget instance by
document and widget name, and compares every property (nested objects too) by the key the widget's own type gives it.
A value is read as widgetdrop.py reads it (primitive, attribute, entity path, expression) plus microflow / action
microflow references and text templates.

  WIDGET-RESET <doc> <widget> (<widget id>) <property>: was <old value>, now <empty | the default "X">
  WIDGET-PROP-GONE <doc> <widget> (<widget id>) <property>: was <old value>; the new package removed it
                   | renamed to <key> (its value moved there)

A RESET (non-default before, empty or the default after) is a finding: exit 1. A property the new package no longer has
is reported, and does not change the exit code (nothing can bring it back; check the page on the new widget).

  --changed FILE   widgetdiff.py's output ("widgets/x.mpk <name> <old> -> <new>"): only widgets whose package file is
                   named there are compared (the widget ids come from each project's own widgets/*.mpk). Without it
                   every widget instance is compared.
Producer: stepupdate.sh runs it after widgetdiff.py for each step (old = the step's prevtree), and the pipeline's
update_widgets (repair row 5) runs it around `update-widgets` / `mxcli fix widgets`.
Exit: 0 = nothing reset, 1 = a reset, 2 = input error.
"""
import argparse, glob, os, re, sys

here = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [here, os.path.join(here, "repair")]
from mprmodel import Model  # noqa: E402
from widgetdrop import find, value, installed_keys  # noqa: E402


def full_value(v):
    """widgetdrop.value, plus the microflow / action microflow and text template forms; '' when nothing is set."""
    s = value(v)
    if s or not isinstance(v, dict):
        return s
    if isinstance(v.get("Microflow"), str) and v["Microflow"]:
        return v["Microflow"]
    act = v.get("Action")
    if isinstance(act, dict) and not str(act.get("$Type", "")).endswith("NoAction"):
        mfs = [x["Microflow"] for x in find(act, lambda d: isinstance(d.get("Microflow"), str) and d["Microflow"])]
        return mfs[0] if mfs else str(act.get("$Type", "")).split("$")[-1]
    t = v.get("TextTemplate")
    if isinstance(t, dict):
        txt = [i.get("Text", "") for i in find(t, lambda d: "Text" in d and "LanguageCode" in d) if i.get("Text")]
        if txt:
            return txt[0]
    ds = v.get("DataSource")
    if isinstance(ds, dict):
        e = [x["Entity"] for x in find(ds, lambda d: isinstance(d.get("Entity"), str) and d["Entity"])]
        if e:
            return e[0]
    return ""


def props(widget):
    """{path: (value, default)} for every property of a widget instance, nested object lists as key[i].key."""
    types = {}
    for pt in find(widget.get("Type") or {}, lambda x: x.get("$Type") == "CustomWidgets$WidgetPropertyType"):
        vt = pt.get("ValueType") or {}
        types[repr(pt.get("$ID"))] = (pt.get("PropertyKey"), str(vt.get("DefaultValue") or ""))
    out = {}

    def walk(obj, prefix):
        for p in (obj or {}).get("Properties") or []:
            if not isinstance(p, dict) or p.get("$Type") != "CustomWidgets$WidgetProperty":
                continue
            key, default = types.get(repr(p.get("TypePointer")), (None, ""))
            if not key:
                continue
            v = p.get("Value") or {}
            out[prefix + key] = (full_value(v), default)
            objs = [o for o in (v.get("Objects") or []) if isinstance(o, dict)]
            for i, o in enumerate(objs):
                walk(o, f"{prefix}{key}[{i}].")
    walk(widget.get("Object"), "")
    keys = {k for k in (t[0] for t in types.values())}
    return out, keys


def widgets(model):
    """{(doc qn, widget name): (widget id, props, declared keys)} over Page, Snippet and Layout documents."""
    out = {}
    for d in model.all_docs:
        if d.type not in ("Forms$Page", "Forms$Snippet", "Forms$Layout") or d.data.get("Excluded") is True:
            continue
        for w in find(d.data, lambda x: x.get("$Type") == "CustomWidgets$CustomWidget"):
            wid = (w.get("Type") or {}).get("WidgetId")
            if wid and w.get("Name"):
                p, keys = props(w)
                out[(d.qn, w["Name"])] = (wid, p, keys)
    return out


def project_dir(p):
    p = os.path.abspath(p)
    return p if os.path.isdir(p) else os.path.dirname(p)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("old"); ap.add_argument("new"); ap.add_argument("--changed")
    a = ap.parse_args()
    for p in (a.old, a.new):
        if not os.path.exists(p):
            print(f"widgetvalues: {p}: no such project", file=sys.stderr); return 2
    only = None
    if a.changed:
        try:
            lines = open(a.changed, encoding="utf-8").read().splitlines()
        except OSError as e:
            print(f"widgetvalues: {a.changed}: {e}", file=sys.stderr); return 2
        only = {os.path.basename(l.split()[0]) for l in lines if l.strip().split() and l.split()[0].endswith(".mpk")}
        ids = {}
        for p in (a.old, a.new):
            f = {}
            installed_keys(project_dir(p), f)
            ids.update({wid: mpk for wid, mpk in f.items() if mpk in only})
        only = set(ids)
    old, new = Model.load(a.old), Model.load(a.new)
    wo, wn = widgets(old), widgets(new)
    lines, seen, nvals, bad, gone = [], 0, 0, 0, 0
    for k in sorted(wo):
        wid, po, _ = wo[k]
        if k not in wn or wn[k][0] != wid or (only is not None and wid not in only):
            continue
        seen += 1
        _, pn, keysn = wn[k]
        for path in sorted(po):
            ov, od = po[path]
            if not ov or ov == od:
                continue                       # nothing configured before
            nvals += 1
            if path in pn:
                nv, nd = pn[path]
                if not nv or (nv == nd and nv != ov):
                    bad += 1
                    now = "empty" if not nv else f'the default "{nd}"'
                    lines.append(f"WIDGET-RESET {k[0]} {k[1]} ({wid}) {path}: was {ov}, now {now}")
            elif path.split("[")[0] not in keysn:
                gone += 1
                moved = sorted(q for q, (v, _d) in pn.items() if v == ov and q not in po)
                how = f"renamed to {moved[0]} (its value moved there)" if moved else "the new package removed it"
                lines.append(f"WIDGET-PROP-GONE {k[0]} {k[1]} ({wid}) {path}: was {ov}; {how}")
    print(f"# widgetvalues {a.old} -> {a.new}")
    if lines:
        print("\n".join(lines))
    print(f"widgetvalues: {'FAIL' if bad else 'PASS'}, {bad} of {nvals} configured value(s) reset on {seen} widget instance(s)"
          + (f"; {gone} property(ies) gone from the new package (check those pages)" if gone else ""))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
