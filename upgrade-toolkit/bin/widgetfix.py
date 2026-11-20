#!/usr/bin/env python3
"""widgetfix.py: the person's question behind a WIDGET-DROP stop, in words a reader can answer, with the fix the toolkit can name.

  widgetfix.py <app dir | app.mpr> --drops widgetdrop.json --plan plan.txt --target 10.24.0
               [--modules FILE] [--versions FILE]   (env UPG_WIDGETFIX_MODULES / _VERSIONS: the same, for the controls) [--cache DIR] [--no-download] [--mxcli CMD]

Why (run DVS, 10.9 -> 10.24): the stop said "Widget settings would be dropped: the installed widget package is older
than the pages ... No recommendation: this one is your call". It named no module and no version, said nothing about what users
lose (7 data grids forget the column layout people saved, a combo box loses its read-only look), offered "Update the module that
ships the widget" although the toolkit knew DataWidgets 2.32.4 fits Mendix 10.24, and its options were agent instructions
("Before the build." / "Create widgetdrop-ack.txt."). Choosing "update" also did nothing: a person wrote the plan line by hand.

Reads widgetdrop.py's --json (one object per widget instance: document, widget, id, drops [[key, value]]), finds the module that
ships those widgets (the Marketplace package name in missing_deps.PLATFORM_WIDGETS matched to an installed module, e.g. "Data
Widgets" -> DataWidgets), asks `mxcli marketplace versions <content id>` for the newest version of the SAME major whose minimum
Mendix is at or below the target and which is newer than the installed one and the plan's, and, when the package is in the cache or
can be downloaded, keeps only a version that really declares the dropped settings (never promises more than the package has: DataWidgets
2.32.4 declares the Data grid's configurationStorageType but not the standalone Combobox's readOnlyStyle).

Prints, for upgrade-pipeline.sh to turn into the stop (nj_meta person ...), one field per line, tab separated:
  Q<TAB>question   R<TAB>recommended key, or none:<why it is the reader's call>   O<TAB>key|label|what the reader notices and what the run does
  W<TAB>key|file|line   what answering key writes into the work folder (decisions.py apply)   B<TAB>one line of the stop's body
Exit: 0 = fields printed, 2 = input error. Producer of --drops: step_update (`widgetdrop.py --json`), the mandatory step before this.
"""
import argparse, glob, io, json, os, re, shutil, subprocess, sys, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "repair"))
sys.path.insert(0, HERE)
from missing_deps import PLATFORM_WIDGETS, norm  # noqa: E402

# what a reader notices when this setting is lost; anything else is said with its key
SAYS = {"configurationStorageType": "forget the column layout people saved",
        "readOnlyStyle": "lose the read-only look"}
NAMES = {"datagrid": "data grid", "gallery": "gallery", "combobox": "combo box", "treenode": "tree node", "dropdownsort": "sort drop-down"}


def vt(v):
    return tuple(int(x) for x in re.findall(r"\d+", str(v or ""))[:4])


def kind(wid):
    last = wid.rsplit(".", 1)[-1].lower()
    if last in NAMES:
        return NAMES[last]
    if last.startswith("datagrid") and last.endswith("filter"):
        return "grid filter"
    return re.sub(r"(?<=[a-z])(?=[A-Z])", " ", wid.rsplit(".", 1)[-1]).lower()


def plural(name, n):
    if n == 1:
        return name
    return name[:-1] + "ies" if name.endswith("y") else name + "s"


def package_of(wid):
    """The Marketplace package name that ships a platform widget, or ''."""
    parts = wid.lower().split(".")
    return PLATFORM_WIDGETS.get(parts[-2], "") if len(parts) >= 5 else ""


def read_modules(app, path):
    if path:
        return json.load(open(path))
    mprs = [app] if os.path.isfile(app) else glob.glob(os.path.join(app, "*.mpr"))
    if len(mprs) != 1:
        return []
    try:
        import localedits
        return localedits.modules(mprs[0])
    except Exception:
        return []


