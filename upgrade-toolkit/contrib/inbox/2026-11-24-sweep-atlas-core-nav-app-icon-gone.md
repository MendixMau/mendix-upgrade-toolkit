---
title: Design module update removes the navigation app icon image
topic: upgrade
kind: pitfall
applies_to: Atlas_Core
versions: "10.12 to 10.24"
keywords: ["CE1613", "app icon", "Atlas_Core"]
layer: public
sources:
  - upgrade field run (see Field evidence)
confidentiality: public
status: draft-unreviewed
slug: atlas-core-nav-app-icon-gone
---

# Design module update removes the navigation app icon image

**From:** learnings sweep of the weekend field runs
**Date:** 2026-11-24
**Kind:** pitfall
**Upgrade:** 10.12 to 10.24
**Field evidence:** ERRH field run (10.12.9 to 10.24.13), update and build steps. Hypothesis: the same happens on any design-module major step.
**Proposed target:** company brain (module and version fact), not steps/

---

## Symptom

After the design module Atlas_Core moved from 3.0.x to 3.22.x, mx check reports CE1613 "The selected image ... no longer exists" at the Responsive navigation profile (property App icon). Three more CE1613 for module Administration 4.5.0 list icons of the old Atlas image collection (Atlas_Filled.*).

## Root cause

The new module version drops images the app, or another module, still references by qualified name; the update replaces the image collection, it does not keep the old names.

## Fix

Administration icons: accept the update stop and repoint or replace the images in the build repair (see repair row for CE1613 images moved). App icon: no mxcli clause authors it; clearing the property in the navigation document is the only route found (SW-8 in FEEDBACK.md).

## Status

draft-unreviewed
