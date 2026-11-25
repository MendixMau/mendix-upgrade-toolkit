---
title: "Mx11: Hebrew and Indonesian language codes were replaced"
topic: upgrade
keywords: ["Hebrew language code iw_IL", "Indonesian language code in_ID", "language codes deprecated", "he_IL id_ID", "MX11-PLATFORM-LANGUAGE-CODES", "Language Operations", "upgrade 11.8.0", "language variant replacement", "project language settings"]
domain: [upgrade, devops-cloud]
kind: pitfall
applies_to: mendix-general
versions: "11.8.0 and later"
layer: field
sources:
  - {title: "Studio Pro 11.8 release notes", url: "https://docs.mendix.com/releasenotes/studio-pro/11.8/", date: "2026-09-15"}
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed

---
**What changes:** Hebrew and Indonesian language codes were replaced. Category: deprecation. Severity in the catalog: medium.

**Applies:** from Mendix 11.8.0 on. Affects: project.

**Status:** will break (catalog: certain).

**How to find it:** automatic, from the project settings; detection confidence high.

**Fix:** Add the non-deprecated language variant, move translations across with Language Operations, then delete the old asterisked language.

**Source quotes:**

- "**Hebrew**: Changed from `iw_IL` (deprecated) to `he_IL` (current standard)" ([Studio Pro 11.8 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.8/))
- "**Indonesian**: Changed from `in_ID` (deprecated) to `id_ID` (current standard)" ([Studio Pro 11.8 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.8/))
