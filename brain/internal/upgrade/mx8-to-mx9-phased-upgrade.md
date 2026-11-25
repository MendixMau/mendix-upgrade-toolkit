---
title: Three-phase Mx8 to Mx9 upgrade through the latest Mx8 MTS
topic: upgrade
domain: [delivery-process]
kind: procedure
applies_to: company-standard
versions: "Mx8 -> Mx9"
keywords: ["Mx8 to Mx9 upgrade", "three-phase upgrade", "MTS module upgrade", "domain model settings wiped", "module configuration capture", "deprecation warnings", "latest 8 MTS", "Atlas 2 to Atlas 3", "Hybrid profile deprecated", "userlib JARs", "predictable upgrade effort"]
layer: field
sources:
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed
---
**When**
- An Mx8 app goes to Mx9.
- The documented flow (upgrade the app, then all modules, then fix errors) gave a customer a long, unmeasurable error-fixing phase.
- In that case, module upgrades wiped domain model settings.
- Module upgrade steps also needed UI access (for example, deep link) after the app upgrade.

**Steps**
1. List the modules needed for Mx9. Order them from least to most dependent.
2. Sort them into three groups:
   - must be upgraded for the latest Mx8 MTS;
   - one version works on both Mx8 and Mx9;
   - the rest, which get upgraded twice.
   - Tip: read the v9 module notes first. They often name the right v8-compatible version.
3. Review: run, test, and fix deprecation warnings on the current Mx8 version.
4. Capture each module's configuration: UI, constants, microflows, domain model security.
5. Upgrade the app to the latest 8 MTS/LTS (the source names 8.18.13 at the time).
6. Upgrade modules. Clear their userlib JARs first. Then re-apply the captured configuration.
7. Run and fix compile errors and deprecations.
8. Back up. Convert in place to the latest 9 MTS, or the 9 LTS if the platform is already on 10+.
9. Upgrade modules and widgets. Run and review between each one.
10. Re-configure modules, review, and commit.
11. Deploy. Re-apply constants on the deployed app and confirm in test.

**Checks**
- Run and review between every module group and every phase.

**Watch out**
- Do not upgrade modules that already work on v9.
- Version dependencies may force several modules to be upgraded together.
- This approach can take longer on average, but the effort is more predictable.
- Atlas 2 → 3 is optional for Mx9 but recommended: many Mx9 Marketplace widgets do not work correctly with Atlas 2, or need customization. Atlas 3 has a different file/folder structure. See [[mx7-to-mx9-styling-migration]].
- The Hybrid profile is deprecated in Mx9.
- [[mx9-uniqueness-violation-check-and-cleanup]]
