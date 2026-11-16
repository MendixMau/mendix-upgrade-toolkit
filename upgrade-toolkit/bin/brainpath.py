#!/usr/bin/env python3
"""Find the company brain: the folder whose baseline/versions holds the Studio Pro version tables.

Order: $UPG_BRAIN, then UPG_BRAIN= in ~/.config/upgrade-toolkit/local.env, then the first ~/Mendix/*-brain folder with
version tables (a folder ending in -test only when nothing else has tables). Prints the path, or nothing and exit 1.

Cold test WM1: the default was the literal text ~/Mendix/<company>-brain, which never matches a folder, so the
release-note check never ran unless a person had set UPG_BRAIN.
"""
import glob
import os
import sys
from pathlib import Path


def has_tables(d):
    return bool(glob.glob(os.path.join(d, "baseline", "versions", "studio-pro-upgrade-*.md")))


def from_local_env():
    p = Path.home() / ".config" / "upgrade-toolkit" / "local.env"
    try:
        for line in p.read_text().splitlines():
            line = line.strip()
            if line.startswith("UPG_BRAIN="):
                return os.path.expanduser(line.split("=", 1)[1].strip().strip("'\""))
    except OSError:
        pass
    return None


def find():
    """(path, how) of the brain, or (None, why not)."""
    for how, d in (("UPG_BRAIN", os.environ.get("UPG_BRAIN")), ("local.env", from_local_env())):
        if d:
            return (d, how) if has_tables(d) else (None, f"{how} points at {d}, which has no baseline/versions tables")
    cands = sorted(c for c in glob.glob(str(Path.home() / "Mendix" / "*-brain*")) if os.path.isdir(c) and has_tables(c))
    cands.sort(key=lambda c: c.endswith("-test"))
    if cands:
        return cands[0], "found under ~/Mendix"
    return None, "no folder under ~/Mendix holds brain version tables (set UPG_BRAIN, or UPG_BRAIN= in ~/.config/upgrade-toolkit/local.env)"


if __name__ == "__main__":
    path, how = find()
    if path:
        print(path)
        sys.exit(0)
    print(how, file=sys.stderr)
    sys.exit(1)
