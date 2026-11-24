---
title: "Mx11: Client date formatting changed to support genitive and abbreviated month names"
topic: upgrade
keywords: ["date formatting", "genitive month names", "abbreviated month names", "client date format", "Mendix 11", "locale month names", "date format change", "month name support", "MX11-CLIENT-DATE-FORMAT-CHANGE", "date localization"]
domain: [upgrade, ux-ui]
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
**What changes:** Client date formatting changed to support genitive and abbreviated month names. Category: behaviour change. Severity in the catalog: low.

**Applies:** from Mendix 11.0.0 on. Affects: project.

**Status:** will break (catalog: certain).

**How to find it:** manual review (cannot be detected automatically); detection confidence medium.

**Fix:** Re-check date-heavy pages in locales using genitive or abbreviated month name forms after upgrading.

**Source quotes:**

- "We updated the date formatting in the client to be consistent with the runtime in supporting genitive and abbreviated month names" ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
