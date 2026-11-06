# Workstation Client Portable (Marketplace component 247456)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Service, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/247456)

| version | published | min Mendix |
|---|---|---|
| 4.2.1 | 2026-09-15 | 9.24.11 |
| 4.2.0 | 2026-09-10 | 9.24.11 |
| 4.1.0 | 2026-08-13 | 9.24.11 |
| 4.0.0 | 2026-07-16 | 9.24.11 |
| 3.8.0 | 2026-06-18 | 9.24.11 |
| 3.7.0 | 2026-05-21 | 9.24.11 |
| 3.6.0 | 2026-04-23 | 9.24.11 |
| 3.5.0 | 2026-03-12 | 9.24.11 |
| 3.4.0 | 2026-02-12 | 9.24.11 |
| 3.3.0 | 2026-01-08 | 9.24.11 |
| 3.2.0 | 2025-12-04 | 9.24.11 |
| 3.1.0 | 2025-11-07 | 9.24.11 |
| 3.0.0 | 2025-09-30 | 9.24.11 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 4.1.0 | improvement | Client now sends detailed installation information (Client Type) to the Management system, providing better visibility into your deployment | client reporting, Management system |  |
| 4.1.0 | improvement | Refactored how devices are managed to ensure they consistently report their status as available, connected, or in an error state | device states, management |  |
| 4.0.0 | feature | Workstation Client now generates and sends an anonymized Client ID, derived from the machine's hardware/OS identifier, to the Management server | Client ID Reporting |  |
| 4.0.0 | feature | Workstation Client can now connect to multiple devices over a single WebSocket connection, improving efficiency and reducing overhead | WebSocket Connection |  |
| 4.0.0 | feature | Client now supports the new SendDeviceRequest API, allowing for more direct and streamlined communication with devices | SendDeviceRequest API |  |
| 4.0.0 | fix | Fixed issues with non-UTF-8 delimiter/suffix encoding in serial, TCP-IP client, and TCP-IP server devices, ensuring reliable data transmission | Serial, TCP-IP client, TCP-IP server |  |
| 3.8.0 | fix | Fixed an issue where the client blocked sign-in to Studio Pro when six or more devices were configured, due to an overlap in port usage | Studio Pro Login, port usage |  |
| 3.6.0 | improvement | Updated the underlying dependencies for the smart card reader functionality, enhancing stability and compatibility | smart card reader, dependencies |  |
| 3.1.0 | fix | Fixed an issue where the Workstation Client could not connect to Workstation Management over a network connection that required a certificate. Client now uses the operating system's certificates | Computer registration, certificate |  |
