# List view controls (Marketplace component 105694)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Widget, Mendix, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/105694)

| version | published | min Mendix |
|---|---|---|
| 1.3.16 | 2021-09-20 | 7.23.21 |
| 1.3.15 | 2021-06-28 | 7.23.21 |
| 1.3.14 | 2021-06-22 | 7.23.21 |
| 1.3.13 | 2021-06-02 | 7.23.21 |
| 1.3.10 | 2021-01-08 | 7.20.0 |
| 1.3.9 | 2020-12-16 | 7.20.0 |
| 1.3.8 | 2020-07-09 | 7.20.0 |
| 1.3.7 | 2020-05-20 | 7.20.0 |
| 1.3.6 | 2020-04-24 | 7.20.0 |
| 1.3.5 | 2020-02-19 | 7.20.0 |
| 1.3.4 | 2019-11-13 | 7.20.0 |
| 1.3.3 | 2019-05-21 | 7.20.0 |
| 1.3.2 | 2019-05-08 | 7.20.0 |
| 1.3.1 | 2019-04-02 | 7.20.0 |
| 1.3.0 | 2018-12-14 | 7.20.0 |
| 1.2.3 | 2018-09-26 | 7.13.1 |
| 1.2.2 | 2018-08-28 | 7.13.1 |
| 1.2.1 | 2018-07-13 | 7.13.1 |
| 1.2.0 | 2018-05-23 | 7.13.1 |
| 1.1.2 | 2018-03-22 | 7.9.0 |
| 1.1.1 | 2018-03-13 | 7.9.0 |
| 1.1.0 | 2018-02-16 | 7.9.0 |
| 1.0.2 | 2018-01-25 | 7.9.0 |
| 1.0.1 | 2018-01-19 | 7.9.0 |
| 1.0.0 | 2017-11-24 | 7.8.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.3.15 | fix | Fixed regression in v1.3.10 where Header Sort and Drop down Sort did not keep list view sorted when pressing back button. | Header Sort, Drop down Sort |  |
| 1.3.13 | fix | Fixed issue in v1.3.12 where widget would error on list view control interaction if search not enabled. | search |  |
| 1.3.10 | fix | Fixed issue where pagination widget would change corresponding listview's ordering in particular scenario. | pagination widget |  |
| 1.3.8 | fix | Fixed unexpected regression in v1.3.7 where you could not combine filters. | filters |  |
| 1.3.6 | fix | Fixed issue when combining multiple filters and sortings where only last applied was considered. | filters, sortings |  |
| 1.3.5 | removal | Removed use of deprecated mendix.lang.delay. | mendix.lang.delay |  |
| 1.3.4 | fix | Sorting now works in combination with standard Load more functionality. | sorting, Load more |  |
| 1.3.3 | fix | Fixed issue where initial sorting of list view header was not being respected. | list view header sorting |  |
| 1.3.1 | fix | Persists original sort of list view when no sorting control used to sort. | sorting |  |
| 1.3.1 | fix | Offset preserved for non-paged list views; Load more items show when navigating back to list view. | Load more, pagination |  |
| 1.3.1 | fix | Can now find list view when navigating back to page with same layout. | list view detection |  |
| 1.3.0 | feature | Persist filters, search and sort state when navigating to detail page; restored on back/close. | filters, search, sort |  |
| 1.2.3 | fix | Filter and text box search now cleared correctly when conditional visibility changes. | filter, text box search, conditional visibility |  |
| 1.2.1 | fix | When lists are sorted, sorting is maintained when filter is applied. | sorting, filter |  |
| 1.2.1 | fix | List view controls can now be used in container that is initially invisible. | list view controls, conditional visibility |  |
| 1.1.2 | fix | Paging buttons now show when initially hidden and new items added to list. | paging buttons |  |
| 1.1.2 | fix | Sorting drop down persists selection when moving to next page. | Sorting drop down |  |
| 1.1.0 | feature | Added support for mobile offline; widgets can be used in offline apps, though XPath cannot be used. | list view controls |  |
| 1.1.0 | fix | Added support for multiple reference [%CurrentObject%] in XPath constraint. | XPath constraint |  |
