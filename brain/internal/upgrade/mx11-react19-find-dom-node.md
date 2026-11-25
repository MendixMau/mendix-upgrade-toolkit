---
title: "Mx11: React 19 removed findDOMNode, breaking older widget builds"
topic: upgrade
keywords: ["findDOMNode removed", "React 19", "widget compatibility", "upgrade breaking change", "Mendix 11.6", "deprecated API", "widget version", "Studio Pro 11", "React deprecation", "marketplace widget update"]
domain: [upgrade, ux-ui]
kind: pitfall
applies_to: mendix-general
versions: "11.6.0 and later"
layer: field
sources:
  - {title: "Upgrading from Mendix Studio Pro 10 to 11", url: "https://docs.mendix.com/refguide/upgrading-from-10-to-11/", date: "2026-09-15"}
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed

---
**What changes:** React 19 removed findDOMNode, breaking older widget builds. Category: breaks with React 19 (Studio Pro 11.6+). Severity in the catalog: high.

**Applies:** from Mendix 11.6.0 on. Affects: project.

**Status:** may break, verify manually (catalog: not certain).

**How to find it:** automatic, by a query over the app model; detection confidence low.

**Fix:** Update every Marketplace and custom widget to a release built against React 19.

**Source quotes:**

- "the previously deprecated `findDOMNode` API is now removed" ([Upgrading from Mendix Studio Pro 10 to 11](https://docs.mendix.com/refguide/upgrading-from-10-to-11/))
- "Please upgrade all installed widgets to the latest published versions." ([Upgrading from Mendix Studio Pro 10 to 11](https://docs.mendix.com/refguide/upgrading-from-10-to-11/))

**Related catalog entries:** MX11-CLIENT-DOJO-DEPRECATED.
