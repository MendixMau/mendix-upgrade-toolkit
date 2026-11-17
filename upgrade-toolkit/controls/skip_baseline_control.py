#!/usr/bin/env python3
"""skip_baseline_control.py DIR: run_journeys --skip-baseline-fail picks, on a fake journey set. Prints the skipped and the
walked ids. A set with data passes: the failing consumer (a _path_needs journey) is skipped, the failing creator still runs,
a passing one runs. A set without data passes: every journey that failed on the old app is skipped."""
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "bin"))
import run_journeys as rj  # noqa: E402

t = Path(sys.argv[1])


def mk(d, jid, needs):
    p = t / d / "journeys" / "User"
    p.mkdir(parents=True, exist_ok=True)
    j = {"id": jid, "role": "User", "steps": []}
    if needs:
        j["_path_needs"] = ["a row in a list"]
    (p / f"{jid}.journey.json").write_text(json.dumps(j))


(t / "b.json").write_text(json.dumps({"journeys": {"make-User": {"verdict": "FAIL"}, "use-User": {"verdict": "FAIL"},
                                                   "ok-User": {"verdict": "PASS"}}}))
mk("w", "make-User", False); mk("w", "use-User", True); mk("w", "ok-User", True)
mk("n", "make-User", False); mk("n", "ok-User", False)
sw = rj.baseline_fail_skips(t / "w" / "journeys", t / "b.json")
sn = rj.baseline_fail_skips(t / "n" / "journeys", t / "b.json")
walked = [rj.read_journey(f)["id"] for _, _, _, fs in rj.data_waves(t / "w" / "journeys", str(t / "w"), None, sw) for f in fs]
print("waves skip:", " ".join(f"{k}={v[0]}/{v[1]}" for k, v in sorted(sw.items())))
print("waves walked:", " ".join(sorted(walked)))
print("no-waves skip:", " ".join(sorted(sn)))
