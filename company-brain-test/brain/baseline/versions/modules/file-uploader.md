# File Uploader (Marketplace component 235351)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/235351)

| version | published | min Mendix |
|---|---|---|
| 2.5.0 | 2026-06-29 | 10.22.0 |
| 2.4.2 | 2026-04-24 | 10.22.0 |
| 2.4.1 | 2026-02-13 | 10.22.0 |
| 2.4.0 | 2025-12-11 | 10.22.0 |
| 2.3.0 | 2025-08-15 | 10.22.0 |
| 2.2.2 | 2025-07-01 | 10.22.0 |
| 2.2.1 | 2025-05-28 | 10.22.0 |
| 2.2.0 | 2025-05-07 | 10.22.0 |
| 2.1.0 | 2025-04-16 | 10.21.0 |
| 2.0.0 | 2025-03-14 | 10.15.0 |
| 1.0.3 | 2025-02-28 | 9.24.0 |
| 1.0.2 | 2025-02-14 | 9.24.0 |
| 1.0.1 | 2024-12-19 | 9.24.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.5.0 | fix | Fixed validation errors persisting after uploading valid file. | validation errors |  |
| 2.5.0 | fix | Fixed dropping more files than allowed rejecting entire batch; now only excess rejected. | file upload |  |
| 2.5.0 | fix | Fixed files rejected due to total limit with no recovery; now show retry button. | file limit, retry |  |
| 2.5.0 | breaking | Maximum number of files property now optional; 0/empty means unlimited (default 10). | Maximum number of files |  |
| 2.5.0 | improvement | Files now upload in queue instead of marked as errors; queued files show 'Waiting...' state. | file queue, concurrent uploads |  |
| 2.5.0 | improvement | Removing file with default button now removes from list immediately, not greyed out. | remove button, file list |  |
| 2.4.2 | fix | Fixed Download button not working on Mendix 11.8. | Download button |  |
| 2.3.0 | fix | Fixed file uploader allowing more files on refresh despite maximum reached. | maximum uploaded files |  |
| 2.3.0 | improvement | Changed max file configuration to set maximum uploaded files through expression. | max file configuration |  |
| 2.1.0 | requirement | Updated minimum Mendix version to 10.21.0 to support Mendix 11. | Mendix Studio Pro |  |
| 2.0.0 | requirement | Bumped minimum supported version to 10.15.0. | Mendix |  |
| 1.0.2 | fix | Fixed error when uploading multiple files on newly created context object. | multiple files, context object |  |
| 1.0.2 | fix | Fixed users uploading unsupported image formats in image mode. | image mode |  |
| 1.0.2 | feature | Added timeout functionality to abort upload if object not created within timeout. | File/Image creation action |  |
