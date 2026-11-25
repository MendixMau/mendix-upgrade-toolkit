---
title: "Mx11: Entities with AutoNumber or calculated attributes can no longer be instantiated on offline navigation profiles"
topic: upgrade
keywords: ["AutoNumber offline", "calculated attributes offline", "offline navigation profile", "instantiate entity offline", "MX11-MODEL-OFFLINE-AUTONUMBER-RESTRICTED", "Mendix 11.7 breaking change", "offline nanoflow entity", "AutoNumber restriction", "offline page entity instantiation", "cannot instantiate AutoNumber"]
domain: [upgrade, architecture]
kind: pitfall
applies_to: mendix-general
versions: "11.7.0 and later"
layer: field
sources:
  - {title: "Studio Pro 11.7 release notes", url: "https://docs.mendix.com/releasenotes/studio-pro/11.7/", date: "2026-09-19"}
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed

---
**What changes:** Entities with AutoNumber or calculated attributes can no longer be instantiated on offline navigation profiles. Category: model semantics change. Severity in the catalog: high.

**Applies:** from Mendix 11.7.0 on. Affects: page, microflow.

**Status:** will break (catalog: certain).

**How to find it:** automatic, by a query over the app model; detection confidence medium.

**Fix:** Only relevant to offline-enabled pages/nanoflows. Find any entity with an AutoNumber or calculated attribute instantiated from an offline navigation profile and redesign around the restriction.

**Source quotes:**

- "We no longer allow you to instantiate entities with AutoNumber or calculated attributes in pages or nanoflows using offline-based navigation profiles" ([Studio Pro 11.7 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.7/))
