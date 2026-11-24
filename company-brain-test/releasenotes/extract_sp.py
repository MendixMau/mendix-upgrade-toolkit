#!/usr/bin/env python3
"""Extract structured change records from the Studio Pro release notes in the docs clone (Claude Haiku 4.5).

Usage:
  extract_sp.py [--majors 9,10,11] [--docs ../mendix-docs] [--out ./sp-changes.jsonl] [--workers 10] [--max N] [--force]

Unit of work = one patch section ("## 10.24.22 {#102422}") of one minor release-notes page.
Output: one JSON line per change item: version, release_date, section, change_type, upgrade_relevant, area, affected,
text, tickets, source (docs path + anchor). Known issues also carry fixed_in when the notes say so.
"""
import argparse, json, re, sys, time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import anthropic

MODEL = "claude-haiku-4-5-20251001"
CHANGE_TYPES = ["breaking", "deprecation", "removal", "requirement", "known-issue", "fix", "improvement", "feature", "security"]
AREAS = ["studio-pro-ide", "runtime", "client-web", "client-react", "native-mobile", "workflow", "data-storage", "odata-rest",
         "java-actions", "pluggable-widgets", "atlas-theming", "security", "deployment-cloud", "git-teamserver", "mxbuild-cli",
         "maia-ai", "external-entities", "performance", "other"]

SYSTEM = f"""You turn one patch section of the Mendix Studio Pro release notes into structured change records.
For EVERY bullet in the section produce one record. Do not skip bullets, do not merge them, do not invent any.

Each record is a JSON object:
- change_type: one of {CHANGE_TYPES}. Use the section heading as the primary signal (Breaking Changes -> breaking, Deprecations -> deprecation, Known Issues -> known-issue, Fixes -> fix, Improvements/New Features -> improvement/feature). Override only when a bullet in Improvements/Fixes clearly removes support, raises a minimum (Java, .NET, Node, OS, browser, database, module version), or ends support: then use removal or requirement.
- upgrade_relevant: true if someone upgrading an app across this version must know it (anything breaking, deprecation, removal, requirement, known-issue, behavior change, migration, "no longer", "now requires", version bumps of Java/.NET/Node/databases, module or widget compatibility). false for ordinary fixes and features.
- area: one of {AREAS}
- affected: list of concrete names touched (modules, widgets, Java APIs, settings, activities, entities, languages, databases, OS). Empty if none.
- text: the bullet rewritten in at most 40 words, keeping every version number, setting name and error string verbatim.
- tickets: list of ticket numbers mentioned (strings), empty if none.
- fixed_in: version string if the bullet says the issue is fixed in a later version, else null.

Return ONLY a JSON array of records, no prose, no code fence."""


def sections(path):
    text = path.read_text()
    fm = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    lts = bool(fm and re.search(r"^lts:\s*true", fm.group(1), re.M))
    mts = bool(fm and re.search(r"^mts:\s*true", fm.group(1), re.M))
    url = re.search(r"^url:\s*(\S+)", fm.group(1), re.M).group(1) if fm else ""
    parts = []
    for p in re.split(r"^(?=## \d+\.\d+\.\d+)", text, flags=re.M):
        # the docs sometimes repeat a patch heading ("## 11.15.0 {#11150}" + date, then "## 11.15.0" + content): one section
        v = re.match(r"## (\d+\.\d+\.\d+)", p)
        pv = parts and re.match(r"## (\d+\.\d+\.\d+)", parts[-1])
        if v and pv and v.group(1) == pv.group(1):
            parts[-1] += "\n" + p.split("\n", 1)[-1]
        else:
            parts.append(p)
    for p in parts:
        m = re.match(r"## (\d+\.\d+\.\d+)[^{\n]*(?:\{#([^}]+)\})?", p)
        if not m:
            continue
        date = re.search(r"\*\*Release date:\s*([^*]+)\*\*", p)
        body = re.sub(r"\{\{%.*?%\}\}", "", p, flags=re.S)  # drop hugo shortcodes (buttons, alerts wrappers keep inner text)
        yield {"version": m.group(1), "anchor": m.group(2) or "", "release_date": date.group(1).strip() if date else "",
               "lts": lts, "mts": mts, "url": url, "body": body.strip()}


CHUNK = 9000  # chars per model call; long sections are split on ### headings so the JSON array stays small


