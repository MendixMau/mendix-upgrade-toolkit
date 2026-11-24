#!/usr/bin/env python3
"""feedback_report.py: at the end of every run, harvest what it taught and write FEEDBACK-REPORT.md, no LLM.

The pipeline calls this from its exit trap, so a run that stops (an environment fault, a judgment stop, a crash) leaves
the same report as one that passes. Before this, bin/harvest.py only ran when a person remembered steps/report.md 3c.

  <work>/learnings/              harvest.py drafts (toolkit; brain drafts in learnings/brain/ when UPG_BRAIN is set)
  <work>/FEEDBACK-REPORT.md      where the run stopped and why, the drafts, and how to send both back: the learnings
                                 by PR (submit-learnings.sh), a toolkit bug as a GitHub issue with a summary to paste

The issue summary holds metadata only (versions, step, exit code, the headings of NEEDS-JUDGMENT.md), never log text,
and goes through the same denylist as harvest.py; a hit leaves the summary out and says so.

usage: feedback_report.py --work DIR --exit N [--step STEP] [--code CODE] [--source V] [--target V]
Never fails the run: exit 0 always, except 2 for a bad call. UPG_HARVEST=0 skips the harvest (the report still comes).
"""
import argparse
import os
import pathlib
import re
import subprocess
import sys

B = pathlib.Path(__file__).resolve().parent
TK = B.parent

MEANING = {
    0: "gate PASS, nothing left for a person",
    2: "usage or version-path error",
    3: "missing tool or setup, or an mxcli of another version (an environment fault, not the app)",
    4: "a fixed step failed unexpectedly (likely a toolkit or environment bug: worth an issue)",
    10: "mx check / build / start errors after the upgrade: repair needed",
    11: "journeys INVALID or FAIL on the old or the new app",
    12: "diff or gate items need a comparison by a person",
    13: "a module plan or a module decision is missing",
    14: "the upgrade proposal awaits sign-off",
    15: "the owner paused the run",
}


def deny_pattern():
    out = subprocess.run(["bash", "-c", f'. "{B}/private_names.sh" >/dev/null 2>&1; printf %s "${{DENY:-}}"'],
                         capture_output=True, text=True)
    return out.stdout.strip()


def toolkit_rev():
    r = subprocess.run(["git", "-C", str(TK), "rev-parse", "--short", "HEAD"], capture_output=True, text=True)
    return r.stdout.strip() or "unknown"


def issues_url():
    r = subprocess.run(["git", "-C", str(TK), "remote", "get-url", "origin"], capture_output=True, text=True)
    m = re.match(r"(?:https://|git@)github\.com[:/]([^/]+/[^/.]+?)(?:\.git)?$", r.stdout.strip())
    return f"https://github.com/{m.group(1)}/issues/new" if m else "the toolkit's GitHub issues page (Issues > New issue)"


def main():
    ap = argparse.ArgumentParser(usage=__doc__.split("usage: ")[1].split("\n")[0])
    ap.add_argument("--work", required=True)
    ap.add_argument("--exit", type=int, required=True)
    ap.add_argument("--step", default="")
    ap.add_argument("--code", default="")
    ap.add_argument("--source", default="")
    ap.add_argument("--target", default="")
    a = ap.parse_args()
    work = pathlib.Path(a.work)
    if not work.is_dir():
        print(f"feedback_report: no work folder {work}", file=sys.stderr)
        return 2

    learn = work / "learnings"
    if os.environ.get("UPG_HARVEST", "1") == "0":
        harvest = "skipped (UPG_HARVEST=0)"
    elif not a.code:
        harvest = "skipped: no app code name (set UPG_APP_CODE, or write it to state/app-code, then run bin/harvest.py)"
    else:
        cmd = [sys.executable, "-I", str(B / "harvest.py"), "--work", str(work), "--code", a.code, "--inbox", str(learn)]
        if os.environ.get("UPG_BRAIN"):
            cmd += ["--to", "both", "--brain-inbox", str(learn / "brain")]
        else:
            cmd += ["--to", "toolkit"]
        r = subprocess.run(cmd, capture_output=True, text=True)
        lines = [l for l in (r.stdout + r.stderr).splitlines() if l.strip()]
        harvest = next((l for l in lines if l.startswith("harvest:")), lines[-1] if lines else f"harvest.py exit {r.returncode}")
        if r.returncode == 1:
            harvest += " (denylist hit: that place was not written)"
    drafts = sorted(p.relative_to(work) for p in learn.rglob("*.md")) if learn.is_dir() else []

    meaning = MEANING.get(a.exit, "unexpected failure (no exit code of the pipeline legend): worth an issue")
    nj = work / "NEEDS-JUDGMENT.md"
    heads = [l.strip() for l in nj.read_text(errors="replace").splitlines() if l.startswith("## ")][:12] if nj.is_file() else []
    issue = [f"toolkit {toolkit_rev()}", f"upgrade {a.source or '?'} -> {a.target or '?'}",
             f"stopped at step: {a.step or 'end of run'}", f"exit {a.exit}: {meaning}"]
    if heads:
        issue += ["needs judgment:"] + [f"  {h[3:]}" for h in heads]
    issue_text = "\n".join(issue)
    deny = deny_pattern()
    if deny and re.search(deny, issue_text, re.I):
        issue_text = "(left out: it matches the private denylist; write the issue by hand)"

    rel_learn = "learnings"
    out = [
        "# Feedback report",
        "",
        f"Exit {a.exit} at {a.step or 'the end of the run'}: {meaning}.",
        "",
        "## What the run taught",
        "",
        f"{harvest}",
        "",
    ]
    out += [f"- `{d}`" for d in drafts] or ["No drafts."]
    out += [
        "",
        "## Send it back",
        "",
        f"1. **Learnings.** Read each draft in `{rel_learn}/`, then run `bin/submit-learnings.sh toolkit --inbox {rel_learn} --dry-run`,",
        "   then without `--dry-run`: one branch, one PR to the public toolkit (no write access: it forks for you with `gh`, or",
        "   prints the manual steps). Brain drafts (`learnings/brain/`) go with `bin/submit-learnings.sh brain --inbox learnings/brain`:",
        "   to your private brain, or, with none, to the public toolkit unless marked `confidentiality: internal`.",
        f"2. **A toolkit bug** (exit 3 or 4 that is not your machine, a wrong verdict, a crash): open {issues_url()}",
        "   and paste the summary below. Read it first: no customer, app, host or person names.",
        "",
        "## Summary for an issue",
        "",
        "```",
        issue_text,
        "```",
        "",
    ]
    (work / "FEEDBACK-REPORT.md").write_text("\n".join(out))
    print(f"feedback: {work / 'FEEDBACK-REPORT.md'} ({len(drafts)} draft(s))")
    # the last lines the person sees: where to send it (the public toolkit takes every user's learnings; exit codes unchanged)
    if a.exit in (3, 4) or a.exit not in MEANING:
        print(f"toolkit bug? the issue summary is in {work / 'FEEDBACK-REPORT.md'} (section 'Summary for an issue'): read it for names, then paste it into {issues_url()}")
    tk = [d for d in drafts if d.parts[:2] != ("learnings", "brain")]
    if tk:
        print(f"{len(tk)} learnings drafted \u2014 send them back: bin/submit-learnings.sh toolkit --inbox {learn} --dry-run")
    elif drafts:
        print(f"{len(drafts)} learnings drafted \u2014 send them back: bin/submit-learnings.sh brain --inbox {learn / 'brain'} --dry-run")
    return 0


if __name__ == "__main__":
    sys.exit(main())
