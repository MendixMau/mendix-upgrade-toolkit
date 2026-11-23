#!/usr/bin/env python3
"""Find the company brain: the folder whose baseline/versions holds the Studio Pro version tables.

Order: $UPG_BRAIN, then UPG_BRAIN= in ~/.config/upgrade-toolkit/local.env, then the first ~/Mendix/*-brain folder with
version tables (a folder ending in -test only when nothing else has tables), else the starter brain the toolkit ships
(data/starter-brain: the public Mendix release-note tables). Prints the path; the reason it was picked goes to stderr.
--company: only a company brain, nothing and exit 1 when there is none.

`--describe` prints one line, always exit 0, for triage and the gate summary (DV-3): `brain: <path> (from UPG_BRAIN|local.env|tools
folder)`, or `brain: none found (looked: ...) - set UPG_BRAIN=<path>`. The search order is unchanged; this only says what it found.

Cold test WM1: the default was the literal text ~/Mendix/<company>-brain, which never matches a folder, so the
release-note check never ran unless a person had set UPG_BRAIN.
Cold test (fresh install): no company brain at all, so the check still never ran and the cockpit asked the person to
decide. The starter brain makes the check run anyway; a company brain adds its own lessons on top and wins where both
have a table (release_impact.py reads the starter only for what the company brain lacks).
"""
import glob
import os
import sys
from pathlib import Path

STARTER = str(Path(__file__).resolve().parent.parent / "data" / "starter-brain")


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


def find_company():
    """(path, how) of the company brain, or (None, why not)."""
    for how, d in (("UPG_BRAIN", os.environ.get("UPG_BRAIN")), ("local.env", from_local_env())):
        if d:
            return (d, how) if has_tables(d) else (None, f"{how} points at {d}, which has no baseline/versions tables")
    cands = sorted(c for c in glob.glob(str(Path.home() / "Mendix" / "*-brain*")) if os.path.isdir(c) and has_tables(c))
    cands.sort(key=lambda c: c.endswith("-test"))
    if cands:
        return cands[0], "found under ~/Mendix"
    return None, "no folder under ~/Mendix holds brain version tables (set UPG_BRAIN, or UPG_BRAIN= in ~/.config/upgrade-toolkit/local.env)"


def find():
    """(path, how): the company brain, else the starter brain (how names why no company brain was used)."""
    path, how = find_company()
    if path:
        return path, how
    if has_tables(STARTER):
        return STARTER, f"starter brain shipped with the toolkit (public Mendix release notes); no company brain: {how}"
    return None, how


def describe():
    """The one visibility line (DV-3): which brain was found and by which source, or that none was and where it looked."""
    path, how = find()
    starter = path == STARTER
    if path and not starter:
        src = how if how in ("UPG_BRAIN", "local.env") else "tools folder"
        return f"brain: {path} (from {src})"
    env, loc = os.environ.get("UPG_BRAIN"), from_local_env()
    looked = [f"UPG_BRAIN {env + ' has no baseline/versions tables' if env else 'unset'}",
              f"local.env {loc + ' has no baseline/versions tables' if loc else 'no entry'}",
              "~/Mendix/*-brain none"]
    line = "brain: none found (looked: " + ", ".join(looked) + ") - set UPG_BRAIN=<path>"
    return line + (f" - using the starter brain {STARTER}" if starter else "")


if __name__ == "__main__":
    if "--describe" in sys.argv[1:]:
        print(describe())
        sys.exit(0)
    path, how = find_company() if "--company" in sys.argv[1:] else find()
    if path:
        if path == STARTER:
            print(how, file=sys.stderr)
        print(path)
        sys.exit(0)
    print(how, file=sys.stderr)
    sys.exit(1)
