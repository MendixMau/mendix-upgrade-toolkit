#!/usr/bin/env bash
# datamove_control.sh CASE: bin/datamove.py check with a fake psql (base and after databases told apart by -d).
#   moved    every value in the target       lost     the target has fewer
#   fail     a count fails                   bad      a malformed plan line
set -euo pipefail
B=$(cd "$(dirname "$0")/../bin" && pwd)
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
cat > "$T/psql" <<'P'
#!/usr/bin/env bash
db=$2 q=${*: -1}
case "$db:$q" in
  base:*'"mendixsso$authrequest" where "nonce"'*) echo 5 ;;
  after:*'"mendixsso_ext$authrequestext" where "nonce"'*) echo "${AFTER_N:-5}" ;;
  *) echo 'ERROR: relation does not exist' >&2; exit 1 ;;
esac
P
chmod +x "$T/psql"
case "$1" in
  bad) echo 'MendixSSO.AuthRequest.Nonce to MendixSSO_Ext.AuthRequestExt.Nonce' > "$T/plan" ;;
  fail) echo 'MendixSSO.AuthRequest.Nonce -> Other.Gone.Col' > "$T/plan" ;;
  *) printf '# the SSO nonce moves to the extension module\nMendixSSO.AuthRequest.Nonce -> MendixSSO_Ext.AuthRequestExt.Nonce  # scenario D\n' > "$T/plan" ;;
esac
[ "$1" != lost ] || export AFTER_N=3
python3 "$B/datamove.py" check --plan "$T/plan" --before-psql "$T/psql -d base" --after-psql "$T/psql -d after"
