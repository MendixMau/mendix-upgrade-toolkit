---
title: SSO starter apps hide the local login form behind a link
topic: upgrade
kind: pitfall
applies_to: OIDC SSO
versions: "10.24 to 11.12"
keywords: ["login", "SSO", "Show alternative login", "walk"]
layer: public
sources:
  - upgrade field run (see Field evidence)
confidentiality: public
status: draft-unreviewed
slug: sso-starter-apps-hide-local-login-form
---

# SSO starter apps hide the local login form behind a link

**From:** learnings sweep of the weekend field runs
**Date:** 2026-11-24
**Kind:** pitfall
**Upgrade:** 10.24 to 11.12
**Field evidence:** SITS field run, basewalk and journeys.
**Proposed target:** company brain (module and version fact), not steps/

---

## Symptom

On an app with OIDC SSO the sign-in page shows only the SSO button; the local form appears after "Show alternative login". Every generated walk failed to log in, and the generated sign-out journey waited for a selector that the folded page does not have.

## Root cause

The walk assumed the form is on the page when it loads.

## Fix

Reveal the alternative form before filling it, and give the sign-out journey a ready selector that exists on the folded page. Fixed in the toolkit; apps with SSO should be expected to need it.

## Status

draft-unreviewed
