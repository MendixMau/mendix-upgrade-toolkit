---
title: Xcode duplicate symbols linker error after upgrading to 9.24
topic: upgrade
domain: [native-mobile]
kind: pitfall
applies_to: mendix-general
versions: "Mx9.24+ native (Native Template 7)"
keywords: ["duplicate symbols linker error", "Xcode build fails", "duplicate symbols architecture", "Linker command failed exit code 1", "DEAD_CODE_STRIPPING", "9.24 upgrade native", "React Native 0.70", "Native Template 7"]
layer: field
sources:
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed
---
**Symptom**
- The native iOS build fails with `duplicate symbols for architecture x86_64` / `Linker command failed with exit code 1`.

**Root cause**
- Not stated. It appeared with the 9.24 upgrade (React Native 0.70, Native Template 7).

**Fix**
- In Xcode, set `DEAD_CODE_STRIPPING = YES` on the `nativeTemplate` target for all three build types.
- Debug matters because local builds always use Debug unless you archive an .ipa.

**Status**
- Workaround (from one field write-up). Root cause and permanent fix unknown.

**Release notes**
- 9.24.0: React Native 0.70.7; Native Template 7.0.0 required (https://docs.mendix.com/releasenotes/studio-pro/9.24/#9240)
