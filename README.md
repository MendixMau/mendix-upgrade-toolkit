# Mendix upgrade toolkit

A scripted Mendix upgrade with gates, run by a coding agent. Scripts do the fixed work: triage, baseline, convert,
Marketplace module updates, build, data diff, smoke walk, page layout compare, journeys and the gate. The agent
repairs build errors, fixes journeys and compares results. Every rung ends in PASS, FAIL or INVALID, with evidence.
A person follows the run on one cockpit page and signs off there.

```
find ──> plan ──> upgrade ──> test ──> go-live
triage    proposal   convert     smoke, layout,    gate verdict,
release   (signed    modules     journeys, data    cockpit page
impact    by you)    repair      old vs new
```

## Quick start

```bash
# 1. set up a machine or a cloud container
bash upgrade-toolkit/bin/setup-container.sh        # or follow upgrade-toolkit/SETUP.md by hand

# 2. run the fixed steps end to end on an .mpk
upgrade-toolkit/bin/cloud/upgrade-pipeline.sh \
  --app-zip app.mpk --source <old full version> --target <new full version> --work run/work

# 3. the toolkit's own tests (a catch and a pass case per script)
bash upgrade-toolkit/controls/run-controls.sh --fast
```

The pipeline stops wherever a person must decide (a proposal to sign, a release-note row, an accepted exclusion) and
the cockpit page says what is still open. Nothing here runs against a customer's systems on its own: `--work` is a
local folder, and any outside system the app calls is a stand-in or an explicit, owner-approved connection.

## Walk through a finished run

[`upgrade-toolkit/examples/fsm/`](upgrade-toolkit/examples/fsm/) is a full run on the public Marketplace **Field
Service template** ([marketplace.mendix.com/link/component/204718](https://marketplace.mendix.com/link/component/204718),
FSM 1.1.1 on Mendix 9.24.2): two version rungs (9.24 → 10.24 → 11.12) and one client-swap rung (Dojo → React, same
Mendix version). Every step's triage, plan, build log, test diff and cockpit page is kept, so you can read what the
toolkit found and did on a real, sizeable app (58 modules, 253 pages) before pointing it at your own.

- Start at [`examples/fsm/README.md`](upgrade-toolkit/examples/fsm/README.md) for the result and the folder map.
- Open any rung's `COCKPIT.html` directly in a browser — it is one self-contained file.
- The original 9.24.2 package is **not** shipped here or as a release asset (it is the publisher's own Marketplace
  download, get it from the link above); its SHA-256 is `2e8bc2b33f1e6568f5bd2c2bed3e2a06c1e072d6a68ac03b25d464c61adfd2e8`
  (`examples/fsm/SHA256SUMS`), so you can confirm you're starting from the same build this example ran on. The
  10.24 and 11.12 upgraded packages this toolkit produced are attached to the
  [v0.1 release](../../releases/tag/v0.1).

## Start here

| | |
|---|---|
| What to run, in order | [upgrade-toolkit/SKILL.md](upgrade-toolkit/SKILL.md) |
| Set up a machine or a cloud container | [upgrade-toolkit/SETUP.md](upgrade-toolkit/SETUP.md), paste-in prompt [SETUP-PROMPT.md](upgrade-toolkit/SETUP-PROMPT.md) |
| Read a verdict | [upgrade-toolkit/READING-THE-VERDICT.md](upgrade-toolkit/READING-THE-VERDICT.md) |
| Version-specific playbooks | [upgrade-toolkit/playbooks/](upgrade-toolkit/playbooks/): 9-to-10, 10-to-11, 11-to-11, Dojo-to-React |
| What's next | [upgrade-toolkit/BACKLOG.md](upgrade-toolkit/BACKLOG.md) |
| Contribute | [CONTRIBUTING.md](CONTRIBUTING.md) |

## Related

- [mxcli-project-toolkit](https://github.com/MendixMau/mxcli-project-toolkit): the toolkit for building Mendix
  apps with a coding agent and [mxcli](https://github.com/mendixlabs/mxcli). Its journey engine is vendored here in
  `upgrade-toolkit/vendor/e2e`.
- [mxcli](https://github.com/mendixlabs/mxcli): the Mendix command line this toolkit drives.

## Licence

Apache License 2.0, see [LICENSE](LICENSE).
