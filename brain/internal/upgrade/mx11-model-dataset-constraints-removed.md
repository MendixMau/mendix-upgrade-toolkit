---
title: "Mx11: DataSetAccess and DataSet Object parameter constraints were removed"
topic: upgrade
keywords: ["DataSetAccess removed", "DataSet Object parameter constraint", "MX11-MODEL-DATASET-CONSTRAINTS-REMOVED", "parameter constraints removed", "Mendix 11.13", "DataSet constraints", "DataSetAccess UI", "Object parameter constraint", "breaking change dataset", "runtime constraints"]
domain: [upgrade, architecture]
kind: pitfall
applies_to: mendix-general
versions: "11.13.0 and later"
layer: field
sources:
  - {title: "Studio Pro 11.13 release notes", url: "https://docs.mendix.com/releasenotes/studio-pro/11.13/", date: "2026-09-19"}
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed

---
**What changes:** DataSetAccess and DataSet Object parameter constraints were removed. Category: removed in Mendix 11. Severity in the catalog: medium.

**Applies:** from Mendix 11.13.0 on. Affects: project.

**Status:** will break (catalog: certain).

**How to find it:** manual review (cannot be detected automatically); detection confidence low.

**Fix:** Configurations depending on DataSetAccess or DataSet Object parameter constraints were already non-functional at runtime before removal -- review any project still configuring them.

**False positives:** Confidence low: the release note itself says these rules were 'not respected by the runtime' even before removal, so the practical impact of the removal is unclear and likely small.

**Source quotes:**

- "DataSetAccess (UI was not working and the rules were not respected by the runtime)" ([Studio Pro 11.13 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.13/))
- "DataSet Object parameter constraint (also not respected by the runtime)" ([Studio Pro 11.13 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.13/))
