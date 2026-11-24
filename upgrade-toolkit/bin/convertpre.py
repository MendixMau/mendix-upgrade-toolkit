#!/usr/bin/env python3
"""convertpre.py: is the tree ready for `mx convert`? (MC-2, MC-3)

Run it right before the convert (steps/upgrade.md, convert), with the app folder.

  convertpre.py <app dir>

REFUSE (exit 1): the git tree is not clean, except for the known baseline build output named in buildout.py (.classpath,
.project, <name>.launch, theme-cache/**: DV-6; reported as ACCEPTED, never hidden). Any other dirty path still refuses. Uncommitted build output (regenerated proxies, JS action stubs, classpath
files) mixes into the convert commit and convertnoise cannot separate it afterwards (MC-3: App H, fixed by
hand with a build: commit, the convert alone, then convertnoise PASS). Every dirty path is listed, grouped by folder; commit
build output as `build: <what>` (and keep the model out of that commit), then rerun.
WARN (exit 0): a commit between the last unedited module state (the newest `step: <Module> <version>` commit, else the
`original...` commit, else the root commit) and HEAD changes the model (*.mpr or mprcontents/) and is not a step, convert
or stepupdate commit. convertmade.sh calls every commit like that a possible edit of every module, because an MPR v1 project
keeps all modules in one .mpr (MC-2: a role-mapping `repair:` commit made nothing provable CONVERT-MADE afterwards). Move
such a change after the post-convert module pass (role mappings especially), or take the pre-convert localedits report
(--localedits) as the pristine proof for the modules.
Exit: 0 = ready (WARN lines possible), 1 = REFUSE, 2 = input error (not a git repository, no commit).
"""
import os, subprocess, sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import buildout   # the exact build-output paths a baseline build leaves (DV-6); one list for triage and convertpre


def git(app, *a):
    return subprocess.run(["git", "-C", app, *a], capture_output=True, text=True)


def main():
    if len(sys.argv) != 2 or sys.argv[1].startswith("-"):
        print(__doc__.split("\n\n")[0] + "\n  convertpre.py <app dir>", file=sys.stderr)
        return 2
    app = os.path.abspath(sys.argv[1])
    if git(app, "rev-parse", "--verify", "--quiet", "HEAD^{commit}").returncode != 0:
        print(f"convertpre: {app}: not a git repository with a commit", file=sys.stderr)
        return 2
    allp = buildout.dirty(app)[1]
    acc = [p for s, p in allp if buildout.accepted(p, s)]
    dirty = [p for s, p in allp if not buildout.accepted(p, s)]
    if acc:
        print(f"ACCEPTED: {len(acc)} baseline build-output path(s) (buildout.py): {', '.join(sorted(acc)[:5])}{' ...' if len(acc) > 5 else ''}")
    rc = 0
    if dirty:
        rc = 1
        groups = Counter()
        for p in dirty:
            groups[p.split("/", 1)[0] + ("/" if "/" in p else "")] += 1
        print(f"REFUSE: {len(dirty)} uncommitted path(s); the convert commit would hold them (convertnoise cannot separate them):")
        for g, n in sorted(groups.items()):
            print(f"   {g} ({n} path{'s' if n != 1 else ''})")
        print("   commit build output as 'build: <what>' first (not the model), then run this again")
    log = git(app, "log", "--format=%H %s").stdout.splitlines()
    base = None
    for ln in log:
        h, _, s = ln.partition(" ")
        if s.startswith("step: ") or s.lower().startswith("original"):
            base = h; break
    if base is None and log:
        base = log[-1].split(" ", 1)[0]
    warned = 0
    for ln in log:
        h, _, s = ln.partition(" ")
        if h == base:
            break
        if s.startswith(("step: ", "stepupdate: ", "convert")):
            continue
        files = git(app, "diff-tree", "--no-commit-id", "--name-only", "-r", "--root", h).stdout.splitlines()
        if any(f.endswith(".mpr") or f.startswith("mprcontents/") or "/mprcontents/" in f for f in files):
            if warned == 0:
                bs = git(app, "log", "-1", "--format=%h %s", base).stdout.strip()
                print(f"WARN: model-changing commit(s) after the last unedited state ({bs}); convertmade cannot prove a module CONVERT-MADE after them:")
            warned += 1
            print(f"   {h[:7]} {s}")
    if warned:
        print("   move them after the post-convert module pass (role mappings: rolecheck NEW-ROLES can wait), or keep the pre-convert localedits report as the proof")
    print(f"convertpre: {'REFUSED' if rc else 'ready'}; {len(dirty)} uncommitted, {warned} model-changing commit(s) since the last unedited state")
    return rc


if __name__ == "__main__":
    sys.exit(main())
