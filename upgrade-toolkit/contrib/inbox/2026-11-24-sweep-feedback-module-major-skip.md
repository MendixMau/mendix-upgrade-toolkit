---
title: A feedback module major version is skipped in a plan
topic: upgrade
kind: pitfall
applies_to: FeedbackModule
versions: "10.24 to 11.12"
keywords: ["FeedbackModule", "major version", "plan"]
layer: public
sources:
  - upgrade field run (see Field evidence)
confidentiality: public
status: draft-unreviewed
slug: feedback-module-major-skip
---

# A feedback module major version is skipped in a plan

**From:** learnings sweep of the weekend field runs
**Date:** 2026-11-24
**Kind:** pitfall
**Upgrade:** 10.24 to 11.12
**Field evidence:** RMS field run, plan rows. Hypothesis, not proved.
**Proposed target:** company brain (module and version fact), not steps/

---

## Symptom

A plan that moves the feedback module from 4.1.1 to 5.0.0 changes the module's own entities and nanoflows; the field run kept 4.1.1 and noted it as a held module.

## Root cause

Hypothesis: the major step changes what the design-module snippet expects (see the neighbouring note).

## Fix

Plan the feedback module with the design module, not apart from it; keep it at its version when no snippet needs the newer nanoflows.

## Status

draft-unreviewed
