---
title: "Mx11: Development servlets now require authentication"
topic: upgrade
keywords: ["development servlet authentication", "Core.addDevelopmentServlet", "X-M2EE-Authentication header", "M2EE admin password", "servlet requires authentication", "MX11-JAVA-DEV-SERVLET-AUTH", "development servlet 11.12", "addDevelopmentServlet auth", "X-M2EE-Authentication", "Base64 authentication header", "Mendix 11.12 servlet security"]
domain: [upgrade, architecture]
kind: pitfall
applies_to: mendix-general
versions: "11.12.3 and later"
layer: field
sources:
  - {title: "Studio Pro 11.12 release notes", url: "https://docs.mendix.com/releasenotes/studio-pro/11.12/", date: "2026-09-15"}
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed

---
**What changes:** Development servlets now require authentication. Category: behaviour change. Severity in the catalog: high.

**Applies:** from Mendix 11.12.3 on. Affects: java.

**Status:** will break (catalog: certain).

**How to find it:** automatic, by a pattern search over the app's code; detection confidence high.

**Fix:** Send the M2EE admin password Base64-encoded in an X-M2EE-Authentication header on every call to a development servlet.

**Source quotes:**

- "Requests to servlets registered via `Core.addDevelopmentServlet` now require authentication." ([Studio Pro 11.12 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.12/))
