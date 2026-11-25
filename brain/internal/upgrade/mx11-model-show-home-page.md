---
title: "Mx11: ShowHomePage microflow now enforces entity access"
topic: upgrade
keywords: ["ShowHomePage microflow", "entity access enforcement", "Mendix 11", "microflow call chain", "System module", "access control error", "entity access verification", "microflow permissions", "MX11 upgrade", "breaking change"]
domain: [upgrade, architecture]
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
**What changes:** ShowHomePage microflow now enforces entity access. Category: behaviour change. Severity in the catalog: high.

**Applies:** from Mendix 11.0.0 on. Affects: microflow.

**Status:** may break, verify manually (catalog: not certain).

**How to find it:** automatic, by a query over the app model; detection confidence medium.

**Fix:** Check every microflow called from ShowHomePage: each must also apply entity access, or the call now errors.

**False positives:** Matches the microflow by name only. It does not verify the call chain, so a match is a prompt to review rather than proof of a break.

**Source quotes:**

- "A microflow that does not apply entity access can only call microflows that also do not apply entity access" ([Upgrading from Mendix Studio Pro 10 to 11](https://docs.mendix.com/refguide/upgrading-from-10-to-11/))
- "We enabled entity access on the **ShowHomePage** microflow in the **System** module" ([Studio Pro 11.0 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.0/))
