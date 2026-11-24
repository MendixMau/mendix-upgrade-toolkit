#!/bin/sh
# brain-index-check.sh DIR: DIR/INDEX.md links every other *.md of DIR exactly once and links nothing that is not a file there.
cd "$1" || exit 2
n=0
for f in *.md; do
  [ "$f" = INDEX.md ] && continue
  n=$((n + 1))
  c=$(grep -o "]($f)" INDEX.md | wc -l)
  [ "$c" = 1 ] || echo "$f listed $c times"
done
l=$(grep -o '](.*\.md)' INDEX.md | wc -l)
[ "$l" = "$n" ] || echo "INDEX links $l, notes $n"
for t in $(grep -o '](.*\.md)' INDEX.md | sed 's/^](//; s/)$//'); do [ -f "$t" ] || echo "$t: not a note"; done
echo "notes=$n links=same"
