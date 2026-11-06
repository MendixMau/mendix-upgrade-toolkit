# Stuck items: ask, record, re-measure

Use when an item cannot be upgraded as it is. A decision here never closes a check: it moves the item from "needs a
decision" to "decided, pending <closes by>". The check closes only when the gate measures its rung PASS or PASS* again.

## Triggers
- a RED localedits module on the plan (SKILL stop rule); a stepupdate kept module or a data-bearing idcheck finding
- convertcheck or repair leaves a Java action that no longer compiles; vendorjava COMMENTED-OUT or EMPTIED
- dojo_report "can't move"; a replacement_check row still hitting a deprecated module
- widgets UNRENDERED, or a widget crash on the new client
- a REGRESSION still open after two repair attempts on the same page

Not triggers: INVALID from missing inputs (fix the measurement), a first-seen regression (repair first), REVIEW pairs
(accept-file judgement, READING-THE-VERDICT.md section 4).

## Options per kind (at most 4, plus "something else")
| kind | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| Marketplace module | keep old version (kept list) | replace with the Marketplace equivalent (`replacements.tsv` row) | rebuild locally, drop the module | hand to a named person |
| page / snippet | keep as converted, accept the look (PASS* path) | rebuild with the new widgets | remove if dead (`impact_map`) | hand to a named person |
| widget (.mpk) | keep old package, accept the risk | swap to the successor (`dojo-successors.tsv`) | rebuild as pluggable / native | hand to a named person |
| Java action / vendor Java | keep old jar, pin | port to the new API | replace with a Marketplace module or a microflow | hand to a named person |

Widget swap, properties with no counterpart: map every property the source widget had; for the rest run `bin/widget_defaults.py --widget <target> --mapped <list>` and commit the swap with its `--commit APP --subject ... -- <paths>` form. Rows verified `doc` or `manifest` in `playbooks/widget-config-defaults.tsv` are applied and written into the commit subject as `defaulted: <property> = <value> (best practice|widget default, <source>)`, which `bin/changelog.py` shows in CHANGES.md; `unverified` rows are listed as "not defaulted" and left at the widget's own value. The closing count line (table rows, mapped, defaulted, unverified) is the denominator: paste it in the decision.

## Asking
One question per item, with the options above and the evidence path in the question. On Claude Code use AskUserQuestion;
on any other harness print the same as a numbered markdown list ending "5. something else". Either way end the turn and
wait. Recommending an option from the evidence is fine; choosing silently is not. UNATTENDED runs keep the existing
default (keep at the old version) and record it ASSUMED.

## Pattern catalogue (playbooks/rearchitecture.md)
Before asking, look for an RA entry for the item: bin/proposal.py already cites it in section 3 (`[RA-n, status]`). Ask with that
entry's options and recipe. When the owner answers **rebuild** or **replace** (options 2-3), the run, in the same commit as the
DECISIONS.md line:
- an RA entry exists: update it. Add the app code name, the decision id (S-n / P-n), the result and the date to `evidence`, and move
  `status` (idea -> tried once after one run; tried once -> proven after a second run or a gate that measured it). Fix `options` or
  `recipe` where the run found them wrong. Never raise a status without a run.
- none exists: append `### RA-<next n> <title>` with the fields in the file's entry format (topic, match, trigger, why, options,
  recommendation, effort, recipe, evidence, status, cards) as `tried once` (or `idea` before any run), and a FEEDBACK row.
- no company or customer names; apps by code name. Line format of the record in DECISIONS.md gets the id at the end:
  `... | CONFIRMED | closes by: <rung> | RA-3`

## Record
`$W/DECISIONS.md`, one line per item, append-only:

`S-1 | widgets: Viewer3D.mpk | widget | swap to successor | <reason> | <who> | CONFIRMED (or ASSUMED) | closes by: widgets rung PASS`

- A kept item stays listed as "kept (S-n)" in every later report; a kept module is never reported as upgraded.
- The progress line never reads DECISIONS.md.
- Owner sign-off cannot close while DECISIONS.md holds an ASSUMED line or a hand-off with no name. Only a person writes APPROVED.
