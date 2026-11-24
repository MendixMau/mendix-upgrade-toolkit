---
title: A missing Data Widgets module makes a grid filter lose five settings
topic: upgrade
kind: pitfall
applies_to: Data Widgets
versions: "10.24"
keywords: ["widgetdrop", "Data Widgets", "grid filter"]
layer: public
sources:
  - upgrade field run (see Field evidence)
confidentiality: public
status: draft-unreviewed
slug: data-widgets-missing-widgetdrop-grid-filter
---

# A missing Data Widgets module makes a grid filter lose five settings

**From:** learnings sweep of the weekend field runs
**Date:** 2026-11-24
**Kind:** pitfall
**Upgrade:** 10.24
**Field evidence:** ERRH field run, update step rung 1.
**Proposed target:** company brain (module and version fact), not steps/

---

## Symptom

The update step stops (exit 13, widgetdrop): one grid filter loses 5 settings because the Data Widgets module is not installed in the app. The ack file would accept the loss.

## Root cause

The widget that carries the settings is part of the Data Widgets module; without it the converter has no definition to keep them in.

## Fix

Install a newer Data Widgets (3.11.10 worked) from the Marketplace with `mxcli marketplace download` and `install --file`, then rerun from update: the stop cleared with no ack. Screens then re-hash: four pairs needed to be looked at again.

## Status

draft-unreviewed
