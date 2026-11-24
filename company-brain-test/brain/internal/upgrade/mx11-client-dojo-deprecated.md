---
title: "Mx11: Dojo client is deprecated and will be removed in Mendix 12"
topic: upgrade
keywords: ["Dojo client deprecated", "Dojo Client removed", "Mendix 12 breaking change", "Switch to React client", "Dojo deprecation", "React client migration", "Mendix 11 Dojo", "client deprecation", "Dojo widgets", "custom widget React compatible"]
domain: [upgrade, ux-ui]
kind: pitfall
applies_to: mendix-general
versions: "11.0.0 and later"
layer: field
sources:
  - {title: "Studio Pro 11.0 release notes", url: "https://docs.mendix.com/releasenotes/studio-pro/11.0/", date: "2026-09-15"}
  - {title: "Upgrading from Mendix Studio Pro 10 to 11", url: "https://docs.mendix.com/refguide/upgrading-from-10-to-11/", date: "2026-09-15"}
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed

---
**What changes:** Dojo client is deprecated and will be removed in Mendix 12. Category: deprecation. Severity in the catalog: high.

**Applies:** from Mendix 11.0.0 on. Affects: project.

**Status:** will break (catalog: certain).

**How to find it:** automatic, from the project settings; detection confidence high.

**Fix:** Switch the app to the React client and confirm every custom widget has a React-compatible release.

**Source quotes:**

- "We deprecated the Dojo Client and it will be removed in Mendix 12. Please switch to the React Client." ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
- "[Dojo-based Mendix Client](https://docs.mendix.com/refguide/mendix-client/): deprecated in 11.0" ([Upgrading from Mendix Studio Pro 10 to 11](https://docs.mendix.com/refguide/upgrading-from-10-to-11/))

**Related catalog entries:** MX11-WIDGET-DOJO-PACKAGE, MX11-REACT19-FIND-DOM-NODE.
