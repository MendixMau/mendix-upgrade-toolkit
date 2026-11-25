---
title: "Mx11: Deprecated Core.*Async methods were removed"
topic: upgrade
keywords: ["Core.changeAsync", "Core.commitAsync", "Core.deleteAsync", "Core.instantiateAsync", "Core.rollbackAsync", "deprecated async methods removed", "ICore async methods", "MX11-JAVA-CORE-ASYNC-METHODS-REMOVED", "Mendix 11 breaking change", "async method replacement"]
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
**What changes:** Deprecated Core.*Async methods were removed. Category: removed in Mendix 11. Severity in the catalog: blocker.

**Applies:** from Mendix 11.0.0 on. Affects: java.

**Status:** will break (catalog: certain).

**How to find it:** automatic, by a pattern search over the app's code; detection confidence high.

**Fix:** Replace any of Core.changeAsync/commitAsync/deleteAsync/instantiateAsync/rollbackAsync (and their ICore# equivalents) with their synchronous counterparts or a scheduled action.

**False positives:** Five related overload removals from the same release notes section, grouped into one entry rather than five near-duplicate ones -- same convention already used by MX11-JAVA-IS-SUB-CLASS-OF for its own six overloads.

**Source quotes:**

- "We removed the deprecated `com.mendix.core.Core.changeAsync(IContext, IMendixObject, Map<String, String>)`" ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
- "We removed the deprecated `com.mendix.core.Core.commitAsync(IContext, List<IMendixObject>)`" ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
- "We removed the deprecated `com.mendix.core.Core.deleteAsync(IContext, IMendixObject, boolean)`" ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
- "We removed the deprecated `com.mendix.core.Core.instantiateAsync(IContext, String)`" ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
- "We removed the deprecated `com.mendix.core.Core.rollbackAsync(IContext, IMendixObject)`" ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
