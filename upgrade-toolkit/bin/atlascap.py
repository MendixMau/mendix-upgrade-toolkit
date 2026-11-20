#!/usr/bin/env python3
"""atlascap.py: hold a module back in the plan while another module is installed (GM-14: Atlas_Core under PDS).

  atlascap.py <localedits.json> <plan.txt> [--app <app dir or .mpr>] [--table playbooks/module-caps.tsv] [--write] [--out caps.md]
  exit 0 no cap applies, 1 at least one CAP, 2 unreadable input

Why (GM-14): an app with the PDS grid module (PlatformDesignSystem) went from Atlas_Core 3.19.0 to 3.22.0. Atlas 3.20+ uses
`@extend .col-<bp>-3`, which needs the PDS grid. mx check and idcheck passed; only the mxbuild theme compile failed. The rule
was prose, so the plan (versions picked from `mxcli marketplace versions`) never used it. It is DATA now, playbooks/module-caps.tsv,
and this tool reads it against the installed modules (localedits.json) and the plan (stepupdate format, "<content id> <version>
<Module>", targets last, a 4th installed-version field is ignored).

  CAP <Module> at <max> (plan has <v>): <row>   the plan line is above the cap
  NOTE <Module> ...                             the installed version is already above the cap: nothing is downgraded, keep it
  --write  rewrites the plan line to the cap (the old file is kept as plan.txt.orig); a line whose installed version already equals the cap
           becomes a comment. A row with status "check" prints "UNVERIFIED": read its why column before accepting the cap.
  CONFLICT  a cap on Atlas_Core meets WorkflowCommons 4.3+ (plan or installed), which needs Atlas 4 (playbooks/10-to-11.md, T7-25):
           exit 1, the owner decides, and --write leaves the plan alone.
  --app    also finds a trigger module that is internal to the app (localedits.json lists only Marketplace modules): a
           themesource/<module lower case> folder or an entity-holding module of the .mpr. Without it the all-clear line says
           internal modules were not checked.
Producer of the inputs: steps/triage.md item 3 (localedits.py --json) and the plan (item 2). Consumer: steps/triage.md item 4.
Still wanted (GM-14): a mxbuild theme compile after each theme-module step; this tool only stops the plan that causes it.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TABLE = os.path.join(HERE, "..", "playbooks", "module-caps.tsv")


def vkey(v):
    return tuple(int(x) for x in re.findall(r"\d+", v or ""))


def load_table(path=TABLE):
    rows = []
    for ln in open(path, encoding="utf-8").read().splitlines():
        if not ln.strip() or ln.startswith("#") or ln.startswith("id\t"):
            continue
        f = ln.split("\t")
        if len(f) >= 6:
            rows.append(dict(zip(("id", "when", "capped", "max", "status", "why", "source"), f + [""])))
    return rows


ATLAS4_NEEDERS = {"WorkflowCommons": "4.3"}  # module: first version that needs Atlas Core 4 (playbooks/10-to-11.md)


def internal_modules(app):
    """Module names found in the app itself: themesource folders and entity-holding modules of the .mpr."""
    import glob
    names = set()
    if not app:
        return names
    folder = app if os.path.isdir(app) else os.path.dirname(os.path.abspath(app))
    for d in glob.glob(os.path.join(folder, "themesource", "*")):
        names.add(os.path.basename(d).lower())
    try:
        sys.path.insert(0, HERE)
        import idcheck
        model, _ = idcheck.load(app)
        names.update(e["module"].lower() for e in model["entity"].values())
    except (Exception, SystemExit):
        pass
    return names


def run(installed, plan_lines, table, write=False, extra=()):
    """installed {name: version}; plan_lines raw lines. Returns (messages, new_lines, capped_count)."""
    msgs, out, n = [], [], 0
    have = set(installed) | {m for r in table for m in [r["when"]] if r["when"].lower() in set(extra)}
    planned = {}
    for raw in plan_lines:
        w = raw.split("#", 1)[0].split()
        if len(w) >= 3:
            planned[w[2]] = w[1]
    conflict = False
    for raw in plan_lines:
        w = raw.split("#", 1)[0].split()
        new = raw
        if len(w) >= 3:
            ver, mod = w[1], w[2]
            for r in table:
                if r["capped"] != mod or r["when"] not in have or not vkey(ver) > vkey(r["max"]):
                    continue
                inst = installed.get(mod)
                tag = f"[{r['id']}, {r['status'].upper() if r['status'] == 'check' else r['status']}" + \
                      (", UNVERIFIED boundary: playbooks/module-caps.tsv" if r["status"] == "check" else ", playbooks/module-caps.tsv") + "]"
                if inst and vkey(inst) > vkey(r["max"]):
                    msgs.append(f"NOTE {mod} {inst} is installed above the cap {r['max']} ({r['when']} is installed too): not a downgrade, keep it and test the theme compile {tag}")
                    break
                n += 1
                for nm, first in ATLAS4_NEEDERS.items():
                    v = planned.get(nm) or installed.get(nm)
                    if mod == "Atlas_Core" and v and vkey(v) >= vkey(first):
                        conflict = True
                        msgs.append(f"CONFLICT {mod} cap {r['max']} ({r['when']}) vs {nm} {v}: {nm} {first}+ needs Atlas Core 4 (playbooks/10-to-11.md). The owner must decide: Atlas 3 with an older {nm}, or Atlas 4 and the PDS grid question; --write does not cap")
                msgs.append(f"CAP {mod} at {r['max']} (plan has {ver}): {r['when']} is installed. {r['why']} {tag}")
                if write and not conflict:
                    if inst and vkey(inst) == vkey(r["max"]):
                        new = f"# held by atlascap (installed {inst} is the cap): {raw}"
                    else:
                        new = re.sub(r"^(\s*\S+\s+)\S+", lambda m: m.group(1) + r["max"], raw, count=1)
                break
        out.append(new)
    if conflict:
        out = list(plan_lines)
    return msgs, out, n, conflict


if __name__ == "__main__":
    a = sys.argv[1:]
    if len(a) < 2 or a[0].startswith("-"):
        sys.exit(__doc__)
    table = a[a.index("--table") + 1] if "--table" in a else TABLE
    outf = a[a.index("--out") + 1] if "--out" in a else None
    write = "--write" in a
    try:
        mods = json.load(open(a[0]))
        installed = {m["name"]: m.get("version") for m in mods if isinstance(m, dict) and m.get("name")}
        lines = open(a[1], encoding="utf-8").read().splitlines()
        rows = load_table(table)
    except (OSError, ValueError, TypeError, AttributeError, KeyError) as e:
        print(f"atlascap: cannot read input ({type(e).__name__}: {e})", file=sys.stderr)
        sys.exit(2)
    app = None
    if "--app" in a:
        i = a.index("--app")
        app = a[i + 1] if i + 1 < len(a) and not a[i + 1].startswith("--") else None
        if not app or not os.path.exists(app):
            print(f"atlascap: --app needs an app folder or .mpr that exists (got {app!r})", file=sys.stderr)
            sys.exit(2)
    msgs, new, n, conflict = run(installed, lines, rows, write, internal_modules(app))
    if write and n and not conflict:
        if not os.path.exists(a[1] + ".orig"):
            import shutil
            shutil.copyfile(a[1], a[1] + ".orig")
        tmp = a[1] + ".tmp"
        open(tmp, "w", encoding="utf-8").write("\n".join(new) + "\n")
        os.replace(tmp, a[1])
        msgs.append(f"plan rewritten ({n} line(s)); the old file is {a[1]}.orig (an existing .orig is never overwritten)")
    if not msgs:
        msgs.append("no cap applies (playbooks/module-caps.tsv: no capped module is on the plan above its cap while its trigger module is installed)"
                    + ("" if app else "; PlatformDesignSystem not in localedits.json (internal modules not checked, pass --app)"))
    txt = "\n".join(msgs) + "\n"
    if outf:
        open(outf, "w", encoding="utf-8").write(txt)
    sys.stdout.write(txt)
    sys.exit(1 if n else 0)
