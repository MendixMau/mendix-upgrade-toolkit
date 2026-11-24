#!/usr/bin/env bash
# SW-15 control: run_journeys.py against a FAKE runner (a `node` stand-in on PATH that writes the findings file the real runner writes)
# and a throwaway local HTTP server for the "is the app alive" probe. No browser, no Mendix app.
#   entry_probe_control.sh BIN_DIR TMP_DIR SCENARIO
# SCENARIO: shared (14 journeys, 12 of them share one first step that is broken: probed, then the rest are BLOCKED-BY-ENTRY),
#           optout (the same set with --no-entry-probe: all 14 walked), unique (a broken step that is NOT the shared first step:
#           every journey is walked and fails normally), compare (the old app's entry is broken, the new app's is not: the
#           baseline blocks, the new app walks all, the rung is INVALID and says so, never a regression or a baseline defect).
# Review fixes (PR 204):
#   suspect       100 journeys, ONE stray step-1 failure on a step nothing else shares: the runner processes are counted (4, not 28)
#   gen           journeys from the REAL gen_journeys.py (fixtures/sw15/actions.json): 12 action journeys on one page each have their
#                 own ui.ready, and still share an entry
#   mixed         the entry fails two different ways: no single broken step, nothing blocked
#   flaky         the entry passed once: not broken, nothing blocked
#   only          --only walks the journeys as asked, no probing
#   appdown       the app dies while the entry is being probed: nothing blocked, --resume walks every journey not run
#   resumeblocked --resume walks the journeys that were blocked at the entry
#   comparefail   a new-app FAIL behind an old-app block is BASELINE NOT WALKED, not a baseline defect
#   datafail      a step-1 data check that is INVALID is no entry failure
#   unit          coverage(): the DEFECT_MAX denominator leaves the blocked out, blocked journeys are no baseline defect
set -u
B=$1; T=$2; SC=$3
here=$(cd "$(dirname "$0")" && pwd)
G=$T/gen; W=$T/work; mkdir -p "$G/journeys/Admin" "$W" "$T/bin"
rm -rf "$W"/* "$G/journeys/Admin"/* "$G/journeys/Clerk"
if [ "$SC" = unit ]; then
  python3 - "$B" <<'PY'
import sys
sys.path.insert(0, sys.argv[1])
import run_journeys as r
def cov(before, now):
    links = {j: [] for j in now}
    return r.coverage(now, before, {"links": links, "sha256": "x"}, {"sha256": "x"}, None, "unit", [], True)
# 20 journeys on the baseline: 7 PASS, 5 FAIL, 8 blocked at the entry. 5 of the 12 that ran failed: 41%, over DEFECT_MAX 30%.
# Counted over all but the deferred (20) it would be 25%: the blocked are not a measurement, so they are left out of the base.
before = {}
for i in range(7): before[f"p{i}"] = {"verdict": "PASS"}
for i in range(5): before[f"f{i}"] = {"verdict": "FAIL", "not_pass": ["x"]}
for i in range(8): before[f"b{i}"] = {"verdict": "INVALID", "blocked_by_entry": {"step": "s"}}
now = {j: {"verdict": "PASS"} for j in before}
c = cov(before, now)
print("D Z:", c["D"], c["Z"])
print("measuring:", [m for m in c["invalid"] if m.startswith("instrument not measuring")])
print("defects:", sorted(c["defects"]))
# the same counts with the 8 blocked walked as PASS: 5 of 20 = 25%, not over the line
c2 = cov({**before, **{f"b{i}": {"verdict": "PASS"} for i in range(8)}}, now)
print("walked all, measuring:", [m for m in c2["invalid"] if m.startswith("instrument not measuring")])
PY
  exit 0
fi
if [ "$SC" = gen ]; then   # REAL generator output, never hand-written journeys
  python3 "$B/gen_journeys.py" --actions "$here/fixtures/sw15/actions.json" --out-dir "$G" --roles-with-users Clerk >"$T/gen.out" 2>&1 \
    || { echo "FAIL gen_journeys: $(tail -2 "$T/gen.out")"; exit 1; }
  ROLE=Clerk
else
  ROLE=Admin
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
elif sc == "suspect":   # j000 has a first step nothing else shares; the other 99 sit 5 to a page, 20 pages: no group big enough to be probed
    names.append(("j000", [own(999), second(0)]))
    for i in range(1, 100):
        names.append((f"j{i:03d}", [own(i // 5), second(i)]))
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
fi
echo "{\"$ROLE\": {\"user\": \"u\", \"pass\": \"p\"}}" > "$T/users.json"
cat > "$T/bin/node" <<'NODE'
#!/usr/bin/env python3
import json, os, re, signal, sys, time
files = [f for f in sys.argv[2:] if f.endswith(".journey.json")]
open(os.environ["FAKE_LOG"], "a").write("batch: %s\n" % " ".join(os.path.basename(f).split(".journey")[0] for f in files))
os.makedirs("artifacts", exist_ok=True)
E = os.environ.get
broken = E("FAKE_BROKEN_ENTRY") == "1"          # every journey that starts with the shared "role home" step fails there
late = E("FAKE_LATE_FAIL") == "1"               # every journey fails its SECOND step
prefix = E("FAKE_BROKEN_PREFIX")                # every journey whose first step name starts with this fails there (gen)
fail_ids = set(filter(None, (E("FAKE_FAIL_IDS") or "").split(",")))
pass_ids = set(filter(None, (E("FAKE_PASS_IDS") or "").split(",")))
mixed = E("FAKE_MIXED") == "1"                  # the entry fails two ways, by the number in the journey id
datafail = E("FAKE_DATAFAIL") == "1"            # step 1 lands, then its data check is INVALID
walks = []
for f in files:
    j = json.load(open(f)); time.sleep(0.05)
    if j["id"] == E("FAKE_KILL_AT") and E("FAKE_SRV_PID"):   # the app dies while this journey is walked
        os.kill(int(open(E("FAKE_SRV_PID")).read()), signal.SIGTERM); time.sleep(0.4)
    steps = []
    for k, st in enumerate(j["steps"]):
        nm = st["name"]
        bad = k == 0 and j["id"] not in pass_ids and ((broken and nm == "role home") or j["id"] in fail_ids or (prefix and nm.startswith(prefix)))
        if bad:
            how = "actions completed" if mixed and int(re.sub(r"\D", "", j["id"]) or 0) % 2 == 0 else "reached"
            checks = [{"verdict": "FAIL", "name": f"{nm}: {how}", "detail": "card container never rendered"}]
            if how == "reached":
                checks.append({"verdict": "INVALID", "name": f"{nm}: downstream rungs", "detail": "not reached; nothing measured"})
        elif k == 0 and datafail:
            checks = [{"verdict": "PASS", "name": f"{nm}: reached", "detail": ""}, {"verdict": "INVALID", "name": f"{nm}: data rung", "detail": "no rows"}]
        else:
            bad2 = late and k == 1
            checks = [{"verdict": "FAIL" if bad2 else "PASS", "name": f"{nm}: reached", "detail": "never appeared" if bad2 else ""}]
        steps.append({"n": k + 1, "checks": checks})
        if bad:
            break
    walks.append({"journey": j["id"], "steps": steps})
json.dump({"results": [{"rung": "ui", "name": "login", "verdict": "PASS", "detail": ""}], "walks": walks}, open("artifacts/journey-findings.json", "w"))
NODE
chmod +x "$T/bin/node"
PORT=$((20000 + $$ % 20000))
SRV=
start_srv() {   # waits until the port answers: a fixed sleep is flaky under load
  ( cd "$T" && exec python3 -m http.server "$PORT" --bind 127.0.0.1 >/dev/null 2>&1 ) & SRV=$!
  echo $SRV > "$T/srv.pid"
  python3 - "$PORT" <<'PY' || { echo "FAIL stand-in server did not come up"; exit 1; }
import socket, sys, time
for _ in range(100):
    try:
        socket.create_connection(("127.0.0.1", int(sys.argv[1])), 0.2).close(); sys.exit(0)
    except OSError:
        time.sleep(0.1)
sys.exit(1)
PY
}
start_srv
trap 'kill $SRV 2>/dev/null' EXIT
export FAKE_LOG=$T/fake.log
rm -f "$FAKE_LOG"
run() { PATH="$T/bin:$PATH" python3 "$B/run_journeys.py" "$G" --label "${LABEL:-t}" --work "$W" --port "$PORT" --admin-port 1 --admin-pass x --users "$T/users.json" --no-actions fixture "$@"; }
ran() { echo "walked: $(sed 's/^batch: //' "$FAKE_LOG" | tr ' ' '\n' | grep -c .) journeys"; }
procs() { echo "runner processes: $(grep -c '^batch: ' "$FAKE_LOG")"; }
tally() { python3 -c "
import json, sys
j = json.load(open(sys.argv[1]))['journeys']
v = {}
for s in j.values(): v[s['verdict']] = v.get(s['verdict'], 0) + 1
print('summary', len(j), 'journeys:', ', '.join(f'{n} {k}' for k, n in sorted(v.items())), '| blocked_by_entry', sum(1 for s in j.values() if s.get('blocked_by_entry')), '| app_down', sum(1 for s in j.values() if s.get('app_down')))" "${1:-$W/t}/summary.json"; }
case $SC in
  shared)
    FAKE_BROKEN_ENTRY=1 run >"$T/out.txt" 2>"$T/err.txt"; echo "rc $?"
    ran; tally | sed 's/ | app_down 0$//'
    grep -c 'BLOCKED-BY-ENTRY: not walked' "$T/out.txt" | sed 's/^/blocked lines: /'
    grep -E '^entry: ' "$T/err.txt" | sed 's/ on b[0-9]*.*$/ ... /'
    grep -E '^  entry probe: ' "$T/out.txt" | sed 's/about [0-9]* min/about N min/; s/[0-9]* s each/S s each/'
    python3 -c "import json,sys; s=json.load(open(sys.argv[1])); b=s['journeys']['b12']; print('b12', b['verdict'], 'probes', ','.join(b['blocked_by_entry']['probes']), '| ok journeys walked:', s['journeys']['a-ok1']['verdict'], s['journeys']['c-ok2']['verdict'])" "$W/t/summary.json";;
  optout)
    FAKE_BROKEN_ENTRY=1 run --no-entry-probe >"$T/out.txt" 2>"$T/err.txt"; echo "rc $?"
    ran; tally | sed 's/ | app_down 0$//'; grep -c 'BLOCKED-BY-ENTRY' "$T/out.txt" | sed 's/^/blocked lines: /';;
  unique)
    FAKE_LATE_FAIL=1 run >"$T/out.txt" 2>"$T/err.txt"; echo "rc $?"
    ran; tally | sed 's/ | app_down 0$//'; grep -c 'BLOCKED-BY-ENTRY' "$T/out.txt" | sed 's/^/blocked lines: /'
    grep -E '^  FAIL +w1 ' "$T/out.txt" | cut -c1-60;;
  compare)
    LABEL=before FAKE_BROKEN_ENTRY=1 run >"$T/old.out" 2>/dev/null; echo "old rc $?"; tally "$W/before" | sed 's/ | app_down 0$//'
    LABEL=t2 run --compare "$W/before" >"$T/out.txt" 2>"$T/err.txt"; echo "new rc $?"; tally "$W/t2" | sed 's/ | app_down 0$//'
    grep -E 'not run: entry step broken' "$T/out.txt" | sed 's/^actions.*\(14 journeys\)/\1/' | cut -c1-200
    grep -E 'coverage INVALID: not measured' "$T/out.txt" | cut -c1-140
    grep -c '\[REGRESSION\]' "$T/out.txt" | sed 's/^/regression lines: /';;
  suspect)
    FAKE_FAIL_IDS=j000 run >"$T/out.txt" 2>"$T/err.txt"; echo "rc $?"
    ran; procs; tally | sed 's/ | app_down 0$//'
    : > "$FAKE_LOG"
    LABEL=t3 FAKE_FAIL_IDS=j000 run --no-entry-probe >"$T/out3.txt" 2>"$T/err3.txt"; echo "opt-out rc $?"; procs | sed 's/^/opt-out /';;
  gen)
    FAKE_BROKEN_PREFIX="open Shop.Home" run >"$T/out.txt" 2>"$T/err.txt"; echo "rc $?"
    ran; tally | sed 's/ | app_down 0$//'
    python3 -c "
import json,sys
a=set(json.load(open(sys.argv[1]))['journeys']['act-Shop.Home.btn12']['blocked_by_entry']['probes']); print('btn12 probes', ','.join(sorted(a)))
import glob
ks=set()
sys.path.insert(0, sys.argv[2]); import run_journeys as r
for f in glob.glob(sys.argv[3]+'/journeys/Clerk/act-Shop.Home.*.journey.json'): ks.add(r.entry_key(json.load(open(f))))
print('entry keys for 12 journeys of one page:', len(ks))
print('own ready widgets:', len({json.load(open(f))['steps'][0]['ui']['ready'] for f in glob.glob(sys.argv[3]+'/journeys/Clerk/act-Shop.Home.*.journey.json')}))" "$W/t/summary.json" "$B" "$G"
    python3 -c "import json,sys; print('Other page journey:', json.load(open(sys.argv[1]))['journeys']['act-Shop.Other.btnZ']['verdict'])" "$W/t/summary.json";;
  mixed)
    FAKE_BROKEN_ENTRY=1 FAKE_MIXED=1 run --chunk 3 >"$T/out.txt" 2>"$T/err.txt"; echo "rc $?"
    ran; tally | sed 's/ | app_down 0$//';;
  flaky)
    FAKE_BROKEN_ENTRY=1 FAKE_PASS_IDS=b01 run --chunk 3 >"$T/out.txt" 2>"$T/err.txt"; echo "rc $?"
    ran; tally | sed 's/ | app_down 0$//';;
  only)
    FAKE_BROKEN_ENTRY=1 run --only a-ok1,b01,b02,b03,b04,b05,b06,b07,b08,b09,b10,b11,b12,c-ok2 >"$T/out.txt" 2>"$T/err.txt"; echo "rc $?"
    ran; tally | sed 's/ | app_down 0$//';;
  datafail)
    FAKE_DATAFAIL=1 run >"$T/out.txt" 2>"$T/err.txt"; echo "rc $?"
    ran; tally | sed 's/ | app_down 0$//';;
  appdown)
    FAKE_BROKEN_ENTRY=1 FAKE_KILL_AT=b03 FAKE_SRV_PID=$T/srv.pid run >"$T/out.txt" 2>"$T/err.txt"; echo "rc $?"
    ran; tally
    : > "$FAKE_LOG"; start_srv   # the app is back: --resume walks what was not run
    run --resume >"$T/out2.txt" 2>"$T/err2.txt"; echo "resume rc $?"
    echo "resume $(ran)"; tally;;
  resumeblocked)
    FAKE_BROKEN_ENTRY=1 run >"$T/out.txt" 2>"$T/err.txt"; echo "rc $?"
    tally | sed 's/ | app_down 0$//'
    : > "$FAKE_LOG"
    run --resume >"$T/out2.txt" 2>"$T/err2.txt"; echo "resume rc $?"
    echo "resume $(ran)"; tally | sed 's/ | app_down 0$//';;
  comparefail)
    LABEL=before FAKE_BROKEN_ENTRY=1 run >"$T/old.out" 2>/dev/null; echo "old rc $?"; tally "$W/before" | sed 's/ | app_down 0$//'
    LABEL=t2 FAKE_LATE_FAIL=1 run --compare "$W/before" >"$T/out.txt" 2>"$T/err.txt"; echo "new rc $?"; tally "$W/t2" | sed 's/ | app_down 0$//'
    python3 -c "
import json,sys,collections
c=collections.Counter((s.get('compare') or '-').split(' (')[0] for s in json.load(open(sys.argv[1]))['journeys'].values())
[print('compare', k + ':', n) for k, n in sorted(c.items())]" "$W/t2/summary.json";;
esac
