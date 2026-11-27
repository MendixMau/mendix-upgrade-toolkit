#!/usr/bin/env python3
"""stubcheck.py: is the code of every JavaScript and Java action still there, or did a stub take its place? (LC-1, backlog 54)

Why: Studio Pro and mxbuild write a stub for every JS or Java action in the model whose file is missing:
`throw new Error("JavaScript action was not implemented")` or `throw new ...MendixRuntimeException("Java action was not
implemented")`. Neither mx check nor the build reports it; the app starts and the action fails at runtime. Field: a
LineApp 10.24 -> 11.12 React upgrade moved 88 HTML snippet scripts into JS actions. The owner's team brought the model
into their own repository without those files, Studio Pro wrote 102 stubs, and every page lost its script with 0 errors
in the error list. Their review read it as "the AI tool silently removed the scripts". NR2-22 is the same on the Java side
(OQL packages with backslash paths gave a green build of 11 stubs).

Usage:
  stubcheck.py <app dir> [--baseline <dir | .mpk/.zip | git:REV>] [--md out.md]

Scanned: javascriptsource/<module>/actions/*.js and javasource/<module>/actions/*.java. An action is a STUB when its
USER CODE block holds only the generated throw (comments and blank lines ignored).
With --baseline (the app before the step, or the pack that was handed over; git:REV reads <app dir>'s own git):
  LOST     the action is a stub here and had code in the baseline
  MISSING  the action file is gone here and had code in the baseline (Studio Pro writes the stub on the next deploy)
  STUB     a stub here that was a stub or absent in the baseline too (listed, never a failure)
Without --baseline every stub is listed and nothing fails.
Exit: 0 no LOST or MISSING, 1 LOST or MISSING found, 2 input error.
"""
import argparse, os, re, subprocess, sys, zipfile

BLOCK = re.compile(r"//\s*BEGIN USER CODE\s*\n(.*?)//\s*END USER CODE", re.S)
STUB = re.compile(r'^throw\s+new\s+[\w.]*(Error|Exception)\(\s*"(JavaScript|Java) action was not implemented"\s*\)\s*;?$')
ACTION = re.compile(r"^(javascriptsource/[^/]+/actions/[^/]+\.js|javasource/[^/]+/actions/[^/]+\.java)$")


def user_code(text):
    m = BLOCK.search(text.replace("\r\n", "\n").replace("\r", "\n"))
    if not m:
        return None   # no markers: hand-written file, never a generated stub
    body = re.sub(r"/\*.*?\*/", "", m.group(1), flags=re.S)
    lines = [re.sub(r"//.*$", "", ln).strip() for ln in body.split("\n")]
    return "\n".join(ln for ln in lines if ln)


def is_stub(text):
    code = user_code(text)
    return code is not None and bool(STUB.match(code))


def from_dir(top):
    out = {}
    for kind in ("javascriptsource", "javasource"):
        base = os.path.join(top, kind)
        if not os.path.isdir(base):
            continue
        for mod in sorted(os.listdir(base)):
            adir = os.path.join(base, mod, "actions")
            if not os.path.isdir(adir):
                continue
            for f in sorted(os.listdir(adir)):
                rel = "%s/%s/actions/%s" % (kind, mod, f)
                if ACTION.match(rel):
                    with open(os.path.join(adir, f), errors="replace") as fh:
                        out[rel] = fh.read()
    return out


def from_zip(path):
    out = {}
    with zipfile.ZipFile(path) as z:
        for n in z.namelist():
            rel = n.replace("\\", "/").lstrip("./")
            if ACTION.match(rel):
                out[rel] = z.read(n).decode("utf-8", "replace")
    return out


def from_git(app, rev):
    ls = subprocess.run(["git", "-C", app, "ls-tree", "-r", "--name-only", rev], capture_output=True, text=True)
    if ls.returncode != 0:
        raise ValueError("git ls-tree %s failed: %s" % (rev, ls.stderr.strip()))
    out = {}
    for rel in ls.stdout.splitlines():
        if ACTION.match(rel):
            show = subprocess.run(["git", "-C", app, "show", "%s:%s" % (rev, rel)], capture_output=True)
            out[rel] = show.stdout.decode("utf-8", "replace")
    return out


def load(src, app):
    if src.startswith("git:"):
        return from_git(app, src[4:])
    if os.path.isdir(src):
        return from_dir(src)
    if os.path.isfile(src) and zipfile.is_zipfile(src):
        return from_zip(src)
    raise ValueError("baseline %s is not a folder, a zip/.mpk or git:REV" % src)


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("app")
    ap.add_argument("--baseline")
    ap.add_argument("--md")
    a = ap.parse_args(argv)
    if not os.path.isdir(a.app):
        print("stubcheck: %s is not a folder" % a.app, file=sys.stderr)
        return 2
    try:
        now = from_dir(a.app)
        base = load(a.baseline, a.app) if a.baseline else None
    except (ValueError, OSError, zipfile.BadZipFile) as e:
        print("stubcheck: %s" % e, file=sys.stderr)
        return 2
    rows = []
    for rel in sorted(set(now) | set(base or {})):
        had = base is not None and rel in base and user_code(base[rel]) != "" and not is_stub(base[rel])
        if rel in now and is_stub(now[rel]):
            rows.append(("LOST" if had else "STUB", rel))
        elif rel not in now and had:
            rows.append(("MISSING", rel))
    bad = [r for r in rows if r[0] in ("LOST", "MISSING")]
    count = {k: sum(1 for r in rows if r[0] == k) for k in ("LOST", "MISSING", "STUB")}
    head = "stubcheck: %d actions scanned%s: %d LOST, %d MISSING, %d STUB" % (
        len(now), " against %d in the baseline" % len(base) if base is not None else "", count["LOST"], count["MISSING"], count["STUB"])
    print(head)
    for kind, rel in rows:
        print("  %-7s %s" % (kind, rel))
    if bad:
        print("FAIL: %d action(s) had code and now have none: the app builds and starts, the action throws at runtime. "
              "Copy the files back from the baseline (javascriptsource/ and javasource/ travel with the model, never the .mpr alone)" % len(bad))
    elif base is None and rows:
        print("NOTE: %d stub(s), no baseline given: run again with --baseline to tell a lost action from a new empty one" % len(rows))
    if a.md:
        with open(a.md, "w") as fh:
            fh.write("# Action stubs\n\n%s\n\n" % head)
            if rows:
                fh.write("| Kind | File |\n|---|---|\n")
                fh.writelines("| %s | `%s` |\n" % r for r in rows)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
