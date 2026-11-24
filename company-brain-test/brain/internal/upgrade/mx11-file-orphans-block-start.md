---
title: Mx11 refuses to start with unmigrated pre-5.12 file documents
topic: upgrade
domain: [data-modeling, devops-cloud]
kind: pitfall
applies_to: mendix-general
versions: "Mx10 -> Mx11.0+"
keywords: ["app won't start Mx11", "pre-5.12 file documents", "unmigrated FileDocuments", "upgrade to Mx11 fails", "FileDocument migration", "Mx11 startup blocked", "file orphans Mx5.12", "background migration Mx8.14", "legacy file migration", "Mx10 to Mx11 upgrade issue"]
layer: field
sources:
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed
---
**Symptom**
- The app does not start after upgrading to Mx11. Mx10 only warned about this.

**Root cause**
- Local file-system FileDocuments created before Mx5.12 are still unmigrated.
- Background migration runs on ≥ 8.14.0.
- Apps that are very old, never started, or long dormant may never have finished it.

**Fix**
- Before the Mx11 upgrade, check for pre-5.12 file orphans.
- Let them finish migrating on a supported 10.x version first.

**Status**
- Confirmed. This is a platform behavior.

**Release notes**
- 11.0.0: blocks app start if pre-5.12 file documents exist (https://docs.mendix.com/releasenotes/studio-pro/11.0/#1100-general-availability)
- 11.0.0: legacy Mx6 thumbnail migration removed; migrate on 10 first (https://docs.mendix.com/releasenotes/studio-pro/11.0/#1100-general-availability)
