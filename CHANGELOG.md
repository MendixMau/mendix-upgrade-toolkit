# Changelog

One line per change, newest group first. Add your line in the same commit as the change.

## Unreleased

- Smoke walk: a home-page button that has a visibility expression (shown only after a row is selected) is not walked and is listed as "not walked: conditionally visible" with its count, instead of making the old-app walk INVALID and stopping basewalk (run ORG, OrgChart Example 10.3). The skip is decided on the button's own node, not by widget name (default names repeat across pages and roles).
- Smoke walk: a home-page button inside the content of a data widget (Data grid, Gallery, Timeline: a widget with a data source, drawn once per data row) is not walked and is listed as "not walked: per-row widget content" with its count, instead of making the baseline smoke walk INVALID ("button not rendered") when the grid has no rows. The decision is based on the data widget's data source in the model (a property value with a DataSource), never on nesting depth or widget name, so buttons in an Accordion, tab container or popup menu are still walked. Credit: weekend lane B (Multi-Tenant Administration example, 9.12 -> 10.24 -> 11.12.5).
- decisions.py pending: a stop with no recommended option prints `--choice <update|accept>` in its chat line, not a blank `--choice` (run DVS).
- Cockpit and terminal brief: the "Broken for your users" box names a regression a stop reports (not only the final gate); a stop the agent cannot resolve says "The agent cannot get past this alone" and what it needs; the same stop returning says "Stopped here N times" (new `state/stops.tsv`, one row per stop); a screens REVIEW count shows as "N screens changed and wait for your look" next to "0 regressions" (gate and verdict unchanged; lane B final findings, issue 22; runs PSOP, PMNT, LDMS, CHK).
- Linux build: an add-on `modules/<Name>.mxmodule` that mxbuild unpacks in lower case no longer fails the build ("mxmodule/javasource not found"): the pipeline links the other case in the cache and builds once more, old and new app; repair row 34 (issue 06; run LDMS).
- Basewalk: the baseline walk applies the same checked `baseline-evidence.txt` lines (FIXTURE / OLD-APP / FLAKY, same checks as the journeys step) to its own FAILs, so a journey the old app fails with a logged error is PASS* instead of a stop with no way past (issue 05; run PMNT).
- Old 10.x app: a toolset that bundles Gradle 7 (10.9) builds in the Java 11 image like 10.6, and the 10.9 runtime runs on Java 11 (run DVS).
- NO-SIGNOUT evidence: a sign-out button in a layout no reachable page renders in is not sign-out UI (#62; run SNOW).
- Baseline: a demo snapshot with no rows for the app's tables falls back to synthetic seed rows (#63; run STOR).
- Baseline: wrong-case SCSS imports of the old app are fixed before its Linux build, repair row 11 (#64; run LDMS).
- Journeys: a create-spec nav item can name its position (nth), so an icon-only menu can be walked (#65; run PMNT).
- Brief: the status sentence and the "Open questions" footer now give the same number (the questions that wait for a person); the AI's own choices are counted apart; "Not measured yet" reads "nothing; every check has run."
- Terminal brief: `upgrade-pipeline.sh --brief` prints the same plain brief as the cockpit page (8 lines at most), at every stop and at the end of a run, followed by the open questions.
- SKILL.md: a short "Driving the run" block (print the brief, ask each open decision in chat, record it, rerun) and a current status line in place of the version history.
- README.md and PUBLIC-README.md: the top of the page says what it does, what you need, the one start command, what you will see and where a person decides; the detail moved below.
- Final-check stop: with 0 regressions the top action no longer says "repair"; it offers to hand the open lists to the owner (issue 20).
- diff: an allow line that matches nothing now warns, is listed in `allow-unmatched.txt` and in the cockpit "Everything else" fold; no verdict changes (issue 21).
- #61 apidirect: name the database copy `_smoke_apid_<side>` so smoke_users accepts it.
- #60 Cockpit: the stop's owner decides the top card; recording the old app is not testing; the second rung keeps the first rung's result; charset in the fragment.
- #59 diff step rebuilds `allow-effective.txt` from `allow.txt` + `heal-allow.txt`, so `--from diff` applies a line written at the stop.
- #58 R38: also catch the bare global `logger.<level>(` call Mendix 11 removed.
- #57 repair row 0: `JavaVersion Java21` also after a 10.0 to 10.6 -> 10.24 convert.
- #56 heal: a twin-noted PASS* row is start noise, and a row the gate accepted in writing stops listing as open.
- #55 Cockpit brief: the tests box no longer says "not started" while they run; nothing-needed plus a ranked list of the AI's choices; plain "who changed what"; labelled run time; unattended plan items are no cards.
- #54 stepupdate: commit the jar cleanup when `vendorlib/` does not exist yet (9.x to 10.x).
- #53 Stop sites: every `nj_add`/`nj_file` in the pipeline says who it is for; person stops carry the question, the options and the recommended one.
- #52 Plan dialog: the held-module evidence no longer says "kept" above a recommendation to update; evidence paths never leave the run folder.
- #51 setup-container: install rsync before the mxcli build, not after.
- #50 Mendix 10.0-10.6: build and run on JDK 11.
- #49 decisions: chat `pending` lists the same questions as the page.
- #48 Cockpit: stops say who they are for; person stops show the real question.
- #47 Cockpit: open with a plain brief for a reader with no context, fold the rest.
