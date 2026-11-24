---
title: "Mx11: Apps still using the deprecated Reporting widgets will not start"
topic: upgrade
keywords: ["Reporting widgets deprecated", "Reporting widget removed", "app not starting", "non-startable app", "MX11-WIDGET-REPORTING-REMOVED", "Mendix 11.13", "widget deprecated since Mx 10", "remove Reporting widgets", "upgrade to 11.13"]
domain: [upgrade, ux-ui]
kind: pitfall
applies_to: mendix-general
versions: "11.13.0 and later"
layer: field
sources:
  - {title: "Studio Pro 11.13 release notes", url: "https://docs.mendix.com/releasenotes/studio-pro/11.13/", date: "2026-09-19"}
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed

---
**What changes:** Apps still using the deprecated Reporting widgets will not start. Category: removed in Mendix 11. Severity in the catalog: blocker.

**Applies:** from Mendix 11.13.0 on. Affects: widget.

**Status:** will break (catalog: certain).

**How to find it:** automatic, by a query over the app model; detection confidence high.

**Fix:** Remove any remaining Reporting widget usage before upgrading to 11.13+ -- the app will fail to start, not just show a finding.

**Source quotes:**

- "Reporting widgets (deprecated since Mx 10, resulted in a non-startable app)" ([Studio Pro 11.13 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.13/))
