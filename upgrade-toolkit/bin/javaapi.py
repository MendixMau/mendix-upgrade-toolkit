#!/usr/bin/env python3
"""javaapi.py: every call of a removed or changed Mendix runtime Java API in the app's Java, with its replacement call.

Why: replacement_check.py rows R18 (runtime Java API removals, 10 and 11) and R30 (changedDate / changedBy read in logic) say
HIT with a file count only, so the proposal asked a person to OK "Runtime Java API removals" with no fix in it (cold run,
9.24 -> 10.24 -> 11.12: every R18 hit was Marketplace module Java that the module updates replaced, and on rung 2 the only
"hit" was MendixSSO's com.mendix.m2ee.api.IMxRuntimeRequest import, which compiles on 11.12.7). This reads the Java line by
line against playbooks/java-api.tsv and names, per call site, the removed API, the replacement call, the effort and the
release note row; a 1:1 rewrite is marked mechanical and can be applied by the toolkit itself.

  javaapi.py <app dir | javasource dir> [--table playbooks/java-api.tsv] [--md out.md] [--json out.json]
  javaapi.py <app dir> --rewrite                     dry run: the unified diff of the mechanical rewrites, nothing written
  javaapi.py <app dir> --rewrite --apply [--commit]  write them; --commit makes them one commit of their own in the app repo
                                                     (Changed-By: toolkit, Upgrade-Change: repair java-api-rewrite)

Read: javasource/**/*.java, proxies/ excluded, comments blanked (strings kept, so line numbers and offsets stay). Every row of
the table (R18, R30) is reported: "HIT" with its call sites, or "checked: not used in this app" when no call site matched.
A rewrite is applied only where the whole call matches the entry's pattern on the original text and its guard holds; any
other call site stays for a person (the line says "by hand").
Exit: scan 0 = no call site, 1 = call sites (listed); --rewrite 0 = nothing to rewrite, 1 = a diff (dry run) or files
written (--apply); 2 = no javasource folder, a bad table or a failed commit.
"""
import argparse, difflib, json, os, re, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEFAULT_TABLE = HERE.parent / "playbooks" / "java-api.tsv"
COLS = ["id", "row", "find", "removed", "replacement", "rewrite", "guard", "kind", "effort", "source"]
STR = r'"(?:[^"\\\n]|\\.)*"'
ARG = rf'(?:[^,()"\n]|{STR}|\((?:[^()"\n]|{STR})*\))+?'   # one argument: no top-level comma, one level of parentheses
ACTION = re.compile(r"\bextends\s+(?:CustomJavaAction|UserAction)\b")
OWN_CONTEXT = re.compile(r"\bcontext\s*\(\s*\)\s*(?:throws\s+[\w.,\s]+)?\{")


def read_table(path):
    rows = []
    with open(path, encoding="utf-8") as f:
        header = None
        for n, line in enumerate(f, 1):
            line = line.rstrip("\n")
            if not line.strip() or line.startswith("#"):
                continue
            cells = line.split("\t")
            if header is None:
                if cells != COLS:
                    raise ValueError(f"{path}:{n}: header is not {' '.join(COLS)}")
                header = cells
                continue
            if len(cells) != len(COLS):
                raise ValueError(f"{path}:{n}: {len(cells)} fields, want {len(COLS)}")
            r = dict(zip(COLS, cells))
            try:
                r["rx"] = re.compile(r["find"].replace("{ARG}", ARG))
            except re.error as e:
                raise ValueError(f"{path}:{n} {r['id']}: bad find regex: {e}")
            rows.append(r)
    if header is None:
        raise ValueError(f"{path}: no header")
    return rows


def blank_comments(s):
    """Comments as spaces (newlines kept): offsets and line numbers stay those of the original text."""
    out, i, n = [], 0, len(s)
    while i < n:
        c = s[i]
        if c == '"' or c == "'":
            j = i + 1
            while j < n and s[j] != c and s[j] != "\n":
                j += 2 if s[j] == "\\" else 1
            out.append(s[i:j + 1]); i = j + 1
        elif s.startswith("//", i):
            j = s.find("\n", i); j = n if j < 0 else j
            out.append(" " * (j - i)); i = j
        elif s.startswith("/*", i):
            j = s.find("*/", i + 2); j = n if j < 0 else j + 2
            out.append(re.sub(r"[^\n]", " ", s[i:j])); i = j
        else:
            out.append(c); i += 1
    return "".join(out)


