---
title: "Mx11: Core.getRuntimeVersion no longer includes the build number"
topic: upgrade
keywords: ["Core.getRuntimeVersion", "getRuntimeVersion", "runtime version", "build number", "version format", "Mendix 11", "string parsing", "Java upgrade", "MX11-JAVA-RUNTIME-VERSION-FORMAT"]
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
**What changes:** Core.getRuntimeVersion no longer includes the build number. Category: behaviour change. Severity in the catalog: medium.

**Applies:** from Mendix 11.0.0 on. Affects: java.

**Status:** will break (catalog: certain).

**How to find it:** automatic, by a pattern search over the app's code; detection confidence medium.

**Fix:** Review any Java code that parses or compares the string from Core.getRuntimeVersion; a build-number component is no longer present.

**False positives:** getRuntimeVersion is still the supported API, so a bare call is not a defect and would carry no information -- only code that parses the returned string is affected. The rule fires only when the call is immediately chained into a string-parsing method (split/substring/charAt/indexOf/lastIndexOf/matches/replaceAll), deliberately missing a parse done later on a variable holding the value, since that shape cannot be told apart from an unrelated string reliably. Verified against a real project: a bare 'body.put("runtimeVersion", Core.getRuntimeVersion())' pass-through did not match, while 'Core.getRuntimeVersion().split("\\.")' -- the actual at-risk pattern -- did.

**Source quotes:**

- "The `com.mendix.core.Core.getRuntimeVersion` method now always returns the runtime version in the format of" ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
