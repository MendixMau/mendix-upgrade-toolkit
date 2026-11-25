---
title: "Mx11: com.mendix.core.conf.RuntimeVersion class was removed"
topic: upgrade
keywords: ["RuntimeVersion removed", "com.mendix.core.conf.RuntimeVersion", "Core.getRuntimeVersion", "MX11-JAVA-RUNTIME-VERSION-CLASS-REMOVED", "deprecated class removal", "Mendix 11 upgrade", "Java runtime version", "getInstance"]
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
**What changes:** com.mendix.core.conf.RuntimeVersion class was removed. Category: removed in Mendix 11. Severity in the catalog: blocker.

**Applies:** from Mendix 11.0.0 on. Affects: java.

**Status:** will break (catalog: certain).

**How to find it:** automatic, by a pattern search over the app's code; detection confidence high.

**Fix:** Replace com.mendix.core.conf.RuntimeVersion.getInstance() with Core.getRuntimeVersion(). Distinct from MX11-JAVA-RUNTIME-VERSION-FORMAT, which is about that method's return-string format, not this class's removal -- do not merge the two.

**False positives:** Gated on the import line or the fully-qualified inline form, so a match proves the exact removed class is referenced, not just a similarly-named one. Verified against two real projects: communitycommons/Misc.java and a deeplink module's session handler both import and call this exact class -- confirmed with scan.py --audit before shipping.

**Source quotes:**

- "We removed the deprecated `com.mendix.core.conf.RuntimeVersion`" ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
