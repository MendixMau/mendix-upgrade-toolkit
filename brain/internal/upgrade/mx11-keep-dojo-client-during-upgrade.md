---
title: Keep the Dojo client when upgrading to Mx11; switch to React as a separate project
topic: upgrade
domain: [ux-ui, delivery-process]
kind: decision
applies_to: company-standard
versions: "Mx10.24 -> Mx11 (before Mx12)"
keywords: ["Mx11 upgrade", "Dojo client", "React client migration", "Mendix UI", "Dojo deprecated", "Mx12 removal", "legacy widgets", "clientModule", "widget replacement", "SCSS import", "glyphicon", "DOM changes"]
layer: field
sources:
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed
---
**Status:** Seen in one upgrade run (10.24 -> 11.9.1, Dojo). Whether the app started is unknown.

**Rule**
- Existing Mx10 apps stay on the Dojo client for the Mx11 version upgrade.
- Plan the switch to the React client (Mendix UI) as its own project before Mx12.

**Why**
- Per the sources, Dojo is deprecated in Mx11 but supported for the whole Mx11 line (until Mx11.24). Removal is planned for Mx12.
- Staying on Dojo avoids DOM, class-name and selector changes. React 19 (since 11.6) applies only to the React path.
- Measured on 11.9.1 (Dojo):
  - legacy `clientModule` widgets still worked (HTMLSnippet 3.9.7, MicroflowTimer 4.0.3, ShowByCondition 1.4.0, URLRedirector 1.1);
  - SCSS `@import` gave warnings only.
- The plan estimated ~2 h for the Dojo path. Switching would add 1–3 days of CSS regression work, or a 2–5 day UI project.

**How to apply**
- Log legacy widgets, `@import` usage, `>` selectors and glyphicon usage as backlog for the React switch.
- Do not trust the 2 h estimate. The real run hit 45 Java errors ([[mx11-java-api-rewrites]]), and whether the app started was not recorded.
