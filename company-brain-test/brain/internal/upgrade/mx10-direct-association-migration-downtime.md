---
title: Switching to direct association storage runs startup migrations and extends downtime
topic: upgrade
domain: [data-modeling, performance]
kind: pitfall
applies_to: mendix-general
versions: "Mx10+ (association storage option)"
keywords: ["direct associations", "association storage", "startup migration downtime", "store IDs on parent", "SQL joins", "association table migration", "long deployment downtime", "reusable module association change", "Mx10 new features", "batch migration"]
layer: field
sources:
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed
---
**Symptom**
- Deployment takes much longer than usual after association storage is changed to direct.

**Root cause**
- Mx10 can store child object IDs on the parent for some association types instead of a separate table.
- The data migration runs during startup, so the app is down while it runs.

**Fix**
- Migrate associations gradually in several batches, not in one big bang.
- For modules exported to other apps, tell their users clearly, so an unexpected long migration does not surprise them.
- Adopt this in a separate epic, not in the version upgrade itself.

**Status**
- Guidance from a Mx9 → Mx10 field guide. No measured downtime is given.
