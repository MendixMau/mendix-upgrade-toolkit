#!/usr/bin/env python3
"""platform_drops.py: a System-module element the platform removes, approved only when the baseline holds no data in it.

Why (cold test WM1, 2026-11-17): the 9.24 -> 10.24 gate stopped on 4 RED idcheck rows, all in the System module
(System.DataBrokerEntityMetadata and its attributes, System.WorkflowActivity.IsMigrationActivity). Mendix 10 drops them;
the app cannot keep them. FSM approved the same rows by hand after counting 0 rows, and the 9-to-10 playbook says the
same. The count is the proof, so it is made here, on the baseline snapshot, and written as the reason.

Rule: only RED REMOVED rows of the System module. Entity: approved when its table has 0 rows. Attribute: approved when
its column holds 0 non-null values (or its table is gone and had 0 rows). Any other count, or a query that fails:
not approved, printed as KEEP with the count, a person decides. App and Marketplace modules are never touched here.

  platform_drops.py OLD.mda NEW.mda --approved approved.txt --psql "docker exec -i PG psql -U mendix -d DB" [--dry-run]
    appends one line per approval: '<element> # platform drop (platform_drops.py): <count> in <DB>'
"""
import argparse, os, re, shlex, subprocess, sys

B = os.path.dirname(os.path.abspath(__file__))
ROW = re.compile(r"^RED\s+REMOVED\s+(entity|attribute)\s+(System\.[\w.]+)", re.M)
TAG = "# platform drop (platform_drops.py)"


def count(psql, sql):
    r = subprocess.run(shlex.split(psql) + ["-tAc", sql], capture_output=True, text=True)
    out = r.stdout.strip()
    return int(out) if r.returncode == 0 and out.isdigit() else None


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("old"); ap.add_argument("new")
    ap.add_argument("--approved", required=True); ap.add_argument("--psql", required=True)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--idcheck-out", help="read the idcheck rows from this file instead of running idcheck.py")
    a = ap.parse_args()
    rows = open(a.idcheck_out).read() if a.idcheck_out else subprocess.run(
        [sys.executable, os.path.join(B, "idcheck.py"), a.old, a.new], capture_output=True, text=True).stdout
    have = open(a.approved).read() if os.path.exists(a.approved) else ""
    db = a.psql.split()[-1]
    new, kept = [], 0
    for kind, qn in ROW.findall(rows):
        if re.search(rf"^{re.escape(qn)}\s", have, re.M):
            continue
        parts = qn.split(".")
        table = f'"system${parts[1].lower()}"'
        if kind == "entity":
            n, what = count(a.psql, f"select count(*) from {table}"), "rows"
        else:
            n, what = count(a.psql, f'select count(*) from {table} where "{parts[2].lower()}" is not null'), "non-null values"
        if n == 0:
            new.append(f"{qn} {TAG}: Mendix removes it; 0 {what} in {db}")
            print(f"APPROVE {qn}: 0 {what} in {db}")
        else:
            kept += 1
            print(f"KEEP {qn}: {'count failed' if n is None else f'{n} {what}'} in {db}; a person decides")
    if new and not a.dry_run:
        with open(a.approved, "a") as f:
            f.write(("" if not have or have.endswith("\n") else "\n") + "\n".join(new) + "\n")
    print(f"platform_drops: {len(new)} approved by count, {kept} kept for a person")
    return 0


if __name__ == "__main__":
    sys.exit(main())
