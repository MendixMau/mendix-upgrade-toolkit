---
title: "Mx11: ORDER BY in a UNION OQL query must reference aliased columns only"
topic: upgrade
keywords: ["UNION ORDER BY", "aliased columns", "OQL query", "SELECT *", "Mendix 11", "ORDER BY alias", "UNION OQL", "column alias", "Mx11", "breaking change"]
domain: [upgrade, data-modeling]
kind: pitfall
applies_to: mendix-general
versions: "11.0.0 and later"
layer: field
sources:
  - {title: "Studio Pro 11.0 release notes", url: "https://docs.mendix.com/releasenotes/studio-pro/11.0/", date: "2026-09-15"}
  - {title: "Upgrading from Mendix Studio Pro 10 to 11", url: "https://docs.mendix.com/refguide/upgrading-from-10-to-11/", date: "2026-09-15"}
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed

---
**What changes:** ORDER BY in a UNION OQL query must reference aliased columns only. Category: behaviour change. Severity in the catalog: high.

**Applies:** from Mendix 11.0.0 on. Affects: project.

**Status:** may break, verify manually (catalog: not certain).

**How to find it:** automatic, by a query over the app model; detection confidence low.

**Fix:** Alias every column used in ORDER BY, and replace SELECT * in UNION queries with an explicit aliased column list.

**Source quotes:**

- "`ORDER BY` used in `UNION` OQL queries must now only refer to aliased columns." ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
- "SELECT \* in combination with UNION and ORDER BY is no longer allowed in runtime" ([Upgrading from Mendix Studio Pro 10 to 11](https://docs.mendix.com/refguide/upgrading-from-10-to-11/))
