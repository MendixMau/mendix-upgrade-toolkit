---
title: "Upgrade catalog: Marketplace module advisories for Mendix 11"
topic: upgrade
keywords: ["Mendix 11 upgrade", "Marketplace modules", "OIDC SSO", "Mendix SSO deprecated", "SAML LDAP", "Deep Link deprecated", "Atlas 4", "React 19", "module compatibility", "minimum versions"]
domain: [upgrade]
kind: reference
applies_to: mendix-general
versions: "10.x -> 11.x"
layer: field
sources:
  - {title: "Upgrading from Mendix Studio Pro 10 to 11", url: "https://docs.mendix.com/refguide/upgrading-from-10-to-11/", date: "2026-09-16"}
  - {title: "OIDC SSO", url: "https://docs.mendix.com/appstore/modules/oidc/", date: "2026-09-16"}
  - {title: "Deep Link", url: "https://docs.mendix.com/appstore/modules/deep-link/", date: "2026-09-16"}
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed

---
**General:** Upgrade Marketplace modules and widgets before moving to Mendix 11, choosing releases compatible with both the latest Studio Pro 10 and the target 11 version. Upgrade in place: do not remove and re-import a module unless its own release notes tell you to, because that can discard data and configuration tied to the component.

**React 19:** Studio Pro 11.6.0 moves the React client to React 19. Upgrade every installed widget to its latest published version as part of that step, not after it.

**No minimum-version thresholds:** the catalog deliberately carries none, because docs.mendix.com does not publish Mendix 11 minimum versions per module. For minimum versions use the module files under `baseline/versions/modules/`.

**Modules:**

- **Mendix SSO** (deprecated): Mendix SSO is deprecated as of 1 May 2026 and is scheduled for removal from the public Marketplace on 1 November 2026. Plan a move to SAML or LDAP. This is a lifecycle deadline rather than a Mendix 11 breakage: the module does not stop working on upgrade, but it will stop being available. Replacement: SAML or LDAP.

- **Deep Link** (deprecated): Replace deep-link routing with built-in page URLs, or microflow URLs where a microflow has to run first. To keep existing links working, set the URL prefix to the prefix the module used so the old addresses still resolve. Replacement: Page URLs and microflow URLs. Catalog entry MX11-MODULE-DEEP-LINK-DEPRECATED.

- **Atlas Core** (advisory): Moving from Atlas 3 to Atlas 4 is optional in Mendix 11; the change is SASS variables to CSS variables, and Atlas 4 remains backwards compatible with apps still using SASS variables. If you do migrate, upgrade Atlas Web Content too, and watch for UI modules still reading old Atlas SASS variables -- those usages silently fall back to Atlas defaults rather than failing. Replacement: Atlas 4. Catalog entry MX11-MODULE-ATLAS-4.
