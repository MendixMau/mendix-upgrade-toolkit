#!/usr/bin/env bash
# cockpit-up.sh: start the live cockpit server for a work folder if it is not already running. No browser, no opener.
#
# Usage: cockpit-up.sh --work WORK [--out COCKPIT.html] [--keep-work]
#   --out        where the one cockpit lives (default WORK/COCKPIT.html); the server's folder is its dirname
#   --keep-work  resume.sh: leave an existing <folder>/.cockpit-work alone (it names the rung that is running; a pipeline that
#                is running rewrites it at its next step) and build the page view from that rung
# Writes <folder>/.cockpit-work (what /status reads), refreshes COCKPIT-view.html (only when it changed), and starts
# bin/cockpitserve.py when <folder>/.cockpit-pid is not a live process: never a second server for the same folder.
# Prints one line: "started PORT", "running PORT" or "failed: REASON". Server output goes to <folder>/.cockpit-serve.log.
# Called by cockpit_live (upgrade-pipeline.sh, whether or not a browser opener exists: DV-4) and by resume.sh (DV-10).
# Exit: 0 server up, 1 not up (the line says why), 2 usage.
set -u
B=$(cd "$(dirname "$0")/.." && pwd)
W=""; OUT=""; KEEP=0
while [ $# -gt 0 ]; do
  case "$1" in --work) W=${2:-}; shift 2 ;; --out) OUT=${2:-}; shift 2 ;; --keep-work) KEEP=1; shift ;; *) sed -n 2,4p "$0" >&2; exit 2 ;; esac
done
[ -n "$W" ] && [ -d "$W" ] || { echo "cockpit-up.sh: --work needs an existing folder" >&2; exit 2; }
W=$(cd "$W" && pwd)
d=$(dirname "${OUT:-$W/COCKPIT.html}"); mkdir -p "$d" 2> /dev/null || { echo "failed: cannot make $d"; exit 1; }
view=$W
if [ "$KEEP" = 1 ] && [ -s "$d/.cockpit-work" ] && [ -d "$(cat "$d/.cockpit-work")" ]; then view=$(cat "$d/.cockpit-work")
else echo "$W" > "$d/.cockpit-work"; fi
mkdir -p "$W/logs"
if ! python3 "$B/cockpitpage.py" --work "$view" --out "$d/.COCKPIT-view.new" --standalone --live >> "$W/logs/decisions.log" 2>&1; then
  rm -f "$d/.COCKPIT-view.new"; echo "failed: cockpitpage.py could not write the page (see $W/logs/decisions.log)"; exit 1
fi
if cmp -s "$d/.COCKPIT-view.new" "$d/COCKPIT-view.html"; then rm -f "$d/.COCKPIT-view.new"; else mv "$d/.COCKPIT-view.new" "$d/COCKPIT-view.html"; fi
state=running
if ! { [ -f "$d/.cockpit-pid" ] && kill -0 "$(cat "$d/.cockpit-pid")" 2> /dev/null; }; then
  state=started; rm -f "$d/.cockpit-port"
  nohup python3 "$B/cockpitserve.py" --dir "$d" > "$d/.cockpit-serve.log" 2>&1 < /dev/null &
  for _ in 1 2 3 4 5 6 7 8 9 10; do [ -s "$d/.cockpit-port" ] && break; sleep 0.3; done
fi
port=$(cat "$d/.cockpit-port" 2> /dev/null || true)
if [ -z "$port" ]; then echo "failed: cockpitserve.py wrote no port ($(tail -n 1 "$d/.cockpit-serve.log" 2> /dev/null | cut -c1-120)), see $d/.cockpit-serve.log"; exit 1; fi
echo "$state $port"
