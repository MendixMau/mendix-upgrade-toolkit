---
title: Tracked node_modules and huge change sets crash Studio Pro version-control panels
topic: upgrade
domain: [devops-cloud, delivery-process]
kind: pitfall
applies_to: mendix-general
versions: "Git projects, seen on Mx10 and 11.9.1 after module upgrades"
keywords: ["NullReferenceException changes panel", "Collection was modified crash", "node_modules tracked git", "module upgrade crash", "huge changeset Studio Pro", "gitignore negation node_modules", "git rm cached node_modules", "Atlas Core upgrade", "NanoflowCommons upgrade", "version control performance", "unstaged changes crash", "700+ files changeset"]
layer: field
sources:
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed
---
**Symptom**
- Changes panel: `NullReferenceException`.
- Project Explorer: `Collection was modified` crash.
- Seen after a NanoflowCommons upgrade: 2,667 changes, including 485 unstaged `node_modules` deletions.
- Also after big Atlas Core upgrades, which delete old font and asset files.

**Root cause**
- `javascriptsource/<module>/actions/node_modules/` was tracked in Git. The module upgrade deleted it.
- Very large change sets overwhelm Studio Pro's file enumeration. The source's rule of thumb: above ~300 changes, typically 500+.
- A `.gitignore` negation `!/javascriptsource/**/node_modules/` re-tracked the files on every `git add -A`. The fix took 3 rounds before this was spotted.

**Fix**
1. Look for `!` negation lines in `.gitignore` and remove the one for node_modules.
2. Untrack: `git rm -r --cached "javascriptsource/<module>/actions/node_modules/"`.
3. Ignore `javascriptsource/**/node_modules/`.
4. Commit all pending changes in one batch.
5. After any big module upgrade (Atlas Core), commit immediately, before doing anything else in Studio Pro.

**Status**
- Confirmed in the field.
