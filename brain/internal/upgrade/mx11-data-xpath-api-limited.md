---
title: "Mx11: The XPath API now uses limited XPath by default"
topic: upgrade
keywords: ["XPath API limited XPath", "limited XPath default", "XPath grammar", "Java XPath retrieval", "MX11-DATA-XPATH-API-LIMITED", "full XPath", "XPath construct", "limited XPath migration", "XPath API upgrade", "Mendix 11 XPath"]
domain: [upgrade, data-modeling]
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
**What changes:** The XPath API now uses limited XPath by default. Category: behaviour change. Severity in the catalog: high.

**Applies:** from Mendix 11.0.0 on. Affects: java.

**Status:** will break (catalog: certain).

**How to find it:** manual review (cannot be detected automatically); detection confidence medium.

**Fix:** Retest Java XPath retrievals that rely on constructs outside limited XPath, and opt back into the full grammar where the query needs it.

**False positives:** Which queries break depends on the XPath grammar each one uses, not on the presence of an API call, so a regex over Java sources would flag every retrieval regardless of whether it is affected.

**Source quotes:**

- "XPath API now uses limited XPath by default." ([Upgrading from Mendix Studio Pro 10 to 11](https://docs.mendix.com/refguide/upgrading-from-10-to-11/))

**Related catalog entries:** MX11-JAVA-CORE-RETRIEVE-XPATH.
