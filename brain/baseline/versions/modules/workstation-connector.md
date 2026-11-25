# Workstation Connector (Marketplace component 254335)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/254335)

| version | published | min Mendix |
|---|---|---|
| 4.2.0 | 2026-09-10 | 10.21.1 |
| 4.1.0 | 2026-08-13 | 10.21.1 |
| 4.0.0 | 2026-07-16 | 10.21.1 |
| 3.8.0 | 2026-06-18 | 10.21.1 |
| 3.6.0 | 2026-04-23 | 10.21.1 |
| 3.3.0 | 2026-01-23 | 10.21.1 |
| 3.2.0 | 2026-01-23 | 10.21.1 |
| 3.1.0 | 2026-01-23 | 10.21.1 |
| 3.0.0 | 2026-01-23 | 10.21.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 4.1.0 | fix | Fixed an issue that occasionally prevented the connector from successfully reconnecting to devices after Workstation Client downtime. | Connection stability |  |
| 4.0.0 | feature | Workstation Connector now supports communication over a single WebSocket connection, enhancing performance and simplifying network configurations. | WebSocket Communication |  |
| 4.0.0 | feature | New SendDeviceRequest JSA introduced. Returns device response or error directly, not passed to onMessage channel. Requires Workstation Client 4.0 or later. | SendDeviceRequest JSA |  |
| 4.0.0 | requirement | SendDeviceRequest JSA requires Workstation Client 4.0 or later for full utilization. | Workstation Client |  |
| 3.8.0 | breaking | Get/Create Device action now returns an empty object instead of throwing an error when no matching device is found. | Get/Create Device action |  |
| 3.6.0 | feature | New GetCreateDevice action to initialize and manage peripheral object creation in one single action. | GetCreateDevice, Initialize peripheral object |  |
| 3.6.0 | feature | Setup callbacks: On connect, On message, On disconnect to manage peripheral object events. | On connect, On message, On disconnect |  |
| 3.6.0 | feature | New widgets to trigger application level logic on device events: On change, On equal, On true, On load/unload actions. | On change, On equal, On true, On load/unload |  |
| 3.6.0 | feature | New SubscribeToObjectChanges JSA nanoflow action to react to object changes in real-time. | SubscribeToObjectChanges JSA |  |
| 3.6.0 | feature | New WaitForObjectChanges JSA nanoflow action to wait for specific object changes before proceeding. | WaitForObjectChanges JSA |  |
| 3.6.0 | feature | New Connect device nanoflow action for managing device connections. | Connect device |  |
| 3.6.0 | feature | New SendDeviceMessage and WaitForDeviceMessage nanoflow actions for easier configuration of most used cases. | SendDeviceMessage, WaitForDeviceMessage | SendMessage |
| 3.6.0 | improvement | Model peripheral entity as specialization of device entity; no association required. | peripheral entity, device entity |  |
| 3.6.0 | improvement | Calling GetStation is not required anymore to initiate station connector; only required for reading station configuration. | GetStation |  |
| 3.6.0 | deprecation | SendMessage deprecated; its wait for response behavior was misleading or unnecessary. Replaced by SendDeviceMessage and WaitForDeviceMessage. | SendMessage | SendDeviceMessage |
| 3.6.0 | deprecation | SubscribeToMessages and SubscribeToErrors deprecated and replaced by GetCreateDevice. | SubscribeToMessages, SubscribeToErrors | GetCreateDevice |
| 3.6.0 | breaking | Removed Station_User association. Object garbage collection now handled internally for more robust object management. | Station_User association |  |
| 3.6.0 | fix | Fixed an issue related to the timing of initial connections. | initial connections |  |
| 3.6.0 | fix | Fixed an issue when devices were sometimes discovered with a delay. | device discovery |  |
