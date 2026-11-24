---
title: "Mx11: Deprecated Metrics API methods were removed"
topic: upgrade
keywords: ["Metrics API removed", "Metrics counters removed", "Metrics gauges removed", "Metrics sets removed", "com.mendix.metrics", "Counters interface", "Gauges interface", "Sets interface", "MX11-JAVA-METRICS-API-REMOVED", "Mendix 11 breaking changes"]
domain: [upgrade, architecture]
kind: pitfall
applies_to: mendix-general
versions: "11.0.0 and later"
layer: field
sources:
  - {title: "Studio Pro 11.0 release notes", url: "https://docs.mendix.com/releasenotes/studio-pro/11.0/", date: "2026-09-19"}
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed

---
**What changes:** Deprecated Metrics API methods were removed. Category: removed in Mendix 11. Severity in the catalog: medium.

**Applies:** from Mendix 11.0.0 on. Affects: java.

**Status:** will break (catalog: certain).

**How to find it:** automatic, by a pattern search over the app's code; detection confidence high.

**Fix:** Replace any use of Metrics#counters()/gauges()/sets() and the Counters/Gauges/Sets interfaces with the current Metrics API.

**False positives:** Three sibling methods on the same Metrics class, removed together -- grouped as one fact rather than three.

**Source quotes:**

- "We removed the deprecated `com.mendix.metrics.Metrics#counters()` method and `com.mendix.metrics.Counters` interface" ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
- "We removed the deprecated `com.mendix.metrics.Metrics#gauges()` method and `com.mendix.metrics.Gauges` interface" ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
- "We removed the deprecated `com.mendix.metrics.Metrics#sets()` method and `com.mendix.metrics.Sets` interface" ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