def versions(cid, path, mxcli):
    """[(version, min mendix)] from `mxcli marketplace versions <cid>` (or its captured output in `path`), newest first."""
    try:
        if path:
            out = open(path, encoding="utf-8").read()
        else:
            out = subprocess.run(mxcli + ["marketplace", "versions", str(cid)], capture_output=True, text=True, timeout=120).stdout
    except (OSError, subprocess.TimeoutExpired):
        return None
    rows = [(m.group(1), m.group(2)) for m in re.finditer(r"^(\d+(?:\.\d+)+)\s+(\d+(?:\.\d+)+)\s", out, re.M)]
    return rows or None


def declared(mpk):
    """{widget id: set of property keys} of every widget package inside a module package (widgets/*.mpk)."""
    out = {}
    try:
        z = zipfile.ZipFile(mpk)
        for n in z.namelist():
            if not re.match(r"widgets/[^/]+\.mpk$", n):
                continue
            inner = zipfile.ZipFile(io.BytesIO(z.read(n)))
            for m in inner.namelist():
                if m.endswith(".xml") and not m.endswith("package.xml"):
                    x = inner.read(m).decode("utf-8", "replace")
                    i = re.search(r'<widget\b[^>]*\bid="([^"]+)"', x)
                    if i:
                        out[i.group(1)] = set(re.findall(r'<property\b[^>]*\bkey="([^"]+)"', x))
    except (OSError, zipfile.BadZipFile):
        return None
    return out


def package(cid, ver, cache, download, mxcli):
    f = os.path.join(cache, f"{cid}-{ver}.mpk")
    if not os.path.isfile(f) and download:
        os.makedirs(cache, exist_ok=True)
        try:
            subprocess.run(mxcli + ["marketplace", "download", str(cid), "--version", ver, "-o", f], capture_output=True, text=True, timeout=300)
        except (OSError, subprocess.TimeoutExpired):
            pass
    return declared(f) if os.path.isfile(f) else None


