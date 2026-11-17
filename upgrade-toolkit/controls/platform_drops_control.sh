#!/usr/bin/env bash
# platform_drops_control.sh: bin/platform_drops.py with fake idcheck rows and a fake psql (WM1 2026-11-17: System-module
# drops of Mendix 10 approved only on a count of 0;
# rerun 9: an editroute VENDOR approval re-counted, MendixSSO.AuthRequest.Nonce held 5 values). Prints the script's output and the approved file.
set -euo pipefail
B=$(cd "$(dirname "$0")/../bin" && pwd)
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
cat > "$T/rows" <<'R'
RED  REMOVED      entity      System.Gone  (column/table dropped; intended?)
RED  REMOVED      attribute   System.Kept.HasData  (column/table dropped; intended?)
RED  REMOVED      attribute   System.Broken.Col  (column/table dropped; intended?)
RED  REMOVED      attribute   Shop.Order.Note  (column/table dropped; intended?)
RED  REMOVED      entity      System.Already  (column/table dropped; intended?)
info REMOVED      attribute   System.Info.Col  (no data)
R
printf '%s\n' 'System.Already # a person: fine' \
  'MendixSSO.AuthRequest.Nonce # editroute VENDOR: the new MendixSSO drops it, nothing outside the module refers to it' \
  'Vend.Old # editroute VENDOR: the new Vend drops it, nothing outside the module refers to it' \
  'Vend.Odd.Col # editroute VENDOR: the new Vend drops it, nothing outside the module refers to it' > "$T/approved.txt"
cat > "$T/psql" <<'P'
#!/usr/bin/env bash
q=${*: -1}
case "$q" in
  *'"system$gone"'*) echo 0 ;;
  *'"system$kept"'*) echo 3 ;;
  *'"system$broken"'*|*'"vend$odd"'*) echo 'ERROR: relation does not exist' >&2; exit 1 ;;
  *'"mendixsso$authrequest" where "nonce"'*) echo 5 ;;
  *) echo 0 ;;
esac
P
chmod +x "$T/psql"
python3 "$B/platform_drops.py" old new --idcheck-out "$T/rows" --approved "$T/approved.txt" --psql "$T/psql -d basedb"
sed 's/^/approved: /' "$T/approved.txt"
