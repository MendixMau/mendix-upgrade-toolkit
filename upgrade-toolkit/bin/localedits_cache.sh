#!/usr/bin/env bash
# localedits_cache.sh: reuse the triage localedits result when nothing it read has changed.
#
#   localedits_cache.sh check APP WORK [ARG ...]   exit 0 = the earlier result is still good (prints its exit code), 1 = redo
#   localedits_cache.sh save  APP WORK RC [ARG ...]   record the result: only RC 0 and 1 are kept (2 = some module UNKNOWN: redo)
#
# Why (GA1): the module plan has no script, so triage stops with exit 13 "write plan.txt, rerun --from triage". The rerun repeated
# localedits.py --mxcli-diff in full: 16 modules, about 15 minutes of `mxcli marketplace diff`, to print the same table.
# The stamp is the hash of the app's git HEAD, the content of its uncommitted changes (`git diff HEAD`) and of its untracked files
# (a file already dirty and edited again changes the stamp), bin/localedits.py itself, the localedits ARGs (--mxcli-diff, --cid,
# --proxy ...) and the mxcli version the run recorded ($WORK/state/mxcli-version). A changed model, localedits.py, a new
# localedits.args line or another mxcli redoes it; UPG_LOCALEDITS_FRESH=1 forces a redo. Needs $WORK/localedits.json and .md.
# An app where `git rev-parse HEAD` fails is never cached (check = redo, save = nothing kept); a missing rc file is a miss.
# NOT in the key: the mpk cache (a marketplace module re-downloaded or changed upstream), the network, and UPG_MXCLI (the binary
# path; only the recorded mxcli version counts). UPG_LOCALEDITS_FRESH=1 is the way to redo after any of those.
set -u
cmd=${1:-}; app=${2:-}; work=${3:-}
[ -n "$cmd" ] && [ -n "$app" ] && [ -n "$work" ] || { echo "usage: localedits_cache.sh check|save APP WORK [RC] [ARG ...]" >&2; exit 2; }
shift 3
rc=""
if [ "$cmd" = save ]; then rc=${1:-}; [ -n "$rc" ] || { echo "localedits_cache: save needs RC" >&2; exit 2; }; shift; fi
head=$(git -C "$app" rev-parse HEAD 2>/dev/null) || head=""
[ -n "$head" ] || { [ "$cmd" = check ] && exit 1; [ "$cmd" = save ] && exit 0; }
here=$(cd "$(dirname "$0")" && pwd)
stamp=$({ echo "$head"; git -C "$app" diff HEAD 2>/dev/null | sha256sum
          (cd "$app" && git ls-files -o --exclude-standard -z 2>/dev/null | sort -z | xargs -0 sha256sum 2>/dev/null)
          sha256sum < "$here/localedits.py" 2>/dev/null
          [ $# -eq 0 ] || printf '%s\n' "$@"
          cat "$work/state/mxcli-version" 2>/dev/null; } | sha256sum | cut -c1-16)
st="$work/state/localedits.stamp"; rcf="$work/state/localedits.rc"
case "$cmd" in
  check)
    [ "${UPG_LOCALEDITS_FRESH:-0}" != 1 ] && [ -s "$work/localedits.json" ] && [ -s "$work/localedits.md" ] \
      && [ "$(cat "$st" 2>/dev/null)" = "$stamp" ] || exit 1
    cat "$rcf" 2>/dev/null || exit 1 ;;
  save)
    case "$rc" in 0|1) mkdir -p "$work/state"; printf '%s\n' "$stamp" > "$st"; printf '%s\n' "$rc" > "$rcf";; *) rm -f "$st" "$rcf";; esac ;;
  *) echo "localedits_cache: unknown command $cmd" >&2; exit 2;;
esac
