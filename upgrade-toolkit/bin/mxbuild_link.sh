#!/usr/bin/env bash
# mxbuild_link.sh TOOLS_DIR VERSION...: make `mxcli` find the mxbuild toolset a run already has.
#
# `mxcli marketplace diff` (localedits --mxcli-diff, triage) looks for its toolchain at ~/.mxcli/mxbuild/<version>. The pipeline's own
# toolsets live in $UPG_TOOLS/mxbuild-<version>. bin/cloud/setup.sh links one to the other (step mxlinks), but a run folder made by
# hand over shared toolsets never runs setup.sh. Then every module came back "mxcli diff: UNKNOWN (Comparing across versions ...
# refused; hint: run 'mxcli setup mxbuild --version <v>')" - 16 of 16 modules on GA1, a misleading reason and a 1.2 GB download
# for a toolset sitting next to the run (GA1 triage, 2026-11-20).
# For each VERSION: when $TOOLS_DIR/mxbuild-<version> is a directory and ~/.mxcli/mxbuild/<version> is missing or a dangling link,
# link it. A real directory or a working link already there is never touched. Prints one line per link made. Exit 0 always
# (a missing toolset is the pipeline's own need_path check, not this script's); 2 = usage.
set -u
tools=${1:-}; [ -n "$tools" ] && [ $# -ge 2 ] || { echo "usage: mxbuild_link.sh TOOLS_DIR VERSION..." >&2; exit 2; }
shift
dest="${HOME:-/root}/.mxcli/mxbuild"
for v in "$@"; do
  [ -n "$v" ] || continue
  [ -d "$tools/mxbuild-$v" ] || continue
  if [ -e "$dest/$v" ]; then continue; fi        # exists and resolves: leave it
  mkdir -p "$dest" && ln -sfn "$tools/mxbuild-$v" "$dest/$v" && echo "mxbuild_link: $dest/$v -> $tools/mxbuild-$v"
done
exit 0
