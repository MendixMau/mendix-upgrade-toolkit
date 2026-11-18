#!/usr/bin/env python3
"""widgetroute.py: one replacement route per module for every deprecated or removed widget, and the safe ones done.

Why (cold rung 2, 10.24 -> 11.12): the build stopped on 36 Any Chart 3.x uses (DEPRECATED-11, T7-29) and said only
"replace with Charts 6". 18 of them sat in a Marketplace sample module of building blocks that nothing opens, 18 in five
snippets of the app's own dashboards. The person got a list of document names, not a way out. This reads the model and
gives, per module and per old widget, ONE recommendation, and does the mechanical part itself:

  ROUTE <module>: <widget> used <n>x in <documents>; <who opens them> -> <what to do> [STATUS] effort ~<time>
    Found: ... Searched: ... Candidates: A ... (recommended: why; effort; what changes), B ... Applied: ...

The toolkit heals itself: the recommended candidate goes into the test build, the person OKs it afterwards or picks B.
No item ever reads only "no replacement": it says where it searched, the candidates and what was applied.
STATUS: DONE (applied here, --apply) or AUTO (dry run: goes into the test build), ASK (a person decides: it blocks the
target), PLAN (deprecated, does not block this target yet). The routes are data: playbooks/widget-routes.json (old
widget id -> new widget, property mapping, effort, alternatives = candidates B...); nothing is hard-coded here.

  widgetroute.py <app dir|.mpr> --target <ver> [--routes F] [--approved F] [--apply [--pass replace|wrap|remove]]
                 [--done F] [--mdl F] [--failed PASSES] [--report F] [--json F]
  widgetroute.py <app dir> --target <ver> --ok-report DONE [--approved F]    the one-OK sections for what was applied

Rules, per module and route:
  - remove the module (AUTO/DONE): every use sits in a module that holds only page-type documents (pages, snippets,
    building blocks, layouts, page templates), no entities, nothing outside the module refers to any of its names and
    the navigation does not open it (a Marketplace sample of building blocks). --mdl gets `DROP MODULE IF EXISTS <module>;`
    (the pipeline runs it with mxcli). `keep-module <module>` in --approved (the person's B) declines; the uses then take
    the next rule.
  - replace (AUTO/DONE): the route's fit is exact and auto is true (Any Chart -> Custom chart: every setting keeps its
    key, the same plotly engine draws it) and the new widget is installed (widgets/*.mpk). --apply rewrites each
    widget in place: widget id and name, the renamed keys, translatable strings the new widget holds as plain strings
    (the en_US text). `mx update-widgets` then brings the saved definition to the installed package and keeps every
    value whose key and type match. A use whose static JSON holds what plotly 3 dropped (Charts 6 runs plotly.js 3), or
    a set value whose type changed, is APPROXIMATED, still replaced, with the trade-off on one line.
  - wrap (AUTO/DONE): a route with needs_container whose use sits outside a data view, list or grid (Any Chart straight
    on a snippet parameter: Custom chart there fails mx check, CE7006 on each attribute) gets a data view on the
    document's one object parameter around it, then the replace; with no such parameter (or attributes of another
    entity) it is an ASK: a data view by hand.
  - `route-b <route>` (the person's B on the replaced list) or a pass in --failed (the test build undid it): the route
    proposes its next candidate (alternatives) as an ASK.
  - otherwise ASK when the route blocks the target major (blocks_from), else PLAN: the new widget, the property mapping
    and the effort from the routes file. A route whose new widget is not installed asks to install its package first.
Each replaced widget and removed module is appended to --done; --ok-report turns that list into one OK per route and per
module (OK writes ok-replaced R N / remove-module M, B writes route-b R / keep-module M). --report gets the ASK items.
Excluded documents are skipped. Building blocks and page templates are design-time templates: never shown at runtime.
Exit: 0 = nothing left that blocks the target (DONE, AUTO and PLAN only), 1 = an ASK, 2 = input error.
"""
import argparse, json, os, re, sys, uuid

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(HERE))
from mprmodel import Model, text_of  # noqa: E402  model reader: modules, refs, navigation (MPR v1 and v2)
from widgetdrop import find, value  # noqa: E402
from missing_deps import installed_widgets  # noqa: E402

ROUTES = os.path.join(os.path.dirname(os.path.dirname(HERE)), "playbooks", "widget-routes.json")
KINDS = {"Forms$Page": "page", "Forms$Snippet": "snippet", "Forms$BuildingBlock": "building block",
         "Forms$Layout": "layout", "Forms$PageTemplate": "page template"}
