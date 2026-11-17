#!/usr/bin/env python3
"""modroles.py: module roles a Marketplace update ADDED, mapped to the app's user roles by name.

Why (cold test WM1, 2026-11-17): Atlas_Core 3 had no module roles; Atlas_Core 4 brings Atlas_Core.Administrator and
Atlas_Core.User, and its layout's language selector calls Atlas_Core.DS_Account_CurrentUser, allowed for those two only.
mxcli's update restored "0 role grant(s)" (there were none), so every page on an Atlas layout failed for every user
role: "Executing action failed for security reasons". The build was clean; only the smoke walk saw it. Company brain:
UI modules' user/administrator module roles must be mapped to the app's user roles.

Rule: only roles that are NEW in this run (absent from the original model) of a module with a 'step: <Module> <version>'
commit, and held by no user role. Such a role Mod.R goes to every user role that already holds a module role named R in
another module (Administrator holds Administration.Administrator, so it gets Atlas_Core.Administrator). No name match:
UNMATCHED, nothing granted, a person decides. The guest (anonymous) user role is never granted: GUEST, a person decides. A role the app left unmapped on purpose is never new, so never touched.

  modroles.py APP.mpr --original ORIGINAL.mpr [--mdl OUT.mdl] [--mxcli CMD]
    prints GRANT / GUEST / UNMATCHED lines and a summary; --mdl writes the ALTER USER ROLE statements (no grants: no file)
"""
import argparse, os, re, shlex, subprocess, sys


def mx(cmd, mpr, q):
    r = subprocess.run(shlex.split(cmd) + ["-p", mpr, "-c", q], capture_output=True, text=True)
    return r.stdout


def table_col(out, col=0):
    rows = []
    for ln in out.splitlines():
        if not ln.startswith("|") or set(ln) <= set("|-"):
            continue
        rows.append([c.strip() for c in ln.strip("|").split("|")][col])
    return rows[1:]  # drop the header


def module_roles(cmd, mpr):
    return {r for r in table_col(mx(cmd, mpr, "show module roles")) if "." in r}


def user_roles(cmd, mpr):
    out = {}
    for u in table_col(mx(cmd, mpr, "show user roles")):
        d = mx(cmd, mpr, f"describe user role {u}")  # "describe userrole X" is a parse error in -c
        m = re.search(r"ModuleRoles:\s*\(([^)]*)\)", d)
        out[u] = [x.strip() for x in m.group(1).split(",") if x.strip()] if m else []
    return out


def updated_modules(app_dir):
    r = subprocess.run(["git", "-C", app_dir, "log", "--format=%s"], capture_output=True, text=True)
    return {m.group(1) for m in re.finditer(r"^step: (\w+) \S+", r.stdout, re.M)}


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("mpr"); ap.add_argument("--original", required=True)
    ap.add_argument("--mdl"); ap.add_argument("--mxcli", default=os.environ.get("UPG_MXCLI_READ", "mxcli"))
    a = ap.parse_args()
    now, orig = module_roles(a.mxcli, a.mpr), module_roles(a.mxcli, a.original)
    users = user_roles(a.mxcli, a.mpr)
    held = {r for rs in users.values() for r in rs}
    moved = updated_modules(os.path.dirname(os.path.abspath(a.mpr)))
    m = re.search(r"Guest User Role:\s*(\w+)", mx(a.mxcli, a.mpr, "describe app security"))
    guest = m.group(1) if m else None
    grants, unmatched = [], []
    for r in sorted(now - orig - held):
        mod, name = r.split(".", 1)
        if mod not in moved:
            continue
        to = [u for u, rs in sorted(users.items()) if any(x.split(".", 1)[1].lower() == name.lower()
                                                          and x.split(".", 1)[0] != mod for x in rs)]
        gu = guest in to
        if gu:  # what anonymous visitors may run is a person's call
            to.remove(guest)
            print(f"GUEST {r}: the guest role {guest} holds a '{name}' role elsewhere; not granted, decide by hand")
        if to:
            for u in to:
                grants.append((u, r))
                print(f"GRANT {r} -> user role {u} (new in the {mod} update; {u} holds a '{name}' role in another module)")
        else:
            unmatched.append(r)
            gu or print(f"UNMATCHED {r}: new in the {mod} update, no user role holds a '{name}' role elsewhere; map it by hand")
    if grants and a.mdl:
        with open(a.mdl, "w") as f:
            f.write("mdl 1;\n" + "".join(f"ALTER USER ROLE {u} ADD MODULE ROLES ({r});\n" for u, r in grants))
    print(f"modroles: {len(grants)} grant(s), {len(unmatched)} unmatched new module role(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
