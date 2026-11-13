# Legacy widget conversion, FSM 11.12.7 (React client)

Generator: `convert_legacy.py model-dump.json convert-legacy.mdl [--gaps g.json] [--notes n.json]` (deterministic, same output on every run).
Script: `convert-legacy.mdl` (368 `ALTER PAGE/SNIPPET { REPLACE ... }` statements, `mxcli check -p` clean, `exec --continue-on-error`: 0 failed).
Result: `conv-app/` (script applied, then `mx update-widgets`), `check-after-convert.txt` and `.json` (mx check, the json names the document).

## Result of mx check

| Code | Baseline (check-react-on) | After | What is left |
|---|---|---|---|
| CE0582 | 160 | 13 | 12 x dynamic image (7 widgets, 6 snippets/pages), 1 x static image in building block `FSM_Specific.Grid_Card` |
| CE9900 | 16 | 0 | |
| CE6086 | 6 | 1 | template grid in building block `FSM_Specific.Templategrid_Grid` (the 6 on pages: 5 were native or excluded units, 1 page converted to a gallery) |
| CE0572 | 12 | 1 | same building block template grid. The other CE0572 items belong to the main session |
| CE6912 | 1 | 0 | gone in the current react-app copy (main session) |
| CE0117 | 0 | 1 | `General.ACT_LoginContext_SignIn`, parameter `UseAuthToken`. Not from this script (login widgets, main session) |
| New error types from the conversion | | 0 | all fixed during iteration (see lessons) |

Total: 20 errors after the first full run, 16 now (13 CE0582, 1 CE6086, 1 CE0572, 1 CE0117).

Reason for the building block leftovers: mxcli has no ALTER for BUILDINGBLOCK or PAGETEMPLATE. Both stay.

## Counts per widget type

| Legacy widget | Found (web, not excluded) | Converted | Became |
|---|---|---|---|
| DataGrid | 152 | 152 | DATAGRID (DG2) |
| ReferenceSetSelector | 3 | 3 | DATAGRID over the association |
| ReferenceSelector | 121 | 121 | COMBOBOX |
| InputReferenceSetSelector | 14 | 14 | COMBOBOX |
| DropDown | 39 | 39 | COMBOBOX |
| StaticImageViewer | 32 | 32 | IMAGE |
| DynamicImageViewer | 7 | 0 | gap |
| TemplateGrid | 1 | 1 | GALLERY (the popup menu inside was dropped) |

Skipped on purpose: 66 native pages, 44 native snippets, 17 native layouts (legacy widgets are valid on native, converting them gave 157 CE6089 and 104 CE6083), 9 excluded units.
Search fields converted to column filters: 353 text, 132 date, 110 drop-down, 47 number. 54 needed an extra hidden column to host the filter. CE9900: 22 select-page bindings removed (pages stay).

## What each control bar button became

| Control bar item | Outcome | Count |
|---|---|---|
| Action button that acts on the selected row (object parameter, page, delete) | action column button on `$currentObject` | 153 |
| Action button with a list parameter | button above the grid on `$grid` selection, grid gets `Selection: Multi` | 30 |
| Action button with no selection needed (New and the like) | ACTIONBUTTON above the grid, wrapped in `<grid>_wrap` | 18 |
| Search button | dropped, column filters are always visible | 117 |
| Select button (selection pages) | dropped | 17 |
| Select all / deselect all | dropped (gap) | 3 |
| Export to Excel | dropped (gap) | 2 |
| Default button | grid `OnClick` (double click kept). With a list parameter: no row click, button above stays (gap) | 8 gaps |

Unmapped parameters of the grid entity are made explicit, as the classic grid did implicitly (11).

## GAPS (nothing dropped silently, 63 entries in the gaps json)

