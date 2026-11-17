#!/usr/bin/env python3
"""parked.py: Interview mode auto: the judgment stops a run parked, compiled into one grouped list for a person.

Why (WM1 cold test 2026-11-17): every judgment stop ended the run, so a person answered one question, reran, and met the
next: 16 stops on one app, most of them with a recommendation the person then took. In auto mode the pipeline parks a stop
that nothing after it depends on (journeys, idcheck, smoke walk, diff, gate) in <work>/parked/<step>.md and goes on; a build
or start failure, a missing plan or a replay that cannot be undone still ends the run at once. At the end this script
prints every parked item in one list, grouped by kind, so the person answers them in one round and one rerun applies them.

  parked.py report --work W --steps "fetch triage ..." [--also DIR]   (--also: the parked/ of rung 1, read first)

A parked file holds blocks, each opened by a line `<!-- park exit N step S -->` and the nj_add text after it. Output: the
grouped markdown on stdout; the last line `first: N S DIR` names the first parked block in step order (rung 1 first): the
exit code of the run and the step to rerun from. Exit 1 when nothing is parked (no output).
"""
import argparse, os, re, sys

OPEN = re.compile(r"^<!-- park exit (\d+) step (\S+) -->$")
KINDS = [("13", "Modules and data"), ("11", "Journeys"), ("12", "Screens, comparisons and the gate")]


def blocks(d, steps):
    out = []
    for s in steps:
        p = os.path.join(d, s + ".md")
        if not os.path.isfile(p):
            continue
        cur = None
        for ln in open(p, encoding="utf-8", errors="replace").read().splitlines():
            m = OPEN.match(ln)
            if m:
                cur = {"code": m.group(1), "step": m.group(2), "dir": d, "text": []}
                out.append(cur)
            elif cur is not None:
                cur["text"].append(ln)
    return out


def assumed(work):
    p = os.path.join(work, "DECISIONS.md")
    return [ln for ln in open(p, encoding="utf-8", errors="replace").read().splitlines() if "ASSUMED" in ln] if os.path.isfile(p) else []


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("report")
    r.add_argument("--work", required=True); r.add_argument("--steps", required=True); r.add_argument("--also")
    a = ap.parse_args()
    steps = a.steps.split()
    rung = lambda d: "rung 1" if a.also and d == a.also else "this rung" if a.also else ""
    bl = (blocks(a.also, steps) if a.also else []) + blocks(os.path.join(a.work, "parked"), steps)
    if not bl:
        return 1
    print(f"# NEEDS JUDGMENT: {len(bl)} parked item(s) (Interview mode: auto), answer them in one round\n")
    print("The run went on past each of these; nothing below is passed. Decide each in writing (the allow/approved/ack files")
    print("its text names, or the cockpit page), then rerun once from the step named in the last line.\n")
    for code, title in KINDS + [(c, f"Other (exit {c})") for c in sorted({b["code"] for b in bl} - {k for k, _ in KINDS})]:
        group = [b for b in bl if b["code"] == code]
        if not group:
            continue
        print(f"# {title}: {len(group)}\n")
        for b in group:
            where = " ".join(x for x in (rung(b["dir"]), "step", b["step"]) if x)
            print(f"<!-- parked at {where} -->")
            print("\n".join(b["text"]).strip("\n").replace("\n## ", "\n### ").replace("## ", "### ", 1) + "\n")
    asm = assumed(a.work) + (assumed(os.path.dirname(a.also)) if a.also else [])
    if asm:
        print(f"# Proposal: {len(asm)} recommendation(s) taken without a sign-off (ASSUMED), confirm them\n")
        print("\n".join(f"- {x}" for x in asm) + "\n")
    f = bl[0]
    print(f"first: {f['code']} {f['step']} {f['dir']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
