#!/usr/bin/env python3
"""brainnotes.py: the company brain's notes that belong next to a run event (a held module, a route, a failed check).

Why (cold test WM1, 2026-11-16): the toolkit read only the brain's version tables. The brain also holds the practice and
pitfall notes for exactly the events a run stops on (never edit a Marketplace module, hide Atlas layouts in the company
UI module, PDFBox 2 jars next to PDFBox 3 after a Community Commons update), and no card showed them. The data test hit
the PDFBox case by hand while the brain already had the note.

Search, no model: every note's title, frontmatter keywords and body are scored against the query words (idf weighted;
title x3, keywords x2, body x1), plain-word stems ("layouts" = "layout"). The brain is found by brainpath.py and only read.
No brain on this machine: prints nothing, exit 0 (the toolkit runs without it).

  brainnotes.py "query text" [-k 3] [--brain DIR] [--json]    top notes: score, path under the brain, title
  brainnotes.py --eval gold.tsv [-k 3] [--brain DIR]           hit@k against a labelled set (id, slugs, why; slugs
                                                               comma-separated paths without .md, or NONE); the queries
                                                               come from a second file column 'text' or --queries FILE
"""
import argparse, json, math, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
STOP = set("a an the and or of to in on for with is are be by it its at as from this that what which how should we our "
           "not no do does after before into out than then when would must can there their them one two new old".split())


def stem(w):
    for suf in ("ies", "es", "s"):
        if len(w) > 4 and w.endswith(suf):
            return w[: -len(suf)] + ("y" if suf == "ies" else "")
    return w


def words(t):
    return [stem(w) for w in re.findall(r"[a-z0-9_]+", (t or "").lower()) if w not in STOP and len(w) > 1]


def load(brain):
    notes = []
    for root, _, files in os.walk(os.path.join(brain, "internal")):
        for f in files:
            if not f.endswith(".md") or f in ("INDEX.md", "INTERNAL-ONLY.md"):
                continue
            p = os.path.join(root, f)
            t = open(p, encoding="utf-8", errors="replace").read()
            fm, body = "", t
            if t.startswith("---"):
                j = t.find("\n---", 3)
                fm, body = t[3:j], t[j + 4:]
            title = (re.search(r"^title:\s*(.+)$", fm, re.M) or [None, ""])[1].strip("'\" ")
            kw = (re.search(r"^keywords:\s*(.+)$", fm, re.M) or [None, ""])[1]
            notes.append({"path": os.path.relpath(p, os.path.join(brain, "internal"))[:-3], "title": title,
                          "f": (set(words(title)), set(words(kw)), words(body))})
    return notes


def search(notes, q, k=3):
    qs = set(words(q))
    n = len(notes) or 1
    df = {w: sum(1 for x in notes if w in x["f"][0] or w in x["f"][1] or w in x["f"][2]) for w in qs}
    out = []
    for x in notes:
        t, kw, body = x["f"]
        bset = set(body)
        s = sum(math.log(1 + n / (1 + df[w])) * (3 * (w in t) + 2 * (w in kw) + (w in bset)) for w in qs)
        if s > 0:
            out.append((round(s, 1), x["path"], x["title"]))
    return sorted(out, key=lambda r: -r[0])[:k]


def brain_dir(arg):
    if arg:
        return arg
    try:
        import brainpath
        return brainpath.find()[0]
    except Exception:
        return None


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("query", nargs="?")
    ap.add_argument("-k", type=int, default=3)
    ap.add_argument("--brain"); ap.add_argument("--json", action="store_true")
    ap.add_argument("--eval"); ap.add_argument("--queries")
    a = ap.parse_args()
    b = brain_dir(a.brain)
    if not b or not os.path.isdir(os.path.join(b, "internal")):
        return 0
    notes = load(b)
    if not a.eval:
        r = search(notes, a.query or "", a.k)
        print(json.dumps([{"score": s, "path": p, "title": t} for s, p, t in r]) if a.json
              else "\n".join(f"{s}\t{p}\t{t}" for s, p, t in r))
        return 0
    q = {}
    if a.queries:
        for ln in open(a.queries):
            if "|" in ln:
                i, t = ln.split("|", 1)
                q[i.strip()] = t.strip()
    hit = tot = none_ok = nones = 0
    for ln in open(a.eval):
        f = ln.rstrip("\n").split("\t")
        if len(f) < 2 or f[0] in ("id", "") or f[0] not in q:
            continue
        gold = {g.strip() for g in f[1].split(",") if g.strip() and g.strip() != "NONE"}
        got = search(notes, q[f[0]], a.k)
        paths = [p for _, p, _ in got]
        if not gold:
            nones += 1
            print(f"{f[0]}\tNONE\t(top: {paths[:1]})")
            continue
        tot += 1
        ok = bool(gold & set(paths))
        hit += ok
        print(f"{f[0]}\t{'HIT ' if ok else 'MISS'}\tgold {sorted(gold)}\tgot {paths}")
    print(f"brainnotes hit@{a.k}: {hit}/{tot} situations with a gold note ({nones} with none in the brain)")
    return 0 if tot and hit == tot else 1


if __name__ == "__main__":
    sys.exit(main())
