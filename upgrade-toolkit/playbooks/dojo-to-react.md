# Playbook: Dojo client to React client

Field run: FSM (Field Service template, 11.12.7, Dojo client to React client, same Mendix version, no version
rung). `examples/fsm/rung3-dojo-to-react/`. Steps refer to [steps/](../steps/). This is a client swap, not a
version upgrade: steps 3 (upgrade) and 4 (test) still apply in full; steps 1-2 (triage, plan) shrink to the
readiness check below.

Route: run `dojo_report.py` once to size the work, convert every legacy widget mechanically, fix what the build
surfaces, then re-walk journeys and expect test-instrument noise, not app regressions, from the client swap itself.

## 1. Readiness (triage)

Run `dojo_report.py` before committing to the rung, on any 10-to-11 or 11-to-11 app, not only when a React
switch is already decided: it is the only report that names legacy widgets and Dojo-only packages. FSM: 67
packages (62 ready, 5 Dojo-only: HTMLSnippet, MicroflowTimer, ShowByCondition, URLRedirector, snippetjs, 0
blocked), 548 legacy widgets across 209 documents. A 10-to-11 rung that skips this only discovers the count when
the client is switched later (TOOLKIT-BUGS: "the pipeline never ran dojo_report.py in rung 2, so React readiness
... only showed up when the client was switched").

## 2. No converter ships with mxcli: generate one from `mx dump-mpr`

Neither mxcli nor `mx` has a convert command for legacy core widgets, and Studio Pro's quick fix works one widget
at a time. `mxcli describe` of a legacy widget is lossy: a classic Data grid loses control-bar buttons, XPath and
search fields ("NOT re-executable"); a Dojo pluggable (MicroflowTimer, HTMLSnippet, snippetjs) loses its
microflow or JS/HTML contents. Only `mx dump-mpr` JSON carries the full definition.

`examples/fsm/rung3-dojo-to-react/convert_legacy.py` reads that JSON and emits `ALTER PAGE ... REPLACE`
statements per widget: DataGrid to Data Grid 2, selectors and drop-downs to Combo box, static images to Image,
template grids to Gallery. FSM: 368 statements (152 + 138 + 32 + 1 + dynamic images below). It skips native
pages, snippets and layouts on purpose, and does not catch:
- dynamic images bound to an object expression (`image x (Image: $currentObject)`) — fix these 7-wide class by hand;
- a widget inside a list view's `template for <Specialization>` ("widget not found" from `mxcli ALTER`) — REPLACE
  the whole list view from its DESCRIBE output instead, adding explicit `Params: (X = $currentObject)` to its
  snippet calls;
- building blocks containing classic widgets — mxcli has no ALTER or DROP for building blocks; remove them as
  Unit rows from the MPR (keep a backup) and re-add with native widgets.

## 3. What the build surfaces, in order

1. **Non-ES-module pluggables fail the export, silently in `mx check`.** DropdownContainer 1.2.0 (2020) is not an
   ES module: mxbuild fails during "export of pluggable widgets" and `mx check` reports nothing. A readiness
   check should flag any pluggable not built as an ES module; until then, replace by hand (FSM: Pop-up menu).
2. **Security grants surface only after the widget errors clear**, not before. A Combo box runs its data-source
   microflow for read-only roles, and any login data view needs entity access for every role that reaches
   Login_Web. FSM needed 2 grants:
   - `grant execute on microflow Technician.DS_TechnicianGroup_GetManagerList to Technician.ViewAll`
   - `alter user role FSMAPIConsumer add module roles (General._AddOn_ViewAnonymousLogin)`
   Treat both as owner sign-off items, not silent fixes — a grant widens what a role can do.
3. **Sign-in and conditional-visibility widgets have no React form.** Dojo's Login id/Password/Sign-in/Validation
   widgets: rebuild as a non-persistent login object plus NanoflowCommons.SignIn. ShowByCondition (visibility
   from a microflow): React only takes an expression, so this needs a list view wrapper or a calculated
   attribute — propose to the owner, do not drop the check silently.
4. **The theme template is still Dojo's.** A customised `theme/web/index.html` fails CE6912 on the React build;
   replace it with the React template from `mxbuild runtemplates/deployment/react-web`, reapplying the app's
   custom lines on top. Scriptable and detectable (CE6912 is specific).
5. **The React bundler can OOM in a constrained container** (exit 137 at ~5.8 GB free): stop idle app containers
   and pass `UPG_EXTRA="-e NODE_OPTIONS=--max-old-space-size=4096"`. Warn below ~4 GB free before a React build.
6. **`mxcli widget init` writes `.claude/skills/widgets` into the app folder** — keep it out of the app commit.

## 4. Gaps a user can see, propose rather than silently accept

| Gap | FSM count |
|---|---|
| Search fields dropped (association path from the non-owner side) | 29 |
| Double-click actions that take a list stay as a button above the grid | 8 |
| Export to Excel and select-all buttons dropped | 2+ |
| Converted captions in the base language only (other locales lost) | 2237 texts |
| `SelectFirst` dropped (Data Grid 2 has no equivalent): a listening data view that opened pre-filled under Dojo now waits for a click | per grid with SelectFirst |
| Custom cell content lost (e.g. a styled empty caption column reading as plain attribute text) | per such column |

`convert_legacy.py` should list every grid that had `SelectFirst` in its own report so these are named, not
discovered by a user. None of this is a toolkit bug to silently patch over: each row is an owner decision
(rebuild, accept, or keep the old client for that page).

## 5. Test-instrument heals, not app changes

A client swap breaks test instruments in ways that look like regressions but are not:
- **`select` steps become `combo` steps.** The React client renders a Combo box, not a native `<select>`; every
  journey step targeting a converted drop-down needs this heal (FSM: 125 steps).
- **`select first` and `combo first` are not the same operation.** Dojo's `select first` can land on an empty
  option ("All groups"); Combo box's `combo first` requires a real option, so a persona with no backing data now
  fails where it used to pass. When the Dojo step picked the empty caption, drop the step in the heal rather than
  converting it 1:1 (FSM: one case, a referenceSelector).
- **Regressions from a client swap must be re-confirmed on fresh data before they're reported.** Destructive and
  additive journeys from the Dojo run can leak state into the React run (an emptied grid, an added row that made
  a later step pass only on Dojo). Rerun every flagged regression on a fresh database copy; FSM found 8
  candidates this way and confirmed 0 real regressions (7 passed clean, the 8th needed the same missing seed data
  on Dojo too).
- **A per-page Dojo vs. React screenshot pair catches what journeys cannot** (lost custom cell content, a
  `display:none` CSS trap below). Keep `shots-pair/` evidence per rung.

## 6. Data Grid 2 styling trap

Data Grid 2 rows are `display:contents` inside one CSS grid. `display:none` on a header cell (for example a
column-picker header `.th.column-selector`) removes that cell from the grid flow and shifts every data cell in
the row by one column — silently, with no build or runtime error. Use `visibility:hidden` (keeps the cell's grid
slot) instead of `display:none` when hiding a Data Grid 2 column-related element. This is caught by a
screenshot pair, not by journeys or `mx check`.

## 7. Result (FSM, for orientation, not a guarantee)

Journeys on React: 252 pass where Dojo passes, 8 flagged as regression in the full run, 0 confirmed after the
fresh-data rerun (section 5). Polish and UX follow-up passes: 5 PASS + 1 PASS* (pre-existing Dojo fail), then 2
PASS + 1 PASS*. See `examples/fsm/rung3-dojo-to-react/README.md` for the full change table and
`CONVERT-REPORT.md`/`dojo-react.md` for the per-widget readiness and conversion detail.

Not proved: a Dojo-to-React swap combined with a version rung in the same pass, an app with native pages beyond
the smoke check, and any app whose legacy-widget count is far above FSM's (548 across 209 documents).
