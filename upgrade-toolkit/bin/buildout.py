#!/usr/bin/env python3
"""buildout.py: the build output a baseline build leaves in the app's git tree, named exactly (DV-6, MC-3).

  buildout.py exclude <app dir>   append the untracked build-output paths to the repo's .git/info/exclude (idempotent;
                                  the app's tracked .gitignore is never touched)
  buildout.py check <app dir>     list what is dirty in the app tree, split into ACCEPTED (known build output) and OTHER;
                                  exit 0 = nothing OTHER, 1 = OTHER paths are dirty, 2 = not a git repository with a commit

Known build output, relative to the app folder, and nothing else:
  .classpath, .project, <name>.launch   Eclipse files mxbuild writes at the app root (untracked: excluded by `exclude`)
  theme-cache/**                        the compiled theme cache (TRACKED in some apps, so an exclude does nothing: it is
                                        ACCEPTED as modified instead; convertnoise.py already files it as "regenerated")
A modified source file, a model file or any other path is never accepted. convertpre.py and steps/triage.md item 9 use the
same list, so a tree that is dirty only from the baseline build passes both and a real change still refuses.
"""
import os, subprocess, sys

UNTRACKED_ROOT = (".classpath", ".project")
LAUNCH_SUFFIX = ".launch"
CACHE_PREFIX = "theme-cache/"


def git(app, *a):
    return subprocess.run(["git", "-C", app, *a], capture_output=True, text=True)


def accepted(rel, status=""):
    """rel: path relative to the app folder; status: the two-letter porcelain code ('' when unknown)."""
    if rel.startswith(CACHE_PREFIX):
        return True
    if "/" in rel:
        return False
    if status and status != "??":
        return False   # a TRACKED .project or launch file that changed is the user's, not build output
    return rel in UNTRACKED_ROOT or rel.endswith(LAUNCH_SUFFIX) and len(rel) > len(LAUNCH_SUFFIX)


def dirty(app):
    """-> (prefix, [(status, path relative to app)]) or None when app is not a git repo with a commit."""
    if git(app, "rev-parse", "--verify", "--quiet", "HEAD^{commit}").returncode != 0:
        return None
    prefix = git(app, "rev-parse", "--show-prefix").stdout.strip()
    out = []
    for ln in git(app, "status", "--porcelain", "--untracked-files=all", "--", ".").stdout.splitlines():
        if not ln.strip():
            continue
        p = ln[3:].strip().strip('"')
        if prefix and p.startswith(prefix):
            p = p[len(prefix):]
        out.append((ln[:2], p))
    return prefix, out


def exclude(app):
    r = git(app, "rev-parse", "--git-path", "info/exclude")
    if r.returncode != 0:
        print(f"buildout: {app}: not a git repository", file=sys.stderr)
        return 2
    path = r.stdout.strip()
    if not os.path.isabs(path):
        path = os.path.normpath(os.path.join(app, path))
    prefix = git(app, "rev-parse", "--show-prefix").stdout.strip()
    want = ["/" + prefix + n for n in UNTRACKED_ROOT] + ["/" + prefix + "*" + LAUNCH_SUFFIX]
    os.makedirs(os.path.dirname(path), exist_ok=True)
    have = open(path).read().splitlines() if os.path.exists(path) else []
    add = [w for w in want if w not in have]
    if add:
        with open(path, "a") as f:
            if have and open(path).read()[-1:] != "\n":
                f.write("\n")
            f.write("# upgrade-toolkit buildout.py: baseline build output (DV-6)\n" + "\n".join(add) + "\n")
    print(f"buildout: exclude {'added ' + str(len(add)) if add else 'already has all'} pattern(s) in {path}")
    return 0


def check(app):
    d = dirty(app)
    if d is None:
        print(f"buildout: {app}: not a git repository with a commit", file=sys.stderr)
        return 2
    acc = [p for s, p in d[1] if accepted(p, s)]
    oth = [(s, p) for s, p in d[1] if not accepted(p, s)]
    for p in acc:
        print(f"ACCEPTED {p}")
    for s, p in oth:
        print(f"OTHER    {s.strip()} {p}")
    print(f"buildout: {len(acc)} accepted build-output path(s), {len(oth)} other dirty path(s)")
    return 1 if oth else 0


def main():
    if len(sys.argv) != 3 or sys.argv[1] not in ("exclude", "check"):
        print(__doc__.split("\n\n")[0] + "\n  buildout.py exclude|check <app dir>", file=sys.stderr)
        return 2
    app = os.path.abspath(sys.argv[2])
    return exclude(app) if sys.argv[1] == "exclude" else check(app)


if __name__ == "__main__":
    sys.exit(main())
