#!/usr/bin/env python3
"""zipcheck.py FILE | --find NAME DIR: exit 0 when the jar/zip opens and every member's CRC matches (GM-1).
--find NAME DIR looks for NAME under DIR (depth 6): none found = exit 1 "missing", any corrupt = exit 1 "corrupt".
Stdlib only, so it runs where unzip is absent (macOS bash 3.2 hosts, Git Bash)."""
import os, sys, zipfile

def bad(path):
    try:
        with zipfile.ZipFile(path) as z:
            first = z.testzip()
            return "member %s fails its CRC" % first if first else None
    except Exception as e:  # BadZipFile, EOFError, OSError, zlib.error
        return "not a readable zip (%s)" % e

def main(a):
    if len(a) == 1:
        r = bad(a[0]); print("zipcheck: %s: %s" % (a[0], r or "ok")); return 1 if r else 0
    if len(a) == 3 and a[0] == "--find":
        name, top = a[1], a[2]; found = []
        for d, ds, fs in os.walk(top):
            if d[len(top):].count(os.sep) >= 6: ds[:] = []
            if name in fs: found.append(os.path.join(d, name))
        if not found:
            print("zipcheck: no %s under %s" % (name, top), file=sys.stderr); return 1
        rc = 0
        for f in found:
            r = bad(f)
            if r: print("zipcheck: %s is corrupt: %s" % (f, r), file=sys.stderr); rc = 1
        return rc
    print("usage: zipcheck.py FILE | --find NAME DIR", file=sys.stderr); return 2

sys.exit(main(sys.argv[1:]))