def java_files(root):
    """{posix path from the app (javasource/...): text}, proxies excluded; None without a javasource folder."""
    root = Path(root)
    js = root if root.name == "javasource" else root / "javasource"
    if not js.is_dir():
        return None
    out = {}
    for f in sorted(js.rglob("*.java")):
        rel = f.relative_to(js)
        if "proxies" in rel.parts:
            continue
        out[f"javasource/{rel.as_posix()}"] = f.read_text(encoding="utf-8", errors="replace")
    return out


def split_args(argtext):
    """Top-level arguments of a call's argument text."""
    args, depth, cur, i = [], 0, "", 0
    while i < len(argtext):
        c = argtext[i]
        if c == '"':
            m = re.match(STR, argtext[i:])
            cur += m.group(0) if m else c; i += len(m.group(0)) if m else 1
            continue
        if c == "(":
            depth += 1
        elif c == ")":
            depth -= 1
        if c == "," and depth == 0:
            args.append(cur.strip()); cur = ""
        else:
            cur += c
        i += 1
    return args + [cur.strip()]


def string_arg(a, text):
    if re.fullmatch(STR, a) or re.fullmatch(r"[\w.]+\.entityName", a) or re.fullmatch(r"[\w.]+\.getType\(\)", a):
        return True
    return bool(re.fullmatch(r"\w+", a) and re.search(rf"\bString\s+{a}\s*[=;,)]", text))


def guard_ok(r, text, m):
    g = r["guard"]
    if g in ("", "-"):
        return True
    if g == "action":
        return bool(ACTION.search(text)) and not OWN_CONTEXT.search(text)
    if g == "string-args":
        return all(string_arg(a, text) for a in m.groups() if a is not None)
    return False


def scan(files, rows):
    """Call sites: [{row, id, file, line, module, code, removed, replacement, effort, kind, source, mechanical, span}]."""
    hits = []
    for rel, text in files.items():
        clean = blank_comments(text)
        taken = set()
        for r in rows:
            if r["guard"] == "action" and not guard_ok(r, text, None):
                continue  # context() outside a Java action, or a class with its own context(): not the removed API
            for m in r["rx"].finditer(clean):
                if m.start() in taken:
                    continue
                taken.add(m.start())
                line = clean.count("\n", 0, m.start()) + 1
                mech = False
                if r["rewrite"] not in ("", "-"):
                    om = r["rx"].fullmatch(text, m.start(), m.end())  # the original text, comments included, must match too
                    mech = bool(om) and guard_ok(r, text, om)
                hits.append({"row": r["row"], "id": r["id"], "file": rel, "line": line,
                             "module": rel.split("/")[1] if rel.count("/") > 1 else "",
                             "code": text.splitlines()[line - 1].strip()[:160], "removed": r["removed"],
                             "replacement": r["replacement"], "effort": r["effort"], "kind": r["kind"], "source": r["source"],
                             "mechanical": mech, "span": [m.start(), m.end()]})
    return sorted(hits, key=lambda h: (h["row"], h["file"], h["line"], h["span"][0]))


def rewritten(rel, text, rows, passes=5):
    """The text with every mechanical hit rewritten. One pass rewrites from the end and skips a hit inside one it already
    rewrote (context() inside a retrieveXPathQuery call); the file is read again until nothing changes."""
    byid = {r["id"]: r for r in rows}
    for _ in range(passes):
        done, new = [], text
        for h in sorted((h for h in scan({rel: text}, rows) if h["mechanical"]), key=lambda h: -h["span"][0]):
            a, b = h["span"]
            if any(a < y and x < b for x, y in done):
                continue
            r = byid[h["id"]]
            new = new[:a] + r["rx"].sub(r["rewrite"], new[a:b], count=1) + new[b:]
            done.append((a, b))
        if new == text:
            break
        text = new
    return text


def report(files, rows, hits, path):
    ids = list(dict.fromkeys(r["row"] for r in rows))
    by = {i: [h for h in hits if h["row"] == i] for i in ids}
    nmech = sum(h["mechanical"] for h in hits)
    out = [f"javaapi: {path}: {len(files)} Java files read, {len(hits)} call sites ({nmech} mechanical rewrites), "
           + ", ".join(f"{i} {'HIT (' + str(len(by[i])) + ')' if by[i] else 'checked'}" for i in ids)]
    for i in ids:
        if not by[i]:
            out.append(f"checked {i}: not used in this app ({len(files)} Java files read, no call of a removed or changed API of this row)")
            continue
        for h in by[i]:
            out.append(f"HIT {i} {h['id']} {h['file']}:{h['line']} [{h['module']}] {h['removed']} -> {h['replacement']} "
                       f"[effort {h['effort']}, {'mechanical: the toolkit rewrites it' if h['mechanical'] else 'by hand'}] ({h['source']})")
            out.append(f"    code: {h['code']}")
    return out


