---
title: "Mx11: Element helper methods were removed from the Model API types"
topic: upgrade
keywords: ["Model API", "element helper methods", "add()", "get()", "getContainer()", "delete()", "Model SDK", "Mendix 11", "breaking change", "MX11-MODELAPI-ELEMENTS-HELPERS", "removed methods", "API migration"]
domain: [upgrade, architecture]
kind: pitfall
applies_to: mendix-general
versions: "11.12.0 and later"
layer: field
sources:
  - {title: "Studio Pro 11.12 release notes", url: "https://docs.mendix.com/releasenotes/studio-pro/11.12/", date: "2026-09-15"}
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed

---
**What changes:** Element helper methods were removed from the Model API types. Category: removed in Mendix 11. Severity in the catalog: medium.

**Applies:** from Mendix 11.12.0 on. Affects: project.

**Status:** will break (catalog: certain).

**How to find it:** manual review (cannot be detected automatically); detection confidence high.

**Fix:** Update Model SDK scripts to use the current Model API surface in place of the removed element helpers.

**Source quotes:**

- "We removed the elements helper methods (`add*()`, `get*()`, `getContainer()`, `delete()`) from the model api types" ([Studio Pro 11.12 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.12/))
