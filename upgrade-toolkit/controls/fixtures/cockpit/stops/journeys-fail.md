# NEEDS JUDGMENT: step journeys, exit 11

run folder: <run>
work: <run>/work
source 10.24.0.73019 -> target 11.12.5
Rule: a FAIL or INVALID below is not a pass. Fix or accept it in writing (allow/approved files named in steps/*.md), then rerun:

    <toolkit>/upgrade-toolkit/bin/cloud/upgrade-pipeline.sh --app-zip <run>/dl/App.mpk --source 10.24.0.73019 --target 11.12.5 --work <run>/work --from journeys

## Journeys on the NEW app (exit 1): REGRESSION/FAIL is a gate FAIL, INVALID blocks DONE, SCREEN REVIEW needs both images opened and a reason in shot-accept.txt (exit 11)

file: <run>/work/journeys-after.out

