# Process Queue (Marketplace component 393)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Module, Mendix, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/393)

| version | published | min Mendix |
|---|---|---|
| 8.0.0 | 2022-03-30 | 8.12.0 |
| 7.0.0 | 2022-03-31 | 7.23.22 |
| 4.2.0 | 2021-02-11 | 8.12.0 |
| 4.1.2 | 2019-08-02 | 7.23.0 |
| 4.1.1 | 2019-03-01 | 7.1.0 |
| 4.1.0 | 2018-02-16 | 7.1.0 |
| 4.0.0 | 2017-11-02 | 7.1.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 7.0.0 | requirement | Upgraded project to Mendix 7.23.22 |  |  |
| 4.2.0 | requirement | Updated to Mendix Studio Pro 8.12.0 |  |  |
| 4.1.2 | requirement | Module is now Mendix 8 compatible |  |  |
| 4.1.1 | fix | Fixed thread leak when calling InitializeQueue.java | InitializeQueue.java |  |
| 4.1.1 | improvement | Improved memory management due to differing IContext behavior in Mx7 vs Mx6 |  |  |
| 4.1.0 | removal | Removed Queue monitor information from QueueOverview page; information was outdated and misaligned with actual queue state | QueueOverview |  |
| 4.1.0 | breaking | Completely replaced retry mechanism with pre-processing mechanism ensuring FIFO ordering |  |  |
| 4.1.0 | improvement | Pre-processing mechanism reduces error-prone handling and processes large queued action batches quicker |  |  |
| 4.1.0 | fix | Removed while loop in ObjectQueueExecutor Java action that might cause queue to hang | ObjectQueueExecutor |  |
| 4.1.0 | removal | Removed full retry mechanism, replaced by preprocessing of actions before appending to queue |  |  |
| 4.1.0 | improvement | Modified _QueueAppenderThread Java functionality to enable thread restart capability | _QueueAppenderThread |  |
| 4.0.0 | requirement | Upgraded to Mendix 7.1.0 |  |  |
