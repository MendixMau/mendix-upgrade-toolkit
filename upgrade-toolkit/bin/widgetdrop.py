#!/usr/bin/env python3
"""widgetdrop.py: which widget settings would `mx update-widgets` drop, because the installed widget package lacks them?

  widgetdrop.py <app dir | app.mpr> [--json out.json]

Why (cold CMM, 9.24.2 -> 10.24.28): Administration 4.5.0 ships Account_Overview with a Data Widgets 3.x drop-down filter
in association mode (baseType ref, refEntity over System.UserRoles). The plan kept DataWidgets at 2.2.1, whose filter has
no association mode. The build's update-widgets repair (row 5) rewrote the filter to the 2.x definition and the ref
settings were gone; when DataWidgets 3.11.8 came later the filter came back with its default, attribute mode. The page
then showed "Unable to get filter store" in the Roles column on 10.24 and on 11, and update-widgets reported success.

A pluggable widget in the model carries the definition it was saved with. A property that holds a value other than its
default there, and that the installed widgets/*.mpk no longer declares, is lost by update-widgets:

  WIDGET-DROP Account_Overview drop_downFilter1 (com.mendix.widget.web.datagriddropdownfilter.
    DatagridDropdownFilter, installed package lacks it): baseType=ref, refEntity=System.UserRoles

Fix before update-widgets: update the module that ships the widget (here DataWidgets) in the same rung as the module
whose pages brought the newer definition (steps/repair.md row 33). Excluded documents are skipped.
Exit: 0 = nothing would be dropped, 1 = a drop, 2 = input error.
"""
import argparse, glob, json, os, re, sys, zipfile

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "repair"))
from missing_deps import units  # noqa: E402  the .mpr reader (v1 and v2)


def installed_keys(proj):
    """{widget id: set of property keys} declared by widgets/*.mpk."""
    out = {}
    for f in glob.glob(os.path.join(proj, "widgets", "*.mpk")):
        try:
            with zipfile.ZipFile(f) as z:
                for n in z.namelist():
                    if not n.endswith(".xml") or n.endswith("package.xml"):
                        continue
                    x = z.read(n).decode("utf-8", "replace")
                    m = re.search(r'<widget\b[^>]*\bid="([^"]+)"', x)
                    if m:
                        out[m.group(1)] = set(re.findall(r'<property\b[^>]*\bkey="([^"]+)"', x))
        except (OSError, zipfile.BadZipFile):
            continue
    return out


def find(d, pred):
    if isinstance(d, dict):
        if pred(d):
            yield d
        for v in d.values():
            yield from find(v, pred)
    elif isinstance(d, list):
        for v in d:
            yield from find(v, pred)


def value(v):
    """The set value of a CustomWidgets$WidgetValue as text, '' when it holds nothing."""
    if not isinstance(v, dict):
        return ""
    if v.get("PrimitiveValue"):
        return v["PrimitiveValue"]
    a = v.get("AttributeRef") or {}
    if a.get("Attribute"):
        return a["Attribute"]
    e = v.get("EntityRef") or {}
    steps = [s.get("Association") for s in e.get("Steps") or [] if isinstance(s, dict) and s.get("Association")]
    if steps or e.get("Entity"):
        return "/".join(steps) or e["Entity"]
    if v.get("Expression"):
        return v["Expression"]
    return ""


def drops(widget, have):
    """[(key, value)] set on this widget instance (its nested objects too) that the installed package does not declare."""
    types = {}
    for pt in find(widget.get("Type") or {}, lambda x: x.get("$Type") == "CustomWidgets$WidgetPropertyType"):
        vt = pt.get("ValueType") or {}
        types[repr(pt.get("$ID"))] = (pt.get("PropertyKey"), str(vt.get("DefaultValue") or ""))
    out = []
    for prop in find(widget.get("Object") or {}, lambda x: x.get("$Type") == "CustomWidgets$WidgetProperty"):
        key, default = types.get(repr(prop.get("TypePointer")), (None, ""))
        val = value(prop.get("Value"))
        if key and key not in have and val and val != default:
            out.append((key, val))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("project"); ap.add_argument("--json")
    a = ap.parse_args()
    p = a.project
    if os.path.isdir(p):
        mprs = glob.glob(os.path.join(p, "*.mpr"))
        if len(mprs) != 1:
            print(f"widgetdrop: {p}: expected one .mpr", file=sys.stderr); return 2
        p = mprs[0]
    if not os.path.isfile(p):
        print(f"widgetdrop: no project {p}", file=sys.stderr); return 2
    have = installed_keys(os.path.dirname(os.path.abspath(p)))
    found, seen = [], 0
    docs = []
    for d in units(p):
        if d.get("$Type", "").startswith("Forms$") and d.get("Excluded") is not True:
            docs.append(d)
    for d in docs:
        name = d.get("Name") or "?"
        for w in find(d, lambda x: x.get("$Type") == "CustomWidgets$CustomWidget"):
            wid = (w.get("Type") or {}).get("WidgetId")
            if not wid or wid not in have:  # not installed at all: missing_deps.py reports it
                continue
            seen += 1
            lost = drops(w, have[wid])
            if lost:
                found.append({"document": name, "widget": w.get("Name"), "id": wid, "drops": lost})
    lines = [f"# widgetdrop {p}", f"widget instances checked {seen}, installed widget ids {len(have)}"]
    for f in found:
        lines.append(f"WIDGET-DROP {f['document']} {f['widget']} ({f['id']}, installed package lacks it): "
                     + ", ".join(f"{k}={v}" for k, v in f["drops"]))
    lines.append(f"widgetdrop: {'FAIL' if found else 'PASS'}, {len(found)} of {seen} widget instances would lose settings")
    print("\n".join(lines))
    if a.json:
        json.dump(found, open(a.json, "w"), indent=1)
    return 1 if found else 0


if __name__ == "__main__":
    sys.exit(main())
