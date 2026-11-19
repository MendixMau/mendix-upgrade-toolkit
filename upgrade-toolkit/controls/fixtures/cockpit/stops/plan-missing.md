# NEEDS JUDGMENT: step triage, exit 13

run folder: <run>
work: <run>/work
source 9.24.23.37735 -> target 10.24.0.73019
Rule: the items below are pending, not passed: a REGRESSION is fixed, the rest are decided in writing (allow/approved files named in steps/*.md), then rerun:

    <toolkit>/upgrade-toolkit/bin/cloud/upgrade-pipeline.sh --app-zip <run>/dl/App.mpk --source 9.24.23.37735 --target 10.24.0.73019 --target2 11.12.5 --work <run>/work --from triage

## Module plan missing: write <run>/work/plan.txt (exit 13)

No script picks module target versions (steps/triage.md item 3: newest version whose min Mendix fits the target, from the brain's modules-index.md and `mxcli marketplace versions <content id>`).
Write `<run>/work/plan.txt`: one line per module, `<content id> <version> <Module>`, cross-module association targets (idcheck --xmod) LAST. An empty plan (comments only) is allowed and means no module updates.
Write `<run>/work/module-jumps.txt`: `<Module> <installed> -> <target>` lines for the release-impact rows. Optional: `<run>/work/plan-pre.txt` (updates BEFORE the convert, 10.x sources only), `<run>/work/localedits.args` (one `--cid Module=ID` or `--proxy Module=VER` argument per line), `<run>/work/env-values.json` (the environment's constants, same for old and new).

## localedits result (exit 13)

file: <run>/work/localedits.md
