# Mendix upgrade — setup prompt

Paste everything below the line into a Claude Code session (cloud session or local terminal).
Fill in the four `<...>` values first. Keep `MENDIX_PAT` in the environment, never in this text.

## Run mode (the switch)

- **Unattended (default).** Paste everything below the line as it is. Nothing here changes it.
- **Attended (you are present and you sign the proposal).** Paste everything below the line, then replace its first
  sentence ("Upgrade my Mendix app ... unattended, until the gate says PASS.") with the block between the two markers
  below. The block is part of the prompt; the markers are not.

<!-- ATTENDED-START -->
Upgrade my Mendix app with the upgrade toolkit, attended: I am here and I sign the upgrade proposal myself. Run until
the proposal sign-off, stop there, and carry on only after I have signed.

**Attended rules** (they override the unattended wording below wherever they differ)
- Do not set `UPG_INTERVIEW_MODE` and do not write `Interview mode: unattended` or `Interview mode: auto` into
  `interview-mode.txt`. Left unset, the pipeline is attended: at the propose step it stops with exit 14 and writes
  `NEEDS-JUDGMENT.md` ("proposal awaits sign-off", `steps/propose.md`, `SKILL.md` Stop rules).
- At every stop do the four things of `SKILL.md` ("At every stop"), in its order: print the brief
  (`upgrade-pipeline.sh --work $W --brief`); ask each open decision in the chat (`python3 $B/decisions.py pending --work $W`),
  then end your turn and wait for me; record my chat answers with `decisions.py add ... --source chat`; rerun the command
  the stop file names.
- At the proposal stop, give me the cockpit address (the `cockpit: server up at http://...` line, started by
  `bin/cloud/cockpit-up.sh`). If that line was not printed because the server was already up, read the port from
  `$W/.cockpit-port` (beside the cockpit page when `UPG_COCKPIT_OUT` is set) and give me `http://127.0.0.1:<port>/`.
  Point me at `$W/PROPOSAL.md`. I sign in the cockpit, or I write `Signed-off: <name> <date>` in section 6 myself.
- In a cloud session the cockpit binds to 127.0.0.1: expose its port through the app's preview if you can. If you cannot,
  tell me you cannot reach it and I sign `PROPOSAL.md` section 6 myself; never sign in my place.
- You never sign for me. You never write the `Signed-off:` line, never write `Status: PAUSED`, never send the sign-off to
  the cockpit server (`POST /decide` with `"item": "signoff"`), never run `decisions.py import` on a sign-off row you wrote
  yourself, and never answer a `P-n` line or any other decision as if I had. A sign-off is never taken from chat, and "go
  ahead" in chat is not a sign-off. Do not convert, update or repair before the proposal is signed.
- Rerun after I have signed (the command at the top of `NEEDS-JUDGMENT.md`), then follow steps 5 to 10 below. The
  "Loop until PASS" rules apply from there on.
<!-- ATTENDED-END -->

---

Upgrade my Mendix app with the upgrade toolkit, unattended, until the gate says PASS.

**Inputs**
- App: `<git URL of the app, or path to the folder holding the .mpr>`
- Target Mendix version: `<version; default = latest LTS (as of 2026-11 Mendix 11.12): give 11.12 and triage picks the newest patch from the release notes; a full version only if you want a specific patch. Another version only if asked by name>`
- Test or sandbox systems for the external APIs the app calls: `<e.g. Opcenter test URL, or none>`
- Systems that cannot be stood in locally (excluded, listed in the verdict): `<e.g. Teamcenter, or none>`

**Setup**
1. Clone the toolkit anywhere: `git clone https://github.com/MendixMau/mendix-upgrade-toolkit` and `cd` into the clone
   (it holds the toolkit in `upgrade-toolkit/`, the release-note brain in `company-brain-test/brain/`, and the
   unattended pipeline in `pipeline/`).
2. Read `upgrade-toolkit/SETUP.md`, then run its one command:
   `bash upgrade-toolkit/bin/setup-container.sh ~/run1 <old version> <target version>` and `source ~/run1/upg-env.sh`.
   Find the old version with `upgrade-toolkit/bin/mxversion.py` on the app's .mpr.
   `MENDIX_PAT` must already be set in the environment; if it is not, stop and tell me.
3. Put the app under `~/run1/app` as its own git repo.
4. Check the instruments: `cd upgrade-toolkit/controls && make fast`. A red control means the toolkit is broken: stop
   and report it, do not upgrade with it.

**Run**
5. Follow `upgrade-toolkit/SKILL.md` from step 1. It is the source of truth for every step, stop rule and verdict word.
6. Use the brain for release-note impact (`release_impact.py`; `UPG_BRAIN` only if the brain lives elsewhere).
7. External APIs, in this order: (a) the test systems I listed above, (b) responses recorded from a real system,
   (c) the API stand-in (`bin/apimock.py`, same stand-in for the old and the new app) only where no test system is
   reachable. A gate on the stand-in ends at best in `PASS (on stand-in APIs: ...)`: a conditional PASS, to be run
   again on real test systems before go-live. Only the systems I listed above may be excluded; any other API the
   stand-in cannot classify stays INVALID.

**Loop until PASS**
8. After each gate run (`bin/gate.sh`):
   - FAIL on a real difference in the app → fix the app as a human upgrader would, commit, rerun the gate.
   - INVALID because the toolkit cannot judge something → write it in `TOOLKIT-FEEDBACK.md` with evidence, work
     around it only where SKILL.md allows, rerun.
   - Stop at PASS, or `PASS (except <system>: N items)` / `PASS (on stand-in APIs: ...)` (never reported as plain
     PASS), or after 5 rounds with the remaining blockers listed.
9. Never weaken a gate: never round INVALID up to PASS, never skip a check to get green.

**Deliver**
10. Write `SCORECARD.md` (verdict per gate rung, with evidence paths), `HANDWORK.md` (what you changed by hand and
    why) and `TOOLKIT-FEEDBACK.md` (toolkit gaps), and push the app branch. Never push customer data into the
    toolkit repo.
