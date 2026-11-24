# Version knowledge (release notes to structured change records)

Studio Pro patch-level change records for the upgrade topic: what changed per patch, with a source link on every row.
All input is public (docs.mendix.com release notes).

## Pipeline (Studio Pro)

| step | script | input | output |
|---|---|---|---|
| 1 | `extract_sp.py` | `content/en/docs/releasenotes/studio-pro/{9,10,11}/*.md` of a clone of github.com/mendix/docs (sparse and blobless is enough) | `sp-changes.jsonl` |
| 2 | `build_matrix.py` | `sp-changes.jsonl` (and `module-changes.jsonl` when present) | `matrix/*.md` reviewable tables |

Refresh: `DOCS=/path/to/docs-clone ./refresh_versions.sh` (needs the `anthropic` package and `ANTHROPIC_API_KEY`).
Step 1 is incremental: only patch sections whose version is not yet in `sp-changes.jsonl` are extracted; `--force` rebuilds.
Copy the resulting `matrix/studio-pro-upgrade-*.md` into `../brain/baseline/versions/` (the script does).

## Record shape

`version, release_date, lts, mts, change_type` (breaking, deprecation, removal, requirement, known-issue, fix, improvement,
feature, security), `upgrade_relevant, area, affected[], text, tickets[], fixed_in, source` (docs anchor), `model`.

## Provenance

Records with `"model": "claude-haiku-4-5-20251001"` came from `extract_sp.py`. Records with `"model": "session-agent"` (the
11 patches 9.24.45, 10.24.27 to 10.24.29, 11.6.12, 11.6.13, 11.12.6 to 11.12.8, 11.16.0, 11.16.1; 245 records) were written by
an AI agent session reading each bullet, following the `SYSTEM` prompt of `extract_sp.py`, because no API key was available.
Each comes from a real bullet with its real anchor. The change_type on Improvements and Fixes bullets is a judgment call;
Breaking, Deprecation and Known Issues types follow the section heading. Extraction is unreviewed.

## Not here yet

The Marketplace module tables (`fetch_marketplace.py`, `extract_modules.py`, `module-changes.jsonl`, the module matrix) are not
part of this change; the modules refresh follows in a second PR. Until then `build_matrix.py` run here produces empty module
tables; refresh only the Studio Pro tables from this folder.
