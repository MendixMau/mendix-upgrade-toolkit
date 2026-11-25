---
title: "Mx11: UserAction#context() was removed"
topic: upgrade
keywords: ["UserAction context removed", "UserAction#context()", "ICoreAction getContext", "MX11-JAVA-USERACTION-CONTEXT-REMOVED", "Mendix 11 breaking change", "com.mendix.systemwideinterfaces.core.UserAction", "UserAction migration", "context() deprecated", "ICoreAction#getContext() replacement"]
domain: [upgrade, architecture]
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
**What changes:** UserAction#context() was removed. Category: removed in Mendix 11. Severity in the catalog: blocker.

**Applies:** from Mendix 11.0.0 on. Affects: java.

**Status:** will break (catalog: certain).

**How to find it:** automatic, by a pattern search over the app's code; detection confidence medium.

**Fix:** Replace UserAction#context() with ICoreAction#getContext(), per the release note's own suggested replacement.

**Source quotes:**

- "We removed the deprecated `com.mendix.systemwideinterfaces.core.UserAction#context()`" ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
