# NEEDS JUDGMENT: step basewalk, exit 11

run folder: /run
work: /run/work
source 9.24.2.6130 -> target 10.24.0.73019
Rule: the items below are pending, not passed: a REGRESSION is fixed, the rest are decided in writing (allow/approved files named in steps/*.md), then rerun:

    /toolkit/upgrade-toolkit/bin/cloud/upgrade-pipeline.sh --app-zip /dl/app.mpk --source 9.24.2.6130 --to 11.12.5 --work /run/work --from basewalk

## Always-on journeys are not all PASS on the OLD app (exit 1): fix the journey, drop it, or write the todo (exit 11)

owner: agent

file: /run/work/journeys-base.out

```
  FAIL    sign-out                                                FAIL sign out: login page shown, role menu gone: reached "#loginButton,.mx-name-loginButton,input[type=password]" never appeared — screenshot sign-out
  FAIL    login-WebServiceUser                                    FAIL WebServiceUser home after login: page does NOT say "An error occurred" rendered — the screen contradicts the data
journeys: 4 PASS, 2 FAIL, 0 INVALID
actions 134 found · 0 generated (134 todo: no-click-path 61, no journey 59, external-call 14) · 0 pass on baseline (0 defect) · - pass on new · - regression · coverage 0/134 (0%)
```

## Plan items (exit 11)

owner: info

plan: /run/work/journeys-base/plan.json (skipped, todo, not_browser). An MFA journey needs a user with an MFA type (users.json `_mfa`); this script cannot create one.
