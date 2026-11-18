# Changelog

One line per change, newest group first. Add your line in the same commit as the change.

## Unreleased

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
