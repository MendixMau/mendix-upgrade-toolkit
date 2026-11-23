#!/usr/bin/env python3
"""keptvendor.py: does a KEPT module's themesource still find the mixins, variables and imports it uses in the TARGET versions of
the packages the plan updates? (GM-15)

Why: a module that stays at its version keeps its own themesource SCSS. When the plan moves a package that ships a theme
(PlatformDesignSystem, Atlas_Core, a design system module) to a new major, a mixin, variable or file the kept SCSS uses can be
gone: PlatformDesignSystem 44.5.0 -> 45.0.0 removed the `dark-theme` mixin that the kept MendixProjectStyling uses. The model
check and the Studio Pro-free build see it only at the theme compile. theme_clash.py judges the app's OWN styling against Atlas
only; keptstyle.py lists widget selectors only. This reads every `@include`, `$variable` and `@use` / `@import` of a kept module.

  keptvendor.py <app dir> (--kept A,B | --kept-file kept.txt) --plan-file plan.txt [--own] [--cache DIR] [--json out.json]

--own (GF-56, GF-45): also judge the app's OWN styling (theme/ and each themesource module that is not a Marketplace package),
which no update refuses and so is never on kept.txt: PlatformDesignSystem 45.0.0 removed four mixins that the team's own styling
module @includes, and the first sign was the mxbuild theme compile. Triage runs it before the sign-off, without a kept list.

plan.txt lines are "<content id> <version> <Module>" (# comments allowed), as the other triage tools read them. The target
package is the cached <content id>-<version>.mpk (--cache, default UPG_CACHE or ~/.cache/upgrade-toolkit/mpk, never downloaded
here): its themesource/<Module>/**/*.scss is what the target defines. A name a kept use needs is satisfied by, in this order:
the kept module's own files, the app's own theme (theme/ and own themesource modules), any other themesource module that the plan
does not move (its current files), or the target package of the planned module. A name that only the CURRENT files of a planned
module define, and its target package does not, is reported:

  MISSING mixin dark-theme: used in themesource/<Kept>/web/main.scss:12, defined in old <Pkg> themesource/<Pkg>/web/_x.scss:3, gone in <Pkg> <version>
  MISSING variable $x / MISSING import <path> (a @use or @import whose file the target package no longer has)

When a planned module's target package is not in the cache (or cannot be read), the kept uses that only that module can answer are
NOT CHECKED with the reason, never "clean":
  NOT CHECKED <Pkg> <version>: package not cached (<cid>-<version>.mpk); N kept use(s) it defines are unverified: ...
A name defined nowhere (a Mendix core or Sass built-in name) is not reported; the summary counts the uses judged.
`--kept-file` takes the first word of each line (not keptstyle's comma split). Kept module folders are themesource/<Module>/**/*.scss; `theme` in --kept stands for the app's theme/ folder.
Exit: 0 every use judged and none missing, 1 at least one MISSING, 3 none missing but something NOT CHECKED, 2 input error.
LIMITS: namespaced `ns.$x` / `@include ns.mixin` are not read; an @import that resolves outside the app is skipped; the
package layout is assumed to hold themesource/<Module>/ at any depth of the .mpk (ASSUMED, not captured from a real package yet).
"""
import argparse, json, os, re, sys, zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import theme_clash as tc  # noqa: E402

IMPORT_RE = re.compile(r"@(?:use|import|forward)\s+([^;{}]+);")
QSTR = re.compile(r"""(["'])(.*?)\1""")


def die(msg):
    print(msg, file=sys.stderr)
    sys.exit(2)


def words(path):
    out = []
    try:
        for l in open(path, encoding="utf-8").read().splitlines():
            if l.strip() and not l.strip().startswith("#"):
                out.append(l.split())
    except OSError as e:
        die("keptvendor: " + str(e))
    return out


def import_targets(text):
    """[(path, line)] of @use/@import/@forward strings; the code copy blanks strings, so offsets are read from the raw text."""
    code = tc.scss_code(text)
    out = []
    for m in IMPORT_RE.finditer(code):
        raw = text[m.start(1):m.end(1)]
        line = code.count("\n", 0, m.start()) + 1
        for q in QSTR.finditer(raw):
            out.append((q.group(2), line))
    return out


