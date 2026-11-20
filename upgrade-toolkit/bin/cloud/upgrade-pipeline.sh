#!/usr/bin/env bash
# upgrade-pipeline.sh: run every FIXED step of a Mendix upgrade with no model, stop at the first step that needs judgment.
#
# Usage: upgrade-pipeline.sh (--app-zip PATH | --app-dir DIR) --source FULL --target FULL [--target2 FULL] --work DIR
#                            [--from STEP] [--only STEP] [--dry-run]
#   --app-zip PATH   a project zip/mpk, unpacked into <run>/app and put under its own git ("original" commit)
#   --app-dir DIR    an unpacked project folder (own git is created when it has none)
#   --to FULL        instead of --target/--target2: the version ladder picks the route (9.x to 11 goes through 10.24;
#                    --via 10.24.x.y names that toolset, else the newest mxbuild-10.24.* in UPG_TOOLS) and writes <work>/ladder.json.
#   --source/--target/--target2  FULL versions (10.24.26.123458; 11.x may be 11.15.0). With --target2 the script runs
#                    rung 1 (source -> target), then calls itself for rung 2 (target -> target2) in <work>/rung2.
#   --work DIR       $WORK of steps/*.md (state/, logs/, evidence). Sources $WORK/env.sh or $RUN/env.sh (bin/cloud/setup.sh).
#   --from STEP      forget the done markers of STEP and every later step, then run from there. An earlier step that is
#                    not done is never run: heal and apidirect are skipped by name (optional); any other refuses the run
#                    (exit 2, names the steps; rerun without --from to continue, or run one step with --only)
#   --only STEP      run just that step (even when done)
#   --dry-run        print the commands, run nothing
#   --cockpit        run no step: only regenerate $WORK/COCKPIT.html (needs just --work)
#   --brief          run no step: print the plain brief (where the upgrade stands, what is broken, what to do now, open
#                    questions) from the same model as the cockpit's top (bin/brief.py). Also printed at every stop and at the end.
# Steps, in order: fetch triage baseline basewalk propose convert update build after afterwalk journeys heal diff gate
# heal (steps/heal.md): classifies every failing row, heals what belongs to the test (start noise, selection-gated buttons, a runner
# that did not run, outside calls via apimock, known harness log lines) and reruns only the affected journeys, at most 2 rounds.
# UPG_HEAL=0 turns it off (journeys then stops on a failure as before). Resume it with --from heal.
# UPG_SMOKE_MICROFLOWS: the smoke walks (basewalk, afterwalk) follow microflow homes and menu items (smokewalk.js
# --microflows) whenever the plan has them; UPG_SMOKE_MICROFLOWS=0 turns that off. Safe: each walk runs on its own copy of
# the frozen DB. Needed when a role reaches its pages through microflows (WM1: the User home and both menu items; cold
# CMM: 13 of 23 steps, two roles judged on no page at all, and the skip was reported only when the walk was INVALID).
# Each finished step writes $WORK/state/<step>.done and is skipped on the next run. Logs: $WORK/logs/<step>.log.
# Judgment stops write $WORK/NEEDS-JUDGMENT.md. Exit codes:
#    0 gate PASS, nothing left for a person
#    2 usage / version-path error
#    3 missing tool or setup (run bin/cloud/setup.sh), an mxcli of another version than the run's (bin/mxcli_pin.sh), or the app dir
#      is not a working git tree at a step start (bin/apptree.sh, GM-10)
#    4 a fixed step failed unexpectedly (see the log named in the message)
#   10 mx check / mxbuild / quick start errors after convert+update: repair needed (steps/repair.md)
#   11 journeys INVALID or FAIL on the old app or the new one: fix the journey or write the todo (steps/journeys.md)
#   12 diff / gate REVIEW, FAIL or INVALID items need a comparison by a person (steps/gate.md). A FAIL is never a pass.
#   13 module plan missing, or a module kept / a replay held / a data-bearing finding needs a decision (steps/upgrade.md)
#   14 the upgrade proposal awaits sign-off ($WORK/PROPOSAL.md section 6, steps/propose.md); also when a plan input changed
#      after the sign-off (the sign-off is cleared). Nothing in the app model has changed yet.
#   15 the owner paused the run on purpose (`Status: PAUSED <reason>` in PROPOSAL.md); NEEDS-JUDGMENT.md has the resume command
# Interview mode unattended (env UPG_INTERVIEW_MODE=unattended, or a line `Interview mode: unattended` in $WORK/interview-mode.txt):
# the propose step signs nothing, records ASSUMED (unattended) in DECISIONS.md, goes on, and every report says 'proposal not signed'.
# Interview mode auto (UPG_INTERVIEW_MODE=auto, or `Interview mode: auto`): the same at propose, and a judgment stop that nothing
# after it depends on (journeys, idcheck, smoke walk, diff, gate: nj_park) is parked in $WORK/parked/<step>.md and the run goes on;
# at the end NEEDS-JUDGMENT.md lists every parked item grouped by kind (bin/parked.py) and the run exits with the first code.
# A build or start failure, a missing plan or a replay that cannot be undone still stops at once (nj_flush).
# Decisions (bin/decisions.py): at the start of the run and of every step the pipeline applies $WORK/decisions.json (the page buttons
# and the chat share it); after every step, and when a step stops, it regenerates $WORK/COCKPIT.html (bin/cockpitpage.py).
# Hidden options for rung 2 (set by this script): --db NAME --old-mda PATH --seed-from DB
set -Eeuo pipefail

ARGS_ORIG=("$@")
SELF=$(readlink -f "${BASH_SOURCE[0]}")
TK="$(cd "$(dirname "$SELF")/../.." && pwd)"
APP_ZIP=""; APP_DIR_ARG=""; SOURCE=""; TARGET=""; TARGET2=""; WORK=""; TO=""; VIA=""
FROM=""; ONLY=""; DRY=0; COCKPIT=0; BRIEF=0; DB_ARG=""; OLD_MDA=""; SEED_FROM=""

STEPS=(fetch triage baseline basewalk propose convert update build after afterwalk journeys heal apidirect diff gate)
SMOKE_PW='Smoke-only-1!'
M2EE_PASS='m2ee-local-only'          # runapp.py's admin API password
PGC=mig-pg                           # runapp.py's Postgres container

usage_die() { echo "upgrade-pipeline.sh: $*" >&2; echo "usage: $0 (--app-zip PATH|--app-dir DIR) --source FULL --target FULL [--target2 FULL] --work DIR [--from STEP] [--only STEP] [--dry-run]" >&2; exit 2; }
die4() { echo "upgrade-pipeline.sh: $*" >&2; exit 4; }
on_err() { echo "upgrade-pipeline.sh: unexpected failure (exit $1) at line $2 in step '${STEP:-none}'; log: ${LOG:-none}" >&2; exit 4; }
trap 'on_err $? $LINENO' ERR

while [ $# -gt 0 ]; do
  case "$1" in
    --app-zip) APP_ZIP=${2:-}; shift 2 ;;
    --app-dir) APP_DIR_ARG=${2:-}; shift 2 ;;
    --source) SOURCE=${2:-}; shift 2 ;;
    --target) TARGET=${2:-}; shift 2 ;;
    --target2) TARGET2=${2:-}; shift 2 ;;
    --to) TO=${2:-}; shift 2 ;;
    --via) VIA=${2:-}; shift 2 ;;
    --work) WORK=${2:-}; shift 2 ;;
    --from) FROM=${2:-}; shift 2 ;;
    --only) ONLY=${2:-}; shift 2 ;;
    --db) DB_ARG=${2:-}; shift 2 ;;
    --old-mda) OLD_MDA=${2:-}; shift 2 ;;
    --seed-from) SEED_FROM=${2:-}; shift 2 ;;
    --dry-run) DRY=1; shift ;;
    --cockpit) COCKPIT=1; shift ;;
    --brief) BRIEF=1; shift ;;
    -h|--help) sed -n 2,43p "$SELF"; exit 0 ;;
    *) usage_die "unknown argument: $1" ;;
  esac
done

[ -n "$WORK" ] || usage_die "--work is required"
if [ "${BRIEF:-0}" = 1 ]; then   # step-free: the brief of the cockpit's top, in the terminal
  [ -d "$WORK" ] || usage_die "no such folder: $WORK"
  exec python3 "$TK/bin/brief.py" --work "$(cd "$WORK" && pwd)"
fi
if [ "$COCKPIT" = 1 ]; then   # step-free: regenerate the cockpit page and stop
  [ -d "$WORK" ] || usage_die "no such folder: $WORK"
  WORK=$(cd "$WORK" && pwd)
  exec python3 "$TK/bin/cockpitpage.py" --work "$WORK" --out "$WORK/COCKPIT.html"
