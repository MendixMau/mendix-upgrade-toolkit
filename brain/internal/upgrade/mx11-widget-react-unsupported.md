---
title: "Mx11: Built-in widget is not supported in the React client"
topic: upgrade
keywords: ["React client unsupported", "built-in widget not supported", "Data Grid React", "Template Grid Gallery", "Combo Box selector", "MX11-WIDGET-REACT-UNSUPPORTED", "widget compatibility React", "Image viewer Image widget", "Mendix 11 widgets"]
domain: [upgrade, ux-ui]
kind: pitfall
applies_to: mendix-general
versions: "11.0.0 and later"
layer: field
sources:
  - {title: "Mendix React Client", url: "https://docs.mendix.com/refguide/mendix-client/react/", date: "2026-09-15"}
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed

---
**What changes:** Built-in widget is not supported in the React client. Category: breaks only in the React client. Severity in the catalog: blocker.

**Applies:** from Mendix 11.0.0 on. Affects: widget.

**Status:** will break (catalog: certain).

**How to find it:** automatic, by a query over the app model; detection confidence high.

**Fix:** Replace each widget with its React equivalent: Data Grid with Data Grid 2, Template Grid with Gallery, the reference selectors and Drop-down with Combo Box, and the image viewers with the Image widget.

**False positives:** Matches built-in widget types exactly, so there is no pattern ambiguity: these types have no React implementation at all. It is a separate rule from MX11-WIDGET-DOJO-PACKAGE because built-in widgets never carry the .widget. package layout, which is why a Dojo-package scan alone misses them entirely.

**Source quotes:**

- "The data grid widget is not supported in the React client." ([Mendix React Client](https://docs.mendix.com/refguide/mendix-client/react/))
- "The template grid widget is not supported in the React client." ([Mendix React Client](https://docs.mendix.com/refguide/mendix-client/react/))

**Related catalog entries:** MX11-CLIENT-DOJO-DEPRECATED, MX11-WIDGET-DOJO-PACKAGE.
