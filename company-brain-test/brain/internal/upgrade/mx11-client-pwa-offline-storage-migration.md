---
title: "Mx11: Offline PWA storage migrates from IndexedDB to OPFS on first load, delaying startup"
topic: upgrade
keywords: ["offline PWA", "IndexedDB", "OPFS", "storage migration", "startup delay", "first load", "upgrade Mx11", "offline storage", "PWA data migration", "app startup slow"]
domain: [upgrade, ux-ui]
kind: pitfall
applies_to: mendix-general
versions: "11.5.0 and later"
layer: field
sources:
  - {title: "Studio Pro 11.5 release notes", url: "https://docs.mendix.com/releasenotes/studio-pro/11.5/", date: "2026-09-19"}
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed

---
**What changes:** Offline PWA storage migrates from IndexedDB to OPFS on first load, delaying startup. Category: behaviour change. Severity in the catalog: medium.

**Applies:** from Mendix 11.5.0 on. Affects: project.

**Status:** will break (catalog: certain).

**How to find it:** automatic, by a query over the app model; detection confidence medium.

**Fix:** Only relevant to offline-first PWA apps. Warn users the first load/refresh after upgrading will be slower while local data migrates.

**Source quotes:**

- "The first time the offline PWA is opened or refreshed on this new Mendix version, it will trigger the migration of data from the IndexedDB storage" ([Studio Pro 11.5 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.5/))
