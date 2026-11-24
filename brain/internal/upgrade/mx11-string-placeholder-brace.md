---
title: "Mx11: Curly braces in placeholder text must be escaped with an extra opening brace"
topic: upgrade
keywords: ["placeholder text curly braces", "escaped opening brace", "placeholder {Name}", "{{Name", "Mx11 placeholder", "string placeholder escape", "curly brace escaping", "placeholder formatting", "MX11-STRING-PLACEHOLDER-BRACE", "brace literal", "placeholder text escape", "Mendix 11.6.1 placeholder"]
domain: [upgrade]
kind: pitfall
applies_to: mendix-general
versions: "11.6.1 and later"
layer: field
sources:
  - {title: "Studio Pro 11.6 release notes", url: "https://docs.mendix.com/releasenotes/studio-pro/11.6/", date: "2026-09-15"}
  - {title: "Studio Pro 11.7 release notes", url: "https://docs.mendix.com/releasenotes/studio-pro/11.7/", date: "2026-09-15"}
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed

---
**What changes:** Curly braces in placeholder text must be escaped with an extra opening brace. Category: behaviour change. Severity in the catalog: medium.

**Applies:** from Mendix 11.6.1 on. Affects: widget.

**Status:** will break (catalog: certain).

**How to find it:** manual review (cannot be detected automatically); detection confidence low.

**Fix:** In text box placeholder text, double the opening brace so a literal {Name} becomes {{Name}.

**False positives:** The strings table has no placeholder StringContext; its brace-bearing rows are log, validation and message texts, which this change does not affect. Detecting it via braces in strings would report hundreds of irrelevant rows, so it ships as an advisory instead.

**Source quotes:**

- "Curly braces in a [placeholder text] (for example, `{Name}`) must now be escaped with an extra opening curly brace" ([Studio Pro 11.6 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.6/))
- "Curly braces in a placeholder text (for example, `{Name}`) must now be escaped with an extra opening curly brace" ([Studio Pro 11.7 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.7/))