TEMPLATES = {"Forms$BuildingBlock", "Forms$PageTemplate"}
SAFE_DOCS = set(KINDS) | {"Images$ImageCollection"}
# what gives a pluggable widget its object: a data view, list or grid around it, or a pluggable container (Data grid 2)
CONTAINERS = {"Forms$DataView", "Forms$ListView", "Forms$TemplateGrid", "Forms$DataGrid", "CustomWidgets$CustomWidget"}


def load_routes(path):
    try:
        d = json.load(open(path, encoding="utf-8"))
        for r in d["routes"]:
            r["_re"] = re.compile(r["match"])
        return d
    except (OSError, ValueError, KeyError, re.error) as e:
        sys.exit(f"widgetroute: cannot read the routes file {path}: {e}")


def route_of(routes, wid):
    return next((r for r in routes["routes"] if r["_re"].fullmatch(wid or "")), None)


def blocks(route, target):
    t = re.findall(r"\d+", target or "")
    return route.get("blocks_from") is not None and bool(t) and int(t[0]) >= int(route["blocks_from"])


def read_approved(path):
    """Lines of the approved file, a trailing '# ...' (who and why, decisions.py) dropped."""
    try:
        return {re.sub(r"\s+#.*$", "", x).strip() for x in open(path, encoding="utf-8")} - {""}
    except (OSError, TypeError):
        return set()


def widgets_in(d, inside=False):
    """(widget, inside a data container) for every pluggable widget of a document."""
    if isinstance(d, dict):
        if d.get("$Type") == "CustomWidgets$CustomWidget":
            yield d, inside
        inside = inside or d.get("$Type") in CONTAINERS
        for v in d.values():
            yield from widgets_in(v, inside)
    elif isinstance(d, list):
        for v in d:
            yield from widgets_in(v, inside)


def props(w):
    """[(key, property type dict, property dict)] of a widget instance (top level object)."""
    types = {repr(pt.get("$ID")): pt for pt in find(w.get("Type") or {}, lambda x: x.get("$Type") == "CustomWidgets$WidgetPropertyType")}
    out = []
    for p in (w.get("Object") or {}).get("Properties") or []:
        if isinstance(p, dict):
            pt = types.get(repr(p.get("TypePointer")))
            if pt:
                out.append((pt.get("PropertyKey"), pt, p))
    return out


def setting(p):
    v = p.get("Value") or {}
    return value(v) or text_of(v.get("TranslatableValue"))


def plotly3(texts, dropped):
    """Trade-off lines for a static plotly JSON that plotly.js 3 reads differently."""
    out = []

    def walk(x):
        if isinstance(x, dict):
            for k, v in x.items():
                if k in dropped and k != "title-string":
                    out.append(dropped[k])
                if k == "title" and isinstance(v, str) and v.strip():
                    out.append(dropped["title-string"])
                if k == "type" and v in dropped:
                    out.append(dropped[v])
                walk(v)
        elif isinstance(x, list):
            for v in x:
                walk(v)
    for t in texts:
        try:
            walk(json.loads(t))
        except ValueError:
            out += [dropped[k] for k in dropped if k != "title-string" and re.search(rf'"{k}"', t)]
    return sorted(set(out))


def check_use(w, route, dropped):
    """Trade-offs of replacing this use along an exact route ([] = exact)."""
    out, texts = [], []
    for key, pt, p in props(w):
        val = setting(p)
        if not val:
            continue
        if key not in route.get("props", {}):
            out.append(f"setting '{key}' has no place in {route['new_name']}")
        elif key in route.get("reset", {}):
            out.append(route["reset"][key])
        if key in route.get("to_string", []):
            texts.append(val)
    if route.get("plotly3"):
        out += plotly3(texts, dropped)
    return out


def swap(w, route):
    """Rewrite one widget instance along an exact route (in place)."""
    t = w["Type"]
    t["WidgetId"], t["WidgetName"], t["WidgetPluginWidget"] = route["new"], route["new_name"], True
    for key, pt, p in props(w):
        if key in route.get("to_string", []):
            (pt.get("ValueType") or {})["Type"] = "String"
            v = p.get("Value") or {}
            v["PrimitiveValue"] = text_of(v.get("TranslatableValue"))
            v["TranslatableValue"] = None
        new = route.get("props", {}).get(key)
        if new and new != key:
            pt["PropertyKey"] = new


