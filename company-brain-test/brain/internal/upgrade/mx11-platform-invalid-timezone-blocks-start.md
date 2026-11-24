---
title: "Mx11: An invalid time zone setting now blocks the runtime from starting"
topic: upgrade
keywords: ["invalid time zone", "time zone setting", "runtime startup blocks", "timezone configuration", "MX11-PLATFORM-INVALID-TIMEZONE", "Mendix 11.4", "startup failure", "invalid timezone blocks", "time zone validation", "runtime fails to start"]
domain: [upgrade, devops-cloud]
kind: pitfall
applies_to: mendix-general
versions: "11.4.0 and later"
layer: field
sources:
  - {title: "Studio Pro 11.4 release notes", url: "https://docs.mendix.com/releasenotes/studio-pro/11.4/", date: "2026-09-19"}
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed

---
**What changes:** An invalid time zone setting now blocks the runtime from starting. Category: behaviour change. Severity in the catalog: blocker.

**Applies:** from Mendix 11.4.0 on. Affects: project.

**Status:** will break (catalog: certain).

**How to find it:** manual review (cannot be detected automatically); detection confidence medium.

**Fix:** Verify the configured time zone setting in every environment is valid before upgrading; it previously only logged a critical message, and now blocks startup entirely.

**Source quotes:**

- "The Mendix runtime will no longer start if an invalid time zone is set" ([Studio Pro 11.4 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.4/))