fi
[ -n "$SOURCE" ] || usage_die "--source is required"
# --to: the version ladder. The pipeline picks the route from the start version: 9.x and 10.x below 10.24 go through 10.24
# (--via, else the newest mxbuild-10.24.* toolset in UPG_TOOLS) before 11; anything else is one rung.
if [ -n "$TO" ]; then
  [ -z "$TARGET$TARGET2" ] || usage_die "--to replaces --target and --target2: give one or the other"
  _sm=${SOURCE%%.*}; _sr=${SOURCE#*.}; _sn=${_sr%%.*}; _tm=${TO%%.*}
  if [ "$_tm" -ge 11 ] && { [ "$_sm" -le 9 ] || { [ "$_sm" -eq 10 ] && [ "$_sn" -lt 24 ]; }; }; then
    if [ -z "$VIA" ]; then
      VIA=$(ls -d "${UPG_TOOLS:-$(dirname "$WORK")/tools}"/mxbuild-10.24.* 2>/dev/null | sed 's#.*/mxbuild-##' | sort -t. -k3,3n -k4,4n | tail -1 || true)
      [ -n "$VIA" ] || usage_die "$SOURCE goes to $TO through 10.24: no mxbuild-10.24.* toolset found, give --via 10.24.x.y"
    fi
    TARGET=$VIA; TARGET2=$TO
  else
    TARGET=$TO
  fi
  echo "upgrade-pipeline.sh: version ladder $SOURCE -> $TARGET${TARGET2:+ -> $TARGET2}"
fi
[ -n "$TARGET" ] || usage_die "--target is required"
{ [ -n "$APP_ZIP" ] || [ -n "$APP_DIR_ARG" ]; } || usage_die "one of --app-zip / --app-dir is required"
{ [ -z "$APP_ZIP" ] || [ -z "$APP_DIR_ARG" ]; } || usage_die "--app-zip and --app-dir are exclusive"
[ -z "$APP_ZIP" ] || [ -f "$APP_ZIP" ] || usage_die "no such file: $APP_ZIP"
[ -z "$APP_DIR_ARG" ] || [ -d "$APP_DIR_ARG" ] || usage_die "no such folder: $APP_DIR_ARG"
for v in "$SOURCE" "$TARGET" ${TARGET2:+"$TARGET2"}; do
  [[ "$v" =~ ^[0-9]+\.[0-9]+\.[0-9]+(\.[0-9]+)?$ ]] || usage_die "'$v' is not a full version (10.24.26.123458)"
done
for s in "$FROM" "$ONLY"; do
  [ -z "$s" ] || [[ " ${STEPS[*]} " == *" $s "* ]] || usage_die "unknown step '$s' (steps: ${STEPS[*]})"
done

major() { echo "${1%%.*}"; }
minor() { local r=${1#*.}; echo "${r%%.*}"; }
# Version path rules (SKILL.md): 9 goes to 10, 10.x goes to 10.24 first, then to 11.
path_check() { # from to
  local fm tm
  fm=$(major "$1"); tm=$(major "$2")
  [ "$tm" -ge "$fm" ] || usage_die "target $2 is older than source $1"
  if [ "$fm" -le 9 ] && [ "$tm" -ge 11 ]; then usage_die "9.x goes to 10.24 first: use --target 10.24.x --target2 $2"; fi
  if [ "$fm" -eq 10 ] && [ "$tm" -ge 11 ] && [ "$(minor "$1")" -lt 24 ]; then
    usage_die "10.$(minor "$1") may not go to $2: take 10.24 first (--target 10.24.x --target2 $2)"; fi
}
path_check "$SOURCE" "$TARGET"
if [ -n "$TARGET2" ]; then
  [ "$(major "$TARGET2")" -ge 11 ] && [ "$(major "$TARGET")" -eq 10 ] && [ "$(minor "$TARGET")" -eq 24 ] ||
    usage_die "--target2 is the 11.x rung and --target must be 10.24.x"
fi

mkdir -p "$WORK"; WORK=$(cd "$WORK" && pwd)
mkdir -p "$WORK/state" "$WORK/logs"
# the route of this run, for the cockpit's version ladder (rung 2 keeps the one rung 1 wrote)
[ "$(basename "$WORK")" = rung2 ] || [ "$DRY" = 1 ] ||
  printf '{"route": ["%s", "%s"%s]}\n' "$SOURCE" "$TARGET" "${TARGET2:+, \"$TARGET2\"}" > "$WORK/ladder.json"

# ---- env.sh from bin/cloud/setup.sh: TK RUN MXCLI UPG_EXTRA UPG_UPDATE_CMD UPG_TOOLS ----
_tk=${TK:-}   # cold rfq run: env.sh's stale TK (~/Mendix/mxcli-project-toolkit/...) replaced this pipeline's own; exit 2
# A RUN from the caller's environment counts only when --work lies inside it (setup.sh exports it so). Cold WM1: a
# wrapper's own RUN=13 became the run folder, "missing source mxbuild toolset: 13/tools/..." and exit 3.
if [ -n "${RUN:-}" ]; then
  _rd=$(cd "$RUN" 2>/dev/null && pwd) || _rd=""
  case "$(cd "$WORK" && pwd)/" in
    "${_rd:-/nonexistent}"/*) ;;
    *) echo "upgrade-pipeline.sh: ignoring RUN=$RUN from the environment: --work $WORK is not inside it"; RUN="" ;;
  esac
fi
: "${RUN:=$(dirname "$WORK")}"
set +u
if [ -f "$WORK/env.sh" ]; then . "$WORK/env.sh"; elif [ -f "$RUN/env.sh" ]; then . "$RUN/env.sh"; fi
set -u
if [ -n "$_tk" ] && [ "$TK" != "$_tk" ]; then echo "upgrade-pipeline.sh: ignoring TK=$TK from env.sh: this pipeline runs from $_tk"; TK=$_tk; fi
: "${RUN:=$(dirname "$WORK")}"
: "${UPG_TOOLS:=$RUN/tools}"
: "${MXCLI:=${UPG_MXCLI:-}}"
B="$TK/bin"
# Apple Silicon: every container call goes to a VM with Rosetta (bin/dockerhost.sh). Cold test WM1: the run used a qemu VM,
# mxcli crashed on all 10 module updates and each was recorded as "kept".
if DH=$(bash "$B/dockerhost.sh"); then
  [ -z "$DH" ] || [ "$DH" = "${DOCKER_HOST:-}" ] || { echo "upgrade-pipeline.sh: containers run on $DH (Rosetta)"; export DOCKER_HOST="$DH"; }
elif [ "${DRY:-0}" != 1 ]; then
  exit 2
fi
PORT_OFF=${PORT_OFF:-0}
APP_PORT=$((8080 + PORT_OFF)); ADMIN_PORT=$((8090 + PORT_OFF))
export TK RUN UPG_TOOLS
export UPG_ROOT="$RUN"
# cold rfq run on a Mac: env.sh from cloud/setup.sh set MXCLI to the Linux build; -x held, the host could not exec it (triage,
# exit 126). Such a binary runs in the container (mxcli-container.sh reads MXC_MXCLI); the Python helpers use the host mxcli.
mxcli_host_check() {
  [ -n "${MXCLI:-}" ] && [ -x "$MXCLI" ] || return 0
  local rc=0; "$MXCLI" --version >/dev/null 2>&1 || rc=$?
  [ "$rc" = 126 ] || return 0
  echo "upgrade-pipeline.sh: $MXCLI does not run on this host ($(uname -s)): mxcli calls go through mxcli-container.sh"
  export MXC_MXCLI="$MXCLI"; MXCLI=""; unset UPG_MXCLI
}
mxcli_host_check
[ -z "${MXCLI:-}" ] || export UPG_MXCLI="$MXCLI"
export UPG_EXTRA="${UPG_EXTRA:-}"
export UPG_MXCLI_STATE="$WORK/state/mxcli-version"   # stepupdate.sh checks it too (bin/mxcli_pin.sh)
# two versions (--target2): every step of rung 1 belongs to the version of --target; rung 2 gets its own (set below), so one
# steps.jsonl and one COCKPIT.html cover 9 to 11 and gate 2 never rewrites the tests of gate 1 (steps.py UPG_PHASE)
[ -z "$TARGET2" ] || export UPG_PHASE=$(echo "$TARGET" | cut -d. -f1-3)
export UPG_STEPS_WORK="$WORK"   # steps.py trailer reads <work>/steps.jsonl: commits that fit a step carry Upgrade-Step (changelog.py -> steps.py done)
# F2 (Purchase Request 10.24, real run): mxrun.sh mounts only the run folder, so an --app-dir outside it was accepted and
# then failed at baseline with mxbuild's "Project file does not exist". Refuse it here, before any step runs.
if [ -n "$APP_DIR_ARG" ]; then
  _app=$(cd "$APP_DIR_ARG" && pwd -P); _run=$(mkdir -p "$RUN" && cd "$RUN" && pwd -P)
  case "$_app/" in "$_run"/*) ;; *)
    echo "upgrade-pipeline.sh: --app-dir $APP_DIR_ARG is outside the run folder $RUN; the containers only see the run folder. Move or copy the app under it (e.g. $RUN/app) and rerun." >&2
    exit 3 ;; esac
fi

APP=""; MPR=""
STEP=""; LOG="$WORK/logs/pipeline.log"; LOG_START=0
NJ_CODE=0; NJ_TMP="$WORK/state/nj.tmp"
APPS_UP=()

# ---- helpers ----
say() { printf '%s\n' "$*"; }
quoted() { printf ' %q' "$@"; }
x() { # run a command, append its output to the step log, return its exit code (never exits)
  if [ "$DRY" = 1 ]; then printf '+'; quoted "$@"; printf '\n'; return 0; fi
  { printf '+'; quoted "$@"; printf '\n'; } >> "$LOG"
  "$@" >> "$LOG" 2>&1
}
xo() { # xo FILE cmd...: like x, but the output goes to FILE (also logged by name)
  local out=$1; shift
  if [ "$DRY" = 1 ]; then printf '+'; quoted "$@"; printf ' > %q\n' "$out"; return 0; fi
  { printf '+'; quoted "$@"; printf ' > %q\n' "$out"; } >> "$LOG"
  "$@" > "$out" 2>&1
}
must() { local rc=0; x "$@" || rc=$?; [ "$rc" = 0 ] || die4 "step '$STEP': command failed (exit $rc): $*  (log: $LOG)"; }
note() { [ "$DRY" = 1 ] || printf '%s: %s\n' "$STEP" "$*" >> "$WORK/state/notes.txt"; }
need_tool() { # need_tool CMD  -> exit 3 when missing (dry-run: warn)
  command -v "$1" > /dev/null 2>&1 && return 0
  if [ "$DRY" = 1 ]; then say "WARN missing tool: $1"; return 0; fi
  echo "upgrade-pipeline.sh: missing tool '$1'. Run: bash $B/cloud/setup.sh --run-dir $RUN --source $SOURCE --target $TARGET${TARGET2:+ --target2 $TARGET2}" >&2
  exit 3
}
need_path() { # need_path PATH WHAT
  [ -e "$1" ] && return 0
  if [ "$DRY" = 1 ]; then say "WARN missing $2: $1"; return 0; fi
  echo "upgrade-pipeline.sh: missing $2: $1. Run: bash $B/cloud/setup.sh --run-dir $RUN --source $SOURCE --target $TARGET${TARGET2:+ --target2 $TARGET2}" >&2
  exit 3
}

# ---- judgment stops ----
# Who the section is for (cockpit clarity): nj_meta agent|info|person ["question" "recommended-key" "key|label|what it does"...] before the
# NEXT nj_add/nj_file. The cockpit shows an agent or info section as no question for the person, and a person section as its real
# question with the options and the recommended one ("none:<why>" in place of the key: no default exists, the page says why). A section
# without nj_meta is read as before.
# Rule for every person section (run DVS): the question says what users notice, 2-3 options each carry a plain consequence (what users
# notice, what the run does next, never an instruction to the agent), the toolkit recommends one when it can judge, and says why when it
# cannot ("none:<why>"). An option that the run can carry out itself gets `nj_writes key|file|line` so one answer is all a person does.
NJ_META=""
nj_meta() {
  NJ_META="owner: $1"; shift
  [ $# -gt 0 ] || return 0
  NJ_META="$NJ_META"$'\n'"question: $1"; local rec=$2; shift 2
  case "$rec" in   # "none:<why>": the toolkit has no default here; the page says so and gives the reason
    none:*) NJ_META="$NJ_META"$'\n'"why: ${rec#none:}" ;;
    "") ;;
    *) NJ_META="$NJ_META"$'\n'"recommended: $rec" ;;
  esac
  local o; for o in "$@"; do NJ_META="$NJ_META"$'\n'"option: $o"; done
}
nj_add() { # nj_add CODE "title" "text"
  [ "$NJ_CODE" != 0 ] || NJ_CODE=$1
  { printf '\n## %s (exit %s)\n\n' "$2" "$1"; [ -z "${NJ_META:-}" ] || printf '%s\n\n' "$NJ_META"; printf '%s\n' "$3"; } >> "$NJ_TMP"
  NJ_META=""
}
nj_file() { # nj_file CODE "title" FILE [lines] [grep-pattern]: first lines of a file (optionally only lines matching)
  local body="(file not found: $3)"
  if [ -f "$3" ]; then
    local from=1; [ "$3" != "$LOG" ] || from=$((LOG_START + 1))   # the step's own log: only the lines of this run (WM1: a stop quoted a walk of yesterday)
    if [ -n "${5:-}" ]; then body=$(tail -n "+$from" "$3" | grep -E "$5" | head -n "${4:-20}" || true); else body=$(tail -n "+$from" "$3" | head -n "${4:-20}" || true); fi
    body=$(printf 'file: %s\n\n```\n%s\n```' "$3" "$body")
  fi
  nj_add "$1" "$2" "$body"
}
# The question of a final check with open rows. Issue 20 (TBUD): "open failures, repair the cause" over 0 regressions. When the
# Progress line counts 0 regressions nothing failed: the open rows are checks that could not be measured or still need a yes or no,
# so the recommended answer is to hand them to the owner. No count (an older summary): the old wording, repair first.
gate_open_nj_meta() { # gate_open_nj_meta REGRESSIONS [NEED_A_DECISION NOT_MEASURED]: the counts of gate-summary.md's Progress line, or empty
  GATE_OPEN_TITLE="gate.sh: open FAIL / REVIEW / INVALID / NOT RUN (exit $rc: 1 = FAIL, 2 = INVALID or NOT RUN); accept in writing (allow files, steps/gate.md) or repair"
  if [ "${1:-}" = 0 ]; then
    GATE_OPEN_TITLE="No regression was found; open rows could not be measured or need a yes or no (exit $rc, gate-summary.md)"
    local what="Some checks could not be measured or still need a yes or no."
    [ -z "${2:-}${3:-}" ] || what="${3:-0} checks could not be measured yet and ${2:-0} still need a yes or no."
    nj_meta person "No regression was found. $what What should we do?" "handoff" "handoff|Hand the open lists to the owner|Nothing is broken for your users; the owner measures or accepts each open row in writing (steps/gate.md)." "accept|Accept a row in writing, with a reason|Allow files in steps/gate.md; only for a change that is intended." "repair|Repair a cause, then rerun the final check|Only if an open row turns out to be a real defect."
  else
    nj_meta person "The final check has open failures. What should we do?" "repair" "repair|Repair the cause, then rerun the gate|A real defect is fixed or handed off, never accepted." "accept|Accept a row in writing, with a reason|Allow files in steps/gate.md; only for a change that is intended."
  fi
}
rerun_cmd() { # the command that resumes at the current step: the run's own --from is dropped so the hint carries exactly one
  # Cold rfq: rung 2 gets RUN, UPG_PHASE and UPG_COCKPIT_OUT from rung 1's exec; a hint without them made the run folder
  # <work> (dirname of rung2), the app outside it, exit 3. A rung-2 hint carries them as an env prefix.
  local a=() skip=0 v pre="" e
  if [ "$(basename "$WORK")" = rung2 ]; then
    for e in RUN UPG_PHASE UPG_COCKPIT_OUT; do [ -z "${!e:-}" ] || pre+="$e=$(printf %q "${!e}") "; done
    [ -z "$pre" ] || pre="env $pre"
  fi
  for v in ${ARGS_ORIG[@]+"${ARGS_ORIG[@]}"}; do
    if [ "$skip" = 1 ]; then skip=0; continue; fi
    case "$v" in --from) skip=1; continue ;; --from=*) continue ;; esac
    a+=("$v")
  done
  printf '%s%s%s --from %s' "$pre" "$SELF" "$(quoted ${a[@]+"${a[@]}"})" "$STEP"
}
nj_flush() { # write NEEDS-JUDGMENT.md and exit with the first recorded code
  [ "$NJ_CODE" != 0 ] || return 0
  {
    printf '# NEEDS JUDGMENT: step %s, exit %s\n\nrun folder: %s\nwork: %s\nsource %s -> target %s\n' "$STEP" "$NJ_CODE" "$RUN" "$WORK" "$SOURCE" "$TARGET"
    printf 'Rule: the items below are pending, not passed: a REGRESSION is fixed, the rest are decided in writing (allow/approved files named in steps/*.md), then rerun:\n\n'
    printf '    %s\n' "$(rerun_cmd)"
    cat "$NJ_TMP"
  } > "$WORK/NEEDS-JUDGMENT.md"
  rm -f "$WORK/state/running"   # the step has ended: the page written now must not say "Running now" (reviews 02 and 03 of a lane run)
  # one row per stop (step, exit code, a fingerprint of what it said with the digits left out): the brief counts "stopped here N times
  # in a row" from the rows that agree, so a stop with a new cause is never called stuck (lane B, PMNT: three reruns, the same two FAILs)
  { mkdir -p "$WORK/state"; printf '%s\t%s\t%s\n' "$STEP" "$NJ_CODE" "$(tr -d '0-9' < "$NJ_TMP" | cksum | cut -d' ' -f1)" >> "$WORK/state/stops.tsv"; } 2> /dev/null || true
  cockpit_regen
  say "STOP    $STEP: needs judgment (exit $NJ_CODE), see $WORK/NEEDS-JUDGMENT.md"
  brief_say || true   # the brief is information: it never changes a stop's exit code
  exit "$NJ_CODE"
}
# WM1 cold test 2026-11-17: 16 stops, one question each, most answered with the recommendation. Auto mode parks the stops
# nothing later depends on and asks them all at the end (park_finish).
nj_park() { # like nj_flush, but in Interview mode auto the items go to $WORK/parked/$STEP.md and the step goes on
  [ "$NJ_CODE" != 0 ] || return 0
  if [ "$DRY" = 1 ] || ! interview_auto; then nj_flush; return 0; fi
  mkdir -p "$WORK/parked"
  { printf '<!-- park exit %s step %s -->\n' "$NJ_CODE" "$STEP"; cat "$NJ_TMP"; } >> "$WORK/parked/$STEP.md"
  say "PARKED  $STEP: exit $NJ_CODE parked (Interview mode: auto), the run goes on; $WORK/parked/$STEP.md"
  : > "$NJ_TMP"; NJ_CODE=0
}
parked_any() { [ -n "$(ls "$WORK/parked" 2> /dev/null)" ] || { [ "$(basename "$WORK")" = rung2 ] && [ -n "$(ls "$WORK/../parked" 2> /dev/null)" ]; }; }
park_finish() { # end of the run: every parked item in one NEEDS-JUDGMENT.md, exit with the first parked code
  [ "$DRY" != 1 ] && parked_any || return 0
  local also=() out first code step
  [ "$(basename "$WORK")" != rung2 ] || [ ! -d "$WORK/../parked" ] || also=(--also "$(cd "$WORK/.." && pwd)/parked")
  out=$(python3 "$B/parked.py" report --work "$WORK" --steps "${STEPS[*]}" ${also[@]+"${also[@]}"}) || return 0
  first=$(printf '%s\n' "$out" | tail -n 1); code=$(echo "$first" | cut -d' ' -f2); step=$(echo "$first" | cut -d' ' -f3)
  STEP=$step
  { printf '%s\n' "$out" | sed '$d'
    printf '\nRerun once, after the answers, from the first parked step (%s; a rung-1 step: the rung-1 command with --from %s):\n\n    %s\n' "$step" "$step" "$(rerun_cmd)"
  } > "$WORK/NEEDS-JUDGMENT.md"
  rm -f "$WORK/state/running"
  cockpit_regen
  say "STOP    auto: $(grep -c '^<!-- parked at' "$WORK/NEEDS-JUDGMENT.md") parked item(s) to answer in one round (exit $code), see $WORK/NEEDS-JUDGMENT.md"
  brief_say || true   # the brief is information: it never changes a stop's exit code
  exit "$code"
}

# nj_writes KEY|FILE|LINE ...: after nj_meta person, what answering KEY writes into the work folder (decisions.py apply does it, so
# one answer on the page or in chat is all a person does; run DVS: choosing "update" left the plan line to be written by hand)
nj_writes() { local w; for w in "$@"; do NJ_META="$NJ_META"$'\n'"writes: $w"; done; }
# widget_drop_stop: the "installed package lacks it" stop in reader words (bin/widgetfix.py names the module, the fixing version,
# what users lose); returns 1 when widgetfix has nothing, and the caller keeps the generic wording
widget_drop_stop() {
  local out q="" r="" k t1 t2 body="" opts=() ws=() mods=()
  [ -s "$WORK/widgetdrop.json" ] || return 1
  out=$(python3 "$B/widgetfix.py" "$APP" --drops "$WORK/widgetdrop.json" --plan "$WORK/plan.txt" --target "${TARGET:-}" 2> /dev/null) || return 1
  while IFS=$'\t' read -r k t1; do
    case "$k" in Q) q=$t1 ;; R) r=$t1 ;; O) opts+=("$t1") ;; W) ws+=("$t1") ;; B) body="$body$t1"$'\n' ;; esac
  done <<< "$out"
  [ -n "$q" ] && [ "${#opts[@]}" -gt 0 ] || return 1
  nj_meta info; nj_file 13 "Widget settings that update-widgets would drop: the installed widget package is older than the pages (steps/repair.md row 33)" "$WORK/widgetdrop.out" 10 '^WIDGET-DROP'
  nj_meta person "$q" "$r" "${opts[@]}"; nj_writes "${ws[@]}"
  nj_add 13 "Decision" "${body%$'\n'}"
}

# stepcheck_stop: stepupdate undid a step because it added model errors (exit 4) and wrote .stepupdate/stepcheck-stop.txt in
# widgetfix's field shape (Q question, R recommended, O options, W what answering writes, B body). Never committed before the
# check was read (GM-23 / A-1). Returns 1 when that file is missing, and the caller dies with the generic message.
stepcheck_stop() {
  local f="$APP/.stepupdate/stepcheck-stop.txt" k t1 q="" r="" body="" opts=() ws=()
  [ -s "$f" ] || return 1
  while IFS=$'\t' read -r k t1; do
    case "$k" in Q) q=$t1 ;; R) r=$t1 ;; O) opts+=("$t1") ;; W) ws+=("$t1") ;; B) body="$body$t1"$'\n' ;; esac
  done < "$f"
  [ -n "$q" ] && [ "${#opts[@]}" -gt 0 ] || return 1
  nj_meta info; nj_file 13 "A module update added model errors; the step was undone before it was committed (steps/upgrade.md, steps/repair.md)" "$WORK/stepupdate-$1.out" 14 '^(   NEW|STOP|   stepcheck)'
  nj_meta person "$q" "$r" "${opts[@]}"; nj_writes "${ws[@]}"
  nj_add 13 "Decision" "${body%$'\n'}"
  nj_flush
}

# decisions.json (page + chat) -> the files the steps read; the cockpit page from the run's files. Neither can fail a step.
decisions_apply() {
  [ "$DRY" != 1 ] || return 0
  python3 "$B/decisions.py" apply --work "$WORK" >> "$WORK/logs/decisions.log" 2>&1 || true
}
brief_say() { # the brief at a stop and at the end of a run: one answer to "what do I do next?", same words as the cockpit's top
  [ "$DRY" != 1 ] || return 0
  printf '\n'; python3 "$B/brief.py" --work "$WORK" 2> /dev/null || true; printf '\n'
}
cockpit_regen() {
  [ "$DRY" != 1 ] || return 0
  python3 "$B/cockpitpage.py" --work "$WORK" --out "$WORK/COCKPIT.html" >> "$WORK/logs/decisions.log" 2>&1 || true
  # the page must not contradict the run (cold test WM1: ghost "Not approved yet" rows, a stop bar while running); a problem is
  # said in the step log and kept in cockpit-check.txt, never a failed step
  if ! python3 "$B/cockpitcheck.py" --work "$WORK" > "$WORK/cockpit-check.txt" 2>&1; then
    say "cockpit: the page contradicts the run, see $WORK/cockpit-check.txt"; sed 's/^/  /' "$WORK/cockpit-check.txt"
  fi
  # rung 2 also refreshes the cockpit of rung 1, so the run keeps one page from start to end
  [ -z "${UPG_COCKPIT_OUT:-}" ] || [ ! -f "$WORK/COCKPIT.html" ] || cp "$WORK/COCKPIT.html" "$UPG_COCKPIT_OUT" 2>/dev/null || true
  # UPG_COCKPIT_HISTORY=1 keeps every version of the page (a demo video shows the cockpit filling up), next to the one cockpit
  if [ "${UPG_COCKPIT_HISTORY:-0}" = 1 ] && [ -f "$WORK/COCKPIT.html" ]; then
    local h; h=$(dirname "${UPG_COCKPIT_OUT:-$WORK/COCKPIT.html}")/cockpit-history; mkdir -p "$h"
    cp "$WORK/COCKPIT.html" "$h/$(date +%Y%m%d-%H%M%S)-$(basename "$(dirname "$WORK/x")").html" 2>/dev/null || true
  fi
  cockpit_live
}
# The live cockpit: from triage on (also a stop in triage), the page is open in the browser and reloads itself when it changes. bin/cockpitserve.py serves
# COCKPIT-view.html next to the one cockpit; the page polls it, and each poll is a heartbeat in .cockpit-seen. After every step
# (and at a stop) the view is rewritten, and when no tab polled in the last UPG_COCKPIT_SEEN seconds (default 90: a background
# tab polls at least once a minute) the page is opened again. On by default where a desktop is (macOS, or Linux with a display);
# UPG_COCKPIT_OPEN=0 turns it off, =1 forces it; UPG_COCKPIT_OPENER replaces the open command (controls).
cockpit_live() {
  local d opener port up state
  [ "$DRY" != 1 ] && [ "${UPG_COCKPIT_OPEN:-auto}" != 0 ] || return 0
  # from triage on: after it, or when it stops for a decision (exactly when the owner should look)
  case "${STEP:-}" in ""|fetch) [ -f "$WORK/state/triage.done" ] || return 0 ;; esac
  opener=${UPG_COCKPIT_OPENER:-}
  if [ -z "$opener" ]; then
    if [ "$(uname -s)" = Darwin ] && command -v open > /dev/null; then opener=open
    elif [ -n "${DISPLAY:-}${WAYLAND_DISPLAY:-}" ] && command -v xdg-open > /dev/null; then opener=xdg-open; fi
  fi
  d=$(dirname "${UPG_COCKPIT_OUT:-$WORK/COCKPIT.html}")
  # the server runs whether or not there is an opener (a headless host still has a cockpit to reach by URL: DV-4); only the
  # browser-open below needs one. cockpit-up.sh also writes .cockpit-work (the rung now running: /status reads its state/running
  # and step log) and the view, rewritten only when it differs, so the tab reloads on a change and not after every step.
  up=$(bash "$B/cloud/cockpit-up.sh" --work "$WORK" ${UPG_COCKPIT_OUT:+--out "$UPG_COCKPIT_OUT"} 2> /dev/null) || {
    say "cockpit: no cockpit is running: ${up#failed: }"; return 0; }
  state=${up% *}; port=${up#* }
  [ -n "$port" ] || return 0
  if [ -z "$opener" ]; then
    [ "$state" != started ] || say "cockpit: server up at http://127.0.0.1:$port/ (no browser opener here (open, xdg-open); open that URL yourself, or set UPG_COCKPIT_OPENER)"
    return 0
  fi
  if [ -f "$d/.cockpit-seen" ] && [ $(( $(date +%s) - $(python3 -c 'import os,sys; print(int(os.stat(sys.argv[1]).st_mtime))' "$d/.cockpit-seen") )) -lt "${UPG_COCKPIT_SEEN:-90}" ]; then
    return 0
  fi
  touch "$d/.cockpit-seen"   # the tab polls within seconds; until then the next step does not open a second one
  say "cockpit: server up at http://127.0.0.1:$port/ (opened in the browser; it reloads itself as the run goes)"
  $opener "http://127.0.0.1:$port/" > /dev/null 2>&1 || true
}

# ---- Postgres / apps ----
db_exists() { # db_exists NAME
  [ "$DRY" = 1 ] && return 1
  [ -n "$(docker exec "$PGC" psql -U mendix -tAc "SELECT 1 FROM pg_database WHERE datname='$1'" 2> /dev/null || true)" ]
}
fresh_name() { # fresh_name BASE: a database name no earlier snapshot, walk or probe used (ledger) and that does not exist
  local n=$1 i=1
  while db_exists "$n" || { [ -f "$WORK/db-ledger.txt" ] && grep -q "^$n " "$WORK/db-ledger.txt"; }; do i=$((i + 1)); n="${1}_r$i"; done
  echo "$n"
}
copy_db() { must docker exec "$PGC" createdb -U mendix -T "$1" "$2"; }
mark_used() { must python3 "$B/snapshot.py" --ledger "$WORK/db-ledger.txt" --mark-used "$1" --use "$2"; }
psql_str() { echo "docker exec -i $PGC psql -U mendix -d $1"; }

# Where the walks and journeys sign in: env UPG_LOGIN_PATH, else the first line of $WORK/login-path.txt, else /login.html.
# An app whose login.html is an SSO redirect needs e.g. /login-with-mendixsso-button.html (seen on a 10.24 app).
login_path() { local p="${UPG_LOGIN_PATH:-}"; [ -n "$p" ] || p=$(head -n1 "$WORK/login-path.txt" 2> /dev/null || true); echo "${p:-/login.html}"; }
runenv() { # env words for runapp.py
  RUNENV=("WORKDIR=$WORK" "UPG_TOOLS=$UPG_TOOLS" "UPG_SESSION_TIMEOUT=30000" "PORT_OFF=$PORT_OFF")
  [ ! -d "$WORK/demo-files" ] || RUNENV+=("UPG_DATA_FILES=$WORK/demo-files")
  if [ -s "$WORK/env-values.json" ]; then RUNENV+=("CONST_OVERRIDES=$(cat "$WORK/env-values.json")"); fi
  # heal reruns: the apimock stand-in's and the NATS broker's constant overrides, merged under the person's env-values.json (theirs win)
  local src=()
  if [ -f "$WORK/state/heal-standin" ] && [ -s "$WORK/apimock/overrides.json" ]; then src+=("$WORK/apimock/overrides.json"); fi
  if { [ -f "$WORK/state/heal-nats" ] || nats_on; } && [ -s "$WORK/natsfixture/overrides.json" ]; then src+=("$WORK/natsfixture/overrides.json"); fi
  if [ "${#src[@]}" -gt 0 ]; then
    [ -s "$WORK/env-values.json" ] && src+=("$WORK/env-values.json")
    python3 -I -c '
import json, sys, os
ov = {}
for f in sys.argv[1:-1]:
    if os.path.isfile(f) and os.path.getsize(f):
        ov.update(json.load(open(f)))
json.dump(ov, open(sys.argv[-1], "w"), indent=1)' "${src[@]}" "$WORK/state/const-heal.json"
    RUNENV+=("CONST_OVERRIDES=$WORK/state/const-heal.json")
  fi
}
infra_rc() { # infra_rc RC NAME: runapp.py exit 3 is an environment fault (F21: a taken port), never a judgment
  [ "$1" != 3 ] || { echo "upgrade-pipeline.sh: $2 could not start: environment fault, see runapp INFRA line in $LOG" >&2; exit 3; }
}
app_up() { # app_up NAME MDA FULLVER DB  -> 0 started
  local rc=0
  runenv
  x env "${RUNENV[@]}" python3 "$B/runapp.py" start "$1" "$2" "$3" "$4" || rc=$?
  infra_rc "$rc" "$1"
  [ "$rc" != 0 ] || APPS_UP+=("$1")
  return "$rc"
}
app_down() {
  runenv
  x env "${RUNENV[@]}" python3 "$B/runapp.py" stop "$1" || true
  local keep=() a
  for a in "${APPS_UP[@]:-}"; do [ -z "$a" ] || [ "$a" = "$1" ] || keep+=("$a"); done
  APPS_UP=("${keep[@]:-}")
}
# ---- step timing ($WORK/state/timing.tsv) ----
# One row per ATTEMPT of a step: step, start (UTC), end (UTC), exit code. Appended, never rewritten: a resumed or re-run step
# gets a new row. bin/runlog.py reads it: machine time = the sum of the rows; person wait = the gap after a row that stopped
# for a person (exit 10 to 15, NEEDS-JUDGMENT.md) until the pipeline next ran. A failure to write a row never fails the run.
TIMING_STEP=""; TIMING_START=""
now_utc() { date -u +%Y-%m-%dT%H:%M:%SZ; }
timing_open() { # timing_open STEP
  [ "$DRY" != 1 ] || return 0
  TIMING_STEP=$1; TIMING_START=$(now_utc)
  # the running step for the cockpit ("Running now"): step, start (epoch), the pipeline's pid (a dead pid = not running)
  printf '%s\t%s\t%s\n' "$1" "$(date +%s)" "$$" > "$WORK/state/running" 2> /dev/null || true
}
timing_close() { # timing_close EXITCODE
  [ -n "$TIMING_STEP" ] || return 0
  rm -f "$WORK/state/running"
  local f="$WORK/state/timing.tsv" end
  end=$(now_utc)
  { [ -s "$f" ] || printf 'step\tstart_utc\tend_utc\texit\n' > "$f"; printf '%s\t%s\t%s\t%s\n' "$TIMING_STEP" "$TIMING_START" "$end" "$1" >> "$f"; } 2> /dev/null || true
  TIMING_STEP=""
}
# feedback (bin/feedback_report.py): every exit, a stop as much as a PASS, harvests what the run taught into
# $WORK/learnings/ and writes $WORK/FEEDBACK-REPORT.md: where it stopped, the drafts, and how to send them back (PR) or
# file a toolkit bug (issue). Rung 2 reports on the whole run folder. Never changes the exit code. UPG_HARVEST=0 skips the
# harvest; the report still comes. Before this, harvest.py ran only when someone remembered steps/report.md 3c (cold WM1).
# rung 2 localedits: modules rung 1 updated carry content id 0 in the MPR, so rung 2's localedits printed UNKNOWN ("give
# --cid Module=<id>") for each one and the run stopped for a hand-written localedits.args (cold CMM, 7 modules). The content
# ids are in rung 1's plan.txt: add a --cid=Module=ID line for each plan module the args file does not name yet.
rung2_cids() { # rung2_cids PLAN ARGSFILE
  [ -f "$1" ] || return 0
  local cid ver mod
  while read -r cid ver mod _; do
    case "$cid" in ''|\#*) continue ;; esac
    [[ "$cid" =~ ^[0-9]+$ ]] && [ "$cid" != 0 ] && [ -n "$mod" ] || continue
    grep -Eq -- "(^|[= ])$mod=" "$2" 2> /dev/null || printf -- '--cid=%s=%s\n' "$mod" "$cid" >> "$2"
  done < "$1"
}
# App code name: UPG_APP_CODE (UPG_APP_NAME is the older spelling), else the line in state/app-code of the rung 1 work
# folder (rung 2 shares it), else a neutral code from the .mpr file name, written there: app-<6 hex>, no name in it,
# so runlog and harvest never carry a customer name. Cold CMM: no code at all, harvest and the run log skipped.
app_code() {
  local c="${UPG_APP_CODE:-${UPG_APP_NAME:-}}" fw=$WORK m
  [ "$(basename "$WORK")" != rung2 ] || fw=$(dirname "$WORK")
  [ -n "$c" ] || c=$(cat "$WORK/state/app-code" "$fw/state/app-code" 2> /dev/null | head -n 1 || true)
  if [ -z "$c" ] && m=$(ls "${APP:-/nonexistent}"/*.mpr 2> /dev/null | head -n 1) && [ -n "$m" ]; then
    c="app-$(basename "$m" | shasum | cut -c1-6)"
    [ "${DRY:-0}" = 1 ] || { mkdir -p "$fw/state" && printf '%s\n' "$c" > "$fw/state/app-code"; }
  fi
  printf '%s' "$c"
}
feedback_finish() { # feedback_finish EXITCODE STEP
  [ "${DRY:-0}" != 1 ] && [ -d "${WORK:-}" ] || return 0
  local fw=$WORK app
  [ "$(basename "$WORK")" != rung2 ] || fw=$(dirname "$WORK")
  app=$(app_code)
  python3 -I "$B/feedback_report.py" --work "$fw" --exit "$1" --step "$2" --code "$app" \
    --source "${SOURCE:-}" --target "${TARGET:-}" 2>&1 | sed 's/^/  /' || true
}
cleanup() {
  local a rc=$? st=${TIMING_STEP:-${STEP:-}}
  [ "$rc" != 0 ] || st=""
  timing_close "$rc" || true   # the step that is stopping (exit 4, a judgment stop, an error) gets its row with its own exit code
  # exit 4 (a failed step; after timing_close, which ends "running") writes no stop file: the page must still say the run is not working (MTA: page "agent is working", brief "waiting")
  if [ "$rc" = 4 ] && [ ! -f "$WORK/NEEDS-JUDGMENT.md" ] && declare -F cockpit_regen > /dev/null; then cockpit_regen || true; fi
  # run log (bin/runlog.py): a gate step that stops for judgment still leaves its row; the exit code stays the step's own
  if [ "${STEP:-}" = gate ] && [ "${DRY:-0}" != 1 ] && [ -z "${RUNLOG_DONE:-}" ]; then record_runlog || true; fi
  for a in "${APPS_UP[@]:-}"; do [ -z "$a" ] || { runenv; env "${RUNENV[@]}" python3 "$B/runapp.py" stop "$a" > /dev/null 2>&1 || true; }; done
  feedback_finish "$rc" "$st" || true
}
trap cleanup EXIT

# BT-10: a full disk reads as an app defect ("An error occurred while creating the deployment package"). Check before the
# heavy steps (exit 3, environment fault) and name the cause when a build fails. Threshold: UPG_MIN_FREE_MB (default 2000).
disk_gate() { # disk_gate STEP: stop before a heavy step when the disk is nearly full
  [ "$DRY" = 1 ] && return 0
  local out rc=0
  out=$("$B/diskcheck.sh" --need-mb "${UPG_MIN_FREE_MB:-2000}" "$WORK") || rc=$?
  [ "$rc" = 0 ] || { echo "upgrade-pipeline.sh: step '$1': $out" >&2; exit 3; }
}
disk_cause() { # disk_cause [LOG]: after a failed build, a judgment item that names a full disk first (nothing when the disk is fine)
  [ "$DRY" = 1 ] && return 0
  local out rc=0
  out=$("$B/diskcheck.sh" --need-mb 300 --log "${1:-$LOG}" "$WORK") || rc=$?
  [ "$rc" = 0 ] || { nj_meta person "The disk is full, so the step cannot go on. This is the machine, not the app. What should we do?" "none:Only you know what else lives on this disk, so the toolkit cannot say what to delete." "free|Free space on this disk, then rerun|Finished run folders, tools of finished runs, docker prune; the step is retried from here." "move|Run on a disk with 4 GB or more free|Point the run folder at it and rerun."; nj_add 10 "DISK FULL, not an app defect" "$out"; }
}

# ---- toolset / project helpers ----
mxw() { if [ "$(major "$1")" -le 9 ]; then echo "$B/mx9.sh"; else echo "$B/mx10.sh"; fi; }
heavy() { # heavy LABEL VER tool args...: a mx/mxbuild call under the heavy lock (steps/repair.md)
  local label=$1 ver=$2; shift 2
  "$B/heavy-lock.sh" "$label" "$(mxw "$ver")" "$ver" "$@"
}
mxcli_run() { if [ -n "${MXCLI:-}" ] && [ -x "$MXCLI" ]; then "$MXCLI" "$@"; else "$B/mxcli-container.sh" "$@"; fi; }
# GM-8 / NR2-7: the original is a git ARCHIVE of the .mpr and its mprcontents/, never `git show rev:App.mpr`: on an MPR v2 app the bare
# .mpr has no units, and impact_map, crosscalls --own, action_inventory and journey_scope would read nothing. mprcontents/ lands
# beside original.mpr ($WORK/mprcontents), where mprmodel.py looks for it.
write_original() { # write_original REV
  local rev=$1 base tmp paths
  base=$(basename "$MPR"); tmp="$WORK/.original.tmp"
  rm -rf "$tmp" "$WORK/mprcontents"; mkdir -p "$tmp"
  paths=("$base"); [ -z "$(git_app ls-tree "$rev" -- mprcontents 2> /dev/null)" ] || paths+=(mprcontents)
  git_app archive "$rev" -- "${paths[@]}" | tar -x -C "$tmp" || { rm -rf "$tmp"; return 1; }
  [ ! -d "$tmp/mprcontents" ] || mv "$tmp/mprcontents" "$WORK/mprcontents"
  mv -f "$tmp/$base" "$WORK/original.mpr"; rm -rf "$tmp"
}
git_app() { git -C "$APP" -c user.name="upgrade-pipeline" -c user.email="upgrade-pipeline@localhost" "$@"; }
# The step scripts (stepupdate.sh, convertpre.py, jardedupe.py, ...) commit with plain git: on a machine with no git identity
# that failed ("Author identity unknown", cold CMM: stepupdate post-convert, exit 4). They get the pipeline's identity then.
git_identity() {
  [ -z "$(git config user.email 2> /dev/null || true)" ] || return 0
  export GIT_AUTHOR_NAME="${GIT_AUTHOR_NAME:-upgrade-pipeline}" GIT_AUTHOR_EMAIL="${GIT_AUTHOR_EMAIL:-upgrade-pipeline@localhost}"
  export GIT_COMMITTER_NAME="${GIT_COMMITTER_NAME:-upgrade-pipeline}" GIT_COMMITTER_EMAIL="${GIT_COMMITTER_EMAIL:-upgrade-pipeline@localhost}"
}
git_identity
# The pipeline names its containers ${UPG_NAME:-mig}-<name> but did not export the name: runapp.py, with UPG_NAME unset, then
# REFUSED to stop mig-oldjp because another run's cmm-oldjp existed (FM-9 guard), and newjp found port 8080 taken (cold WM1
# journeys, next to cold CMM). Exported, every tool it calls uses the same prefix it does.
export UPG_NAME="${UPG_NAME:-mig}"
ensure_gitignore() {
  local f="$APP/.gitignore" l
  for l in '.claude/' '.mxcli/' '.stepupdate/' 'deployment/'; do
    grep -qxF "$l" "$f" 2> /dev/null || printf '%s\n' "$l" >> "$f"
  done
}
commit_app() { # commit_app "subject" KIND RULE: commit all changes in the app repo when there are any. Every toolkit commit
  # carries the trailers Changed-By: toolkit and Upgrade-Change: KIND RULE (trust.md section 3; bin/changelog.py reads them), and
  # Upgrade-Step: S-n when the step records know a step for that kind (steps.py trailer; UPG_STEPS_WORK is the work folder, exported below)
  [ "$DRY" = 1 ] && { say "+ git -C $APP commit -am '$1' (Upgrade-Change: $2 $3)"; return 0; }
  git_app add -A > /dev/null
  git_app diff --cached --quiet || git_app commit -q -m "$1" -m "$(printf 'Changed-By: toolkit\nUpgrade-Change: %s %s' "$2" "$3"; t=$(python3 "$B/steps.py" trailer --kind "$2" 2> /dev/null); [ -z "$t" ] || printf '\n%s' "$t")" >> "$LOG" 2>&1
}
resolve_app() {
  if [ -f "$WORK/state/app-dir" ]; then APP=$(cat "$WORK/state/app-dir")
  elif [ -n "$APP_DIR_ARG" ]; then APP=$(cd "$APP_DIR_ARG" && pwd)
  else APP="$RUN/app"; fi
  MPR=""
  if [ -d "$APP" ]; then
    local list=() f
    for f in "$APP"/*.mpr; do [ -e "$f" ] && list+=("$f"); done
    [ "${#list[@]}" -ne 1 ] || MPR=${list[0]}
    [ "${#list[@]}" -le 1 ] || die4 "more than one .mpr in $APP: ${list[*]}"
  fi
  [ -n "$MPR" ] || MPR="$APP/<app>.mpr"
}
project_version() { python3 "$B/mxversion.py" "$1" 2> /dev/null || true; }
open_errors() { # open_errors CHECKLOG -> number of errors
  local n
  n=$(grep -oE 'The app contains: *[0-9]+ errors' "$1" 2> /dev/null | grep -oE '[0-9]+' | head -n 1 || true)
  [ -n "$n" ] || n=$(grep -c '^\[error\]' "$1" 2> /dev/null || true)
  echo "${n:-0}"
}
roles_of_plan() { # roles_of_plan plan.json -> comma list of the non-guest roles of the smoke-walk plan
  python3 -I -c '
import json, sys
p = json.load(open(sys.argv[1]))
print(",".join(r["role"] for r in p.get("roles", []) if r.get("role") and r["role"] != p.get("guest_role")))' "$1"
}
write_users() { # write_users ROLES out.json: {"<Role>": {"user": "smoke_<role>", "pass": PW}}
  python3 -I -c '
import json, sys
roles, out, pw = sys.argv[1], sys.argv[2], sys.argv[3]
json.dump({r: {"user": "smoke_" + r.lower(), "pass": pw} for r in roles.split(",") if r}, open(out, "w"), indent=1)' "$1" "$2" "$SMOKE_PW"
}
# UPG_SMOKE_MICROFLOWS (header); the after walk also follows the baseline: a baseline that ran microflow steps compared
# with a walk that skipped them gave 4 false REGRESSIONs on WM1 (rerun 7, env not set on the rerun)
smoke_mf() {
  [ "${UPG_SMOKE_MICROFLOWS:-}" != 0 ] || return 0
  if [ "${UPG_SMOKE_MICROFLOWS:-}" = 1 ] || grep -q '"landed": *"microflow ran"' "$WORK/smoke-before.json" 2> /dev/null ||
    grep -q '"kind": *"microflow"' "$WORK/plan.json" 2> /dev/null; then echo --microflows; fi
}
user_args() { # user_args ROLES -> sets UARGS for smokewalk.js
  UARGS=(); local r
  IFS=',' read -ra _rl <<< "$1"
  for r in "${_rl[@]}"; do [ -z "$r" ] || UARGS+=(--user "$r=smoke_${r,,}:$SMOKE_PW"); done
}
mda_old() { if [ -n "$OLD_MDA" ]; then echo "$OLD_MDA"; else echo "$WORK/old-$SOURCE.mda"; fi; }
mda_new() { echo "$WORK/new-$TARGET.mda"; }

# DB names: <X> working, <X>_frozen never started. Cold CMM (2026-11-17): every run folder named "run" (the README's own
# example) got upg_run_*, and a second app's baseline reused the first app's frozen database without a word. The default
# name carries a hash of the run folder and is kept in $WORK/state/db-prefix; a run whose db-ledger.txt predates that keeps
# its old name. The frozen database carries its run folder as a comment (frozen_owner), checked before every reuse.
RUNP=$(cd "$RUN" 2> /dev/null && pwd -P || echo "$RUN")
if [ -n "$DB_ARG" ]; then X=$DB_ARG
elif [ -s "$WORK/state/db-prefix" ]; then X=$(head -n1 "$WORK/state/db-prefix")
else
  X="upg_$(basename "$RUN" | tr '[:upper:]' '[:lower:]' | tr -c 'a-z0-9_\n' '_' | cut -c1-24)"
  [ -f "$WORK/db-ledger.txt" ] || X="${X}_$(printf '%s' "$RUNP" | cksum | awk '{printf "%06x", $1 % 16777216}')"
fi
X_FROZEN="${X}_frozen"
[[ "$X" =~ ^[a-z0-9_]+$ ]] || usage_die "database name '$X' must be lower case letters, digits, underscore (use --db)"
# An explicit --db replaces the kept name: a later --from without --db must not drop back to the old database (cold
# CMM: rerun --from baseline --db upg_cmm_demo, then a resume without --db would have run update on upg_run_*).
[ "$DRY" = 1 ] || { [ -s "$WORK/state/db-prefix" ] && [ "$(head -n1 "$WORK/state/db-prefix")" = "$X" ]; } ||
  { mkdir -p "$WORK/state" && echo "$X" > "$WORK/state/db-prefix"; }
frozen_stamp() { must docker exec "$PGC" psql -U mendix -qc "COMMENT ON DATABASE $X_FROZEN IS 'upgrade-toolkit run $RUNP'"; }
frozen_owner() { # refuse a frozen database that another run made: its comment names another run folder, or it has none and
  # this run's ledger never used a copy of it (a run from before the stamp adopts its own one here)
  local own
  own=$(docker exec "$PGC" psql -U mendix -tAc "SELECT coalesce(shobj_description(oid, 'pg_database'), '') FROM pg_database WHERE datname='$X_FROZEN'" 2> /dev/null || true)
  [ "$own" != "upgrade-toolkit run $RUNP" ] || return 0
  if [ -z "$own" ] && grep -q "^${X}_" "$WORK/db-ledger.txt" 2> /dev/null; then frozen_stamp; return 0; fi
  die4 "frozen database $X_FROZEN exists but this run did not make it (${own:-no owner stamp}; this run: $RUNP). Another app's data would be the baseline: give this run its own name with --db upg_<name>, or drop that database if it is yours."
}

preflight() {
  local t
  # BT-8: `--only propose` reads triage outputs only: no toolset, runtime or mxcli is needed, so none is demanded (a worker
  # who had deleted the 300 MB source runtime to make disk room could not regenerate PROPOSAL.md)
  local toolfree=0
  [ "$ONLY" != propose ] || toolfree=1
  for t in docker zsh git python3 node; do [ "$toolfree" = 1 ] && [ "$t" = docker ] && continue; need_tool "$t"; done
  [ -z "$APP_ZIP" ] || need_tool unzip
  if [ "$DRY" != 1 ] && [ "$toolfree" = 0 ]; then docker info > /dev/null 2>&1 || { echo "upgrade-pipeline.sh: docker daemon not running (setup.sh step docker); after a container restart run bin/cloud/resume.sh <run folder>, which restarts dockerd and the cockpit server and relaunches the pipeline" >&2; exit 3; }; fi
  [ "$toolfree" = 0 ] || return 0
  need_path "$UPG_TOOLS/mxbuild-$SOURCE" "source mxbuild toolset"
  need_path "$UPG_TOOLS/mxbuild-$TARGET" "target mxbuild toolset"
  local v
  for v in "$SOURCE" "$TARGET" ${TARGET2:+"$TARGET2"}; do
    [ "$DRY" = 1 ] && continue
    ls -d "$UPG_TOOLS/runtime-$v" "$UPG_TOOLS/runtime-${v%.*}" > /dev/null 2>&1 || need_path "$UPG_TOOLS/runtime-$v" "runtime $v"
  done
  [ -z "$TARGET2" ] || need_path "$UPG_TOOLS/mxbuild-$TARGET2" "rung 2 mxbuild toolset"
  [ -n "${MXCLI:-}" ] && [ -x "${MXCLI:-}" ] || need_path "$UPG_TOOLS/mxcli-linux" "mxcli (MXCLI in env.sh, or tools/mxcli-linux)"
  [ -x "$B/heavy-lock.sh" ] || need_path "$B/heavy-lock.sh(+x)" "toolkit scripts"
}

# =====================================================================================================
# Steps
# =====================================================================================================

# fetch: unpack, put the project under git, record the original MPR. Script: unzip, git, mxversion.py
step_fetch() {
  if [ -n "$APP_ZIP" ]; then
    APP="$RUN/app"
    if [ -z "$(ls -A "$APP" 2> /dev/null || true)" ]; then
      must mkdir -p "$APP"
      # BT-9: a package may ship the build output deployment/ next to the .mpr (DOCGEN: 858 MB). mxbuild writes it again and
      # ensure_gitignore ignores it, so it is not unpacked; the zip itself is untouched. Only the folder beside the .mpr.
      local mprpath dpre="" listing
      # the listing is read once: `unzip -Z1 | grep -q` under pipefail failed whenever grep quit first (SIGPIPE), and then
      # deployment/ was unpacked after all (bt9-fetch-* controls, 1 run in 3)
      listing=$(unzip -Z1 "$APP_ZIP" 2> /dev/null || true)
      mprpath=$(printf '%s\n' "$listing" | grep -E '\.mpr$' | awk -F/ '{print NF, $0}' | sort -n | head -n 1 | cut -d' ' -f2- || true)
      case "$mprpath" in */*) dpre="${mprpath%/*}/" ;; esac
      if [ "$DRY" != 1 ] && grep -q "^${dpre}deployment/." <<< "$listing"; then
        must unzip -q -o "$APP_ZIP" -d "$APP" -x "${dpre}deployment/*"
        note "fetch: the package ships a deployment/ folder (build output); not unpacked, mxbuild writes it again (BT-9)"
      else
        must unzip -q -o "$APP_ZIP" -d "$APP"
      fi
    fi
    # a zip with one top folder: the project is the folder that holds the .mpr
    if [ "$DRY" != 1 ] && ! ls "$APP"/*.mpr > /dev/null 2>&1; then
      local sub
      sub=$(find "$APP" -mindepth 2 -maxdepth 2 -name '*.mpr' -print -quit)
      sub=${sub%/*}
      [ -n "$sub" ] || die4 "no .mpr found in $APP_ZIP"
      APP=$sub
    fi
  else
    APP=$(cd "$APP_DIR_ARG" && pwd)
  fi
  [ "$DRY" = 1 ] || printf '%s\n' "$APP" > "$WORK/state/app-dir"
  resolve_app
  if [ "$DRY" != 1 ] && [ ! -d "$APP/.git" ]; then
    must git -C "$APP" init -q
    ensure_gitignore
    must python3 "$B/buildout.py" exclude "$APP"   # DV-6: before ANY git add -A, so .classpath/.project/*.launch are never committed
    git_app add -A > /dev/null
    git_app commit -q -m "original" -m "$(printf 'Changed-By: toolkit\nUpgrade-Change: config run-start')" >> "$LOG" 2>&1
  elif [ "$DRY" != 1 ]; then
    ensure_gitignore
    must python3 "$B/buildout.py" exclude "$APP"   # DV-6: before the commit_app calls below (git add -A)
    if [ -n "$OLD_MDA" ]; then commit_app "rung start $SOURCE" config rung-start; fi
    [ -z "$(git_app status --porcelain)" ] || die4 "$APP has uncommitted changes: commit or discard them first (steps/baseline.md needs a clean tree)"
  else say "+ git init + commit original (when $APP has no .git)"; fi
  if [ "$DRY" != 1 ]; then
    local rev
    if [ -n "$OLD_MDA" ]; then rev=HEAD; else rev=$(git_app rev-list --max-parents=0 HEAD | tail -n 1); fi
    write_original "$rev" || die4 "could not write $WORK/original.mpr from $rev (git archive failed)"
    local v
    v=$(project_version "$APP")
    if [[ "$v" != *"$SOURCE"* ]]; then
      echo "upgrade-pipeline.sh: the project is version '${v:-unknown}', not --source $SOURCE" >&2; exit 2
    fi
    if [ -n "$(find "$APP" -maxdepth 2 \( -name 'data-snapshot.zip' -o -name '*.script' \) -print -quit)" ]; then
      todo_hsql_replay
    fi
  fi
}

# Demo data inside the package (HSQLDB data-snapshot.zip): baseline replays it into Postgres with seed_snapshot.py
# (seed_demo). A package with only loose *.script files has no route yet: those runs get seed_pg.py rows.
todo_hsql_replay() {
  if [ -n "$(demo_snapshot)" ]; then say "        hsql demo data present: baseline loads it (seed_snapshot.py)"; return 0; fi
  note "TODO todo_hsql_replay: the package carries HSQLDB *.script data but no data-snapshot.zip; it was NOT replayed, the data baseline uses seed_pg.py rows"
  say "TODO    hsql data present, not replayed (see $WORK/state/notes.txt)"
}
demo_snapshot() { [ -n "${APP:-}" ] && find "$APP" -maxdepth 2 -name 'data-snapshot.zip' -print -quit 2> /dev/null || true; }
# seed_demo: load the package's demo rows into $X (the old app made the schema). 1 = no snapshot or nothing loaded:
# the caller seeds synthetic rows. The file contents go to $WORK/demo-files, which runapp.py copies into every start.
seed_demo() {
  local snap rc=0
  snap=$(demo_snapshot); [ -n "$snap" ] || return 1
  xo "$WORK/logs/seed-snapshot.txt" python3 "$B/seed_snapshot.py" "$snap" --psql "$(psql_str "$X")" || rc=$?
  if [ "$rc" != 0 ] && ! grep -q 'the load was applied' "$WORK/logs/seed-snapshot.txt" 2> /dev/null; then
    note "demo data NOT loaded (seed_snapshot.py exit $rc, UNMAPPED in logs/seed-snapshot.txt): synthetic seed_pg.py rows instead"
    return 1
  fi
  # STOR: a snapshot whose app tables are all empty ("applied: 0 rows") loaded nothing: the frozen database then held only System rows
  # and the baseline diff stopped as vacuous. Same as "nothing loaded": the caller seeds synthetic rows.
  if grep -q '^applied: 0 rows in ' "$WORK/logs/seed-snapshot.txt" 2> /dev/null; then
    note "demo data NOT loaded (the snapshot holds no rows for the app's tables, logs/seed-snapshot.txt): synthetic seed_pg.py rows instead"
    return 1
  fi
  [ "$rc" = 0 ] || note "demo data loaded, but some table counts differ (logs/seed-snapshot.txt)"
  [ "$DRY" = 1 ] || { rm -rf "$WORK/demo-files"; mkdir -p "$WORK/demo-files"
    unzip -qo "$snap" 'data/files/*' -d "$WORK/demo-files/x" 2> /dev/null && mv "$WORK/demo-files/x/data/files"/* "$WORK/demo-files/" 2> /dev/null; rm -rf "$WORK/demo-files/x"; }
  note "demo data loaded from $(basename "$snap") ($(grep -o 'applied: [0-9]* rows in [0-9]* tables' "$WORK/logs/seed-snapshot.txt" 2> /dev/null || echo 'counts in logs/seed-snapshot.txt'))"
  return 0
}

# GM-38: the two facts that close a Java removal row on "target build green, symbols gone from the final javasource".
# Prints "--final-dir DIR --build-log LOG", one word per line, only when this run's target build log ($WORK/build-$TARGET.log, written by
# step_build for this $WORK and $TARGET) AND the project folder it built ($MPR's folder, the run's $APP) both exist; otherwise
# nothing, and release_impact.py is called as before a build. Same-run is not proved here: release_impact.py refuses a log
# older than the newest .java or .mpr of the folder (a rerun after the app was rewound reads as "not the build of that tree").
ri_build_args() {
  local log="$WORK/build-$TARGET.log"
  [ -f "$log" ] && [ -f "$MPR" ] || return 0
  printf '%s\n' --final-dir "$(dirname "$MPR")" --build-log "$log"
}
# GM-38: right after a green target build, close the open java-actions removal rows of the EXISTING release-impact.md whose
# symbols are gone from the final javasource (release_impact.py --close-proved: same rule and staleness check as --auto
# --final-dir, no facts, brain or rows regenerated, no entry replaced, no other triage output touched). Same conditions as
# ri_build_args (this run's log and project folder exist). Never fails the step: a failure warns, the rows stay open.
close_proved_rows() {
  [ "$DRY" != 1 ] && [ -f "$WORK/release-impact.md" ] || return 0
  local args=() rib rc=0
  while IFS= read -r rib; do args+=("$rib"); done < <(ri_build_args)
  [ "${#args[@]}" -gt 0 ] || return 0
  xo "$WORK/release-impact-close.out" python3 "$B/release_impact.py" --close-proved "$WORK/release-impact.md" "${args[@]}" || rc=$?
  if [ "$rc" != 0 ]; then note "release_impact.py --close-proved exit $rc: Java removal rows stay open, see $WORK/release-impact-close.out"
  else note "$(tail -n 1 "$WORK/release-impact-close.out" 2> /dev/null)"; fi
  return 0
}
# triage: versions, catalog, localedits, xmod, scanner, inventory, jarclash, impact map, release impact.
# Judgment: the module plan ($WORK/plan.txt, steps/triage.md item 3) has no script: exit 13 when absent.
step_triage() {
  local rc
  if [ "$DRY" = 1 ]; then say "+ mxversion.py app + toolsets > $WORK/versions.txt"; else
    { printf 'app: %s\n' "$(project_version "$MPR")"; printf 'toolset %s: %s\n' "$SOURCE" "$(project_version "$UPG_TOOLS/mxbuild-$SOURCE")"
      printf 'toolset %s: %s\n' "$TARGET" "$(project_version "$UPG_TOOLS/mxbuild-$TARGET")"; } > "$WORK/versions.txt"
  fi
  # BT-2: a module-only template (no navigation home page, no theme) has no baseline to freeze; say so now, not as "OLD app does not build"
  if [ "$DRY" != 1 ] && [ "${UPG_ALLOW_MODULE_ONLY:-}" != 1 ]; then
    rc=0; xo "$WORK/appshape.out" python3 "$B/appshape.py" "$APP" || rc=$?
    if [ "$rc" = 1 ]; then
      nj_meta person "The source is a module template, not an app: there is no running old app to compare against. What should we do?" "none:Whether a host app exists is something only you know." "wrap|Wrap it in a host app and upgrade that|An app with a home page, a theme and the module imported (steps/triage.md)." "modules|Upgrade its modules inside the app that uses them|Record the template as not upgradeable on its own." "goon|Go on anyway|Set UPG_ALLOW_MODULE_ONLY=1; the build is expected to fail."; nj_add 13 "The source is a module, not an app: it needs a host app" "$(cat "$WORK/appshape.out")

No navigation profile of this project has a home page, so mxbuild stops it with 'Select a default home page' (and, when the layouts use design properties, 'Design property ... is not supported by your theme'): there is no running old app to freeze as the baseline, and no journey to compare. This is a template to import into an app, not an app.
Decide, in writing: (a) wrap it in a host app (an app with a home page, a theme and the module imported) and run the upgrade on that app; or (b) record the template as not upgradeable on its own and upgrade its modules inside the app that uses them. Then rerun. To go on anyway (the build will fail): UPG_ALLOW_MODULE_ONLY=1."
      nj_flush
    fi
  fi
  must mxcli_run -p "$MPR" -c "REFRESH CATALOG FULL"
  local le=() a
  if [ -f "$WORK/localedits.args" ]; then while IFS= read -r a; do [ -z "$a" ] || le+=("$a"); done < "$WORK/localedits.args"; fi
  # GM-11: the element contents (microflows, pages, layouts) are compared only through `mxcli marketplace diff`. Pass it when an
  # mxcli runs here and the model is Mendix 10+ (mx below 10 has no module-import); otherwise localedits.py prints
  # "element contents NOT compared" itself, never a bare "unchanged". UPG_TRIAGE_MXCLI_DIFF=0 opts out (about 1 to 2 min per module).
  local pv; pv=$(project_version "$MPR")
  if [ "${UPG_TRIAGE_MXCLI_DIFF:-1}" != 0 ] && [ -n "${MXCLI:-}" ] && [ -x "$MXCLI" ] && [ "${pv%%.*}" -ge 10 ] 2> /dev/null; then le+=(--mxcli-diff); fi
  rc=0; xo "$WORK/localedits.out" python3 "$B/localedits.py" "$APP" --md "$WORK/localedits.md" --json "$WORK/localedits.json" "${le[@]}" || rc=$?
  [ "$rc" -le 2 ] || die4 "localedits.py failed (exit $rc), see $WORK/localedits.out"
  [ "$rc" = 0 ] || note "localedits exit $rc (1 = RED local edits, 2 = some module UNKNOWN): never read as 'no edits'; stepupdate refuses edited modules and keeps them"
  # BT-6: a renamed or republished Marketplace module is outside every version plan; name it (playbooks/module-renames.tsv)
  rc=0; xo "$WORK/renamed.md" python3 "$B/renamed_modules.py" "$WORK/localedits.json" || rc=$?
  [ "$rc" != 1 ] || note "RENAMED modules in $WORK/renamed.md: not version updates, a decision item in the proposal"
  rc=0; xo "$WORK/xmod.txt" python3 "$B/idcheck.py" "$APP" --xmod || rc=$?
  # scanner (steps/triage.md item 6): optional, lives in the company brain checkout
  # the optional scanner: $EA, $UPG_SCANNER, or UPG_SCANNER= in the private ~/.config/upgrade-toolkit/local.env; `|| true`: without
  # that file sed exits 2 and the ERR trap printed "unexpected failure at line 624" in every triage (cold WM1 #12, cold CMM)
  local EA="${EA:-${UPG_SCANNER:-$(sed -n 's/^UPG_SCANNER=//p' "$HOME/.config/upgrade-toolkit/local.env" 2>/dev/null || true)}}"
  if [ -f "$EA/scripts/scan.py" ]; then
    rc=0; (cd "$APP" && x python3 "$EA/scripts/scan.py" --project . --target "$TARGET" --from-version auto --data "$EA/data" --out "$WORK/findings.json") || rc=$?
    if [ "$rc" = 0 ]; then
      rc=0; xo "$WORK/scancover.out" python3 "$B/scancover.py" "$WORK/findings.json" || rc=$?
      [ "$rc" = 0 ] || note "scancover exit $rc: NO COVERAGE, scanner checked nothing for this rung: scanner rung INVALID, do the manual checks in $WORK/scancover.out"
    else note "scan.py failed (exit $rc): scanner rung INVALID"; fi
  elif [ -z "$EA" ]; then note "scanner not configured (EA, UPG_SCANNER, or UPG_SCANNER= in ~/.config/upgrade-toolkit/local.env): scanner rung INVALID"
  else note "scanner not found at $EA (no scripts/scan.py): scanner rung INVALID"
  fi
  if [ "$(major "$SOURCE")" -le 9 ]; then
    rc=0; xo "$WORK/javafinal.out" python3 "$B/javafinal.py" "$APP" --md "$WORK/javafinal.md" || rc=$?
    [ "$rc" != 1 ] || note "javafinal.py found assignments to Java action parameters: javac will fail at the build (by-hand fix, steps/repair.md row 10), see $WORK/javafinal.md"
  fi
  rc=0; xo "$WORK/test-inventory.out" python3 "$B/test_inventory.py" "$APP" --md "$WORK/test-inventory.md" --endpoints "$WORK/endpoints.txt" || rc=$?
  [ "$rc" = 0 ] || note "test_inventory.py exit $rc: no endpoints list (see $WORK/test-inventory.out)"
  rc=0; xo "$WORK/jarclash-before.out" python3 "$B/repair/jarclash.py" "$APP" --md "$WORK/jarclash-before.md" || rc=$?
  # impact map of the old app alone (always-on journey set, steps/journeys.md)
  must python3 "$B/impact_map.py" "$WORK/original.mpr" "$WORK/original.mpr" --out "$WORK/impact-base.json"
  # DV-3: which company brain this run uses (or that none was found), once, from the same script the gate summary asks
  if [ "$DRY" = 1 ]; then say "+ brainpath.py --describe"; else
    python3 "$B/brainpath.py" --describe 2>&1 | tee "$WORK/brain.txt" || say "brain: not reported (brainpath.py failed)"; fi
  # release impact (V31-RI): needs the module jumps, which come from the plan. --auto with the app's own model and javasource
  # closes the rows the app cannot hit; --evidence: a row stays open only when the app's own modules use what it names, and the
  # environment rows become one go-live checklist (cold test: 190 open rows). The production database and OS come from
  # UPG_DB_VENDOR, UPG_DB_VERSION, UPG_RUNTIME_OS when set (no file holds them).
  rc=0
  local riargs=(--from "$SOURCE" --to "$TARGET" --out "$WORK/release-impact.md")
  if [ -f "$WORK/module-jumps.txt" ]; then riargs+=(--plan "$WORK/module-jumps.txt")
  else note "no module-jumps.txt: release-impact.md holds Studio Pro rows only; module rows NOT generated"; fi
  local riauto=(--auto --evidence --facts-from-mpr "$MPR")
  [ -z "${UPG_DB_VENDOR:-}" ] || riauto+=(--db-vendor "$UPG_DB_VENDOR")
  [ -z "${UPG_DB_VERSION:-}" ] || riauto+=(--db-version "$UPG_DB_VERSION")
  [ -z "${UPG_RUNTIME_OS:-}" ] || riauto+=(--runtime-os "$UPG_RUNTIME_OS")
  local rib; while IFS= read -r rib; do riauto+=("$rib"); done < <(ri_build_args)   # GM-38: after a target build only (a rerun, --only triage); nothing before one
  xo "$WORK/release-impact.out" python3 "$B/release_impact.py" "${riargs[@]}" "${riauto[@]}" || rc=$?
  if [ "$rc" != 0 ] && [ "$rc" != 2 ]; then   # the facts could not be counted: the rows without auto, all open
    note "release_impact.py --auto exit $rc (facts not counted from $MPR): rows written without auto, see $WORK/release-impact.out"
    rc=0; xo "$WORK/release-impact.out" python3 "$B/release_impact.py" "${riargs[@]}" || rc=$?
  fi
  [ "$rc" = 0 ] || note "release_impact.py exit $rc (2 = a module is UNKNOWN to the brain: fill its row by hand), see $WORK/release-impact.out"
  dojo_report
  replacement_report
  # judgment: the plan
  if [ "$DRY" != 1 ] && [ ! -f "$WORK/plan.txt" ]; then
    nj_meta agent; nj_add 13 "Module plan missing: write $WORK/plan.txt" "No script picks module target versions (steps/triage.md item 3: newest version whose min Mendix fits the target, from the brain's modules-index.md and \`mxcli marketplace versions <content id>\`).
Write \`$WORK/plan.txt\`: one line per module, \`<content id> <version> <Module>\`, cross-module association targets (idcheck --xmod) LAST. An empty plan (comments only) is allowed and means no module updates.
Write \`$WORK/module-jumps.txt\`: \`<Module> <installed> -> <target>\` lines for the release-impact rows. Optional: \`$WORK/plan-pre.txt\` (updates BEFORE the convert, 10.x sources only), \`$WORK/localedits.args\` (one \`--cid Module=ID\` or \`--proxy Module=VER\` argument per line), \`$WORK/env-values.json\` (the environment's constants, same for old and new)."
    nj_meta info; nj_file 13 "localedits result" "$WORK/localedits.md" 40
    nj_meta info; nj_file 13 "cross-module association targets (update last)" "$WORK/xmod.txt" 20
    nj_flush
  fi
  kept_java_check
  charts11_check
  kept_vendor_check triage
  nj_flush
}

kept_vendor_check() { # GM-15: does a KEPT module's themesource still find the mixins, variables and files it uses in the planned packages?
  # kept_vendor_check triage|update. keptvendor.py exit: 0 judged and none missing, 1 MISSING, 3 NOT CHECKED (package not cached or
  # unreadable: never clean), 2 input error. The kept list is .stepupdate/kept.txt, written by the update step: a first triage has none,
  # so it says "not measured" (never "clean") and the update step runs this again once the list exists. Only a triage MISSING stops (nj
  # item, code 13); NOT CHECKED, input errors and the update-step call are notes: the package may simply not be cached yet.
  local mode=${1:-triage} rc=0 kf="$APP/.stepupdate/kept.txt" pf="$WORK/keptvendor-plan.txt"
  if [ "$DRY" = 1 ]; then x python3 "$B/keptvendor.py" "$APP" --kept-file "$kf" --plan-file "$pf" --json "$WORK/keptvendor.json"; return 0; fi
  if [ ! -s "$kf" ]; then
    [ "$mode" != triage ] || note "keptvendor NOT MEASURED: no $kf yet (the update step writes the kept list); mixins, variables and files of kept themesources are checked against the planned packages after it"
    return 0
  fi
  [ -f "$WORK/plan.txt" ] || { note "keptvendor NOT MEASURED: no $WORK/plan.txt to check the kept themesources against"; return 0; }
  cat "$WORK/plan.txt" "$WORK/plan-pre.txt" > "$pf" 2> /dev/null || cat "$WORK/plan.txt" > "$pf"
  xo "$WORK/keptvendor.out" python3 "$B/keptvendor.py" "$APP" --kept-file "$kf" --plan-file "$pf" --json "$WORK/keptvendor.json" || rc=$?
  case "$rc" in
    0) ;;
    1) note "keptvendor MISSING (exit 1): a kept themesource uses a mixin, variable or file a planned package removed; fix the kept SCSS or hold the package, see $WORK/keptvendor.out"
       if [ "$mode" = triage ]; then
         nj_meta info; nj_file 13 "A kept module's styling uses something a planned package removes (GM-15: the theme compile would fail)" "$WORK/keptvendor.out" 20 '^MISSING'
       fi ;;
    3) note "keptvendor NOT CHECKED (exit 3): target package not cached or unreadable, so some kept SCSS uses are NOT measured (never read as clean), see $WORK/keptvendor.out" ;;
    *) note "keptvendor exit $rc: kept themesources NOT measured, see $WORK/keptvendor.out" ;;
  esac
}

kept_java_check() { # a plan that keeps a module whose Java calls Runtime API that Mendix 11 removed: javac fails at the build
  # Cold rfq rung 2: a minimum-impact plan kept ExcelImporter, MxModelReflection and SAPODataConnector; the build after
  # convert and update stopped on 34 "cannot find symbol" (Core.retrieveXPathQuery, Core.isSubClassOf). replacements.md R18
  # had the hit, nothing tied it to the plan. MendixSSO's R18 hits (other patterns) built, so only these calls count.
  [ "$DRY" != 1 ] && [ -f "$WORK/plan.txt" ] && [ -d "${APP:-/nonexistent}/javasource" ] || return 0
  [ "$(echo "$TARGET" | cut -d. -f1)" -ge 11 ] 2> /dev/null || return 0
  local re='Core\.(retrieveXPathQuery[A-Za-z]*|isSubClassOf) *\(|com\.mendix\.core\.conf\.RuntimeVersion' d m f skip hits=""
  skip=$(cat "$WORK/plan.txt" "$WORK/plan-pre.txt" 2> /dev/null | grep -vE '^[[:space:]]*(#|$)' | awk '{ print tolower($3) }' || true)
  skip+=$'\n'$(grep -vE '^[[:space:]]*(#|$)' "$WORK/java-port.txt" 2> /dev/null | awk '{ print tolower($1) }' || true)
  for d in "$APP"/javasource/*/; do
    m=$(basename "$d")
    ! printf '%s\n' "$skip" | grep -qxi "$m" || continue
    f=$(grep -rlE "$re" --include='*.java' "$d" 2> /dev/null | grep -v '/proxies/' | sed "s#^$APP/##" || true)
    [ -z "$f" ] || hits+="$m: $(printf '%s\n' "$f" | wc -l | tr -d ' ') file(s), e.g. $(printf '%s\n' "$f" | head -2 | tr '\n' ' ')"$'\n'
  done
  [ -n "$hits" ] || return 0
  nj_meta agent; nj_add 13 "Kept module calls Java API Mendix $TARGET removed (javac will fail at the build)" "Not on the plan, and their Java calls Core.retrieveXPathQuery*, Core.isSubClassOf or com.mendix.core.conf.RuntimeVersion (playbooks/10-to-11.md: update those modules, do not edit their code):

$hits
Put each Marketplace module on $WORK/plan.txt (newest version for $TARGET); a module with no 11 release or an own module is ported as a repair (playbooks/10-to-11.md row 11): name it in $WORK/java-port.txt, one per line."
}

charts11_check() { # Charts 3.x widgets on an 11 target: the build stops on them (T7-29), but only after convert and update
  # Cold run 4, rung 2 (10.24 -> 11.12): basewalk, propose, convert and update ran (16 min), then the build stopped on
  # 36 AnyChart widgets the 10.24 model already held. The old model answers it here; the build check stays.
  [ "$DRY" != 1 ] || return 0
  [ "$(echo "$TARGET" | cut -d. -f1)" -ge 11 ] 2> /dev/null || return 0
  [ ! -s "$WORK/charts11.txt" ] || return 0
  local rc=0
  xo "$WORK/missing_deps-triage.txt" python3 "$B/repair/missing_deps.py" "$APP" --target "$TARGET" || rc=$?
  # exit 2 is INVALID (the model could not be read), never "no Charts 3.x": say it, the build check stays
  if [ "$rc" -ge 2 ]; then note "missing_deps exit $rc: Charts 3.x widgets not checked before convert, see $WORK/missing_deps-triage.txt"; return 0; fi
  grep -q '^DEPRECATED-11' "$WORK/missing_deps-triage.txt" 2> /dev/null || return 0
  # One ask, never two: a removed widget is handled once. When widgetroute.py can read a route for these uses, the build routes them
  # (widget_routes) and asks its own one OK at the end, so this early stop stands down; it stays only when no route can be read (exit 2).
  rc=0; xo "$WORK/widgetroute-triage.txt" python3 "$B/repair/widgetroute.py" "$APP" --target "$TARGET" --approved "$WORK/widget-routes-approved.txt" || rc=$?
  [ "$rc" -ge 2 ] || return 0
  nj_meta agent; nj_add 13 "Charts 3.x widgets on a Mendix $TARGET target: the build stops on them after convert and update" "$(grep -E '^(DEPRECATED-11|  module )' "$WORK/missing_deps-triage.txt" | cut -c1-400)

They build, but fail at runtime on Mendix 11 (T7-29). Route per module: the app's own pages get the Charts 6.x widgets
(playbooks/widgets.md) on the 10.24 rung; a Marketplace module's own demo pages go with that module (update it on the
plan, remove it, or exclude its pages). Write the route in $WORK/charts11.txt, then rerun (the build checks again)."
}

