---
title: "Mx11: Consumer<IMendixObject> overloads are deprecated, to be removed in Mendix 12"
topic: upgrade
keywords: ["Consumer<IMendixObject>", "deprecated Mendix 12", "BiConsumer<IContext, IMendixObject>", "ListenersRegistry", "ActionListener", "EventActionInfo", "MX11-JAVA-CONSUMER-OVERLOAD-DEPRECATED", "Consumer overload migration", "IMendixObject", "migrate overloads"]
domain: [upgrade, architecture]
kind: pitfall
applies_to: mendix-general
versions: "11.14.0 and later"
layer: field
sources:
  - {title: "Studio Pro 11.14 release notes", url: "https://docs.mendix.com/releasenotes/studio-pro/11.14/", date: "2026-09-27"}
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed

---
**What changes:** Consumer<IMendixObject> overloads are deprecated, to be removed in Mendix 12. Category: deprecation. Severity in the catalog: low.

**Applies:** from Mendix 11.14.0 on. Affects: java.

**Status:** will break (catalog: certain).

**How to find it:** automatic, by a pattern search over the app's code; detection confidence medium.

**Fix:** Confirmed affected surface: the existing Consumer<IMendixObject> overloads on ListenersRegistry, ActionListener, and EventActionInfo. Migrate to the new BiConsumer<IContext, IMendixObject> overloads (added the same release) before Mendix 12.

**Source quotes:**

- "The existing Consumer<IMendixObject> methods are deprecated and will be removed in Mendix 12." ([Studio Pro 11.14 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.14/))
