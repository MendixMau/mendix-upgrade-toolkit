---
title: "Mx11: The Deep Link module is deprecated and no longer actively supported"
topic: upgrade
keywords: ["Deep Link module deprecated", "Deep Link module", "deep link routing", "page URLs", "MX11-MODULE-DEEP-LINK-DEPRECATED", "upgrade to 11", "Mendix 11 breaking changes", "deprecated module", "deep link", "page navigation"]
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
**What changes:** The Deep Link module is deprecated and no longer actively supported. Category: deprecation. Severity in the catalog: medium.

**Applies:** from Mendix 11.0.0 on. Affects: module.

**Status:** will break (catalog: certain).

**How to find it:** automatic, by a query over the app model; detection confidence high.

**Fix:** Move deep-link routing onto page URLs, which cover the same use case natively.

**False positives:** Matches on module name, so an app module whose name merely contains DeepLink will also match. Confirm against the module's Marketplace origin before acting.

**Source quotes:**

- "The [Deep Link module] is deprecated, and no longer receives active support starting with Studio Pro 11." ([Upgrading from Mendix Studio Pro 10 to 11](https://docs.mendix.com/refguide/upgrading-from-10-to-11/))
