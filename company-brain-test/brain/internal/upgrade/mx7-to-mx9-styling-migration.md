---
title: Migrating custom styling from Mx7 to Mx9 via 7.23.4 and 8.18
topic: upgrade
domain: [ux-ui, delivery-process]
kind: procedure
applies_to: company-standard
versions: "Mx7 -> 7.23.4 -> 8.18.x -> 9.18.x"
keywords: ["Mx7 to Mx9 upgrade", "custom styling migration", "Atlas UI upgrade", "theme migration", "styling compilation error", "CSS not applied", "login page unstyled", "Atlas Core", "variables.scss", "themesource", "SASS compiler", "Atlas 1.2.4"]
layer: field
sources:
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed
---
**When**
- An Mx7 app with a custom theme goes to Mx9.
- If you did not build the original styling, first judge whether a fresh Atlas Core restyle is faster. It often is:
  - Atlas already covers much of what Mx7 customers hand-wrote.
  - Expect to shrink spacing and typography.
  - Heavy inline styling makes migration harder.

**Steps**
1. Arrange a developer for the Mendix errors that will come up.
2. Set up a data snapshot. It is the only way to test page UI.
3. Get the installers: 7.23.4, 8.18.22, and 9.18.x. Also get the Calypso SASS compiler for Mx8.
4. Before following the docs, rename `theme` to `theme_oldest`. Reuse its files later in a custom UI module's `themesource`.
5. Note the version: Mx7.8 and older ships Atlas v1, which has a different folder structure.
6. Upgrade to 7.23.4. You need a non-SSO password if the app is still below that.
7. Create a sandbox branch that includes the snapshot.
8. Create a `CustomTheme` module. Move custom styles, images and layouts out of `AtlasUI_Resources` into it.
9. Install Atlas 1.2.4. This avoids DOM errors when moving to Atlas 2.
10. Open the branch in 8.18.22 and commit with errors. Install Atlas 2 and fix the errors.
    - Java action errors usually go away after updating Community Commons, Model Reflection, Deep Link and SAML.
11. Open the branch in 9.18.x and commit with errors. Then:
    - update all Marketplace modules;
    - move custom styling out of Atlas UI;
    - rename `Atlas_UI_Resources` to `Atlas_Core`;
    - extract the Atlas 3 `theme.zip` to the app root;
    - install Atlas Core, Atlas Web Content and Atlas Native Content.

**Checks**
- Styling compiles and the login page is styled.

**Watch out**
- CSS not applied:
  - Keep the Mx9 `index.html`. The Mx7 one breaks the stylesheet import.
  - Wire all partials into the custom `main.scss`.
  - Make `Atlas_Core` and `Atlas_Web` use your `variables.scss`.
- No styling from other UI modules: make `theme/web/settings.json` contain only `{"cssFiles": ["theme.compiled.css"]}`.
- Login page unstyled:
  - Carry over Mx7 `login.css` into themesource and reference it from `login.html`.
  - Add any bootstrap includes it used.
