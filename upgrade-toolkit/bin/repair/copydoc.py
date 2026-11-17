#!/usr/bin/env python3
"""copydoc.py: copy a document a module update dropped into an own module, and point its users at the copy (repair row 28).

  copydoc.py <app dir|.mpr> --from <baseline .mpr> --doc Module.Doc --to Dest [--roles Dest.R1,Dest.R2] [--retarget] [--apply]

Why (cold CMM): Administration 2.1.2 -> 4.5.0 dropped the page UserRole_Select and the microflow RetrieveTimeZones; two
own Employee pages used them as the select page of a reference set selector and the source of a reference selector:
3 CE1613. mxcli cannot author those selectors (describe says NOT re-executable), so it cannot repoint them either.

The baseline is the same app at the same Mendix version BEFORE the update (a git commit of the converted tree, written
out with `git show <commit>:<app>.mpr > base.mpr`). The document's BSON is copied with fresh ids into module Dest (at
its top level, same name). Its allowed module roles belong to the old module: --roles names the Dest roles that
replace them (required when it had any). --retarget replaces every string that is exactly Module.Doc with Dest.Doc in
the units of the app's own (non-Marketplace) modules and lists each unit it changed.

Refusals (exit 2): different Mendix versions; the document missing in the baseline; Dest missing or not an own
module; Dest.Doc already present; a document reference inside the copy that the app does not have (copy that first);
roles needed and not given; an MPR v2 project (mprcontents: not supported yet). Dry run unless --apply; the changes
are one new unit plus one per retargeted user, so commit the app before --apply and run mx check after.
Exit: 0 = done (or the dry run shows it), 2 = refused.
"""
import argparse, base64, copy, hashlib, os, re, sqlite3, sys, uuid

import bson
from bson.binary import Binary

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from copy_mappings import Mpr  # noqa: E402

QN = re.compile(r"^[A-Za-z_]\w*\.[A-Za-z_]\w*$")
APPSTORE = ("FromAppStore", "IsThemeModule")


def die(msg):
    print(f"copydoc: REFUSED: {msg}")
    sys.exit(2)


def version(m):
    try:
        return m.con.execute("select _ProductVersion from _MetaData").fetchone()[0]
    except sqlite3.DatabaseError:
        return None


def all_docs(m):
    """qualified name -> uid for every named unit inside a module (pages, flows, snippets, enums, ...)."""
    out = {}
    for uid in m.rows:
        d = m.decode(uid)
        if d and d.get("Name") and d.get("$Type") not in ("Projects$Folder", "Projects$ModuleImpl", "Projects$Module"):
            mod = m.module_of(uid)
            if mod:
                out[f"{mod}.{d['Name']}"] = uid
    return out


def module_unit(m, name):
    for uid in m.rows:
        d = m.decode(uid)
        if d and d.get("$Type") in ("Projects$ModuleImpl", "Projects$Module") and d.get("Name") == name:
            return uid, d
    return None, None


def strings(o):
    if isinstance(o, dict):
        for v in o.values():
            yield from strings(v)
    elif isinstance(o, list):
        for v in o:
            yield from strings(v)
    elif isinstance(o, str):
        yield o


def replace_exact(o, old, new):
    n = 0
    if isinstance(o, dict):
        for k, v in o.items():
            if v == old:
                o[k] = new; n += 1
            else:
                n += replace_exact(v, old, new)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            if v == old:
                o[i] = new; n += 1
            else:
                n += replace_exact(v, old, new)
    return n