def chunks(body):
    if len(body) <= CHUNK:
        return [body]
    head, *subs = re.split(r"^(?=### )", body, flags=re.M)
    out, cur = [], head
    for s in subs:
        if len(cur) + len(s) > CHUNK and cur.strip():
            out.append(cur); cur = head.split("\n")[0] + "\n\n"
        cur += s
    if cur.strip(): out.append(cur)
    return out


def parse_items(text):
    m = re.search(r"\[.*\]", text, re.S)
    try:
        return json.loads(m.group(0) if m else text)
    except json.JSONDecodeError:  # salvage the well-formed objects
        return [json.loads(o) for o in re.findall(r"\{(?:[^{}]|\{[^{}]*\})*\}", text) if '"text"' in o]


def extract(client, sec):
    if not re.search(r"^\s*[*-] ", sec["body"], re.M):
        return []  # a header-only section (release without bullets)
    items, ti, to = [], 0, 0
    for ch in chunks(sec["body"]):
        resp = client.messages.create(model=MODEL, max_tokens=12000, system=SYSTEM,
                                      messages=[{"role": "user", "content": f"Version {sec['version']} ({sec['release_date']})\n\n{ch}"}])
        text = next(b.text for b in resp.content if b.type == "text")
        items += parse_items(text); ti += resp.usage.input_tokens; to += resp.usage.output_tokens
        if resp.stop_reason == "max_tokens":
            print(f"  WARN {sec['version']}: output truncated at max_tokens", file=sys.stderr)
    out, seen = [], set()
    for it in items:
        if not isinstance(it, dict) or "text" not in it or (it.get("change_type"), it["text"]) in seen:
            continue
        seen.add((it.get("change_type"), it["text"]))
        if not isinstance(it, dict) or "text" not in it:
            continue
        it["change_type"] = it.get("change_type") if it.get("change_type") in CHANGE_TYPES else "improvement"
        it["area"] = it.get("area") if it.get("area") in AREAS else "other"
        it.update({"version": sec["version"], "release_date": sec["release_date"], "lts": sec["lts"], "mts": sec["mts"],
                   "source": f"https://docs.mendix.com{sec['url']}#{sec['anchor']}", "model": MODEL})
        out.append(it)
    return out, ti, to


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--majors", default="9,10,11")
    ap.add_argument("--docs", default=str(Path(__file__).resolve().parent.parent / "mendix-docs"))
    ap.add_argument("--out", default=str(Path(__file__).resolve().parent / "sp-changes.jsonl"))
    ap.add_argument("--workers", type=int, default=10)
    ap.add_argument("--max", type=int, default=0)
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()
    root = Path(a.docs) / "content/en/docs/releasenotes/studio-pro"
    secs = [s for mj in a.majors.split(",") for f in sorted((root / mj.strip()).glob("*.md")) if f.name != "_index.md" for s in sections(f)]
    out_f = Path(a.out)
    done = set()
    if out_f.exists() and not a.force:
        done = {json.loads(l)["version"] for l in out_f.read_text().splitlines() if l.strip()}
    todo = [s for s in secs if s["version"] not in done]
    if a.max: todo = todo[:a.max]
    print(f"{len(secs)} patch sections, {len(todo)} to do", flush=True)
    client = anthropic.Anthropic(max_retries=5)
    t0, n_items, n_err, toks = time.time(), 0, 0, [0, 0]
    with out_f.open("w" if a.force else "a") as fh, ThreadPoolExecutor(max_workers=a.workers) as ex:
        futs = {ex.submit(extract, client, s): s for s in todo}
        for i, fut in enumerate(as_completed(futs), 1):
            s = futs[fut]
            try:
                r = fut.result()
            except Exception as e:
                n_err += 1; print(f"  ERR {s['version']}: {type(e).__name__}: {str(e)[:160]}", file=sys.stderr); continue
            if not r:
                continue
            items, ti, to = r
            for it in items: fh.write(json.dumps(it, ensure_ascii=False) + "\n")
            fh.flush(); n_items += len(items); toks[0] += ti; toks[1] += to
            if i % 25 == 0: print(f"  {i}/{len(todo)} sections, {n_items} items, {time.time()-t0:.0f}s", flush=True)
    print(f"done: {n_items} items, {n_err} errors, {toks[0]/1000:.0f}k in / {toks[1]/1000:.0f}k out, ~${toks[0]/1e6+toks[1]/1e6*5:.2f}, {time.time()-t0:.0f}s -> {out_f}")


if __name__ == "__main__":
    main()
