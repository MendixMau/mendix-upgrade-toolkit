#!/usr/bin/env bash
# SW-15 control: run_journeys.py against a FAKE runner (a `node` stand-in on PATH that writes the findings file the real runner writes)
# and a throwaway local HTTP server for the "is the app alive" probe. No browser, no Mendix app.
#   entry_probe_control.sh BIN_DIR TMP_DIR SCENARIO
# SCENARIO: shared (14 journeys, 12 of them share one first step that is broken: probed, then the rest are BLOCKED-BY-ENTRY),
#           optout (the same set with --no-entry-probe: all 14 walked), unique (a broken step that is NOT the shared first step:
#           every journey is walked and fails normally), compare (the old app's entry is broken, the new app's is not: the
#           baseline blocks, the new app walks all, the rung is INVALID and says so, never a regression or a baseline defect).
set -u
B=$1; T=$2; SC=$3
G=$T/gen; W=$T/work; mkdir -p "$G/journeys/Admin" "$W" "$T/bin"
rm -rf "$W"/* "$G/journeys/Admin"/*
python3 - "$G" "$SC" <<'PY'
import json, sys
g, sc = sys.argv[1], sys.argv[2]
HOME = {"name": "role home", "actions": [{"do": "nav", "item": "Home"}], "ui": {"ready": "card-container"}}
def own(i):
    return {"name": f"open page {i}", "actions": [{"do": "nav", "item": f"Page{i}"}], "ui": {"ready": f"page{i}"}}
def second(i):
    return {"name": f"act {i}", "actions": [{"do": "click", "widget": f"btn{i}"}], "ui": {"ready": f"done{i}"}}
names = []
if sc == "unique":   # u01..u03 share a first step that WORKS and a second step that fails; w1 has a unique first step that works and a unique second that fails
    for i in (1, 2, 3):
        names.append((f"u0{i}", [HOME, second(i)]))
    names.append(("w1", [own(9), second(9)]))
else:
    names.append(("a-ok1", [own(1), second(1)]))
    for i in range(1, 13):
        names.append((f"b{i:02d}", [HOME, second(i)]))
    names.append(("c-ok2", [own(2), second(2)]))
for jid, steps in names:
    d = {"id": jid, "title": jid, "persona": "Admin", "requirement": ["impact:Shop." + jid], "_why": "", "steps": [dict(s, n=k + 1) for k, s in enumerate(steps)]}
    json.dump(d, open(f"{g}/journeys/Admin/{jid}.journey.json", "w"))
json.dump({"role_order": ["Admin"]}, open(f"{g}/plan.json", "w"))
PY
echo '{"Admin": {"user": "u", "pass": "p"}}' > "$T/users.json"
cat > "$T/bin/node" <<'NODE'
#!/usr/bin/env python3
import json, os, sys, time
files = [f for f in sys.argv[2:] if f.endswith(".journey.json")]
open(os.environ["FAKE_LOG"], "a").write("batch: %s\n" % " ".join(os.path.basename(f).split(".")[0] for f in files))
os.makedirs("artifacts", exist_ok=True)
broken = os.environ.get("FAKE_BROKEN_ENTRY") == "1"   # every journey that starts with the shared "role home" step fails there
late = os.environ.get("FAKE_LATE_FAIL") == "1"        # every journey fails its SECOND step
walks = []
for f in files:
    j = json.load(open(f)); time.sleep(0.05)
    steps = []
    for k, st in enumerate(j["steps"]):
        bad = (broken and k == 0 and st["name"] == "role home") or (late and k == 1)
        steps.append({"n": k + 1, "checks": [{"verdict": "FAIL" if bad else "PASS", "name": "ready", "detail": "card container never rendered" if bad else ""}]})
    walks.append({"journey": j["id"], "steps": steps})
json.dump({"results": [{"rung": "ui", "name": "login", "verdict": "PASS", "detail": ""}], "walks": walks}, open("artifacts/journey-findings.json", "w"))
NODE
chmod +x "$T/bin/node"
PORT=$((20000 + $$ % 20000))
( cd "$T" && exec python3 -m http.server "$PORT" --bind 127.0.0.1 >/dev/null 2>&1 ) & SRV=$!
trap 'kill $SRV 2>/dev/null' EXIT
sleep 1
export FAKE_LOG=$T/fake.log
rm -f "$FAKE_LOG"
run() { PATH="$T/bin:$PATH" python3 "$B/run_journeys.py" "$G" --label "${LABEL:-t}" --work "$W" --port "$PORT" --admin-port 1 --admin-pass x --users "$T/users.json" --no-actions fixture "$@"; }
ran() { echo "walked: $(sed 's/^batch: //' "$FAKE_LOG" | tr ' ' '\n' | grep -c .) journeys"; }
tally() { python3 -c "
import json, sys
j = json.load(open(sys.argv[1]))['journeys']
v = {}
for s in j.values(): v[s['verdict']] = v.get(s['verdict'], 0) + 1
print('summary', len(j), 'journeys:', ', '.join(f'{n} {k}' for k, n in sorted(v.items())), '| blocked_by_entry', sum(1 for s in j.values() if s.get('blocked_by_entry')))" "${1:-$W/t}/summary.json"; }
case $SC in
  shared)
    FAKE_BROKEN_ENTRY=1 run >"$T/out.txt" 2>"$T/err.txt"; echo "rc $?"
    ran; tally
    grep -c 'BLOCKED-BY-ENTRY: not walked' "$T/out.txt" | sed 's/^/blocked lines: /'
    grep -E '^entry: ' "$T/err.txt" | sed 's/ on b[0-9]*.*$/ ... /'
    grep -E '^  entry probe: ' "$T/out.txt" | sed 's/about [0-9]* min/about N min/; s/[0-9]* s each/S s each/'
    python3 -c "import json,sys; s=json.load(open(sys.argv[1])); b=s['journeys']['b12']; print('b12', b['verdict'], 'probes', ','.join(b['blocked_by_entry']['probes']), '| ok journeys walked:', s['journeys']['a-ok1']['verdict'], s['journeys']['c-ok2']['verdict'])" "$W/t/summary.json";;
  optout)
    FAKE_BROKEN_ENTRY=1 run --no-entry-probe >"$T/out.txt" 2>"$T/err.txt"; echo "rc $?"
    ran; tally; grep -c 'BLOCKED-BY-ENTRY' "$T/out.txt" | sed 's/^/blocked lines: /';;
  unique)
    FAKE_LATE_FAIL=1 run >"$T/out.txt" 2>"$T/err.txt"; echo "rc $?"
    ran; tally; grep -c 'BLOCKED-BY-ENTRY' "$T/out.txt" | sed 's/^/blocked lines: /'
    grep -E '^  FAIL +w1 ' "$T/out.txt" | cut -c1-60;;
  compare)
    LABEL=before FAKE_BROKEN_ENTRY=1 run >"$T/old.out" 2>/dev/null; echo "old rc $?"; tally "$W/before"
    LABEL=t2 run --compare "$W/before" >"$T/out.txt" 2>"$T/err.txt"; echo "new rc $?"; tally "$W/t2"
    grep -E 'not run: entry step broken' "$T/out.txt" | sed 's/^actions.*\(14 journeys\)/\1/' | cut -c1-200
    grep -E 'coverage INVALID: not measured' "$T/out.txt" | cut -c1-140
    grep -c '\[REGRESSION\]' "$T/out.txt" | sed 's/^/regression lines: /';;
esac