def new_ids(doc):
    """Fresh $IDs for the whole copy, and every pointer to one of them follows (a page's ControlBar.DefaultButtonPointer
    holds the $ID of its default button: renewing the button but not the pointer makes mx check die on load with
    KeyNotFoundException, cold CMM)."""
    ids = {}

    def collect(o):
        if isinstance(o, dict):
            for k, v in o.items():
                if k == "$ID" and isinstance(v, (bytes, Binary)):
                    ids[bytes(v)] = uuid.uuid4().bytes
                else:
                    collect(v)
        elif isinstance(o, list):
            for v in o:
                collect(v)

    def swap(v):
        return (Binary(ids[bytes(v)], v.subtype) if isinstance(v, Binary) else ids[bytes(v)]) \
            if isinstance(v, (bytes, Binary)) and bytes(v) in ids else v

    def remap(o):
        if isinstance(o, dict):
            for k, v in o.items():
                o[k] = swap(v) if isinstance(v, (bytes, Binary)) else remap(v)
        elif isinstance(o, list):
            for i, v in enumerate(o):
                o[i] = swap(v) if isinstance(v, (bytes, Binary)) else remap(v)
        return o

    collect(doc)
    return remap(doc), ids


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("app")
    ap.add_argument("--from", dest="base", required=True)
    ap.add_argument("--doc", required=True)
    ap.add_argument("--to", required=True)
    ap.add_argument("--roles", default="")
    ap.add_argument("--retarget", action="store_true")
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    try:
        app, base = Mpr(a.app), Mpr(a.base)
    except ValueError as e:
        die(str(e))
    if "Contents" not in app.cols or any(f for _, _, f in app.rows.values()):
        die(f"{app.path} is an MPR v2 project (mprcontents): not supported yet")
    va, vb = version(app), version(base)
    if va != vb:
        die(f"Mendix versions differ: app {va}, baseline {vb} (write the baseline out of the converted tree's git history)")
    if not QN.match(a.doc):
        die(f"--doc {a.doc}: give Module.Doc")
    src_mod, name = a.doc.split(".")
    bdocs, adocs = all_docs(base), all_docs(app)
    if a.doc not in bdocs:
        die(f"{a.doc} is not in the baseline {base.path}")
    new_qn = f"{a.to}.{name}"
    if new_qn in adocs:
        die(f"{new_qn} already exists in the app")
    muid, mod = module_unit(app, a.to)
    if muid is None:
        die(f"module {a.to} is not in the app")
    if any(mod.get(k) for k in APPSTORE) or mod.get("AppStoreVersion"):
        die(f"module {a.to} is a Marketplace module: copy into one of the app's own modules")
    doc = copy.deepcopy(base.decode(bdocs[a.doc]))
    roles = [r for r in (doc.get("AllowedModuleRoles") or [])[1:] if isinstance(r, str)]
    new_roles = [r.strip() for r in a.roles.split(",") if r.strip()]
    if roles and not new_roles:
        die(f"{a.doc} allows {', '.join(roles)}: name the {a.to} roles that replace them with --roles")
    missing = sorted({s for s in strings(doc) if QN.match(s) and s.split(".")[0] not in ("System",)
                      and s in bdocs and s not in adocs and s != a.doc})
    if missing:
        die(f"{a.doc} uses {', '.join(missing)}, which the app does not have: copy those first")
    if roles:
        doc["AllowedModuleRoles"] = [doc["AllowedModuleRoles"][0]] + new_roles
    doc, ids = new_ids(doc)
    nid = bytes(doc["$ID"])
    blob = bson.encode(doc)
    users = []
    if a.retarget:
        for uid in app.rows:
            d = app.decode(uid)
            if not d or not any(s == a.doc for s in strings(d)):
                continue
            mname = app.module_of(uid)
            _, md = module_unit(app, mname) if mname else (None, None)
            if md is None or any(md.get(k) for k in APPSTORE) or md.get("AppStoreVersion"):
                continue
            d2 = copy.deepcopy(d)
            n = replace_exact(d2, a.doc, new_qn)
            users.append((uid, f"{mname}.{d.get('Name')}", n, bson.encode(d2)))
    print(f"copydoc: {a.doc} ({doc.get('$Type')}) -> {new_qn}" + (f", roles {', '.join(roles)} -> {', '.join(new_roles)}" if roles else ""))
    for _, qn, n, _ in users:
        print(f"  RETARGET {qn}: {n} reference(s) {a.doc} -> {new_qn}")
    if a.retarget and not users:
        print(f"  no own unit uses {a.doc}")
    if not a.apply:
        print("dry run: nothing written (--apply writes it)")
        return 0
    h = lambda b: base64.b64encode(hashlib.sha256(b).digest()).decode()
    cols = ["UnitID", "ContainerID", "ContainmentName", "TreeConflict", "ContentsHash", "ContentsConflicts", "Contents"]
    have = [c for c in cols if c in app.cols]
    vals = {"UnitID": nid, "ContainerID": muid, "ContainmentName": "Documents", "TreeConflict": 0,
            "ContentsHash": h(blob), "ContentsConflicts": "", "Contents": blob}
    app.con.execute(f"insert into Unit ({', '.join(have)}) values ({', '.join('?' * len(have))})", [vals[c] for c in have])
    app.con.commit()
    for uid, qn, n, b in users:
        app.write(uid, b)
    back = Mpr(app.path)
    copied = back.decode(nid) or {}
    dangling = []

    def ptrs(o, p=""):
        if isinstance(o, dict):
            for k, v in o.items():
                if k.endswith("Pointer") and isinstance(v, (bytes, Binary)) and bytes(v) not in seen:
                    dangling.append(p + "/" + k)
                elif not isinstance(v, (bytes, Binary)):
                    ptrs(v, p + "/" + k)
        elif isinstance(o, list):
            for i, v in enumerate(o):
                ptrs(v, f"{p}[{i}]")

    seen = set()

    def allids(o):
        if isinstance(o, dict):
            for k, v in o.items():
                if k == "$ID":
                    seen.add(bytes(v))
                else:
                    allids(v)
        elif isinstance(o, list):
            for v in o:
                allids(v)
    allids(copied); ptrs(copied)
    for x in dangling:
        print(f"  DANGLING pointer {x}: points at no element of the copy")
    ok = not dangling and new_qn in all_docs(back) and all(not any(s == a.doc for s in strings(back.decode(u))) for u, _, _, _ in users)
    print(f"copydoc: written, re-read {'OK' if ok else 'MISMATCH'}; run mx check now")
    return 0 if ok else 2


if __name__ == "__main__":
    sys.exit(main())
