---
title: "Mx11: The CoreAction class was removed"
topic: upgrade
keywords: ["CoreAction removed", "CoreAction class", "com.mendix.core.actionmanagement.CoreAction", "UserAction replacement", "Mendix 11 breaking change", "CoreAction deprecated", "MX11-JAVA-COREACTION-REMOVED", "CoreAction migration", "actionmanagement removal", "Mx11 upgrade"]
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
**What changes:** The CoreAction class was removed. Category: removed in Mendix 11. Severity in the catalog: blocker.

**Applies:** from Mendix 11.0.0 on. Affects: java.

**Status:** will break (catalog: certain).

**How to find it:** automatic, by a pattern search over the app's code; detection confidence high.

**Fix:** Replace CoreAction with com.mendix.systemwideinterfaces.core.UserAction, per the release note's own suggested replacement.

**Source quotes:**

- "We removed the deprecated `com.mendix.core.actionmanagement.CoreAction` class" ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
