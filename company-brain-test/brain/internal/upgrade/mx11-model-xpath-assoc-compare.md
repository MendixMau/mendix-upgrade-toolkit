---
title: "Mx11: Comparing an association to empty or false() is now a consistency error"
topic: upgrade
keywords: ["association comparison empty", "association compare false", "consistency error", "XPATH association", "not(association)", "Mx11 upgrade", "association comparison error", "MX11-MODEL-XPATH-ASSOC-COMPARE", "empty comparison", "boolean association"]
domain: [upgrade, architecture]
kind: pitfall
applies_to: mendix-general
versions: "11.4.0 and later"
layer: field
sources:
  - {title: "Studio Pro 11.4 release notes", url: "https://docs.mendix.com/releasenotes/studio-pro/11.4/", date: "2026-09-15"}
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed

---
**What changes:** Comparing an association to empty or false() is now a consistency error. Category: model semantics change. Severity in the catalog: blocker.

**Applies:** from Mendix 11.4.0 on. Affects: xpath.

**Status:** will break (catalog: certain).

**How to find it:** automatic, by a query over the app model; detection confidence high.

**Fix:** Rewrite the constraint to test the association itself, for example [not(MyModule.MyAssociation)] instead of comparing it to empty or false().

**Source quotes:**

- "incorrectly allowed associations and associated objects to be compared to Boolean values or empty" ([Studio Pro 11.4 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.4/))
- "The following constructs will now lead to consistency errors:" ([Studio Pro 11.4 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.4/))
