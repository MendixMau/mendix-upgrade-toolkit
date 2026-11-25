# Workstation Connector (Mx 9) (Marketplace component 247460)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/247460)

| version | published | min Mendix |
|---|---|---|
| 4.2.0 | 2026-09-10 | 9.24.11 |
| 4.1.0 | 2026-08-13 | 9.24.11 |
| 4.0.0 | 2026-07-16 | 9.24.11 |
| 3.8.0 | 2026-06-18 | 9.24.11 |
| 3.6.0 | 2026-04-23 | 9.24.11 |
| 3.3.0 | 2026-01-08 | 9.24.11 |
| 3.2.0 | 2025-12-04 | 9.24.11 |
| 3.1.0 | 2025-11-07 | 9.24.11 |
| 3.0.0 | 2025-09-30 | 9.24.11 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 4.0.0 | feature | Workstation Connector now supports communication over a single WebSocket connection, enhancing performance. |  |  |
| 4.0.0 | feature | New SendDeviceRequest JSA introduced. Returns device response or error directly; requires Workstation Client 4.0 or later. | SendDeviceRequest JSA |  |
| 3.8.0 | breaking | Get/Create Device action now returns empty object instead of throwing error when no matching device found. | Get/Create Device action |  |
| 3.6.0 | feature | New set of Nanoflow Actions and Widget to simplify creation of reusable peripheral modules. | GetCreateDevice, SubscribeToObjectChanges JSA, WaitForObjectChanges JSA |  |
| 3.6.0 | feature | New nanoflow actions: Connect device, SendDeviceMessage, WaitForDeviceMessage for easier configuration. | Connect device, SendDeviceMessage, WaitForDeviceMessage |  |
| 3.6.0 | improvement | Model peripheral entity as specialization of device entity; no need for association. |  |  |
| 3.6.0 | improvement | Calling GetStation is not required anymore to initiate station connector; only required for reading configuration. | GetStation |  |
| 3.6.0 | deprecation | SendMessage has been deprecated; its wait for response behavior was often misleading or unnecessary. | SendMessage | SendDeviceMessage and WaitForDeviceMessage |
| 3.6.0 | deprecation | SubscribeToMessages and SubscribeToErrors deprecated; replaced by single action GetCreateDevice. | SubscribeToMessages, SubscribeToErrors | GetCreateDevice |
| 3.6.0 | breaking | Removed Station_User association; object garbage collection now handled internally for robust object management. | Station_User association |  |
