---
title: "Mx11: Error message and exception-cause nesting depth changed"
topic: upgrade
keywords: ["exception nesting depth", "error message changed", "exception cause chain", "MX11-JAVA-EXCEPTION-NESTING-CHANGED", "Mendix 11.6", "exception handling", "getCause()", "nested exception", "exception walk", "Java exception", "error nesting", "cause chain depth"]
domain: [upgrade, architecture]
kind: pitfall
applies_to: mendix-general
versions: "11.6.0 and later"
layer: field
sources:
  - {title: "Studio Pro 11.6 release notes", url: "https://docs.mendix.com/releasenotes/studio-pro/11.6/", date: "2026-09-27"}
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed

---
**What changes:** Error message and exception-cause nesting depth changed. Category: behaviour change. Severity in the catalog: medium.

**Applies:** from Mendix 11.6.0 on. Affects: java.

**Status:** will break (catalog: certain).

**How to find it:** manual review (cannot be detected automatically); detection confidence low.

**Fix:** Review Java code that walks exception cause chains by a fixed depth or matches on nested error message text; the nesting shape changed.

**False positives:** Confidence low: this is a qualitative description ('less deep'), not a specific API signature -- there is no literal pattern to grep for, so detecting affected code requires manual review of exception-handling logic.

**Source quotes:**

- "error messages will be different. In addition, exception nesting will be less deep" ([Studio Pro 11.6 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.6/))
