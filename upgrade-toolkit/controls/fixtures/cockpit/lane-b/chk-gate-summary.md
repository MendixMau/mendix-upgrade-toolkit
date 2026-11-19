# Gate summary

Overall: **FAIL** (exit 1): 5 PASS/PASS*, 0 EXCEPT, 2 FAIL, 1 INVALID, 1 required NOT RUN.
Grade: 56% (5 of 9 required rungs done): proven 4, accepted 1, waiting on a person 4, not testable here 0, open regression 0 | verdict FAIL
Progress: 5 of 10 checks closed (50%). 0 with REGRESSIONS to fix, 2 need a decision, 2 not measured yet, owner sign-off pending. Proposal not signed.
Changes: 12 (toolkit 10, agent 0, person 0, unlabelled 2)
Change ledger: `/run/work/CHANGES.md`
heal: 71 failing row(s) classified, 0 accepted with a written reason, 0 journey(s) pass after the heal, 0 stay open (0 real-regression, 0 likely-real); classes: no-click-path 55, test-setup 16; toolkit gaps: 0 (toolkit-gaps.md) (details: `/run/work/heal.md`)
Classes: build=closed idcheck=closed const=closed data=closed rest=none logdiff=closed smoke=unmeasured layout=none journeys=decision screens=decision release=unmeasured apis=none widgets=none trail=none
Work: `/run/work`, evidence: `/run/work`, instruments: `/run run 20261118131322. 2026-11-18T13:13Z

proposal not signed: /run/work/PROPOSAL.md has no Signed-off line, so this verdict is not an owner-approved upgrade (steps/propose.md)

| # | rung | verdict | rc | one line |
|---|---|---|---|---|
| 1 | build | PASS | 0 | BUILD SUCCEEDED and 0 "ERROR at" lines: yes in /run/work/build-10.24.0.73019.log |
| 2 | idcheck | PASS | 0 | findings: 1 total, 1 RED (data-bearing), 1 of them approved, 0 open;verdict: PASS  (FAIL = open data-bearing GUID change; REVIEW = open data-bearing removals or persistence loss only: confirm each is  |
| 3 | const | PASS | 0 | FAIL 0 \| REVIEW 0 \| PASS* 0 \| INFO 0 \| PASS 53 |
| 4 | data | PASS* | 0 | INVALID 0 \| FAIL 0 \| REVIEW 0 \| NEW_ENDPOINT 0 \| PASS* 3 \| PASS 270 \| INFO 63 |
| 5 | rest | NOT RUN | - | not selected (--only build,idcheck,const,data,logdiff,screens,smoke,journeys) (optional rung) |
| 6 | logdiff | PASS | 0 | FAIL 0 \| REVIEW 0 \| PASS* 0 \| INFO 0 |
| 7 | smoke | INVALID | 2 | steps: PASS 11, FAIL 1, INVALID 1, SKIPPED 0; roles not run (INVALID): 0 |
| 8 | layout | NOT RUN | - | not selected (--only build,idcheck,const,data,logdiff,screens,smoke,journeys) (optional rung) |
| 9 | journeys | FAIL | 1 | journeys: 40 PASS, 16 FAIL, 55 INVALID, 129 SKIPPED (failed on the old app too, not run on the new one), 58 INFO (covered, unreachable or out of scope, listed only);actions 292 found · 175 generated  |
| 10 | screens | FAIL | 1 | pairs 11: INVALID 0 \| REVIEW 3 \| PASS* 0 \| PASS 8;screens: 8 PASS, 0 PASS*, 3 REVIEW, 0 INVALID |
| 11 | release | NOT RUN | - | not selected (--only build,idcheck,const,data,logdiff,screens,smoke,journeys) |
| 12 | apis | NOT RUN | - | not selected (--only build,idcheck,const,data,logdiff,screens,smoke,journeys) (optional rung) |
| 13 | widgets | NOT RUN | - | not selected (--only build,idcheck,const,data,logdiff,screens,smoke,journeys) (optional rung) |
| 14 | trail | NOT RUN | - | WARNING: trail: 54 gap(s) in 27 steps. First: S-1 (Review the stand-ins for outside calls) has no change recorded and no note that none was needed. 24 step(s) wait for the owner's OK. (optional rung) |

Report words: PASS = verified; PASS* = verified with accepted differences; FAIL = REGRESSION to fix only when something that passed on the old app fails on the new one, needs a decision when only REVIEW lines are open; INVALID / NOT RUN = not measured yet (or needs a decision when a human item is open).

Not closed, in report words (REGRESSIONS first):
- smoke: not measured yet: steps: PASS 11, FAIL 1, INVALID 1, SKIPPED 0; roles not run (INVALID): 0
- journeys: needs a decision: journeys: 40 PASS, 16 FAIL, 55 INVALID, 129 SKIPPED (failed on the old app too, not run on the new one), 58 INFO (covered, unreachable or out of scope, listed only);actions 292 found · 175 generated  (steps/decide.md, or the accept file named in the rung's report)
- screens: needs a decision: pairs 11: INVALID 0 | REVIEW 3 | PASS* 0 | PASS 8;screens: 8 PASS, 0 PASS*, 3 REVIEW, 0 INVALID (steps/decide.md, or the accept file named in the rung's report)
- release: not measured yet: not selected (--only build,idcheck,const,data,logdiff,screens,smoke,journeys)
- changes: needs a decision: 2 commit(s) in the app repo carry no Changed-By / Upgrade-Change trailers (listed as unlabelled in /run/work/CHANGES.md; say who made them and why, steps/decide.md)

PASS* = accepted in writing (allow or accept file; each reason is in the rung's report). FAIL = an open FAIL or REVIEW.
INVALID = the rung could not judge (instrument rc 2, journeys rc 3, timeout, failed PRE command); it blocks DONE and is never PASS.
NOT RUN = the rung was skipped or its inputs were not given; for a required rung that blocks DONE too.
EXCEPT = the rung's only non-PASS items failed on a call into an excluded system (EXCLUDE_SYSTEMS): NOT CHECKED, listed above; the overall verdict is then PASS (except ...), exit 4, never plain PASS.
PASS (on stand-in APIs: ...) = APIMOCK answered for the listed endpoints; exit 4, never plain PASS: plain PASS needs the real (test) systems.
