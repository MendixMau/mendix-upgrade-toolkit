---
title: SAML module encryption became per-configuration around 3.5.0
topic: upgrade
domain: [security]
kind: pitfall
applies_to: mendix-general
versions: "SAML 3.3.x -> 3.5.0+ (Mx9 line)"
keywords: ["SAML encryption configuration", "SAML upgrade 3.5.0", "encryption per-configuration", "SAML encryption checkbox", "SAML role rename ReadOnly", "Admin_ReadSAMLEntities", "SAML userlib cleanup", "SAML module encryption", "multi-version upgrade", "SAML configuration encryption"]
layer: field
sources:
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed
---
**Symptom**
- After a multi-version SAML upgrade (3.3.12 → 3.6.27), encryption behaves differently.
- An AI assistant attributed the change to the wrong release (3.6.27).

**Root cause**
- Starting around 3.5.0, encryption moved from a single global flag to a per-configuration checkbox.

**Fix**
- Set the encryption checkbox on each SAML configuration.
- When an upgrade spans several minors, read the cumulative release notes across the whole range, not just the target's.
- Also check the SAML role rename (ReadOnly → `Admin_ReadSAMLEntities`) and the userlib cleanup in that range.

**Status**
- Field report. The exact version (3.5.0) is "around" per the source.

**Release notes**
- SAML 3.6.0 renamed the ReadOnly role; many versions require deleting old userlib JARs (https://marketplace.mendix.com/link/component/1174)
