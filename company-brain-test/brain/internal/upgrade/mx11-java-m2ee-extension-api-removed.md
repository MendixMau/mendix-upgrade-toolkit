---
title: "Mx11: Low-level m2ee runtime-extension API surface was removed"
topic: upgrade
keywords: ["m2ee-api removed", "m2ee runtime extension", "AdminAction interface removed", "AdminException interface removed", "IAppContainer interface removed", "InternalCoreAction getMetaInfo", "com.mendix.m2ee-api.jar", "MX11-JAVA-M2EE-EXTENSION-API-REMOVED", "runtime extension API", "Mendix 11 breaking change"]
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
**What changes:** Low-level m2ee runtime-extension API surface was removed. Category: removed in Mendix 11. Severity in the catalog: low.

**Applies:** from Mendix 11.0.0 on. Affects: java.

**Status:** will break (catalog: certain).

**How to find it:** automatic, by a pattern search over the app's code; detection confidence low.

**Fix:** Only relevant to code building directly against the m2ee-api.jar (custom Mendix Runtime extensions/tooling) -- not applicable to ordinary Mendix app Java actions.

**False positives:** Severity kept low: this API surface is for Mendix Runtime extension authors specifically, not app developers. Included for completeness of the audit rather than because most projects are likely to hit it.

**Source quotes:**

- "We removed the `com.mendix.m2ee-api.jar` artifact from the runtime bundles directory" ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
- "We removed most of the content of the deprecated `com.mendix.m2ee.api.AdminAction` interface" ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
- "We removed most of the content of the deprecated `com.mendix.m2ee.api.AdminException` interface" ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
- "We removed most of the content of the deprecated `com.mendix.m2ee.api.IAppContainer` interface" ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
- "We removed the method `com.mendix.core.actionmanagement.internal.InternalCoreAction#getMetaInfo()`" ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
