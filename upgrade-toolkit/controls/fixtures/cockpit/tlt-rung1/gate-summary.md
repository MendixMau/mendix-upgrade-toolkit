# Gate summary

Overall: **INVALID** (exit 2): 8 PASS/PASS*, 0 EXCEPT, 0 FAIL, 0 INVALID, 1 required NOT RUN.
Grade: 89% (8 of 9 required rungs done): proven 4, accepted 4, waiting on a person 1, not testable here 0, open regression 0 | verdict INVALID
Progress: 8 of 10 checks closed (80%). 0 with REGRESSIONS to fix, 0 need a decision, 1 not measured yet, owner sign-off pending. Proposal not signed.
Changes: 17 (toolkit 17, agent 0, person 0, unlabelled 0)
Change ledger: `<run>/work/CHANGES.md`
heal: 8 failing row(s) classified, 2 accepted with a written reason, 0 journey(s) pass after the heal, 0 stay open (0 real-regression, 0 likely-real); classes: accepted 2, no-click-path 1, test-setup 5; toolkit gaps: 0 (toolkit-gaps.md) (details: `<run>/work/heal.md`)
Classes: build=closed idcheck=closed const=closed data=closed rest=none logdiff=closed smoke=closed layout=none journeys=closed screens=closed release=unmeasured apis=none widgets=none trail=none
Work: `<run>/work`, evidence: `<run>/work`, instruments: `<toolkit>/bin`, run 20261118124353. 2026-11-18T12:44Z
Time: fetch 2s, triage 1m, baseline 2m, basewalk 7m, propose 4s, convert 43s, update 15m, build 5m, after 35s, afterwalk 54s, journeys 29m, heal 28s, apidirect 1s, diff 2m, gate 2s; machine 1h3m; person wait 1h12m

proposal not signed: <run>/work/PROPOSAL.md has no Signed-off line, so this verdict is not an owner-approved upgrade (steps/propose.md)

| # | rung | verdict | rc | one line |
|---|---|---|---|---|
| 1 | build | PASS | 0 | BUILD SUCCEEDED and 0 "ERROR at" lines: yes in <run>/work/build-10.24.0.73019.log |
| 2 | idcheck | PASS | 0 | findings: 9 total, 4 RED (data-bearing), 4 of them approved, 0 open;verdict: PASS  (FAIL = open data-bearing GUID change; REVIEW = open data-bearing removals or persistence loss only: confirm each is  |
| 3 | const | PASS* | 0 | FAIL 0 \| REVIEW 0 \| PASS* 1 \| INFO 2 \| PASS 1 |
| 4 | data | PASS* | 0 | INVALID 0 \| FAIL 0 \| REVIEW 0 \| NEW_ENDPOINT 0 \| PASS* 3 \| PASS 100 \| INFO 45 |
| 5 | rest | NOT RUN | - | not selected (--only build,idcheck,const,data,logdiff,screens,smoke,journeys) (optional rung) |
| 6 | logdiff | PASS* | 0 | FAIL 0 \| REVIEW 0 \| PASS* 1 \| INFO 1 |
| 7 | smoke | PASS | 0 | steps: PASS 6, FAIL 0, INVALID 0, SKIPPED 0; roles not run (INVALID): 0 |
| 8 | layout | NOT RUN | - | not selected (--only build,idcheck,const,data,logdiff,screens,smoke,journeys) (optional rung) |
| 9 | journeys | PASS* | 3 | noted, not a failure: nothing that passed on the old app fails on the new one; journeys that fail on the old app too are listed for the owner; journeys: 37 PASS, 0 FAIL, 1 INVALID, 5 PASS* (baseline defect), 4 SKIPPED (failed on the old app too, not run on the new one), 130 INFO (covered, unreachable or out of scope, listed only);actions 150 |
| 10 | screens | PASS | 0 | pairs 6: INVALID 0 \| REVIEW 0 \| PASS* 0 \| PASS 6;screens: 6 PASS, 0 PASS*, 0 REVIEW, 0 INVALID |
| 11 | release | NOT RUN | - | not selected (--only build,idcheck,const,data,logdiff,screens,smoke,journeys) |
| 12 | apis | NOT RUN | - | not selected (--only build,idcheck,const,data,logdiff,screens,smoke,journeys) (optional rung) |
| 13 | widgets | NOT RUN | - | not selected (--only build,idcheck,const,data,logdiff,screens,smoke,journeys) (optional rung) |
| 14 | trail | NOT RUN | - | WARNING: trail: 45 gap(s) in 25 steps. First: S-1 (Module updates that carry the app's edits) has no change recorded and no note that none was needed. 20 step(s) wait for the owner's OK. (optional rung) |

Report words: PASS = verified; PASS* = verified with accepted differences; FAIL = REGRESSION to fix only when something that passed on the old app fails on the new one, needs a decision when only REVIEW lines are open; INVALID / NOT RUN = not measured yet (or needs a decision when a human item is open).

Not closed, in report words (REGRESSIONS first):
- release: not measured yet: not selected (--only build,idcheck,const,data,logdiff,screens,smoke,journeys)

PASS* = accepted in writing (allow or accept file; each reason is in the rung's report). FAIL = an open FAIL or REVIEW.
INVALID = the rung could not judge (instrument rc 2, journeys rc 3, timeout, failed PRE command); it blocks DONE and is never PASS.
NOT RUN = the rung was skipped or its inputs were not given; for a required rung that blocks DONE too.
EXCEPT = the rung's only non-PASS items failed on a call into an excluded system (EXCLUDE_SYSTEMS): NOT CHECKED, listed above; the overall verdict is then PASS (except ...), exit 4, never plain PASS.
PASS (on stand-in APIs: ...) = APIMOCK answered for the listed endpoints; exit 4, never plain PASS: plain PASS needs the real (test) systems.
