# contrib/inbox

The drop zone for what an upgrade run taught you. No quality bar: a draft is welcome, triage polishes it.

| You have | Do |
|---|---|
| A finished run folder | `bin/harvest.py --work <run> --code <APP>` drafts everything here (and a brain draft, see below) |
| One thing you noticed | copy `TEMPLATE.md` to `<YYYY-MM-DD>-<code>-<topic>.md` and fill it in |
| Drafts ready to send | `bin/submit-learnings.sh toolkit --dry-run`, then without `--dry-run`: one branch, one PR |

Two places, never mixed:

- **Here (the toolkit)**: generic lessons. A fix, an error code, a playbook row, a script. Code names only.
- **The company brain** (`$UPG_BRAIN/inbox/`, `bin/submit-learnings.sh brain`): anything internal, customer
  context, notes in the brain's format (`confidentiality: internal`). `submit-learnings.sh toolkit` refuses a file
  marked internal.

Both checks run before anything is pushed: the private denylist, credentials, home folder paths.

Triage (a maintainer): promote what holds into `steps/repair.md`, `playbooks/`, `BACKLOG.md` or `bin/` (with a
catch and a pass control), then delete the draft in the same PR.
