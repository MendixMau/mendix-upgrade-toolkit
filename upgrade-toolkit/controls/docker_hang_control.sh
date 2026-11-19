#!/usr/bin/env bash
# docker_hang_control.sh MODE [SETUP.sh]: GM-4. A `docker` that never answers must not hang bin/setup-container.sh.
#   MODE: timeout   (real timeout/gtimeout on PATH if the host has one)   fallback (PATH without timeout and gtimeout: the bash 3.2 helper)
#         orphans (fast commands through the fallback leave no orphaned sleep)
#         images    (the docker daemon answers `info`, but `image inspect` hangs; step images)   plan  (--plan with a hung daemon)
# Prints "elapsed ok" when setup returned within 12 s of a 2 s UPG_DOCKER_TIMEOUT, then "rc=<setup exit code>" and setup's output.
# The control's own guard kills setup after 15 s, so a setup that still hangs (origin/main) FAILS here instead of hanging the suite.
TK=$(cd "$(dirname "$0")/.." && pwd); MODE=${1:?mode}; SETUP=${2:-$TK/bin/setup-container.sh}
W=$(mktemp -d "${TMPDIR:-/tmp}/dockhang.XXXXXX"); trap 'rm -rf "$W"' EXIT
mkdir -p "$W/fake" "$W/path" "$W/h"
# fake docker: sleeps forever (the images mode answers `info` and hangs on everything else)
if [ "$MODE" = images ]; then
  printf '#!/bin/sh\n[ "$1" = info ] && exit 0\nexec sleep 1000\n' > "$W/fake/docker"
else printf '#!/bin/sh\nexec sleep 1000\n' > "$W/fake/docker"; fi
chmod +x "$W/fake/docker"
# a PATH made of symlinks to exactly the tools setup uses, so "no timeout" is a real absence
for c in true bash env sh sleep date mktemp rm kill pkill dirname basename head tr cat ls readlink seq zsh uname wc cut grep sed awk mkdir pwd python3 git; do
  p=$(command -v "$c" 2>/dev/null); case "$p" in /*) ln -sf "$p" "$W/path/$c";; esac
done
if [ "$MODE" != fallback ] && [ "$MODE" != orphans ]; then for c in timeout gtimeout; do p=$(command -v "$c" 2>/dev/null); case "$p" in /*) ln -sf "$p" "$W/path/$c";; esac; done; fi
[ "$MODE" != fallback ] && [ "$MODE" != orphans ] || { [ ! -e "$W/path/timeout" ] && [ ! -e "$W/path/gtimeout" ] || { echo "control error: timeout on PATH"; exit 9; }; }
if [ "$MODE" = orphans ]; then
  # upg_timeout (the real function, cut out of SETUP) on fast commands, no timeout on PATH: no `sleep 7919` may outlive the calls, and rc stays honest
  # no pkill on the PATH: the old watchdog's `pkill -P` cleaned its sleep up when a pkill existed, the leak only shows without one
  rm -f "$W/path/pkill"
  sed -n '/^upg_timeout()/,/^}/p' "$SETUP" > "$W/fn.sh"
  [ -s "$W/fn.sh" ] || { echo "control error: upg_timeout not found"; exit 0; }
  out=$(env -i PATH="$W/path" bash -c ". '$W/fn.sh'; for i in 1 2 3 4 5; do upg_timeout 7919 true || echo BAD-true-\$?; done; upg_timeout 7919 sh -c 'exit 3'; echo rc3=\$?; upg_timeout 2 sleep 1000; echo rc124=\$?; sleep 1" 2>&1)
  echo "$out"
  n=$(ps -eo args | grep -c '^sleep 7919$')
  echo "leftover sleep 7919: $n"
  pkill -f '^sleep 7919$' 2>/dev/null
  exit 0
fi
args=("$W/run" 11.6.3); steps=docker
case "$MODE" in images) steps=images;; plan) args=(--plan "$W/run" 11.6.3);; esac
start=$(date +%s)
env -i HOME="$W/h" PATH="$W/fake:$W/path" UPG_SETUP_STEPS=$steps UPG_DOCKER_TIMEOUT=2 bash "$SETUP" "${args[@]}" > "$W/out" 2>&1 &
pid=$!
( sleep 15; pkill -P "$pid" 2>/dev/null; kill "$pid" 2>/dev/null ) >/dev/null 2>&1 & wd=$!
rc=0; wait "$pid" 2>/dev/null || rc=$?
pkill -P "$wd" 2>/dev/null; kill "$wd" 2>/dev/null; wait "$wd" 2>/dev/null
pkill -f "$W/fake" 2>/dev/null; pkill -f 'sleep 1000' -P 1 2>/dev/null
el=$(( $(date +%s) - start ))
if [ "$el" -le 12 ]; then echo "elapsed ok"; else echo "elapsed $el s: setup hung"; fi
echo "rc=$rc"; cat "$W/out"
exit 0
