---
title: "Mx11: Several other deprecated Java APIs were removed"
topic: upgrade
keywords: ["deprecated Java APIs removed", "CustomJavaAction removed", "UserBlockedException removed", "EnumConstant setImagePath removed", "Configuration checkConfig removed", "Mendix 11 breaking changes", "MX11-JAVA-MISC-DEPRECATED-API-REMOVED", "Java API migration", "Mendix 11 upgrade", "deprecated class removal", "Java compatibility", "Studio Pro 11.0"]
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
**What changes:** Several other deprecated Java APIs were removed. Category: removed in Mendix 11. Severity in the catalog: medium.

**Applies:** from Mendix 11.0.0 on. Affects: java.

**Status:** will break (catalog: certain).

**How to find it:** manual review (cannot be detected automatically); detection confidence high.

**Fix:** Unrelated small removals from the same release: CustomJavaAction, UserBlockedException, EnumConstant#setImagePath, and Configuration#checkConfig. Check for direct references to any of these.

**False positives:** A grab-bag of otherwise-unrelated single-method/class removals, grouped only because each is too small to warrant its own entry.

**Source quotes:**

- "We removed the deprecated `com.mendix.webui.CustomJavaAction` class" ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
- "We removed the deprecated `com.mendix.systemwideinterfaces.core.UserBlockedException` class" ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
- "We removed the deprecated `com.mendix.webui.reporting.EnumConstant#setImagePath(String)` method" ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
- "We removed the deprecated `com.mendix.core.conf.Configuration#checkConfig()` method" ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
