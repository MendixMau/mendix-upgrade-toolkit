---
title: "Mx11: Offline sync now rejects changes from entities with Online/Nothing/Never sync modes"
topic: upgrade
keywords: ["offline sync stricter", "Online Nothing Never sync", "sync mode rejected", "offline app sync", "entity sync configuration", "offline synchronization changes", "sync mode behavior change", "MX11-DATA-OFFLINE-SYNC-STRICTER", "11.10.0 breaking change", "offline client sync"]
domain: [upgrade, data-modeling]
kind: pitfall
applies_to: mendix-general
versions: "11.10.0 and later"
layer: field
sources:
  - {title: "Studio Pro 11.10 release notes", url: "https://docs.mendix.com/releasenotes/studio-pro/11.10/", date: "2026-09-19"}
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed

---
**What changes:** Offline sync now rejects changes from entities with Online/Nothing/Never sync modes. Category: behaviour change. Severity in the catalog: high.

**Applies:** from Mendix 11.10.0 on. Affects: entity.

**Status:** will break (catalog: certain).

**How to find it:** automatic, by a query over the app model; detection confidence medium.

**Fix:** Only relevant to offline apps. Review entities configured with Online/Nothing/Never sync modes that offline clients attempt to sync changes for.

**Source quotes:**

- "We introduced a stricter requirements check on the server synchronization APIs for offline apps" ([Studio Pro 11.10 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.10/))