def plan_versions(path):
    out = {}
    try:
        for ln in open(path, encoding="utf-8"):
            p = ln.split("#")[0].split()
            if len(p) >= 3:
                out[p[2]] = max(out.get(p[2], ()), vt(p[1]))
    except OSError:
        pass
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("app"); ap.add_argument("--drops", required=True); ap.add_argument("--plan", default=""); ap.add_argument("--target", default="")
    ap.add_argument("--modules", default=os.environ.get("UPG_WIDGETFIX_MODULES")); ap.add_argument("--versions", default=os.environ.get("UPG_WIDGETFIX_VERSIONS")); ap.add_argument("--no-download", action="store_true")
    ap.add_argument("--cache", default=os.environ.get("UPG_CACHE") or os.path.expanduser("~/.cache/upgrade-toolkit/mpk"))
    ap.add_argument("--mxcli", default=os.environ.get("UPG_MXCLI") or shutil.which("mxcli") or os.path.expanduser("~/.local/bin/mxcli"))
    a = ap.parse_args()
    try:
        found = json.load(open(a.drops, encoding="utf-8"))
    except (OSError, ValueError) as e:
        print(f"widgetfix: cannot read {a.drops}: {e}", file=sys.stderr); return 2
    if not found:
        print("widgetfix: no drops", file=sys.stderr); return 2
    mxcli = a.mxcli.split()

    # what people lose, counted per kind of widget and setting
    lost = {}   # (phrase, widget kind) -> instances
    for f in found:
        for key, _v in f["drops"]:
            k = (SAYS.get(key) or f"lose the setting {key}", kind(f["id"]))
            lost[k] = lost.get(k, 0) + 1
    items = [f"{n} {plural(w, n)} would {p}" for (p, w), n in sorted(lost.items(), key=lambda kv: (-kv[1], kv[0]))]
    inst = len(found)

    # the module that ships them
    pk = {package_of(f["id"]) for f in found} - {""}
    mods = read_modules(a.app, a.modules)
    mod = next((m for m in mods if len(pk) == 1 and norm(m.get("name")) == norm(next(iter(pk)))), None)
    fit = None
    if mod and mod.get("cid"):
        rows = versions(mod["cid"], a.versions, mxcli) or []
        inst_v, planned = vt(mod.get("version")), plan_versions(a.plan).get(mod["name"], ())
        target = vt(a.target)[:3]
        for ver, mn in sorted(rows, key=lambda r: vt(r[0]), reverse=True):
            if inst_v and vt(ver)[0] != inst_v[0]:
                continue   # a major version is a bigger change than this stop may decide for the person
            if vt(ver) <= max(inst_v, planned, ()) or (target and vt(mn)[:3] > target):
                continue
            have = package(mod["cid"], ver, a.cache, not a.no_download, mxcli)
            fixed = [f for f in found if have is None or all(k in have.get(f["id"], ()) for k, _ in f["drops"])]
            if have is not None and not fixed:
                continue
            fit = {"ver": ver, "min": mn, "fixed": fixed, "checked": have is not None}
            break

    first = items[0][0].upper() + items[0][1:]
    more = f", and {len(items) - 1} more kind{'s' if len(items) > 2 else ''} of loss" if len(items) > 1 else ""
    q = f"{first}{more}."
    modname = mod["name"] if mod else ""
    if fit:
        left = [f for f in found if f not in fit["fixed"]]
        print(f"Q\t{q} Update {modname} to {fit['ver']} first?")
        print("R\tupdate")
        keep = (f"Users keep what they saved on {len(fit['fixed'])} of the {inst} widgets." if fit["checked"] else
                "The package could not be checked here, so what users keep is not promised.") + (
            f" The other {len(left)} ({', '.join(sorted({kind(f['id']) for f in left}))}) {'is' if len(left) == 1 else 'are'} not in this package and still lose{'s' if len(left) == 1 else ''} the setting; the run asks once more." if left and fit["checked"] else "")
        print(f"O\tupdate|Update {modname} to {fit['ver']}|{keep} The run adds {modname} {fit['ver']} to the module plan and updates it when it goes on.")
        print(f"O\taccept|Go on without updating|Users notice it: {'; '.join(items)}. Your name is recorded with the answer; the build goes on.")
        print(f"W\tupdate|plan.txt|{mod['cid']} {fit['ver']} {modname}")
        why = (f"{modname} {fit['ver']} (Marketplace {mod['cid']}, Mendix {fit['min']} or newer) is the newest version that fits Mendix {a.target or 'the target'}"
               + (" and has these settings." if fit["checked"] else "."))
    else:
        print(f"Q\t{q} What should we do?")
        if mod:
            reason = f"No newer {modname} fits Mendix {a.target or 'the target'} and has these settings, so no update brings them back."
        elif pk:
            reason = f"None of the installed modules ships {sorted(pk)[0]}, so the toolkit cannot name an update."
        else:
            reason = "These widgets are not from a package the toolkit knows, so it cannot name an update."
        print(f"R\tnone:{reason} Only you know whether losing them matters.")
        print(f"O\taccept|Go on and lose them|Users notice it: {'; '.join(items)}. Your name is recorded with the answer; the build goes on.")
        if pk and not mod:
            pkg = sorted(pk)[0]
            print(f"O\tfix|Install {pkg} yourself first|The run stays paused. Install the missing widget module: mxcli marketplace search \"{pkg}\", then mxcli marketplace download <id> --version <a version whose minimum Mendix fits {a.target or 'the target'}> -o <folder>/ and mxcli marketplace install --file <folder>/<file>.mpk, delete the .mpk, and rerun from the update step.")
        else:
            print("O\tfix|Update the widget yourself first|The run stays paused. Update the widget package (a newer widget or module version), then rerun from the update step.")
        why = reason
    print(f"W\taccept|widgetdrop-ack.txt|accepted: {'; '.join(items)}")
    print(f"B\tThe pages were saved with newer widgets than the installed ones. If the build goes on, users lose settings on {inst} widget{'s' if inst != 1 else ''}: {'; '.join(items)}.")
    print(f"B\t{why}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
