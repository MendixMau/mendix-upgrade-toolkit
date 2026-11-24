---
title: "Mx11: Support was dropped for MariaDB 10.5, SQL Server 2019 and MySQL 8.0"
topic: upgrade
keywords: ["MariaDB 10.5", "SQL Server 2019", "MySQL 8.0", "database version dropped", "Mendix 11.4", "unsupported database", "database upgrade", "MariaDB deprecated", "MySQL 8.0 support", "SQL Server 2019 support"]
domain: [upgrade, data-modeling]
kind: pitfall
applies_to: mendix-general
versions: "11.4.0 and later"
layer: field
sources:
  - {title: "Studio Pro 11.2 release notes", url: "https://docs.mendix.com/releasenotes/studio-pro/11.2/", date: "2026-09-15"}
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed

---
**What changes:** Support was dropped for MariaDB 10.5, SQL Server 2019 and MySQL 8.0. Category: platform or configuration change. Severity in the catalog: high.

**Applies:** from Mendix 11.4.0 on. Affects: project.

**Status:** will break (catalog: certain).

**How to find it:** manual review (cannot be detected automatically); detection confidence high.

**Fix:** Upgrade the database engine off MariaDB 10.5, SQL Server 2019 or MySQL 8.0 before moving past 11.4.

**False positives:** Announced in the 11.2 notes but effective from 11.4, so applies_from is 11.4.0. The database server version is a deployment property the project model does not record.

**Source quotes:**

- "Starting with Mendix version 11.4, we will drop support for the following database versions" ([Studio Pro 11.2 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.2/))

**Related catalog entries:** MX11-DB-VERSION-SUPPORT-DROPPED.
