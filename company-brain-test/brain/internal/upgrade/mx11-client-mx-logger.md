---
title: "Mx11: Client API mx.logger removed"
topic: upgrade
keywords: ["mx.logger removed", "mx.logger", "Client API removed", "mx.logger Mendix 11", "window.console", "client logging", "JavaScript logger", "mx.logger replace", "upgrade Mendix 11", "broken client API", "console functions", "JS logging"]
domain: [upgrade, ux-ui]
kind: pitfall
applies_to: mendix-general
versions: "11.0.0 and later"
layer: field
sources:
  - {title: "Upgrading from Mendix Studio Pro 10 to 11", url: "https://docs.mendix.com/refguide/upgrading-from-10-to-11/", date: "2026-09-15"}
  - {title: "Studio Pro 11.0 release notes", url: "https://docs.mendix.com/releasenotes/studio-pro/11.0/", date: "2026-09-15"}
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed

---
**What changes:** Client API mx.logger removed. Category: removed in Mendix 11. Severity in the catalog: blocker.

**Applies:** from Mendix 11.0.0 on. Affects: js.

**Status:** will break (catalog: certain).

**How to find it:** automatic, by a pattern search over the app's code; detection confidence high.

**Fix:** Replace mx.logger calls with the equivalent window.console functions.

**False positives:** A bundled third-party library may contain the literal string. Confirm the match is in hand-written app code, not a vendored bundle.

**Source quotes:**

- "Client API `mx.logger` is no longer supported." ([Upgrading from Mendix Studio Pro 10 to 11](https://docs.mendix.com/refguide/upgrading-from-10-to-11/))
- "For logging, please use the `window.console` logging functions instead." ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
