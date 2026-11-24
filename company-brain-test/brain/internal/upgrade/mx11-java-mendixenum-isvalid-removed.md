---
title: "Mx11: MendixEnum#isValid(IContext, String) was removed"
topic: upgrade
keywords: ["MendixEnum isValid removed", "MendixEnum#isValid IContext String", "isValid deprecated Mendix 11", "Mendix 11 breaking change", "MX11-JAVA-MENDIXENUM-ISVALID-REMOVED", "isValid single argument overload", "enum validation method", "IContext parameter removed"]
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
**What changes:** MendixEnum#isValid(IContext, String) was removed. Category: removed in Mendix 11. Severity in the catalog: blocker.

**Applies:** from Mendix 11.0.0 on. Affects: java.

**Status:** will break (catalog: certain).

**How to find it:** automatic, by a pattern search over the app's code; detection confidence medium.

**Fix:** Replace MendixEnum#isValid(IContext, String) with the single-argument MendixEnum#isValid(String) overload, per the release note's own suggested replacement.

**False positives:** The removed overload takes two arguments (IContext, String); the still-supported one takes one, so the any_of pattern requires a comma inside the parens to tell them apart. Gated on MendixEnum being imported or fully-qualified in the same file, which real code does when working with enum values generically (confirmed: mxmodelreflection and communitycommons both do this). This will under-report code that calls .isValid(context, value) on a generated enum proxy class without ever naming MendixEnum in that file -- a narrower, safer miss rather than a regex that can't tell a two-argument isValid on an unrelated class apart from this one.

**Source quotes:**

- "We removed the deprecated `com.mendix.core.objectmanagement.member.MendixEnum#isValid(IContext, String)`" ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
