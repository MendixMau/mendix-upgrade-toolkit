---
title: "Mx11: JavaScript actions must not use the Dojo-era client APIs"
topic: upgrade
keywords: ["Dojo client APIs", "JavaScript actions", "Mendix 11", "React client", "mx.ui.openForm", "dojo global", "dijit global", "page-navigation API", "MX11-CLIENT-FORBIDDEN-DOJO-APIs", "forbidden APIs", "Dojo deprecated", "client API migration"]
domain: [upgrade, ux-ui]
kind: pitfall
applies_to: mendix-general
versions: "11.0.0 and later"
layer: field
sources:
  - {title: "Mendix React Client", url: "https://docs.mendix.com/refguide/mendix-client/react/", date: "2026-09-15"}
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed

---
**What changes:** JavaScript actions must not use the Dojo-era client APIs. Category: breaks only in the React client. Severity in the catalog: blocker.

**Applies:** from Mendix 11.0.0 on. Affects: js.

**Status:** will break (catalog: certain).

**How to find it:** automatic, by a pattern search over the app's code; detection confidence high.

**Fix:** Rewrite the JavaScript action against the mx-api modules: replace mx.ui.openForm with the page-navigation API and drop the dojo and dijit globals entirely.

**False positives:** The dojo and dijit patterns are anchored to a global reference followed by a dot or bracket so a variable merely named dojoConfig does not match. A hit inside a vendored bundle under javascriptsource still needs confirming as hand-written code.

**Source quotes:**

- "JavaScript actions must not use any of the following client APIs:" ([Mendix React Client](https://docs.mendix.com/refguide/mendix-client/react/))
- "These APIs are related to Dojo and are no longer needed." ([Mendix React Client](https://docs.mendix.com/refguide/mendix-client/react/))

**Related catalog entries:** MX11-CLIENT-DOJO-DEPRECATED.