| Gap | Count | Why / what to do |
|---|---|---|
| Dynamic image kept as is | 7 | IMAGE object binding cannot be written in MDL. These are the 13 CE0582 left. Options: URL based IMAGE with a `/file?guid=` expression, or hand conversion in Studio Pro |
| Search field dropped, association path runs against the owner side | 29 | DG2 attribute paths cannot go child to parent (CE7247). Filter by other columns or add a microflow/XPath filter |
| Default (double click) action takes a list | 8 | `OnClick` cannot pass a list. The button above the grid stays |
| Enumeration column shown as image | 8 | shown as text |
| Association drop-down search field | 13 notes, 3 gaps | approximated by a text filter, options XPath and multi select lost |
| Select all / export buttons | 5 | DG2 header checkbox and its own export |
| Button icon | 2 | dropped |
| Popup menu inside template grid | 1 | `Dashboard.Grids`, dropped |
| Translations | all converted captions | only the default language (en_US) is written. 2237 of 2285 texts had nl_NL as well. nl_NL is checked (CheckCompleteness true) but mx check reports nothing. Restore with `CREATE OR MODIFY TRANSLATIONS` as a follow-up |
| Date and number formats | all | classic column formatting (date format, decimals) not carried over |
| Design properties without a place on the new widget | 8 | on the gallery containers |

## mxcli bugs and missing features

| # | Command | Message / behaviour | Workaround |
|---|---|---|---|
| M1 | `ALTER BUILDINGBLOCK` / `PAGETEMPLATE ... REPLACE` | not available | gap (2 building blocks) |
| M2 | `REPLACE x WITH { DYNAMICIMAGE ... }` and `IMAGE` | no MDL way to write the Image widget object source; DYNAMICIMAGE still gives CE0582 | gap |
| M3 | `ALTER PAGE ... REPLACE w WITH { COMBOBOX ... Attribute: Assoc }` for a combo box outside a recognised data view | `names no object for association` | write `$Var.Assoc` (needed for 2 widgets, now in native pages that are skipped) |
| M4 | COMBOBOX association mode without `DataSource` | falls back to enumeration mode, CE1613 | always emit DataSource |
| M5 | `DROPDOWNFILTER` written by mxcli | CE0463 "definition of this widget has changed" on 3 pages | `mx update-widgets` (MPR v1 project, no mprcontents). `mxcli widget sync` is documented as partial |
| M6 | COMBOBOX `CaptionAttribute:` for a non-String attribute | CE7247 "Only attributes of type String" | `optionsSourceAssociationCaptionType: expression, optionsSourceAssociationCaptionExpression: 'getCaption($currentObject/X)'`. `CaptionExpression:` and `CaptionType:` are rejected (MDL-WIDGET01) |
| M7 | IMAGE with Atlas design properties (`Size`, `Shape`, `Center`) | MDL-WIDGET11 | dropped. `Spacing` must be written `'Spacing': ('margin-right': 'M')` with parentheses (brackets give DEPR125) |
| M8 | DROPDOWNFILTER `defaultValue: true` | MDL-WIDGET49 (Boolean not accepted) | write `'''true'''` |
| M9 | `mxcli exec` on a REPLACE of a grid with `[%CurrentObject%]` inside `DATABASE FROM $x/Assoc` | mx check CE1161 / CE1152 | use the source variable in the XPath, a data view that listens needs `$currentObject`, not `$gridN` |
| M10 | `mxcli exec` speed | about 0.8 s per ALTER, 368 statements in 4.7 min | none |
| M11 | `mx check` | messages carry no document name | `mx check app.mpr -j out.json` has `document-name` and `element-name` |

## Lessons and decisions to know

| Topic | Decision |
|---|---|
| ReferenceSetSelector | converted to a DATAGRID over the association (my choice) |
| Association navigation | the generator reads parent/child/owner from the dump and drops a path that runs against the owner (the legacy grid allowed it) |
| Listening data views | `SET (DataSource: SELECTION grid) ON dataViewN` appended, the listened grid gets `Selection: Single`. Verified with `describe` on `Form.Form_Overview` |
| DATABASE FROM with `[%CurrentObject%]` | replaced by the source variable (1 case, `Ticket_View`) |
| Nanoflow data view source | entity taken from the nanoflow return type (needed for `Part_View` grid) |
| CE6086 | in this app it is "Template grids are not allowed on web pages", not a validation message. Handled by converting the template grid to a gallery |
| `mx update-widgets` | run once on `conv-app` to clear CE0463. It touches every widget in the app, so check the diff before using on the real app |

## Files

- `convert_legacy.py`, `convert-legacy.mdl`, `check-after-convert.txt`, `check-after-convert.json`, `CONVERT-REPORT.md`
- `conv-app/` scratch copy (not committed anywhere, react-app untouched)
