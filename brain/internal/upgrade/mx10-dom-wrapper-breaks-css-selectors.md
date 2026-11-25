---
title: Mx10 data-widget-wrapper div and reference selector class move break custom CSS selectors
topic: upgrade
domain: [ux-ui]
kind: pitfall
applies_to: mendix-general
versions: "Mx9 -> Mx10; fixed for Atlas with Atlas Core >= 3.11"
keywords: ["data-widget-wrapper CSS break", "reference selector class move", "Mx10 upgrade CSS", "list-view table break", "data view layout break", "glyphicon override Mx10", "mx-referenceselector move", "mx-compound-control wrapper", "DOM structure change Mx10", "child selector break", "Atlas Core 3.11"]
layer: field
sources:
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed
---
**Symptom**
- After upgrading to Mx10:
  - list-view tables break because of the extra DOM wrapper;
  - data view layouts with actions break (for example, rules like `.mx-window-body > .mx-placeholder > .mx-dataview > …`);
  - glyphicon overrides may need updating;
  - reference selector styling silently stops applying. In one app, `.mx-referenceselector.form-group` may have been broken since the Mx10 upgrade. A visual check is still pending.

**Root cause**
- A React widget inside a Dojo container now gets a `div[data-widget-wrapper]` (`display: contents`).
- This may affect CSS that relies on direct child (`>`), sibling (`+`) or `nth-child` selectors.
- `.mx-referenceselector` and `.mx-referencesetselector` are no longer on the widget root. They only work as nested classes (e.g. `.mx-referenceselector-input-wrapper`).
- A new `.mx-compound-control` wraps the input and button group.
- Icons in Atlas and widgets moved to the new Atlas icon set, which uses new class names.

**Fix**
- Atlas apps: upgrade Atlas Core to 3.11 or higher.
- Custom themes: use descendant selectors (`.panel .mx-dataview`) instead of `>`.
- Style reference selectors via `.mx-compound-control` or the nested classes.
- Check CSS that targets glyphicon classes against the latest widget markup.

**Status**
- Seen in one reference app upgrade (list-view tables, data view layout).
- Fix for Atlas apps: Atlas Core 3.11+, per the Mx9 → Mx10 upgrade docs.
- A Datagrid 2 data error found in the same run was unresolved.
- Mx11 (Dojo client): unknown whether direct child selectors are broken. This still needs a visual smoke test.

**Release notes**
- 10.0.0: DOM structure change and new Atlas icons (Atlas Core 3.11.0) (https://docs.mendix.com/releasenotes/studio-pro/10.0/#1000)
