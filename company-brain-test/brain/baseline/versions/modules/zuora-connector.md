# Zuora Connector (Marketplace component 114782)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/114782)

| version | published | min Mendix |
|---|---|---|
| 3.0.1 | 2024-07-16 | 9.24.24 |
| 3.0.0 | 2024-07-06 | 9.24.23 |
| 2.3.0 | 2024-01-12 | 9.24.14 |
| 2.2.2 | 2024-01-10 | 9.24.14 |
| 2.1.2 | 2023-12-21 | 9.24.12 |
| 2.1.1 | 2023-12-20 | 9.24.12 |
| 2.1.0 | 2023-12-19 | 9.24.12 |
| 2.0.1 | 2023-04-21 | 9.24.1 |
| 2.0.0 | 2023-02-17 | 9.18.4 |
| 1.3.0 | 2022-12-02 | 9.6.14 |
| 1.2.0 | 2021-06-07 | 8.18.6 |
| 1.1.1 | 2021-06-01 | 8.6.9 |
| 1.1.0 | 2020-08-07 | 8.6.5 |
| 1.0.0 | 2020-08-05 | 8.6.5 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 3.0.1 | breaking | zObject updated_time and created_time are now date time attributes | zObject.updated_time, zObject.created_time |  |
| 3.0.0 | breaking | Migrated majority of domain model and actions to V2 API with different naming conventions; entities and attributes renamed or deleted |  |  |
| 3.0.0 | requirement | Upgrade to Mendix 9.24.23 |  |  |
| 2.3.0 | migration-step | json-20200518.jar.zuoraconnector.RequiredLib no longer required as of 2.2.0; delete from userlib if unused | json-20200518.jar.zuoraconnector.RequiredLib |  |
| 2.2.2 | breaking | Removed wrapper entities; deleted OrderActions, Subscriptions, CustomField, SubscriptionRatePlan entities | OrderActions, Subscriptions, CustomField, SubscriptionRatePlan |  |
| 2.2.2 | breaking | Renamed OrderActionWrapper entity to Array | OrderActionWrapper | Array |
| 2.2.2 | breaking | Changed return value for SUB_Contact_Create and SUB_Contact_Update to Contact instead of ZuoraResponse | SUB_Contact_Create, SUB_Contact_Update |  |
| 2.2.2 | breaking | Renamed some microflow actions to better reflect the objects involved |  |  |
| 2.0.1 | requirement | Upgraded to Mendix 9.24.1 |  |  |
| 2.0.0 | breaking | Refactored module and logic; upgrading can break existing implementation |  |  |
| 2.0.0 | requirement | Upgraded to Mendix 9.18.4 |  |  |
| 1.3.0 | security | Added encryption to Authorization Token and removed read access for improved security | Authorization Token |  |
| 1.2.0 | requirement | Upgraded to Mendix 8.18.6 |  |  |
