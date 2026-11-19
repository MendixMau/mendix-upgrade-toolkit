# NEEDS JUDGMENT: step afterwalk, exit 12

run folder: /run
work: /run/work
source 9.24.3.8044 -> target 10.24.0.73019
Rule: the items below are pending, not passed: a REGRESSION is fixed, the rest are decided in writing (allow/approved files named in steps/*.md), then rerun:

    /toolkit/upgrade-toolkit/bin/cloud/upgrade-pipeline.sh --app-zip /dl/app.mpk --source 9.24.3.8044 --to 11.12.5 --work /run/work --from afterwalk

## Smoke walk vs baseline (exit 1: 1 = a PASS step regressed or broke, 2 = INVALID): a gate FAIL/INVALID, not a pass (exit 12)

owner: person
question: A step that passed on the old app fails or breaks on the new one. What should we do?
recommended: fix
option: fix|Fix the app, then rerun|The old app passes it, so the upgrade changed behaviour (steps/heal.md: heal the test, never the app).
option: accept|Accept it as intended, in writing|A reason per line in the allow files (steps/gate.md).
option: test|The test is wrong: fix the test|Only when the step fails the same way on the old app.

file: /run/work/logs/afterwalk.log

```
== ProjectManager: FAIL
  FAIL    menu   Production -> Plantapp.ProductionProcess_Overview [content, 1555ms]
== QualityManager: FAIL
  FAIL    menu   Production -> Plantapp.ProductionProcess_Overview [content, 1613ms]
== Technician: FAIL
  FAIL    menu   Production -> Plantapp.ProductionProcess_Overview [content, 1541ms]
steps: PASS 33, FAIL 3, INVALID 0, SKIPPED 0; roles not run (INVALID): 0
  REGRESSION ProjectManager | menu | Production | Plantapp.ProductionProcess_Overview: old PASS 3 of 3, new not PASS 1 of 1; console: [Client] TypeError: titleGetter is not a function at http://localhost:#/widgets/mendix/schedulerwidget/SchedulerWidget.js?#:#:# at Array.map (<anonymous>) at getResourceList (http://localhost
  REGRESSION QualityManager | menu | Production | Plantapp.ProductionProcess_Overview: old PASS 3 of 3, new not PASS 1 of 1; console: [Client] TypeError: getTitle is not a function at http://localhost:#/widgets/mendix/schedulerwidget/SchedulerWidget.js?#:#:# at Array.map (<anonymous>) at getEventObjects (http://localhost:#/
  REGRESSION Technician | menu | Production | Plantapp.ProductionProcess_Overview: old PASS 3 of 3, new not PASS 1 of 1; console: [Client] TypeError: titleGetter is not a function at http://localhost:#/widgets/mendix/schedulerwidget/SchedulerWidget.js?#:#:# at Array.map (<anonymous>) at getResourceList (http://localhost
```
