---
title: "Mx11: Apps with unmigrated pre-5.12 local file documents are blocked from starting"
topic: upgrade
keywords: ["local file documents migration", "pre-5.12 file documents", "unmigrated file documents", "file-document storage migration", "app won't start", "MX11-DATA-LEGACY-FILE-DOCS-BLOCKED", "Mendix 11 blocking", "legacy file documents", "file system migration", "document storage blocked"]
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
**What changes:** Apps with unmigrated pre-5.12 local file documents are blocked from starting. Category: behaviour change. Severity in the catalog: high.

**Applies:** from Mendix 11.0.0 on. Affects: project.

**Status:** will break (catalog: certain).

**How to find it:** manual review (cannot be detected automatically); detection confidence high.

**Fix:** Only relevant to apps with a very long history (pre-Mendix-5.12) that never completed the file-document storage migration. Confirm the migration completed before upgrading, or the app will fail to start.

**Source quotes:**

- "We block the start of an app when there are still file documents on the local file system which are created before Mendix 5.12" ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
