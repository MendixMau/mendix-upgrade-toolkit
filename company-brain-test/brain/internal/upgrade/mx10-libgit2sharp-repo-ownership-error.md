---
title: "LibGit2Sharp 'repository path is not owned by current user' when opening in Mx10"
topic: upgrade
domain: [devops-cloud]
kind: pitfall
applies_to: mendix-general
versions: "Mx10 (Git)"
keywords: ["LibGit2Sharp", "repository path is not owned by current user", "Mx10 Git", "safe directory", ".gitconfig", "LibGit2SharpException", "Git upgrade", "project opening", "safe.directory"]
layer: field
sources:
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed
---
**Symptom**
- Opening the project in the new Mx10 fails with `LibGit2Sharp.LibGit2SharpException: repository path '…' is not owned by current user`.

**Root cause**
- Unknown. The source does not explain it.

**Fix**
- Add this to `.gitconfig`:
```
[safe]
    directory = *
```

**Status**
- Workaround. It was seen in one project during an Mx9→Mx10 upgrade investigation.
