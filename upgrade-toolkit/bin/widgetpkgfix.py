#!/usr/bin/env python3
"""widgetpkgfix.py: what a module step must do about widgets/*.mpk that the import leaves wrong (GF-41, GF-43).

  widgetpkgfix.py restore APP --module M --new-version V --package PKG.mpk (--old-version V | --prev PREV_MPR)
  widgetpkgfix.py defs APP

restore (GF-41): a step to a LOWER module version leaves the newer widgets/*.mpk the module's earlier version brought
  (field run GF: MxDock 12.0.0 -> 10.0.0 put the 10.0.0 model back and kept the 12.0.0 widget package, 20 957 bytes
  against 9 053; update-widgets then bound the widget to 12's properties and mx check had 2 CE1613). The package's own
  widgets/*.mpk go back over a widget the working copy holds in a NEWER version, but only a widget the module's own
  earlier step brought: the commit "step: <module> <old> ..." changed it and nothing has changed it since. A shared widget
  the app upgraded itself (or another step did) is left alone. Upgrades are never touched.
    WIDGET-RESTORED widgets/x.mpk <name> 12.0.0 -> 10.0.0 (the package's own, <module> 12.0.0 -> 10.0.0)
    WIDGET-NOT-RESTORED <reason>      (a downgrade whose package is not in the cache or unreadable, or a newer widget the
                                       module's earlier step did not bring: left as it is, compare by hand)
defs (GF-43): mxcli keeps a definition of every widget it described in APP/.mxcli/widgets/<name>.def.json and does not
  re-key it by package version, so `mxcli check` judged 10.0.0's own properties against 12's. The cached def of every
  widget package the working copy changed against HEAD (widgetdiff.py's set) is MOVED (with its templateFile, if the def
  names one) to .stepupdate/saved/mxcli-widgets/; mxcli writes a fresh one. Project-scope defs can be hand-written, so
  nothing is deleted.
    WIDGET-DEF-DROPPED .mxcli/widgets/x.def.json (widget id ...) moved to .stepupdate/saved/mxcli-widgets/
Exit: 0 always for what it judged, 2 = input error.
"""
import argparse, glob, io, json, os, re, shutil, sqlite3, subprocess, sys, zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from widgetdiff import meta  # noqa: E402


def vtuple(v):
    return tuple(int(x) for x in re.findall(r"\d+", v or ""))


def widget_ids(data):
    """Widget ids (<widget id="...">) of the XML files an .mpk's package.xml lists."""
    ids = []
    try:
        with zipfile.ZipFile(io.BytesIO(data)) as z:
            px = z.read("package.xml").decode("utf-8", "replace")
            for p in re.findall(r'<widgetFile\b[^>]*\bpath="([^"]+)"', px):
                try:
                    x = z.read(p).decode("utf-8", "replace")
                except KeyError:
                    continue
                ids += re.findall(r'<widget\b[^>]*\bid="([^"]+)"', x)
    except Exception:
        pass
    return ids


def old_version(a):
    if a.old_version:
        return a.old_version
    if a.prev:
        try:
            import mprmodel
            return mprmodel.Model.load(a.prev).modules[a.module].get("version") or ""
        except (ImportError, OSError, KeyError, ValueError, AttributeError, TypeError, sqlite3.Error):
            return ""
    return ""


def own_widgets(app, module, old):
    """{path: blob} of the widgets/*.mpk the commit "step: <module> <old> ..." changed against its parent, or None when no such commit
    is found. A widget is the module's own only if that commit changed it (the module brought it); whether it is still that blob is
    asked of the working copy by the caller."""
    git = lambda *x, text=True: subprocess.run(["git", "-C", app, *x], capture_output=True, text=text)
    if git("rev-parse", "--verify", "--quiet", "HEAD^{commit}").returncode != 0:
        return None
    prefix = git("rev-parse", "--show-prefix").stdout.strip()
    head = f"step: {module} {old} "
    for ln in git("log", "--format=%H%x09%s").stdout.splitlines():
        sha, _, subj = ln.partition("\t")
        if not subj.startswith(head):
            continue
        out = {}
        for row in git("diff-tree", "-r", "--no-commit-id", "--name-only", "--no-renames", "--root", sha, "--", f"{prefix}widgets/").stdout.splitlines():
            b = git("show", f"{sha}:{row}", text=False)
            if row.endswith(".mpk") and b.returncode == 0:
                out[row[len(prefix):]] = b.stdout
        return out
    return None


