---
title: "Mx11: Several deprecated custom runtime settings and behaviors were removed"
topic: upgrade
keywords: ["Mendix 11 upgrade", "deprecated settings removed", "ObjectManagement.StrictChangeBehavior", "Microflows.RemoveVariableOnDeleteObjectsActivity", "Objects.SetSystemAttributesOnChange", "workflow state change handlers", "custom runtime settings", "MX11-PLATFORM-DEPRECATED-SETTINGS-REMOVED", "breaking changes", "deployment configuration"]
domain: [upgrade, devops-cloud]
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
**What changes:** Several deprecated custom runtime settings and behaviors were removed. Category: removed in Mendix 11. Severity in the catalog: medium.

**Applies:** from Mendix 11.0.0 on. Affects: project.

**Status:** will break (catalog: certain).

**How to find it:** manual review (cannot be detected automatically); detection confidence medium.

**Fix:** Check deployment custom settings for ObjectManagement.StrictChangeBehavior, Microflows.RemoveVariableOnDeleteObjectsActivity, and Objects.SetSystemAttributesOnChange; check workflows for on-state-change handlers.

**Source quotes:**

- "We removed the deprecated `ObjectManagement.StrictChangeBehavior` custom runtime setting" ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
- "We removed the deprecated `Microflows.RemoveVariableOnDeleteObjectsActivity` runtime setting" ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
- "We removed the deprecated `Objects.SetSystemAttributesOnChange` runtime setting" ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
- "We removed the (deprecated) **on state change** handlers for workflows" ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
- "We removed the legacy migration of thumbnails" ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
