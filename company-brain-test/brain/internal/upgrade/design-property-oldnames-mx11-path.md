---
title: Design property oldNames migration fails on direct 10.24 to 11.12 jump
topic: upgrade
domain: [ux-ui]
kind: pitfall
applies_to: mendix-general
versions: "10.24.x -> 11.12.x"
keywords: ["design property oldNames", "oldNames migration", "custom design property", "design property value not carried over", "10.24 to 11.12 upgrade", "design property rename", "upgrade jump", "migration path", "design system"]
layer: field
sources:
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed
---
**Symptom**
- A custom design property renamed with `oldNames` does not carry over the previously selected value on 11.12.x. It worked on 10.24.10.

**Root cause**
- Unclear. It appears to depend on the migration path.

**Fix**
- One customer avoided the error by going 10.24.15 → 11.6.6 → 11.12.0 instead of jumping straight to 11.12.0.

**Status**
- The underlying platform issue is marked fixed, but it still recurs in edge cases.
- Single field report.
