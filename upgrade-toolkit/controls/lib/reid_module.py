#!/usr/bin/env python3
"""reid_module.py: give every unit of one module a new UnitID, as a delete plus re-import of the module does (NS-7).

  reid_module.py <App.mpr> <Module> [--guids]     (in place; MPR v1, run it on a copy)

--guids also gives every element of the module's domain model (entity, attribute, association) a new GUID: a real
delete and re-import, where the data goes too. Without it only the unit ids change, as mxcli's update does (WM1).

notification-service cc318c0b: the DataWidgets 2.27.6 import re-created the module, so its ModuleImpl, folder,
enumeration, security, domain model, settings and JavaScript action units all got new ids. The new ids here are
uuid5 of the old one, so the fixture is the same on every run. Units outside the module keep theirs; a ContainerID
that pointed into the module follows the new id.
"""
import sqlite3, sys, uuid

import bson

path, mod = sys.argv[1], sys.argv[2]
guids = "--guids" in sys.argv[3:]


def regen(x):
    """New GUIDs (uuid5 of the old, same BSON type) everywhere under x; the number replaced."""
    n = 0
    if isinstance(x, dict):
        for k, v in x.items():
            if k == "GUID" and isinstance(v, (bytes, bytearray)):
                b = uuid.uuid5(uuid.NAMESPACE_OID, "reguid:" + bytes(v).hex()).bytes_le
                x[k] = type(v)(b, v.subtype) if hasattr(v, "subtype") else b
                n += 1
            else:
                n += regen(v)
    elif isinstance(x, list):
        n = sum(regen(i) for i in x)
    return n
con = sqlite3.connect(path)
rows = [(bytes(u), bytes(c) if c else None, b) for u, c, b in con.execute("select UnitID, ContainerID, Contents from Unit")]
parent = {u: c for u, c, _ in rows}
root = [u for u, _, b in rows if b and bson.decode(b).get("$Type") == "Projects$ModuleImpl" and bson.decode(b).get("Name") == mod]
if len(root) != 1:
    sys.exit(f"reid_module: {mod}: {len(root)} modules of that name in {path}")
inside = set()
for u in parent:
    x, seen = u, set()
    while x is not None and x not in seen:
        if x == root[0]:
            inside.add(u); break
        seen.add(x); x = parent.get(x)
new = {u: uuid.uuid5(uuid.NAMESPACE_OID, "reid:" + u.hex()).bytes_le for u in inside}
ng = 0
if guids:
    for u, _, b in rows:
        if u in inside and b and bson.decode(b).get("$Type") == "DomainModels$DomainModel":
            d = bson.decode(b)
            ng += regen(d)
            con.execute("update Unit set Contents = ? where UnitID = ?", (bson.encode(d), u))
for u, c, _ in rows:
    nu, nc = new.get(u, u), new.get(c, c) if c else c
    if (nu, nc) != (u, c):
        con.execute("update Unit set UnitID = ?, ContainerID = ? where UnitID = ?", (nu, nc, u))
con.commit()
print(f"reid_module: {mod}: {len(inside)} units got new ids" + (f", {ng} element GUIDs new" if guids else ""))
