#!/usr/bin/env python3
"""repoint_images.py: images a module moved between its image collections (repair row 38, CE1613).

  repoint_images.py <app dir|.mpr> (--log check.log | --image Module.Coll.Name ...) [--apply]

Why (field run GF-38): a Marketplace module update moved its images from the collection `Images` into
`Restricted_Images` / `Universal_Images` / `Dummy_Images`, same names. Own pages kept the old three-part name
`Module.Images.Logo`; 54 of 85 CE1613 ("the selected image no longer exists") were exactly this. mxcli cannot rewrite an
image reference on a page, so it was rewritten in the BSON.

Input: the missing names, either as the CE1613 lines of a mx check log (--log: only the quoted name of an image message,
`The selected image 'Module.Coll.Name' no longer exists.`, is taken; the same CE1613 code also reports attributes,
enumerations, pages and microflows, and those lines are skipped even when their name has three parts) or named with
--image (repeatable). For each name the app's module Module must hold exactly ONE image collection that has
an image called Name: every string equal to `Module.Coll.Name` in an OWN unit becomes `Module.NewColl.Name`.
  REPOINT   one collection holds it now: the rewrite (units and counts are listed)
  LEFT      the name is still there (nothing is missing), the module is not in the app, no collection holds the name,
            or two or more do: left alone and the reason is printed (a person picks the collection)
Own units = units of modules that are not Marketplace modules (FromAppStore / IsThemeModule / AppStoreVersion), and never
the units of the module the images moved in. Marketplace modules are never edited.

Dry run unless --apply; commit the app before --apply, then run mx check. A unit is written only when its BSON re-encodes
byte for byte before the change and the rewritten unit is read back with no old name left; otherwise the unit is
REFUSED (exit 2) and nothing else is changed. ContentsHash is updated (MPR v1 Contents and v2 mprcontents).
Exit: 0 = done (or nothing to do), 2 = input error or unsafe unit.
"""
import argparse, copy, os, re, sys

import bson

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from copy_mappings import Mpr  # noqa: E402
from copydoc import module_unit, replace_exact, strings, APPSTORE  # noqa: E402

IMG = re.compile(r"selected image '([A-Za-z_]\w*\.[A-Za-z_]\w*\.[A-Za-z_]\w*)'")


def names_from_log(path):
    out = []
    for line in open(path, errors="replace"):
        if "CE1613" not in line:
            continue
        for m in IMG.finditer(line):
            qn = m.group(1)
            if qn not in out:
                out.append(qn)
    return out


def collections(m):
    """{module: {collection name: set(image names)}} for every Images$ImageCollection of the app."""
    out = {}
    for uid in m.rows:
        d = m.decode(uid)
        if not d or d.get("$Type") != "Images$ImageCollection" or not d.get("Name"):
            continue
        mod = m.module_of(uid)
        if mod:
            imgs = {i.get("Name") for i in (d.get("Images") or []) if isinstance(i, dict)}
            out.setdefault(mod, {})[d["Name"]] = imgs
    return out


_OWN = {}


def is_own(m, mod):
    key = (id(m), mod)
    if key not in _OWN:
        _, md = module_unit(m, mod) if mod else (None, None)
        _OWN[key] = md is not None and not any(md.get(k) for k in APPSTORE) and not md.get("AppStoreVersion")
    return _OWN[key]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("project")
    ap.add_argument("--log")
    ap.add_argument("--image", action="append", default=[])
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    try:
        m = Mpr(a.project)
        wanted = list(a.image) + (names_from_log(a.log) if a.log else [])
    except (ValueError, OSError) as e:
        print(f"repoint_images: {e}")
        return 2
    if not a.log and not a.image:
        print("repoint_images: give --log <check log> or --image Module.Coll.Name")
        return 2
    colls = collections(m)
    plan = {}   # old qn -> new qn
    for qn in dict.fromkeys(wanted):
        parts = qn.split(".")
        if len(parts) != 3:
            print(f"LEFT {qn}: not a Module.Collection.Image name")
            continue
        mod, coll, name = parts
        have = colls.get(mod)
        if have is None:
            print(f"LEFT {qn}: module {mod} has no image collection in the app")
        elif name in have.get(coll, ()):
            print(f"LEFT {qn}: the image is still in {mod}.{coll} (nothing is missing)")
        else:
            holders = sorted(c for c, imgs in have.items() if name in imgs)
            if len(holders) == 1:
                plan[qn] = f"{mod}.{holders[0]}.{name}"
            elif holders:
                print(f"LEFT {qn}: {name} is in {len(holders)} collections of {mod} ({', '.join(holders)}); pick one by hand")
            else:
                print(f"LEFT {qn}: no collection of {mod} holds an image called {name}")
    todo, n = [], 0
    for uid in sorted(m.rows):
        d = m.decode(uid)
        mod = m.module_of(uid)
        if not d or not mod or not is_own(m, mod):
            continue
        hit = {o for o in plan if any(s == o for s in strings(d))}
        # never the units of the module the images moved in
        hit = {o for o in hit if o.split(".")[0] != mod}
        if not hit:
            continue
        if bson.encode(d) != m.rows[uid][1]:
            print(f"REFUSED {mod}.{d.get('Name')}: its unit does not re-encode byte for byte; not edited (report it with the Mendix version)")
            return 2
        d2 = copy.deepcopy(d)
        cnt = {o: replace_exact(d2, o, plan[o]) for o in sorted(hit)}
        if any(s == o for o in hit for s in strings(d2)):
            print(f"REFUSED {mod}.{d.get('Name')}: an old name is left after the rewrite; not edited")
            return 2
        todo.append((uid, f"{mod}.{d.get('Name') or d.get('$Type')}", cnt, bson.encode(d2)))
    for _, qn, cnt, _ in todo:
        for o, c in cnt.items():
            print(f"REPOINT {qn}: {c} x {o} -> {plan[o]}")
            n += c
    used = {o for _, _, cnt, _ in todo for o in cnt}
    for o in plan:
        if o not in used:
            print(f"LEFT {o}: no own unit uses it")
    tail = ("written" if a.apply else "dry run, rerun with --apply (commit the app first), then mx check") if todo else "nothing to write"
    if a.apply:
        for uid, _, _, b in todo:
            m.write(uid, b)
        back = Mpr(m.path)
        for uid, qn, cnt, _ in todo:
            if any(s == o for o in cnt for s in strings(back.decode(uid) or {})):
                print(f"REFUSED {qn}: read back with an old name left")
                return 2
    print(f"repoint_images: {n} reference(s) in {len(todo)} unit(s); {tail}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
