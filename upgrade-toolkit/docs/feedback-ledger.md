# Feedback ledger

Every piece of the owner's feedback on the toolkit, the conclusion we reached, and where it landed. One row per point.
Status: **done** (merged to main), **branch** (committed on `fix/signed-cards`, no PR yet), **PR** (open pull request),
**open** (agreed, not built), **owner** (waits for the owner's call). Newest first. Update this file in the same commit
that closes a row.

| date | feedback (owner's words, short) | conclusion | status | where |
|---|---|---|---|---|
| 11-17 | "Make the sidebar 50% of screen ... show what was found per action, and what it MEANS" | drawer is 50% wide; per action a "What it means" box and an item-by-item table, worst first | branch | ba76a0e |
| 11-17 | "If we could write such a thing per issue which needs a decision ... embed this" | a decision opens its case in the cockpit: headline, tiles, old vs new screenshot, why, options with the catch | branch | 775ddae |
| 11-17 | the step writes its case on its own, not by hand | case files written by the step that raises the decision | open | |
| 11-17 | "All routine decisions just have one sign off ... in auto mode they just upgrade" | routine work: one plan sign-off, or approved by the agent in auto mode; only a deviation asks a person | branch | ba76a0e |
| 11-17 | modules with screen edits counted as routine (6 of 10 carry local edits) | stop counting a module with local edits as routine | owner | |
| 11-17 | "No manual copying" (Accounts page) | a Marketplace page the menu opens: copied onto the app layout, or its layout set in place when a copy is not safe | branch | 132323a, 183d044, 8aa073d |
| 11-17 | 7 Accounts actions work on the old app, fail on the new | in-place layout keeps the user grid; rerun WM1 from build to prove the 7 pass | open | |
| 11-17 | "we still don't understand what fails means" | a FAIL is only "worked on old, broken on new"; fails on both = a note; known platform differences PASS* with reason | branch | 44d9111, ba76a0e |
| 11-17 | "see which tests actually ran? On old & new" | test step shows the runs on old and new; repeated context hideable | branch | ba76a0e |
| 11-17 | "build the SQL standin skill into toolkit" | 9.24 data reads go through the toolkit's own Postgres route | branch | e1b677f, 186c0f1 |
| 11-17 | CLI testing does not work on the old app: skill + bug report for mxcli | playbook entry in the toolkit; mxcli issue filed | branch + issue | e1b677f, mendixlabs/mxcli#1879 |
| 11-17 | "we don't spend 50 hours of testing when it's not needed" | e2e strategy: journeys once at the end, skip what failed on the old app | open (partly) | ba76a0e |
| 11-17 | proper e2e journeys incl. unhappy paths | rendered widget check | PR | #8 |
| 11-16 | "Is our advice at all correct to keep it on the old version?" | update instead of keep: refused modules routed to an update that carries the edits | done | #10 |
| 11-16 | "we give people 000 information on what the local edits are" | every plan card shows the evidence behind it; cockpitcheck fails a card without it | done | #10 |
| 11-16 | "Is our brain and script so far routing as it should? Are we measuring that?" | route score per run and a ledger; brain notes hit@k | branch | 6d73740, 081799b |
| 11-16 | rows "not approved yet" with nothing to approve; "create a gate" | cockpitcheck gate; grey when unmeasured | done | #10 |
| 11-16 | "Dojo React will always be a topic" | Dojo to React report on every upgrade | done | #10 |
| 11-16 | "Don't we want more than click paths?" | one test row per kind of app part | done | #10 |
| 11-16 | "Cockpit not up to date? Talk to your agent" | sidebar note | done | #10 |
| 11-16 | "how do I now let this continue? ... a mode for upgrades" | judgment stop as a red bar with the rerun command; interview mode auto | done + branch | #9, acdabb2 |
| 11-16 | "I signed off ... but it still said blocked" | a sign-off counts for the plan it was given on; signed item leaves Blocked | done | #10 |
| 11-16 | decisions hard to find; buttons like ask-user-question, read every 15 s | Decide now cards, one click per question, saved by the local server | done | #10 |
| 11-16 | end-to-end testing was poor | test resilience | done | #6 |
| 11-15 | cockpit: show when stuff is running | live cockpit shows the running step | done | #4 |
| 11-15 | open the cockpit as localhost after triage | live cockpit opens after triage | done | #4 |
| 11-15 | harvest learnings and submit them back | harvest and submit learnings | PR | #3 |
| 11-15 | version chip label | says what is open | PR | #2 |