# LDMS (repair row 34): mxbuild on Linux unpacks an add-on into .mendix-cache/modules/<lower case>.mxmodule, Gradle asks for the
# case of modules/<Name>.mxmodule. After a build that failed with that message, link the other case; true when a link was made.
modcase_fix() { # modcase_fix BUILD_LOG
  [ "$DRY" != 1 ] || return 1
  tail -n 2000 "$1" 2> /dev/null | grep -q "mendix-cache/modules/.*\.mxmodule/javasource.*not found" || return 1
  local out="$WORK/mxmodulecase.out"
  xo "$out" python3 "$B/repair/mxmodulecase.py" "$APP" --log "$1" || return 1
  grep -q '^LINK ' "$out" || return 1
  note "add-on cache folder case fixed (repair row 34): $(grep -c '^LINK ' "$out") link(s), building once more"
  return 0
}

# baseline: build old, start on a fresh DB, seed, freeze, endpoint probe, snapshot, controls.
# Scripts: heavy-lock.sh + mx9/mx10.sh mxbuild, runapp.py, seed_pg.py, snapshot.py, diff.py
step_baseline() {
  local old rc=0 base probe keep line p code
  old=$(mda_old)
  # DV-6: idempotent again here, because a run resumed (--from/--only baseline) on an app whose run start predates the exclude never passed it
  x python3 "$B/buildout.py" exclude "$APP" || note "buildout.py exclude failed: .classpath, .project, *.launch may show as dirty (DV-6)"
  if [ -z "$OLD_MDA" ] && [ ! -f "$old" ]; then
    disk_gate baseline
    # LDMS: a publisher SCSS import with the wrong letter case (components/ for Components/) fails the theme compile of the OLD app on
    # Linux too, and repair row 11 only ran for the new one: fix it before the old build, one commit
    x python3 "$B/repair/scsscase.py" "$APP" || note "scsscase.py failed on the old app: the theme compile may fail"
    commit_app "linux: SCSS import case fix (old app)" repair repair-row-11
    x heavy build-old "$SOURCE" mxbuild --target=package -o "$old" "$MPR" || rc=$?
    if [ "$rc" != 0 ] && modcase_fix "$LOG"; then   # LDMS: add-on cache folder case on Linux (repair row 34): link, build once more
      rc=0; x heavy build-old "$SOURCE" mxbuild --target=package -o "$old" "$MPR" || rc=$?
    fi
    if [ "$rc" != 0 ]; then
      disk_cause
      nj_meta agent; nj_file 10 "OLD app does not build (exit $rc)" "$LOG" 20 '^ERROR at|ERROR|error'
      nj_flush
    fi
    commit_app "build: regenerated stubs" config build-stubs
  fi
  if db_exists "$X_FROZEN"; then
    frozen_owner
    note "reusing existing frozen database $X_FROZEN"
  else
    if [ -n "$SEED_FROM" ]; then copy_db "$SEED_FROM" "$X"; fi
    app_up old "$old" "$SOURCE" "$X" || die4 "old app did not start on $X (log: $LOG, $WORK/logs/runtime-old.log)"
    app_down old
    if [ -z "$SEED_FROM" ]; then
      seed_demo || must python3 "$B/seed_pg.py" --psql "$(psql_str "$X")" --per-entity 5
      app_up old "$old" "$SOURCE" "$X" || die4 "old app did not start after the seed (log: $LOG)"
      app_down old
    fi
    # GM-A5: the baseline is frozen only from a CLEAN start: read the old app's start log first (bin/startcheck.py).
    # UNCLEAN (after-startup unfinished or failed, never started) and INVALID (log missing or unreadable) stop as a judgment item:
    # a log nobody read proves nothing. A plain ERROR outside after-startup is CLEAN-WITH-ERRORS: noted, listed in
    # $WORK/start-errors-old.txt, not a stop. Accept a known benign line with $WORK/startup-allow.txt (fnmatch, "# reason").
    local sc_rc=0 sc_allow=()
    [ ! -s "$WORK/startup-allow.txt" ] || sc_allow=(--allow "$WORK/startup-allow.txt")
    if [ "$DRY" != 1 ]; then
      python3 "$B/startcheck.py" "$WORK/logs/runtime-old.log" --list "$WORK/start-errors-old.txt" ${sc_allow[@]+"${sc_allow[@]}"} > "$WORK/startcheck-old.txt" 2>&1 || sc_rc=$?
      if [ "$sc_rc" != 0 ]; then
        note "baseline NOT frozen: $(head -1 "$WORK/startcheck-old.txt")"
        nj_meta agent "The old app did not start cleanly (startcheck exit $sc_rc), so $X_FROZEN is not frozen. Fix the cause, or accept a known benign line?" "fix the cause; or add a pattern to $WORK/startup-allow.txt (ERROR Node: message*  # reason), then rerun"
        nj_file 10 "Old app did not start cleanly" "$WORK/startcheck-old.txt"
        nj_flush
      fi
      if grep -q '^ERROR line' "$WORK/start-errors-old.txt" 2> /dev/null; then
        note "old app start log has $(grep -c '^ERROR line' "$WORK/start-errors-old.txt") ERROR line(s) outside after-startup (baseline frozen anyway, listed in $WORK/start-errors-old.txt)"
      fi
      if grep -q '^line .*accepted:' "$WORK/start-errors-old.txt" 2> /dev/null; then
        note "old app start log: $(grep -c '^line .*accepted:' "$WORK/start-errors-old.txt") ERROR line(s) accepted by startup-allow.txt (listed in $WORK/start-errors-old.txt)"
      fi
    fi
    copy_db "$X" "$X_FROZEN"; frozen_stamp
  fi
  # endpoint probe on its own copy (steps/triage.md item 8): drop listed paths that answer 404 on the old app
  if [ -s "$WORK/endpoints.txt" ] && [ ! -f "$WORK/endpoints.probed" ]; then
    probe=$(fresh_name "${X}_probe")
    copy_db "$X_FROZEN" "$probe"
    app_up oldprobe "$old" "$SOURCE" "$probe" || die4 "old app did not start for the endpoint probe (log: $LOG)"
    keep="$WORK/endpoints.new"; : > "$keep"
    if [ "$DRY" != 1 ]; then
      while IFS= read -r line; do
        p=$(printf '%s\n' "$line" | awk '{for(i=1;i<=NF;i++) if ($i ~ /^\//) {print $i; exit}}')
        [ -n "$p" ] || { printf '%s\n' "$line" >> "$keep"; continue; }
        code=$(curl -s -o /dev/null -w '%{http_code}' "http://localhost:$APP_PORT$p" || true)
        if [ "$code" = 404 ]; then note "endpoint $p dropped: 404 on the old app"; else printf '%s\n' "$line" >> "$keep"; fi
      done < "$WORK/endpoints.txt"
      cp "$WORK/endpoints.txt" "$WORK/endpoints.all.txt"; mv "$keep" "$WORK/endpoints.txt"; : > "$WORK/endpoints.probed"
    else say "+ curl each endpoint of $WORK/endpoints.txt on the old app, drop the 404s"; fi
    app_down oldprobe
    mark_used "$probe" probe
  fi
  base=$(fresh_name "${X}_base")
  copy_db "$X_FROZEN" "$base"
  app_up oldbase "$old" "$SOURCE" "$base" || die4 "old app did not start on $base (log: $LOG)"
  local ep_args=()
  [ ! -s "$WORK/endpoints.txt" ] || ep_args=(--endpoints "$WORK/endpoints.txt")
  rc=0
  x python3 "$B/snapshot.py" --label before --ledger "$WORK/db-ledger.txt" --psql "$(psql_str "$base")" \
    --app-url "http://localhost:$APP_PORT" "${ep_args[@]}" --log-cmd "docker logs ${UPG_NAME:-mig}-oldbase" \
    --admin-url "http://localhost:$ADMIN_PORT" --admin-pass "$M2EE_PASS" --out "$WORK/before.json" || rc=$?
  app_down oldbase
  [ "$rc" = 0 ] || die4 "snapshot before failed (exit $rc), log: $LOG"
  # controls (steps/baseline.md item 4)
  rc=0; x python3 "$B/diff.py" "$WORK/before.json" "$WORK/before.json" || rc=$?
  [ "$rc" = 0 ] || die4 "control failed: diff before vs before is not clean (exit $rc): the instrument is broken, log: $LOG"
  todo_mutant_control
}

