#!/usr/bin/env python3
"""changeledger.py: what left the model and what was swapped, per document, original against final (LC-2, backlog 157).

Why: the LineApp owner read a 10.24 -> 11.12 React hand-over as "the tool silently removes many elements", although every
removal was in the run's decision log. An owner reads one table, not a decision log: which page lost which widget, which
document is gone, which widget type became which, and the decision that says why.

  changeledger.py <original dir|.mpr> <final dir|.mpr> [--decisions FILE ...] [--md out.md]

Documents: pages, snippets, layouts, building blocks, page templates, microflows, nanoflows, constants and the other
document types mprmodel reads. Widgets: every named widget of a page, snippet or layout that is in both models, keyed
by its name (Studio Pro keeps names unique per document); a pluggable widget's type is its widget id.
  REMOVED   a document, or a widget of a document that is still there, that is gone in the final model
  RENAMED   a removed document with exactly one added document of the same module and type whose name extends or
            shortens its name (listed, not a removal)
  REPLACED  same widget name, other type (Static image -> Image, HTML snippet -> Events): counted per type pair
  ADDED     documents only, counted per type
Who: "update" when the module is a Marketplace module whose version changed (the module update did it), "run" otherwise.
--decisions: the run's decision files (AGENT-DECISIONS.md, DECISIONS.md, PROPOSAL.md). A run removal is EXPLAINED when its
document's qualified name appears in one of them (the first decision id on that line, D12 or D-12, is cited), else
UNEXPLAINED.
Exit: 0 no UNEXPLAINED run removal (or no --decisions given: everything listed, nothing judged), 1 UNEXPLAINED run
removals, 2 input error.
"""
import argparse, collections, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mprmodel  # noqa: E402

FORMS = ("Forms$Page", "Forms$Snippet", "Forms$Layout")
SKIP_DOC = {"Forms$BuildingBlock", "Forms$PageTemplate"}   # their widgets are templates, not screens: documents only
DECISION = re.compile(r"\b(D-?\d+[a-z]?)\b")


def wtype(x):
    t = x.get("$Type", "")
    if t == "CustomWidgets$CustomWidget":
        return (x.get("Type") or {}).get("WidgetId") or t
    return t.split("$", 1)[-1]


def widgets(data, out):
    if isinstance(data, dict):
        t = data.get("$Type", "")
        if isinstance(data.get("Name"), str) and data["Name"] and t.startswith(("Forms$", "CustomWidgets$")) \
                and t not in FORMS and t not in SKIP_DOC:
            out.setdefault(data["Name"], wtype(data))
        for v in data.values():
            widgets(v, out)
    elif isinstance(data, list):
        for v in data:
            widgets(v, out)
    return out


def updated_modules(o, n):
    out = set()
    for name, info in o.modules.items():
        new = n.modules.get(name)
        if info.get("from_appstore") and new and str(new.get("version")) != str(info.get("version")):
            out.add(name)
    return out


def load_decisions(paths):
    lines = []
    for p in paths or []:
        with open(p, errors="replace") as fh:
            lines += fh.read().splitlines()
    return lines


def explain(qn, lines):
    pat = re.compile(r"(?<![\w.])" + re.escape(qn) + r"(?![\w])")
    bare = qn.split(".", 1)[-1]
    short = re.compile(r"(?<![\w.])" + re.escape(bare) + r"(?![\w])")
    # the bare name alone only for distinctive names: "Home" or "Login" would match unrelated decision lines
    for want in (pat, short) if len(bare) >= 8 else (pat,):
        for ln in lines:
            if want.search(ln):
                m = DECISION.search(ln)
                return m.group(1) if m else "logged"
    return None


