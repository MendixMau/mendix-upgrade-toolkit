---
title: "Mx11: Core.retrieveXPath Java APIs removed"
topic: upgrade
keywords: ["Core.retrieveXPath removed", "Core.retrieveXPath", "retrieveXPath deprecated", "Core.createXPathQuery", "XPath API", "Mendix 11 migration", "Java XPath retrieval", "XPath query fluent API", "MX11-JAVA-CORE-RETRIEVE-XPATH", "breaking change Mx11"]
domain: [upgrade, architecture]
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
**What changes:** Core.retrieveXPath Java APIs removed. Category: removed in Mendix 11. Severity in the catalog: blocker.

**Applies:** from Mendix 11.0.0 on. Affects: java.

**Status:** will break (catalog: certain).

**How to find it:** automatic, by a pattern search over the app's code; detection confidence high.

**Fix:** Rewrite the retrieval using the fluent Core.createXPathQuery API.

**Source quotes:**

- "We removed the deprecated Java APIs `Core.retrieveXPath...`." ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))

**Related catalog entries:** MX11-MODEL-XPATH-ASSOC-COMPARE.
