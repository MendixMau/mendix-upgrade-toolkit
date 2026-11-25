---
title: Clean userlib before and after each Marketplace module update (pre-managed-deps)
topic: upgrade
domain: [delivery-process]
kind: procedure
applies_to: company-standard
versions: "Mx7 -> Mx11, apps not yet on managed dependencies"
keywords: ["userlib cleanup", "Marketplace module update", "JAR management", "RequiredLib", "vendor dependencies", "pre-managed-deps", "duplicate libraries", "Java imports", "userlib outdated JARs", "library version mismatch"]
layer: field
sources:
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed
---
**Status:** Field best practice (steps 1–5). Steps 3, 6 and 7 come from a Mx9 → Mx10 triage checklist and one Mx11 upgrade run. The SAML and OIDC SSO release notes require deleting old userlib JARs before upgrading.

**When**
- Updating a Marketplace module whose JARs live in `userlib`.

**Steps**
1. Before the update, delete JARs whose only `.RequiredLib` file belongs to the module being updated.
   - Keep any JAR that has RequiredLib files from several modules.
2. Update the module in Studio Pro.
3. Check that the `userlib` JARs match what the new Java source imports. Use the module release notes or the imports in `javasource/<module>/`.
   - A Mx9 → Mx10 triage checklist says Marketplace module upgrades replace Java source but do not update the JARs in `userlib`. See [[community-commons-pdfbox3-userlib-mismatch]].
4. Re-check `userlib` for duplicates or multiple versions. Keep the latest and delete the rest.
5. Watch for the same library under different names, for example `commons.io-<v>.jar` and `org.apache.commons.io-<v>.jar`.
6. For any JAR you add by hand, create `<jar>.RequiredLib`. Its content is the owning module name, e.g. `CommunityCommons`.
7. Delete stale `.RequiredLib` markers whose JAR is gone. One app had 7. They are harmless at runtime but clutter `userlib`.

**Checks**
- Exactly one version of each library remains.
- No duplicates with `vendorlib`.

**Watch out**
- Keep customizations in a separate module so updates stay clean.

**Release notes**
- The SAML and OIDC SSO module notes repeatedly require deleting old userlib JARs before upgrading. Examples:
  - OIDC SSO 4.2.0 (https://marketplace.mendix.com/link/component/120371)
  - SAML 3.6.25 (https://marketplace.mendix.com/link/component/1174)
