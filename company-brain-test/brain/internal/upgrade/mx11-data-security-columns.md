---
title: "Mx11: DataStorage.OptimizeSecurityColumns now defaults to true"
topic: upgrade
keywords: ["DataStorage.OptimizeSecurityColumns", "OptimizeSecurityColumns", "defaults to true", "security columns", "entity access", "Mendix 11", "MX11-DATA-SECURITY-COLUMNS", "runtime setting", "breaking change", "data storage"]
domain: [upgrade, data-modeling]
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
**What changes:** DataStorage.OptimizeSecurityColumns now defaults to true. Category: behaviour change. Severity in the catalog: medium.

**Applies:** from Mendix 11.0.0 on. Affects: project.

**Status:** will break (catalog: certain).

**How to find it:** manual review (cannot be detected automatically); detection confidence high.

**Fix:** Retest queries that rely on columns being retrieved regardless of entity access, and set DataStorage.OptimizeSecurityColumns to false explicitly if the old behavior is required.

**Source quotes:**

- "The default value of the custom runtime setting **DataStorage.OptimizeSecurityColumns** was changed to true." ([Upgrading from Mendix Studio Pro 10 to 11](https://docs.mendix.com/refguide/upgrading-from-10-to-11/))
