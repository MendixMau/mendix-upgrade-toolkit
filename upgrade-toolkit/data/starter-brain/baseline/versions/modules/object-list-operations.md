# Object List Operations (Marketplace component 117715)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/117715)

| version | published | min Mendix |
|---|---|---|
| 4.1.0 | 2026-04-10 | 11.9.0 |
| 4.0.0 | 2026-02-07 | 10.24.9 |
| 3.1.0 | 2024-09-13 | 9.18.0 |
| 3.0.0 | 2024-05-28 | 9.18.0 |
| 2.0.0 | 2024-04-04 | 8.18.1 |
| 1.1.0 | 2021-11-23 | 8.18.1 |
| 1.0.1 | 2021-10-26 | 8.18.1 |
| 1.0.0 | 2021-06-14 | 8.18.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 4.1.0 | migration-step | Replace deprecated IMendixObject.getMember(IContext, String) calls with IMendixObject.getMember(String). | IMendixObject.getMember(IContext, String), IMendixObject.getMember(String) | IMendixObject.getMember(String) |
| 4.1.0 | migration-step | Replace IMendixObjectMember.getState() == MemberState.CHANGED with IMendixObjectMember.isChanged(). | IMendixObjectMember.getState(), IMendixObjectMember.isChanged() | IMendixObjectMember.isChanged() |
| 4.0.0 | requirement | Mendix project version raised to 10.24.9 to make utilities available in Mx11. |  |  |
| 3.0.0 | requirement | Mendix project version raised to 9.18.0 to make utilities available in Mx10. |  |  |
| 2.0.0 | migration-step | Sample data pages, logic and entities moved to separate ListOperationsExamples module; no longer shipped with Java actions. | ListOperationsExamples |  |
| 2.0.0 | deprecation | V1 sorting versions moved to Deprecated folder; functionality unchanged to prevent breaking changes. | V1 sorting operations |  |
| 2.0.0 | breaking | V2 sorting Java actions renamed; V1 versions renamed to new names. | JA_List_MoveObjectToPosition, JA_List_PerformSortingAction, JA_List_SanitizeSorting |  |
| 2.0.0 | breaking | V2 sorting Java actions now return list of objects changed during execution. | JA_List_MoveObjectToPosition, JA_List_PerformSortingAction, JA_List_SanitizeSorting |  |
| 2.0.0 | breaking | Parameter AffectedList renamed to ProvidedList in sorting operations. | AffectedList, ProvidedList | ProvidedList |
| 2.0.0 | improvement | Sorting attribute now also accepts Long attributes. | sorting operations |  |
| 2.0.0 | breaking | New required parameter StartingIndex added to JA_List_SanitizeSorting; previously fixed at 1. | JA_List_SanitizeSorting, StartingIndex |  |
| 2.0.0 | breaking | New position parameter reworked; now must equal sorting attribute value of another object in provided list. | JA_List_MoveObjectToPosition, New position |  |
| 1.0.1 | fix | Fixed issue where Commit = false didn't update standalone object instance with new sort value. |  |  |
