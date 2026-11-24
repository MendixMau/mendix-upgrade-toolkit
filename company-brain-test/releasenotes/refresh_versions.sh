#!/usr/bin/env bash
# Refresh the brain's Studio Pro version table (brain/baseline/versions/) from the public docs.mendix.com release notes.
# Incremental: extract_sp.py only sends patch sections that are not yet in sp-changes.jsonl to the model.
#
#   DOCS=/path/to/docs-clone ./refresh_versions.sh
#
# DOCS is a clone (sparse is enough) of github.com/mendix/docs holding content/en/docs/releasenotes/studio-pro/{9,10,11}.
# PY is the python with the anthropic package (default python3). Needs ANTHROPIC_API_KEY.
# The Marketplace steps (fetch_marketplace.py, extract_modules.py) are not part of this script yet.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(dirname "$HERE")"
PY="${PY:-python3}"
DOCS="${DOCS:?set DOCS to a clone of github.com/mendix/docs}"
[ -d "$DOCS/content/en/docs/releasenotes/studio-pro" ] || { echo "DOCS=$DOCS has no content/en/docs/releasenotes/studio-pro" >&2; exit 2; }
: "${ANTHROPIC_API_KEY:?set ANTHROPIC_API_KEY (extract_sp.py calls the API)}"
cd "$HERE"
echo "== 1. Studio Pro release notes"
"$PY" extract_sp.py --docs "$DOCS"
echo "== 2. Tables"
"$PY" build_matrix.py
cp matrix/studio-pro-upgrade-*.md "$ROOT/brain/baseline/versions/"
echo "done: Studio Pro tables in brain/baseline/versions/ refreshed (SUMMARY.md and module tables: see README)"
