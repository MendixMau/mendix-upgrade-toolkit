---
title: "Mx11: Deprecated ActionListener and EventActionInfo API surface was removed"
topic: upgrade
keywords: ["ActionListener deprecated removed", "EventActionInfo removed", "clone() method removed", "setTargetClass() removed", "IMendixObject Consumer", "addBeforeEvent", "addAfterEvent", "Mendix 11 breaking change", "generic type parameter removed", "com.mendix.core.actionmanagement", "MX11-JAVA-ACTIONLISTENER-API-REMOVED"]
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
**What changes:** Deprecated ActionListener and EventActionInfo API surface was removed. Category: removed in Mendix 11. Severity in the catalog: medium.

**Applies:** from Mendix 11.0.0 on. Affects: java.

**Status:** will break (catalog: certain).

**How to find it:** manual review (cannot be detected automatically); detection confidence medium.

**Fix:** Update any custom ActionListener/EventActionInfo usage to the non-generic, IMendixObject-typed signatures; drop calls to the removed clone()/setTargetClass() methods.

**False positives:** Four related changes to the same ActionListener/EventActionInfo pairing, grouped into one entry.

**Source quotes:**

- "We removed the deprecated `com.mendix.core.actionmanagement.ActionListener#clone()`" ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
- "We removed the deprecated `com.mendix.core.actionmanagement.ActionListener#setTargetClass(Class<T>)` method" ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
- "We removed the type parameter from the `com.mendix.core.actionmanagement.EventActionInfo` class as it only accepts `java.util.function.Consumer` instances with type parameter `IMendixObject`" ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
- "We removed the result type parameter of the methods `addBeforeEvent(Consumer<IMendixObject>, boolean)` and `addAfterEvent(Consumer<IMendixObject>)` in the `com.mendix.core.actionmanagement.ActionListener` class" ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
