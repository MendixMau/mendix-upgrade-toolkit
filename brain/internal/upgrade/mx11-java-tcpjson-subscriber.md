---
title: "Mx11: The tcpjson log subscriber was removed"
topic: upgrade
keywords: ["tcpjson log subscriber removed", "tcpjson deprecated", "log subscriber tcpjson", "MX11-JAVA-TCPJSON-SUBSCRIBER", "tcpjsonlines", "Mendix 11.9", "tcpjson migration", "log configuration", "tcpjson tcpjsonlines", "upgrade Mendix 11", "log subscriber deprecated", "tcpjson replacement"]
domain: [upgrade, architecture]
kind: pitfall
applies_to: mendix-general
versions: "11.9.0 and later"
layer: field
sources:
  - {title: "Studio Pro 11.9 release notes", url: "https://docs.mendix.com/releasenotes/studio-pro/11.9/", date: "2026-09-15"}
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed

---
**What changes:** The tcpjson log subscriber was removed. Category: removed in Mendix 11. Severity in the catalog: medium.

**Applies:** from Mendix 11.9.0 on. Affects: project.

**Status:** will break (catalog: certain).

**How to find it:** manual review (cannot be detected automatically); detection confidence high.

**Fix:** Switch the log subscriber configuration from tcpjson to tcpjsonlines.

**Source quotes:**

- "We removed the deprecated `tcpjson` log subscriber." ([Studio Pro 11.9 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.9/))
