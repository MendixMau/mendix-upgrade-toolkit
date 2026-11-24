---
title: "Mx11: Published REST services now always send JSON"
topic: upgrade
keywords: ["REST service JSON", "published REST XML", "REST response format", "Mendix 11 upgrade", "REST JSON only", "published web service", "REST API response", "JSON response", "XML response", "REST service consumer", "MX11-REST-PUBLISHED-JSON", "REST format change"]
domain: [upgrade, integration]
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
**What changes:** Published REST services now always send JSON. Category: behaviour change. Severity in the catalog: high.

**Applies:** from Mendix 11.0.0 on. Affects: project.

**Status:** may break, verify manually (catalog: not certain).

**How to find it:** automatic, by a query over the app model; detection confidence medium.

**Fix:** Check every consumer of a published REST service that relied on an XML response and switch it to JSON.

**Source quotes:**

- "This has been changed to always send JSON." ([Upgrading from Mendix Studio Pro 10 to 11](https://docs.mendix.com/refguide/upgrading-from-10-to-11/))
