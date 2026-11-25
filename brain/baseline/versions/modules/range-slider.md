# Range Slider (Marketplace component 52704)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Widget, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/52704)

| version | published | min Mendix |
|---|---|---|
| 3.0.3 | 2026-07-22 | 9.6.0 |
| 3.0.2 | 2026-06-17 | 9.6.0 |
| 3.0.1 | 2026-02-11 | 9.6.0 |
| 3.0.0 | 2026-01-07 | 9.6.0 |
| 2.1.4 | 2024-08-28 | 9.6.0 |
| 2.1.3 | 2024-07-15 | 9.6.0 |
| 2.1.2 | 2024-06-25 | 9.6.0 |
| 2.1.1 | 2023-09-27 | 9.6.0 |
| 2.1.0 | 2023-06-06 | 9.6.0 |
| 2.0.0 | 2021-12-23 | 9.6.0 |
| 1.3.1 | 2018-12-14 | 7.13.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 3.0.3 | fix | Fixed issue where widget was not loading in Dojo client due to broken JavaScript bundle. | JavaScript bundle, Dojo client |  |
| 3.0.2 | fix | Mark labels and numeric tooltips now respect decimalPlaces and user session locale (decimal separator and thousands grouping). | mark labels, numeric tooltips, decimalPlaces, locale |  |
| 3.0.0 | breaking | Updated rc-slider library to @rc-component/slider (major version). May break current custom styling. | rc-slider, @rc-component/slider |  |
| 2.1.3 | fix | Fixed issue with initial value being reset to default min value. | initial value |  |
| 2.1.2 | fix | Fixed issue where slider tooltip would not position correctly when scrolling page. | tooltip positioning |  |
| 2.0.0 | breaking | Converted into a pluggable widget. | widget architecture |  |
| 1.3.1 | fix | On change events now triggered only when value changed; no longer double trigger on loose focus. | on change events |  |
| 1.3.1 | fix | Value no longer updated when value, upper bound or lower bound is invalid. | value update |  |
| 1.3.1 | fix | Added validation for decimal steps incompatible with lower, upper value. | decimal steps |  |
