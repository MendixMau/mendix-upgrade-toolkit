#!/usr/bin/env python3
"""absentmods.py: which modules does a planned module update call that are neither in the app nor in the plan? (GM-12)

  absentmods.py APP --plan-file plan.txt [--plan-file plan-pre.txt] [--cache DIR] [--json out.json]
  APP            the app folder (the .mpr, mprcontents/ side by side) or the .mpr itself
  --plan-file    stepupdate's plan.txt: "<content id> <version> <Module>" per line, # comments allowed. Repeatable: on a 10.x to
                 11 run the updates are split between plan-pre.txt (before the convert) and plan.txt; give both. Modules of every
                 file count as planned, and the updates of every file are checked.
  --cache        where the packages are (default UPG_CACHE or ~/.cache/upgrade-toolkit/mpk): <content id>-<version>.mpk,
                 the same cache and naming as crosscalls.py, planbuild.py and localedits.py. Never downloaded here.

NotificationProducer 3.1.0 -> 4.1.0: 4.1.0 calls MxTokenModule, which the app does not have. 31 CE1613 at the build, and
nothing at plan time said so (bin/repair/missing_module_stop.py stops at the build, after the update has run). This reads
the target package's project.mpr (crosscalls.package_model) and lists the modules its non-excluded documents refer to
that are none of: a module of the package itself, a module of the app, a module on a plan file, System, an add-on
(modules/*.mxmodule) of the app. "Refer to" is what bin/repair/missing_deps.py counts: a qualified name in a reference
field (Entity, Microflow, Page, Generalization ... : its REF_KEYS), so a text that only looks like Module.Name is not one.
A plan line whose version is the installed one is no update and is skipped.
Limits: only the reference fields of REF_KEYS are scanned (not XPath, expression text or widget properties), and module names
are matched exactly, so a renamed module or a case difference can give a false NEEDS.

Output: a header with the denominators (plan lines, checked, not checked, skipped), then
  NEEDS <Module>: called by <P> <installed> -> <plan> (<n> refs, e.g. <kind> <document> -> <Module.Name>; ...)
  NOT CHECKED <P> <plan version>: <why> (never read as "needs nothing")
Exit: 0 every update checked and none needs an absent module, 1 at least one NEEDS (a section-3 item "needs module X"
in the proposal: install it, or hold the caller), 3 no NEEDS but a package was not checked (not cached, unreadable),
2 input error (no model, no plan file). NEEDS wins over NOT CHECKED.

Producer: the triage step (steps/triage.md item 3, after planbuild.py) and step_propose in bin/cloud/upgrade-pipeline.sh
write $W/absentmods.json (--json); bin/proposal.py reads it. Consumers of the same fact at the build: missing_deps.py ->
missing_module_stop.py.
"""
import argparse, collections, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "repair"))
import mprmodel  # noqa: E402
import crosscalls  # noqa: E402  package_model, read_first_words, entity_names: the readers crosscalls.py already has
import missing_deps  # noqa: E402  REF_KEYS, QN, BUILTIN: the one definition of "a reference to a module"


def refs_to_modules(model, skip):
    """{module: [(document, target)]} for every qualified name in a reference field of a non-excluded document whose
    module is not one of `skip`."""
    out = collections.defaultdict(list)

    def walk(d, key, doc):
        if isinstance(d, dict):
            for k, v in d.items():
                if k not in ("$ID", "GUID"):
                    walk(v, k, doc)
        elif isinstance(d, list):
            for v in d:
                walk(v, key, doc)
        elif isinstance(d, str) and key in missing_deps.REF_KEYS:
            m = missing_deps.QN.match(d)
            if m and m.group(1) not in skip:
                out[m.group(1)].append((doc, d))

    docs = list(model.all_docs) + [d for d in model.docs.values() if d.type == "DomainModels$DomainModel"]
    for d in docs:
        if d.data.get("Excluded"):
            continue
        name = f"{d.module}.{d.data.get('Name')}" if d.type != "DomainModels$DomainModel" else f"{d.module} domain model"
        walk(d.data, None, name)
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("app")
    ap.add_argument("--plan-file", action="append")
    ap.add_argument("--cache", default=os.environ.get("UPG_CACHE") or os.path.expanduser("~/.cache/upgrade-toolkit/mpk"))
    ap.add_argument("--json")
    a = ap.parse_args()
    if not a.plan_file:
        print("absentmods: give --plan-file plan.txt", file=sys.stderr)
        return 2
    try:
        plan = [x for f in a.plan_file for x in crosscalls.read_first_words(f, True)]
    except OSError as e:
        print(f"absentmods: {e}", file=sys.stderr)
        return 2
    try:
        model = mprmodel.Model.load(a.app)
    except SystemExit as e:
        print(e, file=sys.stderr)
        return 2
    base = os.path.dirname(os.path.abspath(model.path))
    addons = set()
    mdir = os.path.join(base, "modules")
    if os.path.isdir(mdir):
        addons = {f[:-9] for f in os.listdir(mdir) if f.endswith(".mxmodule")}
    planned = {n for n, _ in plan}
    have = set(model.modules) | planned | addons | set(missing_deps.BUILTIN)

    needs, unchecked, checked, skipped = collections.OrderedDict(), [], 0, 0
    for pm, ver in plan:
        inst = (model.modules.get(pm) or {}).get("version") or ""
        cid = (model.modules.get(pm) or {}).get("package_id")
        if pm not in model.modules or (inst and inst == ver):
            skipped += 1   # not in the app (a new module is no update) or already at the plan version
            continue
        pkg = crosscalls.package_model(a.cache, cid, ver)
        if pkg is None:
            unchecked.append((pm, ver, f"the package {cid or '<content id unknown>'}-{ver}.mpk is not in the cache {a.cache} "
                                       "or cannot be read; nothing was downloaded here"))
            continue
        checked += 1
        for x, rows in refs_to_modules(pkg, have | set(pkg.modules)).items():
            rows = sorted(set(rows))
            needs.setdefault(x, {})[pm] = {"installed": inst, "plan": ver, "refs": len(rows),
                                           "examples": [list(r) for r in rows[:3]]}
    print(f"absentmods: {len(plan)} plan line(s), {checked} package(s) read, {len(unchecked)} NOT CHECKED, {skipped} skipped "
          f"(no update or not an installed module); app modules {len(model.modules)}")
    for x, by in sorted(needs.items()):
        parts = [f"{p} {v['installed'] or '?'} -> {v['plan']} ({v['refs']} refs, e.g. "
                 + "; ".join(f"{doc} -> {tgt}" for doc, tgt in v["examples"]) + ")" for p, v in sorted(by.items())]
        print(f"NEEDS {x}: called by " + ", ".join(parts))
    for pm, ver, why in unchecked:
        print(f"NOT CHECKED {pm} {ver}: {why}")
    print(f"absentmods: {len(needs)} absent module(s) needed" + (f", {len(unchecked)} update(s) NOT CHECKED (not clean)" if unchecked else ""))
    if needs:
        print("  each is CE1613 at the build: install the module before the update (mxcli marketplace search/install), or hold "
              "the caller at its current version; the build-time stop is bin/repair/missing_module_stop.py")
    if a.json:
        json.dump({"checked": checked, "skipped": skipped, "needs": needs,
                   "unchecked": [{"module": m, "version": v, "reason": w} for m, v, w in unchecked]}, open(a.json, "w"), indent=1)
    return 1 if needs else 3 if unchecked else 0


if __name__ == "__main__":
    sys.exit(main())
