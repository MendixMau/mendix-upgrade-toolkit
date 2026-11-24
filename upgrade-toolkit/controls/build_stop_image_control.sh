#!/bin/bash
# Control for the build stop's image line (issue 33): cuts the build-stop `if` block out of upgrade-pipeline.sh (from the
# `[ "$DRY" != 1 ] && { [ "$rc" != 0 ]` line to its closing `  fi`) and runs it against stubs, so the check is about the stop path,
# not about the words appearing somewhere in the 4000-line file.
# Usage: build_stop_image_control.sh <upgrade-pipeline.sh> <stop|ok>
#   stop: rc=2, a build log with mxbuild's image line  -> $WORK/build-image.txt written, a "Build image" item added
#   ok:   rc=0, no errors, the package exists          -> the block does not run: no build-image.txt, no "Build image" item
set -u
src=${1:?pipeline file}; mode=${2:?stop|ok}
blk=$(awk '/^  if \[ "\$DRY" != 1 \] && \{ \[ "\$rc" != 0 \] \|\| \[ "\$n" != 0 \]/{f=1} f{print} f&&/^  fi$/{exit}' "$src")
[ -n "$blk" ] || { echo "FAIL block: build-stop if not found in $src"; exit 1; }
WORK=$(mktemp -d); trap 'rm -rf "$WORK"' EXIT
TARGET=10.24.16; DRY=0; n=0; rc=2
printf 'mx10.sh: mxbuild image mig-mx10-j11\nERROR at x\n' > "$WORK/build-$TARGET.log"
mda_new() { echo "$WORK/new.mda"; }
if [ "$mode" = ok ]; then rc=0; : > "$WORK/new.mda"; fi
items=$WORK/items
nj_meta() { :; }; nj_add() { echo "ITEM $2" >> "$items"; }; nj_file() { echo "ITEM $2" >> "$items"; }; nj_flush() { :; }
disk_cause() { :; }; xo() { :; }; python3() { :; }
eval "$blk"
got=absent; [ -s "$WORK/build-image.txt" ] && got=$(cat "$WORK/build-image.txt")
item=none; grep -q '^ITEM Build image' "$items" 2> /dev/null && item=Build-image
echo "build-image.txt: $got"; echo "item: $item"
if [ "$mode" = stop ]; then want_f="mx10.sh: mxbuild image mig-mx10-j11"; want_i=Build-image; else want_f=absent; want_i=none; fi
[ "$got" = "$want_f" ] && [ "$item" = "$want_i" ] && { echo "ok   $mode path"; exit 0; }
echo "FAIL $mode path: expected build-image.txt '$want_f' and item $want_i"; exit 1
