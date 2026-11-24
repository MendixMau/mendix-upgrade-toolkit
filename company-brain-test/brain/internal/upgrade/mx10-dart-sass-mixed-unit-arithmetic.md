---
title: Mx10 Dart Sass rejects LibSass-era mixed-unit arithmetic (CE6093)
topic: upgrade
domain: [ux-ui]
kind: pitfall
applies_to: mendix-general
versions: "Mx9 -> Mx10+"
keywords: ["CE6093", "Dart Sass", "LibSass", "mixed-unit arithmetic", "SCSS compilation error", "calc()", "division operator", "upgrade Mx9 Mx10", "Sass variables", "math.div()"]
layer: field
sources:
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed
---
**Symptom**
- CE6093 SCSS compilation error after converting to Mx10.

**Root cause**
- Mx10 moved from LibSass to Dart Sass, which is stricter:
  - mixed-unit math without `calc()` fails, e.g. `$font-size-default + 2px` where the variable is in `rem`;
  - the `/` division operator (`58px / 2`) is deprecated.

**Fix**
- Wrap the expression in `calc()` and interpolate variables with `#{}`:
```scss
// before
height: 3 * $font-size-default + 2 * $spacing-small;
// after
height: calc(3 * #{$font-size-default} + 2 * #{$spacing-small});
```
- For division, pre-compute (`58px / 2` → `29px`) or use `math.div()`.
- Pay special attention to custom module SCSS written for LibSass.

**Status**
- Workaround: rewrite the SCSS for Dart Sass as shown above. An upgrade triage checklist lists this as a known Mx9 → Mx10 breaking change.
