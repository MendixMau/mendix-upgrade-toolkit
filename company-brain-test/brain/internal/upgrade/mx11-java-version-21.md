---
title: "Mx11: Java 21 is required"
topic: upgrade
keywords: ["Java 21 required", "Mendix 11 Java version", "Java action rebuild", "Java version setting", "JDK upgrade", "Mx11 Java blocker", "Java 21 deprecated", "project Java configuration", "Studio Pro 11 Java", "Java version 21"]
domain: [upgrade, architecture]
kind: pitfall
applies_to: mendix-general
versions: "11.0.0 and later"
layer: field
sources:
  - {title: "Upgrading from Mendix Studio Pro 10 to 11", url: "https://docs.mendix.com/refguide/upgrading-from-10-to-11/", date: "2026-09-15"}
  - {title: "Studio Pro 11.14 release notes", url: "https://docs.mendix.com/releasenotes/studio-pro/11.14/", date: "2026-09-15"}
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed

---
**What changes:** Java 21 is required. Category: platform or configuration change. Severity in the catalog: blocker.

**Applies:** from Mendix 11.0.0 on. Affects: project.

**Status:** will break (catalog: certain).

**How to find it:** automatic, from the project settings; detection confidence high.

**Fix:** Set the app's Java version to 21 and rebuild every Java action against that JDK. Note that Java 21 itself is already deprecated as of 11.14 and goes away in Mendix 12.

**Source quotes:**

- "Studio Pro 10.21 and above requires your application to use Java 21." ([Upgrading from Mendix Studio Pro 10 to 11](https://docs.mendix.com/refguide/upgrading-from-10-to-11/))
- "We deprecated support for Java 21. Support for Java 21 will be removed in Mendix 12." ([Studio Pro 11.14 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.14/))
