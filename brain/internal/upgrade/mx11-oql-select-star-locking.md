---
title: "Mx11: SELECT * in OQL now always returns the same columns regardless of optimistic locking"
topic: upgrade
keywords: ["SELECT * OQL", "optimistic locking columns", "OQL query columns", "column ordering OQL", "SELECT star locking", "OQL breaking change", "positional indexing OQL", "Mendix 11.10", "locking-dependent columns", "OQL consistency"]
domain: [upgrade, data-modeling]
kind: pitfall
applies_to: mendix-general
versions: "11.10.0 and later"
layer: field
sources:
  - {title: "Studio Pro 11.10 release notes", url: "https://docs.mendix.com/releasenotes/studio-pro/11.10/", date: "2026-09-19"}
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed

---
**What changes:** SELECT * in OQL now always returns the same columns regardless of optimistic locking. Category: behaviour change. Severity in the catalog: low.

**Applies:** from Mendix 11.10.0 on. Affects: project.

**Status:** may break, verify manually (catalog: not certain).

**How to find it:** automatic, by a query over the app model; detection confidence low.

**Fix:** Review OQL consumers that positionally index SELECT * columns and previously relied on the optimistic-locking-dependent column set.

**Source quotes:**

- "We now ensure a `SELECT *` OQL query returns the same columns independent of the optimistic locking setting value" ([Studio Pro 11.10 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.10/))
