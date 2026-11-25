# Mendix upgrade toolkit

Upgrades a Mendix app to a newer Mendix version, then tells you in plain words whether anything broke for your users.

**You need:** your app (an `.mpk` or project zip) and the Mendix version it runs on now and the one you want;
a coding agent (such as Claude Code) in a Linux or macOS terminal with Docker; a Mendix token (`MENDIX_PAT`).
Machine setup, once: [upgrade-toolkit/SETUP.md](upgrade-toolkit/SETUP.md).

**Start with one command:**
```bash
upgrade-toolkit/bin/cloud/upgrade-pipeline.sh --app-zip app.mpk --source <current full version> --target <new full version> --work run/work
```
**You will see** a page in your browser (`COCKPIT.html`, refreshes itself) and the same short brief in the terminal
at every stop: where the upgrade stands, what is broken for your users, what is not measured yet, what to do now,
who changed what. Print it any time with `--work run/work --brief`.

**A person decides** at two places: you approve the upgrade plan once (the sign-off), and you answer the few questions
the run cannot settle itself, each with a recommended answer. Answer in the chat with your agent or on the page.
The AI never signs off for you.

---
The rest of this page is detail; skip it on a first read.

## How it works

A scripted Mendix upgrade with gates, run by a coding agent. Scripts do the fixed work: triage, baseline, convert,
Marketplace module updates, build, data diff, smoke walk, page layout compare, journeys and the gate. The agent
repairs build errors, fixes journeys and compares results. Every rung ends in PASS, FAIL or INVALID, with evidence.
A person follows the run on one cockpit page and signs off there.

Headless end to end: nothing here opens Studio Pro. Point it at your app on your own machine (or a cloud
container), tell the agent to upgrade it, and it runs the whole ladder in your terminal — Studio Pro, the latest
version, is only for opening the finished app afterward to look at it.

```
find ──> plan ──> upgrade ──> test ──> go-live
triage    proposal   convert     smoke, layout,    gate verdict,
release   (signed    modules     journeys, data    cockpit page
impact    by you)    repair      old vs new
```

## Start here

| | |
|---|---|
| What to run, in order | [upgrade-toolkit/SKILL.md](upgrade-toolkit/SKILL.md) |
| Set up a machine or a cloud container | [upgrade-toolkit/SETUP.md](upgrade-toolkit/SETUP.md), paste-in prompt [SETUP-PROMPT.md](upgrade-toolkit/SETUP-PROMPT.md) |
| Read a verdict | [upgrade-toolkit/READING-THE-VERDICT.md](upgrade-toolkit/READING-THE-VERDICT.md) |
| See a finished run | [upgrade-toolkit/examples/](upgrade-toolkit/examples/): the cockpit page of an upgrade of a public Marketplace app |
| The toolkit's own tests | `bash upgrade-toolkit/controls/run-controls.sh --fast` (a catch and a pass case for every script) |
| One command for the fixed steps | `upgrade-toolkit/bin/cloud/upgrade-pipeline.sh --app-zip app.mpk --source <old full version> --target <new full version> --work run/work` |

Release-note tables per Mendix version: `brain/baseline/versions/`.

## Related

- [mxcli-project-toolkit](https://github.com/MendixMau/mxcli-project-toolkit): the toolkit for building Mendix
  apps with a coding agent and [mxcli](https://github.com/mendixlabs/mxcli). Its journey engine is vendored here in
  `upgrade-toolkit/vendor/e2e`.
- [mxcli](https://github.com/mendixlabs/mxcli): the Mendix command line this toolkit drives.

## Licence

Apache License 2.0, see [LICENSE](LICENSE).
