#!/usr/bin/env python3
"""widgetvalues.py: did a step reset the settings of a pluggable widget the app had configured? (GF-44)

  widgetvalues.py <old project dir|.mpr> <new project dir|.mpr> [--changed FILE] [--cache FILE]

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

A value is also read when it is a datasource or action microflow or nanoflow, a Form, Image or Selection (a datasource is
read as its entity, else the microflow or nanoflow it calls). A RESET (non-default before, empty or the default after;
an object list that lost or cleared items) is a finding: exit 1. A property the new package no longer has is reported,
and does not change the exit code (nothing can bring it back; check the page on the new widget):

  WIDGET-RESET <doc> <widget> (<widget id>) <list property>: was N item(s), now M
  MARKETPLACE-WIDGET-RESET <doc> <widget> (<widget id>) <property>: the same, in a document of a Marketplace module
                   (Projects$ModuleImpl FromAppStore). Reported apart and never an exit code: the module's new version
                   changed its own default (a vendor page, nothing the app configured); writing the old value back would
                   edit vendor content the next module update overwrites again. The own modules' resets stay WIDGET-RESET.
  WIDGET-MISSING <doc> <widget> (<widget id>): N configured value(s), no such widget instance in the new model
                   (counted in the summary line; not an exit code either: a page or module removed on purpose looks the same)

  --changed FILE   widgetdiff.py's output ("widgets/x.mpk <name> <old> -> <new>"): only widgets whose package file is
                   named there are compared (the widget ids come from each project's own widgets/*.mpk). Without it
                   every widget instance is compared.
  --cache FILE     the old model's widget values, kept in FILE (keyed by the old file's path, size and time): a run that
                   compares the same baseline after every pass parses it once; the new model is always read fresh.
Compare against the RUN BASELINE (the run's original.mpr), never only the pass before: two passes that go 12 -> 10 hide
a reset from a per-pass comparison that sees only one of them. Without --changed every widget instance is compared (a
round trip leaves the package version unchanged, so a package filter would skip it).
Producers (the mandatory steps that call it): stepupdate.sh after every module step (old = --baseline original.mpr, else
the first step's snapshot), and the pipeline's update_widgets (repair row 5) after each `update-widgets` / `mxcli fix
widgets` pass (old = $WORK/original.mpr).
Exit: 0 = nothing reset, 1 = a reset, 2 = a project could not be read or any other failure (never 1: 1 means a reset).
"""
import argparse, glob, json, os, re, sys

here = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [here, os.path.join(here, "repair")]
from mprmodel import Model  # noqa: E402
from widgetdrop import find, value, installed_keys  # noqa: E402

FLOWKEYS = ("Microflow", "Nanoflow", "Form")   # the qualified-name fields a flow or page reference lives in


def _first(node, keys):
    """The first non-empty string under `keys` anywhere inside node."""
    hit = next(iter(find(node, lambda d: any(isinstance(d.get(k), str) and d[k] for k in keys))), None)
    return next((hit[k] for k in keys if isinstance(hit.get(k), str) and hit[k]), "") if hit else ""


def full_value(v):
    """The value on one line (an expression ends in a newline)."""
    return " ".join(_full_value(v).split())


def _full_value(v):
    """widgetdrop.value, plus microflow / nanoflow / form / image / selection values, action and datasource flows and
    text templates; '' when nothing is set (a Selection of "None" is the unset default)."""
    s = value(v)
    if s or not isinstance(v, dict):
        return s
    for k in ("Microflow", "Nanoflow", "Form", "Image"):
        if isinstance(v.get(k), str) and v[k]:
            return v[k]
    if isinstance(v.get("Selection"), str) and v["Selection"] not in ("", "None"):
        return v["Selection"]
    act = v.get("Action")
    if isinstance(act, dict) and not str(act.get("$Type", "")).endswith("NoAction"):
        return _first(act, FLOWKEYS) or str(act.get("$Type", "")).split("$")[-1]
    t = v.get("TextTemplate")
    if isinstance(t, dict):
        txt = [i.get("Text", "") for i in find(t, lambda d: "Text" in d and "LanguageCode" in d) if i.get("Text")]
        if txt:
            return txt[0]
    ds = v.get("DataSource")
    if isinstance(ds, dict):
        return _first(ds, ("Entity",)) or _first(ds, FLOWKEYS)
    return ""


def props(widget):
    """(values {path: (value, default)}, item counts {list path: n}, declared keys): every property of a widget
    instance, nested object lists as key[i].key."""
    types = {}
    for pt in find(widget.get("Type") or {}, lambda x: x.get("$Type") == "CustomWidgets$WidgetPropertyType"):
        vt = pt.get("ValueType") or {}
        types[repr(pt.get("$ID"))] = (pt.get("PropertyKey"), str(vt.get("DefaultValue") or ""))
    out, lens = {}, {}

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
            if objs:
                lens[prefix + key] = len(objs)
            for i, o in enumerate(objs):
                walk(o, f"{prefix}{key}[{i}].")
    walk(widget.get("Object"), "")
    return out, lens, sorted({t[0] for t in types.values() if t[0]})


def widgets(model):
    """{(doc qn, widget name): (widget id, values, item counts, declared keys)} over Page, Snippet and Layout documents."""
    out = {}
    for d in model.all_docs:
        if d.type not in ("Forms$Page", "Forms$Snippet", "Forms$Layout") or d.data.get("Excluded") is True:
            continue
        for w in find(d.data, lambda x: x.get("$Type") == "CustomWidgets$CustomWidget"):
            wid = (w.get("Type") or {}).get("WidgetId")
            if wid and w.get("Name"):
                out[(d.qn, w["Name"])] = (wid,) + props(w)
    return out


