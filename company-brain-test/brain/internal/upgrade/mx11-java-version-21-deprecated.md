---
title: "Mx11: Java 21 support is deprecated, to be removed in Mendix 12"
topic: upgrade
keywords: ["Java 21 deprecated", "Mendix 12 Java", "Java version requirement", "MX11-JAVA-VERSION-21-DEPRECATED", "Java 21 removal", "project settings Java", "Java 25", "upgrade Java version", "Mendix 11.14 Java", "Java compatibility"]
domain: [upgrade, architecture]
kind: pitfall
applies_to: mendix-general
versions: "11.14.0 and later"
layer: field
sources:
  - {title: "Studio Pro 11.14 release notes", url: "https://docs.mendix.com/releasenotes/studio-pro/11.14/", date: "2026-09-19"}
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed

---
**What changes:** Java 21 support is deprecated, to be removed in Mendix 12. Category: deprecation. Severity in the catalog: low.

**Applies:** from Mendix 11.14.0 on. Affects: project.

**Status:** will break (catalog: certain).

**How to find it:** automatic, from the project settings; detection confidence high.

**Fix:** Not yet a break in 11.x -- Java 21 is still required through Mendix 11 (see MX11-JAVA-VERSION-21). Plan for whatever Java version Mendix 12 requires.

**False positives:** Same SHOW SETTINGS fact as MX11-JAVA-VERSION-21. Only applies from 11.14, where Java 25 became available; a project on Java 21 is fine today and is told to plan the move before Mendix 12.

**Source quotes:**

- "Support for Java 21 will be removed in Mendix 12" ([Studio Pro 11.14 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.14/))

**Related catalog entries:** MX11-JAVA-VERSION-21.
