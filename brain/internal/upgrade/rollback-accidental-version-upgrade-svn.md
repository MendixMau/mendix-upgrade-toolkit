---
title: Rolling back an accidental model version upgrade committed to SVN
topic: upgrade
domain: [delivery-process]
kind: procedure
applies_to: mendix-general
versions: "SVN only (example 7.23.4 opened in 8.0.0)"
keywords: ["accidental model upgrade", "version downgrade", "reverse merge SVN", "rescue branch", "rollback model version", "SVN version control", "model version mismatch", "Studio Pro version", ".mendix-cache", "trunk version restore", "TortoiseSVN delete", "Upload to version control"]
layer: field
sources:
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed
---
**Status:** Workaround. It is described for one example, where a 7.23.4 main line was opened in 8.0.0 and committed.

**When**
- The main line was opened in a newer version and committed.
- A reverse merge does not work, because Studio Pro refuses to reverse-merge to a lower version.

**Steps**
1. Update the main line locally and back up the folder.
2. In branch management, create a "rescue" branch from the last revision in the old version.
3. Delete everything in the main line folder except `.svn` and `.mendix-cache`.
4. Copy the rescue branch contents in, again excluding `.svn` and `.mendix-cache`.
5. Open the main line mpr. It should open in the old version.
6. In the TortoiseSVN repo-browser, select `trunk` and delete all items. This is a commit.
7. Delete `.svn` from the main line folder.
8. Studio Pro: Project > More Versioning > Upload to version control server, then pick your project.

**Checks**
- Trunk is on the old version.
- Full history is kept.

**Watch out**
- The sources contain no Git equivalent.
