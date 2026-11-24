---
title: A 10.6 app does not build on JDK 21; use the JDK 11 image
topic: upgrade
kind: pitfall
applies_to: Mendix runtime
versions: "10.6"
keywords: ["JDK 11", "mxbuild", "Gradle 7.6", "10.6"]
layer: public
sources:
  - upgrade field run (see Field evidence)
confidentiality: public
status: draft-unreviewed
slug: old-10-6-app-needs-jdk-11
---

# A 10.6 app does not build on JDK 21; use the JDK 11 image

**From:** learnings sweep of the weekend field runs
**Date:** 2026-11-24
**Kind:** pitfall
**Upgrade:** 10.6
**Field evidence:** CHK and DVS field runs, baseline step. Fixed generically in the toolkit; kept here as the version fact.
**Proposed target:** company brain (module and version fact), not steps/

---

## Symptom

The old app (10.6.3) fails to build under the default JDK and its repair row for the Java 11 setting (CE2513) ran only for 9.x sources.

## Root cause

mxbuild for 10.6 uses Gradle 7.6, which did not work on JDK 21 in the field run; the runtime image must be JDK 11 as well.

## Fix

Use the Java 11 build image for the baseline build and the runtime of the old app, and keep it for that app alone: a per-run override left set later broke the 10.24 build ("release version 21 not supported").

## Status

draft-unreviewed
