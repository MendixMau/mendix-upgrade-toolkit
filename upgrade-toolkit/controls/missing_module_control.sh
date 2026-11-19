#!/bin/bash
# Controls for bin/repair/missing_module_stop.py (issue 24: an updated module needs a module the app lacks).
# The missing_deps.txt it reads is the REAL output of repair/missing_deps.py on a fixture model; the app is a real git repo whose
# "step:" commit adds the bytes of a reference, as a module update does.
#   missing_module_control.sh CASE MISSING_DEPS_PY MODEL_DIR CATALOG B
case=$1; MD=$2; MODEL=$3; CAT=$4; B=$5
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
APP=$T/app; mkdir -p "$APP"; git -C "$APP" init -q; git -C "$APP" config user.email t@t; git -C "$APP" config user.name t
printf '1 4.7.0 Atlas_Core\n2 1.0.0 Other\n' > "$T/plan.txt"
mkapp() { # mkapp <commit that adds the reference: step|init>
  printf 'binary \x00 page' > "$APP/unit.mxunit"; git -C "$APP" add -A; git -C "$APP" commit -qm "init"
  if [ "$1" = step ]; then printf 'binary \x00 UserCommons.SNIP_Header \x00' > "$APP/unit.mxunit"; git -C "$APP" commit -qam "step: Atlas_Core 4.7.0 (stepupdate, idcheck PASS)"
  else printf 'binary \x00 UserCommons.SNIP_Header \x00' > "$APP/unit.mxunit"; git -C "$APP" commit -qam "init: dangling already"; fi; }
deps() { python3 "$MD" --catalog "$CAT" ${1:+--target $1} "$MODEL" > "$T/deps.txt"; }
run() { python3 "$B/repair/missing_module_stop.py" "$T/deps.txt" "$T/plan.txt" --app "$APP" "$@"; echo "exit $?"; }
case $case in
  update-introduced) mkapp step; deps; run ;;
  above-target) mkapp step; deps 10.6.0; run ;;
  already-dangling) mkapp init; deps; run ;;
  acked) mkapp step; deps; echo 'UserCommons comes from the Marketplace import of the platform team' > "$T/ack.txt"; run --ack "$T/ack.txt" ;;
  nothing-missing) mkapp step; python3 "$MD" "$(dirname "$MODEL")/base" > "$T/deps.txt" 2>/dev/null; run ;;
  no-git) deps; python3 "$B/repair/missing_module_stop.py" "$T/deps.txt" "$T/plan.txt" --app "$T"; echo "exit $?" ;;
  *) echo "no case $case"; exit 2 ;;
esac
