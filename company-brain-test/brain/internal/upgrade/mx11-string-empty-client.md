---
title: "Mx11: Empty values are no longer converted to empty strings in the client"
topic: upgrade
keywords: ["Mx11 empty values strings client", "MX11-STRING-EMPTY-CLIENT", "empty string conversion behavior", "compare string empty", "string comparison expressions", "Runtime tab string behavior", "Mendix 11 upgrade pitfall", "empty values client behavior", "string empty conversion", "breaking change empty strings", "comparing '' empty"]
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
**What changes:** Empty values are no longer converted to empty strings in the client. Category: behaviour change. Severity in the catalog: high.

**Applies:** from Mendix 11.0.0 on. Affects: project.

**Status:** may break, verify manually (catalog: not certain).

**How to find it:** automatic, by a query over the app model; detection confidence medium.

**Fix:** Review expressions comparing strings to '' or empty before enabling the new string behavior in the Runtime tab.

**Source quotes:**

- "We no longer convert `empty` values sent to the client into empty strings." ([Upgrading from Mendix Studio Pro 10 to 11](https://docs.mendix.com/refguide/upgrading-from-10-to-11/))
- "Make sure to carefully analyze all expressions that are comparing strings against `''` or `empty`" ([Upgrading from Mendix Studio Pro 10 to 11](https://docs.mendix.com/refguide/upgrading-from-10-to-11/))
- "Projects migrating from Mendix 10 to 11 will retain the old String behavior unless you manually switch" ([Upgrading from Mendix Studio Pro 10 to 11](https://docs.mendix.com/refguide/upgrading-from-10-to-11/))
