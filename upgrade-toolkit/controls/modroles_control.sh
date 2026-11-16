#!/usr/bin/env bash
# modroles_control.sh: bin/repair/modroles.py on a fake model (WM1 2026-11-17: Atlas_Core 4's new module roles unmapped,
# every page on an Atlas layout failed "for security reasons"). Prints the script's output; run-controls.sh greps it.
set -euo pipefail
B=$(cd "$(dirname "$0")/../bin" && pwd)
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
mkdir -p "$T/app"; : > "$T/app/App.mpr"; : > "$T/original.mpr"
git -C "$T/app" init -q; git -C "$T/app" -c user.name=c -c user.email=c@c commit -q --allow-empty -m "step: Atlas_Core 4.1.0 (stepupdate)"
git -C "$T/app" -c user.name=c -c user.email=c@c commit -q --allow-empty -m "step: Widgets 2.0.0 (stepupdate)"
cat > "$T/mxcli" <<'EOF'
#!/usr/bin/env bash
# fake: -p MPR -c QUERY
mpr=$2 q=$4
roles() { printf '| Qualified Name | Module | Role |\n|---|---|---|\n'; for r in "$@"; do printf '| %s | x | x |\n' "$r"; done; }
case "$q" in
  "show module roles")
    if [[ $mpr == *original.mpr ]]; then roles Administration.Administrator Administration.User Legacy.Viewer
    else roles Administration.Administrator Administration.User Legacy.Viewer Atlas_Core.Administrator Atlas_Core.User \
         Atlas_Core.Designer Widgets.Reader Other.User; fi ;;
  "show user roles") printf '| Name | Module Roles |\n|---|---|\n| Administrator | 2 |\n| User | 1 |\n| Anonymous | 1 |\n' ;;
  "describe user role Administrator") echo "  ModuleRoles: (Administration.Administrator, Administration.User)," ;;
  "describe user role User") echo "  ModuleRoles: (Administration.User)," ;;
  "describe user role Anonymous") echo "  ModuleRoles: (Administration.User)," ;;
  "describe app security") echo "Guest User Role: Anonymous" ;;
esac
EOF
chmod +x "$T/mxcli"
python3 "$B/repair/modroles.py" "$T/app/App.mpr" --original "$T/original.mpr" --mdl "$T/out.mdl" --mxcli "$T/mxcli"
[ ! -f "$T/out.mdl" ] || sed 's/^/mdl: /' "$T/out.mdl"
