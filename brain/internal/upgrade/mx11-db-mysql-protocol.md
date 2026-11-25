---
title: "Mx11: jdbc:mysql: is no longer accepted as a database protocol"
topic: upgrade
keywords: ["jdbc:mysql protocol removed", "DatabaseJdbcUrl", "jdbc:mariadb protocol", "MySQL upgrade Mendix 11", "database protocol change", "MX11-DB-MYSQL-PROTOCOL", "jdbc:mysql no longer accepted", "MariaDB migration", "custom database setting", "Mendix 11 breaking change"]
domain: [upgrade, data-modeling]
kind: pitfall
applies_to: mendix-general
versions: "11.0.0 and later"
layer: field
sources:
  - {title: "Upgrading from Mendix Studio Pro 10 to 11", url: "https://docs.mendix.com/refguide/upgrading-from-10-to-11/", date: "2026-09-15"}
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed

---
**What changes:** jdbc:mysql: is no longer accepted as a database protocol. Category: platform or configuration change. Severity in the catalog: blocker.

**Applies:** from Mendix 11.0.0 on. Affects: project.

**Status:** will break (catalog: certain).

**How to find it:** manual review (cannot be detected automatically); detection confidence high.

**Fix:** Change the DatabaseJdbcUrl custom setting in every environment to use the jdbc:mariadb: protocol.

**Source quotes:**

- "we no longer accept `jdbc:mysql:` as a protocol. Use `jdbc:mariadb:` instead" ([Upgrading from Mendix Studio Pro 10 to 11](https://docs.mendix.com/refguide/upgrading-from-10-to-11/))
