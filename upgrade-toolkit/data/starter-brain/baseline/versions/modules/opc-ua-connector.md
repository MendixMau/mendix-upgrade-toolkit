# OPC UA Connector (Marketplace component 230843)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/230843)

| version | published | min Mendix |
|---|---|---|
| 2.3.0 | 2026-08-13 | 10.24.0 |
| 2.2.0 | 2026-04-02 | 10.24.0 |
| 2.1.0 | 2026-02-18 | 10.24.0 |
| 2.0.3 | 2025-09-25 | 10.21.0 |
| 2.0.2 | 2025-08-20 | 10.21.0 |
| 2.0.1 | 2025-06-12 | 10.21.0 |
| 2.0.0 | 2025-05-12 | 10.21.0 |
| 1.3.0 | 2026-08-13 | 9.24.3 |
| 1.2.0 | 2026-04-02 | 9.24.3 |
| 1.1.3 | 2026-02-18 | 9.24.3 |
| 1.1.2 | 2025-09-25 | 9.24.3 |
| 1.1.1 | 2025-08-20 | 9.24.3 |
| 1.1.0 | 2025-04-10 | 9.24.3 |
| 1.0.1 | 2024-11-20 | 9.24.3 |
| 1.0.0 | 2024-09-23 | 9.24.3 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.3.0 | improvement | Improved automatic recovery from stale OPC UA sessions. | OPC UA sessions |  |
| 2.3.0 | feature | Added automatic recreation of missing subscriptions after reconnection or transfer failures. | subscriptions |  |
| 2.3.0 | improvement | Improved validation, error handling, logging, and thread safety. |  |  |
| 2.3.0 | security | Updated Netty and Bouncy Castle dependencies to address known vulnerabilities. | Netty, Bouncy Castle |  |
| 2.3.0 | improvement | Improved certificate handling, browsing, and monitored-item state management. | certificate handling, browsing, monitored-item state management |  |
| 2.2.0 | feature | Added advanced configuration options to influence the server's certificate validation. | certificate validation |  |
| 2.1.0 | requirement | Updated to Mendix version 10.24.0. | Mendix |  |
| 2.1.0 | improvement | Updated netty-io dependencies. | netty-io |  |
| 2.0.3 | improvement | Updated dependencies of bouncycastle and netty. | bouncycastle, netty |  |
| 2.0.2 | breaking | Removed Before delete event from Subscription entity. | Subscription |  |
| 2.0.2 | fix | Fixed dependencies in module settings. | module settings |  |
| 2.0.1 | migration-step | Replaced deprecated context() method with getContext(). | context() | getContext() |
| 2.0.0 | requirement | Upgraded to Mendix version 10.21.0. | Mendix |  |
| 1.3.0 | improvement | Improved automatic recovery from stale OPC UA sessions. | OPC UA sessions |  |
| 1.3.0 | feature | Added automatic recreation of missing subscriptions after reconnection or transfer failures. | subscriptions |  |
| 1.3.0 | improvement | Improved validation, error handling, logging, and thread safety. |  |  |
| 1.3.0 | security | Updated Netty and Bouncy Castle dependencies to address known vulnerabilities. | Netty, Bouncy Castle |  |
| 1.3.0 | improvement | Improved certificate handling, browsing, and monitored-item state management. | certificate handling, browsing, monitored-item state management |  |
| 1.2.0 | feature | Added advanced configuration options to influence the server's certificate validation. | certificate validation |  |
| 1.1.3 | improvement | Updated bouncycastle and netty-io dependencies. | bouncycastle, netty-io |  |
| 1.1.2 | improvement | Updated dependencies of bouncycastle and netty. | bouncycastle, netty |  |
| 1.1.1 | breaking | Removed Before delete event from Subscription entity. | Subscription |  |
| 1.1.1 | fix | Fixed dependencies so correct libraries load when upgrading to Mendix 10 or importing to Mendix 10. |  |  |
| 1.1.0 | security | Fixed vulnerabilities in used libraries. |  |  |
| 1.0.1 | improvement | Connector is now fully compatible with React client in 10.12+. | React client |  |