def effort(minutes):
    return "a minute" if minutes <= 1 else f"~{minutes} min" if minutes < 60 else f"~{round(minutes / 60 + 0.24, 1):g} h"


def plural(n, word):
    return f"{n} {word}" + ("" if n == 1 else "es" if word.endswith(("x", "ch")) else "s")


def analyse(m, routes, have, target):
    """{(module, route id): {...}} with the uses, who opens the documents and the module facts."""
    callers = m.callers_index()
    nav = json.dumps(m.singletons.get("Navigation$NavigationDocument") or {}, default=str)
    groups = {}
    for d in m.all_docs:
        if d.type not in KINDS or d.data.get("Excluded") is True:
            continue
        for w, inside in widgets_in(d.data):
            r = route_of(routes, (w.get("Type") or {}).get("WidgetId"))
            if not r:
                continue
            g = groups.setdefault((d.module, r["id"]), {"module": d.module, "route": r, "uses": [], "docs": {}, "bare": []})
            g["uses"].append((d, w))
            if r.get("needs_container") and not inside:
                g["bare"].append((d, w))
            opened = sorted(c for c in callers.get(d.qn, ()) if c in m.docs and m.docs[c].type not in TEMPLATES)
            g["docs"][d.qn] = {"kind": KINDS[d.type], "opened": opened, "nav": bool(re.search(rf'"{re.escape(d.qn)}"', nav))}
    for g in groups.values():
        g["removable"], g["why_not"] = removable(m, g["module"], callers, nav)
    return groups


def removable(m, mod, callers, nav):
    """(True, roles note) when the module holds only page-type documents, no entities, and nothing outside refers to it."""
    docs = [d for d in m.all_docs if d.module == mod]
    other = sorted({d.type for d in docs} - SAFE_DOCS)
    if other:
        return False, f"it also holds {', '.join(t.split('$')[-1] for t in other)}"
    dm = m.docs.get(f"{mod}.$DomainModel")
    if dm and [e for e in dm.data.get("Entities") or [] if isinstance(e, dict)]:
        return False, "it has entities (data)"
    if re.search(rf'"{re.escape(mod)}\.', nav):
        return False, "the navigation opens it"
    outside = sorted({c for qn in m.docs if qn.startswith(mod + ".") for c in callers.get(qn, ()) if not c.startswith(mod + ".")}
                     | {qn for qn in m.docs if not qn.startswith(mod + ".") and any(r.startswith(mod + ".") for r in m.refs(qn))})
    if outside:
        return False, f"{outside[0]} refers to it"
    return True, ""


def wrap_target(d, w):
    """(parameter, entity, kind) of the one object parameter a bare use can be wrapped on, or (None, reason)."""
    if d.type not in ("Forms$Snippet", "Forms$Page"):
        return None, f"a {KINDS[d.type]} has no object to wrap it on"
    ps = [p for p in d.data.get("Parameters") or [] if isinstance(p, dict) and (p.get("ParameterType") or {}).get("Entity")]
    if len(ps) != 1:
        return None, f"the {KINDS[d.type]} has {len(ps) or 'no'} object parameters"
    ent = ps[0]["ParameterType"]["Entity"]
    attrs = {x.get("Attribute", "").rsplit(".", 1)[0] for x in find(w, lambda x: x.get("$Type") == "DomainModels$AttributeRef")} - {""}
    if attrs - {ent}:
        return None, f"its attributes belong to {', '.join(sorted(attrs - {ent}))}, not to the parameter {ps[0].get('Name')}"
    return (ps[0].get("Name"), ent, "SnippetParameter" if d.type == "Forms$Snippet" else "PageParameter"), ""


