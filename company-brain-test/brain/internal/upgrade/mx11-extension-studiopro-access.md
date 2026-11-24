---
title: "Mx11: Extensions can no longer obtain the studioPro object directly"
topic: upgrade
keywords: ["studioPro object access", "extension API entry point", "Mendix 11 extensions", "Studio Pro 11.2", "MX11-EXTENSION-STUDIOPRO-ACCESS", "extension breaking change", "studioPro removed", "extension upgrade", "Studio Pro extension API", "cannot obtain studioPro"]
domain: [upgrade, architecture]
kind: pitfall
applies_to: mendix-general
versions: "11.2.0 and later"
layer: field
sources:
  - {title: "Studio Pro 11.2 release notes", url: "https://docs.mendix.com/releasenotes/studio-pro/11.2/", date: "2026-09-15"}
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed

---
**What changes:** Extensions can no longer obtain the studioPro object directly. Category: removed in Mendix 11. Severity in the catalog: medium.

**Applies:** from Mendix 11.2.0 on. Affects: project.

**Status:** will break (catalog: certain).

**How to find it:** manual review (cannot be detected automatically); detection confidence high.

**Fix:** Update Studio Pro extensions to acquire the API through the supported entry point rather than reaching for the studioPro object.

**Source quotes:**

- "Extension authors cannot simply obtain access to `studioPro` object anymore" ([Studio Pro 11.2 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.2/))
