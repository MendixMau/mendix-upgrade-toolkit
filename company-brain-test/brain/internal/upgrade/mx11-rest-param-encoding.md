---
title: "Mx11: Automatic encoding of Send REST request parameters was removed"
topic: upgrade
keywords: ["Send REST request parameters encoding", "REST parameter encoding removed", "urlEncode", "automatic encoding REST", "Mendix 11 upgrade", "REST request location parameters", "MX11-REST-PARAM-ENCODING", "encode parameter values REST", "breaking change REST", "Send REST microflow"]
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
**What changes:** Automatic encoding of Send REST request parameters was removed. Category: behaviour change. Severity in the catalog: high.

**Applies:** from Mendix 11.0.0 on. Affects: project.

**Status:** will break (catalog: certain).

**How to find it:** automatic, by a query over the app model; detection confidence medium.

**Fix:** Add explicit urlEncode calls around any parameter value interpolated into a Send REST request location.

**Source quotes:**

- "removed app setting 'Automatically encode parameter values in Send REST request microflow activities'" ([Upgrading from Mendix Studio Pro 10 to 11](https://docs.mendix.com/refguide/upgrading-from-10-to-11/))
- "If you require encoding for parameters, you must add that yourself." ([Upgrading from Mendix Studio Pro 10 to 11](https://docs.mendix.com/refguide/upgrading-from-10-to-11/))
