# AWS Authentication Connector (Marketplace component 120333)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/120333)

| version | published | min Mendix |
|---|---|---|
| 4.1.4 | 2026-04-29 | 10.21.0 |
| 4.0.0 | 2025-04-14 | 10.21.0 |
| 3.2.3 | 2025-09-30 | 9.24.2 |
| 3.1.3 | 2024-09-19 | 9.18.0 |
| 3.0.2 | 2024-03-05 | 9.18.0 |
| 2.3.2 | 2023-11-27 | 9.18.0 |
| 2.1.2 | 2023-03-28 | 9.12.1 |
| 2.0.1 | 2022-11-15 | 9.12.1 |
| 1.0.1 | 2022-09-15 | 9.12.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 4.1.4 | breaking | Changed fixed length String attributes in Domain Model to unlimited, including Sig4Header calculation entity. | String attributes in Domain Model |  |
| 4.1.4 | fix | Bugfix in calculating Sig4 Header by encoding canonical path, excluded forward slashes, before signing. | Sig4Header calculation |  |
| 4.0.0 | requirement | Upgraded to Mendix 10.21.0, added Java dependencies to module settings. | Mendix |  |
| 3.2.3 | security | Fixed vulnerabilities in netty-handler and netty-commons libraries. | netty-handler, netty-commons |  |
| 3.2.3 | breaking | Removed widgets folder from package, no longer forcing widget definitions on project download. | widgets folder |  |
| 2.3.2 | fix | Bug fix to make Authentication compatible with textract 1.2.2. | textract |  |
| 2.0.1 | fix | Bug fix - Update in Domain model. | Domain model |  |
| 1.0.1 | security | Security fix - updated userlib removed unused jar files. | userlib |  |
