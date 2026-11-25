---
title: "Mx11: The scope parameter was removed from subscribe in mx-api/data"
topic: upgrade
keywords: ["subscribe scope removed", "mx-api data scope", "subscribe callback binding", "MX11-CLIENT-SUBSCRIBE-SCOPE", "scope parameter subscribe", "arrow function bind", "mx-api/data breaking change", "subscribe mx-api", "Mendix 11.10 scope", "removed scope argument"]
domain: [upgrade, ux-ui]
kind: pitfall
applies_to: mendix-general
versions: "11.10.0 and later"
layer: field
sources:
  - {title: "Studio Pro 11.10 release notes", url: "https://docs.mendix.com/releasenotes/studio-pro/11.10/", date: "2026-09-15"}
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed

---
**What changes:** The scope parameter was removed from subscribe in mx-api/data. Category: removed in Mendix 11. Severity in the catalog: high.

**Applies:** from Mendix 11.10.0 on. Affects: js.

**Status:** will break (catalog: certain).

**How to find it:** automatic, by a pattern search over the app's code; detection confidence medium.

**Fix:** Drop the scope argument and bind the callback with an arrow function or Function.prototype.bind instead.

**False positives:** Matches any subscribe call in a file that imports mx-api/data; whether the removed scope argument was actually passed still needs a look at the matched line.

**Source quotes:**

- "We removed the `scope` parameter from the `subscribe` method in `mx-api/data`." ([Studio Pro 11.10 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.10/))
