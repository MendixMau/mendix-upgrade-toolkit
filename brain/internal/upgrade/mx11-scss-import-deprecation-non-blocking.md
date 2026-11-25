---
title: SCSS @import only warns on Mx11 (Dojo); migrate to @use later
topic: upgrade
domain: [ux-ui]
kind: pitfall
applies_to: mendix-general
versions: "Mx10 -> 11.9.1 (Dojo client)"
keywords: ["SCSS @import deprecation", "@import @use migration", "Dart Sass deprecation warning", "SCSS @use", "Mx11 Sass upgrade", "custom-variables import"]
layer: field
sources:
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed
---
**Symptom**
- Dart Sass deprecation warnings for `@import` after converting to Mx11.
- A pre-upgrade stub predicted a hard compile failure. That did not happen.

**Root cause**
- `@import` is deprecated in Dart Sass and will be removed in a future Dart Sass release.
- Almost every module started with `@import '../../../theme/web/custom-variables';`.

**Fix**
- Defer if needed. When ready, per module:
```scss
@use '../../../theme/web/custom-variables' as *;
```
- `as *` drops the namespace, so it behaves like `@import`.
- For Marketplace modules (Atlas Web Content, Data Widgets, third-party), take the vendor update.

**Status**
- Measured: 168 instances across ~45 modules compiled with warnings only on 11.9.1 (Dojo).
- Behavior on the React client or newer Dart Sass is unverified.
