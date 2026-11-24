---
title: "Mx11: Cookies lose the secure attribute under forwarded-proto/scheme headers"
topic: upgrade
keywords: ["cookies secure attribute", "X-Forwarded-Proto header", "X-Forwarded-Scheme header", "reverse proxy cookies", "cookie security", "MX11-SECURITY-COOKIE-SECURE-ATTR", "forwarded proto http", "load balancer https", "cookie attribute loss", "Mendix 11.3"]
domain: [upgrade, security]
kind: pitfall
applies_to: mendix-general
versions: "11.3.0 and later"
layer: field
sources:
  - {title: "Studio Pro 11.3 release notes", url: "https://docs.mendix.com/releasenotes/studio-pro/11.3/", date: "2026-09-19"}
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed

---
**What changes:** Cookies lose the secure attribute under forwarded-proto/scheme headers. Category: behaviour change. Severity in the catalog: high.

**Applies:** from Mendix 11.3.0 on. Affects: project.

**Status:** will break (catalog: certain).

**How to find it:** manual review (cannot be detected automatically); detection confidence medium.

**Fix:** If running behind a reverse proxy/load balancer that sets X-Forwarded-Proto or X-Forwarded-Scheme, verify it correctly reports https, or cookies will be issued without the secure attribute.

**Source quotes:**

- "When either the `X-Forwarded-Proto` or `X-Forwarded-Scheme` header is set to `http`, cookies will now be set without the `secure` attribute" ([Studio Pro 11.3 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.3/))
