# Amazon Rekognition Connector (Marketplace component 204717)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/204717)

| version | published | min Mendix |
|---|---|---|
| 3.0.1 | 2026-02-19 | 10.21.0 |
| 2.0.0 | 2023-12-18 | 9.18.0 |
| 1.2.2 | 2023-08-01 | 9.18.0 |
| 1.1.0 | 2022-12-19 | 9.12.2 |
| 1.0.1 | 2022-11-24 | 9.12.2 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 3.0.1 | requirement | Minimum Mendix version raised to 10.21.0 |  |  |
| 3.0.1 | migration-step | All third party jar dependencies now configured in module; remove them from user lib |  |  |
| 2.0.0 | requirement | Connector requires Authentication Connector 3.0 or newer versions | Authentication Connector |  |
| 1.1.0 | fix | Fixed 400 bad request issue for authentication through session-based credentials |  |  |
| 1.0.1 | fix | Fixed issue that occurred when using the latest version of AWSAuthentication | AWSAuthentication |  |
