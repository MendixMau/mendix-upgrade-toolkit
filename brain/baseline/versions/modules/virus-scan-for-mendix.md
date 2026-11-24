# Virus Scan For Mendix (Marketplace component 29130)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Module, Emixa, Partner, [marketplace](https://marketplace.mendix.com/link/component/29130)

| version | published | min Mendix |
|---|---|---|
| 7.0.0 | 2026-08-05 | 11.12.1 |
| 6.0.1 | 2026-04-13 | 10.24.0 |
| 6.0.0 | 2026-02-06 | 10.24.0 |
| 5.2.1 | 2023-06-15 | 8.18.24 |
| 5.2.0 | 2023-06-01 | 8.18.24 |
| 5.1.0 | 2022-12-06 | 8.18.18 |
| 5.0.0 | 2022-07-06 | 8.18.18 |
| 4.0.0 | 2021-04-23 | 8.14.1 |
| 3.1.0 | 2021-02-08 | 7.23.17 |
| 3.0.0 | 2019-12-18 | 7.2.0 |
| 2.0.1 | 2019-04-24 | 7.2.0 |
| 2.0.0 | 2019-04-05 | 7.2.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 7.0.0 | requirement | Minimum Mendix version upgraded to 11.12.1 |  |  |
| 6.0.1 | fix | Fixed issues with parameters, versioning and leftover jars | parameters, versioning |  |
| 6.0.0 | breaking | Changed parameters for synchronous scanning; jar no longer needed | parameters, synchronous scanning |  |
| 5.2.1 | breaking | Updated to work with latest ApprontoLicencer; license name must be 'VirusScan4Mendix'. Fixed InputParamter | ASU_VirusScan4Mendix, ApprontoLicencer, InputParamter |  |
| 5.2.1 | requirement | Recommended to update Appronto Licensing module for compatibility | Appronto Licensing |  |
| 5.2.0 | requirement | Minimum Mendix version upgraded to 8.18.24 |  |  |
| 5.2.0 | improvement | Jackson Java libraries updated to 2.15.2 | Jackson |  |
| 5.2.0 | improvement | Scanii Java library updated to 5.0.0 | Scanii |  |
| 5.1.0 | security | Updated jackson libraries to 2.13.4 series, slf4j-api to 2.0.5, added slf4j-nop-2.0.5, removed http-request-6.0 | jackson-databind, jackson-annotations, jackson-core, jackson-datatype-jsr310, slf4j-api, slf4j-nop, http-request |  |
| 5.0.0 | fix | Fixed bug in closing thread after scanning file resulting in thread overflow | thread management |  |
| 4.0.0 | removal | Removed dependencies on ProcessQueue module | ProcessQueue |  |
| 4.0.0 | breaking | AfterStartup flow now returns a boolean value | AfterStartup |  |
| 4.0.0 | breaking | Input parameter name of scan Java action has been changed | scan Java action |  |
| 4.0.0 | migration-step | Include excluded ProcessQueue microflows if you want to keep using ProcessQueue | ProcessQueue |  |
| 3.1.0 | requirement | Minimum Mendix version upgraded to 7.23.17 |  |  |
| 3.0.0 | removal | Removed dependencies on other modules except ApprontoLicenser |  |  |
| 3.0.0 | breaking | Default behavior changed to NOT use ProcessQueue; include excluded flows if required | ProcessQueue |  |
| 2.0.1 | improvement | Updated com.fasterxml.jackson.* jar files | com.fasterxml.jackson |  |
| 2.0.0 | requirement | Upgraded to Mendix 7 |  |  |
