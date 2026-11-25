#!/usr/bin/env python3
"""mxversion.py: print the FULL Mendix version (10.24.16.96987) of a toolset, runtime, project or package.

mxcli refuses a near match ("10.24.16" is not "10.24.16.96987"), and a log line or a report that says only "10.24"
cannot be reproduced. Every step records the full string.

  mxversion.py <path> [--short]

  mxbuild dir     runtime/bundles/com.mendix.public-api.jar  MANIFEST Implementation-Version
  runtime dir     runtime/launcher/runtimelauncher.jar (or the public-api bundle)  MANIFEST; also the CDN layout
                  <dir>/<full version>/runtime/... (one version only; S4: the 11.x
                  tarball extracts to <dir>/11.12.2/runtime, a 3-part folder name, the full version is read from the jar)
  app.mpr / dir   _MetaData._ProductVersion
  app.mda         model/metadata.json RuntimeVersion, else the version in the model file name
  x.mpk           a Marketplace module package (zip holding project.mpr): the Studio Pro version that built it (GM-17;
                  planbuild.py drops a plan line whose package was built before 10.21 on a target of 11)
  x.mxmodule      add-on module (a zip holding project.mpr): the Studio Pro version that BUILT it (T2-2). Mendix 11
                  refuses one built before 10.21 (CE1893) and a vendor binary cannot be reopened.
--short prints major.minor.patch. Exit 0, or 2 when no version is found.

  mxversion.py --check <version> [--uses tag,tag]            a patch listed in playbooks/patch-windows.tsv: exit 1 (REFUSE) or WARN
  mxversion.py --pick <major.minor> --available v,v,... [--uses tag,tag]   newest listed patch outside every window
--available is the patches that have release notes (read at triage, SKILL.md LTS-1). Producer of the table: this repo
(playbooks/patch-windows.tsv, public release-note facts only); consumers: steps/triage.md item 2 (--pick, then --check) and
bin/cloud/upgrade-pipeline.sh (--check on --target / --target2; UPG_ALLOW_BAD_PATCH=1 goes on anyway). Exit 0 / 1 refused / 2 unusable input.
"""
import glob, json, os, re, sqlite3, sys, tempfile, zipfile


def manifest(jar):
    try:
        with zipfile.ZipFile(jar) as z:
            m = z.read("META-INF/MANIFEST.MF").decode("utf-8", "replace")
    except (OSError, KeyError, zipfile.BadZipFile):
        return None
    for key in ("Implementation-Version", "Bundle-Version"):
        r = re.search(rf"^{key}:\s*(\S+)", m, re.M)
        if r and re.match(r"^\d+\.\d+\.\d+", r.group(1)):
            return r.group(1)
    return None


def mxmodule_version(path):
    """Studio Pro version inside an add-on module (.mxmodule = zip with project.mpr; T2-2). None when unreadable."""
    try:
        with zipfile.ZipFile(path) as z:
            mprs = [n for n in z.namelist() if n.lower().endswith(".mpr")]
            if not mprs:
                return None
            mprs.sort(key=lambda n: (os.path.basename(n).lower() != "project.mpr", n.count("/"), n))
            with tempfile.TemporaryDirectory() as d:
                out = os.path.join(d, "inner.mpr")
                with open(out, "wb") as f:
                    f.write(z.read(mprs[0]))
                return version(out)
    except (OSError, zipfile.BadZipFile, sqlite3.Error):
        return None


def addons(project):
    """[(file name, version or None)] for <project dir>/modules/*.mxmodule, sorted. Shared by triage and missing_deps."""
    return [(os.path.basename(f), mxmodule_version(f))
            for f in sorted(glob.glob(os.path.join(project, "modules", "*.mxmodule")))]


def below(v, major, minor):
    """True when version string v is older than major.minor (10.21 -> (10, 21)); unreadable is not below."""
    m = re.match(r"^(\d+)\.(\d+)", v or "")
    return bool(m) and (int(m.group(1)), int(m.group(2))) < (major, minor)


def version(p):
    if p.endswith((".mxmodule", ".mpk")):
        return mxmodule_version(p)
    if os.path.isdir(p):
        for rel in ("runtime/bundles/com.mendix.public-api.jar", "runtime/launcher/runtimelauncher.jar",
                    "bundles/com.mendix.public-api.jar", "launcher/runtimelauncher.jar"):
            if os.path.exists(os.path.join(p, rel)):
                v = manifest(os.path.join(p, rel))
                if v:
                    return v
        # the CDN runtime layout: runtime-9.24.32/9.24.32.58223/runtime/... (runapp.py reads it the same way; E7-10)
        subs = [d for d in glob.glob(os.path.join(p, "*")) if os.path.isdir(d)
                and re.match(r"^\d+\.\d+\.\d+(\.\d+)?$", os.path.basename(d))]
        found = {v for v in (version(d) for d in subs) if v}
        if len(found) == 1:
            return found.pop()
        if len(found) > 1:
            print(f"mxversion: {p} holds several runtimes ({', '.join(sorted(found))}): name one", file=sys.stderr)
            return None
        mprs = glob.glob(os.path.join(p, "*.mpr"))
        if len(mprs) == 1:
            p = mprs[0]
    if p.endswith(".mpr"):
        con = sqlite3.connect(f"file:{p}?mode=ro", uri=True)
        try:
            return con.execute("select _ProductVersion from _MetaData").fetchone()[0]
        except sqlite3.Error:
            return None
    if p.endswith(".mda"):
        with zipfile.ZipFile(p) as z:
            try:
                meta = json.loads(z.read("model/metadata.json"))
                if meta.get("RuntimeVersion"):
                    return meta["RuntimeVersion"]
            except KeyError:
                pass
            for n in z.namelist():
                r = re.search(r"(\d+\.\d+\.\d+\.\d+)", n)
                if r:
                    return r.group(1)
    return None


