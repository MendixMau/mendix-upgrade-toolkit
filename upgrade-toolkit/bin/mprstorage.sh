#!/bin/bash
# mprstorage.sh guard <app dir>: has the working tree changed the project's STORAGE FORMAT since HEAD? (GF-42)
#   exit 0  same format (or an MPR v1 project: nothing to lose)
#   exit 1  COLLAPSED: HEAD holds mprcontents/*.mxunit units (MPR v2) and the working tree holds none, or the single .mpr
#           grew from the small v2 index to a v1 file (10x and 5 MB or more); says so on stdout. The caller undoes the change.
#   exit 2  usage error / no .mpr
# mprstorage.sh sig <app dir>   prints "units=N mpr_bytes=S" of the working tree (for messages and controls)
# Why: `mx update-widgets` and `mx rename-design-properties` rewrite an MPR v2 (Git) project as a single-file v1 .mpr. In a
# field run (GF-42) a repair commit deleted all 4 098 mprcontents units and grew the .mpr from 549 KB to 158 MB; checkdiff
# compared error counts only (123 -> 2), so it was committed. The format is never something a repair or step may change.
# Producer: upgrade-pipeline.sh try_fix and commit_app (every repair, build and convert commit), stepupdate.sh before each
# step commit and remedy_apply.sh commit_all. All run it on the app's own git work tree.
cmd=${1:-}; app=${2:-}
[ -d "$app" ] || { echo "usage: mprstorage.sh guard|sig <app dir>" >&2; exit 2; }
mpr=$(ls "$app"/*.mpr 2> /dev/null | head -n 1); [ -n "$mpr" ] || { echo "mprstorage: no .mpr in $app" >&2; exit 2; }
name=$(basename "$mpr")
units_now=$(find "$app/mprcontents" -name '*.mxunit' 2> /dev/null | wc -l | tr -d ' ')
size_now=$(wc -c < "$mpr" | tr -d ' ')
case $cmd in
  sig) echo "units=$units_now mpr_bytes=$size_now";;
  guard)
    units_head=$(git -C "$app" ls-tree -r --name-only HEAD -- mprcontents 2> /dev/null | grep -c '\.mxunit$' || true)
    [ "${units_head:-0}" -gt 0 ] || exit 0
    size_head=$(git -C "$app" cat-file -s "HEAD:$name" 2> /dev/null || echo 0)
    if [ "$units_now" -eq 0 ]; then
      echo "STORAGE FORMAT CHANGED: $name was an MPR v2 project ($units_head mprcontents units) and is now a single-file MPR v1 (0 units, $size_now bytes); a repair tool rewrote it. Refused and undone. On MPR v2 use mxcli fix widgets / fix design-properties, never mx update-widgets / mx rename-design-properties (steps/repair.md row 5)."
      exit 1
    fi
    if [ "$size_head" -gt 0 ] && [ "$size_now" -gt $((size_head * 10)) ] && [ $((size_now - size_head)) -ge 5000000 ]; then
      echo "STORAGE FORMAT CHANGED: $name grew from $size_head to $size_now bytes beside $units_now mprcontents units: the v2 index became a v1 file. Refused and undone (steps/repair.md row 5)."
      exit 1
    fi
    exit 0;;
  *) echo "usage: mprstorage.sh guard|sig <app dir>" >&2; exit 2;;
esac
