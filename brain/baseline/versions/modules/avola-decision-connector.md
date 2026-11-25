# Avola Decision Connector (Marketplace component 33257)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Module, Ciphix, Partner, [marketplace](https://marketplace.mendix.com/link/component/33257)

| version | published | min Mendix |
|---|---|---|
| 3.7.0 | 2024-06-12 | 10.6.1 |
| 3.6.0 | 2024-04-02 | 10.6.1 |
| 3.5.0 | 2024-04-02 | 9.24.16 |
| 3.4.0 | 2023-05-17 | 9.12.6 |
| 3.3.0 | 2022-10-21 | 9.1.1 |
| 3.2.0 | 2022-05-06 | 9.1.1 |
| 3.1.0 | 2021-11-09 | 9.1.1 |
| 3.0.0 | 2021-08-18 | 9.1.1 |
| 2.2.0 | 2021-11-09 | 8.18.1 |
| 2.1.0 | 2020-09-21 | 8.1.1 |
| 2.0.0 | 2020-09-15 | 8.1.1 |
| 1.9.0 | 2020-09-21 | 7.15.1 |
| 1.8.0 | 2020-09-15 | 7.15.1 |
| 1.7.0 | 2020-03-19 | 7.15.1 |
| 1.6.0 | 2020-03-13 | 7.15.1 |
| 1.5.1 | 2019-06-14 | 7.15.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 3.6.0 | requirement | Upgraded to Mendix 10.6.1 (MTS), Encryption module 9.0.2, Atlas Core 3.14.0, Atlas Web Content 3.5.1. | Mendix, Encryption module, Atlas Core, Atlas Web Content |  |
| 3.5.0 | requirement | Upgraded to Mendix 9.24 LTS. | Mendix |  |
| 3.4.0 | requirement | Updated to Encryption module version 8.0.4. | Encryption module |  |
| 3.3.0 | requirement | Updated to MTS. Compatible with Atlas 3. | Mendix, Atlas |  |
| 3.3.0 | migration-step | Renamed module. |  |  |
| 3.2.0 | requirement | Updated dependent module Encryption to version 4.0.2. | Encryption module |  |
| 3.1.0 | improvement | Improved the method to get the token endpoint, using the authority server details. |  |  |
| 3.1.0 | feature | Added support for a seamless migration of an authority during runtime and running executions. |  |  |
| 3.0.0 | requirement | Upgraded to Mendix 9.1.1. | Mendix |  |
| 3.0.0 | requirement | Upgraded support for Atlas UI to 2.7. | Atlas UI |  |
| 2.2.0 | improvement | Improved the method to get the token endpoint, using the authority server details. |  |  |
| 2.2.0 | feature | Added support for a seamless migration of an authority during runtime and running executions. |  |  |
| 2.1.0 | improvement | All TimeOuts on REST calls can now be configured using the TimeOut_Short and TimeOut_Long constants. | TimeOut_Short, TimeOut_Long |  |
| 2.0.0 | requirement | Updated for new identity server implementation in Avola Decision. |  |  |
| 1.9.0 | improvement | All REST call timeouts can now be configured using the TimeOut_Short and TimeOut_Long constants. | TimeOut_Short, TimeOut_Long |  |
| 1.8.0 | requirement | Updated for new identity server implementation in Avola Decision. |  |  |
| 1.7.0 | improvement | Added extra logic to refreshing token, making sure the expiry date will be valid. |  |  |
| 1.7.0 | feature | Added time-outs on requests for getting token and execution of single decision request. |  |  |
| 1.6.0 | improvement | Improved logging functionality. |  |  |
| 1.6.0 | improvement | Tokens are requested in a subtransaction which cannot be executed concurrently. |  |  |
| 1.6.0 | feature | Added scheduled event to delete old execution request logs with a retention setup. |  |  |