def candidates(rel):
    d, b = os.path.split(rel)
    b = b[:-5] if b.endswith(".scss") else b
    return [os.path.join(d, x).replace(os.sep, "/") for x in (b + ".scss", "_" + b + ".scss", b + "/_index.scss", b + "/index.scss")]


def package_facts(mpk, module):
    """(facts, files, why): definitions of themesource/<module>/**/*.scss inside the .mpk, and the file paths under it."""
    facts = {"variable": set(), "mixin": set()}
    files = set()
    try:
        with zipfile.ZipFile(mpk) as z:
            for n in z.namelist():
                parts = n.replace("\\", "/").split("/")
                low = [p.lower() for p in parts]
                if "themesource" not in low:
                    continue
                i = low.index("themesource")
                if len(parts) <= i + 2 or low[i + 1] != module.lower():
                    continue
                rel = "/".join(parts[i + 2:])
                files.add(rel)
                if rel.endswith(".scss") and not os.path.basename(rel).startswith("._"):
                    f = tc.analyse(z.read(n).decode("utf-8", "replace"))
                    facts["variable"].update(x for x, _ in f["var_defs"])
                    facts["mixin"].update(x for x, _ in f["mixin_defs"])
    except (OSError, zipfile.BadZipFile) as e:
        return None, None, f"cannot read {os.path.basename(mpk)} ({type(e).__name__})"
    return facts, files, ""


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("app")
    ap.add_argument("--kept")
    ap.add_argument("--kept-file")
    ap.add_argument("--plan-file")
    ap.add_argument("--cache", default=os.environ.get("UPG_CACHE") or os.path.expanduser("~/.cache/upgrade-toolkit/mpk"))
    ap.add_argument("--json")
    ap.add_argument("--own", action="store_true", help="also read the app's own styling (theme/ and every own themesource module) like a kept module (GF-56)")
    a = ap.parse_args()
    app = os.path.abspath(a.app)
    if not os.path.isdir(app):
        die("keptvendor: not a directory: " + a.app)
    if a.kept is None and not a.kept_file:
        die("keptvendor: give --kept A,B (or --kept ''), or --kept-file FILE")
    if not a.plan_file:
        die("keptvendor: give --plan-file plan.txt")
    kept = [x for x in (a.kept or "").split(",") if x.strip()]
    if a.kept_file:
        kept += [w[0] for w in words(a.kept_file)]
    plan = {}
    for w in words(a.plan_file):
        if len(w) >= 3:
            plan[w[2]] = (w[0], w[1])
    if a.own:   # GF-56: the app's own styling is never refused by an update, so it is not on kept.txt, yet it @uses the same packages
        kept += [m for m in tc.classify(app, (), ())[1] if m not in plan] + (["theme"] if os.path.isdir(os.path.join(app, "theme")) else [])  # a planned package is the target, never own
    kept = list(dict.fromkeys(kept))
    ts = os.path.join(app, "themesource")
    mods = {d: os.path.join(ts, d) for d in sorted(os.listdir(ts)) if os.path.isdir(os.path.join(ts, d))} if os.path.isdir(ts) else {}
    planned = [m for m in mods if m in plan and m not in kept]
    rel = lambda p: os.path.relpath(p, app).replace(os.sep, "/")

    def roots(m):
        return [os.path.join(app, "theme")] if m == "theme" else [mods[m]] if m in mods else []

    def analysed(root):
        for p in tc.scss_files(root):
            yield p, tc.analyse(tc.read(p))

    # definitions available regardless of the plan: own theme, other modules the plan keeps in place, atlas included
    base = {"variable": set(), "mixin": set()}
    oldp = {m: {"variable": {}, "mixin": {}} for m in planned}
    for m in list(mods) + (["theme"] if os.path.isdir(os.path.join(app, "theme")) else []):
        if m in kept:
            continue
        for p, f in (x for r in roots(m) for x in analysed(r)):
            if m in planned:
                for x, l in f["var_defs"]:
                    oldp[m]["variable"].setdefault(x, f"{rel(p)}:{l}")
                for x, l in f["mixin_defs"]:
                    oldp[m]["mixin"].setdefault(x, f"{rel(p)}:{l}")
            else:
                base["variable"].update(x for x, _ in f["var_defs"])
                base["mixin"].update(x for x, _ in f["mixin_defs"])
    tgt, notchecked_why = {}, {}
    for m in planned:
        cid, ver = plan[m]
        mpk = os.path.join(a.cache, f"{cid}-{ver}.mpk")
        if not os.path.isfile(mpk):
            notchecked_why[m] = f"package not cached ({cid}-{ver}.mpk in {a.cache})"
            continue
        facts, files, why = package_facts(mpk, m)
        if why:
            notchecked_why[m] = why
        else:
            tgt[m] = (facts, files)

    missing, unchecked, files_n, judged = [], {}, 0, 0
    for k in kept:
        kdef = {"variable": set(), "mixin": set()}
        kfiles = []
        for root in roots(k):
            for p, f in analysed(root):
                kfiles.append((p, f))
                kdef["variable"].update(x for x, _ in f["var_defs"])
                kdef["mixin"].update(x for x, _ in f["mixin_defs"])
        files_n += len(kfiles)
        for p, f in kfiles:
            r = rel(p)
            uses = [("variable", n, l) for n, l in f["var_uses"]] + [("mixin", n, l) for n, l in f["mixin_uses"]]
            for kind, n, line in uses:
                if n in kdef[kind] or n in base[kind]:
                    judged += 1
                    continue
                owners = [m for m in planned if n in oldp[m][kind]]
                if not owners:
                    continue   # defined nowhere we can see: a core or Sass name
                judged += 1
                m = owners[0]
                shown = ("$" if kind == "variable" else "") + n
                if any(n in t[0][kind] for t in tgt.values()):
                    continue   # defined by some target package (a name may move between two planned packages)
                if notchecked_why:   # it could live in a planned package whose target cannot be read
                    um = next((o for o in owners if o in notchecked_why), next(iter(notchecked_why)))
                    unchecked.setdefault(um, []).append(f"{kind} {shown} at {r}:{line}")
                    continue
                missing.append(dict(kind=kind, name=shown, module=k, where=f"{r}:{line}", old=oldp[m][kind][n], pkg=m, version=plan[m][1]))
            for target, line in import_targets(tc.read(p)):
                base_dir = os.path.dirname(p)
                full = os.path.normpath(os.path.join(base_dir, target))
                hit = None
                for m in planned:
                    pre = os.path.join(mods[m], "")
                    if full.startswith(pre) or full == mods[m]:
                        hit = (m, os.path.relpath(full, mods[m]).replace(os.sep, "/"))
                        break
                if not hit or not any(os.path.exists(os.path.join(mods[hit[0]], c)) for c in candidates(hit[1])):
                    continue   # not into a planned module, or not a file of the current app at all
                m, sub = hit
                judged += 1
                if m in tgt:
                    if not any(c in tgt[m][1] for c in candidates(sub)):
                        missing.append(dict(kind="import", name=target, module=k, where=f"{r}:{line}", old=f"themesource/{m}/{sub}", pkg=m, version=plan[m][1]))
                else:
                    unchecked.setdefault(m, []).append(f"import {target} at {r}:{line}")
    for x in missing:
        print(f"MISSING {x['kind']} {x['name']}: used in {x['where']}, defined in old {x['pkg']} {x['old']}, gone in {x['pkg']} {x['version']}")
    for m, items in sorted(unchecked.items()):
        print(f"NOT CHECKED {m} {plan[m][1]}: {notchecked_why[m]}; {len(items)} kept use(s) only it defines are unverified: "
              + "; ".join(items[:5]) + (f" (+{len(items) - 5} more)" if len(items) > 5 else ""))
    print(f"keptvendor: {len(kept)} kept module(s), {files_n} file(s), {judged} use(s) judged against {len(planned)} planned module(s) with a theme; "
          f"{len(missing)} missing, {sum(len(v) for v in unchecked.values())} not checked"
          + ("; read the theme compile of the kept module, add a page that shows its styling to the screens step (steps/triage.md, GM-15)" if missing else ""))
    if a.json:
        json.dump(dict(missing=missing, not_checked={m: dict(why=notchecked_why[m], uses=v) for m, v in unchecked.items()}), open(a.json, "w"), indent=1)
    sys.exit(1 if missing else 3 if unchecked else 0)


main()
