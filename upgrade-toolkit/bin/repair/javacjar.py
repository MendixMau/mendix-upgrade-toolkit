#!/usr/bin/env python3
"""javacjar.py: for each javac "cannot find symbol" in an mxbuild log, name the jars that carry the class and the one that hides it.

  javacjar.py <project dir> <build log>
  javacjar.py <project dir> --strip userlib/<fat>.jar [--apply]

Why (cold CMM, 10.24.28): MendixSSO 10.6.2 calls CookieHeaderNames.SameSite, which netty-codec-http 4.2.17 in
vendorlib has. userlib/server-examples-0.4.1-SNAPSHOT.jar (an OPC UA library, built as one fat jar) carries its
own older Netty without it, and javac took that copy: "cannot find symbol ... location: class CookieHeaderNames".
jarclash.py listed the clash after the updates, as a note; the build stop named only javafinal.py.

The class of each error is resolved through the imports of the source file, then looked up in every userlib/ and
vendorlib/ jar (and their nested jars). A jar that has the class but not the symbol (no nested class, no name in the
class file) HIDES the jar that has both:

  SYMBOL io.netty.handler.codec.http.cookie.CookieHeaderNames.SameSite (OpenIDUtils.java:237)
    HAS        vendorlib/netty-codec-http-4.2.17.Final.jar
    HIDDEN BY  userlib/server-examples-0.4.1-SNAPSHOT.jar (an older copy of the class)

--strip writes the fat jar again without every class a vendorlib jar also carries (the libraries the modules manage
win), dry run unless --apply; its own classes and the classes only it has stay. The app's git keeps the old jar.
Exit: 0 = nothing hidden (or a strip done), 1 = a class is hidden by an older copy, 2 = input error.
"""
import argparse, io, os, re, shutil, sys, tempfile, zipfile

ERR = re.compile(r"^(?P<file>\S+\.java):(?P<line>\d+): error: cannot find symbol\n(?:.*\n){0,3}?\s*symbol:\s+(?P<kind>\w+)\s+(?P<sym>[\w$]+)[^\n]*\n\s*location:\s+(?:\w+\s+)*?(?:of type\s+)?(?P<loc>[\w.$]+)\s*$", re.M)


def jars(project):
    """[(label, ZipFile)] of userlib/ and vendorlib/ jars and the jars nested in them."""
    out = []
    for d in ("userlib", "vendorlib"):
        p = os.path.join(project, d)
        for f in sorted(os.listdir(p)) if os.path.isdir(p) else []:
            if not f.endswith(".jar"):
                continue
            try:
                z = zipfile.ZipFile(os.path.join(p, f))
            except zipfile.BadZipFile:
                continue
            out.append((f"{d}/{f}", z))
            for n in z.namelist():
                if n.endswith(".jar") and re.search(r"(^|/)(lib|BOOT-INF/lib)/[^/]+\.jar$", n):
                    try:
                        out.append((f"{d}/{f}!{n}", zipfile.ZipFile(io.BytesIO(z.read(n)))))
                    except zipfile.BadZipFile:
                        pass
    return out


def fqcn(project, src, simple):
    """The full class name of a simple name, from the imports of the source file."""
    if "." in simple:
        return simple
    path = src if os.path.isabs(src) else os.path.join(project, src)
    try:
        text = open(path, encoding="utf-8", errors="replace").read()
    except OSError:
        return None
    m = re.search(rf"^import\s+([\w.]+\.{re.escape(simple)})\s*;", text, re.M)
    if m:
        return m.group(1)
    m = re.search(r"^package\s+([\w.]+)\s*;", text, re.M)
    return f"{m.group(1)}.{simple}" if m else None


def errors(log):
    t = open(log, encoding="utf-8", errors="replace").read()
    for m in ERR.finditer(t):
        yield m.group("file"), m.group("line"), m.group("sym"), m.group("loc")


def strip(project, jar, apply):
    vend = set()
    for label, z in jars(project):
        if label.startswith("vendorlib/"):
            vend |= {n for n in z.namelist() if n.endswith(".class")}
    path = os.path.join(project, jar)
    try:
        src = zipfile.ZipFile(path)
    except (OSError, zipfile.BadZipFile) as e:
        print(f"javacjar: {jar}: {e}", file=sys.stderr); return 2
    drop = [i for i in src.infolist() if i.filename in vend]
    pk = sorted({i.filename.rsplit("/", 1)[0].replace("/", ".") for i in drop})
    print(f"STRIP {jar}: {len(drop)} class(es) a vendorlib jar also carries, in {len(pk)} package(s)"
          + (f" ({', '.join(pk[:4])}{', ...' if len(pk) > 4 else ''})" if pk else ""))
    print(f"  KEEP {len(src.infolist()) - len(drop)} entries")
    if not drop or not apply:
        print("dry run (add --apply to write the jar)" if drop else "nothing to strip")
        return 0
    gone = {i.filename for i in drop}
    fd, tmp = tempfile.mkstemp(suffix=".jar", dir=os.path.dirname(path)); os.close(fd)
    with zipfile.ZipFile(tmp, "w") as out:
        for i in src.infolist():
            if i.filename not in gone:
                out.writestr(i, src.read(i.filename))
    src.close()
    shutil.move(tmp, path)
    print(f"wrote {jar}; rerun mxbuild, then the quick start (the library now runs on the vendorlib copies)")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("project"); ap.add_argument("log", nargs="?")
    ap.add_argument("--strip"); ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    if a.strip:
        sys.exit(strip(a.project, a.strip, a.apply))
    if not a.log or not os.path.isfile(a.log):
        sys.exit(f"javacjar: give the mxbuild log ({a.log}: not a file)")
    js = jars(a.project)
    seen, hidden, n = set(), 0, 0
    for src, line, sym, loc in errors(a.log):
        cls = fqcn(a.project, src, loc.split("<")[0])
        key = (cls, sym)
        if key in seen:
            continue
        seen.add(key); n += 1
        where = f"{os.path.basename(src)}:{line}"
        if not cls:
            print(f"SYMBOL {loc}.{sym} ({where}): the class name is not in the imports, not looked up"); continue
        entry = cls.replace(".", "/") + ".class"
        has, lacks = [], []
        for label, z in js:
            names = set(z.namelist())
            if entry not in names:
                continue
            nested = cls.replace(".", "/") + "$" + sym + ".class"
            (has if nested in names or sym.encode() in z.read(entry) else lacks).append(label)
        print(f"SYMBOL {cls}.{sym} ({where})")
        for h in has:
            print(f"  HAS        {h}")
        for l in lacks:
            print(f"  HIDDEN BY  {l} (an older copy of the class)" if has else f"  LACKS      {l}")
        if has and lacks:
            hidden += 1
        if not has and not lacks:
            print("  in no jar of userlib/ or vendorlib/")
    print(f"javacjar: {n} missing symbol(s), {hidden} hidden by an older copy of the class in another jar"
          + ("; repair: steps/repair.md row 31" if hidden else ""))
    sys.exit(1 if hidden else 0)


if __name__ == "__main__":
    main()
