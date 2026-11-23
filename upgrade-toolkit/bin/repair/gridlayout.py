#!/usr/bin/env python3
"""gridlayout.py: remove an app theme rule that breaks the Data grid 2 layout after a Data Widgets update.

Why (cold 9.24 -> 10.24 run): DataWidgets 2.7.2 -> 3.11.8. The app's own theme module carried a rule written for the
old grid markup, `.widget-datagrid .table { display: block !important; }`. On Data Widgets 2 `.table` was the outer
wrapper and the CSS grid sat on `.table-content`, so the rule was harmless. Data Widgets 3 makes `.table` itself the
grid (`.widget-datagrid-grid.table { display: grid !important; grid-template-columns: ... }`); same specificity, and the
app module compiles after datawidgets, so the old rule wins: every cell of every Data grid 2 renders as its own full-width
row, the header filters stack, the pager falls below the fold. Build, mx check, smoke walk and journeys all pass (the data
is on the page); only the screens rung sees it, as a REVIEW with no cause. keptstyle.py and theme_clash.py do not catch
it (the module is not kept, the class still exists).

  gridlayout.py <app dir> [--check] [--causes FILE]

1. Reads the installed Data Widgets theme (themesource/datawidgets*/web/*.scss). Applies only when it lays out `.table`
   itself as a grid (a rule with "display: grid" whose selector ends on a compound with class .table). When it does not
   (Data Widgets 2: the grid is on .table-content), prints "not applicable" and exits 0.
2. Scans every other *.scss / *.css under theme/ and themesource/<module>/ (Atlas Core and Atlas Web Content are the
   reference and are skipped) for a rule on a Data grid 2 `.table` (selector with .widget-datagrid, .widget-datagrid-grid
   or mx-name-dataGrid, last compound has class .table) that sets display to a non-grid layout value (block, flex,
   inline-block, inline-flex, table, inline, flow-root). display: none (hiding on purpose), grid and contents are left.
3. Writes by default: that one declaration is commented out in place, with a short note; nothing else in the file
   changes. --check only reports.

Output: one "CLASH <file>:<line> <selector> { display: <value> }" line per hit (FIXED instead of CLASH when written), then
"gridlayout: N rule(s) ..." and, when there were hits, the one-line explanation for the person ("SAY ...").
--causes FILE: (re)writes this tool's line in FILE ("* # <explanation>"), the screen-cause file shotdiff.py --causes
reads, so a screens REVIEW of a page with changed layout points at this cause; other lines in FILE are kept. With no hits
FILE is left as it is: a line from an earlier run of the same rung (the repair already committed) stays.
Selectors are resolved through SCSS nesting (&, &-suffix, @media/@include blocks, @at-root, #{$var} of a string variable
set in the same file). LIMITS: a partial @import-ed inside a selector block is read on its own (its outer selector is not
known); mixins are not expanded.
Exit: 0 = nothing to fix, not applicable, or all fixed; 1 = hits (--check); 2 = input error.
"""
import argparse, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from theme_clash import scss_code  # noqa: E402  (same-length copy with comments and strings blanked)

TAG = "[gridlayout]"
REFERENCE = ("atlas_core", "atlas_web_content")
SKIP_DIRS = {".git", "node_modules", "public", "native", "deployment", ".mendix-cache"}
BAD = {"block", "flex", "inline-block", "inline-flex", "table", "inline", "flow-root", "inline-table"}
TABLE = re.compile(r"\.table(?![\w-])")
GRID_OWNER = re.compile(r"\.widget-datagrid(?![\w-])|\.widget-datagrid-grid(?![\w-])|mx-name-dataGrid", re.I)
STRVAR = re.compile(r"""^\s*\$([\w-]+)\s*:\s*(["'])([^"'\n]*)\2\s*(?:!default\s*)?;""", re.M)
COMMENT = re.compile(r"/\*.*?\*/|//[^\n]*", re.S)
DISPLAY = re.compile(r"^\s*display\s*:\s*([^;{}]+?)\s*$", re.S)


def split_top(s, seps=","):
    """Split on any char in seps outside parentheses/brackets."""
    out, depth, cur = [], 0, []
    for ch in s:
        if ch in "([":
            depth += 1
        elif ch in ")]":
            depth = max(0, depth - 1)
        if ch in seps and depth == 0:
            out.append("".join(cur)); cur = []
        else:
            cur.append(ch)
    out.append("".join(cur))
    return [x.strip() for x in out if x.strip()]


def last_compound(sel):
    parts = split_top(sel, " \t\n>+~")
    return parts[-1] if parts else ""


def resolve(parents, prelude):
    """Resolved selector list of a rule nested under parents (a list; [] at the root)."""
    out = []
    for s in split_top(prelude):
        if not parents:
            out.append(s.replace("&", "").strip())
        elif "&" in s:
            out += [s.replace("&", p) for p in parents]
        else:
            out += [p + " " + s for p in parents]
    return out


