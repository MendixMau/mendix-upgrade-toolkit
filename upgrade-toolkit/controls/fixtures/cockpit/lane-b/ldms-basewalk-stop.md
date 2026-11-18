# NEEDS JUDGMENT: step basewalk, exit 11

run folder: /run
work: /run/work
source 9.24.1.4658 -> target 10.24.0.73019
Rule: the items below are pending, not passed: a REGRESSION is fixed, the rest are decided in writing (allow/approved files named in steps/*.md), then rerun:

    /toolkit/upgrade-toolkit/bin/cloud/upgrade-pipeline.sh --app-zip /dl/app.mpk --source 9.24.1.4658 --to 11.12.5 --work /run/work --from basewalk

## Always-on journeys are not all PASS on the OLD app (exit 1): fix the journey, drop it, or write the todo (exit 11)

owner: agent

file: /run/work/journeys-base.out

```
  FAIL    login-User                                              FAIL User home after login: reached ".mx-name-dataView1" never appeared — screenshot login-User-step1-NOT-REACHED.png; INVALID User home after login: 
  INVALID create-save                                             todo: no --create spec: write one core create-and-save spec per app at baseline (widget names are app-specific)
journeys: 1 PASS, 1 FAIL, 1 INVALID
actions ? found · 2 journeys (todo unknown) · 1 pass on baseline (1 defect) · - pass on new · - regression · coverage ? (no actions.json: coverage unknown)
```

## Plan items (exit 11)

owner: info

plan: /run/work/journeys-base/plan.json (skipped, todo, not_browser). An MFA journey needs a user with an MFA type (users.json `_mfa`); this script cannot create one.
