---
title: "Mx11: String concatenation in expressions changed for empty and null values"
topic: upgrade
keywords: ["string concatenation", "null values", "empty values", "Mendix 11", "MX11-STRING-CONCAT-NULL", "expression behavior change", "string coercion", "null handling", "upgrade from 10 to 11", "empty check"]
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
**What changes:** String concatenation in expressions changed for empty and null values. Category: behaviour change. Severity in the catalog: high.

**Applies:** from Mendix 11.0.0 on. Affects: project.

**Status:** may break, verify manually (catalog: not certain).

**How to find it:** automatic, by a query over the app model; detection confidence low.

**Fix:** Review expressions that concatenate a possibly-empty value into a string and add an explicit empty check where the old coercion was relied on.

**Source quotes:**

- "String concatenation in expressions for empty/null values has changed." ([Upgrading from Mendix Studio Pro 10 to 11](https://docs.mendix.com/refguide/upgrading-from-10-to-11/))

**Related catalog entries:** MX11-STRING-EMPTY-CLIENT.
