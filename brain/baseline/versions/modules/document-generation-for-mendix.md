# Document Generation for Mendix (Marketplace component 2026)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Module, Emixa, Partner, [marketplace](https://marketplace.mendix.com/link/component/2026)

| version | published | min Mendix |
|---|---|---|
| 10.4.1 | 2026-06-17 | 10.21.0 |
| 10.4.0 | 2026-02-25 | 10.21.0 |
| 10.3.0 | 2026-01-30 | 10.21.0 |
| 10.2.0 | 2026-01-14 | 10.21.0 |
| 10.1.0 | 2025-12-01 | 10.21.0 |
| 9.0.0 | 2025-10-08 | 10.18.11 |
| 8.0.1 | 2025-08-20 | 9.18.0 |
| 8.0.0 | 2025-04-15 | 9.18.0 |
| 7.0.1 | 2024-05-21 | 9.18.0 |
| 7.0.0 | 2022-07-08 | 8.18.1 |
| 5.5.0 | 2020-04-09 | 7.23.10 |
| 5.4.0 | 2020-03-19 | 7.23.10 |
| 5.3.1 | 2020-02-13 | 7.23.10 |
| 5.2.1 | 2019-12-19 | 7.23.8 |
| 5.2.0 | 2019-12-12 | 7.23.8 |
| 5.1.0 | 2019-10-24 | 7.23.8 |
| 5.0.1 | 2019-03-04 | 7.2.0 |
| 5.0.0 | 2018-11-30 | 7.2.0 |
| 4.2.2 | 2017-09-12 | 7.2.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 10.4.1 | requirement | Added dependency on Nanoflow Commons module. | Nanoflow Commons |  |
| 10.4.1 | improvement | Improved flexibility by allowing changes in the connected microflow without blocking the save action. | Table_Save |  |
| 10.4.0 | fix | Fixed document generation issue where attributes accessed through 1-1 associations were not resolved correctly, causing XPath validation errors and failed merges. |  |  |
| 10.3.0 | improvement | Enhanced XPath validation to correctly handle associations targeting a generalized entity, including all underlying specializations as valid targets. |  |  |
| 10.2.0 | improvement | Added correct many-to-many validation for XPath processing using bidirectional navigability. |  |  |
| 10.1.0 | requirement | Module updated to Mendix 10.21.0. |  |  |
| 10.1.0 | feature | Fully compatible with Mendix 11, ensuring a smooth migration to the latest version. |  |  |
| 10.1.0 | fix | Fixed XPath validation issue that occurred when the same entity name was used across different modules. |  |  |
| 10.1.0 | fix | Fixed problem where quotation marks in Word IF/ELSE statements caused errors, now correctly escaped using {QUOTE 34}. |  |  |
| 10.1.0 | migration-step | Clean up userlib to avoid conflicts with old or duplicate libraries. |  |  |
| 9.0.0 | requirement | Upgrade to Mendix 10 (version 10.18.11 or higher) with React client compatibility. |  |  |
| 8.0.1 | removal | Removed commons-lang-2.5.jar dependency. | commons-lang-2.5.jar |  |
| 8.0.0 | removal | Removed the dependency on the Mx Model Reflection module. | Mx Model Reflection |  |
| 8.0.0 | feature | Introduced configuration validation for templates, ensuring that required tables and fields are correctly defined. |  |  |
| 8.0.0 | feature | Added support for validating fields using XPath expressions. |  |  |
| 8.0.0 | migration-step | Replace the afterstartup ASU_DocumentGenerationForMendix_ActivateLicense with ASU_DocumentGenerationForMendix. | ASU_DocumentGenerationForMendix_ActivateLicense, ASU_DocumentGenerationForMendix | ASU_DocumentGenerationForMendix |
| 7.0.1 | migration-step | Clean up userlib; documentgenerationformendix-1.0.0.jar is added. |  |  |
| 7.0.1 | feature | This release is Mendix 10 compatible. |  |  |
| 5.2.1 | migration-step | Rename TemplateType to TemplateConfiguration first, do not run the model, download new version, update Community Commons if needed, and fix references to layouts and pages. | TemplateType, TemplateConfiguration | TemplateConfiguration |
| 5.2.0 | breaking | TemplateType has been renamed to TemplateConfiguration. | TemplateType | TemplateConfiguration |
| 5.1.0 | feature | Compatible with Mendix 8. |  |  |
| 5.1.0 | requirement | Use newest version of CommunityCommons and MxModelreflection. | CommunityCommons, MxModelreflection |  |
| 5.0.0 | requirement | Upgraded to Mendix 7.18.1 to make use of native REST capabilities. |  |  |
| 5.0.0 | feature | Full compatibility with MS Word Add-in from Microsoft Office Appstore. |  |  |
