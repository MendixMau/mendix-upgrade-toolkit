# AWS Lambda Connector (Marketplace component 204511)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/204511)

| version | published | min Mendix |
|---|---|---|
| 3.0.1 | 2026-02-19 | 10.21.0 |
| 2.1.0 | 2024-09-27 | 9.24.2 |
| 2.0.0 | 2024-03-08 | 9.18.0 |
| 1.1.2 | 2024-01-23 | 9.18.0 |
| 1.0.0 | 2022-11-22 | 9.18.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 3.0.1 | requirement | Minimum Mendix version upgraded to 10.21.0 | Mendix |  |
| 3.0.1 | breaking | All third party jar dependencies now configured in module itself; removed from user lib | third party jar dependencies |  |
| 2.1.0 | improvement | Upgraded Lambda SDK to 2.27.17 | Lambda SDK |  |
| 2.0.0 | requirement | Connector now requires Authentication Connector 3.0 or newer | Authentication Connector |  |
| 2.0.0 | breaking | IsAsynchonous replaced with InvocationType enum | IsAsynchonous | InvocationType |
| 1.1.2 | migration-step | Migration file added for Mendix 10.3+ to rebuild dependencies with Java Dependency Management | Java Dependency Management |  |
