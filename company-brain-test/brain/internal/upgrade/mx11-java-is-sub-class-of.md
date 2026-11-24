---
title: "Mx11: Core.isSubClassOf was removed"
topic: upgrade
keywords: ["Core.isSubClassOf removed", "isSubClassOf", "Core helper method removed", "Mendix 11 breaking change", "IMetaObject.isSubClassOf", "MX11-JAVA-IS-SUB-CLASS-OF", "static Core call", "deprecated API", "upgrade blocker", "Java compatibility issue"]
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
**What changes:** Core.isSubClassOf was removed. Category: removed in Mendix 11. Severity in the catalog: blocker.

**Applies:** from Mendix 11.0.0 on. Affects: java.

**Status:** will break (catalog: certain).

**How to find it:** automatic, by a pattern search over the app's code; detection confidence high.

**Fix:** Call isSubClassOf on the IMetaObject itself rather than through the static Core helper.

**False positives:** Anchored to the static Core call on purpose. The instance method metaObject.isSubClassOf(...) still exists, and an unanchored pattern also matches longer identifiers that merely begin with isSubClassOf.

**Source quotes:**

- "We removed the deprecated `com.mendix.core.Core.isSubClassOf(IMetaObject, IMetaObject)`" ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
