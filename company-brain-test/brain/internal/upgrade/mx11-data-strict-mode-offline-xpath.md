---
title: "Mx11: Strict mode for offline apps can break code still using retrieve_by_xpath"
topic: upgrade
keywords: ["retrieve_by_xpath deprecated", "strict mode offline", "offline apps strict mode", "retrieve_by_xpath break", "MX11-DATA-STRICT-MODE-OFFLINE-XPATH", "Mendix 11.9 xpath", "client API xpath", "offline strict mode breaking change", "migrate retrieve_by_xpath", "xpath deprecation"]
domain: [upgrade, data-modeling]
kind: pitfall
applies_to: mendix-general
versions: "11.9.0 and later"
layer: field
sources:
  - {title: "Studio Pro 11.9 release notes", url: "https://docs.mendix.com/releasenotes/studio-pro/11.9/", date: "2026-09-19"}
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed

---
**What changes:** Strict mode for offline apps can break code still using retrieve_by_xpath. Category: behaviour change. Severity in the catalog: high.

**Applies:** from Mendix 11.9.0 on. Affects: js.

**Status:** may break, verify manually (catalog: not certain).

**How to find it:** automatic, by a pattern search over the app's code; detection confidence medium.

**Fix:** Only relevant to offline apps that enable strict mode and still call the deprecated retrieve_by_xpath client API. Migrate those calls before enabling strict mode.

**False positives:** certain:false -- this only breaks apps that both enable strict mode AND still use the old API; enabling strict mode alone is not itself the break.

**Source quotes:**

- "switching strict mode on for existing offline apps may cause problems for existing apps that still call the old API (`retrieve_by_xpath`)" ([Studio Pro 11.9 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.9/))
