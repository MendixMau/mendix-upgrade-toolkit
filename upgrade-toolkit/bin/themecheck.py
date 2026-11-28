#!/usr/bin/env python3
"""themecheck.py: does the web theme compile with the strict Sass that Studio Pro uses? (LC-7)

Why: Studio Pro's mx check compiles the theme with Dart Sass and reports a failure as CE6093. In a slow container that
compile hits the 30 s limit ("Theme compilation took longer than the allowed time of 30000ms"), and later checks in the
same run printed no theme result at all, while mxbuild compiled the same theme without a word. Field: the LineApp
10.24 -> 11.12.6 run handed over an app whose own theme had `@media only screen and(min-width: 1295px)` (no space after
`and`). The build, the runtime and every journey passed; the owner's Studio Pro 11.12.6 showed "The theme could not be
compiled: Expected whitespace" on first open. This tool runs the same compiler on the same files, without a time limit,
so a theme error stops the run instead of reaching the owner.

Usage:
  themecheck.py <app dir> [--mpr App.mpr] [--version 11.12.6] [--sass "CMD ..."] [--tmp DIR] [--md out.md]

The root stylesheet is the one Studio Pro writes (deployment/sass/main.scss) when it is there; it gives the modules and
their order. Otherwise it is generated like Studio Pro's: theme/web/custom-variables.scss, then every module's
themesource/<module>/web/main.scss (with --mpr: only the modules the model has; Marketplace modules first), then
theme/web/main.scss. A generated order can differ from Studio Pro's; the output says which root was used. --tmp: where the root is written
(default the system temp; a Sass that runs in a container needs a folder the container sees, such as the run's work folder).
Sass (first that runs): --sass (then only that one), $UPG_SASS, Studio Pro <version> (macOS), $UPG_TOOLS/mxbuild-<version> and
~/.mxcli/mxbuild/<version> (tools/sass/<host platform>/sass), any Studio Pro, `sass` on PATH.
Exit: 0 PASS, 1 FAIL (the theme does not compile; the Sass error is printed), 2 input error or no Sass to run.
"""
import argparse, glob, os, platform, re, shlex, subprocess, sys, tempfile


def host_platform():
    m = platform.machine().lower()
    arch = "arm64" if m in ("arm64", "aarch64") else "x64"
    return ("osx-" if sys.platform == "darwin" else "linux-") + arch


def runs(cmd):
    try:
        r = subprocess.run(cmd + ["--version"], capture_output=True, text=True, timeout=60)
    except (OSError, subprocess.TimeoutExpired):
        return None
    return r.stdout.strip() if r.returncode == 0 else None


def find_sass(version, given):
    if given:   # the one the caller names, or none: no silent fallback to another compiler
        v = runs(shlex.split(given))
        return (shlex.split(given), f"{v} (--sass)") if v else (None, None)
    cands = []
    if os.environ.get("UPG_SASS"):
        cands.append(("UPG_SASS", shlex.split(os.environ["UPG_SASS"])))
    plat = host_platform()
    apps = sorted(glob.glob("/Applications/Mendix Studio Pro*.app"), reverse=True)
    if version:
        for a in apps:
            if re.search(rf"Studio Pro {re.escape(version)}\b", a):
                cands.append((a, [f"{a}/Contents/modeler/tools/sass/{plat}/sass"]))
        for base in (os.environ.get("UPG_TOOLS", ""), os.path.expanduser("~/.mxcli/mxbuild")):
            if base:
                for d in (f"{base}/mxbuild-{version}", f"{base}/{version}"):
                    cands.append((d, [f"{d}/modeler/tools/sass/{plat}/sass"]))
    for a in apps:
        cands.append((a, [f"{a}/Contents/modeler/tools/sass/{plat}/sass"]))
    cands.append(("PATH", ["sass"]))
    for where, cmd in cands:
        if cmd[0] != "sass" and len(cmd) == 1 and not os.access(cmd[0], os.X_OK):
            continue
        v = runs(cmd)
        if v:
            return cmd, f"{v} ({where})"
    return None, None


