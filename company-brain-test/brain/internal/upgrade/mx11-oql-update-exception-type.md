---
title: "Mx11: OQL UPDATE with a multi-row SET expression now throws a different exception"
topic: upgrade
keywords: ["OQL UPDATE exception", "CardinalityViolationException", "ConnectionBusException", "multi-row SET", "Mendix 11.5", "OQL multi-row", "error handling UPDATE", "exception type change", "SET expression exception", "upgrade Mendix 11"]
domain: [upgrade, data-modeling]
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
**What changes:** OQL UPDATE with a multi-row SET expression now throws a different exception. Category: behaviour change. Severity in the catalog: medium.

**Applies:** from Mendix 11.5.0 on. Affects: project.

**Status:** will break (catalog: certain).

**How to find it:** manual review (cannot be detected automatically); detection confidence medium.

**Fix:** Update any Java/nanoflow error handling that catches ConnectionBusException around an OQL UPDATE with a multi-row SET expression to also catch CardinalityViolationException.

**Source quotes:**

- "Studio Pro now throw a CardinalityViolationException instead of a generic ConnectionBusException" ([Studio Pro 11.5 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.5/))