def wrap(doc, wname, param, ent, kind):
    """Put a data view on the parameter around the widget named wname (in place); its name is returned."""
    names = {x.get("Name") for x in find(doc, lambda x: "Name" in x)}
    name = next(f"dataView{k}" for k in range(1, 10000) if f"dataView{k}" not in names)
    for holder in find(doc, lambda x: True):
        for key, v in holder.items():
            if not isinstance(v, list):
                continue
            for i, w in enumerate(v):
                if isinstance(w, dict) and w.get("$Type") == "CustomWidgets$CustomWidget" and w.get("Name") == wname:
                    nid = (lambda: uuid.uuid4().bytes) if isinstance(w.get("$ID"), bytes) else (lambda: str(uuid.uuid4()))
                    v[i] = {"$ID": nid(), "$Type": "Forms$DataView",
                            "Appearance": {"$ID": nid(), "$Type": "Forms$Appearance", "Class": "", "DesignProperties": [3],
                                           "DynamicClasses": "", "Style": ""},
                            "ConditionalEditabilitySettings": None, "ConditionalVisibilitySettings": None,
                            "DataSource": {"$ID": nid(), "$Type": "Forms$DataViewSource",
                                           "EntityRef": {"$ID": nid(), "$Type": "DomainModels$DirectEntityRef", "Entity": ent},
                                           "ForceFullObjects": False,
                                           "SourceVariable": {"$ID": nid(), "$Type": "Forms$PageVariable", "LocalVariable": "",
                                                              "PageParameter": param if kind == "PageParameter" else "",
                                                              "SnippetParameter": param if kind == "SnippetParameter" else "",
                                                              "SubKey": "", "UseAllPages": False, "Widget": ""}},
                            "Editability": "Always", "FooterWidgets": [3], "LabelWidth": 3, "Name": name,
                            "NoEntityMessage": {"$ID": nid(), "$Type": "Texts$Text", "Items": [3]},
                            "ReadOnlyStyle": "Control", "ShowFooter": False, "TabIndex": 0, "Widgets": [3, w]}
                    return name
    return None


def cand(letter, name, why, minutes, changes, rec=False):
    return f"{letter} {name} ({'recommended: ' if rec else ''}{why}; {effort(minutes) if minutes else 'no work now'}; {changes})"


def alt_cands(r, n, start="B"):
    return [cand(chr(ord(start) + i), x["name"], x["why"], x.get("minutes_per_use", 30) * n, x["changes"])
            for i, x in enumerate(r.get("alternatives", []))]


def searched(routes, have):
    return (f"Searched: the platform-supported list (playbooks/widget-routes.json: {len(routes['routes'])} routes, from the "
            f"Marketplace packages), the installed widget packages ({len(have)} widgets in widgets/), the app's own modules "
            f"(navigation, page, snippet and microflow calls)")


def found(r, docs, nuse, mod, reach):
    kinds = {}
    for x in docs.values():
        kinds[x["kind"]] = kinds.get(x["kind"], 0) + 1
    where = ", ".join(plural(n, k) for k, n in sorted(kinds.items(), key=lambda kv: -kv[1]))
    return f"Found: {r['name']} on {where} ({plural(nuse, 'use')}) in module {mod}; {reach}"


def section(title, shape, rec, writes=()):
    return "\n".join([f"## {title}", ""] + shape + ["", f"Recommended: {rec}"] + list(writes)) + "\n"


