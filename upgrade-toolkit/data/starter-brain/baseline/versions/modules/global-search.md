# Global Search (Marketplace component 115019)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/115019)

| version | published | min Mendix |
|---|---|---|
| 6.2.1 | 2025-03-11 | 9.24.28 |
| 6.2.0 | 2025-01-24 | 9.24.28 |
| 6.1.0 | 2024-10-02 | 9.24.28 |
| 6.0.1 | 2024-08-30 | 8.18.30 |
| 6.0.0 | 2024-08-29 | 8.18.30 |
| 5.0.0 | 2023-10-03 | 8.15.1 |
| 4.0.0 | 2022-09-28 | 8.12.7 |
| 3.0.0 | 2021-12-10 | 8.12.7 |
| 2.0.0 | 2021-02-16 | 8.6.4 |
| 1.0.0-beta2 | 2020-08-18 | 8.6.4 |
| 1.0.0-beta | 2020-08-17 | 8.6.4 |
| 1.0.0 | 2020-09-02 | 8.6.4 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 6.2.1 | breaking | Last remaining getParent() replaced by getPath(). | getParent(), getPath() | getPath() |
| 6.2.0 | requirement | Upgrade to latest 9.x version of Lucene, with 9.12.1 jar files included. | Lucene |  |
| 6.1.0 | requirement | Upgrade to latest Mx9 LTS version, making module compatible with Mx10. | Mendix |  |
| 6.0.1 | requirement | Upgrade to latest Mx8 LTS version. | Mendix |  |
| 6.0.1 | requirement | Major upgrade to Lucene 9.11.1 (latest version). | Lucene |  |
| 6.0.1 | feature | Extra Administrator module role for managing index data. | Administrator |  |
| 6.0.1 | breaking | getParent() method replaced by getPath(). | getParent(), getPath() | getPath() |
| 6.0.1 | migration-step | IndexWriter gets closed before zip-file creation (preferably in Bsd-flow). | IndexWriter |  |
| 6.0.1 | migration-step | Event handler for Indexing moved to AfterCommit. | Event handler |  |
| 6.0.1 | breaking | Implicit cast to String replaced by x.toString() for Advanced search. | Advanced search |  |
| 6.0.1 | known-issue | Sorting by weight/lucene score result not yet sorted out. | Sorting |  |
| 6.0.1 | known-issue | Deprecations from upgrading Lucene core not yet fixed. Will be done in future release. | Lucene |  |
| 6.0.0 | requirement | Upgrade to latest Mx8 LTS version. | Mendix |  |
| 6.0.0 | requirement | Major upgrade to Lucene 9.11.1 (latest version). | Lucene |  |
| 6.0.0 | feature | Extra Administrator module role for managing index data. | Administrator |  |
| 6.0.0 | breaking | getParent() method replaced by getPath(). | getParent(), getPath() | getPath() |
| 6.0.0 | migration-step | IndexWriter gets closed before zip-file creation (preferably in Bsd-flow). | IndexWriter |  |
| 6.0.0 | migration-step | Event handler for Indexing moved to AfterCommit. | Event handler |  |
| 6.0.0 | breaking | Implicit cast to String replaced by x.toString() for Advanced search. | Advanced search |  |
| 6.0.0 | known-issue | Sorting by weight/lucene score result not yet sorted out. | Sorting |  |
| 6.0.0 | known-issue | Deprecations from upgrading Lucene core not yet fixed. Will be done in future release. | Lucene |  |
| 5.0.0 | requirement | Upgrade to Mx 8.15.1. | Mendix |  |
| 5.0.0 | feature | Two new Java actions: IndexDataToFileDocument and FileDocumentToIndexData. | IndexDataToFileDocument, FileDocumentToIndexData |  |
| 5.0.0 | feature | Two new constants: IndexFileRestoreAfterStartup and IndexFileStoreBeforeShutdown. | IndexFileRestoreAfterStartup, IndexFileStoreBeforeShutdown |  |
| 5.0.0 | breaking | Changed behaviour of After startup flow and Before shutdown microflow to store index data in database. | After startup flow, Before shutdown microflow |  |
| 5.0.0 | migration-step | Index data management either on BSd and ASu or manually. | Index data |  |
| 5.0.0 | breaking | ACO on SearchableObject instead of BCO, allows use in task queues. Potential breaking change. | SearchableObject |  |
| 4.0.0 | breaking | Reworked module set-up. No more runtime configuration; everything reflected in Mendix model during development. |  |  |
| 4.0.0 | breaking | Entities searchable must inherit from SearchableObject. | SearchableObject |  |
| 4.0.0 | removal | Highlighting removed as it reduces search performance and introduces overhead. | Highlighting |  |
| 3.0.0 | feature | Compatibility with Mendix 9. | Mendix |  |
| 3.0.0 | requirement | Upgraded to Lucene 8.9. | Lucene |  |
| 2.0.0 | breaking | Wildcard search option replaced with advanced search query builder combining exact match, phrase search, wildcard search. | wildcard search | advanced search query builder |
| 2.0.0 | feature | After startup microflow to refresh indexes when restarting. | After startup microflow |  |
