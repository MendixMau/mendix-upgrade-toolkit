---
title: "Mx11: Multi-dimensional arrays from WSDL can no longer be selected in Import/Export Mapping"
topic: upgrade
keywords: ["WSDL multi-dimensional arrays", "Import Mapping", "Export Mapping", "Mendix 11 upgrade", "multi-dimensional array", "WSDL", "Import/Export Mapping", "consumed web services", "MX11-INTEGRATION-WSDL-MULTIDIM-ARRAY", "multidim array"]
domain: [upgrade, integration]
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
**What changes:** Multi-dimensional arrays from WSDL can no longer be selected in Import/Export Mapping. Category: removed in Mendix 11. Severity in the catalog: medium.

**Applies:** from Mendix 11.0.0 on. Affects: project.

**Status:** may break, verify manually (catalog: not certain).

**How to find it:** automatic, by a query over the app model; detection confidence low.

**Fix:** Only relevant to consumed web services whose WSDL exposes multi-dimensional arrays. Review Import/Export Mapping documents built against such a WSDL.

**Source quotes:**

- "We disallowed multi-dimensional array from WSDL to be selected in **Import Mapping** and **Export Mapping** documents" ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
