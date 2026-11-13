# Rung 3: 11.12.7 Dojo client to React client

Branch `react/rung3` on gated 2d4e0d5 (local, no remote). Commits f1865f1 (React client), 6e21f21 (header fix,
row click selection) bd4a49e (tickets and parts grids back to the Dojo look) and 27d0ca7 (column picker hidden).

## Readiness

67 packages: 62 ready, 5 Dojo packages moved (HTMLSnippet, MicroflowTimer, ShowByCondition, URLRedirector, snippetjs),
0 blocked. 548 legacy widgets in 209 documents. Report: `dojo-react.md`.

## What changed

| Change | Count | Where |
|---|---|---|
| Legacy widgets converted (DataGrid → Data Grid 2, selectors and drop-downs → Combo box, images → Image) | 368 statements | `convert-legacy.mdl`, `CONVERT-REPORT.md` |
| Dynamic images bound to the object | 7 | `dynimage-*.mdl` |
| DropdownContainer (not an ES module, breaks mxbuild) → Pop-up menu | 1 | `dropdown-react.mdl` |
| Building blocks with legacy widgets deleted (no ALTER/DROP in mxcli) | 2 | MPR rows, backups kept |
| Login: UseAuthToken empty → false | 1 | `login-react.mdl` |
| **Security grants surfaced by the React build** | **2** | `security-react.mdl` |
| Header CSS `flex-shrink: 0` (title and buttons overlapped the grid) | 1 | `_headers.scss` |
| Grids that drive a detail view select on row click | 30 | `selection-rowclick.mdl` |
| Tickets and Parts: one toolbar above the grid on the selected row, priority dot back, filters on key columns only, classic header | 2 pages | `tickets-polish.mdl`, `parts-polish.mdl`, `_react-grid.scss` |
| Data Grid 2 column picker (eye) hidden, Dojo had none | all grids | `_react-grid.scss` |

The two security grants:

- `grant execute on microflow Technician.DS_TechnicianGroup_GetManagerList to Technician.ViewAll`
- `alter user role FSMAPIConsumer add module roles (General._AddOn_ViewAnonymousLogin)`

Fine for the demo. An owner signs them off before production.

## Gaps a user can see

| Gap | Count |
|---|---|
| Search fields dropped (association path from the non-owner side) | 29 |
| Double-click actions that take a list stay as a button above the grid | 8 |
| Export to Excel and select-all buttons dropped | 2 + |
| Converted captions in en_US only (nl_NL lost) | 2237 texts |
| Forms overview no longer selects the first form (Data Grid 2 has no select-first) | 1 page |
| Ticket list: the priority dot column showed the word instead of the coloured dot | fixed in bd4a49e; seen on the screenshot pair, not by the journeys |

## Test instrument heals (not app changes)

- 125 `select` steps became `combo` (the React client renders a Combo box, not a native select).
- 5 Forms journeys click a form first (see the select-first gap).
- 1 Scheduler journey keeps "All groups", as Dojo did.

## Retest result

Journeys on React (b2 build): 252 pass where Dojo passes, 8 flagged as regression in the full run. All 8 were rerun on a
fresh copy of the frozen data (`e2e-react-rr`, `journeys-react-rr.out`): 7 pass. The 8th (work order button 27) needs a
technician on the first work order, which an earlier journey of the Dojo run had added; on fresh data Dojo shows the
same empty list (`probe-wo.js`). **0 real regressions.** Smoke: 74 PASS, 6 FAIL, same 6 as Dojo (Switch user).
The app stop mid-run was the trial license (about 3 h), not a crash.

Polish retest (b3 build, fresh data, `journeys-react-b3.out`): the 6 Tickets and Parts journeys give 5 PASS and 1 PASS*
(Cancel already fails on Dojo). Screenshot pairs in `shots-pair/`.

UX polish ported to React (branch `ux/react-polish`, commit e715d9d, build u1): KPI cards, chart title "Open work
orders", Status as a chip on the ticket list. Retest on fresh data (`journeys-react-ux.out`): 2 PASS and 1 PASS*.
Before and after shots in `ux-shots/`.