def restore(a):
    app = os.path.abspath(a.app)
    ov, nv = old_version(a), a.new_version
    if not ov:
        return   # the installed version is not recorded (no step commit, no AppStoreVersion): nothing says this step lowered it
    if not (vtuple(nv) and vtuple(nv) < vtuple(ov)):
        return
    if not a.package or not os.path.isfile(a.package):
        print(f"WIDGET-NOT-RESTORED {a.module} {ov} -> {nv} is a downgrade and the package is not in the cache ({a.package or 'no content id'}): "
              f"the widgets/*.mpk of {ov} may remain; compare widgets/ with the {nv} package by hand")
        return
    try:
        z = zipfile.ZipFile(a.package)
    except Exception as e:
        print(f"WIDGET-NOT-RESTORED {os.path.basename(a.package)} cannot be read ({e}); widgets/ not compared")
        return
    own_set = own_widgets(app, a.module, ov)
    for n in sorted(z.namelist()):
        if not (n.startswith("widgets/") and n.endswith(".mpk")) or n.count("/") != 1:
            continue
        dst = os.path.join(app, n)
        if not os.path.isfile(dst):
            continue
        own = z.read(n)
        cur = open(dst, "rb").read()
        if cur == own:
            continue
        (cn, cv), (pn, pv) = meta(cur), meta(own)
        if vtuple(cv) > vtuple(pv):
            if own_set is None or own_set.get(n) != cur:
                print(f"WIDGET-NOT-RESTORED {n} {cn if cn != '?' else pn} {cv} stays: "
                      + (f"the {a.module} {ov} step did not bring this file as it is now (the app or another step set it)" if own_set is not None
                         else f"no 'step: {a.module} {ov} ...' commit is in the git log to show the module brought it")
                      + f"; the {nv} package holds {pv}, compare by hand")
                continue
            open(dst, "wb").write(own)
            print(f"WIDGET-RESTORED {n} {pn if pn != '?' else cn} {cv} -> {pv} (the package's own, {a.module} {ov} -> {nv})")


def defs(a):
    app = os.path.abspath(a.app)
    git = lambda *x, text=True: subprocess.run(["git", "-C", app, *x], capture_output=True, text=text)
    if git("rev-parse", "--verify", "--quiet", "HEAD^{commit}").returncode != 0:
        print("widgetpkgfix: no HEAD commit in " + app, file=sys.stderr); sys.exit(2)
    rows = [ln.split("\t", 1) for ln in git("diff", "--relative", "--name-status", "--no-renames", "HEAD", "--", "widgets/").stdout.splitlines() if "\t" in ln]
    rows += [["A", p] for p in git("ls-files", "--others", "--exclude-standard", "--", "widgets/").stdout.splitlines() if p]
    prefix = git("rev-parse", "--show-prefix").stdout.strip()
    ids = set()
    for _, p in rows:
        if not p.endswith(".mpk"):
            continue
        if os.path.isfile(os.path.join(app, p)):
            ids.update(widget_ids(open(os.path.join(app, p), "rb").read()))
        old = git("show", f"HEAD:{prefix}{p}", text=False)
        if old.returncode == 0:
            ids.update(widget_ids(old.stdout))
    if not ids:
        return
    for f in sorted(glob.glob(os.path.join(app, ".mxcli", "widgets", "*.def.json"))):
        try:
            d = json.load(open(f))
            wid = d.get("widgetId")
        except Exception:
            continue
        if wid in ids:
            keep = os.path.join(app, ".stepupdate", "saved", "mxcli-widgets"); os.makedirs(keep, exist_ok=True)
            tf = d.get("templateFile") if isinstance(d, dict) else None
            moved = [f]
            if isinstance(tf, str) and tf and not os.path.isabs(tf) and ".." not in tf.split("/"):
                t = os.path.join(os.path.dirname(f), tf)
                if os.path.isfile(t):
                    moved.append(t)
            for m in moved:
                dst = os.path.join(keep, os.path.basename(m)); n = 1
                while os.path.exists(dst):  # never overwrite: the first copy (maybe hand-written) stays; later ones get .2, .3
                    n += 1; dst = os.path.join(keep, f"{os.path.basename(m)}.{n}")
                shutil.move(m, dst)
            print(f"WIDGET-DEF-DROPPED .mxcli/widgets/{os.path.basename(f)} (widget id {wid}: a step changed its package; mxcli describes it afresh) "
                  f"moved with {len(moved) - 1} template file(s) to .stepupdate/saved/mxcli-widgets/")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("restore"); r.add_argument("app"); r.add_argument("--module", required=True)
    r.add_argument("--new-version", required=True); r.add_argument("--package", default="")
    r.add_argument("--old-version", default=""); r.add_argument("--prev", default="")
    d = sub.add_parser("defs"); d.add_argument("app")
    a = ap.parse_args()
    restore(a) if a.cmd == "restore" else defs(a)


if __name__ == "__main__":
    main()