def load_widgets(path, cache=None):
    """(widgets(), the Marketplace modules' names) of a project; with `cache` (a file) the result is kept there, keyed by the
    project file's path, size and time."""
    key = None
    if cache:
        try:
            st = os.stat(path if os.path.isfile(path) else glob.glob(os.path.join(path, "*.mpr"))[0])
            key = [os.path.abspath(path), st.st_size, int(st.st_mtime)]
            c = json.load(open(cache, encoding="utf-8"))
            if c.get("key") == key:
                return ({(r[0], r[1]): (r[2], {k: tuple(v) for k, v in r[3].items()}, r[4], r[5]) for r in c["widgets"]},
                        set(c["appstore"]))
        except (OSError, ValueError, KeyError, IndexError, TypeError):
            pass
    model = Model.load(path)
    w, store = widgets(model), {n for n, m in model.modules.items() if m.get("from_appstore")}
    if cache and key:
        try:
            tmp = f"{cache}.{os.getpid()}.tmp"
            json.dump({"key": key, "widgets": [[k[0], k[1], v[0], v[1], v[2], v[3]] for k, v in w.items()],
                       "appstore": sorted(store)},
                      open(tmp, "w", encoding="utf-8"))
            os.replace(tmp, cache)
        except OSError:
            pass
    return w, store


def project_dir(p):
    p = os.path.abspath(p)
    return p if os.path.isdir(p) else os.path.dirname(p)


def run(a):
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
    (wo, so), (wn, sn) = load_widgets(a.old, a.cache), load_widgets(a.new)
    store = so | sn
    lines, seen, nvals, bad, gone, miss, mkt = [], 0, 0, 0, 0, 0, 0
    for k in sorted(wo):
        wid, po, lo, _ = wo[k]
        if only is not None and wid not in only:
            continue
        configured = sum(1 for ov, od in po.values() if ov and ov != od) + len(lo)
        if k not in wn or wn[k][0] != wid:
            if configured:
                miss += 1
                lines.append(f"WIDGET-MISSING {k[0]} {k[1]} ({wid}): {configured} configured value(s), no such widget instance in the new model")
            continue
        seen += 1
        _, pn, ln, keysn = wn[k]
        for path in sorted(lo):                  # object lists: an item lost or cleared is a reset of what it held
            if re.sub(r"\[\d+\]", "", path).split(".")[-1] in keysn and ln.get(path, 0) < lo[path]:
                nvals += 1
                if k[0].split(".")[0] in store:
                    mkt += 1; lines.append(f"MARKETPLACE-WIDGET-RESET {k[0]} {k[1]} ({wid}) {path}: was {lo[path]} item(s), now {ln.get(path, 0)}")
                else:
                    bad += 1; lines.append(f"WIDGET-RESET {k[0]} {k[1]} ({wid}) {path}: was {lo[path]} item(s), now {ln.get(path, 0)}")
            else:
                nvals += 1
        for path in sorted(po):
            ov, od = po[path]
            if not ov or ov == od:
                continue                       # nothing configured before
            nvals += 1
            if path in pn:
                nv, nd = pn[path]
                if not nv or (nv == nd and nv != ov):
                    now = "empty" if not nv else f'the default "{nd}"'
                    if k[0].split(".")[0] in store:   # a Marketplace module's own document: its new version changed its own default
                        mkt += 1; lines.append(f"MARKETPLACE-WIDGET-RESET {k[0]} {k[1]} ({wid}) {path}: was {ov}, now {now}")
                    else:
                        bad += 1; lines.append(f"WIDGET-RESET {k[0]} {k[1]} ({wid}) {path}: was {ov}, now {now}")
            elif re.sub(r"\[\d+\]", "", path).split(".")[-1] not in keysn:
                gone += 1
                moved = sorted(q for q, (v, _d) in pn.items() if v == ov and q not in po)
                how = f"renamed to {moved[0]} (its value moved there)" if moved else "the new package removed it"
                lines.append(f"WIDGET-PROP-GONE {k[0]} {k[1]} ({wid}) {path}: was {ov}; {how}")
            # else: the property exists in the new package but its list item is gone: the list line above says so
    print(f"# widgetvalues {a.old} -> {a.new}")
    if lines:
        print("\n".join(lines))
    print(f"widgetvalues: {'FAIL' if bad else 'PASS'}, {bad} of {nvals} configured value(s) reset on {seen} widget instance(s)"
          + (f"; {mkt} reset(s) in Marketplace module documents reported apart, not counted (the module's new version changed its own default)" if mkt else "")
          + (f"; {gone} property(ies) gone from the new package (check those pages)" if gone else "")
          + (f"; {miss} widget instance(s) with configured values missing in the new model" if miss else ""))
    return 1 if bad else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("old"); ap.add_argument("new"); ap.add_argument("--changed"); ap.add_argument("--cache")
    a = ap.parse_args()
    try:
        return run(a)
    except SystemExit as e:   # mprmodel.py refuses an unreadable model with sys.exit("..."): that is 2, never the 1 of a reset
        print(f"widgetvalues: could not read the models: {e.code}", file=sys.stderr); return 2
    except Exception as e:   # noqa: BLE001  any load or parse failure
        print(f"widgetvalues: could not compare: {type(e).__name__}: {e}", file=sys.stderr); return 2


if __name__ == "__main__":
    sys.exit(main())
