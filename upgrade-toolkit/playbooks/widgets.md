# Playbook: widgets that break at runtime (build clean, page broken)

Evidence: batch 1 template runs T3 (App B 9.24 to 10.24), T5 (App G 9.24 to 10.24), T7 (App E
10.6 to 10.24 to 11.15) and T8 (FSM 9.24 to 10.24); branches `origin/runs/<slug>`, files SCORECARD, COMPARE, JOURNAL,
TOOLKIT-FEEDBACK. Release facts from the brain version tables (`brain/baseline/versions`) and the
public sources named per section. Row ids (T7-29, ...) are the workers' TOOLKIT-FEEDBACK items; FEEDBACK.md row R1-1.

mx check, mxbuild, quick start and the data diff cannot see these. Only the smoke walk (console errors) and shotdiff
catch them. So triage has to list them, and the 11 rung has to fix them before its gate.

## 1. Legacy Charts widgets (`com.mendix.widget.custom.*`): replace before Mendix 11

**What broke (T7 rung 2, FAIL).** On 11.15.0 every page with the deprecated Charts widgets showed "An error occurred
in a com.mendix.widget.custom.PieChart.PieChart widget" (also ColumnChart, TimeSeries). Console: `Invariant Violation:
Could not find "store" ... PieChart.js`. 6 smoke-walk regressions (Dashboard and Reports, all 3 roles), 4 widget
instances: `ChecklistExecution.PageDashboardInspections` (pieChart2, timeSeries1, columnChart1) and snippet
`ChecklistExecution.ToleranceReportItemType` (timeSeries1). The same widgets worked on rung 1 (10.24.26).

**Root cause.** Three facts together:
1. These widgets are the old Charts 1.x/2.x widgets (source `github.com/mendix/charts`, archived 2023-02-23, moved to
   `mendix/web-widgets`). They are classic client widgets (`needsEntityContext`, no `pluginWidget`), built with
   `react-redux` 5.1.2 and with `react`/`react-dom` as webpack **externals** (`package.json`, `webpack.config.js` of
   that repo): they run on whatever React the Mendix client ships.
2. react-redux 5 passes the store through React's legacy context (`contextTypes` / `getChildContext`). React 19
   removed legacy context (React 19 upgrade guide, "Removed: legacy context"). Without it `connect()` cannot find the
   store: exactly the "Could not find store" error.
3. Mendix 11.6.0 upgraded the client to React 19, 11.10.0 to React 19.2 (brain `studio-pro-upgrade-11.md` rows
   11.6.0 and 11.10.0; docs "Upgrading from 10 to 11": "upgrade all installed widgets to the latest published versions").
   Mendix 10.x is on React 18, which still has legacy context (deprecated): so the widgets work on 10.24 and break on
   11.6 and later. Expect 11.0 to 11.5 to still render them (not tested).

So the playbook line "Dojo (classic) widgets break only on the React client, optional until 12" is wrong for these
widgets: they break on the Dojo client too, from 11.6 (T7-29).

**Lineage (brain `modules/charts.md`, component 105695).** Charts 3.0.0 (2022-07) deprecated the old widgets and
shipped the reworked pluggable ones; 3.0.1 still carries both. **Charts 4.0.0 (2022-10) removed all deprecated chart
widgets** ("Apps must manually replace deprecated widgets with new ones"). 6.0.0 moved to plotly.js 3 and added the
Custom chart (the Any Chart successor; Any Chart is deprecated and will not be made React-ready). Current 6.3.2
(2026-08), min Mendix 10.6.0; the 6.1.x line also runs on 9.24.

**Why the toolkit walks into it.** Atlas_Web_Content 3.6.1 and later ship their own `widgets/Charts.mpk` (Charts 6.x)
and overwrite the app's 3.0.1 copy (T3 note, T5-14, T7-19). The old widgets then give CE0462 on mx check, and
`missing_deps.py` has no package that still contains them. T5 and T7 "fixed" CE0462 by putting the 3.0.1 package
back (T5 as `widgets/ChartsLegacy.mpk` next to Charts 6, T7 over `Charts.mpk`). That passes on 10.24 and only moves
the break to the Mendix 11 runtime. T3 did the right thing: it replaced the widget.

**Replacement (proved headless in T3).** mxcli can author the Charts 6 widgets as pluggable widgets
(T7's "mxcli cannot author chart widgets" is not true for Charts 6). T3, `evidence/repair/repair-2-barchart.mdl`:

```
alter page BOMDashboarding.ProgramBOM_ProgressDashboard {
  replace barChart2 with {
    pluggablewidget 'com.mendix.widget.web.barchart.BarChart' barChart2 {
      series sStatus (
        DataSet: 'static',
        DataSource: microflow BOMDashboarding.DS_ProgramBOMGraph_Status,
        StaticXAttribute: Value,
        StaticYAttribute: Name,
        StaticName: 'Status'
      )
    }
  }
};
```

| old id (Charts 1.x to 3.0.1) | new id (Charts 4+; take 6.x) |
|---|---|
| `com.mendix.widget.custom.PieChart.PieChart` | `com.mendix.widget.web.piechart.PieChart` (pie and doughnut) |
| `com.mendix.widget.custom.ColumnChart.ColumnChart` | `com.mendix.widget.web.columnchart.ColumnChart` |
| `com.mendix.widget.custom.BarChart.BarChart` | `com.mendix.widget.web.barchart.BarChart` |
| `com.mendix.widget.custom.LineChart.LineChart` | `com.mendix.widget.web.linechart.LineChart` |
| `com.mendix.widget.custom.TimeSeries.TimeSeries` | `com.mendix.widget.web.timeseries.TimeSeries` |
| `com.mendix.widget.custom.AreaChart/HeatMap/BubbleChart` | same pattern (`com.mendix.widget.web.<type>.<Type>`); read the exact id from the installed Charts.mpk (`unzip -p widgets/Charts.mpk package.xml` and the widget XMLs) |
| Any Chart (`AnyChart_BuildingBlocks`, T5, T6) | Custom chart (Charts 6.0+) |

Keep the data source (XPath, microflow or association) and the X/Y attributes; series move into the `series` list.
Configuration that does not carry over: colours, on-click actions, "Custom settings" JSON (Charts 4.2.0 notes: line
and marker colour and on-click lose their values; reconfigure). Open both screenshots after the repair: the look changes.

**Where in the run.** Do it on the **10.24 rung**, right after the Atlas_Web_Content step that overwrote
`Charts.mpk` (CE0462 points at it). Never restore the 3.0.1 package when the path goes on to 11. On a 9-to-10 run that
stops at 10.24, restoring as `ChartsLegacy.mpk` (T5, ids do not overlap) is allowed as a temporary measure, with a
line in the report: "legacy charts, break from Mendix 11.6".

**Triage.** List every page and snippet using a `com.mendix.widget.custom.` widget id (and Any Chart), with the
Charts.mpk version installed: `grep -l 'com.mendix.widget.custom' app/widgets/*.mpk` (unzip -l) and the widget ids
`missing_deps.py` already reads. Each one is a planned repair for the 10.24 rung of a path to 11.

**The route, per module (cold rung 2: 36 Any Chart uses, 18 of them in a sample module).** `bin/repair/widgetroute.py
app/ --target <ver>` gives one route per module and old widget, from `playbooks/widget-routes.json` (the table above as
data: old id, new id, property mapping, what plotly 3 dropped, effort, and the next candidates; `missing_deps.py` reads
its DEPRECATED-11 ids from it too). The toolkit heals itself: the recommended candidate goes into the test build and the
person OKs it afterwards or picks B. Any Chart 3.0.4 maps 1:1 to Custom chart (Charts 6.x): every key exists, four
translatable strings become plain strings, the same plotly engine (plotly.js 3) draws it; `--apply` rewrites the widget
and `mx update-widgets` does the rest. A static JSON with keys plotly 3 dropped (titlefont, a title as plain text) is
replaced and listed as approximated. An Any Chart straight on a snippet parameter (Custom chart there fails mx check,
CE7006 on its attributes) gets a data view on that one object parameter first. A module that holds only pages,
snippets and building blocks, no entities, and that nothing opens is removed (`keep-module M` puts it back). Cold app:
all 36 handled (15 replaced, 3 wrapped and replaced, the sample module removed), mx check 0 errors. Every item reads
"Found / Searched / Candidates (one recommended) / Applied", never a bare "no replacement". The pipeline (build, row 37)
runs replace, wrap and remove as separate repair commits (each undone if mx check gets worse; the route then proposes
its next candidate) and asks one OK per item: "N charts replaced by Charts 6.x (Custom chart), M approximated: OK?";
B (`route-b R`, `keep-module M`) reverts that commit on the rerun.

## 2. Teardown console errors after 9 to 10 (T8 FAIL)

**What broke (T8, FSM 9.24.2 to 10.24.26).** 7 smoke-walk regressions, pages render the same content
(`shots-sample/dashboardall-*.png`). Errors (`evidence/smoke-after.json`):
- `Dashboard.DashboardAll.container2 / container42`, `Dashboard.DashboardInternal.layoutGrid1`,
  `Dashboard.DashboardExternal.layoutGrid1`, `Visualizations.Snippet_Alerts.NotificationBadgeAlerts`:
  "attempt to uninitialize widget that is not loaded yet, check widget structure";
- with it `Minified React error #409` thrown from `mxui.js` (React: "Cannot update an unmounted root": a
  `createRoot` root rendered after it was unmounted);
- `NotFoundError: Failed to execute 'removeChild'` on the Technician and SLA overviews: already there on 9.24
  (baseline defect on Technician_Overview; SLA_Overview had a LineChart TypeError on 9.24 instead).

**Read the walk right first (T8-20).** The walk attributes console output to the step during which it arrived. Per
role, in walk order:

| step that FAILed | message names | real source |
|---|---|---|
| DashboardInternal, DashboardAll | their own containers | the dashboard itself |
| Ticket_Overview_ServiceDesk, Contract_Overview (ServiceDeskEmployee) | `DashboardAll.container42` | the dashboard, 1 and 4 steps later |
| Technician_Overview (CallCenterEmployee) | `DashboardExternal.layoutGrid1` | the dashboard, 6 steps later |
| Ticket_Overview_NeedsAction | `Snippet_Alerts.NotificationBadgeAlerts` | the alerts snippet on that page |
| TechnicianGroup_Overview | removeChild | follows Technician_Overview, which has the 9.24 removeChild defect |

So 3 sources, not 7 pages: the two dashboards and the alerts snippet. An error naming a page **4 to 6 steps after
leaving it** means something on that page keeps a timer or a pending callback after the page is gone.

**Root cause (probable; the app was not kept, so not confirmed widget by widget).** Mendix 10.0 changed how React
widgets live in classic (Dojo) containers: "A `div[data-widget-wrapper]` element will be placed around a React widget
if its container is rendered as a Dojo widget" (10.0 release notes, brain `studio-pro-upgrade-10.md` 10.0.0
breaking row). Each such widget gets its own React 18 root. When the container is destroyed while a widget in it has
not finished loading, mxui logs "attempt to uninitialize widget that is not loaded yet", and a late render into the
unmounted root throws #409. Candidates on these pages, from T8's COMPARE: the classic widgets kept from 9.x
(MicroflowTimer, HTMLSnippet, URLRedirector, DropdownContainer, snippetjs) next to pluggable widgets that the module
updates replaced (Charts 6 via Atlas_Web_Content, Badge, ProgressBar/Circle). Microflow Timer (component 27) is
**deprecated** (last 4.0.4, 2023, a classic widget): a timer that fires after the page is gone is the best fit for an
error 4 to 6 steps later. The "Cumulative" checkbox caption lost on the Ticket trend card is a separate visible change
(T8-16; shotdiff passed it).

**How to pin it on the next run (do this before calling it a regression).**
1. `mxcli describe page Dashboard.DashboardAll` (and DashboardInternal, DashboardExternal, snippet
   `Visualizations.Snippet_Alerts`): list the widget type of every widget inside the named containers
   (container2, container42, layoutGrid1, NotificationBadgeAlerts).
2. On a throwaway copy, remove one candidate at a time, build, walk only that role: the message that disappears names
   the widget.
3. Replace, do not patch: Microflow Timer -> **Events** widget (component 224259, min Mendix 9.24, pluggable);
   HTMLSnippet -> HTML/JavaScript Snippet 4.x (its 4.0.0 notes: the content property must be re-entered) or HTML
   element; classic containers holding a pluggable widget that loads data: keep, but update the pluggable widget to
   its newest version for the target. An Events widget + a bridging nanoflow is another real migration shape for
   HTMLSnippet, seen on a React-client app: 140 of 146 Events-widget instances wired to one bridge nanoflow, the rest
   converted to native HTML element. Either way, judge "is HTMLSnippet still on an old version" from the shipped
   `.mpk` or a live `mxcli` catalog query on it (RX1-2), not from an archived run's decision log: a decision log can
   predate the fix, or the fix can land in a later rerun the log never mentions.
4. Accept as PASS* only what is proved harmless: the page content equal (shotdiff and text), no failed request, the
   error only on leaving the page. A teardown error is still a FAIL if the walk shows a missing value or a stuck
   progress bar.

## 3. Widget versions a module update swaps underneath you

Atlas_Web_Content (3.6.1 and later) and Data Widgets ship shared widget packages and overwrite the app's copies
(T7: Charts, ProgressCircle 1.7.0 -> 3.3.2, Badge, Maps, ProgressBar, Datagrid, Timeline). `mx update-widgets` then
resets properties that do not exist in the new version. Seen:
- ProgressCircle 1.x -> 3.x: attribute bindings reset to a static 50 (T7; repaired by `fix_progresscircle.py`
  in that run; shotdiff caught it).
- Charts.mpk 3.0.1 -> 6.x: section 1.
- After EVERY module step, not only Atlas_Web_Content or Data Widgets (NS-6): any module import can carry widgets.
  notification-service cdd62cc5 ("added email connector module") swapped 9 widgets, Datagrid 2.28.3 -> 2.30.6 among
  them, and the team reverted the data grid widgets on day 111 (d870f330). stepupdate.sh runs `bin/widgetdiff.py app/`
  after each update and prints `WIDGETS: the <Module> update changed N widget package(s)` with name and old -> new
  version per package (ledger `.stepupdate/widgets.txt`, repeated in the summary). By hand: `python3 $B/widgetdiff.py
  app/ --rev HEAD~1`. For each replaced package, the pages that use it go on the shotdiff must-open list; a swap the
  plan did not ask for is restored from the previous commit or recorded as accepted.
- Datagrid swapped, DataWidgets left behind (cold CMM run 10): Atlas_Web_Content 3.9 brought Datagrid 2.30 while the
  app kept DataWidgets 2.x. The 2.x filters then render inside a red box ("must be placed inside the header") on every
  filtered grid page. Update DataWidgets in the same rung as Atlas_Web_Content (3.11.8 cleared it); smokewalk fails a
  page that shows a widget error box. Data grid 2.2 (9.24) rows are `div.tr[role=row]` with `display: contents` and
  cells `div.td` with no role and no `widget-datagrid` class on the root; the journeys row verb handles both shapes.
- Administration 4.x needs DataWidgets 3.x in the same rung (cold CMM): its pages are saved with Data Widgets 3.x
  (Account_Overview's Roles filter is a drop-down in association mode). Under a kept DataWidgets 2.x, update-widgets
  rewrites the filter to the 2.x definition and drops the association settings; on 3.x later the filter is back in
  attribute mode and shows "Unable to get filter store". `bin/widgetdrop.py` names such losses before the build
  (steps/repair.md row 33).
- Data Widgets 3.x refuses a filter on an attribute it cannot filter (cold CMM rung 1 and 2): the MaterialHandler
  dashboard's Mixes grid has a "Material Nr." column over an association to an external (OData) entity
  (`MasterData.Recipes.MaterialNumber`). The 2.x filter took it without a word; the 3.x filter checks the attribute's
  `filterable` and draws "The attribute is not filterable. Please choose a different attribute." in the header. The
  9.24 original shows no box, 10.24 and 11 do. Fix in the app: take the filter off that column (or filter on an
  attribute of the grid's own entity); it is a person's call, the filter never filtered. Smokewalk fails the page.

## 4. React-client readiness is not upgrade work, but list it

What the publishers did and the toolkit did not (T1, T3, T4, T6 COMPARE): reference selectors -> Combo box, static
image / image viewer -> Image widget, Data grid -> Data grid 2, template grid -> Gallery, Dojo custom widgets removed.
Mendix 11 flags them (CW9516 Dojo data grid deprecated, CE0582/CE0572 widget not supported in the React client: T2
had 37/17/5 on 11.15, the publisher's 11.12 version 33/17/5, so the publisher had not done it either). They break
only on the React client, which is required from Mendix 12. Do not do this in an upgrade run; put the counts from
`mx check -d` of the 11 rung in the report as "React-client backlog", per module, with the owner (own module or a
kept Marketplace module: Administration 2.x/3.x alone holds most of the reference selectors and data grids, T4, T6).

Sources (public): github.com/mendix/charts (archived; `src/package.xml`, `src/PieChart/PieChart.xml`,
`package.json`, `webpack.config.js`), github.com/mendix/web-widgets (`packages/pluggableWidgets/*-chart-web`),
docs.mendix.com/refguide/upgrading-from-10-to-11/ (React 19), docs.mendix.com/releasenotes/studio-pro/10.0/
(widget wrapper), React 19 upgrade guide (legacy context removed), React error 409 (createRoot reference),
docs.mendix.com/refguide/mendix-client/marketplace-react-status/ (Any Chart -> Custom chart).
