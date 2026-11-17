#!/usr/bin/env python3
"""test_runs_control.py DIR CASE: cockpitmatrix.test_runs on a fake work folder, the Test stage's "what ran, on the old and
the new app" table. Prints one line per row and per listed test. Cases:
  both   both apps walked: a journey that passed on the old app only is counted and listed
  stale  the new app's journeys file is older than the old app's (a rerun that has not walked the new app yet)"""
import json
import os
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "bin"))
import cockpitmatrix as cm  # noqa: E402

w, case = sys.argv[1], sys.argv[2]


def put(rel, obj):
    p = os.path.join(w, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w") as f:
        json.dump(obj, f)
    return p


for sd, v in (("before", "PASS"), ("after", "PASS")):
    put(f"smoke-{sd}.json", {"roles": [{"role": "User", "steps": [{"caption": "Orders", "verdict": v}]}]})
old = put("e2e-before-picked/before-picked/summary.json", {"journeys": {"a-User": {"verdict": "PASS"}, "b-User": {"verdict": "PASS"}}})
new = put("e2e-after/after/summary.json", {"journeys": {"a-User": {"verdict": "PASS"}, "b-User": {"verdict": "FAIL"}}})
t0 = os.path.getmtime(old)
os.utime(new, (t0 - 3600, t0 - 3600) if case == "stale" else (t0 + 60, t0 + 60))
with open(os.path.join(w, "data.out"), "w") as f:
    f.write("INVALID 0 | FAIL 0 | REVIEW 0 | PASS* 1 | PASS 9 | INFO 2\n")
r = cm.test_runs(w)
for row in r["rows"]:
    print("row: " + " | ".join(row))
for k, l in r["lists"].items():
    for t in l:
        print(f"list {k}: " + " | ".join(t))
