---
title: "Mx11: Downgrading a database deployed with a newer Mendix version is disallowed"
topic: upgrade
keywords: ["database downgrade disallowed", "Mendix 11.2 downgrade", "one-way upgrade", "database rollback", "version downgrade database", "MX11-DB-DOWNGRADE-DISALLOWED", "downgrading database", "deployment rollback", "Mendix version incompatibility", "database migration one-way"]
domain: [upgrade, data-modeling]
kind: pitfall
applies_to: mendix-general
versions: "11.2.0 and later"
layer: field
sources:
  - {title: "Studio Pro 11.2 release notes", url: "https://docs.mendix.com/releasenotes/studio-pro/11.2/", date: "2026-09-15"}
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed

---
**What changes:** Downgrading a database deployed with a newer Mendix version is disallowed. Category: behaviour change. Severity in the catalog: high.

**Applies:** from Mendix 11.2.0 on. Affects: project.

**Status:** will break (catalog: certain).

**How to find it:** manual review (cannot be detected automatically); detection confidence high.

**Fix:** Plan the upgrade as one-way per environment: take a database backup before deploying, since rolling back to an older Mendix version against the same database no longer starts.

**False positives:** A deployment-time constraint rather than a model property. It matters most for the rollback plan, which is why it belongs in upgrade planning even though nothing in the app changes.

**Source quotes:**

- "We now disallow downgrading a Mendix database that had been previously deployed with a newer version of Mendix." ([Studio Pro 11.2 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.2/))
