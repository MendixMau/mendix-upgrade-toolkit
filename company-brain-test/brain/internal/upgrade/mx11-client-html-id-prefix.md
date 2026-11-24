---
title: "Mx11: Generated HTML IDs lost their numeric part and gained l or p prefixes"
topic: upgrade
keywords: ["HTML ID format changed", "numeric part removed", "l prefix layout", "p prefix page", "generated element ID", "CSS selector broken", "ID locator broken", "JavaScript querySelector", "test automation locator", "Mx11 upgrade", "HTML ID prefix", "element ID selector"]
domain: [upgrade, ux-ui]
kind: pitfall
applies_to: mendix-general
versions: "11.2.0 and later"
layer: field
sources:
  - {title: "Studio Pro 11.2 release notes", url: "https://docs.mendix.com/releasenotes/studio-pro/11.2/", date: "2026-09-15"}
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed

---
**What changes:** Generated HTML IDs lost their numeric part and gained l or p prefixes. Category: behaviour change. Severity in the catalog: high.

**Applies:** from Mendix 11.2.0 on. Affects: js.

**Status:** will break (catalog: certain).

**How to find it:** manual review (cannot be detected automatically); detection confidence medium.

**Fix:** Rework any CSS selector, end-to-end test locator or JavaScript lookup that depends on the generated element id format.

**Source quotes:**

- "We removed the numeric part of IDs in the HTML and added `l` or `p` prefixes for layouts and pages." ([Studio Pro 11.2 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.2/))
