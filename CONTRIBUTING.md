# Contributing

This repo is private. Contributions from outside the team aren't open yet, but the same bar
applies to anyone with access: every change should be backed by a field run or a control, not
a guess.

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
