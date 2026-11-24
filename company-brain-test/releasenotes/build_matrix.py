#!/usr/bin/env python3
"""Turn sp-changes.jsonl and module-changes.jsonl into reviewable markdown tables (no model involved).

Usage:  python3 build_matrix.py [--out ./matrix]

Writes:
  matrix/studio-pro-upgrade-<major>.md   breaking / removal / requirement / deprecation / known-issue rows per patch, newest first
  matrix/modules-compat.md               per Platform module: version -> min Mendix -> published, plus upgrade-relevant notes
  matrix/modules-index.md                one line per module with latest version, min Mendix, number of breaking rows (links to modules/)
  matrix/modules/<slug>.md               one file per module: the same section as in modules-compat.md
  matrix/SUMMARY.md                      counts
"""
import argparse, json, re
from collections import defaultdict, Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
UPG = ("breaking", "removal", "requirement", "deprecation", "known-issue", "migration-step")


def vkey(v):
    return tuple(int(x) if x.isdigit() else 0 for x in re.findall(r"\d+|[a-z]+", str(v or "")))


def load(p):
    return [json.loads(l) for l in p.read_text().splitlines() if l.strip()] if p.exists() else []


def esc(s):
    return str(s or "").replace("|", "\\|").replace("\n", " ")


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", str(s).lower()).strip("-")


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--out", default=str(HERE / "matrix")); a = ap.parse_args()
    out = Path(a.out); out.mkdir(exist_ok=True)
    (out / "modules").mkdir(exist_ok=True)
    for old in (out / "modules").glob("*.md"): old.unlink()
    sp = load(HERE / "sp-changes.jsonl"); mods = load(HERE / "module-changes.jsonl")
    summary = [f"# Version knowledge matrix\n", f"Studio Pro change records: {len(sp)}  |  module records: {len(mods)}\n"]
    # --- Studio Pro
    by_major = defaultdict(list)
    for r in sp:
        if r["change_type"] in UPG or r.get("upgrade_relevant"):
            by_major[r["version"].split(".")[0]].append(r)
    for mj, rows in sorted(by_major.items()):
        rows.sort(key=lambda r: (vkey(r["version"]), r["change_type"]), reverse=True)
        lines = [f"# Studio Pro {mj}: what an upgrader must know\n",
                 f"Source: docs.mendix.com release notes, extracted by Haiku, layer baseline. {len(rows)} rows.\n",
                 "| version | date | type | area | change | affected | source |", "|---|---|---|---|---|---|---|"]
        for r in rows:
            lines.append(f"| {r['version']} | {esc(r.get('release_date'))} | {r['change_type']} | {r['area']} | {esc(r['text'])} | {esc(', '.join(r.get('affected') or []))} | [notes]({r['source']}) |")
        (out / f"studio-pro-upgrade-{mj}.md").write_text("\n".join(lines) + "\n")
        c = Counter(r["change_type"] for r in rows)
        summary.append(f"- Studio Pro {mj}: {len(rows)} upgrade rows ({', '.join(f'{k} {v}' for k, v in c.most_common())})")
    # --- modules
    per = defaultdict(lambda: {"versions": {}, "changes": []})
    for r in mods:
        m = per[(r["content_id"], r["module"])]
        if r["record"] == "version":
            m["versions"][r["version"]] = r
            m.update({k: r.get(k) for k in ("publisher", "type", "support")})
        elif r["change_type"] in UPG or r.get("upgrade_relevant"):
            m["changes"].append(r)
    idx = ["# Marketplace modules: index\n", "| module | type | support | latest | min Mendix (latest) | versions | upgrade rows |", "|---|---|---|---|---|---|---|"]
    compat = ["# Marketplace modules: compatibility and upgrade notes\n", "Source: marketplace-api.mendix.com per-version release notes, layer baseline.\n"]
    used = set()
    for (cid, name), m in sorted(per.items(), key=lambda kv: kv[0][1].lower()):
        vers = sorted(m["versions"].values(), key=lambda v: vkey(v["version"]), reverse=True)
        if not vers: continue
        fn = slug(name) if slug(name) not in used else f"{slug(name)}-{cid}"
        used.add(fn)
        latest = vers[0]
        idx.append(f"| [{esc(name)}](modules/{fn}.md) | {m.get('type')} | {m.get('support')} | {latest['version']} | {latest.get('min_mendix') or '?'} | {len(vers)} | {len(m['changes'])} |")
        body = [f"{m.get('type')}, {m.get('publisher')}, {m.get('support')}, [marketplace](https://marketplace.mendix.com/link/component/{cid})\n",
                "| version | published | min Mendix |", "|---|---|---|"]
        body += [f"| {v['version']} | {v.get('published')} | {v.get('min_mendix') or '?'} |" for v in vers[:40]]
        if len(vers) > 40: body.append(f"| … {len(vers)-40} older versions | | |")
        if m["changes"]:
            body += ["", "| version | type | change | affected | replaced by |", "|---|---|---|---|---|"]
            for r in sorted(m["changes"], key=lambda r: vkey(r["version"]), reverse=True):
                body.append(f"| {r['version']} | {r['change_type']} | {esc(r['text'])} | {esc(', '.join(r.get('affected') or []))} | {esc(r.get('replaced_by') or '')} |")
        compat += [f"\n## {esc(name)} <a id=\"{cid}\"></a>"] + body
        (out / "modules" / f"{fn}.md").write_text("\n".join(
            [f"# {name} (Marketplace component {cid})\n", "Source: marketplace-api.mendix.com per-version release notes, layer baseline. "
             "Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.\n"] + body) + "\n")
    (out / "modules-index.md").write_text("\n".join(idx) + "\n")
    (out / "modules-compat.md").write_text("\n".join(compat) + "\n")
    summary.append(f"- Modules: {len(per)} items, {sum(len(m['versions']) for m in per.values())} versions, {sum(len(m['changes']) for m in per.values())} upgrade rows")
    (out / "SUMMARY.md").write_text("\n".join(summary) + "\n")
    print("\n".join(summary))


if __name__ == "__main__":
    main()
