---
title: "Mx11: The sql_mode driver parameter is no longer set for MySQL and MariaDB"
topic: upgrade
keywords: ["sql_mode driver parameter", "MySQL MariaDB", "Mendix 11", "database configuration", "sql_mode", "driver parameter", "MySQL upgrade", "MariaDB upgrade", "database server setting", "connection mode"]
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
**What changes:** The sql_mode driver parameter is no longer set for MySQL and MariaDB. Category: behaviour change. Severity in the catalog: medium.

**Applies:** from Mendix 11.0.0 on. Affects: project.

**Status:** will break (catalog: certain).

**How to find it:** manual review (cannot be detected automatically); detection confidence high.

**Fix:** Set the required sql_mode on the database server itself, since the runtime no longer sets it per connection.

**False positives:** Only relevant to MySQL and MariaDB deployments, and the setting lives on the database server rather than in the app.

**Source quotes:**

- "For MariaDB and MySQL, we no longer set the sql_mode driver parameter." ([Upgrading from Mendix Studio Pro 10 to 11](https://docs.mendix.com/refguide/upgrading-from-10-to-11/))
