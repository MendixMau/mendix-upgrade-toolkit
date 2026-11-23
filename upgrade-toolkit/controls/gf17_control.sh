#!/usr/bin/env bash
# GF-17 / GF-21 helpers for run-controls.sh: the pipeline functions run on their own, from the pipeline script's text.
#   gf17_control.sh entity PIPELINE WORK [ENV_VALUE]   prints what smoke_entity_args answers
#   gf17_control.sh roles  PIPELINE PLAN IMPACT        prints what roles_all answers
#   gf17_control.sh cause  TOOLS_BIN LOGFILE [MARK]    prints run_journeys.login_cause for the engine's cap text, from the log lines after MARK (default 0)
set -u
fn() { awk -v n="$2" '$0 ~ "^"n"\\(\\) \\{"{p=1} p{print} p&&/^}/{exit}' "$1"; }
case "$1" in
  entity) eval "$(fn "$2" smoke_entity_args)"; WORK=$3; UPG_SMOKE_ENTITY=${4:-}; smoke_entity_args; echo "end" ;;
  roles)  eval "$(fn "$2" roles_all)"; roles_all "$3" "$4" ;;
  cause)  python3 - "$2" "$3" "${4:-0}" <<'PY'
import sys, types; sys.path.insert(0, sys.argv[1]); import run_journeys as r
d = "login faulted: x (measured cause on 2026-08-18: trial-licence concurrent-session cap). y"
t = r.runtime_log_since(types.SimpleNamespace(runtime_log=sys.argv[2]), int(sys.argv[3])) if sys.argv[2] != "none" else ""
print(r.login_cause(d, t))
PY
  ;;
esac