def model_modules(mpr):
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from mprmodel import Model
    m = Model.load(mpr)
    store = sorted(n for n, i in m.modules.items() if i.get("from_appstore"))
    own = sorted(n for n, i in m.modules.items() if not i.get("from_appstore"))
    return [n.lower() for n in store + own]


def root_lines(app, mpr):
    """-> (list of paths relative to app, how the root was made)"""
    made = os.path.join(app, "deployment", "sass", "main.scss")
    if os.path.isfile(made):
        rel = re.findall(r'@use\s+"\.\./\.\./([^"]+)"', open(made, encoding="utf-8", errors="replace").read())
        if rel:
            return rel, "deployment/sass/main.scss (written by Studio Pro or mxbuild)"
    have = {os.path.basename(os.path.dirname(os.path.dirname(p))) for p in glob.glob(os.path.join(app, "themesource", "*", "web", "main.scss"))}
    if mpr:
        mods = [n for n in model_modules(mpr) if n in have]
        how = "generated from the model's modules (order may differ from Studio Pro)"
    else:
        mods = sorted(have)
        how = "generated from every themesource folder (no --mpr; order may differ from Studio Pro)"
    rel = []
    if os.path.isfile(os.path.join(app, "theme", "web", "custom-variables.scss")):
        rel.append("theme/web/custom-variables.scss")
    rel += [f"themesource/{n}/web/main.scss" for n in mods]
    if os.path.isfile(os.path.join(app, "theme", "web", "main.scss")):
        rel.append("theme/web/main.scss")
    return rel, how


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("app")
    ap.add_argument("--mpr")
    ap.add_argument("--version")
    ap.add_argument("--sass")
    ap.add_argument("--tmp")
    ap.add_argument("--md")
    a = ap.parse_args()
    app = os.path.abspath(a.app)
    if not os.path.isdir(os.path.join(app, "theme", "web")):
        print(f"themecheck: {app} has no theme/web folder", file=sys.stderr)
        return 2
    rel, how = root_lines(app, a.mpr)
    missing = [r for r in rel if not os.path.isfile(os.path.join(app, r))]
    if missing:
        print(f"themecheck: the root names files that are not there: {', '.join(missing)}", file=sys.stderr)
        return 2
    sass, sv = find_sass(a.version, a.sass)
    if not sass:
        print("themecheck: no Sass compiler runs here (give --sass or UPG_SASS, or install Studio Pro "
              f"{a.version or ''} or the mxbuild toolset)".replace("  ", " "), file=sys.stderr)
        return 2
    with tempfile.TemporaryDirectory(prefix="themecheck-", dir=a.tmp) as tmp:
        root = os.path.join(tmp, "main.scss")
        with open(root, "w", encoding="utf-8") as f:
            f.write("".join(f'@use "{r}" as module{i};\n' for i, r in enumerate(rel)))
        r = subprocess.run(sass + ["--no-source-map", "--quiet", f"--load-path={app}", root, os.path.join(tmp, "out.css")],
                           capture_output=True, text=True, cwd=app)
        err = (r.stderr or r.stdout).replace(tmp + os.sep, "").replace(app + os.sep, "").strip()
    print(f"sass:  {sv}")
    print(f"root:  {how}, {len(rel)} stylesheets")
    status = "PASS" if r.returncode == 0 else "FAIL"
    print(f"{status} the web theme {'compiles' if status == 'PASS' else 'does not compile'}")
    if status == "FAIL":
        print("\n".join("  " + ln for ln in err.splitlines()[:30]))
        loc = re.search(r"^\s*(\S+\.scss) (\d+):(\d+)", err, re.M)
        if loc:
            print(f"  FILE {loc.group(1)} line {loc.group(2)} (Studio Pro shows this as CE6093 on open)")
    if a.md:
        with open(a.md, "w", encoding="utf-8") as f:
            f.write(f"# Theme compile\n\n{status}: the web theme {'compiles' if status == 'PASS' else 'does not compile'} "
                    f"with Sass {sv}.\n\nRoot: {how}, {len(rel)} stylesheets.\n")
            if status == "FAIL":
                f.write("\n```\n" + "\n".join(err.splitlines()[:30]) + "\n```\n")
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
