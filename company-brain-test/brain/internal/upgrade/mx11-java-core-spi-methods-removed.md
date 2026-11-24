---
title: "Mx11: Deprecated low-level Core SPI methods were removed"
topic: upgrade
keywords: ["Core SPI methods removed", "IContext clone", "IMendixObject clone", "ICoreAction methods", "IMendixIdentifier", "IMetaObject", "setExecutionId", "setExecutionThread", "SPI deprecated", "Mendix 11 breaking changes", "systemwideinterfaces.core"]
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
**What changes:** Deprecated low-level Core SPI methods were removed. Category: removed in Mendix 11. Severity in the catalog: medium.

**Applies:** from Mendix 11.0.0 on. Affects: java.

**Status:** will break (catalog: certain).

**How to find it:** manual review (cannot be detected automatically); detection confidence medium.

**Fix:** Almost never called by app-level Java actions -- mainly relevant to Mendix Runtime extensions and connectors. Check for direct calls to any of these IContext/IMendixObject/IMendixIdentifier/IMetaObject/ICoreAction methods.

**False positives:** Severity/confidence set lower than the other Java-removal entries in this batch: these are internal SPI-shaped methods almost exclusively used by extension and connector authors, not typical app Java actions, so a match is less certain to be load-bearing and less certain to be present at all. Twelve related removals grouped into one entry rather than twelve near-empty ones.

**Source quotes:**

- "We removed the deprecated `com.mendix.systemwideinterfaces.core.IContext#clone()` method" ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
- "We removed the deprecated `com.mendix.systemwideinterfaces.core.IMendixObject#clone()` method" ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
- "We removed the deprecated `com.mendix.systemwideinterfaces.core.IMendixObjectMember#setValue(IContext, T, boolean)` method" ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
- "We removed the deprecated `com.mendix.systemwideinterfaces.core.ICoreAction#setContext(IContext)` method" ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
- "We removed the deprecated `com.mendix.systemwideinterfaces.core.ICoreAction#getMetaInfo()` method" ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
- "We removed the deprecated `com.mendix.systemwideinterfaces.core.meta.IMetaObject#getId()` method" ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
- "We removed the deprecated `com.mendix.systemwideinterfaces.core.IMendixIdentifier#getEntityId()` method" ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
- "We removed the deprecated `com.mendix.systemwideinterfaces.core.IMendixIdentifier#clone()` method" ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
- "We removed the deprecated `com.mendix.systemwideinterfaces.core.IMendixIdentifier#setObject(IMendixObject)` method" ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
- "We removed the deprecated `com.mendix.systemwideinterfaces.core.IContext#setExecutionId(String)` method" ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
- "We removed the deprecated `com.mendix.systemwideinterfaces.core.IContext#setExecutionThread(Thread)` method" ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
- "We removed the deprecated `com.mendix.systemwideinterfaces.core.IContext#setExecutionType(ExecutionType)` method" ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
