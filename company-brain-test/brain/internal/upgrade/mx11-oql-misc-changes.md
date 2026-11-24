---
title: "Mx11: OQL COALESCE result type and alias-dot rules changed"
topic: upgrade
keywords: ["OQL COALESCE", "type precedence", "numeric types", "OQL alias", "dot in alias", "Mendix 11", "breaking change", "alias-dot rules", "result type", "query behavior"]
domain: [upgrade, data-modeling]
kind: pitfall
applies_to: mendix-general
versions: "11.0.0 and later"
layer: field
sources:
  - {title: "Studio Pro 11.0 release notes", url: "https://docs.mendix.com/releasenotes/studio-pro/11.0/", date: "2026-09-19"}
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed

---
**What changes:** OQL COALESCE result type and alias-dot rules changed. Category: behaviour change. Severity in the catalog: medium.

**Applies:** from Mendix 11.0.0 on. Affects: project.

**Status:** may break, verify manually (catalog: not certain).

**How to find it:** automatic, by a query over the app model; detection confidence low.

**Fix:** Review OQL queries using COALESCE with mixed numeric argument types, and rename any OQL alias containing a dot.

**Source quotes:**

- "The result type of OQL function `COALESCE` is now defined using type precedence if all function arguments are of numeric type" ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
- "We no longer allow aliases in OQL to contain a dot (".") even if the OQL query is not a View Entity definition" ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))

**Related catalog entries:** MX11-OQL-UNION-ORDER-BY.
