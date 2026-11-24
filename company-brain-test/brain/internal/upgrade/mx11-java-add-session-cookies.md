---
title: "Mx11: ICore#addSessionCookies removed"
topic: upgrade
keywords: ["addSessionCookies removed", "ICore#addSessionCookies", "addMendixCookies", "Mendix 11 breaking change", "session cookies", "ICore API", "Core.addMendixCookies", "MX11-JAVA-ADD-SESSION-COOKIES", "removed API", "cookie handling"]
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
**What changes:** ICore#addSessionCookies removed. Category: removed in Mendix 11. Severity in the catalog: blocker.

**Applies:** from Mendix 11.0.0 on. Affects: java.

**Status:** will break (catalog: certain).

**How to find it:** automatic, by a pattern search over the app's code; detection confidence high.

**Fix:** Replace addSessionCookies calls with Core.addMendixCookies.

**Source quotes:**

- "Please use `ICore#addMendixCookies` instead." ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
