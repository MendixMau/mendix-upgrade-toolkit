#!/bin/bash
# stepcheck-run.sh APP.mpr LOG: `mx check` of an app under the heavy lock, for stepupdate's per-step model check (GM-23).
# The toolset is the one of the app's own Mendix version (mxversion.py), so a pass before the convert checks with the old
# toolset and one after it with the new. Writes LOG as mx prints it, the document of each error appended (checkwhere.py),
# and a `[error] [MXCHECK]` line when mx died without a summary: a crash is never "0 errors" (stepcheck.py reads that line).
# Producer of the log stepcheck.py compares; consumer: stepupdate.sh (UPG_STEPCHECK_CMD, set by upgrade-pipeline.sh).
# Exit 0 always when a log was written; 2 on input error.
set -u
mpr=${1:?usage: stepcheck-run.sh APP.mpr LOG}; log=${2:?}
bin=$(cd "$(dirname "$0")" && pwd)
ver=$(python3 "$bin/mxversion.py" "$mpr" --short 2> /dev/null) || { echo "stepcheck-run: no Mendix version in $mpr" >&2; exit 2; }
# RM-3: a toolset unpacked under its full name (mxbuild-10.24.0.73019, what the pipeline's --source names) is not found by the
# short version; without this the check said "no .../mxbuild-10.24.0/modeler/mx" and every step was STEPCHECK NOT RUN.
tools=${UPG_TOOLS:-${UPG_ROOT:-$(pwd)}/tools}
if [ ! -e "$tools/mxbuild-$ver" ]; then
  full=$(python3 "$bin/mxversion.py" "$mpr" 2> /dev/null || true)
  [ -z "$full" ] || [ ! -e "$tools/mxbuild-$full" ] || ver=$full
fi
major=${ver%%.*}; w="$bin/mx10.sh"; [ "$major" -gt 9 ] || w="$bin/mx9.sh"
j=(); cj="${log%.log}.json"; rm -f "$cj"
[ "$major" -le 9 ] || j=(-j "$cj")
"$bin/heavy-lock.sh" check "$w" "$ver" mx check "$mpr" ${j[@]+"${j[@]}"} > "$log" 2>&1 || true
[ ! -s "$cj" ] || python3 "$bin/checkwhere.py" "$cj" "$log" || true
if ! grep -q 'The app contains:' "$log" 2> /dev/null; then
  printf '[error] [MXCHECK] mx check ended without a result: %s\n' "$(grep -m1 -E '^ERROR' "$log" 2> /dev/null | cut -c1-200 || true)" >> "$log"
fi
exit 0
