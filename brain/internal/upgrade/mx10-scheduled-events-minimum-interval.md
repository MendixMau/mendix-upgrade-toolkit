---
title: Mx10 scheduled events have a 1-minute minimum interval
topic: upgrade
domain: [architecture, delivery-process]
kind: pitfall
applies_to: mendix-general
versions: "Mx9 -> Mx10+"
keywords: ["scheduled event", "minimum interval", "sub-minute", "1 minute", "non-recurring", "Core.schedule", "Mx9 to Mx10 upgrade", "microflow scheduled event", "migration", "cron scheduler"]
layer: field
sources:
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed
---
**Symptom**
- Processes that relied on sub-minute scheduled events cannot be modeled that way in Mx10.
- Non-recurring scheduled events are no longer supported.

**Root cause**
- Mx10 enforces a minimum scheduled event interval of 1 minute. The public migration guide does not mention this.

**Fix**
- First question whether you really need that frequency. Refactor if you can.
- Otherwise, a scheduled event can call Java that runs a microflow repeatedly within the minute using `Core.schedule`. The AAA team can help.
- A lightweight cron-based scheduler, inspired by Microflow Scheduled Event Manager, is another option.
- Do not use that module itself; it is deprecated and Quartz-based.

**Status**
- Confirmed. This is a platform behavior.

**Release notes**
- 10.0.0: legacy (non-repeating / start-time) scheduled events are removed; the runtime fails to start if any exist (https://docs.mendix.com/releasenotes/studio-pro/10.0/#1000)