# TODO (not automated): the mutant control needs a data-bearing table and column chosen from the schema and a value
# that fits the column length (T1, T2 both failed their first guess). It is reported as NOT RUN, never as passed.
todo_mutant_control() {
  note "TODO todo_mutant_control: mutant control NOT RUN (steps/baseline.md item 4); the tools' proof is 'make test' in controls/"
}

# basewalk: smoke users + smoke walk + always-on journeys on the OLD app, each on its own copy of the frozen DB.
# Scripts: smokewalk_gen.py, smoke_users.py, smokewalk.js, gen_journeys.py, run_journeys.py
step_basewalk() {
  local old roles rc=0 db
  old=$(mda_old)
  must python3 "$B/smokewalk_gen.py" "$APP" -o "$WORK/plan.json"
  roles=""; [ "$DRY" = 1 ] || roles=$(roles_of_plan "$WORK/plan.json")
  [ "$DRY" = 1 ] && roles="Role1,Role2"
  [ -n "$roles" ] || { nj_meta agent; nj_add 11 "No user roles in the smoke-walk plan" "plan.json has no non-guest role: nothing can log in. $WORK/plan.json"; nj_flush; }
  [ "$DRY" = 1 ] || write_users "$roles" "$WORK/users.json"
  user_args "$roles"
  # smoke walk
  db=$(fresh_name "${X}_smoke_walk")
  copy_db "$X_FROZEN" "$db"
  app_up oldwalk "$old" "$SOURCE" "$db" || die4 "old app did not start for the smoke walk (log: $LOG)"
  must python3 "$B/smoke_users.py" "$db" --roles "$roles" --apply
  rc=0; x node "$B/smokewalk.js" --plan "$WORK/plan.json" --url "http://localhost:$APP_PORT" "${UARGS[@]}" $(smoke_mf) --login-path "$(login_path)" \
    --out "$WORK/smoke-before.json" --shots "$WORK/smoke-before-shots" || rc=$?
  app_down oldwalk
  mark_used "$db" walk
  [ "$rc" -le 1 ] || { nj_meta agent; nj_file 11 "Smoke walk on the OLD app is INVALID (exit $rc)" "$LOG" 30 'INVALID|FAIL|credential'; }
  ! grep -q 'microflow (use --microflows)' "$LOG" 2> /dev/null ||
    note "the smoke walk SKIPPED microflow steps (UPG_SMOKE_MICROFLOWS=0): roles that reach pages only through them are judged on less; unset it to walk them on the walk's own DB copy"
  [ "$rc" != 1 ] || note "smoke walk on the old app has FAIL steps (baseline defects, listed apart): $WORK/smoke-before.json"
  # always-on journeys
  # BT-4: baseline-evidence.txt (a NO-SIGNOUT line for an app with no sign-out UI) is read here as well as at the gate
  local create=() ev=()
  [ ! -f "$WORK/create-spec.json" ] || create=(--create "$WORK/create-spec.json")
  [ ! -f "$WORK/baseline-evidence.txt" ] || ev=(--baseline-evidence "$WORK/baseline-evidence.txt")
  # BT-12: a NO-CREATE / UNREACHABLE line is checked against the --actions inventory of the OLD model: write it here too
  if [ -f "$WORK/baseline-evidence.txt" ] && [ "$DRY" != 1 ] && [ -f "$WORK/original.mpr" ]; then
    { [ -s "$WORK/actions.json" ] && [ "$WORK/actions.json" -nt "$B/action_inventory.py" ]; } \
      || must python3 "$B/action_inventory.py" "$WORK/original.mpr" --out "$WORK/actions.json"
    ev+=(--actions "$WORK/actions.json")
  fi
  must python3 "$B/gen_journeys.py" "$WORK/impact-base.json" --out-dir "$WORK/journeys-base" --roles-with-users "$roles" --data-rung "${create[@]}"
  # hand-written journeys (WORK/hand-journeys/<Role>/*.journey.json, e.g. the anonymous visitor) join the generated set
  [ ! -d "$WORK/hand-journeys" ] || cp -R "$WORK/hand-journeys/." "$WORK/journeys-base/journeys/"
  db=$(fresh_name "${X}_smoke_jbase")
  copy_db "$X_FROZEN" "$db"
  app_up oldj "$old" "$SOURCE" "$db" || die4 "old app did not start for the journeys (log: $LOG)"
  must python3 "$B/smoke_users.py" "$db" --roles "$roles" --apply
  rc=0; xo "$WORK/journeys-base.out" python3 "$B/run_journeys.py" "$WORK/journeys-base" --label before --port "$APP_PORT" --psql "$(psql_str "$db")" \
    --admin-port "$ADMIN_PORT" --admin-pass "$M2EE_PASS" --users "$WORK/users.json" --login-path "$(login_path)" --work "$WORK/e2e-base" --pause 50 ${ev[@]+"${ev[@]}"} || rc=$?
  app_down oldj
  mark_used "$db" journeys
  if [ "$rc" != 0 ]; then
    nj_meta agent; nj_file 11 "Always-on journeys are not all PASS on the OLD app (exit $rc): fix the journey, drop it, or write the todo" "$WORK/journeys-base.out" 40 'FAIL|INVALID|todo|skipped|INFO'
    nj_meta info; nj_add 11 "Plan items" "plan: $WORK/journeys-base/plan.json (skipped, todo, not_browser). An MFA journey needs a user with an MFA type (users.json \`_mfa\`); this script cannot create one."
    nj_park
  fi
}

# propose (trust spec section 2): nothing in the app model changes before a person signs $WORK/PROPOSAL.md.
# Scripts: action_inventory.py + apimock.py inventory on the original model (their output is a proposal input), proposal.py.
interview_unattended() { # auto takes the recommendations at propose the same way
  case "${UPG_INTERVIEW_MODE:-}" in unattended|auto) return 0 ;; esac
  grep -qiE '^Interview mode:[[:space:]]*(unattended|auto)' "$WORK/interview-mode.txt" 2> /dev/null
}
interview_auto() {
  [ "${UPG_INTERVIEW_MODE:-}" = auto ] || grep -qiE '^Interview mode:[[:space:]]*auto' "$WORK/interview-mode.txt" 2> /dev/null
}
scope_run() { # journey_scope.py on the OLD model: sets SC=(--scope FILE) for gen_journeys.py, or SC=() when it cannot run
  SC=()
  [ -s "$WORK/actions.json" ] && [ -f "$WORK/original.mpr" ] || return 0
  local sa=(--out "$WORK/journey-scope.json" --md "$WORK/journey-scope.md") rc=0
  [ ! -s "$WORK/localedits.json" ] || sa+=(--localedits "$WORK/localedits.json")
  [ ! -s "$WORK/usage.json" ] || sa+=(--usage "$WORK/usage.json")   # optional: without it nothing is said about usage
  [ ! -s "$WORK/vendor-modules.txt" ] || sa+=(--vendor "$(tr '\n' ',' < "$WORK/vendor-modules.txt" | sed 's/,$//')")
  [ ! -d "$APP/javasource" ] || sa+=(--code-root "$APP")
  xo "$WORK/journey-scope.out" python3 "$B/journey_scope.py" "$WORK/actions.json" --model "$WORK/original.mpr" "${sa[@]}" || rc=$?
  if [ "$rc" = 0 ]; then
    SC=(--scope "$WORK/journey-scope.json")
    # why the reachable actions have no click path (read only; a failure only loses the cause text of the INVALID rows)
    if xo "$WORK/click-causes.out" python3 "$B/click_causes.py" "$WORK/actions.json" --model "$WORK/original.mpr" --scope "$WORK/journey-scope.json" \
         --out "$WORK/click-causes.json" --md "$WORK/click-causes.md"; then SC+=(--causes "$WORK/click-causes.json"); fi
  else note "journey_scope.py exit $rc: every action counts toward the journeys rung (see $WORK/journey-scope.out)"; fi
}
proposal_args() { # sets PA for proposal.py
  PA=(--work "$WORK" --source "$SOURCE" --target "$TARGET" --app "$APP")
  [ -z "$TARGET2" ] || PA+=(--target2 "$TARGET2")
  [ ! -f "$WORK/original.mpr" ] || PA+=(--original "$WORK/original.mpr")
  ! interview_unattended || PA+=(--unattended)
}
proposal_stop() { # proposal_stop RC: rc 14 / 15 end the run with NEEDS-JUDGMENT.md, anything else but 0 is a failed fixed step
  case "$1" in
    0) return 0 ;;
    14) nj_meta person "Do you approve the upgrade plan?" "approve" "approve|Approve and continue|Signs with your Git name; nothing in the app changes before this." "change|Change a choice first|Answer the plan questions, then approve."; nj_add 14 "Upgrade proposal awaits sign-off: read $WORK/PROPOSAL.md" "$(head -n 3 "$WORK/proposal.out" 2> /dev/null)
