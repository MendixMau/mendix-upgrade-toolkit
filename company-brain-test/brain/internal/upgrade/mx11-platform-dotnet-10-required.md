---
title: "Mx11: Studio Pro itself now requires .NET 10"
topic: upgrade
keywords: ["Studio Pro .NET 10 requirement", ".NET 10 prerequisite", "Studio Pro 11.7 .NET upgrade", ".NET version upgrade", "developer machine .NET", "MX11-PLATFORM-DOTNET-10-REQUIRED", "Studio Pro 11.7.0", ".NET 8 to .NET 10", "upgrade blocker", "system requirement .NET"]
domain: [upgrade, devops-cloud]
kind: pitfall
applies_to: mendix-general
versions: "11.7.0 and later"
layer: field
sources:
  - {title: "Studio Pro 11.7 release notes", url: "https://docs.mendix.com/releasenotes/studio-pro/11.7/", date: "2026-09-19"}
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed

---
**What changes:** Studio Pro itself now requires .NET 10. Category: platform or configuration change. Severity in the catalog: blocker.

**Applies:** from Mendix 11.7.0 on. Affects: project.

**Status:** will break (catalog: certain).

**How to find it:** manual review (cannot be detected automatically); detection confidence high.

**Fix:** This blocks opening the project at all, not just a runtime behavior -- install .NET 10 on every developer machine before upgrading Studio Pro to 11.7+.

**Source quotes:**

- "Studio Pro has been updated to run on .NET 10 instead of .NET 8. As a result, .NET 10 is now a required prerequisite" ([Studio Pro 11.7 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.7/))
