# v0.1 (draft — not yet tagged or released)

First release of the Mendix upgrade toolkit as its own repo. A scripted upgrade with gates, run
by a coding agent: triage, baseline, convert, Marketplace module updates, build, data diff,
smoke walk, page layout compare, journeys and the gate, ending in PASS/FAIL/INVALID with
evidence and one cockpit page per rung.

## What's in this release

- The full step pipeline (`steps/`, `bin/`, `controls/`) and its own test suite
  (`controls/run-controls.sh`, 2400+ controls).
- Version-path playbooks: 9-to-10, 10-to-11, 11-to-11, and a new **Dojo-to-React client-swap
  playbook** ([`playbooks/dojo-to-react.md`](playbooks/dojo-to-react.md)) — a mechanical legacy-
  widget converter, the security grants and build errors a React swap surfaces, and which test
  failures are instrument noise rather than app regressions.
- A worked example: the public Marketplace **Field Service template**, three rungs — 9.24 →
  10.24 → 11.12, then Dojo → React on 11.12.7 — with every step's evidence kept
  (`examples/fsm/`).
- `BACKLOG.md` and `FEEDBACK.md`: the open items and the full finding register behind every
  control in this release.

## Release assets

| File | Mendix | Notes |
|---|---|---|
| `FSM-10.24.28-upgraded.mpk` | 10.24.28 | end of rung 1, this toolkit's output |
| `FSM-11.12.7-upgraded.mpk` | 11.12.7 | end of rung 2, this toolkit's output |

The original 9.24.2 source package is **not** attached here: it is the publisher's own
Marketplace download
([marketplace.mendix.com/link/component/204718](https://marketplace.mendix.com/link/component/204718),
FSM 1.1.1). Its SHA-256 (`examples/fsm/SHA256SUMS`) lets you confirm you're starting from the
same build this release's run started from.

## Known gaps (tracked in BACKLOG.md)

- No parallel role execution or checkpoint/resume for journeys (#138, #146) — a full app run is
  still single-threaded and restarts at 0 if interrupted.
- No Mendix 11 Java API rewriter for kept modules, and no pre-build scan for removed `mx.*`
  client APIs in widget packages (#144) — both are found only by a build or a runtime crash
  today.
- The Dojo-to-React converter (`examples/fsm/rung3-dojo-to-react/convert_legacy.py`) is a
  working script, not yet a shipped `bin/` tool; mxcli itself has no `ALTER`/`DROP` for building
  blocks or wrapped widgets (#137, upstream `mendixlabs/mxcli#1807`).

## Not proved yet

- A Dojo-to-React swap combined with a version rung in one pass.
- An 11.x-to-11.y rung on a source below Mendix 11.6, or any target other than 11.15.0.
- A legacy-widget count far above the Field Service example's 548 widgets / 209 documents.
