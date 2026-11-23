#!/usr/bin/env bash
# GF-50 control: run_journeys.py against a FAKE runner (a `node` stand-in on PATH that writes the findings file the real runner
# writes, one PASS walk per journey) and a throwaway local HTTP server for the "is the app alive" probe. No browser, no Mendix app.
#   journeys_cap_control.sh BIN_DIR TMP_DIR SCENARIO
# SCENARIO: checkpoint (the runner process is killed in its 3rd batch: summary.json must hold the 2 batches before it, and --resume
#           must run the rest), cap (--max 4 of 7: tier order, the dropped count printed, listed deferred), nocap (no flag: all run).
set -u
B=$1; T=$2; SC=$3
G=$T/gen; W=$T/work; mkdir -p "$G/journeys/Admin" "$W" "$T/bin"
rm -rf "$W"/* "$G/journeys/Admin"/*
python3 - "$G" <<'PY'
import json, sys
g = sys.argv[1]
# 7 journeys: 2 always-on, 2 impact-picked (menu), 3 plain; sorted by file name = the set order, always-on first
spec = [("a1-login-Admin", ["always-on: login per role"], "always-on: login"), ("a2-sign-out", ["always-on: sign out"], "always-on: sign out"),
        ("b1-menu", ["impact:Shop.P1"], ""), ("b2-menu", ["impact:Shop.P2"], ""), ("c1-act", ["action:Shop.x1"], ""), ("c2-act", ["action:Shop.x2"], ""), ("c3-act", ["action:Shop.x3"], "")]
for i, (jid, req, why) in enumerate(spec):
    d = {"id": jid, "title": jid, "persona": "Admin", "requirement": req, "_why": why, "steps": [{"n": 1, "do": "noop"}]}
    json.dump(d, open(f"{g}/journeys/Admin/{jid}.journey.json", "w"))
json.dump({"role_order": ["Admin"]}, open(f"{g}/plan.json", "w"))
PY
echo '{"Admin": {"user": "u", "pass": "p"}}' > "$T/users.json"
cat > "$T/bin/node" <<'NODE'
#!/usr/bin/env python3
import json, os, sys
files = [f for f in sys.argv[2:] if f.endswith(".journey.json")]
cnt = os.environ["FAKE_COUNT"]
n = int(open(cnt).read() or 0) + 1 if os.path.exists(cnt) else 1
open(cnt, "w").write(str(n))
open(os.environ["FAKE_LOG"], "a").write("batch %d: %s\n" % (n, " ".join(os.path.basename(f).split(".")[0] for f in files)))
if os.environ.get("FAKE_KILL_AT") == str(n):
    os.kill(os.getppid(), 9); sys.exit(1)
os.makedirs("artifacts", exist_ok=True)
res = [{"rung": "ui", "name": "login", "verdict": "PASS", "detail": ""}]
walks = []
for f in files:
    j = json.load(open(f))
    walks.append({"journey": j["id"], "steps": [{"n": 1, "checks": [{"verdict": "PASS", "name": "c", "detail": ""}]} for _ in j["steps"]]})
json.dump({"results": res, "walks": walks}, open("artifacts/journey-findings.json", "w"))
NODE
chmod +x "$T/bin/node"
PORT=$((20000 + $$ % 20000))
( cd "$T" && exec python3 -m http.server "$PORT" --bind 127.0.0.1 >/dev/null 2>&1 ) & SRV=$!
trap 'kill $SRV 2>/dev/null' EXIT
sleep 1
export FAKE_COUNT=$T/count FAKE_LOG=$T/fake.log
rm -f "$FAKE_COUNT" "$FAKE_LOG"
run() { PATH="$T/bin:$PATH" python3 "$B/run_journeys.py" "$G" --label t --work "$W" --port "$PORT" --admin-port 1 --admin-pass x --users "$T/users.json" --no-actions fixture "$@"; }
count() { python3 -c "import json,sys; d=json.load(open(sys.argv[1])); j=d['journeys']; print('summary', len(j), 'journeys,', sum(1 for s in j.values() if s.get('verdict')=='PASS'), 'PASS,', sum(1 for s in j.values() if s.get('deferred')), 'deferred, partial', d.get('partial', False))" "$W/t/summary.json"; }
case $SC in
  checkpoint)
    FAKE_KILL_AT=3 run --chunk 2 >/dev/null 2>&1
    echo "run killed in batch 3"; count
    rm -f "$FAKE_COUNT"; run --resume --chunk 2 >/dev/null 2>"$T/resume.err"; echo "resume rc $?"; grep '^resume:' "$T/resume.err"; count;;
  cap)
    run --max 4 --chunk 2 2>&1 | grep -E '^cap:|^deferred:'; count
    echo "ran: $(sed 's/^batch [0-9]*: //' "$FAKE_LOG" | tr '\n' ' ')";;
  budget)
    run --budget-min 0.01 --chunk 2 2>&1 | grep -E '^cap:|^deferred:'; count;;
  nocap)
    run --chunk 3 2>&1 | grep -E '^cap:|^deferred:'; echo "rc ${PIPESTATUS[0]}"; count;;
esac
