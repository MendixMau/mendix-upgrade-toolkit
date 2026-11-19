# Mendix Feedback Module (Marketplace component 205506)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/205506)

| version | published | min Mendix |
|---|---|---|
| 5.0.0 | 2026-06-16 | 10.24.0 |
| 4.1.1 | 2026-02-06 | 10.21.0 |
| 4.0.4 | 2025-12-04 | 10.21.0 |
| 4.0.3 | 2025-10-14 | 10.21.0 |
| 4.0.2 | 2025-07-18 | 10.21.0 |
| 4.0.1 | 2025-05-20 | 10.21.0 |
| 4.0.0 | 2025-04-25 | 10.21.0 |
| 3.1.0 | 2025-04-25 | 9.24.0 |
| 3.0.0 | 2024-09-20 | 9.24.0 |
| 2.0.1 | 2024-08-12 | 9.24.0 |
| 2.0.0 | 2024-07-26 | 9.24.0 |
| 1.4.1 | 2024-03-14 | 9.18.6 |
| 1.4.0 | 2024-02-02 | 9.18.6 |
| 1.3.2 | 2023-11-03 | 9.18.6 |
| 1.3.1 | 2023-10-31 | 9.18.6 |
| 1.3.0 | 2023-10-27 | 9.18.6 |
| 1.2.1 | 2023-09-27 | 9.18.6 |
| 1.2.0 | 2023-07-13 | 9.18.6 |
| 1.1.1 | 2023-04-14 | 9.18.5 |
| 1.1.0 | 2023-04-11 | 9.18.5 |
| 1.0.0 | 2022-12-13 | 9.12.2 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 5.0.0 | requirement | Minimum LTS support is now Mendix Studio Pro 10.24.0 |  |  |
| 5.0.0 | improvement | Updated XSS_Sanitizer & ValidateEmail java actions to remove unwanted console log runtime messages on app startup. | XSS_Sanitizer, ValidateEmail |  |
| 4.1.1 | fix | Resolved issue where Feedback widget could break Mendix page layout when React client was disabled. | Feedback widget |  |
| 4.1.1 | breaking | PopulateAttributes microflow has been updated; may need to reassign attributes within it. | PopulateAttributes |  |
| 4.0.2 | fix | Default Feedback button did not open modal pop-up in Mendix Studio Pro 10.24+ due to hidden nanoflow configuration being ignored. | Feedback button |  |
| 4.0.2 | fix | Local storage JavaScript actions in DS_Feedback_Populate nanoflow did not function properly, causing failures in retrieving feedback metadata. | DS_Feedback_Populate |  |
| 4.0.2 | fix | Exposing custom JavaScript actions as nanoflow actions caused conflicts with default actions. |  |  |
| 4.0.1 | fix | When Strict Mode is enabled, feedback local storage meta data is now correctly captured and saved. |  |  |
| 4.0.0 | improvement | Feedback Module is now compatible with React client enabled in Mendix apps. | Feedback Module |  |
| 4.0.0 | breaking | Feedback widget now uses new functionality to open modal form; no longer backwards compatible with Mendix Studio Pro versions earlier than v10.15.0. | Feedback widget |  |
| 3.1.0 | known-issue | Not compatible with Strict Mode (Mendix 10.12.0+). Use Feedback Module v4.0.1 or higher. |  |  |
| 3.0.0 | removal | Removed all example translation pages; translations now handled using batch translations tool. |  |  |
| 3.0.0 | migration-step | Feedback widget must be manually deleted and re-added on page to re-sync Studio Pro localization with new XML translation definitions. | Feedback widget |  |
| 3.0.0 | migration-step | Use batch translate tool to change translations on ShareFeedback modal pages or Screenshot & Annotation button labels. | ShareFeedback, Screenshot, Annotation |  |
| 2.0.1 | fix | Fixed incorrectly assigned nanoflows used in translated ShareFeedback modal pop-up pages. | ShareFeedback |  |
| 2.0.0 | feature | Feedback widget reengineered using Mendix; extensive customization options for button placement, form triggering, styling, and copy. | Feedback widget |  |
| 1.2.0 | feature | Added compatibility with Mendix SSO 4.0.2 and above. |  |  |
| 1.2.0 | improvement | Submitting user details now provided via datasource attributes. |  |  |
| 1.2.0 | removal | Removed DS_GetCurrentIDToken microflow from module. | DS_GetCurrentIDToken |  |
| 1.2.0 | breaking | Renamed Authentication tab to User Info and made configuration more intuitive. | Authentication tab | User Info |
| 1.1.1 | breaking | Removed default App ID from Feedback Widget Building Block. | Feedback Widget |  |
| 1.1.0 | breaking | Feedback submit success image is now optional instead of having default fallback. |  |  |
