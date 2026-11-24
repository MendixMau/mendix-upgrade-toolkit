---
title: A newer design module snippet needs a feedback module the app never installed
topic: upgrade
kind: pitfall
applies_to: Atlas_Core
versions: "10.24 to 11.12"
keywords: ["Atlas_Core", "FeedbackModule", "CE1613"]
layer: public
sources:
  - upgrade field run (see Field evidence)
confidentiality: public
status: draft-unreviewed
slug: design-module-snippet-needs-feedback-module
---

# A newer design module snippet needs a feedback module the app never installed

**From:** learnings sweep of the weekend field runs
**Date:** 2026-11-24
**Kind:** pitfall
**Upgrade:** 10.24 to 11.12
**Field evidence:** SNOW field run, update and build steps.
**Proposed target:** company brain (module and version fact), not steps/

---

## Symptom

Atlas_Core 4.3.x to 4.7.0 ships a snippet whose Feedback widget calls a nanoflow in FeedbackModule; the app has no such module, so the build stops with CE1613 (nanoflow no longer exists) while triage said the replacement was clear.

## Root cause

The widget id belongs to the design module, the nanoflow to another module; triage reads the first only.

## Fix

Install the feedback module from the Marketplace at the version the snippet expects, commit, and write the widget-skew ack because the skew check still calls the widget a skew. SW-3 in FEEDBACK.md proposes install-on-plan.

## Status

draft-unreviewed