def ok_report(done, routes, have, ok):
    """NJ sections (one OK each) for what the test build already did: the replaced widgets per route, each removed module."""
    rows = [x.rstrip("\n") for x in open(done, encoding="utf-8") if x.strip()]
    by_id = {r["id"]: r for r in routes["routes"]}
    out = []
    for rid in sorted({m.group(1) for x in rows for m in [re.search(r" \[(\w+)\] ", x)] if m and not x.startswith("REMOVED-MODULE")}):
        r = by_id.get(rid)
        mine = [x for x in rows if f" [{rid}] " in x and not x.startswith("REMOVED-MODULE")]
        if not r or f"ok-replaced {rid} {len(mine)}" in ok:
            continue
        napx = sum(1 for x in mine if x.startswith("APPROXIMATED"))
        docs = sorted({x.split()[1] for x in mine})
        noun = "charts" if r["package"].startswith("Charts") else "widgets"
        lst_ = [f"- {x.split()[1]} {x.split()[2]}" + (f": {x.split(': ', 1)[1]}" if ": " in x else "") for x in mine[:40]]
        shape = [f"Found: {r['name']} on {len(docs)} {'page or snippet' if len(docs) == 1 else 'pages or snippets'} ({plural(len(mine), 'use')}): {', '.join(d.split('.')[-1] for d in docs[:6])}"
                 + (" and more" if len(docs) > 6 else ""), searched(routes, have),
                 "Candidates: " + ", ".join([cand("A", f"{r['new_name']} ({r['package']})", r["mapping"], r.get("minutes_per_use", 5) * len(mine),
                                                  "the widget id changes, every setting is kept", rec=True)] + alt_cands(r, len(mine))),
                 f"Applied: A in the test build, as repair commits 'repair: deprecated widgets ... (widgetroute)' (mx check not worse):"] + lst_
        b = r.get("alternatives") and f"B writes: widget-routes-approved.txt: route-b {rid}"
        out.append(section(f"{len(mine)} {noun} replaced by {r['package']} ({r['new_name']}), {napx} approximated: OK?", shape,
                           "OK; look at the charts on their pages once (the gate's screenshots show them). Picking B undoes those commits on the rerun and asks for the rebuild.",
                           [f"OK writes: widget-routes-approved.txt: ok-replaced {rid} {len(mine)}"] + ([b] if b else [])))
    for x in rows:
        m = re.match(r"REMOVED-MODULE (\S+) \[(\w+)\] (\d+) (.*)$", x)
        if not m or {f"remove-module {m[1]}", f"keep-module {m[1]}"} & ok:
            continue
        r, n = by_id.get(m[2], {"name": m[2], "new_name": "the new widget", "minutes_per_use": 5}), int(m[3])
        shape = [f"Found: {r['name']} {plural(n, 'time')} in module {m[1]}: {m[4]}", searched(routes, have),
                 "Candidates: " + ", ".join([cand("A", "remove the module", "nothing in the app opens or refers to it", 1,
                                                  "its sample pages and their theme and Java files go", rec=True),
                                             cand("B", "keep the module", "if someone copies its samples", 5 * n,
                                                  f"each chart gets a data view and {r['new_name']} by hand")]),
                 "Applied: A in the test build, its own repair commit 'repair: unused sample module removed (widgetroute)' (mx check not worse)"]
        out.append(section(f"Module {m[1]}: unused sample module removed: OK?", shape,
                           "OK. Picking B puts the module back (the commit is reverted on the rerun).",
                           [f"OK writes: widget-routes-approved.txt: remove-module {m[1]}",
                            f"B writes: widget-routes-approved.txt: keep-module {m[1]}"]))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("project")
    ap.add_argument("--target", required=True)
    ap.add_argument("--routes", default=ROUTES)
    ap.add_argument("--approved", help="lines: keep-module M, route-b ROUTE, remove-module M, ok-replaced ROUTE N (widget-routes-approved.txt)")
    ap.add_argument("--apply", action="store_true", help="replace, wrap and (with --mdl) remove in the .mpr (commit the app first)")
    ap.add_argument("--pass", dest="only", choices=["replace", "wrap", "remove"], help="with --apply: only this kind")
    ap.add_argument("--failed", default="", help="passes the test build undid (replace,wrap,remove): their candidate A failed")
    ap.add_argument("--done", help="append each replaced widget and removed module here")
    ap.add_argument("--mdl", help="write DROP MODULE for a removal here (overwritten)")
    ap.add_argument("--report", help="write the NEEDS-JUDGMENT sections of what is left (overwritten)")
    ap.add_argument("--ok-report", help="read this --done file and print the one-OK sections for what was applied, then stop")
    ap.add_argument("--json")
    a = ap.parse_args()
    routes = load_routes(a.routes)
    ok = read_approved(a.approved)
    failed = set(filter(None, a.failed.split(",")))
    if a.ok_report:
        proj = a.project if os.path.isdir(a.project) else os.path.dirname(os.path.abspath(a.project))
        if os.path.isfile(a.ok_report):
            print("\n".join(ok_report(a.ok_report, routes, installed_widgets(proj, []), ok)), end="")
        return 0
    try:
        m = Model.load(a.project)
    except SystemExit as e:
        print(f"widgetroute: {e}", file=sys.stderr); return 2
    proj = os.path.dirname(os.path.abspath(m.path))
    have = installed_widgets(proj, [])
    groups = analyse(m, routes, have, a.target)
    nuse = sum(len(g["uses"]) for g in groups.values())
    lines = [f"# widgetroute {m.path} (target {a.target}): {plural(nuse, 'deprecated widget use')} in "
             f"{plural(len({g['module'] for g in groups.values()}), 'module')}"]
    swaps, drops, out, report = [], [], [], []
    counts = {"DONE": 0, "AUTO": 0, "ASK": 0, "PLAN": 0}
    srch = searched(routes, have)
    do = (lambda kind: a.apply and a.only in (None, kind))
    for (mod, rid), g in sorted(groups.items()):
        r, uses, docs = g["route"], g["uses"], g["docs"]
        kinds = {}
        for qn, x in docs.items():
            kinds[x["kind"]] = kinds.get(x["kind"], 0) + 1
        where = ", ".join(plural(n, k) for k, n in sorted(kinds.items(), key=lambda kv: -kv[1]))
        opened = sorted({o for x in docs.values() for o in x["opened"]}) + (["the navigation"] if any(x["nav"] for x in docs.values()) else [])
        reach = (f"opened by {', '.join(o.split('.')[-1] for o in opened[:4])}{' and more' if len(opened) > 4 else ''}" if opened
                 else "nothing opens them (no navigation, page, snippet or microflow call)" if not all(x["kind"] in ("building block", "page template") for x in docs.values())
                 else "templates, never shown at runtime; nothing opens them")
        head = f"ROUTE {mod}: {r['name']} used {len(uses)}x in {where}; {reach}"
        row = {"module": mod, "route": rid, "row": r.get("row"), "uses": len(uses), "documents": sorted(docs), "opened_by": opened}
        fnd = found(r, docs, len(uses), mod, reach)
        if g["removable"] and f"keep-module {mod}" not in ok and "remove" not in failed:
            # self-heal: a module nothing opens or refers to is removed in the test build; the OK (or B: keep) comes after
            st = "DONE" if do("remove") and a.mdl else "AUTO"
            rec = "remove the module" + ("; DROP MODULE written for mxcli" if st == "DONE" else "") + f": it holds only {where} and nothing in the app refers to it"
            if st == "DONE":
                drops.append((mod, rid, len(uses), f"{where}; {reach}"))
            lines.append(f"{head} -> {rec} [{st}] effort a minute")
            lines += [f"  {fnd}", f"  {srch}",
                      "  Candidates: " + ", ".join([cand("A", "remove the module", "nothing in the app opens or refers to it", 1,
                                                         "its sample pages and their theme and Java files go", rec=True),
                                                    cand("B", "keep the module", "if someone copies its samples", 5 * len(uses),
                                                         f"each chart gets a data view and {r['new_name']} by hand")]),
                      f"  Applied: {'A in the test build' if st == 'DONE' else 'A goes into the test build as its own repair commit'}; OK or B (keep-module {mod}) afterwards"]
            row.update(status=st, action="remove-module", recommendation=rec)
        elif (r.get("fit") == "exact" and r.get("auto") and r.get("new") in have and f"route-b {rid}" not in ok
              and "replace" not in failed):
            bare = g["bare"]
            uses = [u for u in uses if u not in bare]
            wraps, stuck = [], []
            for d, w in bare:
                tgt, why = wrap_target(d, w)
                (wraps.append((d, w, tgt)) if tgt and "wrap" not in failed else stuck.append((d, w, why or "the wrap failed in the test build")))
            head = head.replace(f"used {len(g['uses'])}x", f"used {len(uses) + len(wraps)}x", 1)
            dropped = routes.get("plotly3_dropped", {})
            trade = [(d, w, check_use(w, r, dropped), None) for d, w in uses]
            trade += [(d, w, check_use(w, r, dropped) + [f"wrapped in a data view on the parameter {t[0]} ({r['new_name']} reads its object only there)"], t)
                      for d, w, t in wraps]
            napprox = sum(1 for t in trade if t[2])
            st = "DONE" if do("replace") or do("wrap") else "AUTO"
            fnd = found(r, {q: docs[q] for q in {d.qn for d, w, t, tgt in trade}}, len(trade), mod, reach)
            rec = (f"{'replaced' if st == 'DONE' else 'replace'} by {r['new_name']} ({r['package']}), the same settings"
                   + (f"; {napprox} approximated" if napprox else ""))
            if trade:
                n = len(trade)
                lines.append(f"{head} -> {rec} [{st}] effort {effort(r.get('minutes_per_use', 5) * n)} to look at the result")
                lines += [f"  {fnd}", f"  {srch}",
                          "  Candidates: " + ", ".join([cand("A", f"{r['new_name']} ({r['package']})", r["mapping"], r.get("minutes_per_use", 5) * n,
                                                             "the widget id changes, every setting is kept", rec=True)] + alt_cands(r, n)),
                          f"  Applied: {'A in the test build' if st == 'DONE' else 'A goes into the test build as one repair commit'}; OK or B afterwards"]
            for d, w, t, tgt in trade:
                kind = "wrap" if tgt else "replace"
                done_ = do(kind)
                verb = ("WRAPPED" if tgt else "APPROXIMATED" if t else "REPLACED") if done_ else ("WOULD-WRAP" if tgt else "WOULD-APPROXIMATE" if t else "WOULD-REPLACE")
                lines.append(f"  {verb} {d.qn} {w.get('Name')} -> {r['new_name']}" + (f": {'; '.join(t)}" if t else " (exact)"))
                if done_:
                    swaps.append((d, w, r, t, tgt))
            row.update(status=st, action="replace", recommendation=rec, approximated=napprox, uses=len(trade))
            if stuck:  # mx check: CE7006 on each attribute of a Custom chart that sits straight on a snippet parameter
                if trade:
                    counts[st] += 1
                    out.append(row)
                st = "ASK" if blocks(r, a.target) else "PLAN"
                bd = sorted({d.qn for d, w, y in stuck})
                rec = (f"put a data view around each, then rerun: {r['new_name']} then goes in here "
                       f"({r['new_name']} reads its settings only inside a data view or list; {r['name']} took the snippet's object)")
                lines.append(f"ROUTE {mod}: {r['name']} used {len(stuck)}x outside a data view in {', '.join(q.split('.')[-1] for q in bd)}"
                             f" -> {rec} [{st}] effort {effort(5 * len(stuck))}")
                shape = [found(r, {q: docs[q] for q in bd}, len(stuck), mod, reach), srch,
                         "Candidates: " + ", ".join([cand("A", f"a data view by hand around each, then {r['new_name']}",
                                                          f"no object to wrap it on automatically: {stuck[0][2]}", 5 * len(stuck),
                                                          "one data view per chart; the rerun swaps the widget", rec=True)] + alt_cands(r, len(stuck))),
                         f"Applied: not yet: {stuck[0][2]}; once the data views are there the rerun applies {r['new_name']} by itself"]
                lines += [f"  {x}" for x in shape] + [f"  OUTSIDE-DATA-VIEW {d.qn} {w.get('Name')}" for d, w, y in stuck]
                if st == "ASK":
                    report.append(section(f"{r['name']} in {mod}: {len(stuck)} outside a data view, a data view by hand recommended", shape,
                                          f"A: put a data view around each ({effort(5 * len(stuck))}), then rerun."))
                row = {"module": mod, "route": rid, "row": r.get("row"), "uses": len(stuck), "documents": bd,
                       "opened_by": opened, "status": st, "action": "wrap", "recommendation": rec}
        else:
            st = "ASK" if blocks(r, a.target) else "PLAN"
            n = len(uses)
            alts = r.get("alternatives", [])
            if f"route-b {rid}" in ok and alts:  # the person picked B on the replaced list: that rebuild is the route now
                x = alts[0]
                rec = f"rebuild as {x['name']} (picked B): {x['changes']}"
                mins = x.get("minutes_per_use", 30) * n
                cands = [cand("A", x["name"], "picked B: " + x["why"], mins, x["changes"], rec=True)]
                applied = f"not automatic: a rebuild by hand; {r['new_name']} (candidate A) was undone on your pick"
            elif r.get("fit") == "exact" and r.get("auto") and r.get("new") not in have:
                rec = f"install {r['package']} (it ships {r['new_name']}), then rerun: the replacement is then done here"
                mins = 10
                cands = [cand("A", f"install {r['package']}, then {r['new_name']} here", f"{r['package']} is not installed", 10,
                              "the package comes from the Marketplace; the rerun swaps the widgets", rec=True)] + alt_cands(r, n)
                applied = f"will apply A on your OK: install {r['package']} from the Marketplace in Studio Pro, then rerun"
            elif r.get("fit") == "exact" and r.get("auto") and failed & {"replace", "wrap"}:
                x = alts[0] if alts else {"name": f"rebuild the pages with {r['new_name']} by hand", "why": "the settings are set again",
                                          "minutes_per_use": 30, "changes": "each widget is set up again"}
                rec = f"rebuild as {x['name']}: {r['new_name']} failed the check in the test build"
                mins = x.get("minutes_per_use", 30) * n
                cands = [cand("A", f"{r['new_name']} ({r['package']})", "tried: mx check got worse, undone", 0, "nothing changed"),
                         cand("B", x["name"], x["why"], mins, x["changes"], rec=True)]
                applied = f"A tried in the test build: mx check got worse, undone (see the build log). Proposal: B, {x['name']}, {effort(mins)}"
            else:
                rec = f"replace with {r['new_name']} ({r['package']}){' (closest option)' if r.get('fit') == 'approximate' else ''}: {r['mapping']}"
                mins = r.get("minutes_per_use", 30) * n
                cands = [cand("A", f"{r['new_name']} ({r['package']})", r["mapping"] if r.get("fit") != "approximate" else "the closest option",
                              mins, r["mapping"] if r.get("fit") == "approximate" else "the settings are set again", rec=True)] + alt_cands(r, n)
                applied = (f"not automatic: the settings do not carry over one to one; A is a rebuild by hand" if st == "ASK"
                           else f"nothing: it does not block {a.target}; A is planned for the rung that needs it")
            lines.append(f"{head} -> {rec} [{st}] effort {effort(mins)}")
            shape = [fnd, srch, "Candidates: " + ", ".join(cands), f"Applied: {applied}"]
            lines += [f"  {x}" for x in shape]
            if g["removable"] is False and g["why_not"] and not opened:
                lines.append(f"  not removed: {g['why_not']}")
            lines.append(f"  WHY {r['why']}")
            if st == "ASK":
                aname = next(re.match(r"[A-Z] (.+?) \(recommended", c) for c in cands if "(recommended" in c)
                report.append(section(f"{r['name']} in {mod}: {plural(n, 'use')}, {aname[1]} recommended", shape, f"{rec} ({effort(mins)})"))
            row.update(status=st, action="manual", recommendation=rec)
        counts[st] += 1
        out.append(row)
    if swaps:
        from copy_mappings import Mpr
        import bson
        mp = Mpr(m.path)
        todo = {}
        for d, w, r, t, tgt in swaps:
            todo.setdefault((d.module, d.data.get("Name"), d.type), []).append((w.get("Name"), r, tgt))
        for uid in list(mp.rows):
            d = mp.decode(uid)
            if not d or d.get("$Type") not in KINDS:
                continue
            key = (mp.module_of(uid), d.get("Name"), d.get("$Type"))
            if key not in todo:
                continue
            names = {n: (r, tgt) for n, r, tgt in todo[key]}
            for w in list(find(d, lambda x: x.get("$Type") == "CustomWidgets$CustomWidget" and x.get("Name") in names)):
                if route_of(routes, (w.get("Type") or {}).get("WidgetId")):
                    swap(w, names[w["Name"]][0])
            for n, (r, tgt) in names.items():
                if tgt:
                    wrap(d, n, *tgt)
            mp.write(uid, bson.encode(d))
    if a.done and (swaps or drops):
        with open(a.done, "a", encoding="utf-8") as f:
            for d, w, r, t, tgt in swaps:
                f.write(f"{'APPROXIMATED' if t else 'REPLACED'} {d.qn} {w.get('Name')} [{r['id']}] {r['name']} -> {r['new_name']}"
                        + (f": {'; '.join(t)}" if t else "") + "\n")
            for mod, rid, n, why in drops:
                f.write(f"REMOVED-MODULE {mod} [{rid}] {n} {why}\n")
    if a.mdl:
        with open(a.mdl, "w", encoding="utf-8") as f:
            f.write("".join(f"DROP MODULE IF EXISTS {x[0]};\n" for x in drops))
    if a.report:
        with open(a.report, "w", encoding="utf-8") as f:
            f.write("\n".join(report))
    nrem = sum(1 for o in out if o.get("action") == "remove-module")
    nsw = len(swaps) if a.apply else sum(o.get("uses", 0) for o in out if o.get("action") == "replace")
    napx = sum(1 for s in swaps if s[3]) if a.apply else sum(o.get("approximated", 0) for o in out if o.get("action") == "replace")
    lines.append(f"summary: {plural(nsw, 'widget')} {'replaced' if swaps else 'to replace'} in the test build ({napx} approximated), "
                 f"{plural(nrem, 'module')} {'removed' if drops else 'to remove'}, OK afterwards; {counts['ASK']} to decide, "
                 f"{counts['PLAN']} planned (not blocking {a.target})" if groups else "summary: no deprecated widget in use")
    print("\n".join(lines))
    if a.json:
        json.dump({"target": a.target, "routes": out}, open(a.json, "w"), indent=1)
    return 1 if counts["ASK"] else 0


if __name__ == "__main__":
    sys.exit(main())
