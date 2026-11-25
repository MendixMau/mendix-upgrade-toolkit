---
title: Mx9 renders pages before nested data views load and loads them sequentially
topic: upgrade
domain: [performance, ux-ui]
kind: pitfall
applies_to: mendix-general
versions: "Mx8 -> Mx9+"
keywords: ["nested data views", "page rendering delay", "empty data views", "Mx9 upgrade", "sequential loading", "loading order", "data view nested", "progressive rendering", "empty CSS pseudo-class", "nested data loading"]
layer: field
sources:
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed
---
**Symptom**
- After upgrading to Mx9, pages appear with empty nested data views that fill in one by one.

**Root cause**
- Mx8 waits for all data views on a page before rendering.
- Mx9 waits only for top-level data views. Nested data then loads sequentially.

**Fix**
- Target the `:empty` CSS pseudo-class on the affected widgets. Use it to show a message or loading animation while nested data loads.

**Status**
- Confirmed. It is a behavior change, not a bug.
- To reproduce, use nested data views with delayed data sources.
