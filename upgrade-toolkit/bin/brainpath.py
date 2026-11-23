#!/usr/bin/env python3
"""Find the company brain: the folder whose baseline/versions holds the Studio Pro version tables.

Order: $UPG_BRAIN, then UPG_BRAIN= in ~/.config/upgrade-toolkit/local.env, then the first ~/Mendix/*-brain folder with
version tables (a folder ending in -test only when nothing else has tables), then the brain this repo ships
(<repo>/company-brain-test/brain, found from this file's own location; GF-10; UPG_BRAIN_SHIPPED=0 skips it). Prints the path, or nothing and exit 1.

`--describe` prints one line, always exit 0, for triage and the gate summary (DV-3): `brain: <path> (from UPG_BRAIN|local.env|tools
folder)`, or `brain: none found (looked: ...) - set UPG_BRAIN=<path>`. The search order is unchanged; this only says what it found.

Cold test WM1: the default was the literal text ~/Mendix/<company>-brain, which never matches a folder, so the
release-note check never ran unless a person had set UPG_BRAIN.
"""
import glob
import os
import sys
from pathlib import Path


# GF-10: the brain this repo ships (SETUP.md says so); upgrade-toolkit/bin/brainpath.py -> <repo>/company-brain-test/brain
SHIPPED = str(Path(__file__).resolve().parent.parent.parent / "company-brain-test" / "brain")


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
    if os.environ.get("UPG_BRAIN_SHIPPED") != "0" and has_tables(SHIPPED):
        return SHIPPED, "shipped in this repo"
    return None, "no folder under ~/Mendix holds brain version tables (set UPG_BRAIN, or UPG_BRAIN= in ~/.config/upgrade-toolkit/local.env)"


def describe():
    """The one visibility line (DV-3): which brain was found and by which source, or that none was and where it looked."""
    path, how = find()
    if path:
        src = how if how in ("UPG_BRAIN", "local.env") else ("this repo" if how == "shipped in this repo" else "tools folder")
        return f"brain: {path} (from {src})"
    env, loc = os.environ.get("UPG_BRAIN"), from_local_env()
    looked = [f"UPG_BRAIN {env + ' has no baseline/versions tables' if env else 'unset'}",
              f"local.env {loc + ' has no baseline/versions tables' if loc else 'no entry'}",
              "~/Mendix/*-brain none", "this repo none"]
    return "brain: none found (looked: " + ", ".join(looked) + ") - set UPG_BRAIN=<path>"


if __name__ == "__main__":
    if "--describe" in sys.argv[1:]:
        print(describe())
        sys.exit(0)
    path, how = find()
    if path:
        print(path)
        sys.exit(0)
    print(how, file=sys.stderr)
    sys.exit(1)
