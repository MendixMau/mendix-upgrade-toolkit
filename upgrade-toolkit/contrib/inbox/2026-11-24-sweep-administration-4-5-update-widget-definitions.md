---
title: Administration 4.5.0 update shows CE0463 on 11 widgets, fixed by update-widgets
topic: upgrade
kind: pitfall
applies_to: Administration
versions: "10.24"
keywords: ["CE0463", "update-widgets", "Administration"]
layer: public
sources:
  - upgrade field run (see Field evidence)
confidentiality: public
status: draft-unreviewed
slug: administration-4-5-update-widget-definitions
---

# Administration 4.5.0 update shows CE0463 on 11 widgets, fixed by update-widgets

**From:** learnings sweep of the weekend field runs
**Date:** 2026-11-24
**Kind:** pitfall
**Upgrade:** 10.24
**Field evidence:** ERRH field run, update stops 1 and 2, build repair update-widgets 18 to 0.
**Proposed target:** company brain (module and version fact), not steps/

---

## Symptom

Updating the Administration module to 4.5.0 on a 10.24 app adds 11 CE0463 (widget definition changed) errors.

## Root cause

The module ships newer widget definitions than the widgets the app has; the pages keep the old property sets.

## Fix

Accept the update stop (not keep: a kept module blocks the gate on a kept-ack) and run `mx update-widgets` in the build repair; 18 CE0463 went to 0 in one pass. Unmapped new roles of the module still need a person to map them.

## Status

draft-unreviewed
