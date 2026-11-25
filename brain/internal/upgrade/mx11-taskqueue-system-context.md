---
title: "Mx11: The Task Queue System context tasks setting was removed"
topic: upgrade
keywords: ["Task Queue System context", "System context tasks", "Task Queue setting removed", "App Settings Runtime", "MX11-TASKQUEUE-SYSTEM-CONTEXT", "Mendix 11 upgrade", "queued tasks context", "context tasks setting"]
domain: [upgrade, performance]
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
**What changes:** The Task Queue System context tasks setting was removed. Category: removed in Mendix 11. Severity in the catalog: medium.

**Applies:** from Mendix 11.0.0 on. Affects: project.

**Status:** may break, verify manually (catalog: not certain).

**How to find it:** automatic, by a query over the app model; detection confidence medium.

**Fix:** Confirm queued tasks still run under the context they need now that the System context tasks setting no longer exists.

**Source quotes:**

- "The Task Queue setting `System context tasks` (**Runtime** tab in App Settings) is removed." ([Upgrading from Mendix Studio Pro 10 to 11](https://docs.mendix.com/refguide/upgrading-from-10-to-11/))
