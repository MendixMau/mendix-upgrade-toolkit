#!/usr/bin/env python3
"""cockpitcheck.py: the cockpit must never contradict itself or the run. Builds the page model exactly as cockpitpage.py does
and checks what a person reads against the run's own files.

Why (cold test WM1, 2026-11-16): the owner saw rows that said "Not approved yet" and "Test gap" with nothing to approve, a red
"waits for your answers" bar after the plan was approved and the run was going, and "2 items to decide" next to "0 for you
now". Each was a separate cockpit bug; this check makes the whole class fail a run instead of confusing a person.

Rules (each line of output names one):
  ghost-step       an undecided plan-item step (P-n alias) on the page that the current PROPOSAL.md no longer holds
  wait-no-ask      a row whose plan cell asks for an approval ("Not approved yet", "Needs your OK") while the plan is signed
                   and Blocked on you does not hold that item
  stop-no-ask      the red stop bar says the run waits for you, and Blocked on you is empty
  stop-and-running the red stop bar and the "Running now" bar at the same time
  ask-no-evidence  a plan question card that lists no element, file or finding behind it (evidence.py found nothing)
  count-mismatch   the "for you now" number differs from the Blocked on you list while the run is stopped for a person

  cockpitcheck.py --work W       prints CONSISTENT, or one line per problem; exit 0 / 1 (2 usage)
Run by: upgrade-pipeline.sh after each cockpit render (a problem is a note and a cockpit item, never a silent page), and controls.
"""
import argparse, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cockpitpage  # noqa: E402
import cockpitmatrix  # noqa: E402
import steps as stp  # noqa: E402

ASK = ("Not approved yet", "Needs your OK")


def check(work):
    model = cockpitpage.build_model(work)
    M = cockpitmatrix.build(work, model)
    out = []
    asks = cockpitmatrix.open_questions(model)
    ask_names = {re.sub(r"\s*\((module|widget|jar|java)\)$", "", i.get("title", "")) for i in asks}
    plan = cockpitpage.rd(os.path.join(work, "PROPOSAL.md")) or ""
    in_plan = set(re.findall(r"\[(P-\d+)\]", plan))
    recs, _ = stp.load(work)
    for r in recs or []:
        decided = (r.get("approval") or {}).get("state") in ("approved", "rejected")   # a module the update kept after the sign-off
        if plan and r.get("alias", "").startswith("P-") and stp.mine(r) and r["alias"] not in in_plan and not decided:
            out.append(f"ghost-step {r['id']} ({r['alias']}, {r['title']}): not in the current plan")
    signed = bool(model.get("signed"))
    for row in M["rows"]:
        c = row["cells"].get("plan") or {}
        if signed and c.get("l") in ASK and not any(n and n in row["name"] for n in ask_names):
            out.append(f"wait-no-ask {row['id']} ({row['name']}): says \"{c['l']}\" but the plan is signed and nothing asks for it")
    for i in asks:   # a question with nothing under it cannot be decided (cold test WM1: "local edits refuse the update", no list)
        if i["kind"] == "plan-choice" and not (i.get("evidence") or {}).get("what"):
            out.append(f"ask-no-evidence {i['id']} ({i['title']}): the card asks a person to decide but shows no element, file or finding")
    stopped, running = model.get("stopped"), model.get("running")
    if stopped and not asks and str(stopped.get("code")) in ("14", "15"):
        out.append("stop-no-ask the red bar says the plan waits for your answers, and Blocked on you is empty")
    if stopped and running:
        out.append(f"stop-and-running the red stop bar (exit {stopped.get('code')}) shows while the run is running")
    if stopped:
        mine = [o for o in M["band"]["open"]["items"] if o["owner"] != "agent" and o["group"] != "At deploy"]
        if len(mine) != len(asks):
            out.append(f"count-mismatch the run waits for a person: Blocked on you holds {len(asks)}, \"for you now\" says {len(mine)}")
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--work", required=True)
    a = ap.parse_args()
    if not os.path.isdir(a.work):
        print(f"cockpitcheck: no work folder {a.work}", file=sys.stderr)
        return 2
    probs = check(os.path.abspath(a.work))
    print("\n".join(probs) if probs else "CONSISTENT")
    return 1 if probs else 0


if __name__ == "__main__":
    sys.exit(main())
