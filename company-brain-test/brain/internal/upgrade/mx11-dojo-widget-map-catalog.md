---
title: "Upgrade catalog: Dojo widget to React replacement map"
topic: upgrade
keywords: ["Dojo widget", "React replacement", "Data Grid 2", "Gallery", "Combo Box", "batch convert", "widget conversion", "Mendix 10 to 11", "upgrade", "Reference Selector", "Template Grid"]
domain: [upgrade, ux-ui]
kind: reference
applies_to: mendix-general
versions: "10.x -> 11.x"
layer: field
sources:
  - {title: "Mendix React Client", url: "https://docs.mendix.com/refguide/mendix-client/react/", date: "2026-09-16"}
  - {title: "Widget conversion limitations", url: "https://docs.mendix.com/refguide/mendix-client/widget-conversion-limitations/", date: "2026-09-16"}
  - {title: "Batch conversion of widgets", url: "https://docs.mendix.com/refguide/mendix-client/batch-conversion/", date: "2026-09-16"}
  - {title: "Marketplace components React client status", url: "https://docs.mendix.com/refguide/mendix-client/marketplace-react-status/", date: "2026-09-16"}
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed

---
| Dojo widget | Replacement | Batch convert | Lost in conversion |
|---|---|---|---|
| Data Grid (`Forms$DataGrid`) | Data Grid 2 | yes | Data Source Wait for Search, Server Side Paging, Show Empty Rows, Column Size in Pixels, Tooltip Page, Paging Bar Without Total Count, Single and Maintain Selection, Select First, Aggregate Caption, Aggregate Function, Editable Columns, Reference Set Columns, Range Search Field, Read-only Search Field, Hidden Search Field with Default Value, Multiple Search Fields for an Attribute, All Rows Variable, Select All Button, Export to CSV Button, Inline Editing |
| Template Grid (`Forms$TemplateGrid`) | Gallery | no | nothing listed |
| Reference Selector (`Forms$ReferenceSelector`) | Combo Box | yes | Go to Page, Screen Reader Caption, 'Required' Validation, 'Custom' Validation, Decimal Precision Formatting, Group Digits Formatting |
| Reference Set Selector (`Forms$ReferenceSetSelector`) | Combo Box | yes | Constrained By, Decimal Precision Formatting, Group Digits Formatting |
| Input Reference Set Selector (`Forms$InputReferenceSetSelector`) | Combo Box | yes | Screen Reader Caption, Constrained By, Decimal Precision Formatting, Group Digits Formatting |
| Drop-down (`Forms$DropDown`) | Combo Box | yes | nothing listed |
| Dynamic Image (`Forms$ImageViewer`) | Image | yes | Height in Percentage |
| Static Image (`Forms$StaticImageViewer`) | Image | yes | Height in Percentage |
| HTML Snippet (`HTMLSnippet.widget.HTMLSnippet`) | HTML Element widget, or a JavaScript action | no | nothing listed |
| JavaScript Snippet (`SnippetJS.widget.SnippetJS`) | JavaScript action | no | nothing listed |

**custom widget:** A custom Dojo widget has to be rebuilt as a React pluggable widget; there is no conversion path and the work requires JavaScript.

**marketplace widget:** For a Marketplace widget, check whether the vendor has published a React-ready release before assuming a rewrite is needed. Mendix maintains a per-component status table.

**batch conversion:** Studio Pro 11.4.0 and above can convert the widgets flagged batch_convert automatically, in bulk. Do this before hand-editing pages, then re-check the settings listed in conversion_loses.