Nothing in the app model has changed. Answer the questions under Blocked on you in the live cockpit and approve the plan there
(the approval carries your Git name), or answer the section-3 items in chat (steps/decide.md) and approve on the page.
To stop on purpose, write \`Status: PAUSED <reason>\` in PROPOSAL.md section 6. Then run the command at the top of this file."
       nj_meta info; nj_file 14 "PROPOSAL.md (head)" "$WORK/PROPOSAL.md" 30 ;;
    15) nj_meta info; nj_add 15 "Upgrade proposal PAUSED by the owner" "$(head -n 3 "$WORK/proposal.out" 2> /dev/null)
The run stopped on purpose; no step after propose has run. Resume: remove the \`Status: PAUSED\` line from $WORK/PROPOSAL.md section 6, write \`Signed-off: <name> <yyyy-mm-dd>\`, then
    $(rerun_cmd)" ;;
    *) die4 "proposal.py failed (exit $1), see $WORK/proposal.out" ;;
  esac
  nj_flush
}
# Dojo to React (B6-4) on every run, against the last rung: the move is part of each upgrade, not a later project. Cold
# test WM1: the pipeline never ran dojo_report.py, so 144 legacy core widgets in 83 documents showed up nowhere.
dojo_report() {
  [ "$DRY" != 1 ] || { say "+ dojo_report.py $WORK/original.mpr --to ${TARGET2:-$TARGET} --out $WORK/dojo-react.md"; return 0; }
  [ -f "$WORK/original.mpr" ] || return 0
  local rc=0
  xo "$WORK/dojo-react.out" python3 "$B/dojo_report.py" "$WORK/original.mpr" --to "${TARGET2:-$TARGET}" --out "$WORK/dojo-react.md" || rc=$?
  [ "$rc" = 0 ] || note "dojo_report.py exit $rc, see $WORK/dojo-react.out"
}

# Replacements (B6) on every run, against the last rung, like dojo_report. Cold CMM: rung 2 built and walked 11.12.7 with
# MicroflowTimer 4.0.3 on the mix wizard pages; R38 (mx.logger, removed in 11.0) names it from the .mpk, but only the
# agent's triage item 10 ran replacement_check.py, so the unattended proposal said "not measured: replacements.md" and
# the wizard steps never rendered (TypeError reading 'debug').
replacement_report() {
  [ "$DRY" != 1 ] || { say "+ replacement_check.py $APP --to ${TARGET2:-$TARGET} --out $WORK/replacements.md"; return 0; }
  [ -d "${APP:-/nonexistent}" ] || return 0
  local rc=0
  xo "$WORK/replacements.out" python3 "$B/replacement_check.py" "$APP" --to "${TARGET2:-$TARGET}" --out "$WORK/replacements.md" || rc=$?
  case "$rc" in
    0) ;;
    1) note "replacement_check.py: $(grep -cE '^HIT ' "$WORK/replacements.out" 2> /dev/null || true) HIT row(s) for ${TARGET2:-$TARGET} (open in the proposal), see $WORK/replacements.md" ;;
    2) note "replacement_check.py exit 2: the app could not be read or an extra rule table failed ($(grep -cE '^HIT ' "$WORK/replacements.out" 2> /dev/null || true) HIT row(s) printed for ${TARGET2:-$TARGET}), see $WORK/replacements.out" ;;
    *) note "replacement_check.py exit $rc, see $WORK/replacements.out" ;;
  esac
}

# GM-12: the target packages of the planned updates are read for calls into modules the app does not have; proposal.py
# makes each one a section-3 item "needs module X". Run at propose (plan.txt exists then), fresh each time: the plan may change.
absent_modules_report() {
  local pf=(--plan-file "$WORK/plan.txt")
  [ ! -f "$WORK/plan-pre.txt" ] || pf+=(--plan-file "$WORK/plan-pre.txt")   # the pre-convert updates are planned and checked too
  [ "$DRY" != 1 ] || { say "+ absentmods.py $WORK/original.mpr ${pf[*]} --json $WORK/absentmods.json"; return 0; }
  [ -f "$WORK/plan.txt" ] && [ -e "$WORK/original.mpr" ] || return 0
  local rc=0
  rm -f "$WORK/absentmods.json"   # a failed or crashed rerun must not leave an earlier run's answer for proposal.py
  xo "$WORK/absentmods.out" python3 "$B/absentmods.py" "$WORK/original.mpr" "${pf[@]}" --json "$WORK/absentmods.json" || rc=$?
  # a Python traceback also exits 1: it is NEEDS only when the output has a NEEDS line
  if [ "$rc" = 1 ] && ! grep -q '^NEEDS ' "$WORK/absentmods.out" 2> /dev/null; then rc=9; fi
  case "$rc" in
    0) ;;
    1) note "absentmods.py: $(grep -c '^NEEDS ' "$WORK/absentmods.out" 2> /dev/null || true) absent module(s) a planned update calls (section 3 of the proposal), see $WORK/absentmods.out" ;;
    3) note "absentmods.py: a planned update's package is not in the cache: NOT CHECKED, not clean, see $WORK/absentmods.out" ;;
    *) note "absentmods.py failed (exit $rc, no NEEDS line): calls into absent modules NOT CHECKED, see $WORK/absentmods.out" ;;
  esac
}

step_propose() {
  local rc=0
  absent_modules_report
  # a run whose triage predates the report
  [ -s "$WORK/dojo-react.md" ] || dojo_report
  [ -s "$WORK/replacements.md" ] || replacement_report
  if [ "$DRY" = 1 ]; then
    say "+ action_inventory.py $WORK/original.mpr --out $WORK/actions.json; apimock.py inventory $WORK/original.mpr --json $WORK/apimock-inventory.json"
    say "+ proposal.py --work $WORK --source $SOURCE --target $TARGET (exit 14 unsigned, 15 PAUSED, 0 signed or unattended)"
    return 0
  fi
  if [ -f "$WORK/original.mpr" ]; then
    # the same file and the same freshness rule as the journeys step, so that step finds it done
    if [ ! -s "$WORK/actions.json" ] || [ ! "$WORK/actions.json" -nt "$B/action_inventory.py" ]; then
      rc=0; xo "$WORK/actions.out" python3 "$B/action_inventory.py" "$WORK/original.mpr" --out "$WORK/actions.json" || rc=$?
      [ "$rc" = 0 ] || note "action_inventory.py exit $rc: the proposal shows the action count as not measured (see $WORK/actions.out)"
    fi
    scope_run   # the triage line "journeys in scope: N reachable, M out of scope (...)" the proposal cites
    rc=0; xo "$WORK/apimock-inventory.out" python3 "$B/apimock.py" inventory "$WORK/original.mpr" --json "$WORK/apimock-inventory.json" || rc=$?
    [ "$rc" -le 3 ] || note "apimock.py inventory exit $rc: the proposal lists external systems as not measured (see $WORK/apimock-inventory.out)"
    # every version reviews its stand-ins again, as a step of its own; rung 2 compares with the inventory of rung 1
    if [ -s "$WORK/apimock-inventory.json" ]; then
      local prev=(); [ "$(basename "$WORK")" != rung2 ] || [ ! -s "$WORK/../apimock-inventory.json" ] || prev=(--previous "$WORK/../apimock-inventory.json")
      python3 "$B/steps.py" standins --work "$WORK" --inventory "$WORK/apimock-inventory.json" ${prev[@]+"${prev[@]}"} --by toolkit >> "$LOG" 2>&1 ||
        note "steps.py standins failed: the stand-ins of this version are not a step (see $LOG)"
    fi
  else
    note "no original.mpr: the proposal counts no modules, pages, microflows or actions"
  fi
  proposal_args
  rc=0; python3 "$B/proposal.py" "${PA[@]}" > "$WORK/proposal.out" 2>&1 || rc=$?
  cat "$WORK/proposal.out" >> "$LOG"
  if [ "$rc" = 0 ] && interview_unattended && [ "$(python3 "$B/proposal.py" --status --work "$WORK")" != signed ]; then
    note "proposal not signed: Interview mode unattended, ASSUMED (unattended) lines in $WORK/DECISIONS.md"
  fi
  proposal_stop "$rc"
}
# a plan input that changed after the sign-off clears it (proposal.py): every step after propose asks again
proposal_recheck() {
  local rc=0 keep=$STEP
  STEP=propose
  proposal_args
  python3 "$B/proposal.py" "${PA[@]}" > "$WORK/proposal.out" 2>&1 || rc=$?
  cat "$WORK/proposal.out" >> "$WORK/logs/propose.log"
  proposal_stop "$rc"
  STEP=$keep
}

# convert: mx convert in place with the TARGET toolset, convertcheck, commit. Scripts: heavy-lock.sh, mx10.sh, convertcheck.py, stepupdate.sh
step_convert() {
  local rc=0 cur
  cur=$(project_version "$APP")
  if [ "$DRY" != 1 ] && [[ "$cur" == *"$TARGET"* ]]; then note "project already at $TARGET, convert skipped"; return 0; fi
  # F13 (Purchase Request 10.24, real run): with only plan.txt, all eight updates ran after the convert and Mendix 11
  # refused every package (made before Studio Pro 10.21). A 10.x to 11 run states its pre-convert plan, even an empty one.
  if [ "$DRY" != 1 ] && [ "$(major "$SOURCE")" = 10 ] && [ "$(major "$TARGET")" -ge 11 ] && [ ! -e "$WORK/plan-pre.txt" ] \
     && [ -f "$WORK/plan.txt" ] && grep -qvE '^[[:space:]]*(#|$)' "$WORK/plan.txt"; then
    nj_meta agent; nj_add 13 "plan-pre.txt missing on a 10.x to 11 run" "Mendix 11 imports no package made before Studio Pro 10.21, so those updates must run before the convert. Split $WORK/plan.txt: lines whose package was made before 10.21 go to $WORK/plan-pre.txt (steps/triage.md, ORDER). Nothing to run before the convert: write $WORK/plan-pre.txt with only a comment."
    nj_flush
  fi
  if [ "$(major "$SOURCE")" -ge 10 ] && [ -s "$WORK/plan-pre.txt" ]; then
    run_stepupdate "$WORK/plan-pre.txt" "pre-convert"
    replay_edits pre
  fi
  disk_gate convert
  rc=0
  xo "$WORK/convert-$TARGET.log" env "UPG_ROOT=$RUN" "$B/heavy-lock.sh" convert "$B/mx10.sh" "$TARGET" mx convert --in-place "$APP" || rc=$?
  [ "$DRY" = 1 ] || note "mx convert exit $rc (never trusted, convertcheck decides)"
  rc=0; xo "$WORK/convertcheck.out" python3 "$B/convertcheck.py" "$WORK/convert-$TARGET.log" "$APP" --target "$TARGET" || rc=$?
  [ "$DRY" = 1 ] || cat "$WORK/convertcheck.out" >> "$LOG"
  [ "$rc" = 0 ] || die4 "NOT CONVERTED to $TARGET (convertcheck exit $rc): see $WORK/convertcheck.out and $WORK/convert-$TARGET.log. A 10.x below 10.24 must take the 10.24 rung first"
  commit_app "convert $TARGET" convert mx-convert
  rc=0; xo "$WORK/localedits-post-convert.out" python3 "$B/localedits.py" "$APP" --md "$WORK/localedits-post-convert.md" --json "$WORK/localedits-post-convert.json" || rc=$?
}

# one stepupdate batch, unattended. Exit 1 = modules kept (recorded), anything else = failure.
run_stepupdate() { # run_stepupdate PLAN label
  local plan=$1 rc=0 cmd="${UPG_UPDATE_CMD:-}"
  if [ "$DRY" != 1 ] && ! grep -qvE '^[[:space:]]*(#|$)' "$plan"; then note "$2 plan $plan has no module lines: no module updates"; return 0; fi
  [ -f "$WORK/approved.txt" ] || { [ "$DRY" = 1 ] || printf '# accepted step-idcheck findings: <pattern> # reason\n' > "$WORK/approved.txt"; }
  # an MPR name with a space broke the unquoted {mpr} in T1, T4, T8: quote it
  if [ -n "$cmd" ] && [[ "$cmd" != *"'{mpr}'"* ]] && [[ "$cmd" != *'"{mpr}"'* ]]; then cmd=${cmd//\{mpr\}/\'\{mpr\}\'}; fi
  local envs=("UPG_ROOT=$RUN")
  [ -z "$cmd" ] || envs+=("UPG_UPDATE_CMD=$cmd")
  # F1 (Purchase Request 10.24, real run): an edited module the judgment says to update anyway (and replay the edits) was
  # always KEPT, since --unattended keeps every refused module. $WORK/force-ui.txt names them, one per line.
  local fu=()
  if [ -f "$WORK/force-ui.txt" ]; then
    local mods; mods=$( { grep -vE '^[[:space:]]*(#|$)' "$WORK/force-ui.txt" || true; } | awk '{print $1}' | paste -sd, -)
    [ -z "$mods" ] || fu=(--force-ui "$mods" --saved-edits "$WORK/saved-edits")
  fi
  # R-hook (pr-rerun): $WORK/accept-unsaved.txt names modules whose update may commit although the installed package cannot
  # prove their theme/JavaScript files unedited (stepupdate --accept-unsaved; NanoflowCommons 6.0.0 is not in the catalog)
  local au=()
  if [ -f "$WORK/accept-unsaved.txt" ]; then
    local amods; amods=$( { grep -vE '^[[:space:]]*(#|$)' "$WORK/accept-unsaved.txt" || true; } | awk '{print $1}' | paste -sd, -)
    [ -z "$amods" ] || au=(--accept-unsaved "$amods")
  fi
  # cold rfq: $WORK/java-port.txt names modules whose local Java edits a person ports by hand onto the newer version
  # (stepupdate --port-java); the build waits for $WORK/java-port-done.txt
  local pj=()
  if [ -f "$WORK/java-port.txt" ]; then
    local jmods; jmods=$( { grep -vE '^[[:space:]]*(#|$)' "$WORK/java-port.txt" || true; } | awk '{print $1}' | paste -sd, -)
    [ -z "$jmods" ] || pj=(--port-java "$jmods")
  fi
  # F14: approved-step.txt holds step-only acceptances (a removal the replay restores): the step idcheck reads them,
  # the total idcheck (original vs final) never does, so a restore that did not happen still stops the run
  local apf="$WORK/approved.txt"
  if [ -f "$WORK/approved-step.txt" ]; then
    apf="$WORK/.approved-with-step.txt"
    [ "$DRY" = 1 ] || cat "$WORK/approved.txt" "$WORK/approved-step.txt" > "$apf"
  fi
  # the pre-convert localedits report tells stepupdate which modules have UI edits at all (UNSAVED, convert-made rows)
  local le=()
  [ ! -s "$WORK/localedits.json" ] || le=(--localedits "$WORK/localedits.json")
  # GM-23 / A-1: the model check after every step, read before the commit (stepcheck-run.sh = mx check under the heavy lock);
  # UPG_NO_STEPCHECK=1 turns it off. Answers: stepcheck-accepted.txt (errors accepted for a module), step-keep.txt (modules kept).
  # GM-24: the original-to-now idcheck at each batch end reads approved.txt only, never the step-only acceptances.
  local sc=()
  if [ "${UPG_NO_STEPCHECK:-0}" != 1 ]; then
    local scc="${UPG_STEPCHECK_CMD:-}"   # (a default inside ${..:-..} would end at the first } of {mpr})
    [ -n "$scc" ] || scc="bash $(printf %q "$B/stepcheck-run.sh") {mpr} {log}"
    envs+=("UPG_STEPCHECK_CMD=$scc")
    [ ! -s "$WORK/stepcheck-accepted.txt" ] || sc+=(--check-accepted "$WORK/stepcheck-accepted.txt")
  fi
  if [ -s "$WORK/step-keep.txt" ]; then
    local kmods; kmods=$( { grep -vE '^[[:space:]]*(#|$)' "$WORK/step-keep.txt" || true; } | awk '{print $1}' | paste -sd, -)
    [ -z "$kmods" ] || sc+=(--skip "$kmods")
  fi
  [ ! -f "$WORK/approved.txt" ] || sc+=(--approved-total "$WORK/approved.txt")
  xo "$WORK/stepupdate-$2.out" env "${envs[@]}" bash "$B/stepupdate.sh" "$APP" "$plan" --approved "$apf" \
    --baseline "$WORK/original.mpr" --unattended ${fu[@]+"${fu[@]}"} ${au[@]+"${au[@]}"} ${pj[@]+"${pj[@]}"} ${le[@]+"${le[@]}"} ${sc[@]+"${sc[@]}"} || rc=$?
  [ "$DRY" = 1 ] || cat "$WORK/stepupdate-$2.out" >> "$LOG"
  if [ "$rc" = 4 ] && [ "$DRY" != 1 ]; then stepcheck_stop "$2" || true; fi
  # a batch-end finding is said here, with the cause still near; the stop stays the total idcheck after the routes and replays
  # (a route restores GUIDs, so stopping before them would stop on what they repair)
  if [ "$DRY" != 1 ] && grep -q '^stepupdate: BATCH-IDCHECK original' "$WORK/stepupdate-$2.out" 2> /dev/null; then
    note "idcheck original -> now after the $2 batch has open finding(s): $(grep -c '^   BATCH-IDCHECK' "$WORK/stepupdate-$2.out") listed in $WORK/stepupdate-$2.out; the total idcheck decides after the routes and replays"
  elif [ "$DRY" != 1 ] && grep -q '^stepupdate: BATCH-IDCHECK could not run' "$WORK/stepupdate-$2.out" 2> /dev/null; then
    note "batch idcheck not run after the $2 batch, see $WORK/stepupdate-$2.out; the total idcheck after the routes and replays still runs"
  fi
  if [ "$rc" -gt 1 ]; then die4 "stepupdate ($2) failed (exit $rc), output: $WORK/stepupdate-$2.out"; fi
  return 0
}

# replay: the local edits of a --force-ui module, run after the updates and committed one module at a time ("replay: <Module>"):
#   $WORK/replay/<Module>.mdl    model edits, run with mxcli exec (write it against the NEW version's definition: a
#                                "create or modify entity" drops every attribute it does not list)
#   $WORK/replay/<Module>.patch  file edits (theme SCSS, JavaScript), a diff against the OLD package with paths relative to
#                                the app folder, applied with git apply onto the NEW files: copying the old files back would
#                                undo the update. A patch that does not apply is never applied in part: like a failed .mdl it is
#                                HELD (replay-held.txt, the gate stops 13), its own changes undone.
# A module that was kept (not updated) is not replayed: its edits are still there. The total idcheck that follows compares
# the result with the original, so a replay that misses a model edit stays visible.
replay_edits() { # replay_edits [pre]: pre = only modules the post-convert plan does not touch (their final version came
  # before the convert; F14: else the convert runs with MendixSSO's six associations gone); a replayed module is not redone
  [ -d "$WORK/replay" ] || return 0
  local f mod rc
  for f in "$WORK/replay"/*.mdl "$WORK/replay"/*.patch; do
    [ -f "$f" ] || continue
    mod=$(basename "$f"); mod=${mod%.*}
    if [ "${1:-}" = pre ] && grep -qE "^[0-9]+ [^ ]+ $mod([[:space:]]+#.*)?\$" "$WORK/plan.txt" 2> /dev/null; then continue; fi
    # one replay per module per rung: the 10.24 rung's replay must not skip the 11 rung's (editroute writes a new replay/ each rung)
    # no -q: grep must read the whole log, or git dies of SIGPIPE and pipefail makes the check false
    if [ "$DRY" != 1 ] && git_app log --format=%s 2> /dev/null | grep -xF "replay: $mod${UPG_PHASE:+ ($UPG_PHASE)}" > /dev/null; then note "replay $mod skipped: replayed already"; continue; fi
    if [ "$DRY" != 1 ] && grep -q "^$mod " "$APP/.stepupdate/kept.txt" 2> /dev/null; then note "replay $mod skipped: the module was kept, its edits are in place"; continue; fi
    rc=0 clean=1
    [ "$DRY" = 1 ] || [ -z "$(git_app status --porcelain 2> /dev/null)" ] || clean=0
    case "$f" in
      *.mdl) xo "$WORK/replay-$mod.out" mxcli_run exec "$f" -p "$MPR" || rc=$?
             # F14 (Purchase Request 10.24, real run): MendixSSO 10.6.2 dropped the six associations PurchaseApprovals
             # owns into MendixSSOUser. Re-created by MDL they get new GUIDs (DROP + ADD column, the data is gone), so
             # replay/<Module>.guids names the elements whose ORIGINAL GUID goes back (restore_guid.py, one per line)
             if [ "$rc" = 0 ] && [ -f "$WORK/replay/$mod.guids" ]; then
               local el
               while read -r el; do
                 case "$el" in ''|'#'*) continue ;; esac
                 xo "$WORK/replay-$mod-guid-${el##*.}.out" python3 "$B/restore_guid.py" "$MPR" "$el" --from "$WORK/original.mpr" || { rc=$?; break; }
               done < "$WORK/replay/$mod.guids"
             fi ;;
      *.patch) # F15 (Purchase Request 10.24, real run): Atlas_Core 4.5.0 rewrote the line next to the edited one, so the
               # context no longer matched. Fallbacks, in order: already in place (reverse applies) = nothing to do; every
               # removed block found exactly once in its file = apply without context (patch_unique.py); else a stop
               if xo "$WORK/replay-$mod-patch.out" git -C "$APP" apply --check "$f"; then
                 xo "$WORK/replay-$mod-patch.out" git -C "$APP" apply "$f" || rc=$?
               elif git -C "$APP" apply --check --reverse "$f" > /dev/null 2>&1; then
                 note "replay $mod: the edit is already in place"
               elif xo "$WORK/replay-$mod-unique.out" python3 -I "$B/patch_unique.py" "$f" "$APP" &&
                    xo "$WORK/replay-$mod-patch.out" git -C "$APP" apply --check -C0 "$f"; then
                 xo "$WORK/replay-$mod-patch.out" git -C "$APP" apply -C0 "$f" || rc=$?
                 note "replay $mod: context changed, applied without context (each removed line unique in its file)"
               else rc=1; fi ;;
    esac
    local rlog="$WORK/replay-$mod$([ "${f##*.}" = patch ] && echo -patch).out"
    if [ "$rc" != 0 ] && [ "$clean" = 0 ]; then
      nj_meta agent; nj_file 13 "replay of $mod failed (exit $rc) on a tree that was not clean before it, so it cannot be undone: $f" "$rlog" 30; nj_flush
    elif [ "$rc" != 0 ]; then
      # a failed replay is held, not a stop (WM1): its own changes are undone (the tree was clean before it), the build,
      # journeys and gate still run and give evidence, and the gate stops 13 on replay-held.txt until a person decides
      git_app checkout -q -- . 2> /dev/null || true
      git_app ls-files -z --others --exclude-standard 2> /dev/null | (cd "$APP" && xargs -0 rm -f --)   # paths are relative to the app
      printf '%s exit %s: %s (log: %s)\n' "$mod" "$rc" "$f" "$rlog" >> "$WORK/replay-held.txt"
      note "replay $mod HELD (exit $rc): its changes undone, the run goes on; the gate stops on $WORK/replay-held.txt"
      continue
    fi
    [ ! -f "$WORK/replay-held.txt" ] || { grep -v "^$mod exit " "$WORK/replay-held.txt" > "$WORK/replay-held.txt.n" || true; mv "$WORK/replay-held.txt.n" "$WORK/replay-held.txt"; }
    commit_app "replay: $mod${UPG_PHASE:+ ($UPG_PHASE)}" replay "replay-$mod"
    note "replayed the local edits of $mod from $f"
  done
}

# mxcli v0.28.0 (#1502): `--save-edits` also writes the associations OTHER modules own that point into the updated module, as
# saved-edits/<Module>/association-<Owner>_<Name>.mdl (the update removes them with the entity). One that no replay/<Module>.mdl
# names is a lost association: noted here, and the total idcheck (original vs now) shows its removal.
assoc_unreplayed() {
  [ "$DRY" != 1 ] || return 0
  local f mod qn
  for f in "$WORK"/saved-edits/*/association-*.mdl; do
    [ -f "$f" ] || continue
    mod=$(basename "$(dirname "$f")"); mod=${mod%%.*}
    qn=$(grep -m1 -ioE 'association +[A-Za-z0-9_]+\.[A-Za-z0-9_]+' "$f" | awk '{print $2}')
    [ -n "$qn" ] || continue
    if [ ! -f "$WORK/replay/$mod.mdl" ] || ! grep -qF "$qn" "$WORK/replay/$mod.mdl"; then
      note "association $qn (owned by another module, removed by the $mod update) is saved in $f but no replay/$mod.mdl creates it: NOT replayed"
    fi
  done
}

# Cold WM1: editroute held both Atlas layouts for a person (edit-routes.json held[]) inside a replay that itself ran fine,
# so nothing stopped; every page lost the app's shell and only the screens caught it. A held element is a local edit that
# is NOT in the app, like a failed replay: it goes in replay-held.txt (as "<module> held: ...") and the gate stops 13.
held_routes() {
  [ "$DRY" != 1 ] && [ -s "$WORK/edit-routes.json" ] || return 0
  local f="$WORK/replay-held.txt" n
  [ ! -f "$f" ] || { grep -v '^[^ ]* held: ' "$f" > "$f.n" || true; mv "$f.n" "$f"; }
  python3 - "$WORK/edit-routes.json" >> "$f" <<'PY' || note "held_routes: edit-routes.json unreadable, held elements not listed"
import json, sys
for x in json.load(open(sys.argv[1])):
    for h in x.get("held") or []:
        print(f"{x.get('module')} held: {h} (edit-routes.json)")
PY
  n=$(grep -c '^[^ ]* held: ' "$f" 2> /dev/null || true)
  [ "${n:-0}" = 0 ] || note "editroute: $n element(s) held for a person are not in the app; the gate stops on $f"
  [ -s "$f" ] || rm -f "$f"
}

# route_kept (cold test WM1): a module the update refused is not kept at its old version by default. editroute.py routes each one
# (diagram-only, UI and constants replayed, unreadable but unedited, files kept as copies, vendor drops nothing uses, associations
# of other modules replayed with their ids) and a second stepupdate pass updates the routed modules; only HOLD rows stay kept.
route_kept() {
  if [ "$DRY" = 1 ]; then x python3 "$B/editroute.py" plan --work "$WORK" --app "$APP" --original "$WORK/original.mpr" --plan "$WORK/plan.txt"; return 0; fi
  [ -s "$APP/.stepupdate/kept.txt" ] || return 0
  local rc=0 le=()
  [ ! -s "$WORK/localedits.json" ] || le=(--localedits "$WORK/localedits.json")
  xo "$WORK/editroute.out" python3 "$B/editroute.py" plan --work "$WORK" --app "$APP" --original "$WORK/original.mpr" --plan "$WORK/plan.txt" "${le[@]}" || rc=$?
  cat "$WORK/editroute.out" >> "$LOG"
  [ "$rc" = 0 ] || { note "editroute: no kept module could be routed, they stay kept (see $WORK/editroute.out)"; return 0; }
  local pass
  for pass in 1 2 3; do   # a routed update can keep a module for a second reason (WM1 Email_Connector: diagram-only, then 3 associations)
    run_stepupdate "$WORK/route-plan.txt" routed
    [ -s "$APP/.stepupdate/kept.txt" ] && [ "$pass" -lt 3 ] || break
    rc=0; xo "$WORK/editroute.out" python3 "$B/editroute.py" plan --work "$WORK" --app "$APP" --original "$WORK/original.mpr" --plan "$WORK/plan.txt" "${le[@]}" || rc=$?
    cat "$WORK/editroute.out" >> "$LOG"
    [ "$rc" = 0 ] || break
  done
  # check with the mxcli that exec runs (the container's may be older than the local one)
  local chk="$B/mxcli-container.sh"; [ -z "${MXCLI:-}" ] || [ ! -x "$MXCLI" ] || chk=$MXCLI
  rc=0; xo "$WORK/editroute-collect.out" env UPG_MXCLI_CHECK="$chk" python3 "$B/editroute.py" collect --work "$WORK" || rc=$?
  cat "$WORK/editroute-collect.out" >> "$LOG"
  ! grep -q '^HELD ' "$WORK/editroute-collect.out" || note "editroute: $(grep -c '^HELD ' "$WORK/editroute-collect.out" || true) replayed element(s) held for a person: $(grep '^HELD ' "$WORK/editroute-collect.out" | head -3 | tr '\n' ';')"
  note "editroute: $(grep -c '^ROUTE' "$WORK/editroute.out" || true) kept module(s) routed, $(grep -c ' HOLD:' "$WORK/editroute.out" || true) held for a person (edit-routes.json)"
}

# update: module updates with the post-convert plan; kept modules are routed (route_kept), the rest decided at the gate.
step_update() {
  [ -f "$WORK/plan.txt" ] || [ "$DRY" = 1 ] || { nj_meta agent; nj_add 13 "plan.txt missing" "$WORK/plan.txt does not exist"; nj_flush; }
  # an update rerun cannot redo this rung's replays: the module steps read as applied ("0 committed"), replay skips what the
  # log holds, and the replayed copies and menu pointers stay. Cold WM1: an older replay's empty Account_Overview copy
  # stayed in the menu after the rerun, the Local Users tab showed nothing. Rewind to the convert commit first.
  if [ "$DRY" != 1 ] && [ ! -f "$WORK/replay-keep.txt" ]; then
    local conv reps
    # awk reads the whole log: an awk that quit at the match made git log die of SIGPIPE, and under pipefail the step with it
    # (cold rfq rung 2, the convert the newest commit: exit 4 at this line, 29 of 40 tries)
    conv=$(git_app log --format='%h %s' 2> /dev/null | awk -v s="convert $TARGET" 'substr($0, index($0, " ") + 1) == s && c == "" { c = $1 } END { print c }')
    reps=$([ -z "$conv" ] || git_app log --format='%h %s' "$conv..HEAD" 2> /dev/null | grep -E '^[0-9a-f]+ replay: ' | head -5 | tr '\n' ';' || true)
    if [ -n "$reps" ]; then
      nj_meta info; nj_add 12 "Update rerun on an app that holds replay commits" "Since convert $conv: $reps an update rerun keeps their documents and menu changes and does not route again."
      nj_meta person "The update rerun finds replay commits already in the app. What should we do?" "" "rewind|Rewind the app to the convert commit|Tag a backup, rewind, rerun from update." "keep|Keep the replays|Create replay-keep.txt; the rerun keeps their documents and menu changes."; nj_add 12 "Decision" "Tag a backup, then rewind the app to $conv (git -C $APP tag backup/<name>; git -C $APP reset --hard $conv) and rerun --from update; to keep the replays, create $WORK/replay-keep.txt."
      nj_flush
    fi
  fi
  # a rerun starts as the first run did: an earlier routing's force-ui lines would force modules before they are routed
  [ "$DRY" = 1 ] || { python3 "$B/editroute.py" reset --work "$WORK" | tee -a "$LOG" > /dev/null || true; }
  # own modules that use a document the plan version drops get CE1613 after the update; say which before it (cold CMM:
  # Administration 4.5.0 has no UserRole_Select or RetrieveTimeZones, two own employee pages used them)
  if [ "$DRY" != 1 ]; then
    local orc=0
    xo "$WORK/owngone.out" python3 "$B/crosscalls.py" "$WORK/original.mpr" --kept '' --own --plan-file "$WORK/plan.txt" || orc=$?
    if grep -q '^  GONE' "$WORK/owngone.out" 2> /dev/null; then
      note "own modules use $(grep -c '^  GONE' "$WORK/owngone.out") target(s) the plan versions drop: CE1613 after the update, see $WORK/owngone.out (steps/repair.md row 28)"
    elif [ "$orc" = 2 ]; then
      note "crosscalls --own exit 2: own modules not checked against the plan versions, see $WORK/owngone.out"
    fi
  else
    x python3 "$B/crosscalls.py" "$WORK/original.mpr" --kept '' --own --plan-file "$WORK/plan.txt"
  fi
  run_stepupdate "$WORK/plan.txt" post-convert
  route_kept
  replay_edits
  held_routes
  if [ "$DRY" != 1 ] && [ -s "$WORK/edit-routes.json" ]; then   # did each route work, here and across runs (route ledger)
    local sl="${UPG_ROUTE_LEDGER:-${UPG_CACHE:-$HOME/.cache/upgrade-toolkit}/route-ledger.tsv}"; mkdir -p "$(dirname "$sl")"
    python3 "$B/editroute.py" score --work "$WORK" --app "$APP" --plan "$WORK/plan.txt" --ledger "$sl" > "$WORK/editroute-score.out" 2>&1 || true
    note "$(tail -1 "$WORK/editroute-score.out") (editroute-score.tsv; all runs: $sl)"
  fi
  assoc_unreplayed
  if [ "$DRY" != 1 ]; then
    # a stale kept.txt from an earlier pass parked a module updated since (cold WM1: Email_Connector, on 6.4.4 by then)
    if [ -s "$APP/.stepupdate/kept.txt" ]; then cp "$APP/.stepupdate/kept.txt" "$WORK/kept.txt"; else rm -f "$WORK/kept.txt"; fi
    kept_vendor_check update
    local rc=0
    xo "$WORK/jarclash.out" python3 "$B/repair/jarclash.py" "$APP" --md "$WORK/jarclash.md" || rc=$?
    [ "$rc" = 0 ] || note "jarclash after the updates exit $rc: classes in two jars, see $WORK/jarclash.md (clashes listed in jarclash-before.md are older than the upgrade)"
    # a widget another module's update replaced, styled by a kept module (cold CMM: Datagrid 2.30.6 under DataWidgets' old
    # styles; afterwalk passed every grid page, the rows rendered unstyled)
    rc=0
    xo "$WORK/widgetskew.out" python3 "$B/widgetskew.py" "$APP" --plan "$WORK/plan.txt" || rc=$?
    if [ "$rc" = 1 ] && [ ! -f "$WORK/widgetskew-ack.txt" ]; then
      nj_meta info; nj_file 13 "A module update replaced a widget whose styles stay with a kept module (steps/repair.md row 32)" "$WORK/widgetskew.out" 10 '^WIDGET-SKEW'
      nj_meta person "A module update replaced a widget whose styles stay with a kept module. What should we do?" "" "update|Update the kept module|One-line stepupdate plan." "restore|Put the old widget back|The old widget package returns." "accept|Accept the skew|Create widgetskew-ack.txt."; nj_add 13 "Decision" "Update the kept module (stepupdate with a one-line plan), or put the old widget back; to accept the skew, create $WORK/widgetskew-ack.txt."
      nj_park
    fi
    # a module update brought pages saved with a newer widget than the installed package: update-widgets (row 5) would
    # drop the settings the old package lacks (cold CMM: Administration 4.5.0's Roles filter lost its association mode)
    rc=0
    rm -f "$WORK/widgetdrop.json"
    xo "$WORK/widgetdrop.out" python3 "$B/widgetdrop.py" "$APP" --json "$WORK/widgetdrop.json" || rc=$?
    if [ "$rc" = 1 ] && [ ! -f "$WORK/widgetdrop-ack.txt" ]; then
      if grep -q '^WIDGET-DROP .*installed package lacks it' "$WORK/widgetdrop.out" && widget_drop_stop; then
        :
      elif grep -q '^WIDGET-DROP .*installed package lacks it' "$WORK/widgetdrop.out"; then
        nj_meta info; nj_file 13 "Widget settings that update-widgets would drop: the installed widget package is older than the pages (steps/repair.md row 33)" "$WORK/widgetdrop.out" 10 '^WIDGET-DROP'
        nj_meta person "Widget settings would be dropped: the installed widget package is older than the pages. What should we do?" "" "update|Update the module that ships the widget|Before the build." "accept|Accept the loss|Create widgetdrop-ack.txt."; nj_add 13 "Decision" "Update the module that ships the widget (stepupdate with a one-line plan) before the build; to accept the loss, create $WORK/widgetdrop-ack.txt."
      else   # cold rfq: every drop is a property a widget update in this rung removed upstream
        nj_meta info; nj_file 13 "Widget settings the newer widget no longer has: a module update in this rung replaced the widget (steps/repair.md row 33)" "$WORK/widgetdrop.out" 10 '^WIDGET-DROP'
        nj_meta person "A widget update in this rung removed settings the pages used. Have the pages been checked on the new widget?" "" "accept|Accept the loss after checking each page|Write widgetdrop-ack.txt with the reason."; nj_add 13 "Decision" "No module update brings these settings back. Check each page on the new widget (the listed setting now has the new widget's behaviour), then accept with a reason in $WORK/widgetdrop-ack.txt."
      fi
      nj_park
    elif [ "$rc" -ge 2 ]; then   # input error (model unreadable): nothing was checked, never read as "no drops"
      note "widgetdrop exit $rc: widget settings update-widgets would drop not checked, see $WORK/widgetdrop.out"
    fi
  else
    x python3 "$B/repair/jarclash.py" "$APP" --md "$WORK/jarclash.md"
    x python3 "$B/widgetskew.py" "$APP" --plan "$WORK/plan.txt"
    x python3 "$B/widgetdrop.py" "$APP"
  fi
  local rc=0 ap=()
  [ ! -f "$WORK/approved.txt" ] || ap=(--approved "$WORK/approved.txt")
  xo "$WORK/idcheck-total.out" python3 "$B/idcheck.py" "$WORK/original.mpr" "$MPR" --md "$WORK/idcheck-total.md" "${ap[@]}" || rc=$?
  if [ "$rc" != 0 ]; then
    nj_meta person "The update removes or changes data the app stores. What should we do?" "none:Each finding is data that may be lost; only the owner knows whether that data matters." "accept|Accept each finding in writing|One line per finding in approved.txt with a reason (steps/upgrade.md)." "keep|Keep the module at its old version|The module is dropped from the plan and listed as kept."; nj_file 13 "Total idcheck (original vs now) has open data-bearing findings (exit $rc)" "$WORK/idcheck-total.md" 30
    nj_park
  fi
}

# build: mx check + the FIXED repair rows + mxbuild + stubs commit + quick start.
# Fixed rows (steps/repair.md): 0 JavaVersion (CE2513), 1 backslash paths, 2 sync-java-dependencies, 3 jardedupe, 5 update-widgets
# (CE0463), 6 design_props_guard (CE6087), 36 gridlayout (theme, no code). Everything else (rows 4, 7-10 and own-document fixes) is a judgment stop (10).
CHECK_N=0
mxcheck() { # writes $WORK/check-N.log, sets CHECK_LOG
  CHECK_N=$((CHECK_N + 1)); CHECK_LOG="$WORK/check-$CHECK_N.log"
  # -j (mx 10 and later): the JSON names the document of each error, which the text output leaves out (cold CMM: four
  # CE0117 "at Action button 'actionButton1'" with no page); checkwhere.py appends those as [where] lines
  local cj="$WORK/check-$CHECK_N.json" j=()
  [ "$(major "$TARGET")" -le 9 ] || j=(-j "$cj")
  # -j goes AFTER the mpr: before it, mx prints its usage (steps/repair.md row 15, T8R2 R-6)
  if [ "$DRY" = 1 ]; then printf '+ %s check %s%s > %s\n' "$B/heavy-lock.sh check $(mxw "$TARGET") $TARGET mx" "$MPR" "${j[@]+" ${j[*]}"}" "$CHECK_LOG"; return 0; fi
  rm -f "$cj"
  heavy check "$TARGET" mx check "$MPR" ${j[@]+"${j[@]}"} > "$CHECK_LOG" 2>&1 || true
  [ ! -s "$cj" ] || python3 "$B/checkwhere.py" "$cj" "$CHECK_LOG" || true
  # no summary line = mx check died (it prints "The app contains: N errors." on every finished check, 0 included); a
  # crash is never 0 errors (cold CMM: a copied page with a stale pointer, KeyNotFoundException on load, and the run went on
  # to mxbuild with "0 errors")
  if ! grep -q 'The app contains:' "$CHECK_LOG" 2> /dev/null; then
    printf '[error] [MXCHECK] mx check ended without a result (it died loading or checking the model): %s\n' \
      "$(grep -m1 -E '^ERROR' "$CHECK_LOG" 2> /dev/null | cut -c1-200 || true)" >> "$CHECK_LOG"
  fi
}
has_code() { grep -q "\[$1\]" "$CHECK_LOG" 2> /dev/null; }
try_fix() { # try_fix "subject" RULE CODES cmd...: run a fixer, re-check, keep when checkdiff says not worse, else undo
  local subj=$1 rule=$2 codes=$3 prev rc=0; shift 3
  prev=$CHECK_LOG
  x "$@" || { note "fixer '$subj' failed (exit $?): left undone"; [ "$DRY" = 1 ] || { git_app checkout -q -- . ; git_app clean -fdq; }; return 0; }
  mxcheck
  [ "$DRY" = 1 ] && return 0
  python3 "$B/checkdiff.py" "$prev" "$CHECK_LOG" --fixed "$codes" >> "$LOG" 2>&1 || rc=$?
  if [ "$rc" = 0 ]; then commit_app "repair: $subj" repair "$rule"; say "        repair: $subj ($(open_errors "$prev") -> $(open_errors "$CHECK_LOG") errors)"
  else note "fix '$subj' made mx check WORSE (checkdiff exit $rc): undone"; git_app checkout -q -- . ; git_app clean -fdq; CHECK_LOG=$prev; fi
}
# row 37 (cold rung 2: 36 Any Chart uses stopped the build with "replace with Charts 6" and a list of documents): every
# deprecated widget gets one route per module from playbooks/widget-routes.json (bin/repair/widgetroute.py). The toolkit
# heals itself: the recommended candidate goes into the test build, each kind its own repair commit (mx check may not get
# worse, else undone): replace (Any Chart -> Custom chart, update-widgets in it), wrap (a use straight on a snippet
# parameter gets a data view on it first) and remove (a sample module nothing opens). A pass that was undone makes its
# route propose the next candidate. What was applied waits for one OK at the end (widget_routes_ok); the person's B
# (keep-module M, route-b R in widget-routes-approved.txt) undoes it on the rerun (widgetroute_undo).
widgetroute_pass() { # widgetroute_pass replace|wrap|remove
  local rc=0
  rm -f "$WORK/widgetroute.mdl"
  python3 "$B/repair/widgetroute.py" "$APP" --target "$TARGET" --approved "$WORK/widget-routes-approved.txt" --apply --pass "$1" \
    --done "$WORK/widgetroute-done.new" --mdl "$WORK/widgetroute.mdl" || rc=$?
  [ "$rc" -le 1 ] || return "$rc"
  if [ "$1" = remove ]; then [ ! -s "$WORK/widgetroute.mdl" ] || mxcli_run exec "$WORK/widgetroute.mdl" -p "$MPR"
  else heavy update-widgets "$TARGET" mx update-widgets "$MPR"; fi
}
widgetroute_undo() { # the person picked B on the one-OK list: revert what the test build did for it, once
  local ok="$WORK/widget-routes-approved.txt" done="$WORK/widgetroute-done.txt" h subj pat
  [ -f "$ok" ] && [ -f "$done" ] || return 0
  for subj in "unused sample module removed" "deprecated widgets"; do
    if [ "$subj" = "deprecated widgets" ]; then pat=$(sed -nE 's/^(REPLACED|APPROXIMATED) [^ ]+ [^ ]+ \[([a-z0-9]+)\] .*/route-b \2/p' "$done")
    else pat=$(sed -nE 's/^REMOVED-MODULE ([^ ]+) .*/keep-module \1/p' "$done"); fi
    [ -n "$pat" ] && sed 's/[[:space:]]*#.*//' "$ok" | grep -qxF "$pat" || continue
    for h in $(git_app log --format='%H %s' | awk -v s="repair: $subj" 'index($0, " " s) && / \(widgetroute\)$/ {print $1}'); do
      git_app revert --no-commit "$h" > /dev/null 2>&1 || { note "widgetroute: could not revert $h, see git -C $APP status"; git_app revert --abort > /dev/null 2>&1; return 0; }
    done
    commit_app "repair: undone on the person's B ($subj, widgetroute)" repair repair-widgetroute
    if [ "$subj" = "deprecated widgets" ]; then sed -i.bak -E '/^(REPLACED|APPROXIMATED) /d' "$done"; else sed -i.bak '/^REMOVED-MODULE /d' "$done"; fi
    rm -f "$done.bak"; note "widgetroute: B picked, '$subj' undone"
  done
}
nj_sections() { # nj_sections CODE FILE: "## title" sections written by a tool, each one stop item
  [ -s "$2" ] || return 0
  [ "$NJ_CODE" != 0 ] || NJ_CODE=$1
  { echo; sed "s/^## \(.*\)$/## \1 (exit $1)/" "$2"; } >> "$NJ_TMP"
}
widget_routes() {
  local rc=0 wr=(python3 "$B/repair/widgetroute.py" "$APP" --target "$TARGET" --approved "$WORK/widget-routes-approved.txt")
  if [ "$DRY" = 1 ]; then
    xo "$WORK/widgetroute.txt" "${wr[@]}"
    try_fix "deprecated widgets replaced (widgetroute)" repair-widgetroute CE0463 widgetroute_pass replace
    try_fix "deprecated widgets wrapped in a data view and replaced (widgetroute)" repair-widgetroute CE0463 widgetroute_pass wrap
    try_fix "unused sample module removed (widgetroute)" repair-widgetroute CE0463 widgetroute_pass remove
    return 0
  fi
  widgetroute_undo
  xo "$WORK/widgetroute.txt" "${wr[@]}" || rc=$?
  if [ "$rc" -ge 2 ]; then   # no route could be read: the plain list, as before
    nj_meta agent; nj_file 10 "Charts 3.x widgets on an 11 target: replace with Charts 6.x before the gate (T7-29)" "$WORK/missing_deps.txt" 30 '^DEPRECATED-11'
    return 0
  fi
  local pass subj pat failed=""
  for pass in replace wrap remove; do
    case "$pass" in
      replace) pat='^  WOULD-(REPLACE|APPROXIMATE) '; subj="deprecated widgets replaced (widgetroute)" ;;
      wrap)    pat='^  WOULD-WRAP '; subj="deprecated widgets wrapped in a data view and replaced (widgetroute)" ;;
      remove)  pat='-> remove the module: .*\[AUTO\]'; subj="unused sample module removed (widgetroute)" ;;
    esac
    grep -qE -- "$pat" "$WORK/widgetroute.txt" || continue
    rm -f "$WORK/widgetroute-done.new"
    try_fix "$subj" repair-widgetroute CE0463 widgetroute_pass "$pass"
    if [ "$(git_app log -1 --format=%s)" = "repair: $subj" ]; then
      [ ! -f "$WORK/widgetroute-done.new" ] || cat "$WORK/widgetroute-done.new" >> "$WORK/widgetroute-done.txt"
    else failed="$failed${failed:+,}$pass"; note "widgetroute: $pass made mx check worse or failed: undone, the next candidate is proposed (see $LOG)"; fi
  done
  rc=0; xo "$WORK/widgetroute.txt" "${wr[@]}" --failed "$failed" --report "$WORK/widgetroute-report.md" --json "$WORK/widgetroute.json" || rc=$?
  note "widgetroute: $(tail -1 "$WORK/widgetroute.txt") (see $WORK/widgetroute.txt)"
  [ "$rc" != 1 ] || nj_sections 10 "$WORK/widgetroute-report.md"
}
widget_routes_ok() { # end of build: what the test build applied, one OK per route and per removed module (parked in Interview mode auto)
  [ "$DRY" != 1 ] && [ -s "$WORK/widgetroute-done.txt" ] || return 0
  python3 "$B/repair/widgetroute.py" "$APP" --target "$TARGET" --approved "$WORK/widget-routes-approved.txt" \
    --ok-report "$WORK/widgetroute-done.txt" > "$WORK/widgetroute-ok.md" || return 0
  nj_sections 10 "$WORK/widgetroute-ok.md"
  nj_park
}
step_build() {
  local n=0 rc=0
  # cold rfq: an update with --port-java replaced Java files that carried a local edit; mxbuild would pass without it
  # (javac knows nothing of the edit), so the build waits until a person ports it and writes $WORK/java-port-done.txt
  if [ "$DRY" != 1 ] && [ ! -f "$WORK/java-port-done.txt" ]; then
    local pjl; pjl=$(cat "$WORK"/stepupdate-*.out 2> /dev/null | grep -E '^ *PORT-JAVA ' | sed 's/^ *//' | sort -u || true)
    if [ -n "$pjl" ]; then
      nj_meta agent; nj_add 13 "Local Java edits to port by hand before the build" "The update replaced these files; the old edited copy is under the path shown. Port each edit onto the new file, commit it in the app, then write $WORK/java-port-done.txt (one line per file: what was ported) and rerun.

$pjl"
      nj_flush
    fi
  fi
  CHECK_N=0
  local f
  for f in "$WORK"/check-*.log; do if [ -e "$f" ]; then CHECK_N=$((CHECK_N + 1)); fi; done
  mxcheck
  # row 1: literal backslashes in file names (OQL package)
  if [ "$DRY" = 1 ] || [ -n "$(find "$APP" -maxdepth 1 -name '*\\*' -print -quit)" ]; then
    try_fix "backslash paths" repair-row-1 CE0463 python3 "$B/repair/backslash_paths.py" "$APP" --apply
  fi
  # row 0: Java 11 setting after a 9 -> 10 convert, and after a 10.0 to 10.6 -> 10.24 convert (CHK-3: the 10.6 project says Java11 too)
  if { [ "$DRY" = 1 ] && { [ "$(major "$SOURCE")" -le 9 ] || { [ "$(major "$SOURCE")" = 10 ] && [ "$(minor "$SOURCE")" -le 6 ]; }; }; } ||
     { [ "$DRY" != 1 ] && has_code CE2513; }; then
    try_fix "JavaVersion Java21" repair-row-0 CE2513 mxcli_run -p "$MPR" -c "alter settings model JavaVersion = 'Java21'"
  fi
  # row 35: an expression text parameter that kept a source variable (9.24 ignored it, 10 says CE7005)
  if [ "$DRY" = 1 ] || has_code CE7005; then
    try_fix "expression parameter source" repair-row-35 CE7005 python3 "$B/repair/exprparam_source.py" "$APP" --apply
  fi
  # rows 2 and 3: always, before the first build
  rc=0; xo "$WORK/logs/sync-java.log" heavy sync "$TARGET" mx sync-java-dependencies "$MPR" || rc=$?
  if [ "$rc" != 0 ]; then
    # T2-9, T6-2, T7-8, T8-14: Gradle behind the proxy; the failed sync still lists the deps: resolve them with host Maven
    local vrc=0; x bash "$B/cloud/vendorlib_mvn.sh" "$APP" "$WORK/logs/sync-java.log" --apply || vrc=$?
    if [ "$vrc" = 0 ]; then note "mx sync-java-dependencies failed (exit $rc); vendorlib filled by vendorlib_mvn.sh (host Maven)"
    else note "mx sync-java-dependencies failed (exit $rc), vendorlib_mvn.sh exit $vrc (3 = version range to pin), recorded NOT RUN; the build decides"; fi
  fi
  # --updated-from-git: the 'step:' commits prove which modules moved; without it the old userlib copies they left behind
  # stay (WM1: pdfbox 2.0.24 next to vendorlib 3.0.7, javac failed in CommunityCommons Misc.java:643)
  rc=0; x python3 "$B/repair/jardedupe.py" "$APP" --updated-from-git || rc=$?
  x python3 "$B/repair/jardedupe.py" "$APP" --updated-from-git --apply || true
  commit_app "repair: sync java dependencies, jardedupe" repair repair-row-2-3
  # module roles an update ADDED, mapped by name (WM1: Atlas_Core 4's language selector needs Atlas_Core.User; unmapped,
  # every page on an Atlas layout failed "for security reasons" while mx check stayed clean). Guest role: never granted.
  if [ -f "$WORK/original.mpr" ]; then
    rm -f "$WORK/modroles.mdl"
    xo "$WORK/modroles.txt" python3 "$B/repair/modroles.py" "$MPR" --original "$WORK/original.mpr" --mdl "$WORK/modroles.mdl" || true
    if [ "$DRY" != 1 ] && [ -s "$WORK/modroles.mdl" ]; then
      rc=0; xo "$WORK/modroles-exec.out" mxcli_run exec "$WORK/modroles.mdl" -p "$MPR" || rc=$?
      [ "$rc" = 0 ] || note "modroles: exec failed (exit $rc), see $WORK/modroles-exec.out"
      commit_app "repair: map module roles the updates added" repair repair-modroles
    fi
    [ "$DRY" = 1 ] || note "$(tail -1 "$WORK/modroles.txt") (see $WORK/modroles.txt)"
  fi
  # row 4: missing or broken packages are noted (mx check reports what matters); DEPRECATED-11 builds clean but fails at
  # runtime on 11 (T7-29), so it stops here
  rc=0; xo "$WORK/missing_deps.txt" python3 "$B/repair/missing_deps.py" "$APP" --target "$TARGET" || rc=$?
  if [ "$DRY" != 1 ] && [ "$rc" = 1 ]; then
    note "missing_deps: $(grep -cE '^(MISSING|BROKEN)' "$WORK/missing_deps.txt" || true) missing or broken (see $WORK/missing_deps.txt)"
    # issue 24 (SNOW, Atlas_Core 4.7.0 needs FeedbackModule): a module an UPDATE made necessary is a person's decision, said before the
    # build goes on. Never installed here: it adds a module to the owner's app. missing_module_stop.py header has the design note.
    if grep -q '^MISSING module' "$WORK/missing_deps.txt"; then
      local msrc=0
      python3 "$B/repair/missing_module_stop.py" "$WORK/missing_deps.txt" "$WORK/plan.txt" --app "$APP" --ack "$WORK/missing-module-ack.txt" > "$WORK/missing-module.out" 2> /dev/null || msrc=$?
      if [ "$msrc" = 1 ]; then
        local mq mr mo=() mb
        mq=$(sed -n 's/^Q\t//p' "$WORK/missing-module.out"); mr=$(sed -n 's/^R\t//p' "$WORK/missing-module.out")
        mapfile -t mo < <(sed -n 's/^O\t//p' "$WORK/missing-module.out"); mb=$(sed -n 's/^B\t//p' "$WORK/missing-module.out")
        nj_meta person "$mq" "$mr" "${mo[@]}"; nj_add 13 "An updated module needs a module the app does not have (CE1613 after the update)" "$mb"
        nj_flush
      fi
    fi
    if grep -q '^DEPRECATED-11' "$WORK/missing_deps.txt"; then widget_routes; fi
  elif [ "$DRY" != 1 ] && [ "$rc" -ge 2 ]; then   # INVALID: nothing was checked, never read as "0 missing"
    note "missing_deps exit $rc: missing, broken and Charts 3.x packages not checked: $(grep -m1 'INVALID' "$WORK/missing_deps.txt" || tail -1 "$WORK/missing_deps.txt") (see $WORK/missing_deps.txt)"
  fi
  [ "$DRY" != 1 ] || widget_routes
  # row 5, row 6
  if [ "$DRY" = 1 ] || has_code CE0463; then try_fix "update-widgets" repair-row-5 CE0463 heavy update-widgets "$TARGET" mx update-widgets "$MPR"; fi
  if [ "$DRY" = 1 ] || has_code CE6087; then
    try_fix "design properties" repair-row-6 CE6087 "$B/repair/design_props_guard.sh" "$APP" "$TARGET" --fixed CE6087 -- "$(mxw "$TARGET")" "$TARGET" mx rename-design-properties APP
  fi
  # row 36: an app theme rule written for the Data Widgets 2 markup (display: block !important on .widget-datagrid .table)
  # overrides the Data Widgets 3 grid: every cell its own row, while mx check, build and smoke pass (cold 9.24 -> 10.24).
  # Theme only, so no mx check round: its own commit, the SAY line to the person, and a screen cause for the screens rung
  rc=0; xo "$WORK/gridlayout.out" python3 "$B/repair/gridlayout.py" "$APP" --causes "$WORK/screen-causes.txt" || rc=$?
  if [ "$DRY" != 1 ] && grep -q '^FIXED' "$WORK/gridlayout.out" 2> /dev/null; then
    commit_app "repair: data grid 2 layout (old theme rule commented out)" repair repair-row-36
    say "        repair: $(sed -n 's/^SAY //p' "$WORK/gridlayout.out")"
  elif [ "$rc" != 0 ]; then note "gridlayout exit $rc (see $WORK/gridlayout.out): not repaired"; fi
  # all fixed rows done: where do we stand
  [ "$DRY" = 1 ] || { mxcheck; n=$(open_errors "$CHECK_LOG"); }
  # bounded loop (fix, recheck, again while it makes progress): a fixed row can expose the code of another one (L42), so the rows
  # whose code is still open run again, at most 2 more rounds, and the loop stops at the first round that lowers nothing
  if [ "$DRY" != 1 ] && [ "$n" != 0 ] && [ "${UPG_BUILD_ROUNDS:-2}" -gt 0 ]; then
    local brnd=0 bprev
    while [ "$brnd" -lt "${UPG_BUILD_ROUNDS:-2}" ] && [ "$n" != 0 ]; do
      brnd=$((brnd + 1)); bprev=$n
      if has_code CE0463; then try_fix "update-widgets (round $((brnd + 1)))" repair-row-5 CE0463 heavy update-widgets "$TARGET" mx update-widgets "$MPR"; fi
      if has_code CE6087; then try_fix "design properties (round $((brnd + 1)))" repair-row-6 CE6087 "$B/repair/design_props_guard.sh" "$APP" "$TARGET" --fixed CE6087 -- "$(mxw "$TARGET")" "$TARGET" mx rename-design-properties APP; fi
      mxcheck; n=$(open_errors "$CHECK_LOG")
      if [ "$n" -ge "$bprev" ]; then note "build loop round $((brnd + 1)): $bprev -> $n errors, no progress: stop"; break; fi
      note "build loop round $((brnd + 1)): $bprev -> $n errors"
    done
  fi
  if [ "$DRY" != 1 ] && [ "$n" != 0 ]; then
    nj_meta agent; nj_add 10 "mx check: $n errors after convert + updates + the fixed repair rows" "Summary file: $CHECK_LOG
Codes: $(grep -oE '^\[error\] *\[C[EW][0-9]+\]' "$CHECK_LOG" | grep -oE 'C[EW][0-9]+' | sort | uniq -c | sort -rn | head -n 15 | tr '\n' ';')
Work the list with steps/repair.md (rows 4, 7-10 and own-document fixes; one commit per fix; checkdiff.py after each)."
    nj_meta info; nj_file 10 "First 20 error lines" "$CHECK_LOG" 20 '^\[error\]'
    grep -q '^\[where\]' "$CHECK_LOG" 2> /dev/null && { nj_meta info; nj_file 10 "Where they are (first 20)" "$CHECK_LOG" 20 '^\[where\]'; }
    if has_code CE1613 && grep -q '^  GONE' "$WORK/owngone.out" 2> /dev/null; then
      nj_meta info; nj_file 10 "Own documents use targets the module update dropped (CE1613; steps/repair.md row 28)" "$WORK/owngone.out" 20 '^(OWN|  GONE)'
    fi
    nj_flush
  fi
  # mxbuild
  disk_gate build
  rc=0; xo "$WORK/build-$TARGET.log" heavy build "$TARGET" mxbuild --target=package -o "$(mda_new)" "$MPR" || rc=$?
  if [ "$rc" != 0 ] && modcase_fix "$WORK/build-$TARGET.log"; then   # LDMS: add-on cache folder case on Linux (repair row 34)
    rc=0; xo "$WORK/build-$TARGET.log" heavy build "$TARGET" mxbuild --target=package -o "$(mda_new)" "$MPR" || rc=$?
  fi
  n=0; [ "$DRY" = 1 ] || n=$(grep -c '^ERROR at' "$WORK/build-$TARGET.log" 2> /dev/null || true)
  # the stubs come from the model, built or not: committed before a stop too. Cold rfq rung 2: a javac stop left 18 stub files
  # uncommitted, and the rerun from update died in stepupdate ("uncommitted changes; commit or stash first", exit 4)
  commit_app "build: regenerated stubs" config build-stubs
  if [ "$DRY" != 1 ] && { [ "$rc" != 0 ] || [ "$n" != 0 ] || [ ! -f "$(mda_new)" ]; }; then
    disk_cause "$WORK/build-$TARGET.log"
    nj_meta agent; nj_add 10 "mxbuild failed (exit $rc, $n ERROR at lines)" "Summary file: $WORK/build-$TARGET.log (a 30 s theme-compile timeout is not a model error: retry when the machine is quiet; javac errors: javafinal.py, kept-module API removals)"
    nj_meta info; nj_file 10 "First 20 error lines" "$WORK/build-$TARGET.log" 20 '^ERROR at|error:|ERROR'
    # cold CMM: a userlib fat jar's older Netty hid the class MendixSSO 10.6.2 needs; name the jar, not only the error
    if grep -q 'error: cannot find symbol' "$WORK/build-$TARGET.log" 2> /dev/null; then
      xo "$WORK/javacjar.out" python3 "$B/repair/javacjar.py" "$APP" "$WORK/build-$TARGET.log" || true
      if grep -q '^  HIDDEN BY' "$WORK/javacjar.out" 2> /dev/null; then
        nj_meta agent; nj_file 10 "An older copy of a class inside another jar hides what the code needs (steps/repair.md row 31)" "$WORK/javacjar.out" 20 '^(SYMBOL|  HAS|  HIDDEN BY)'
      fi
    fi
    nj_flush
  fi
  if [ "$DRY" != 1 ] && [ "$rc" = 0 ] && [ "$n" = 0 ] && [ -f "$(mda_new)" ]; then close_proved_rows; fi   # GM-38: a green build only
  # quick start (mandatory before the gate)
  local q
  q=$(fresh_name "${X}_quick"); copy_db "$X_FROZEN" "$q"
  rc=0; runenv; x env "${RUNENV[@]}" python3 "$B/runapp.py" quick new "$(mda_new)" "$TARGET" "$q" || rc=$?
  mark_used "$q" quickstart
  infra_rc "$rc" quick
  if [ "$rc" != 0 ]; then
    nj_meta agent; nj_add 10 "QUICK START FAIL" "The new app does not start. Fix before the gate (after-startup contract, constants, missing jars). Start log: $WORK/logs/runtime-new.log"
    nj_meta info; nj_file 10 "First 20 error lines" "$WORK/logs/runtime-new.log" 20 'ERROR|CRITICAL|Exception'
    nj_flush
  fi
  widget_routes_ok
}

# after: the new app on a fresh copy of the frozen DB, snapshot after. Scripts: runapp.py, snapshot.py
step_after() {
  local db rc=0
  db=$(fresh_name "${X}_after"); copy_db "$X_FROZEN" "$db"
  app_up newafter "$(mda_new)" "$TARGET" "$db" || { nj_meta agent; nj_file 10 "New app did not start on a copy of the frozen DB" "$WORK/logs/runtime-newafter.log" 20 'ERROR|CRITICAL|Exception'; nj_flush; }
  local ep_args=()
  [ ! -s "$WORK/endpoints.txt" ] || ep_args=(--endpoints "$WORK/endpoints.txt")
  x python3 "$B/snapshot.py" --label after --ledger "$WORK/db-ledger.txt" --psql "$(psql_str "$db")" \
    --app-url "http://localhost:$APP_PORT" "${ep_args[@]}" --log-cmd "docker logs ${UPG_NAME:-mig}-newafter" \
    --admin-url "http://localhost:$ADMIN_PORT" --admin-pass "$M2EE_PASS" --out "$WORK/after.json" || rc=$?
  app_down newafter
  [ "$rc" = 0 ] || die4 "snapshot after failed (exit $rc), log: $LOG"
}

# afterwalk: impact map, smoke walk of the NEW project against the baseline. Scripts: impact_map.py, smokewalk_gen.py, smoke_users.py, smokewalk.js
step_afterwalk() {
  local roles rc=0 db
  must python3 "$B/impact_map.py" "$WORK/original.mpr" "$MPR" --out "$WORK/impact.json" --md "$WORK/impact.md"
  must python3 "$B/smokewalk_gen.py" "$APP" -o "$WORK/plan-new.json"
  roles=""; [ "$DRY" = 1 ] || roles=$(roles_of_plan "$WORK/plan-new.json")
  [ "$DRY" = 1 ] && roles="Role1,Role2"
  user_args "$roles"
  db=$(fresh_name "${X}_smoke_new"); copy_db "$X_FROZEN" "$db"
  app_up newwalk "$(mda_new)" "$TARGET" "$db" || { nj_meta agent; nj_file 10 "New app did not start for the smoke walk" "$WORK/logs/runtime-newwalk.log" 20 'ERROR|CRITICAL|Exception'; nj_flush; }
  must python3 "$B/smoke_users.py" "$db" --roles "$roles" --apply
  x node "$B/smokewalk.js" --plan "$WORK/plan-new.json" --url "http://localhost:$APP_PORT" "${UARGS[@]}" $(smoke_mf) --login-path "$(login_path)" \
    --compare "$WORK/smoke-before.json" --out "$WORK/smoke-after.json" --shots "$WORK/smoke-after-shots" || rc=$?
  app_down newwalk
  mark_used "$db" walk
  if [ "$rc" != 0 ]; then
    nj_meta person "A step that passed on the old app fails or breaks on the new one. What should we do?" "fix" "fix|Fix the app, then rerun|The old app passes it, so the upgrade changed behaviour (steps/heal.md: heal the test, never the app)." "accept|Accept it as intended, in writing|A reason per line in the allow files (steps/gate.md)." "test|The test is wrong: fix the test|Only when the step fails the same way on the old app."; nj_file 12 "Smoke walk vs baseline (exit $rc: 1 = a PASS step regressed or broke, 2 = INVALID): a gate FAIL/INVALID, not a pass" "$LOG" 40 'REGRESS|FAIL|INVALID'
    nj_park
  fi
}

# Each run_journeys call gets --psql for the database the app runs on (F7, Purchase Request 10.24: without it every data
# rung was INVALID "no --psql / UPG_PSQL", though the pipeline made that database itself).
# --data-rung: the journeys always get --psql (F7), so the own-row check (a create's ${RUN_ID} row exists) is asked
heal_on() { [ "${UPG_HEAL:-1}" != 0 ]; }
# AD-1: run_journeys.py exit 75 = the app went down under the run (FSM 10.24 baseline: the runtime died after 53 min, 297
# journeys "did not run" and counted as baseline defects). Restart the app on the SAME database, as if it had not stopped,
# and run only the journeys left (--resume merges them into the same summary.json); at most UPG_RESUME_TRIES (2) times.
journeys_resume() { # journeys_resume NAME MDA FULLVER DB OUTFILE RC -- run_journeys command...  -> the last exit code
  local name=$1 mda=$2 ver=$3 db=$4 outf=$5 rc=$6 k=0; shift 7
  while [ "$rc" = 75 ] && [ "$k" -lt "${UPG_RESUME_TRIES:-2}" ]; do
    k=$((k + 1))
    note "the $name app went down during the journeys: restart on the same database, run the rest again ($k of ${UPG_RESUME_TRIES:-2})"
    app_down "$name"
    app_up "$name" "$mda" "$ver" "$db" || { note "the $name app did not start again: the journeys stay unfinished (INVALID)"; break; }
    [ "$k" != 1 ] || cp "$outf" "${outf%.out}.run0.out"
    rc=0; xo "${outf%.out}.resume$k.out" "$@" --resume || rc=$?
    cp "${outf%.out}.resume$k.out" "$outf"   # the last run judges the merged summary: the main file is the whole report
  done
  return "$rc"
}
# journeys: impact-picked set on the old app (before-picked) and the new app (after, --compare). Scripts: gen_journeys.py, run_journeys.py
step_journeys() {
  local roles rc=0 db create=() old
  old=$(mda_old)
  roles=""; [ "$DRY" = 1 ] || roles=$(roles_of_plan "$WORK/plan-new.json")
  [ "$DRY" = 1 ] && roles="Role1,Role2"
  # PR-F36: a rerun writes journeys-*.out and e2e-*/ in place; keep the previous run's evidence first (pipe-30 -> 31)
  [ "$DRY" = 1 ] || must bash "$B/archive_journeys.sh" "$WORK"
  [ "$DRY" = 1 ] || rm -rf "$WORK/heal.json" "$WORK/heal-plan.json" "$WORK/heal-done.json" "$WORK/heal" "$WORK/e2e-heal-old" "$WORK/e2e-heal-new"   # a fresh run: nothing was healed yet
  [ -f "$WORK/users.json" ] || [ "$DRY" = 1 ] || write_users "$roles" "$WORK/users.json"
  [ ! -f "$WORK/create-spec.json" ] || create=(--create "$WORK/create-spec.json")
  # F22 (Purchase Request 10.24, real run): without the action inventory every journeys run was coverage INVALID
  # ("no actions.json") and the journeys covered the impact set only. The denominator is the OLD model's actions
  local act=() SC=()
  if [ "$DRY" != 1 ]; then
    # PR-F26: an actions.json older than action_inventory.py is written again (a rerun from journeys on a fixed toolkit
    # kept the old one: navigation list hops without their item)
    [ -s "$WORK/actions.json" ] && [ "$WORK/actions.json" -nt "$B/action_inventory.py" ] \
      || must python3 "$B/action_inventory.py" "$WORK/original.mpr" --out "$WORK/actions.json"
    act=(--actions "$WORK/actions.json")
    scope_run
  fi
  local si=()   # UPG_STANDIN=1: the whole journeys run on the stand-in APIs (apimock.py), on the old and the new app alike, with the journeys it makes possible
  if [ -n "${UPG_STANDIN:-}" ] && [ "$DRY" != 1 ]; then si=(--standin); heal_standin_start; fi
  must python3 "$B/gen_journeys.py" "$WORK/impact.json" ${act[@]+"${act[@]}"} --out-dir "$WORK/journeys" --roles-with-users "$roles" --users "$WORK/users.json" --data-rung "${create[@]}" ${si[@]+"${si[@]}"} ${SC[@]+"${SC[@]}"}
  [ ! -d "$WORK/hand-journeys" ] || cp -R "$WORK/hand-journeys/." "$WORK/journeys/journeys/"   # hand-written journeys join the impact set too
  # PR-F25: confirmed user processes (process_journeys.py) were never compiled by the pipeline, so a hand-confirmed
  # "submit a purchase request" never ran. Exit 3 is either a process INVALID (stops below) or no confirmed process
  if [ -f "$WORK/processes.md" ] && [ "${#act[@]}" -gt 0 ]; then
    rc=0; xo "$WORK/processes.out" python3 "$B/process_journeys.py" "$WORK/processes.md" --actions "$WORK/actions.json" --out-dir "$WORK/journeys" --users "$WORK/users.json" || rc=$?
    [ "$rc" = 0 ] || [ "$rc" = 3 ] || die4 "process_journeys exit $rc: $WORK/processes.out"
    # PR-F34: an INVALID confirmed process compiles to no legs at all, so the journeys ran for hours without it
    # (pipe-29). Stop before the apps start: the fix is a line in processes.md
    if grep -q '^INVALID' "$WORK/processes.out"; then
      nj_meta agent; nj_file 11 "A confirmed process is INVALID: fix processes.md (or set the process to status: dropped), then rerun --from journeys" "$WORK/processes.out" 20 '^INVALID'
      nj_park
    fi
  fi
  fixtures_start
  db=$(fresh_name "${X}_smoke_jold"); copy_db "$X_FROZEN" "$db"; fixture_db "$db"
  app_up oldjp "$old" "$SOURCE" "$db" || die4 "old app did not start for before-picked (log: $LOG)"
  # PR-F32: each smoke user is its role's only holder, so a workflow that targets "all users with role X" picks it
  must python3 "$B/smoke_users.py" "$db" --roles "$roles" --sole-target --apply
  fixture_users_db "$db"
  local jb=(python3 "$B/run_journeys.py" "$WORK/journeys" --label before-picked --port "$APP_PORT" --psql "$(psql_str "$db")"
    --admin-port "$ADMIN_PORT" --admin-pass "$M2EE_PASS" --users "$WORK/users.json" --login-path "$(login_path)" --work "$WORK/e2e-before-picked" --pause 50 ${act[@]+"${act[@]}"})
  rc=0; xo "$WORK/journeys-before-picked.out" "${jb[@]}" || rc=$?
  local r0=$rc; rc=0; journeys_resume oldjp "$old" "$SOURCE" "$db" "$WORK/journeys-before-picked.out" "$r0" -- "${jb[@]}" || rc=$?
  app_down oldjp
  mark_used "$db" journeys
  [ "$rc" = 0 ] || note "before-picked journeys on the old app exit $rc (baseline defects are listed apart): $WORK/journeys-before-picked.out"
  db=$(fresh_name "${X}_smoke_jnew"); copy_db "$X_FROZEN" "$db"; fixture_db "$db"
  app_up newjp "$(mda_new)" "$TARGET" "$db" || { nj_meta agent; nj_file 10 "New app did not start for the journeys" "$WORK/logs/runtime-newjp.log" 20 'ERROR|CRITICAL|Exception'; nj_flush; }
  # PR-F32: each smoke user is its role's only holder, so a workflow that targets "all users with role X" picks it
  must python3 "$B/smoke_users.py" "$db" --roles "$roles" --sole-target --apply
  fixture_users_db "$db"
  local sa=() ev=()
  [ ! -f "$WORK/shot-accept.txt" ] || sa=(--shot-accept "$WORK/shot-accept.txt")
  [ ! -f "$WORK/baseline-evidence.txt" ] || ev=(--baseline-evidence "$WORK/baseline-evidence.txt")   # BT-4: same file the gate reads
  # WM1 2026-11-17: a journey that failed on the old app and feeds no later one is listed SKIPPED, not walked again (UPG_JOURNEYS_ALL=1 walks all)
  [ "${UPG_JOURNEYS_ALL:-0}" = 1 ] || ev+=(--skip-baseline-fail)
  local ja=(python3 "$B/run_journeys.py" "$WORK/journeys" --label after --port "$APP_PORT" --psql "$(psql_str "$db")"
    --admin-port "$ADMIN_PORT" --admin-pass "$M2EE_PASS" --users "$WORK/users.json" --login-path "$(login_path)" --work "$WORK/e2e-after" --pause 50 ${act[@]+"${act[@]}"}
    --compare "$WORK/e2e-before-picked" ${sa[@]+"${sa[@]}"} ${ev[@]+"${ev[@]}"})
  rc=0; xo "$WORK/journeys-after.out" "${ja[@]}" || rc=$?
  local r0=$rc; rc=0; journeys_resume newjp "$(mda_new)" "$TARGET" "$db" "$WORK/journeys-after.out" "$r0" -- "${ja[@]}" || rc=$?
  app_down newjp
  mark_used "$db" journeys
  [ "${#si[@]}" = 0 ] || heal_standin_stop
  if [ "$rc" != 0 ] && heal_on; then
    # the heal step classifies every failing row next; the gate (diff step) still judges the journeys rung and stops on what is left
    note "journeys on the NEW app exit $rc: the heal step classifies the failing rows next (UPG_HEAL=0 stops here instead): $WORK/journeys-after.out"
  elif [ "$rc" != 0 ]; then
    local code=11
    # only SCREEN REVIEW lines and no FAIL/REGRESSION/INVALID journey: a comparison job (12), else a journey fix (11)
    if [ -f "$WORK/journeys-after.out" ] && grep -q 'SCREEN REVIEW' "$WORK/journeys-after.out" &&
       [ "$(grep -E 'REGRESSION|NOT IN BASELINE|INVALID|\bFAIL\b' "$WORK/journeys-after.out" | grep -vc 'SCREEN REVIEW' || true)" = 0 ]; then code=12; fi
    # a count, not `| grep -vq`: under pipefail an early-quitting grep -q made the first grep die of SIGPIPE, and `!` turned
    # that into "only SCREEN REVIEW lines" (stop 12) for a run that had FAIL lines
    nj_meta person "Journeys that passed on the old app fail or look different on the new one. What should we do?" "fix" "fix|Fix the app, then rerun the journeys|A REGRESSION or FAIL is a gate FAIL (steps/journeys.md)." "accept|Accept a changed screen, with a reason|Only for SCREEN REVIEW lines: write the reason in shot-accept.txt." "test|The journey is wrong: fix the journey|Only when it fails the same way on the old app."
    nj_file "$code" "Journeys on the NEW app (exit $rc): REGRESSION/FAIL is a gate FAIL, INVALID blocks DONE, SCREEN REVIEW needs both images opened and a reason in shot-accept.txt" "$WORK/journeys-after.out" 60 'REGRESSION|NOT IN BASELINE|INVALID|FAIL|SCREEN|todo|skipped|journeys:'
    nj_meta info; nj_add "$code" "Evidence" "summary: $WORK/e2e-after/after/summary.json ; plan: $WORK/journeys/plan.json ; screens: $WORK/e2e-after"
    nj_park
  fi
}

# heal: classify every failing row, heal what belongs to the TEST, rerun only the affected checks (max 2 rounds, stops when a round
# changes nothing). steps/heal.md. Scripts: heal.py, apimock.py, gen_journeys.py --standin, run_journeys.py --only, seed_pg.py.
# Policy: the app is never edited here; a row that may be a real defect of the upgrade stays open (heal.py nj, exit 12 from diff).
nats_on() { [ -n "${UPG_NATS:-}${UPG_HEAL_NATS:-}" ]; }   # UPG_NATS=1: the journeys and heal steps run with the test broker (steps/heal.md, test fixtures)
fixtures_start() { # the test broker (stand-in broker and auth) and the browser's trust for its certificate, before a journeys or heal run
  nats_on || return 0
  [ "$DRY" != 1 ] || return 0
  must env APP="$APP" UPG_NAME="${UPG_NAME:-mig}" python3 "$B/natsfixture.py" up --work "$WORK"
  export UPG_BROWSER_SPKI; UPG_BROWSER_SPKI=$(python3 "$B/natsfixture.py" spki --work "$WORK") || die4 "natsfixture.py spki failed"
}
fixture_db() { # fixture_db DB: the same test-setup rows in a database copy of the old and the new app (never in the frozen baseline)
  [ "$DRY" != 1 ] || return 0
  if nats_on; then must env UPG_NAME="${UPG_NAME:-mig}" python3 "$B/natsfixture.py" seed --work "$WORK" --psql "$(psql_str "$1")"; fi
  [ ! -f "$WORK/test-setup.sql" ] || must python3 "$B/setup_sql.py" --psql "$(psql_str "$1")" --file "$WORK/test-setup.sql"
}
heal_drop() { local d; for d in "$@"; do x docker exec "$PGC" dropdb -U mendix --if-exists "$d" || true; done; }   # the heal copies are ~20 MB each and never read again
heal_twin() { # the restart control (steps/baseline.md item 4, PV-7): a second start of the OLD app on a fresh copy of the frozen DB
  if [ -f "$WORK/twin-old.md" ] && [ "$WORK/twin-old.md" -nt "$WORK/before.json" ]; then return 0; fi
  local db rc=0 ep_args=()
  db=$(fresh_name "${X}_restart"); copy_db "$X_FROZEN" "$db"
  app_up oldtwin "$(mda_old)" "$SOURCE" "$db" || die4 "old app did not start for the restart control (log: $LOG)"
  [ ! -s "$WORK/endpoints.txt" ] || ep_args=(--endpoints "$WORK/endpoints.txt")
  x python3 "$B/snapshot.py" --label restart --ledger "$WORK/db-ledger.txt" --psql "$(psql_str "$db")" \
    --app-url "http://localhost:$APP_PORT" ${ep_args[@]+"${ep_args[@]}"} --log-cmd "docker logs ${UPG_NAME:-mig}-oldtwin" \
    --admin-url "http://localhost:$ADMIN_PORT" --admin-pass "$M2EE_PASS" --out "$WORK/restart.json" || rc=$?
  app_down oldtwin
  mark_used "$db" restart
  heal_drop "$db"
  [ "$rc" = 0 ] || die4 "snapshot restart failed (exit $rc), log: $LOG"
  xo "$WORK/twin-old.out" python3 "$B/diff.py" "$WORK/before.json" "$WORK/restart.json" --md "$WORK/twin-old.md" || true
}
fixture_users_db() { # fixture_users_db DB: rows that point at the test users (a stored sign-in token), applied right after smoke_users.py made them
  [ "$DRY" != 1 ] || return 0
  [ ! -f "$WORK/test-setup-users.sql" ] || must python3 "$B/setup_sql.py" --psql "$(psql_str "$1")" --file "$WORK/test-setup-users.sql"
}
heal_standin_start() { # the same stand-in for the old and the new app (apimock.py), reachable from the containers
  local cls=()
  [ ! -f "$WORK/apimock-classify.txt" ] || cls=(--classify "$WORK/apimock-classify.txt")
  [ ! -d "$WORK/apimock-recorded" ] || cls+=(--recorded "$WORK/apimock-recorded")   # recorded bodies for the stand-in (apimock.py header)
  x python3 "$B/apimock.py" stop --state "$WORK/apimock" || true
  must python3 "$B/apimock.py" serve "$WORK/original.mpr" "$MPR" --state "$WORK/apimock" --public-host host.docker.internal --background ${cls[@]+"${cls[@]}"}
  : > "$WORK/state/heal-standin"
}
heal_standin_stop() { rm -f "$WORK/state/heal-standin"; x python3 "$B/apimock.py" stop --state "$WORK/apimock" || true; }
heal_gen() { # the journeys again, with --standin: an action whose only todo is an external call gets a journey
  local roles act=() create=() rc=0 SC=()
  roles=$(roles_of_plan "$WORK/plan-new.json")
  [ ! -s "$WORK/actions.json" ] || { act=(--actions "$WORK/actions.json"); scope_run; }
  [ ! -f "$WORK/create-spec.json" ] || create=(--create "$WORK/create-spec.json")
  must python3 "$B/gen_journeys.py" "$WORK/impact.json" ${act[@]+"${act[@]}"} --out-dir "$WORK/journeys" --roles-with-users "$roles" --users "$WORK/users.json" --data-rung ${create[@]+"${create[@]}"} --standin ${SC[@]+"${SC[@]}"}
  [ ! -d "$WORK/hand-journeys" ] || cp -R "$WORK/hand-journeys/." "$WORK/journeys/journeys/"   # hand-written journeys join the impact set too
  if [ -f "$WORK/processes.md" ] && [ "${#act[@]}" -gt 0 ]; then
    xo "$WORK/processes.out" python3 "$B/process_journeys.py" "$WORK/processes.md" --actions "$WORK/actions.json" --out-dir "$WORK/journeys" --users "$WORK/users.json" || rc=$?
  fi
}
heal_run_journeys() { # heal_run_journeys IDS_CSV BASE_DB: those journeys on the old app, then the new app (--compare), then merge
  local ids=$1 base=$2 roles db rc=0 act=() sa=() ev=()
  roles=$(roles_of_plan "$WORK/plan-new.json")
  [ ! -s "$WORK/actions.json" ] || act=(--actions "$WORK/actions.json")
  [ ! -f "$WORK/shot-accept.txt" ] || sa=(--shot-accept "$WORK/shot-accept.txt")
  [ ! -f "$WORK/baseline-evidence.txt" ] || ev=(--baseline-evidence "$WORK/baseline-evidence.txt")
  rm -rf "$WORK/e2e-heal-old" "$WORK/e2e-heal-new"
  db=$(fresh_name "${X}_smoke_jheal_old"); copy_db "$base" "$db"; fixture_db "$db"
  app_up healold "$(mda_old)" "$SOURCE" "$db" || die4 "old app did not start for the heal rerun (log: $LOG)"
  must python3 "$B/smoke_users.py" "$db" --roles "$roles" --sole-target --apply
  fixture_users_db "$db"
  rc=0; xo "$WORK/heal-journeys-old.out" python3 "$B/run_journeys.py" "$WORK/journeys" --label before-picked --only "$ids" --port "$APP_PORT" --psql "$(psql_str "$db")" \
    --admin-port "$ADMIN_PORT" --admin-pass "$M2EE_PASS" --users "$WORK/users.json" --login-path "$(login_path)" --work "$WORK/e2e-heal-old" --pause 50 ${act[@]+"${act[@]}"} || rc=$?
  app_down healold; mark_used "$db" heal; heal_drop "$db"
  db=$(fresh_name "${X}_smoke_jheal_new"); copy_db "$base" "$db"; fixture_db "$db"
  app_up healnew "$(mda_new)" "$TARGET" "$db" || { nj_meta agent; nj_file 10 "New app did not start for the heal rerun" "$WORK/logs/runtime-healnew.log" 20 'ERROR|CRITICAL|Exception'; nj_flush; }
  must python3 "$B/smoke_users.py" "$db" --roles "$roles" --sole-target --apply
  fixture_users_db "$db"
  rc=0; xo "$WORK/heal-journeys-new.out" python3 "$B/run_journeys.py" "$WORK/journeys" --label after --only "$ids" --port "$APP_PORT" --psql "$(psql_str "$db")" \
    --admin-port "$ADMIN_PORT" --admin-pass "$M2EE_PASS" --users "$WORK/users.json" --login-path "$(login_path)" --work "$WORK/e2e-heal-new" --pause 50 ${act[@]+"${act[@]}"} \
    --compare "$WORK/e2e-heal-old" ${sa[@]+"${sa[@]}"} ${ev[@]+"${ev[@]}"} || rc=$?
  app_down healnew; mark_used "$db" heal; heal_drop "$db"
  must python3 "$B/heal.py" merge --work "$WORK" --old "$WORK/e2e-heal-old" --new "$WORK/e2e-heal-new"
}
heal_nats() { # UPG_HEAL_NATS=1: a local NATS broker (natsfixture.py) for the old and the new app, then the journeys that failed at the NATS dialog again (steps/heal.md)
  local plan ids names sdb e sn=()
  plan=$(python3 "$B/heal.py" nats-plan --work "$WORK") || die4 "heal.py nats-plan failed"
  ids=$(python3 -I -c 'import json,sys; print(",".join(json.loads(sys.argv[1])["rerun"]))' "$plan")
  names=$(python3 -I -c 'import json,sys; print(" ".join(json.loads(sys.argv[1])["seedname"]))' "$plan")
  [ -z "${UPG_HEAL_NATS_IDS:-}" ] || ids=$UPG_HEAL_NATS_IDS   # a probe: a few journey ids (comma list) instead of the plan; the seedname values stay (a probe on the plain base reports a test-data error dialog as a regression)
  [ -n "$ids" ] || { note "heal nats: no journey to run again"; return 0; }
  say "heal nats: $(printf '%s' "$ids" | tr ',' '\n' | grep -c .) journey(s) on a base with the broker's connection data"
  must env APP="$APP" UPG_NAME="${UPG_NAME:-mig}" python3 "$B/natsfixture.py" up --work "$WORK"
  export UPG_BROWSER_SPKI; UPG_BROWSER_SPKI=$(python3 "$B/natsfixture.py" spki --work "$WORK") || die4 "natsfixture.py spki failed"   # the test browser trusts the broker's certificate key only
  : > "$WORK/state/heal-nats"
  sdb=$(fresh_name "${X}_smoke_jnats"); copy_db "$X_FROZEN" "$sdb"
  must env UPG_NAME="${UPG_NAME:-mig}" python3 "$B/natsfixture.py" seed --work "$WORK" --psql "$(psql_str "$sdb")"
  if [ -n "$names" ]; then   # the seedname rows need their valid names on this base too (same values on both sides)
    for e in $names; do sn+=(--value "$e"); done
    [ ! -f "$WORK/seedname-set.txt" ] || sn+=(--set-file "$WORK/seedname-set.txt")
    must python3 "$B/seedname_fix.py" --psql "$(psql_str "$sdb")" "${sn[@]}"
  fi
  mark_used "$sdb" heal-seed
  heal_standin_start
  heal_run_journeys "$ids" "$sdb"
  heal_standin_stop
  heal_drop "$sdb"
  unset UPG_BROWSER_SPKI
  rm -f "$WORK/state/heal-nats"   # the broker keeps running until `natsfixture.py down`: a second round and the evidence need it
  must python3 "$B/heal.py" finalize --work "$WORK"
  say "$(python3 "$B/heal.py" summary --work "$WORK")"
}
heal_reshoot() { # UPG_HEAL_RESHOOT=1: the healed and likely-real rows again, so the compared runs hold their own screenshots (steps/heal.md)
  local plan ids snids snames sdb e sn=()
  plan=$(python3 "$B/heal.py" reshoot-plan --work "$WORK") || die4 "heal.py reshoot-plan failed"
  ids=$(python3 -I -c 'import json,sys; print(",".join(json.loads(sys.argv[1])["rerun"]))' "$plan")
  snids=$(python3 -I -c 'import json,sys; print(",".join(json.loads(sys.argv[1])["seedname_ids"]))' "$plan")
  snames=$(python3 -I -c 'import json,sys; print(" ".join(json.loads(sys.argv[1])["seedname"]))' "$plan")
  say "heal reshoot: $(printf '%s' "$ids" | tr ',' '\n' | grep -c .) journey(s) on the plain base, $(printf '%s' "$snids" | tr ',' '\n' | grep -c .) on the seedname base"
  heal_standin_start
  if [ -n "$ids" ]; then heal_run_journeys "$ids" "$X_FROZEN"; fi
  if [ -n "$snids" ]; then
    sdb=$(fresh_name "${X}_smoke_jseeded"); copy_db "$X_FROZEN" "$sdb"
    for e in $snames; do sn+=(--value "$e"); done
    [ ! -f "$WORK/seedname-set.txt" ] || sn+=(--set-file "$WORK/seedname-set.txt")
    must python3 "$B/seedname_fix.py" --psql "$(psql_str "$sdb")" "${sn[@]}"
    mark_used "$sdb" heal-seed
    heal_run_journeys "$snids" "$sdb"
    heal_drop "$sdb"
  fi
  heal_standin_stop
  must python3 "$B/heal.py" finalize --work "$WORK"
  say "$(python3 "$B/heal.py" summary --work "$WORK")"
}
step_heal() {
  heal_on || { note "heal is off (UPG_HEAL=0): failing rows go to the gate unclassified"; return 0; }
  if [ "$DRY" = 1 ]; then say "+ heal: restart control of the old app, heal.py plan (at most 2 rounds), apimock stand-in, reruns of the affected journeys, heal.py finalize"; return 0; fi
  if [ -n "${UPG_HEAL_RESHOOT:-}" ]; then fixtures_start; heal_reshoot; return 0; fi
  if [ -n "${UPG_HEAL_NATS:-}" ]; then heal_nats; return 0; fi
  fixtures_start
  local rnd n ids base seeds sdb al=() la=() e
  [ -f "$WORK/e2e-after/after/summary.pre-heal.json" ] || rm -f "$WORK/heal.json" "$WORK/heal-plan.json" "$WORK/heal-done.json"   # nothing merged yet: a fresh start
  must python3 "$B/heal.py" grids --model "$WORK/original.mpr" --out "$WORK/heal-grids.json"
  [ ! -f "$WORK/allow.txt" ] || al=(--allow "$WORK/allow.txt")
  [ ! -f "$WORK/log-allow.txt" ] || la=(--log-allow "$WORK/log-allow.txt")
  local jm=(); [ -f "$WORK/module-jumps.txt" ] && jm=(--module-jumps "$WORK/module-jumps.txt")
  xo "$WORK/heal-pre-diff.out" python3 "$B/diff.py" "$WORK/before.json" "$WORK/after.json" --md "$WORK/heal-pre-diff.md" ${al[@]+"${al[@]}"} ${la[@]+"${la[@]}"} ${jm[@]+"${jm[@]}"} || true
  heal_twin
  for rnd in 1 2; do
    xo "$WORK/heal-plan-$rnd.out" python3 "$B/heal.py" plan --work "$WORK" --round "$rnd" || die4 "heal.py plan failed (log: $WORK/heal-plan-$rnd.out)"
    n=$(sed -n 's/^CHANGED //p' "$WORK/heal-plan-$rnd.out"); n=${n:-0}
    ids=$(python3 -I -c 'import json,sys; print(",".join(json.load(open(sys.argv[1]))["rerun"]))' "$WORK/heal-plan.json")
    [ "$n" != 0 ] && [ -n "$ids" ] || { note "heal round $rnd changed nothing: stop"; break; }
    if [ -n "$(python3 -I -c 'import json,sys; print(",".join(json.load(open(sys.argv[1]))["standin"]))' "$WORK/heal-plan.json")" ]; then
      heal_standin_start; heal_gen
    fi
    must python3 "$B/heal.py" patch --work "$WORK"
    base="$X_FROZEN"
    seeds=$(python3 -I -c 'import json,sys; print(" ".join(json.load(open(sys.argv[1]))["seed"]))' "$WORK/heal-plan.json")
    snames=$(python3 -I -c 'import json,sys; print(" ".join(json.load(open(sys.argv[1])).get("seedname", [])))' "$WORK/heal-plan.json")
    if [ -n "$seeds$snames" ]; then   # the same rows go into the base of BOTH reruns (a seed on one side would be a difference of its own)
      sdb=$(fresh_name "${X}_smoke_jseeded"); copy_db "$X_FROZEN" "$sdb"
      if [ -n "$seeds" ]; then
        local so=(); for e in $seeds; do so+=(--per-entity-override "$e=3"); done
        must python3 "$B/seed_pg.py" --psql "$(psql_str "$sdb")" --per-entity 0 "${so[@]}"
      fi
      if [ -n "$snames" ]; then   # seeded junk used as an entity/member name: valid names, same on both sides (steps/heal.md, seedname)
        local sn=(); for e in $snames; do sn+=(--value "$e"); done
        [ ! -f "$WORK/seedname-set.txt" ] || sn+=(--set-file "$WORK/seedname-set.txt")
        must python3 "$B/seedname_fix.py" --psql "$(psql_str "$sdb")" "${sn[@]}"
      fi
      mark_used "$sdb" heal-seed; base="$sdb"
    fi
    heal_run_journeys "$ids" "$base"
    [ "$base" = "$X_FROZEN" ] || heal_drop "$base"
    heal_standin_stop
  done
  must python3 "$B/heal.py" finalize --work "$WORK"
  say "$(python3 "$B/heal.py" summary --work "$WORK")"
}

# diff: build log, identity, constants, data diff, start log, smoke screens, and the stored journeys results (PRC-8), all through gate.sh (smoke, release ran or run elsewhere)
# ---- apidirect: every consumed REST call tested directly, on the old and the new app (bin/apidirect.py, steps/apis.md) ----
# Why: the apis rung counted an outside endpoint as tested only when a browser journey happened to trigger it (16 of 170 in a
# field run). A throwaway COPY of the old and of the new app gets a test-only module (a wrapper microflow per REST-calling
# microflow, never committed); the runtime's client API runs each wrapper against the SAME stand-in, in three runs (ok, 500,
# malformed), and the requests sent and the results read are compared. UPG_APIDIRECT=0 turns the step off.
apidirect_on() { [ "${UPG_APIDIRECT:-1}" != 0 ] && [ -f "$WORK/original.mpr" ] && [ -f "$WORK/apimock/inventory.json" ]; }
apidirect_user() { # apidirect_user ROLE FIELD: the test user of a role from users.json
  python3 -I -c 'import json,sys; print(json.load(open(sys.argv[1])).get(sys.argv[2], {}).get(sys.argv[3], ""))' "$WORK/users.json" "$1" "$2" 2> /dev/null || true
}
apidirect_side() { # apidirect_side SIDE VER MDA: build the throwaway copy, run its wrappers, keep the results
  local side=$1 ver=$2 mda=$3 AD="$WORK/apidirect" db rc=0 role="${UPG_APIDIRECT_ROLE:-Administrator}" user pass base rec=()
  [ ! -f "$WORK/apidirect-recipes.json" ] || rec=(--recipes "$WORK/apidirect-recipes.json")   # inputs for calls whose inputs cannot be sampled (steps/apis.md)
  user=$(apidirect_user "$role" user); pass=$(apidirect_user "$role" pass)
  [ -n "$user" ] || { user="smoke_$(echo "$role" | tr 'A-Z ' 'a-z_')"; pass='Smoke-only-1!'; }
  xo "$AD/prepare-$side.out" python3 "$B/apidirect.py" prepare "$AD/calls-$side.json" --app "$AD/$side-src" --mxcli "${MXCLI:-$B/mxcli-container.sh}" --user-role "$role" ${rec[@]+"${rec[@]}"} || rc=$?
  [ "$rc" = 0 ] || { note "apidirect: the $side test module could not be prepared (exit $rc, $AD/prepare-$side.out)"; return 1; }
  rc=0; xo "$AD/build-$side.log" heavy "apid-build-$side" "$ver" mxbuild --target=package -o "$mda" "$AD/$side-src/$(basename "$MPR")" || rc=$?
  [ "$rc" = 0 ] || { note "apidirect: the $side test build failed (exit $rc, $AD/build-$side.log)"; return 1; }
  db=$(fresh_name "${X}_smoke_apid_$side"); copy_db "$X_FROZEN" "$db"; fixture_db "$db"
  app_up "apid$side" "$mda" "$ver" "$db" || { note "apidirect: the $side test app did not start"; heal_drop "$db"; return 1; }
  must python3 "$B/smoke_users.py" "$db" --roles "$role" --sole-target --apply
  fixture_users_db "$db"
  base=$(cat "$WORK/apimock/ready" 2> /dev/null | sed 's#//[^:/]*:#//localhost:#')
  rc=0; xo "$AD/drive-$side.out" python3 "$B/apidirect.py" drive "$AD/calls-$side.json" --side "$side" --app-url "http://localhost:$APP_PORT" \
    --standin "$base" --out "$AD/results-$side.jsonl" --user "$user" --password "$pass" --log-cmd "docker logs ${UPG_NAME:-mig}-apid$side" || rc=$?
  app_down "apid$side"; mark_used "$db" apidirect; heal_drop "$db"
  [ "$rc" = 0 ] || { note "apidirect: the $side run stopped (exit $rc, $AD/drive-$side.out)"; return 1; }
}
apidirect_run() {
  local AD="$WORK/apidirect" cls=() rev side rc=0
  mkdir -p "$AD"; rm -f "$AD"/results-*.jsonl "$AD"/direct.json "$AD"/direct.md
  [ ! -f "$WORK/apimock-classify.txt" ] || cls=(--classify "$WORK/apimock-classify.txt")
  [ ! -d "$WORK/apimock-recorded" ] || cls+=(--recorded "$WORK/apimock-recorded")
  must python3 "$B/apidirect.py" inventory "$WORK/original.mpr" --side old --out "$AD/calls-old.json" ${cls[@]+"${cls[@]}"}
  must python3 "$B/apidirect.py" inventory "$WORK/original.mpr" "$MPR" --side new --out "$AD/calls-new.json" ${cls[@]+"${cls[@]}"}
  rev=$(git_app log --format=%H --grep='^original$' | tail -1)
  [ -n "$rev" ] || { note "apidirect: no 'original' commit to take the old app from"; return 0; }
  for side in old new; do rm -rf "$AD/$side-src"; mkdir -p "$AD/$side-src"; done
  must bash -c "git -C '$APP' archive '$rev' | tar -x -C '$AD/old-src'"
  must rsync -a --exclude .git --exclude deployment --exclude theme-cache "$APP/" "$AD/new-src/"
  heal_standin_start
  rc=0
  apidirect_side old "$SOURCE" "$AD/ad-old.mda" || rc=1
  apidirect_side new "$TARGET" "$AD/ad-new.mda" || rc=1
  x python3 "$B/apidirect.py" split-log --state "$WORK/apimock" --out "$AD/standin/requests.jsonl"
  heal_standin_stop
  rm -rf "$AD/old-src" "$AD/new-src" "$AD"/ad-*.mda
  if [ "$rc" = 0 ]; then
    must python3 "$B/apidirect.py" compare --state "$AD"
  else
    note "apidirect: a side did not run: no direct results (the apis rung shows the journey evidence only)"
  fi
}
step_apidirect() {
  if [ "$DRY" = 1 ]; then say "+ apidirect.py inventory/prepare/drive/compare: every consumed REST call on a throwaway copy of the old and the new app"; return 0; fi
  apidirect_on || { note "apidirect is off (UPG_APIDIRECT=0, or no original.mpr / stand-in inventory)"; return 0; }
  apidirect_run
}
step_diff() {
  local rc=0 conf="$WORK/gate.conf" f k only="build,idcheck,const,data,logdiff,screens" bad
  local kv=("WORK=$WORK" "GATE_DIR=$WORK" "BUILD_LOG=$WORK/build-$TARGET.log" "OLD_MDA=$(mda_old)" "NEW_MDA=$(mda_new)")
  # GATE_DIR=$WORK: the evidence names stay as before and the screens rung finds $WORK/smoke-after-shots (afterwalk's)
  local allowf=allow.txt logallowf=log-allow.txt
  # the heal step's own lists (the person's file plus the rows the evidence accepted) replace the plain ones; they are
  # rebuilt here from the two sources, so a line written to allow.txt at a diff stop counts on `--from diff` without a heal rerun (TLT rung 2)
  local nm t
  for nm in allow log-allow; do
    [ -f "$WORK/$nm-effective.txt" ] || [ -f "$WORK/heal-$nm.txt" ] || continue
    : > "$WORK/$nm-effective.txt.new"
    for t in "$WORK/$nm.txt" "$WORK/heal-$nm.txt"; do
      [ ! -f "$t" ] || { cat "$t"; [ -z "$(tail -c1 "$t")" ] || echo; } >> "$WORK/$nm-effective.txt.new"
    done
    mv "$WORK/$nm-effective.txt.new" "$WORK/$nm-effective.txt"
  done
  [ ! -f "$WORK/allow-effective.txt" ] || allowf=allow-effective.txt
  local notesf=gate-notes.txt; [ ! -f "$WORK/gate-notes-effective.txt" ] || notesf=gate-notes-effective.txt   # the person's notes plus the heal's behaviour-change lines
  [ ! -f "$WORK/log-allow-effective.txt" ] || logallowf=log-allow-effective.txt
  # platform drops (System module) with no data in the baseline are approved by count, not by a person (WM1, FSM: 9->10
  # drops System.DataBrokerEntityMetadata; 0 rows); any other count stays open for a person
  local bdb; bdb=$(awk '$2 == "snapshot" && $3 == "before" { d = $1 } END { print d }' "$WORK/db-ledger.txt" 2> /dev/null || true)   # no ledger: awk exit 2 must not end the step under set -e
  if [ -n "$bdb" ] && [ -f "$(mda_old)" ] && [ -f "$(mda_new)" ]; then
    xo "$WORK/platform-drops.out" python3 "$B/platform_drops.py" "$(mda_old)" "$(mda_new)" --approved "$WORK/approved.txt" --psql "$(psql_str "$bdb")" || true
    [ "$DRY" = 1 ] || note "$(tail -1 "$WORK/platform-drops.out") (see $WORK/platform-drops.out)"
  fi
  for f in APPROVED=approved.txt CONST_OVERRIDES=env-values.json CONST_ALLOW=const-allow.txt ALLOW=$allowf LOG_ALLOW=$logallowf SMOKE_SHOT_ACCEPT=shot-accept.txt GATE_NOTES=$notesf HEAL_JSON=heal.json; do
    k=${f%%=*}; [ ! -f "$WORK/${f#*=}" ] || kv+=("$k=$WORK/${f#*=}")
  done
  # L55: the smoke rung judges the stored smoke results (no app); L56 is GATE_NOTES above
  if [ -f "$WORK/smoke-after.json" ] && [ -f "$WORK/smoke-before.json" ]; then
    kv+=("SMOKE_BEFORE=$WORK/smoke-before.json" "SMOKE_REJUDGE=1"); only="$only,smoke"
  fi
  # the apis rung: the stand-in's own check of what was requested (apimock.py check)
  if [ -f "$WORK/apimock/inventory.json" ]; then kv+=("APIMOCK=$WORK/apimock"); only="$only,apis"; fi
  [ ! -f "$WORK/apidirect/direct.json" ] || kv+=("APIDIRECT=$WORK/apidirect")
  kv+=("BEFORE_JSON=$WORK/before.json" "AFTER_JSON=$WORK/after.json" "OLD_LOG=$WORK/logs/runtime-oldbase.log" "NEW_LOG=$WORK/logs/runtime-newafter.log" "SMOKE_BEFORE_SHOTS=$WORK/smoke-before-shots" "SMOKE_LOGIN_PATH=$(login_path)")
  # PRC-8: the journeys stage ran just before; judge its stored results again (gate.sh JOURNEYS_REJUDGE: no app, nothing
  # written) so the gate's Progress line counts the rung instead of "journeys: not measured yet" (Purchase Request run 4)
  if [ -f "$WORK/e2e-after/after/summary.json" ] && [ -d "$WORK/journeys" ] && [ -d "$WORK/e2e-before-picked" ]; then
    kv+=("JOURNEYS_DIR=$WORK/journeys" "JOURNEYS_BEFORE=$WORK/e2e-before-picked" "JOURNEYS_REJUDGE=1")
    [ ! -s "$WORK/actions.json" ] || kv+=("ACTIONS=$WORK/actions.json")
    [ ! -f "$WORK/shot-accept.txt" ] || kv+=("JOURNEY_SHOT_ACCEPT=$WORK/shot-accept.txt")
    [ ! -f "$WORK/baseline-evidence.txt" ] || kv+=("JOURNEY_EVIDENCE=$WORK/baseline-evidence.txt")
    [ ! -f "$WORK/effect-accept.txt" ] || kv+=("JOURNEY_EFFECT_ACCEPT=$WORK/effect-accept.txt")   # the journeys rung's effect REVIEWs had no written-accept path
    only="$only,journeys"
  fi
  # PRC-4: the change ledger (gate.sh `Changes:` line) reads the app's git repo; the app is not always under $WORK/app
  # (Purchase Request run 4: the line never printed). Only a repo is named, like gate.sh's own $WORK/app default.
  [ ! -e "${APP:-/nonexistent}/.git" ] || kv+=("APP_REPO=$APP")
  if [ "$DRY" = 1 ]; then say "+ write $conf:"; printf '  %s\n' "${kv[@]}"; else printf '%s\n' "${kv[@]}" > "$conf"; fi
  local ga=(--config "$conf" --only "$only")
  [ "$DRY" != 1 ] || ga+=(--dry-run)
  xo "$WORK/gate.out" bash "$B/gate.sh" "${ga[@]}" || rc=$?
  [ "$DRY" != 1 ] || return 0
  # --only leaves smoke/journeys/release NOT RUN, which gate.sh counts as exit 2: judge the selected rungs' own rows
  bad=$(grep -E "^\| [0-9]+ \| (${only//,/|}) \| (FAIL|INVALID|NOT RUN) " "$WORK/gate-summary.md" 2> /dev/null || true)
  if [ "$rc" = 1 ] || [ -n "$bad" ] || { [ "$rc" != 0 ] && [ "$rc" != 2 ]; } || [ ! -f "$WORK/gate-summary.md" ]; then
    gate_open_nj_meta $(sed -n 's/.* \([0-9][0-9]*\) with REGRESSIONS to fix, \([0-9][0-9]*\) need a decision, \([0-9][0-9]*\) not measured yet.*/\1 \2 \3/p' "$WORK/gate-summary.md" 2> /dev/null | head -1); nj_file 12 "$GATE_OPEN_TITLE" "$WORK/gate-summary.md" 40 'FAIL|REVIEW|INVALID|NOT RUN'
  fi
  if [ -f "$WORK/heal.json" ]; then   # rows that may be a real defect of the upgrade stay open, with options and a recommendation
    python3 "$B/heal.py" finalize --work "$WORK" > /dev/null 2>&1 || true
    local hn; hn=$(python3 "$B/heal.py" nj --work "$WORK" 2> /dev/null || true)
    [ -z "$hn" ] || { nj_meta person "Some checks may be real defects of the upgrade; no automatic fix applies. What should we do?" "fix" "fix|Fix the app, then rerun|The old version passes it, so a person must see why the new one does not." "accept|Accept the change as intended, in writing|A reason per row (steps/heal.md)." "old|The old behaviour was wrong: say so in writing|A reason per row."; [ -z "$hn" ] || nj_add 12 "Heal: rows that may be real defects of the upgrade (no automatic fix)" "$hn"; }
  fi
  nj_park
}

# gate: release impact, kept modules, written verdict. Scripts: release_impact.py --check
step_gate() {
  local rc=0
  if [ -s "$WORK/plan.txt" ] && grep -qvE '^[[:space:]]*(#|$)' "$WORK/plan.txt" && [ ! -f "$WORK/module-jumps.txt" ] && [ "$DRY" != 1 ]; then
    nj_meta agent; nj_add 12 "Release impact INVALID: module rows missing" "plan.txt has updates but $WORK/module-jumps.txt does not exist, so release-impact.md has no module rows (steps/triage.md item 10). Write module-jumps.txt, rerun triage, then fill every row."
  fi
  xo "$WORK/release-impact.check" python3 "$B/release_impact.py" --check "$WORK/release-impact.md" || rc=$?
  [ "$rc" = 0 ] || { nj_meta agent; nj_file 12 "release_impact.py --check: open rows (exit $rc). Every row needs 'handled: <evidence>' or 'not relevant: <reason>' (INVALID until then)" "$WORK/release-impact.check" 30; }
  # NOT RUN items (mutant control, demo data replay) are never a pass: stop until a person ran them or wrote why not
  if [ "$DRY" != 1 ] && grep -q 'NOT RUN\|NOT replayed' "$WORK/state/notes.txt" 2> /dev/null && [ ! -f "$WORK/notrun-ack.txt" ]; then
    nj_meta info; nj_file 12 "Gate items NOT RUN by the pipeline (steps/baseline.md item 4: the mutant control must FAIL)" "$WORK/state/notes.txt" 20 'NOT RUN|NOT replayed'
    nj_meta person "Some final-check items were not run by the pipeline. What should we do?" "" "run|Run each item by hand|Record the result of each." "reason|Write why each does not apply|In notrun-ack.txt."; nj_add 12 "Decision" "Run each item by hand and record the result, or write the reason it does not apply, in $WORK/notrun-ack.txt; then rerun --from gate."
  fi
  nj_park
  # kept modules: complete except kept, unless a person acknowledged the list
  if [ "$DRY" != 1 ] && [ -s "$WORK/kept.txt" ] && [ ! -f "$WORK/kept-ack.txt" ]; then
    nj_meta info; nj_file 13 "upgrade complete except kept modules (never reported as upgraded)" "$WORK/kept.txt" 40
    nj_meta person "The upgrade is complete except the kept modules. What should we do?" "" "update|Update them by hand|steps/upgrade.md, playbooks/edited-modules.md." "ack|Acknowledge the list|Copy kept.txt to kept-ack.txt; the verdict then says complete except kept modules."; nj_add 13 "Decision" "Update them by hand (steps/upgrade.md, playbooks/edited-modules.md), or acknowledge the list: copy $WORK/kept.txt to $WORK/kept-ack.txt (then the verdict says 'complete except kept modules')."
    nj_park
  fi
  # held replays: the module is updated but its local edits are not back (replay_edits)
  if [ "$DRY" != 1 ] && [ -s "$WORK/replay-held.txt" ] && [ ! -f "$WORK/replay-held-ack.txt" ]; then
    nj_meta info; nj_file 13 "upgrade complete except held replays (the local edits of these modules are NOT in the app)" "$WORK/replay-held.txt" 40
    nj_meta person "The upgrade is complete except held replays: their local edits are NOT in the app. What should we do?" "" "fix|Fix the replay and rerun from upgrade|Its log is named per line." "ack|Acknowledge the loss in writing|Copy replay-held.txt to replay-held-ack.txt with a reason per line."; nj_add 13 "Decision" "Fix the replay (its log is named per line) and rerun --from upgrade, or acknowledge the loss in writing: copy $WORK/replay-held.txt to $WORK/replay-held-ack.txt with a reason per line."
    nj_park
  fi
  parked_any || write_summary   # auto: a parked item is never a PASS; park_finish asks them at the end
  record_runlog || true
}

write_summary() {
  [ "$DRY" != 1 ] || return 0
  {
    printf '# Pipeline result %s -> %s: gate PASS (fixed steps)\n\n' "$SOURCE" "$TARGET"
    printf 'No judgment stop remained. Evidence (all under %s):\n' "$WORK"
    printf -- '- build: check-*.log, build-%s.log, quick start log logs/runtime-new.log\n- gate: gate-summary.md (one row per rung)\n- identity: idcheck.md, idcheck-total.md\n- constants: constants.md\n- data: diff.md (before.json, after.json)\n- start log: logdiff.md\n- smoke walk: smoke-after.json, shotdiff-smoke.md\n- journeys: e2e-after/, journeys-after.out\n- release impact: release-impact.md (check clean)\n\n' "$TARGET"
    if [ -s "$WORK/kept.txt" ]; then printf 'upgrade complete except kept modules (acknowledged): see kept.txt\n\n'; fi
    if [ -s "$WORK/replay-held.txt" ]; then printf 'local edits NOT replayed (acknowledged): see replay-held-ack.txt\n\n'; fi
    case "$(python3 "$B/proposal.py" --status --work "$WORK" 2> /dev/null)" in
      signed|none) ;;
      *) printf 'proposal not signed: %s/PROPOSAL.md has no Signed-off line (unattended run); the verdict is not an owner-approved upgrade.\n\n' "$WORK" ;;
    esac
    printf 'Read impact.md before you sign the verdict (high constants read at startup, flows no longer called at startup).\n\n'
    printf '## Not run / notes (never read these as passed)\n'
    cat "$WORK/state/notes.txt" 2> /dev/null || true
  } > "$WORK/SUMMARY.md"
  say "PASS    gate $SOURCE -> $TARGET: $WORK/SUMMARY.md"
  record_grade
}

# report step (steps/report.md): print the completion grade and write the run row to the run-local $WORK/history-row.md (UPG_HISTORY
# chooses another file). Never the toolkit checkout: runs/HISTORY.md changes only through a toolkit PR. Information only: a failure
# here never changes the pipeline result.
record_grade() {
  [ -f "$WORK/gate-summary.md" ] || return 0
  local kept; kept=$(grep -cvE '^[[:space:]]*(#|$)' "$WORK/kept.txt" 2> /dev/null || true)
  python3 "$B/grade.py" "$WORK/gate-summary.md" --history "${UPG_HISTORY:-$WORK/history-row.md}" ${UPG_RUN_ID:+--run "$UPG_RUN_ID"} \
    --app "${UPG_APP_NAME:-unnamed app}" --path "$SOURCE > $TARGET" --kept "${kept:-0}" 2>&1 | sed 's/^/  /' || true
}

# run log (steps/report.md): append this run's row to FIELD-RUNS.md ($UPG_FIELD_RUNS, default the toolkit checkout) with
# bin/runlog.py. Never fails the run: the exit code and the gate verdict stay as they are. When runlog.py refuses (a run id
# already in the log, exit 3; a customer name, exit 4; no app code name, exit 2) the reason goes to the console, to the gate
# output (a `Run log:` line in gate-summary.md) and to NEEDS-JUDGMENT.md as an information section, and the run continues.
# App code name: app_code (UPG_APP_CODE, state/app-code, else a neutral app-<hex> from the .mpr name); type: UPG_APP_TYPE,
# else $WORK/state/app-type. UPG_RUN_ID sets the run id. The Time: line (step timing) is stamped into gate-summary.md first.
record_runlog() {
  RUNLOG_DONE=1
  [ -f "$WORK/gate-summary.md" ] || return 0
  local log="${UPG_FIELD_RUNS:-$TK/FIELD-RUNS.md}" out rc=0 app typ="${UPG_APP_TYPE:-}" why
  app=$(app_code)
  [ -n "$typ" ] || typ=$(head -n 1 "$WORK/state/app-type" 2> /dev/null || true)
  python3 -I "$B/runlog.py" --stamp-time --work "$WORK" > /dev/null 2>&1 || true
  out=$(python3 -I "$B/runlog.py" --work "$WORK" --log "$log" --require-app ${UPG_RUN_ID:+--run-id "$UPG_RUN_ID"} \
        ${app:+--app "$app"} ${typ:+--type "$typ"} 2>&1) || rc=$?
  if [ "$rc" = 0 ]; then
    echo "runlog: row added to $log. Commit FIELD-RUNS.md and CHANGES.md ($WORK/CHANGES.md) with explicit paths (git commit -- <paths>), then open a toolkit PR: the row is not in the toolkit until that PR is merged."
  else
    case "$rc" in
      3) why="the run id is already in the log (exit 3)" ;;
      4) why="the row holds a customer name (exit 4): set UPG_APP_CODE and UPG_APP_TYPE to code names" ;;
      2) why="runlog.py needs an app code name or a run id (exit 2): set UPG_APP_CODE (and UPG_APP_TYPE), or write it to $WORK/state/app-code" ;;
      *) why="" ;;
    esac
    why="${why:+$why: }$(printf '%s' "$out" | tr '\n' ' ' | cut -c1-300)"
    echo "WARN    runlog: no row added (runlog.py exit $rc): $why"
    if [ "$DRY" != 1 ]; then
      { printf '\nRun log: no row added to FIELD-RUNS.md (runlog.py exit %s). %s\n' "$rc" "$why"; } >> "$WORK/gate-summary.md" 2> /dev/null || true
      [ -f "$WORK/NEEDS-JUDGMENT.md" ] || printf '# NEEDS JUDGMENT: information only, the run result is unchanged\n\nwork: %s\n' "$WORK" >> "$WORK/NEEDS-JUDGMENT.md" 2> /dev/null || true
      {
        printf '\n## Run log not added (information; the exit code and the verdict are unchanged)\n\nFIELD-RUNS.md has no row for this run: %s\nFix the cause and run: python3 -I %s/runlog.py --work %s --app <CODE> --type <TEXT>\nThen commit FIELD-RUNS.md through a toolkit PR.\n' "$why" "$B" "$WORK"
      } >> "$WORK/NEEDS-JUDGMENT.md" 2> /dev/null || true
    fi
  fi
  return 0
}

# =====================================================================================================
# Driver
# =====================================================================================================
# One mxcli version per run (bin/mxcli_pin.sh has the why): triage records it in $WORK/state/mxcli-version, every later
# step that uses mxcli compares it and REFUSES (exit 3, on stderr) when the binary is another version. --from fetch|triage
# (or --only triage) re-records on purpose. A run that predates the pin records on its first checked step, and says so.
mxcli_pin() { # mxcli_pin STEP
  [ "$DRY" != 1 ] || return 0
  case "$1" in fetch|propose) return 0 ;; esac
  local sf="$WORK/state/mxcli-version" rc=0 reset=0
  if [ "$1" = triage ] && { [ "$FROM" = triage ] || [ "$FROM" = fetch ] || [ "$ONLY" = triage ]; }; then reset=1; fi
  if [ ! -s "$sf" ] || [ "$reset" = 1 ]; then
    if [ ! -s "$sf" ] && [ "$1" != triage ]; then
      say "WARN    mxcli version: no pin from triage (a run older than the pin); recording it now, the steps before $1 are unchecked"
    fi
    bash "$B/mxcli_pin.sh" record "$sf" || rc=$?
  else
    bash "$B/mxcli_pin.sh" check "$sf" || rc=$?
  fi
  [ "$rc" = 0 ] || { echo "upgrade-pipeline.sh: step '$1' not run: mxcli version pin (exit $rc)" >&2; exit 3; }
  return 0
}

run_step() { # run_step NAME
  STEP=$1; LOG="$WORK/logs/$STEP.log"
  decisions_apply
  if [ "$DRY" != 1 ] && [ -f "$WORK/state/$STEP.done" ] && [ "$ONLY" != "$STEP" ]; then
    printf '%-10s %s\n' "$STEP" "skipped (done $(cat "$WORK/state/$STEP.done"))"; return 0
  fi
  # GM-10: the app's git tree is checked at the start of every step after fetch (a worktree whose main clone was deleted mid-run)
  if [ "$STEP" != fetch ] && [ "$DRY" != 1 ] && [ -d "${APP:-}" ] && ! bash "$B/apptree.sh" "$APP"; then
    echo "upgrade-pipeline.sh: STOP before step '$STEP': the app's git tree is not usable (exit 3). Fix it, then rerun (finished steps are skipped)." >&2; exit 3
  fi
  mxcli_pin "$STEP"
  [ "$DRY" = 1 ] || { : > "$NJ_TMP"; rm -f "$WORK/parked/$STEP.md"; }   # a step that runs again parks afresh
  NJ_CODE=0
  case " convert update build after afterwalk journeys heal apidirect diff gate " in
    *" $STEP "*) if [ "$DRY" != 1 ] && [ -f "$WORK/PROPOSAL.md" ]; then proposal_recheck; fi ;;
  esac
  printf '%-10s %s\n' "$STEP" "running (log: $LOG)"
  # the journeys' progress line (bin/journeys_progress.py): into this step's log, a state file the page and the brief read, and the pace of earlier runs
  export UPG_PROGRESS_LOG="$LOG" UPG_PROGRESS_FILE="$WORK/state/journeys-progress.json" UPG_PACE_FILE="$WORK/state/journeys-pace.tsv"
  LOG_START=0; [ ! -f "$LOG" ] || LOG_START=$(wc -l < "$LOG" | tr -d ' ')   # a step log keeps earlier runs: nj_file quotes only this run
  timing_open "$STEP"
  cockpit_regen   # the page shows the step as running from its start, not only after it
  "step_$STEP"
  nj_flush
  timing_close 0 || true
  if [ "$DRY" != 1 ]; then date -u +%Y-%m-%dT%H:%M:%SZ > "$WORK/state/$STEP.done"; fi
  printf '%-10s %s\n' "$STEP" "done"
  cockpit_regen
}

# Cold WM1: a rung-1 rerun (the app rewound to the convert commit, --from update) kept rung2/state/{triage,baseline}.done,
# so rung 2 would compare 11 with a baseline of the rung-1 app the rerun had replaced. rung2/state/rung1-head is the app's
# HEAD when rung 2 last started on the $TARGET app. That commit no longer in the app's history, or the app back on $TARGET
# after rung 2 converted it, means rung 1 changed under rung 2: its markers (all but fetch) move to state/stale-<time>/.
rung2_stale() {
  local r2s="$WORK/rung2/state" mpr ver head old aside m n=0
  mpr=$(ls "$APP"/*.mpr 2> /dev/null | head -1); [ -n "$mpr" ] || return 0
  ver=$(python3 -c 'import sqlite3, sys; print(sqlite3.connect(sys.argv[1]).execute("select _ProductVersion from _MetaData").fetchone()[0])' "$mpr" 2> /dev/null) || ver=""
  case "$ver" in "$TARGET2"|"$TARGET2".*) return 0 ;; esac   # rung 2 converted the app: its markers are its own
  head=$(git -C "$APP" rev-parse HEAD 2> /dev/null) || return 0
  old=$(cat "$r2s/rung1-head" 2> /dev/null || true)
  if { [ -n "$old" ] && ! git -C "$APP" merge-base --is-ancestor "$old" HEAD 2> /dev/null; } || [ -f "$r2s/convert.done" ]; then
    aside="$r2s/stale-$(date -u +%Y%m%dT%H%M%SZ)"
    for m in "$r2s"/*.done; do
      [ -f "$m" ] && [ "$(basename "$m")" != fetch.done ] || continue
      mkdir -p "$aside"; mv "$m" "$aside/"; n=$((n + 1))
    done
    [ "$n" = 0 ] || say "rung 2   the $TARGET app changed under rung 2 (rung 1 reran on another history): $n step marker(s) moved to $aside, rung 2 redoes them"
  fi
  printf '%s\n' "$head" > "$r2s/rung1-head"
}

# --from STEP never runs a step before STEP (DV-9: --from propose re-ran basewalk). A step before it that is not done is
# optional (heal, apidirect: skipped, logged) or a step the later ones build on (refused, nothing changed).
from_guard() {
  [ -n "$FROM" ] && [ -z "$ONLY" ] || return 0
  local s miss=() opt=()
  for s in "${STEPS[@]}"; do
    [ "$s" != "$FROM" ] || break
    [ -f "$WORK/state/$s.done" ] || case "$s" in heal|apidirect) opt+=("$s") ;; *) miss+=("$s") ;; esac
  done
  if [ "${#miss[@]}" -gt 0 ]; then
    local them=it; [ "${#miss[@]}" = 1 ] || them=them
    echo "upgrade-pipeline.sh: --from $FROM refused: ${miss[*]} not done, and $FROM builds on $them. Nothing was changed." >&2
    echo "  To run from the first step not done: rerun without --from (done markers skip the finished steps)." >&2
    echo "  To run just $FROM: --only $FROM. After a container restart: bin/cloud/resume.sh <run folder>." >&2
    exit 2
  fi
  [ "${#opt[@]}" = 0 ] || echo "from      --from $FROM skips ${opt[*]} (not done, optional)"
}

main() {
  from_guard
  preflight
  resolve_app
  decisions_apply   # resume: what was decided on the page or in chat while the run was stopped (before the stop file goes: a stop's answer is in its options)
  [ "$DRY" = 1 ] || rm -f "$WORK/NEEDS-JUDGMENT.md"
  if [ -n "$FROM" ] && [ "$DRY" != 1 ]; then
    # cold WM1: --from update with another mxcli cleared the .done of update..gate, and only then the pin refused; check first
    local ps=$FROM; case "$ps" in fetch) ps=triage ;; propose) ps=convert ;; esac
    mxcli_pin "$ps"
    local s found=0
    # cold rfq: --from triage --only triage cleared baseline..gate though only triage ran; a later --from build then redid
    # baseline, basewalk, propose and convert (a convert over the update commits). With --only, nothing past it is cleared.
    for s in "${STEPS[@]}"; do
      [ "$s" != "$FROM" ] || found=1; [ "$found" = 0 ] || rm -f "$WORK/state/$s.done"
      [ -z "$ONLY" ] || [ "$s" != "$ONLY" ] || break
    done
  fi
  local s reached=0
  for s in "${STEPS[@]}"; do
    [ -z "$ONLY" ] || [ "$s" = "$ONLY" ] || continue
    # --from: every step before FROM stays as it is (from_guard has checked them); also under --dry-run
    [ "$s" != "$FROM" ] || reached=1
    [ -z "$FROM" ] || [ -n "$ONLY" ] || [ "$reached" = 1 ] || continue
    if [ "$s" != fetch ]; then resolve_app; fi
    run_step "$s"
  done
  [ -z "$ONLY" ] || { park_finish; brief_say || true; exit 0; }
  # rung 2 (steps/upgrade.md rule: 10.24 first, then 11): the same pipeline, new app of rung 1 is the old app of rung 2
  if [ -n "$TARGET2" ]; then
    say "rung 2   $TARGET -> $TARGET2 in $WORK/rung2"
    local r2=("$SELF" --app-dir "$APP" --source "$TARGET" --target "$TARGET2" --work "$WORK/rung2"
              --old-mda "$(mda_new)" --seed-from "$X_FROZEN" --db "${X}_r2")
    [ "$DRY" != 1 ] || r2+=(--dry-run)
    if [ "$DRY" != 1 ]; then
      mkdir -p "$WORK/rung2/state"
      rung2_stale
      # one version per run: rung 2 inherits the pin of rung 1 (its triage then checks, not re-records)
      [ ! -s "$WORK/state/mxcli-version" ] || [ -s "$WORK/rung2/state/mxcli-version" ] || cp "$WORK/state/mxcli-version" "$WORK/rung2/state/mxcli-version"
      # one step file for both versions: rung 2 appends to the steps.jsonl of rung 1
      touch "$WORK/steps.jsonl"; [ -e "$WORK/rung2/steps.jsonl" ] || ln -s ../steps.jsonl "$WORK/rung2/steps.jsonl"
      for s in env-values.json create-spec.json localedits.args interview-mode.txt; do
        [ ! -f "$WORK/$s" ] || [ -f "$WORK/rung2/$s" ] || cp "$WORK/$s" "$WORK/rung2/$s"
      done
      rung2_cids "$WORK/plan.txt" "$WORK/rung2/localedits.args"
    fi
    exec env "RUN=$RUN" "UPG_PHASE=$(echo "$TARGET2" | cut -d. -f1-3)" "UPG_COCKPIT_OUT=$WORK/COCKPIT.html" "${r2[@]}"
  fi
  park_finish
  brief_say || true   # the brief is information: it never changes a stop's exit code
  exit 0
}
main