def ledger(o, n, lines):
    upd = updated_modules(o, n)
    who = lambda qn: "update" if qn.split(".", 1)[0] in upd else "run"
    od = {(d.qn, d.type): d for d in o.all_docs}
    nd = {(d.qn, d.type): d for d in n.all_docs}
    rows = []   # (kind, who, document, widget, what, why)
    new_docs = set(nd) - set(od)
    for qn, t in sorted(set(od) - set(nd)):
        if qn in {k[0] for k in nd}:
            continue   # same name, other document type: not a removal
        mod, name = qn.split(".", 1)
        # a rename keeps module and type and extends or shortens the name (D77: ACT_OnClickSourceEquipment ->
        # ACT_OnClickSourceEquipmentTransfer); only a single candidate counts, two would be a guess
        cand = [q for q, tt in new_docs if tt == t and q.split(".", 1)[0] == mod
                and (q.split(".", 1)[1].startswith(name) or name.startswith(q.split(".", 1)[1]))]
        if len(cand) == 1:
            new_docs.discard((cand[0], t))
            rows.append(("RENAMED", who(qn), qn, "", "%s -> %s" % (t.split("$", 1)[-1], cand[0]), None))
            continue
        rows.append(("REMOVED", who(qn), qn, "", t.split("$", 1)[-1], explain(qn, lines) if lines else None))
    pairs = collections.Counter()
    where = collections.defaultdict(set)
    for (qn, t), d in sorted(od.items()):
        if t not in FORMS or (qn, t) not in nd:
            continue
        a, b = widgets(d.data, {}), widgets(nd[(qn, t)].data, {})
        for name, wt in sorted(a.items()):
            if name not in b:
                rows.append(("REMOVED", who(qn), qn, name, wt, explain(qn, lines) if lines else None))
            elif b[name] != wt:
                pairs[(wt, b[name])] += 1
                where[(wt, b[name])].add(qn)
    added = collections.Counter(t.split("$", 1)[-1] for k, t in new_docs)
    return rows, pairs, where, added, upd


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("original")
    ap.add_argument("final")
    ap.add_argument("--decisions", nargs="+")
    ap.add_argument("--md")
    a = ap.parse_args(argv)
    for p in [a.original, a.final] + (a.decisions or []):
        if not os.path.exists(p):
            print("changeledger: %s does not exist" % p, file=sys.stderr)
            return 2
    o, n = mprmodel.Model.load(a.original), mprmodel.Model.load(a.final)
    lines = load_decisions(a.decisions)
    rows, pairs, where, added, upd = ledger(o, n, lines)
    renamed = [r for r in rows if r[0] == "RENAMED"]
    rows = [r for r in rows if r[0] != "RENAMED"]
    run = [r for r in rows if r[1] == "run"]
    unexplained = [r for r in run if lines and not r[5]]
    docs_gone = sum(1 for r in rows if not r[3])
    head = ("changeledger: %d documents in the original, %d in the final: %d documents removed, %d widgets removed, "
            "%d widgets replaced, %d documents added; %d removals by the run, %d by module updates (%s)" % (
                len(o.all_docs), len(n.all_docs), docs_gone, len(rows) - docs_gone, sum(pairs.values()),
                sum(added.values()), len(run), len(rows) - len(run), ", ".join(sorted(upd)) or "none"))
    print(head)
    for r in renamed:
        print("  RENAMED  %-6s %s (%s)" % (r[1], r[2], r[4]))
    for (old, new), c in pairs.most_common():
        print("  REPLACED %4d  %s -> %s (%d documents)" % (c, old, new, len(where[(old, new)])))
    for kind, w, qn, name, what, why in rows:
        if w == "run":
            tag = ("EXPLAINED %s" % why) if why else ("UNEXPLAINED" if lines else "")
            print("  REMOVED  %-6s %s%s (%s) %s" % (w, qn, "/" + name if name else "", what, tag))
    print("  (%d removals by module updates: see --md)" % (len(rows) - len(run)))
    if not lines:
        print("NOTE: no --decisions given: removals are listed, not judged")
    elif unexplained:
        print("FAIL: %d removal(s) by the run name no decision: say why in the decision log or put them back" % len(unexplained))
    else:
        print("PASS: every removal by the run names a decision")
    if a.md:
        with open(a.md, "w") as fh:
            fh.write("# What changed in the model\n\n%s\n\n" % head)
            fh.write("## Widgets replaced\n\n| Count | Old widget | New widget | Documents |\n|---|---|---|---|\n")
            for (old, new), c in pairs.most_common():
                docs = sorted(where[(old, new)])
                fh.write("| %d | %s | %s | %s |\n" % (c, old, new, ", ".join("`%s`" % d for d in docs[:12]) + (
                    " and %d more" % (len(docs) - 12) if len(docs) > 12 else "")))
            for label, who_ in (("Removed by the run", "run"), ("Removed by module updates", "update")):
                sel = [r for r in rows if r[1] == who_]
                fh.write("\n## %s (%d)\n\n| Document | Widget | Type | Why |\n|---|---|---|---|\n" % (label, len(sel)))
                for kind, w, qn, name, what, why in sel:
                    fh.write("| `%s` | %s | %s | %s |\n" % (qn, name or "(whole document)", what,
                             why or ("module update" if w == "update" else "**no decision**" if lines else "")))
            if renamed:
                fh.write("\n## Documents renamed (%d)\n\n" % len(renamed) + "".join("- `%s`: %s\n" % (r[2], r[4]) for r in renamed))
            if added:
                fh.write("\n## Documents added\n\n" + "".join("- %d %s\n" % (c, t) for t, c in added.most_common()))
    return 1 if unexplained else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