def rules(text):
    """Yield (selectors, value, start, end) for every display declaration; start/end are offsets in text."""
    code = scss_code(text)
    svars = {m.group(1): m.group(3) for m in STRVAR.finditer(text)}
    stack, cur = [], []          # stack of parent selector lists
    i, n, stmt = 0, len(code), 0

    def decl(a, b):
        seg = code[a:b]
        m = DISPLAY.match(seg)
        if m and cur:
            lead = len(seg) - len(seg.lstrip())
            return (list(cur), m.group(1).strip(), a + lead, b)
        return None

    while i < n:
        c = code[i]
        if code.startswith("#{", i):
            j = code.find("}", i)
            i = n if j < 0 else j + 1
            continue
        if c == "{":
            pre = COMMENT.sub(" ", text[stmt:i]).strip()    # raw text: selector strings ([class^="..."]) kept
            pre = re.sub(r"#\{\s*\$([\w-]+)\s*\}", lambda m: svars.get(m.group(1), m.group(0)), pre)
            stack.append(cur)
            if pre.startswith("@at-root"):
                rest = pre[len("@at-root"):].strip()
                cur = resolve([], rest) if rest else []
            elif pre.startswith("@"):
                cur = cur                                   # @media, @include ... { }, @if: same selectors
            else:
                cur = resolve(cur, pre)
            stmt = i + 1
        elif c in ";}":
            d = decl(stmt, i)
            if d:
                yield d[0], d[1], d[2], (i + 1 if c == ";" else i)
            if c == "}":
                cur = stack.pop() if stack else []
            stmt = i + 1
        i += 1


def files(root):
    for d, dirs, fs in os.walk(root):
        dirs[:] = sorted(x for x in dirs if x not in SKIP_DIRS)
        for f in sorted(fs):
            if f.endswith((".scss", ".css")):
                yield os.path.join(d, f)


def read(p):
    try:
        return open(p, encoding="utf8", errors="replace", newline="").read()   # CRLF kept
    except OSError:
        return None


def table_is_grid(app):
    """The installed Data Widgets theme puts display: grid on .table itself (Data Widgets 3 markup)."""
    ts = os.path.join(app, "themesource")
    for mod in sorted(os.listdir(ts)) if os.path.isdir(ts) else []:
        if not mod.lower().startswith("datawidgets"):
            continue
        for p in files(os.path.join(ts, mod)):
            t = read(p) or ""
            for sels, val, _, _ in rules(t):
                if val.split()[0].lower() in ("grid", "inline-grid") and any(TABLE.search(last_compound(s)) for s in sels):
                    return os.path.relpath(p, app)
    return None


def scan_roots(app):
    yield os.path.join(app, "theme")
    ts = os.path.join(app, "themesource")
    for mod in sorted(os.listdir(ts)) if os.path.isdir(ts) else []:
        if mod.lower() in REFERENCE or mod.lower().startswith("datawidgets"):
            continue
        yield os.path.join(ts, mod)


def clashes(text):
    for sels, val, a, b in rules(text):
        word = val.replace("!important", "").strip().lower()
        if word not in BAD:
            continue
        hit = [s for s in sels if TABLE.search(last_compound(s)) and GRID_OWNER.search(s)]
        if hit:
            hit.sort(key=lambda s: "widget-datagrid" not in s)    # name the widget class first
            yield hit[0], val, a, b


def write_causes(path, say):
    keep = []
    try:
        keep = [ln for ln in open(path).read().splitlines() if TAG not in ln]
    except OSError:
        pass
    with open(path, "w") as fh:
        fh.write("\n".join(keep + [f"* # {say} {TAG}"]) + "\n")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("app")
    ap.add_argument("--check", action="store_true", help="report only, write nothing")
    ap.add_argument("--causes", help="screen-cause file for shotdiff.py --causes")
    a = ap.parse_args()
    if not os.path.isdir(os.path.join(a.app, "themesource")) and not os.path.isdir(os.path.join(a.app, "theme")):
        print(f"gridlayout: {a.app}: no theme/ or themesource/ folder", file=sys.stderr); sys.exit(2)
    ref = table_is_grid(a.app)
    if not ref:
        print("gridlayout: not applicable: the installed Data Widgets theme does not lay out .table as the grid")
        sys.exit(0)
    hits = []
    for root in scan_roots(a.app):
        for p in files(root):
            t = read(p)
            if t is None:
                continue
            found = list(clashes(t))
            if not found:
                continue
            rel = os.path.relpath(p, a.app)
            new = t
            for sel, val, s, e in reversed(found):
                old = t[s:e]
                new = new[:s] + f"/* {old.strip()}  -- removed by the upgrade toolkit (repair/gridlayout.py): Data " \
                                f"Widgets 3 lays out .table as the grid itself */" + new[e:]
            for sel, val, s, e in found:
                hits.append((rel, t.count("\n", 0, s) + 1, " ".join(sel.split()), val))
            if not a.check:
                with open(p, "w", encoding="utf8", newline="") as fh:
                    fh.write(new)
    word = "CLASH" if a.check else "FIXED"
    for rel, ln, sel, val in hits:
        print(f"{word} {rel}:{ln} {sel} {{ display: {val} }}")
    where = ", ".join(f"{r}:{l}" for r, l, _, _ in hits[:3]) + (f" (+{len(hits) - 3} more)" if len(hits) > 3 else "")
    say = ""
    if hits and a.check:
        say = (f"Data grid 2 pages show every cell as its own row: an app theme rule written for the old grid ({where}, "
               f"display on .table) overrides the Data Widgets 3 grid layout; fix: python3 bin/repair/gridlayout.py "
               f"<app> comments it out, then build again")
    elif hits:
        say = (f"Data grid 2 pages showed every cell as its own row: an app theme rule written for the old grid ({where}, "
               f"display on .table) overrode the Data Widgets 3 grid layout; the toolkit commented it out "
               f"(commit 'repair: data grid 2 layout'): check one grid page and OK it")
    print(f"gridlayout: {len(hits)} rule(s) override the Data grid 2 layout (reference: {ref})"
          + ("" if hits else ": nothing to do") + ("" if a.check or not hits else ", commented out"))
    if say:
        print("SAY " + say)
    if a.causes and say:
        write_causes(a.causes, say)
    sys.exit(1 if hits and a.check else 0)


if __name__ == "__main__":
    main()
