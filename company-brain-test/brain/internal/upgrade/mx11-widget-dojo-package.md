---
title: "Mx11: Widget uses the Dojo-era package layout"
topic: upgrade
keywords: ["Dojo widget", "Dojo package layout", "widget not supported", "React client migration", "MX11-WIDGET-DOJO-PACKAGE", "deprecated Dojo", "widget rebuild", "React widget replacement", "Mendix 11 upgrade", "Dojo era package", "widget Marketplace", "Dojo client removal"]
domain: [upgrade, ux-ui]
kind: pitfall
applies_to: mendix-general
versions: "11.0.0 and later"
layer: field
sources:
  - {title: "Studio Pro 11.0 release notes", url: "https://docs.mendix.com/releasenotes/studio-pro/11.0/", date: "2026-09-15"}
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed

---
**What changes:** Widget uses the Dojo-era package layout. Category: Dojo widget, not supported by the React client. Severity in the catalog: high.

**Applies:** from Mendix 11.0.0 on. Affects: widget.

**Status:** may break, verify manually (catalog: not certain).

**How to find it:** automatic, by a query over the app model; detection confidence medium.

**Fix:** Find a React release of the widget in the Marketplace, or rebuild it against the React client API.

**Source quotes:**

- "We deprecated the Dojo Client and it will be removed in Mendix 12. Please switch to the React Client." ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))

**Related catalog entries:** MX11-CLIENT-DOJO-DEPRECATED.
