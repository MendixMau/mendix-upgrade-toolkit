---
title: "Mx11: The IMxRuntime interface was removed"
topic: upgrade
keywords: ["IMxRuntime interface removed", "IMxRuntime", "com.mendix.m2ee.api.IMxRuntime", "Mendix 11 breaking change", "com.mendix.core.Core", "MX11-JAVA-IMXRUNTIME", "IMxRuntime dependency", "deprecated interface", "java runtime access", "core runtime access"]
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
**What changes:** The IMxRuntime interface was removed. Category: removed in Mendix 11. Severity in the catalog: blocker.

**Applies:** from Mendix 11.0.0 on. Affects: java.

**Status:** will break (catalog: certain).

**How to find it:** automatic, by a pattern search over the app's code; detection confidence high.

**Fix:** Drop the IMxRuntime dependency and reach the runtime through com.mendix.core.Core instead.

**False positives:** The pattern excludes IMxRuntimeRequest and IMxRuntimeResponse, which were not removed and are the overwhelming majority of matches for a naive IMxRuntime search.

**Source quotes:**

- "We removed the deprecated `com.mendix.m2ee.api.IMxRuntime` interface." ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
