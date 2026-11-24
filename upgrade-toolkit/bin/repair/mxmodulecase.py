#!/usr/bin/env python3
"""mxmodulecase.py: make an add-on module's build cache folder findable under the case Gradle asks for (Linux).

Why: mxbuild on Linux unpacks `modules/<Name>.mxmodule` into `.mendix-cache/modules/<name>.mxmodule` (lower case), then
Gradle looks for `.mendix-cache/modules/<Name>.mxmodule/javasource`: "not found", followed by hundreds of javac errors
"package <name>.proxies does not exist" (run LDMS, mxbuild 9.24.1). Windows and macOS (case-insensitive) never see it.

  mxmodulecase.py <project dir> [--log build.log] [--check]

The case Gradle wants comes from the file names under modules/*.mxmodule and, with --log, from every
`.mendix-cache/modules/<X>.mxmodule/` the build log named. For each wanted spelling that is missing in
`.mendix-cache/modules/` while a folder with the same name in another case is there, a relative symlink
`<wanted> -> <existing>` is created; a spelling that already resolves (a case-insensitive disk) needs none. Prints one LINK line per link and a summary. Never touches a folder that exists, a
spelling with no folder in any case (the cache is created by the build, so run this AFTER a failed build), or anything
outside the cache. Idempotent. Exit: 0 = nothing to do (or all linked), 1 = links needed (--check), 2 = input error.
The pipeline runs it after a build that failed with that message and retries the build once.
"""
import argparse, os, re, sys

WANT_IN_LOG = re.compile(r"\.mendix-cache/modules/([^/\s'\"]+\.mxmodule)/")


def wanted(project, log):
    names = set()
    mods = os.path.join(project, "modules")
    if os.path.isdir(mods):
        names |= {f for f in os.listdir(mods) if f.endswith(".mxmodule")}
    if log:
        try:
            names |= set(WANT_IN_LOG.findall(open(log, errors="replace").read()))
        except OSError as e:
            print(f"mxmodulecase: --log {log}: {e}", file=sys.stderr); sys.exit(2)
    return sorted(names)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("project")
    ap.add_argument("--log")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    if not os.path.isdir(a.project):
        print(f"mxmodulecase: {a.project}: not a folder", file=sys.stderr); return 2
    cache = os.path.join(a.project, ".mendix-cache", "modules")
    todo = []
    if os.path.isdir(cache):
        have = os.listdir(cache)
        for w in wanted(a.project, a.log):
            # already resolves: linked before, or a case-insensitive disk (macOS, Windows) finds the other case itself
            if w in have or os.path.exists(os.path.join(cache, w)):
                continue
            # a real folder in another case (a link of ours is not a second folder)
            src = [h for h in have if h.lower() == w.lower() and os.path.isdir(os.path.join(cache, h))
                   and not os.path.islink(os.path.join(cache, h))]
            if len(src) == 1:
                todo.append((w, src[0]))
    for w, src in todo:
        print(f"{'WOULD LINK' if a.check else 'LINK'} .mendix-cache/modules/{w} -> {src}")
        if not a.check:
            os.symlink(src, os.path.join(cache, w))
    print(f"summary: {len(todo)} cache folder(s) {'need' if a.check else 'given'} the other-case name")
    return 1 if (a.check and todo) else 0


if __name__ == "__main__":
    sys.exit(main())
