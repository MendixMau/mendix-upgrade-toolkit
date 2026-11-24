# Contributing

Contributions are open to everyone, inside or outside the team. Ran the toolkit on your own app and hit a wall, a
wrong verdict or a missing step? Send it: an issue, a learnings draft or a pull request are all welcome. One bar for
everyone: every change is backed by a field run or a control, not a guess.

## How to contribute, step by step

1. **Open an issue first** for anything bigger than a small fix: say what broke or what's missing, on which Mendix
   versions, and how far the run got. A small, obvious fix can go straight to step 2.
2. **Fork the repo** on GitHub and create a branch on your fork (`fix/<topic>` or `docs/<topic>`).
3. **Make the change** with a control that proves it (see "What a good contribution looks like").
4. **Run the checks** in "Before you open a PR" below.
5. **Open a pull request against `main`.** Say what changed, why, and the evidence: the control names, or the run and
   row id (by code name) the finding came from. Link the issue if there is one.
6. **Review.** A maintainer reads the diff and runs the controls. On your first PR, GitHub waits for a maintainer to
   approve the CI run; that is a GitHub default, not a judgement on the PR. If CI fails on a control your change
   doesn't touch, say so in the PR and the maintainer checks it against `main`. Once review is done and the controls
   pass, the maintainer merges it.

## One intake for everyone

Every user's learnings come back to this repo, whatever their setup. A run ends with a line such as
`2 learnings drafted: send them back: bin/submit-learnings.sh toolkit --inbox <run>/learnings --dry-run`. The flow:

1. Read the drafts (`<run>/learnings/`) for customer, app, person and host names.
2. `upgrade-toolkit/bin/submit-learnings.sh toolkit --inbox <run>/learnings --dry-run`, then again without `--dry-run`.
   It leak-checks, cuts a `learnings/` branch and opens one PR into `contrib/inbox/`. No write access? It forks the repo
   with `gh repo fork --remote` and opens the PR from your fork; without `gh` it prints the manual steps and keeps the branch.
3. Notes in the company-brain format: `submit-learnings.sh brain`. With a private brain repo they go there; with none
   (no `UPG_BRAIN`, or the brain this repo ships) they go to the same public inbox, unless marked
   `confidentiality: internal`, which never leaves the brain.
4. A maintainer triages the inbox (labels `bug`, `learning`, `feature`, `contrib-inbox` are set automatically): promote
   what holds into `FEEDBACK.md`, `playbooks/` or `steps/` with a control, delete the draft in the same PR.

## Four ways in

1. **An issue** for a bug you can't fix yourself. Every run ends with `FEEDBACK-REPORT.md` in its work folder: where it
   stopped, the exit code and the drafts it harvested. Paste its summary into a GitHub issue after you have read it for
   names, hosts and paths.
2. **Drop a note.** Copy `upgrade-toolkit/contrib/inbox/TEMPLATE.md` to
   `contrib/inbox/<YYYY-MM-DD>-<code>-<topic>.md` and open a PR with it. No quality bar: triage promotes it and deletes
   the draft.
3. **Harvest a run.** `upgrade-toolkit/bin/harvest.py --work <run folder> --code <APP>` drafts the fixes the agent
   made by hand, unknown error codes, scripts and toolkit items into the inbox. Then
   `upgrade-toolkit/bin/submit-learnings.sh toolkit` runs the leak checks and opens one PR from a `learnings/` branch.
4. **A direct PR** for a finished change, following the steps above.

## What a good contribution looks like

- **Small and on one topic.** One fix or one lesson per PR; a refactor goes in its own PR.
- **Proven by a control.** A changed script gets a catch case that fails on the old code and a pass case that passes
  on the new one, in `controls/run-controls.sh`. Check the catch case really fails before your fix.
- **Traceable.** A lesson from a real run names the run by code name and row id, so a reader can find the evidence.
- **Clean.** No customer, app, person or host names, no credentials, no home-folder paths: the leak checks below pass.
- **Generic.** Written so it helps the next app, not only yours.

Toolkit or brain: the toolkit takes generic lessons under code names. Anything internal (customer context, notes from
the company brain, `confidentiality: internal`) goes to the brain with `submit-learnings.sh brain`, never here;
`submit-learnings.sh toolkit` refuses a file marked internal.

## Before you open a PR

1. **Run the controls.** `bash upgrade-toolkit/controls/run-controls.sh --fast` for a quick
   pass, drop `--fast` for the full suite. A new behaviour needs a new catch case and a new pass
   case, same as every existing script.
2. **Run the leak checks.** Nothing here names a customer, a real app, an internal host, a
   credential or a home-folder path. A finding from a real engagement is welcome, but it goes in
   under a code name (see `FEEDBACK.md`'s glossary for the convention), never the real name.
   ```bash
   bash upgrade-toolkit/bin/customer_names_check.sh upgrade-toolkit
   source upgrade-toolkit/bin/private_hosts.sh   # sets HOSTS_DENY/HOSTS_ALLOW for your own grep
   grep -rnE 'ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|glpat-[A-Za-z0-9_-]{10,}|AKIA[0-9A-Z]{16}|BEGIN (RSA|OPENSSH|PRIVATE) KEY' upgrade-toolkit
   ```
   `customer_names_check.sh` reads its denylist from `$UPG_PRIVATE_NAMES`
   (`~/.config/upgrade-toolkit/private-names.txt` by default), which lives outside the repo on
   purpose — set it locally before relying on the check.
3. **Evidence files (`.log`, `.tsv`, `.json`, `.out`) get a manual read before they're added**,
   not just a grep. A log can carry a path, a hostname or a customer-shaped string a denylist
   doesn't know about yet; if you find one, add the pattern to your local denylist and redact
   the file.
4. **Playbooks and BACKLOG items cite a field run by code name and row id** (`FSM`, `N1`, `AM-3`,
   ...), never by the real app or customer. If your finding doesn't fit an existing code, pick a
   short one and add it to the relevant glossary (`FEEDBACK.md` header).

## What belongs where

| Change | Goes in |
|---|---|
| A new or fixed check, a bug in a script | `bin/`, `controls/run-controls.sh` (pass + catch case) |
| A lesson from a real run that isn't yet generalised | `FEEDBACK.md` (register) first, then `BACKLOG.md` if it's an open item with a "done when" |
| A reusable upgrade recipe (a version jump, a client swap, a widget family) | `playbooks/` |
| A finished, evidence-complete example run | `examples/<app>/` (see `examples/fsm/` for the shape: `COCKPIT.html` plus `steps/{triage,plan,upgrade,test}/`) |
| A step's own behaviour (what step 3 must produce, etc.) | `steps/*.md` |

## Commit style

One topic per commit. State what changed and, if it came from a run, which one (code name + row
id), so a later reader can trace the evidence back to `FEEDBACK.md` without re-deriving it.

## Licence

The toolkit is Apache-2.0 (see `LICENSE`). By opening a pull request you agree your contribution is released under
the same licence.