WINDOWS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "playbooks", "patch-windows.tsv")


def vkey(v):
    return tuple(int(x) for x in re.findall(r"\d+", v or "")[:3])


def windows(path=WINDOWS):
    cols = ("id", "from", "to", "fixed_in", "applies_if", "effect", "why", "source")
    rows = []
    for n, ln in enumerate(open(path, encoding="utf-8").read().splitlines(), 1):
        if not ln.strip() or ln.startswith("#") or ln.startswith("id\t"):
            continue
        if ln.count("\t") < 7:
            print(f"mxversion: {os.path.basename(path)} line {n} has {ln.count(chr(9)) + 1} columns, want 8: row skipped", file=sys.stderr)
            continue
        rows.append(dict(zip(cols, ln.split("\t"))))
    return rows


def known_tags(path=WINDOWS):
    return sorted({r["applies_if"] for r in windows(path)} - {"always"})


def hits(v, uses=(), path=WINDOWS):
    """[(level, row)] for every window holding patch v. level REFUSE or WARN; an unconfirmed condition is WARN."""
    out = []
    for r in windows(path):
        if not vkey(r["from"]) <= vkey(v) <= vkey(r["to"]):
            continue
        known = r["applies_if"] == "always" or r["applies_if"] in uses
        out.append(("REFUSE" if r["effect"] == "refuse" and known else "WARN", r))
    return out


def pick(minor, available, uses=(), path=WINDOWS):
    """Newest available patch of major.minor outside every window; else the newest not refused; else None."""
    mine = sorted((v for v in available if v.startswith(minor + ".")), key=vkey, reverse=True)
    clean = [v for v in mine if not hits(v, uses, path)]
    ok = [v for v in mine if all(lv != "REFUSE" for lv, _ in hits(v, uses, path))]
    return (clean or ok or [None])[0]


def say(v, found):
    for lv, r in found:
        cond = "" if r["applies_if"] == "always" or lv == "REFUSE" else f" (applies if: {r['applies_if']})"
        fix = "No fixed version yet" if r["fixed_in"].startswith("none") else f"Fixed in {r['fixed_in']}"
        print(f"{lv} {v}{cond}: {r['why']} {fix}. [{r['id']}: {r['source']}]")


def cli(a):
    def bad(msg):
        print(f"mxversion: {msg}", file=sys.stderr); return 2
    uses = ()
    if "--uses" in a:
        k = a.index("--uses")
        if k + 1 >= len(a) or a[k + 1].startswith("--"):
            return bad("--uses needs a value (tag,tag)")
        uses = tuple(t for t in a[k + 1].split(",") if t)
        tags = known_tags()
        unknown = [t for t in uses if t not in tags]
        if unknown:
            return bad(f"unknown --uses tag {', '.join(unknown)}; known tags: {', '.join(tags)}")
    if a[0] == "--check":
        if len(a) < 2 or a[1].startswith("--"):
            return bad("--check needs a version (10.24.7 or 10.24.7.96987)")
        if not re.match(r"^\d+\.\d+\.\d+", a[1]):
            return bad(f"'{a[1]}' has no three-part x.y.z version")
        found = hits(a[1], uses)
        say(a[1], found)
        if not found:
            print(f"OK {a[1]}: in no window of playbooks/patch-windows.tsv")
        return 1 if any(lv == "REFUSE" for lv, _ in found) else 0
    if a[0] == "--pick":
        if "--available" not in a or a.index("--available") + 1 >= len(a):
            return bad("--pick <major.minor> --available v,v,... (the patches that have release notes)")
        if len(a) < 2 or not re.match(r"^\d+\.\d+$", a[1]):
            return bad("--pick needs a major.minor such as 10.24")
        got = pick(a[1], [v for v in a[a.index("--available") + 1].split(",") if v], uses)
        if not got:
            print(f"mxversion: no usable {a[1]} patch among the available ones (every one is refused or none was given)", file=sys.stderr); return 2
        say(got, hits(got, uses))
        print(got)
        return 0
    sys.exit(__doc__)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    if sys.argv[1] in ("--check", "--pick"):
        sys.exit(cli(sys.argv[1:]))
    v = version(sys.argv[1])
    if not v:
        print(f"mxversion: no Mendix version found in {sys.argv[1]}", file=sys.stderr); sys.exit(2)
    print(".".join(v.split(".")[:3]) if "--short" in sys.argv else v)
