---
title: "Mx11: mx.ui.downloadFile and mx.data.getFileUrl are now asynchronous"
topic: upgrade
keywords: ["mx.ui.downloadFile", "mx.data.getFileUrl", "asynchronous", "async", "Promise", "await", "breaking change", "Mendix 11.7", "JavaScript action", "MX11-CLIENT-DOWNLOADFILE-ASYNC"]
domain: [upgrade, ux-ui]
kind: pitfall
applies_to: mendix-general
versions: "11.7.0 and later"
layer: field
sources:
  - {title: "Studio Pro 11.7 release notes", url: "https://docs.mendix.com/releasenotes/studio-pro/11.7/", date: "2026-09-19"}
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed

---
**What changes:** mx.ui.downloadFile and mx.data.getFileUrl are now asynchronous. Category: behaviour change. Severity in the catalog: high.

**Applies:** from Mendix 11.7.0 on. Affects: js.

**Status:** will break (catalog: certain).

**How to find it:** automatic, by a pattern search over the app's code; detection confidence medium.

**Fix:** Custom JavaScript actions calling mx.ui.downloadFile or mx.data.getFileUrl synchronously (using the return value directly) must be updated to await the returned Promise.

**False positives:** A negative lookbehind excludes any call already preceded by 'await ' on the same line, so an already-fixed call site does not re-flag. This assumes a single space between await and the call; unusual spacing would under-detect rather than over-detect, the safer direction. Does not catch a call whose result is awaited on a later line (e.g. assigned to a variable first) -- that shape needs a human look either way.

**Source quotes:**

- "The `mx.ui.downloadFile` function is now asynchronous" ([Studio Pro 11.7 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.7/))
- "The `mx.data.getFileUrl` function is now asynchronous" ([Studio Pro 11.7 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.7/))
