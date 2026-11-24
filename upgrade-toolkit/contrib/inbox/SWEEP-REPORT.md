# Learnings sweep of the weekend field runs (2026-11-24)

**From:** learnings sweep, a learnings sweep
**Date:** 2026-11-24
**Kind:** report
**Upgrade:** 9.x and 10.x to 10.24 to 11.12 (about 20 field runs, 2026-11-18 to 2026-11-21)
**Field evidence:** lane notes and issue drafts kept in a short-lived cloud work folder, which is lost when the container ends
**Proposed target:** triage reads this once, then deletes it; the rows went to FEEDBACK.md (SW-1 to SW-22), runs/HISTORY.md and the notes beside this file

---

**Denominator: files read 78, learnings 69, every 69 accounted for.**

| class | count | where it went |
|---|---|---|
| CAPTURED | 18 | already in FEEDBACK.md, CHANGELOG.md, steps/ or an open branch (cited below) |
| TOOLKIT-GAP | 20 | FEEDBACK.md rows SW-1 to SW-19 and SW-22, status open |
| BRAIN | 7 | `contrib/inbox/2026-11-24-sweep-*.md`, brain frontmatter, `confidentiality: public` |
| RUN-HISTORY | 19 | `runs/HISTORY.md`, metadata only (dates marked `~` are not recorded in the notes) |
| NOISE | 3 | not kept |
| HELD | 2 | not written, reasons below |

## Files read (78)

- 39 issue drafts: all.
- 12 lane status files, 3 briefs, the house-rules brief, the field-feedback register (headline lines only).
- 2 harvest run tables, the run claims file, the feedback report and harvest draft of one run.
- The mining summary of the weekend runs and the NOTES heads of 16 runs (TLT, CHK, ERRH, RMS, SITS, SNOW, ORG, DVS, MTA, PSOP, PMNT, LDMS, STOR, TBUD, AIB, WTD).

Not read in full, so learnings that live only there are not counted: the remainder of one status file and the field-feedback register, the coaching text files, the cockpit work notes, per-run notes of the remaining runs, the gate summary of one run, shared research notes (the folder holds none).

## Skipped

- Checkout dirs of the toolkit (several, confirmed by their git layout) and the worktree folder: the content is the toolkit itself.
- One work folder that was in use: not read.
- Any .mpr, .mpk or binary; screenshots.

## CAPTURED (18)

1. MPK without vendorlib: MC-1, DV-5.
2. afterwalk has no accept route for a baseline-equal smoke row: WK-4.
3. Baseline journey failures have no route; the doomed share known only at the gate: WK-5.
4. create-spec.json undocumented in the brief: WK-3.
5. Ladder `--from` restarts rung 1: WK-2.
6. Release rung never selected by the diff step: WK-1.
7. localedits redone when a module version is a build number: CHANGELOG.md (localedits cache, UNKNOWN kept), FR-9.
8. Smoke walk INVALID on a conditionally visible button: CHANGELOG.md (not walked: conditionally visible).
9. A per-run image override leaked into later rungs: CHANGELOG.md (image chosen from the toolset and version).
10. Top action says repair over 0 regressions: fixed on main (mining row 7).
11. Cockpit stale "Running now", "Blocked on you" over assumed items, stop owner, tests box: open branches (mining rows 2, 3), not yet on main.
12. harvest lists the unpacked runtime of every walked app as scripts: FR-5.
13. `mxcli marketplace diff` UNKNOWN in triage: FR-8.
14. R38 misses a bare global logger; allow.txt not applied until heal reruns: open branches, not yet on main.
15. Journeys run with no progress line and no cap: CHANGELOG.md (GF-50).
16. Add-on module cache case on Linux: open branch, not yet on main.
17. Generated click lands on a layout footer link of the same name: fixed on main (#173).
18. decisions.py placeholder choice and reused item ids: fixed on main (#174).

## TOOLKIT-GAP (20): FEEDBACK.md SW-1 to SW-19 and SW-22

SW-1 journey todo accept route; SW-2 screens count a skipped journey twice; SW-3 plan line installs an absent module (GM-12 only reports it); SW-4 plan-pre below 10.24; SW-5 gate stop with no brain; SW-6 UNKNOWN wording for no release notes; SW-7 module-update stop not a decision item; SW-8 app icon CE1613 repair; SW-9 owner-only blocker wording; SW-10 apimock classify reload; SW-11 hand-processes.json undocumented; SW-12 allow line matches nothing; SW-13 widget-drop option for a standalone widget; SW-14 no time estimates; SW-15 shared entry step probed once; SW-16 chromium build mismatch; SW-17 two stops from one replay decision; SW-18 disabled button reported covered; SW-19 smoke users without a tenant; SW-22 cockpit top card follows a settled question.

## BRAIN (7): `contrib/inbox/2026-11-24-sweep-*.md`

nav app icon gone after a design-module update; Administration 4.5 CE0463; Data Widgets missing (widget drop); design-module snippet needs a feedback module; 10.6 app needs JDK 11; SSO starter apps hide the local login form; feedback module major skip (hypothesis).

## RUN-HISTORY (19)

TLT, CHK, PSOP, PMNT, LDMS, STOR, TBUD, SNOW, ORG, DVS, MTA, AIB, WTD, RMS, SITS, ALT, WKS, ERRH, GA1. Toolkit commit, duration and some dates were not in the notes; they read `?` or `~`. Runs of the skipped app (no download URL on the Marketplace) and one run with no notes read (RKT) have no row.

## NOISE (3)

A hand-written state marker that had to be reverted (a process lesson, not a toolkit change); several runs stopped on the shared disk guard (host, not toolkit); one app skipped because the Marketplace exposes no download URL.

## HELD (2)

- A widget-filter question for one page of one app: only meaningful with that app's own context.
- Confirmation of a collapsed icon-only menu after a design-module step: the question belongs to that app's owner, not to the toolkit.