def md(lines, hits, ids):
    L = ["# Java API check (javaapi.py)", "", lines[0], "",
         "| row | file:line | module | removed API | replacement | effort | rewrite | release note |", "|---|---|---|---|---|---|---|---|"]
    esc = lambda s: str(s).replace("|", "\\|")
    for h in hits:
        L.append(f"| {h['row']} | {h['file']}:{h['line']} | {h['module']} | {esc(h['removed'])} | {esc(h['replacement'])} | {h['effort']} | "
                 f"{'mechanical' if h['mechanical'] else 'by hand'} | {esc(h['source'])} |")
    L += [""] + [f"- {i}: checked: not used in this app" for i in ids if not any(h["row"] == i for h in hits)]
    return "\n".join(L) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("app", help="app folder (with javasource/) or the javasource folder")
    ap.add_argument("--table", default=str(DEFAULT_TABLE))
    ap.add_argument("--md"), ap.add_argument("--json")
    ap.add_argument("--rewrite", action="store_true", help="the mechanical rewrites: a dry-run diff unless --apply")
    ap.add_argument("--apply", action="store_true", help="with --rewrite: write the files")
    ap.add_argument("--commit", action="store_true", help="with --apply: one commit of its own in the app repo")
    a = ap.parse_args()
    if (a.apply and not a.rewrite) or (a.commit and not a.apply):
        print("javaapi: --apply needs --rewrite, --commit needs --apply")
        return 2
    try:
        rows = read_table(a.table)
    except (OSError, ValueError) as e:
        print(f"javaapi: cannot read the table: {e}")
        return 2
    files = java_files(a.app)
    if files is None:
        print(f"javaapi: no javasource folder in {a.app}")
        return 2
    hits = scan(files, rows)
    lines = report(files, rows, hits, a.app)
    ids = list(dict.fromkeys(r["row"] for r in rows))
    if a.md:
        Path(a.md).write_text(md(lines, hits, ids))
    if a.json:
        Path(a.json).write_text(json.dumps({"app": str(a.app), "files": len(files), "hits": hits,
                                            "rows": {i: {"status": "HIT" if any(h["row"] == i for h in hits) else "checked",
                                                         "say": None if any(h["row"] == i for h in hits) else "checked: not used in this app"}
                                                     for i in ids}}, indent=1))
    if not a.rewrite:
        print("\n".join(lines))
        return 1 if hits else 0
    base = Path(a.app).parent if Path(a.app).name == "javasource" else Path(a.app)
    changed = []
    for rel in sorted({h["file"] for h in hits if h["mechanical"]}):
        old = files[rel]
        new = rewritten(rel, old, rows)
        if new == old:
            continue
        changed.append(rel)
        sys.stdout.writelines(difflib.unified_diff(old.splitlines(True), new.splitlines(True), f"a/{rel}", f"b/{rel}"))
        if a.apply:
            with open(base / rel, "w", encoding="utf-8", newline="") as f:
                f.write(new)
    n = sum(h["mechanical"] for h in hits)
    left = len(hits) - n
    print(f"javaapi: {n} mechanical rewrites in {len(changed)} files ({'written' if a.apply else 'dry run, nothing written'}); "
          f"{left} call sites left by hand")
    if a.commit and changed:
        g = ["git", "-C", str(base)]
        msg = (f"repair: Java API rewrites ({n} call sites, javaapi.py)\n\n"
               + "\n".join(f"{h['file']}:{h['line']} {h['removed']} -> {h['replacement']}" for h in hits if h["mechanical"])
               + "\n\nChanged-By: toolkit\nUpgrade-Change: repair java-api-rewrite\n")
        try:
            subprocess.run(g + ["add", "--"] + changed, check=True)
            subprocess.run(g + ["commit", "-q", "-m", msg, "--"] + changed, check=True)
        except (OSError, subprocess.CalledProcessError) as e:
            print(f"javaapi: commit failed: {e}")
            return 2
        print(f"javaapi: committed {len(changed)} files as one change")
    return 1 if changed else 0


if __name__ == "__main__":
    sys.exit(main())
