---
title: "Mx11: Support was dropped for PostgreSQL 13 and MariaDB 10.6"
topic: upgrade
keywords: ["PostgreSQL 13 dropped", "MariaDB 10.6 dropped", "database version support", "Mendix 11.13.0", "database upgrade", "unsupported database version", "PostgreSQL unsupported", "MariaDB unsupported", "database compatibility", "MX11-DB-VERSION-SUPPORT-DROPPED"]
domain: [upgrade, data-modeling]
kind: pitfall
applies_to: mendix-general
versions: "11.13.0 and later"
layer: field
sources:
  - {title: "Studio Pro 11.13 release notes", url: "https://docs.mendix.com/releasenotes/studio-pro/11.13/", date: "2026-09-15"}
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed

---
**What changes:** Support was dropped for PostgreSQL 13 and MariaDB 10.6. Category: platform or configuration change. Severity in the catalog: high.

**Applies:** from Mendix 11.13.0 on. Affects: project.

**Status:** will break (catalog: certain).

**How to find it:** manual review (cannot be detected automatically); detection confidence high.

**Fix:** Check the database engine version behind every environment and upgrade PostgreSQL past 13 or MariaDB past 10.6 before moving to 11.13.

**False positives:** The database server version is a deployment property, not something the project model records, so it has to be checked per environment by hand.

**Source quotes:**

- "We dropped support for the following database versions that are no longer supported by the vendors:" ([Studio Pro 11.13 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.13/))
