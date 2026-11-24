---
title: "Mx11: Atlas 3 to Atlas 4 migration is optional but recommended"
topic: upgrade
keywords: ["Atlas 3 to Atlas 4", "Atlas migration", "Atlas 4 upgrade", "Mendix 11 Atlas", "optional migration", "Atlas module", "design system upgrade", "MX11-MODULE-ATLAS-4"]
domain: [upgrade]
kind: pitfall
applies_to: mendix-general
versions: "11.0.0 and later"
layer: field
sources:
  - {title: "Upgrading from Mendix Studio Pro 10 to 11", url: "https://docs.mendix.com/refguide/upgrading-from-10-to-11/", date: "2026-09-15"}
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed

---
**What changes:** Atlas 3 to Atlas 4 migration is optional but recommended. Category: deprecation. Severity in the catalog: low.

**Applies:** from Mendix 11.0.0 on. Affects: module.

**Status:** may break, verify manually (catalog: not certain).

**How to find it:** automatic, by a query over the app model; detection confidence medium.

**Fix:** Plan the Atlas 4 migration separately from the version upgrade; the app runs on Atlas 3 in Mendix 11.

**Source quotes:**

- "Upgrading from Atlas 3 to Atlas 4 in Mendix 11 is an optional process" ([Upgrading from Mendix Studio Pro 10 to 11](https://docs.mendix.com/refguide/upgrading-from-10-to-11/))
