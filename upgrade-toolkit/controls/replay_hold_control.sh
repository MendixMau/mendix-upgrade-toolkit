#!/usr/bin/env bash
# replay_hold_control.sh CASE: replay_edits and step_gate from the pipeline on a real git app with a fake mxcli.
# A failed replay is held (its changes undone, the run goes on) and the gate stops 13 on replay-held.txt.
#   fail     the replay writes half the model and a new unit, then fails
#   dirty    the same, on a tree that was not clean before the replay (cannot be undone: the old stop)
#   ok       the replay succeeds after an earlier run held it (the held line goes)
#   gate     step_gate with a held replay: stop 13
#   gate-ack the same with replay-held-ack.txt: the gate goes through
set -euo pipefail
P=$(cd "$(dirname "$0")/../bin/cloud" && pwd)/upgrade-pipeline.sh
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
APP=$T/app WORK=$T/work DRY=0 MPR=$T/app/App.mpr B=$T/b
mkdir -p "$APP" "$WORK/replay" "$WORK/state" "$B"
echo orig > "$MPR"
git -C "$APP" init -q; git -C "$APP" add -A; git -C "$APP" -c user.name=c -c user.email=c@c commit -qm original
echo 'create page Mod.P;' > "$WORK/replay/Mod.mdl"
git_app() { git -C "$APP" -c user.name=c -c user.email=c@c "$@"; }
xo() { local o=$1; shift; "$@" > "$o" 2>&1; }
note() { echo "note: $*"; }
Q=""
nj_file() { echo "STOP $1: $2"; Q=$1; }
nj_add() { echo "STOP $1: $2"; Q=$1; }
nj_flush() { [ -z "$Q" ] || { echo "EXIT $Q"; exit "$Q"; }; }
commit_app() { git_app add -A; git_app commit -qm "$1"; echo "commit: $1"; }
write_summary() { :; }
record_runlog() { :; }
case "$1" in
  fail|dirty) mxcli_run() { echo half > "$MPR"; echo unit > "$APP/new.unit"; echo "MDL081 refused" >&2; return 3; } ;;
  *) mxcli_run() { echo replayed > "$MPR"; } ;;
esac
eval "$(sed -n '/^replay_edits() {/,/^}/p' "$P")"
eval "$(sed -n '/^step_gate() {/,/^}/p' "$P")"
case "$1" in
  dirty) echo stray > "$APP/stray.txt"; replay_edits ;;
  ok) echo "Mod exit 3: old (log: x)" > "$WORK/replay-held.txt"; echo "Other exit 1: y (log: z)" >> "$WORK/replay-held.txt"; replay_edits ;;
  gate|gate-ack) echo 'Mod exit 3: r (log: l)' > "$WORK/replay-held.txt"; : > "$WORK/release-impact.md"; printf '#!/bin/sh\n' > "$B/release_impact.py"
        [ "$1" = gate ] || echo 'Mod exit 3: accepted, the page edit is redone by hand' > "$WORK/replay-held-ack.txt"
        step_gate; echo "gate went through"; exit 0 ;;
  *) replay_edits ;;
esac
echo "mpr: $(cat "$MPR")"
echo "untracked: $(git_app ls-files --others --exclude-standard | tr '\n' ' ')"
[ ! -f "$WORK/replay-held.txt" ] || sed 's/^/held: /' "$WORK/replay-held.txt"
echo "commits: $(git_app log --format=%s | tr '\n' '|')"
