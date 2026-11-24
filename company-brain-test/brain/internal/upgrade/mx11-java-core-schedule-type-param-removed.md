---
title: "Mx11: Core scheduling methods lost their generic type parameter"
topic: upgrade
keywords: ["scheduling methods generic type parameter", "Core.schedule removed type parameter", "Core.reschedule type parameter", "scheduleAtFixedRate type parameter", "scheduleWithFixedDelay type parameter", "Mendix 11 breaking change scheduling", "MX11-JAVA-CORE-SCHEDULE-TYPE-PARAM-REMOVED", "ICoreAction scheduling", "RunnableScheduledFuture reschedule", "generic type removed"]
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
**What changes:** Core scheduling methods lost their generic type parameter. Category: removed in Mendix 11. Severity in the catalog: blocker.

**Applies:** from Mendix 11.0.0 on. Affects: java.

**Status:** will break (catalog: certain).

**How to find it:** manual review (cannot be detected automatically); detection confidence high.

**Fix:** Update any custom code calling Core.schedule/reschedule/scheduleAtFixedRate/scheduleWithFixedDelay to the non-generic signatures.

**False positives:** Seven overloads across schedule/reschedule/scheduleAtFixedRate(x3)/scheduleWithFixedDelay, all losing the same generic type parameter in the same release -- grouped as one fact.

**Source quotes:**

- "We removed the type parameter from the `com.mendix.core.Core.schedule(String, Date)` method" ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
- "We removed the type parameter from the `com.mendix.core.Core.schedule(ICoreAction, long, TimeUnit)` method" ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
- "We removed the type parameter from the `com.mendix.core.Core.reschedule(RunnableScheduledFuture, ICoreAction, long, TimeUnit)` method" ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
- "We removed the type parameter from the `com.mendix.core.Core.scheduleAtFixedRate(String, Date, long, TimeUnit, String, String)` method" ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
- "We removed the type parameter from the `com.mendix.core.Core.scheduleWithFixedDelay(ICoreAction, long, long, TimeUnit)` method" ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
