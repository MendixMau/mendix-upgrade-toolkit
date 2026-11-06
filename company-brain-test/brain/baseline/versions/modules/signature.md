# Signature (Marketplace component 107984)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Widget, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/107984)

| version | published | min Mendix |
|---|---|---|
| 2.1.0 | 2026-08-31 | 11.8.0 |
| 2.0.1 | 2026-07-22 | 11.8.0 |
| 2.0.0 | 2026-06-24 | 11.8.0 |
| 1.0.8 | 2026-03-05 | 8.0.0 |
| 1.0.7 | 2025-01-15 | 8.0.0 |
| 1.0.4 | 2020-02-17 | 7.13.1 |
| 1.0.3 | 2019-10-01 | 7.13.1 |
| 1.0.2 | 2019-01-02 | 7.13.1 |
| 1.0.1 | 2018-12-19 | 7.13.1 |
| 1.0.0 | 2018-11-20 | 7.13.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.0.0 | breaking | Complete rewrite using Pluggable Widget API. Migrated from Custom Widget (v1.x) to Pluggable Widget architecture. | Signature |  |
| 2.0.0 | requirement | Minimum Mendix version increased to 11.8.0 (previously 7.13.1). |  |  |
| 2.0.0 | migration-step | No backward compatibility. Existing v1.x implementations must be reconfigured. | Signature |  |
| 2.0.0 | breaking | Widget ID changed from com.mendix.widget.custom.signature.Signature to com.mendix.widget.web.signature.Signature. | com.mendix.widget.custom.signature.Signature | com.mendix.widget.web.signature.Signature |
| 2.0.0 | migration-step | Widget MPK renamed from Signature.mpk to com.mendix.widget.web.Signature.mpk. Remove old Signature.mpk manually after migration. | Signature.mpk | com.mendix.widget.web.Signature.mpk |
| 2.0.0 | breaking | Widget category changed from Add-ons to Input elements. | Signature |  |
