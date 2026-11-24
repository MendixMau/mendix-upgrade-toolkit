---
title: Mx10.24 changed generated widget HTML IDs, breaking ID-based CSS and test selectors
topic: upgrade
domain: [ux-ui, testing]
kind: pitfall
applies_to: mendix-general
versions: "Mx10.24"
keywords: ["Mx10.24 widget ID changes", "mxui_widget ID format", "CSS selector broken", "test selector broken", "widget HTML ID", "Playwright selector", "Selenium selector", "CSS #mxui_", "generated widget IDs", "widget ID prefix", "numeric suffix removed", "layout widget prefix"]
layer: field
sources:
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed
---
**Symptom**
- CSS rules or Playwright/Selenium tests that target IDs like `#mxui_widget_TextBox_1_2` stop matching.

**Root cause**
- Per the source, 10.24 removed the numeric suffix (`mxui_widget_TextBox_1_2` → `mxui_widget_TextBox`).
- It also added an `l` prefix for layout widgets and a `p` prefix for page widgets.

**Fix**
- Search custom SCSS, JS and tests for `#mxui_` / `#widget_`.
- Never target Mendix-generated HTML IDs in CSS or tests. They change across versions and even across page renders.

**Status**
- Described only in an upgrade triage checklist. The sources contain no release note or field verification.
