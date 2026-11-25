---
title: "Mx11: Intel-based Macs are no longer supported"
topic: upgrade
keywords: ["Intel Mac support dropped", "Apple Silicon required", "Intel-based Macs unsupported", "Mendix 11.12 Mac compatibility", "Studio Pro Intel Mac", "Mac platform requirement", "MX11-PLATFORM-INTEL-MAC", "Intel processor not supported", "Apple Silicon hardware upgrade", "macOS Intel deprecated"]
domain: [upgrade, devops-cloud]
kind: pitfall
applies_to: mendix-general
versions: "11.12.0 and later"
layer: field
sources:
  - {title: "Studio Pro 11.12 release notes", url: "https://docs.mendix.com/releasenotes/studio-pro/11.12/", date: "2026-09-15"}
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed

---
**What changes:** Intel-based Macs are no longer supported. Category: platform or configuration change. Severity in the catalog: medium.

**Applies:** from Mendix 11.12.0 on. Affects: project.

**Status:** will break (catalog: certain).

**How to find it:** manual review (cannot be detected automatically); detection confidence high.

**Fix:** Developers on Intel Macs need Apple Silicon hardware to run Studio Pro 11.12 or later.

**False positives:** A property of the developer's machine, not the app. Relevant to upgrade planning for the team rather than to any model element.

**Source quotes:**

- "Intel-based Macs are no longer supported." ([Studio Pro 11.12 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.12/))
