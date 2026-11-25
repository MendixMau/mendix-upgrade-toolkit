# MQTT Connector (Marketplace component 119508)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Service, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/119508)

| version | published | min Mendix |
|---|---|---|
| 3.0.1 | 2026-09-15 | 10.24.11 |
| 3.0.0 | 2026-08-18 | 10.24.11 |
| 2.2.1 | 2026-05-21 | 10.24.11 |
| 2.2.0 | 2025-12-15 | 10.24.11 |
| 2.1.1 | 2025-10-08 | 10.21.0 |
| 2.1.0 | 2025-04-25 | 10.21.0 |
| 2.0.0 | 2025-01-22 | 10.12.10 |
| 1.7.2 | 2026-05-21 | 9.24.11 |
| 1.7.1 | 2025-12-15 | 9.24.11 |
| 1.7.0 | 2024-05-27 | 9.24.11 |
| 1.6.0 | 2023-11-10 | 9.24.11 |
| 1.5.0 | 2023-10-25 | 9.24.9 |
| 1.4.0 | 2023-09-26 | 9.18.4 |
| 1.3.0 | 2023-04-05 | 9.18.4 |
| 1.2.0 | 2022-10-13 | 9.1.1 |
| 1.1.1 | 2022-09-06 | 9.1.1 |
| 1.1.0 | 2022-05-02 | 9.1.1 |
| 1.0.0 | 2022-01-24 | 9.1.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 3.0.1 | improvement | Updated MQTT Connector userlib jars | userlib jars |  |
| 3.0.0 | breaking | Upgraded MQTT client from Eclipse Paho v3 to v5 | Eclipse Paho MQTT client |  |
| 3.0.0 | improvement | Upgraded BouncyCastle jar to v1.85 | BouncyCastle jar |  |
| 2.2.1 | improvement | Upgraded bouncy castle jar to v1.84 | bouncy castle jar |  |
| 2.2.1 | improvement | Removed TLSv1.2 constraint from MQTT | MQTT |  |
| 2.2.0 | requirement | Upgraded module to Studio Pro version 10.24.11 | Studio Pro |  |
| 2.2.0 | improvement | Upgraded data widget to latest available version | data widget |  |
| 2.1.1 | fix | Fixed event tracking library missing error (#255814), delete eventTrackingLibrary*.jar from userlib | eventTrackingLibrary jar |  |
| 2.1.1 | improvement | Upgraded bouncycastle jar to v1.81 | bouncycastle jar |  |
| 2.1.0 | requirement | Updated studio pro minimum version to 10.21.0 to support Mendix 11 | Studio Pro |  |
| 2.1.0 | improvement | Upgraded 3rd party jars and widgets | 3rd party jars, widgets |  |
| 2.0.0 | requirement | Upgraded the module to Mendix version 10.12.10 | Mendix |  |
| 2.0.0 | breaking | Replaced old UI components with new ones compatible with the React Client | UI components |  |
| 2.0.0 | improvement | Upgraded the Combobox widget to version 2.1.3 | Combobox widget |  |
| 2.0.0 | improvement | Upgraded Data Widgets to version 2.29.0 | Data Widgets |  |
| 1.7.2 | improvement | Upgraded bouncy castle jar to v1.84 | bouncy castle jar |  |
| 1.7.2 | improvement | Removed TLSv1.2 constraint from MQTT | MQTT |  |
| 1.7.1 | improvement | Upgraded bouncycastle to 1.81 along with some other test dependencies | bouncycastle jar |  |
| 1.7.1 | improvement | Upgraded Switch widget to latest available version | Switch widget |  |
| 1.6.0 | requirement | Upgraded module to Mendix version 9.24.11 | Mendix |  |
| 1.5.0 | requirement | Upgraded module to Mendix version 9.24.9 | Mendix |  |
| 1.4.0 | migration-step | Introduction of migration file for JDM | JDM |  |
| 1.3.0 | requirement | Updated module to Mendix version 9.18.4 | Mendix |  |
| 1.1.1 | migration-step | Before updating delete MqttConnector-1.0.0-all.jar file from userlib folder | MqttConnector-1.0.0-all.jar |  |
| 1.1.1 | improvement | Upgraded Bouncy Castle jars to 1.70 | Bouncy Castle jars |  |
