#!/usr/bin/env bash
# platform_drops_control.sh: bin/platform_drops.py with fake idcheck rows and a fake psql (WM1 2026-11-17: System-module
# drops of Mendix 10 approved only on a count of 0). Prints the script's output and the approved file.
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
printf 'System.Already # a person: fine\n' > "$T/approved.txt"
cat > "$T/psql" <<'P'
#!/usr/bin/env bash
q=${*: -1}
case "$q" in
  *'"system$gone"'*) echo 0 ;;
  *'"system$kept"'*) echo 3 ;;
  *'"system$broken"'*) echo 'ERROR: relation does not exist' >&2; exit 1 ;;
  *) echo 0 ;;
esac
P
chmod +x "$T/psql"
python3 "$B/platform_drops.py" old new --idcheck-out "$T/rows" --approved "$T/approved.txt" --psql "$T/psql -d basedb"
sed 's/^/approved: /' "$T/approved.txt"
