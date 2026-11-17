#!/usr/bin/env bash
# scss_boilerplate_control.sh CASE: bin/scss_boilerplate_check.py on a fake themesource module.
#   pass   only the two stock Mendix theme-folder imports (no app edit)
#   catch  the two stock imports plus one app-specific outward import (a real FILES-route edit)
set -euo pipefail
B=$(cd "$(dirname "$0")/../bin" && pwd)
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
mkdir -p "$T/mod/web"
case "$1" in
  catch)
    cat > "$T/mod/web/main.scss" <<'S'
@import "../../../theme/web/exclusion-variables";
@import "../../../theme/web/company-brand-overrides";
@import "../../../theme/web/custom-variables";
S
    ;;
  *)
    cat > "$T/mod/web/main.scss" <<'S'
@import "../../../theme/web/exclusion-variables";
@import "variables";
@import "../../../theme/web/custom-variables";
S
    ;;
esac
python3 "$B/scss_boilerplate_check.py" "$T/mod"
