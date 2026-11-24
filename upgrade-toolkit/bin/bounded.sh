#!/usr/bin/env bash
# bounded.sh SECS CMD [ARG...]: run CMD, kill it after SECS seconds, exit 124 when it timed out, in every mode, KILL needed or not.
# Why (GF-34, a field run): `docker info` hung 22 minutes on a Docker CLI plugin and the run said nothing. Every docker probe the
# toolkit makes goes through this. macOS has no `timeout`: GNU timeout, else gtimeout (brew install coreutils), else perl's alarm
# (ships with macOS), else a bash watchdog. Never silently unlimited. BOUNDED_FORCE=watchdog|perl picks one (controls).
secs=${1:?usage: bounded.sh SECS CMD [ARG...]}; shift
[ $# -gt 0 ] || { echo "usage: bounded.sh SECS CMD [ARG...]" >&2; exit 2; }
mode=${BOUNDED_FORCE:-}
if [ -z "$mode" ]; then
  if command -v timeout > /dev/null 2>&1; then mode=timeout
  elif command -v gtimeout > /dev/null 2>&1; then mode=gtimeout
  elif command -v perl > /dev/null 2>&1; then mode=perl
  else mode=watchdog; fi
fi
case $mode in
  timeout|gtimeout)   # -k: KILL 2 s after TERM, like the perl and watchdog modes. GNU timeout then returns 137, not 124: a command that
    # ignores TERM must still read as "timed out" (callers check only 124), so 137 after a full bound is mapped to 124.
    t0=$SECONDS; rc=0
    "$mode" -k 2 "$secs" "$@" || rc=$?
    [ "$rc" -ne 137 ] || [ $((SECONDS - t0)) -lt $((secs + 1)) ] || rc=124
    exit "$rc" ;;
  perl)  # alarm kills the child with SIGALRM: shell status 142, mapped to 124
    perl -e '$s = shift; $p = fork(); if (!$p) { exec @ARGV or exit 127 } $SIG{ALRM} = sub { kill 9, $p; waitpid $p, 0; exit 124 }; alarm $s; waitpid $p, 0; exit($? & 127 ? 128 + ($? & 127) : $? >> 8)' "$secs" "$@"
    exit $? ;;
  *)
    "$@" & pid=$!
    ( sleep "$secs"; kill -9 "$pid" 2> /dev/null ) > /dev/null 2>&1 & wd=$!
    rc=0; wait "$pid" 2> /dev/null || rc=$?
    if kill -0 "$wd" 2> /dev/null; then kill "$wd" 2> /dev/null; wait "$wd" 2> /dev/null || true; exit "$rc"; fi
    exit 124 ;;
esac
