#!/bin/bash
# setup_prompt_control.sh [FILE]: DV-7. SETUP-PROMPT.md carries both run modes (a default unattended text and a marked
# attended block), and everything the attended block names exists in the toolkit. Exit 0 = ok, 1 = a problem.
TK=$(cd "$(dirname "$0")/.." && pwd); F=${1:-$TK/SETUP-PROMPT.md}; bad=0
fail() { echo "FAIL: $1"; bad=1; }
grep -q 'unattended, until the gate says PASS' "$F" || fail "the unattended default sentence is missing"
if ! { grep -q '^<!-- ATTENDED-START -->$' "$F" && grep -q '^<!-- ATTENDED-END -->$' "$F"; }; then
  fail "no marked attended block"; echo "setup-prompt: problems"; exit 1; fi
blk=$(sed -n '/^<!-- ATTENDED-START -->$/,/^<!-- ATTENDED-END -->$/p' "$F")
for w in 'You never sign for me' 'Signed-off:' 'NEEDS-JUDGMENT.md'; do echo "$blk" | grep -q "$w" || fail "attended block lacks: $w"; done
for t in $(echo "$blk" | grep -oE '`(bin|steps)/[A-Za-z0-9_./-]+`' | tr -d '`'); do [ -e "$TK/$t" ] || fail "named path does not exist: $t"; done
for t in $(echo "$blk" | grep -oE '\$B/[A-Za-z0-9_.-]+' | sed 's#\$B/#bin/#'); do [ -e "$TK/$t" ] || fail "named tool does not exist: $t"; done
for e in $(echo "$blk" | grep -oE '`UPG_[A-Z_]+`' | tr -d '`'); do grep -rq "$e" "$TK/bin" || fail "named variable is in no script: $e"; done
for fl in $(echo "$blk" | grep -oE '(^|[ (`])--[a-z][a-z-]+' | tr -d ' (`' | sort -u); do
  grep -q -- "$fl" "$TK/bin/cloud/upgrade-pipeline.sh" "$TK/bin/decisions.py" || fail "named flag is in no script: $fl"; done
grep -q 'interview-mode.txt' "$TK/bin/cloud/upgrade-pipeline.sh" || fail "pipeline does not read interview-mode.txt"
grep -q 'item == "signoff"' "$TK/bin/cockpitserve.py" || fail "cockpit server has no signoff item"
grep -q -- '--source' "$TK/bin/decisions.py" || fail "decisions.py has no --source"
grep -q 'pending' "$TK/bin/decisions.py" || fail "decisions.py has no pending"
[ $bad = 0 ] && echo "setup-prompt: ok"; exit $bad
