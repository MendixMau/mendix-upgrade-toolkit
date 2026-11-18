# PDF Document Generation (Marketplace component 211553)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/211553)

| version | published | min Mendix |
|---|---|---|
| 2.1.4 | 2025-09-04 | 10.21.0 |
| 2.1.3 | 2025-08-06 | 10.21.0 |
| 2.1.2 | 2025-07-17 | 10.21.0 |
| 2.1.1 | 2025-07-04 | 10.21.0 |
| 2.1.0 | 2025-06-23 | 10.21.0 |
| 2.0.1 | 2025-05-26 | 10.21.0 |
| 2.0.0 | 2025-05-02 | 10.21.0 |
| 1.11.4 | 2025-09-04 | 9.24.0 |
| 1.11.3 | 2025-08-06 | 9.24.0 |
| 1.11.2 | 2025-07-17 | 9.24.0 |
| 1.11.1 | 2025-07-03 | 9.24.0 |
| 1.11.0 | 2025-06-23 | 9.24.0 |
| 1.10.3 | 2025-05-26 | 9.24.0 |
| 1.10.2 | 2025-03-31 | 9.24.0 |
| 1.10.1 | 2025-02-20 | 9.24.0 |
| 1.10.0 | 2024-11-01 | 9.24.0 |
| 1.9.0 | 2024-06-05 | 9.24.0 |
| 1.8.0 | 2024-04-25 | 9.18.0 |
| 1.7.0 | 2024-03-14 | 9.18.0 |
| 1.6.0 | 2024-03-01 | 9.18.0 |
| 1.5.0 | 2024-01-23 | 9.18.0 |
| 1.4.0 | 2024-01-12 | 9.18.0 |
| 1.3.0 | 2023-12-04 | 9.18.0 |
| 1.2.1 | 2023-10-24 | 9.18.0 |
| 1.2.0 | 2023-09-18 | 9.18.0 |
| 1.1.1 | 2023-09-07 | 9.18.0 |
| 1.1.0 | 2023-08-29 | 9.18.0 |
| 1.0.0 | 2023-05-31 | 9.18.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.1.4 | fix | Fixed document generation failing with wait for content exception if any network request fails while navigating to document page. |  |  |
| 2.1.4 | known-issue | Cloud service media queries evaluated incorrectly, resulting in unexpected widths for layout grids and widgets in PDF. | layout grids |  |
| 2.1.3 | improvement | Updated commons-lang3 dependency to version 3.18.0. | commons-lang3 |  |
| 2.1.3 | improvement | Updated local service to version 2.3.4. | local service |  |
| 2.1.3 | known-issue | Cloud service media queries evaluated incorrectly, resulting in unexpected widths for layout grids and widgets in PDF. | layout grids |  |
| 2.1.2 | fix | Fixed issue introduced in 2.1.1 where updating would not replace Redirect widget and fail document generation. | Redirect widget |  |
| 2.1.2 | known-issue | Cloud service media queries evaluated incorrectly, resulting in unexpected widths for layout grids and widgets in PDF. | layout grids |  |
| 2.1.1 | fix | Fixed document generation failing with client error 'mx.data.action is disabled' when running with Strict mode enabled for React client. |  |  |
| 2.1.1 | known-issue | Cloud service media queries evaluated incorrectly, resulting in unexpected widths for layout grids and widgets in PDF. | layout grids |  |
| 2.1.0 | feature | Added new service type 'Private' supporting private PDF document generation service hosted and managed by customer. |  |  |
| 2.1.0 | known-issue | Cloud service media queries evaluated incorrectly, resulting in unexpected widths for layout grids and widgets in PDF. | layout grids |  |
| 2.1.0 | known-issue | Document generation fails with client error 'mx.data.action is disabled' when running with Strict mode enabled for React client. |  |  |
| 2.0.1 | fix | Fixed issue where document generation could intermittently result in runtime exception whilst processing document result. |  |  |
| 2.0.1 | known-issue | Cloud service media queries evaluated incorrectly, resulting in unexpected widths for layout grids and widgets in PDF. | layout grids |  |
| 2.0.1 | known-issue | Document generation fails with client error 'mx.data.action is disabled' when running with Strict mode enabled for React client. |  |  |
| 2.0.0 | requirement | Upgraded module to Mendix version 10.21.0 for compatibility with Mendix 11. |  |  |
| 2.0.0 | improvement | Updated Atlas Core compatibility to version 3.17.0. | Atlas Core |  |
| 2.0.0 | improvement | Updated Atlas Web Content compatibility to version 3.8.0. | Atlas Web Content |  |
| 2.0.0 | improvement | Updated Data Widgets compatibility to version 2.31.0. | Data Widgets |  |
| 2.0.0 | improvement | Updated Combo Box widget compatibility to version 2.3.0. | Combo Box widget |  |
| 2.0.0 | known-issue | Cloud service media queries evaluated incorrectly, resulting in unexpected widths for layout grids and widgets in PDF. | layout grids |  |
| 2.0.0 | known-issue | Document generation fails with client error 'mx.data.action is disabled' when running with Strict mode enabled for React client. |  |  |
| 1.11.4 | fix | Fixed document generation failing with wait for content exception if any network request fails while opening document page. |  |  |
| 1.11.3 | improvement | Updated commons-lang3 dependency to version 3.18.0. | commons-lang3 |  |
| 1.11.3 | improvement | Updated local service to version 2.3.4. | local service |  |
| 1.11.2 | fix | Fixed issue introduced in 1.11.1 where updating would not replace Redirect widget and fail document generation. | Redirect widget |  |
| 1.11.1 | fix | Fixed document generation failing with client error 'mx.data.action is disabled' when running with Strict mode enabled for React client. |  |  |
| 1.11.1 | known-issue | Cloud service media queries evaluated incorrectly, resulting in unexpected widths for layout grids and widgets in PDF. | layout grids |  |
| 1.11.0 | feature | Added new service type 'Private' supporting private PDF document generation service hosted and managed by customer. |  |  |
| 1.11.0 | known-issue | Cloud service media queries evaluated incorrectly, resulting in unexpected widths for layout grids and widgets in PDF. | layout grids |  |
| 1.11.0 | known-issue | Document generation fails with client error 'mx.data.action is disabled' when running with Strict mode enabled for React client. |  |  |
| 1.10.3 | fix | Fixed issue where document generation could intermittently result in runtime exception whilst processing document result. |  |  |
| 1.10.3 | known-issue | Cloud service media queries evaluated incorrectly, resulting in unexpected widths for layout grids and widgets in PDF. | layout grids |  |
| 1.10.2 | improvement | Updated Combo Box compatibility to v1.7.1. | Combo Box |  |
| 1.10.2 | known-issue | Cloud service media queries evaluated incorrectly, resulting in unexpected widths for layout grids and widgets in PDF. | layout grids |  |
| 1.10.1 | known-issue | Testing PDF document generation locally using Chrome or Chromium version 117 or 118 might result in different scaling compared to Chromium version 112. |  |  |
| 1.10.1 | known-issue | Cloud service media queries evaluated incorrectly, resulting in unexpected widths for layout grids and widgets in PDF. | layout grids |  |
| 1.10.0 | feature | Added support for custom 'URL prefix' runtime setting for apps running in Mendix 10.5.0 or higher. |  |  |
| 1.10.0 | improvement | Upgraded 'axios' library used in local service to v1.7.7. | axios |  |
| 1.10.0 | removal | Removed dependency on 'commons-io' library; remove corresponding files from userlib folder after upgrading. | commons-io |  |
| 1.10.0 | migration-step | Remove 'commons-io-2.11.0.DocumentGeneration' files and 'commons-io-2.11.0.jar' from userlib folder if not used by other modules. | commons-io |  |
| 1.10.0 | known-issue | Testing PDF document generation locally using Chrome or Chromium version 117 or 118 might result in different scaling compared to Chromium version 112. |  |  |
| 1.10.0 | known-issue | Cloud service media queries evaluated incorrectly, resulting in unexpected widths for layout grids and widgets in PDF. | layout grids |  |
| 1.9.0 | requirement | Upgraded module to Mendix 9.24.0. |  |  |
| 1.9.0 | feature | Added support for React client, introduced as public beta in Mendix 10.7.0. |  |  |
| 1.9.0 | breaking | Switched to new Combo Box widget for selecting deployment type when registering app environment. | Combo Box widget | Combo Box widget |
| 1.9.0 | requirement | Ensure Combo Box widget is installed in project. | Combo Box widget |  |
| 1.9.0 | known-issue | Importing module in Mendix 10.6.0+ might raise consistency error CE6087 for renamed design properties; update all renamed design properties. |  |  |
| 1.9.0 | known-issue | Testing PDF document generation locally using Chrome or Chromium version 117 or 118 might result in different scaling compared to Chromium version 112. |  |  |
| 1.9.0 | known-issue | Cloud service media queries evaluated incorrectly, resulting in unexpected widths for layout grids and widgets in PDF. | layout grids |  |
| 1.8.0 | known-issue | Testing PDF document generation locally using Chrome or Chromium version 117 or 118 might result in different scaling compared to Chromium version 112. |  |  |
| 1.7.0 | known-issue | Chrome/Chromium 117-118 local testing produces different PDF scaling than service's Chromium 112. Fixed in Chrome 119. |  |  |
| 1.6.0 | known-issue | Chrome/Chromium 117-118 local testing produces different PDF scaling than service's Chromium 112. Fixed in Chrome 119. |  |  |
| 1.5.0 | known-issue | Chrome/Chromium 117-118 local testing produces different PDF scaling than service's Chromium 112. Fixed in Chrome 119. |  |  |
| 1.4.0 | known-issue | Chrome/Chromium 117-118 local testing produces different PDF scaling than service's Chromium 112. Fixed in Chrome 119. |  |  |
| 1.3.0 | breaking | App environment registration now requires personal access token (PAT) instead of developer API key. Existing registrations remain valid. |  |  |
| 1.3.0 | known-issue | Chrome/Chromium 117-118 local testing produces different PDF scaling than service's Chromium 112. Fixed in Chrome 119. |  |  |
| 1.2.1 | breaking | Aligned behavior between local and online service: redirects to external URLs are no longer allowed. |  |  |
| 1.2.1 | known-issue | Chrome/Chromium 117-118 local testing produces different PDF scaling than service's Chromium 112. Fixed in Chrome 119. |  |  |
| 1.2.0 | migration-step | Included migration file for Java dependencies for Studio Pro 10 compatibility. |  |  |
| 1.2.0 | known-issue | Chrome/Chromium 117-118 local testing produces different PDF scaling than service's Chromium 112. Fixed in Chrome 119. |  |  |
| 1.1.1 | fix | Fixed timeout issue when generating document with custom Mendix Runtime setting ApplicationRootURL to custom domain. | ApplicationRootURL |  |
| 1.1.1 | known-issue | Chrome/Chromium 117+ local testing produces different PDF scaling than cloud service. Use recommended Chromium version locally. |  |  |
| 1.1.0 | improvement | Use time zone of 'Generate as user' for date/time localization; fall back to App Settings or UTC. |  |  |
| 1.1.0 | improvement | No longer require Create and Write access rights for 'Generate as user' property user. |  |  |
| 1.1.0 | removal | Remove dependency on FieldSet widget. | FieldSet widget |  |
| 1.1.0 | removal | Remove RedirectLayout from the module. | RedirectLayout |  |
| 1.1.0 | removal | Remove constants UseCustomApplicationUrl and CustomApplicationUrl; use Application Root URL or App URL. | UseCustomApplicationUrl, CustomApplicationUrl |  |
| 1.1.0 | breaking | Cannot use @media print for PDF-specific styles; use document-generation-body-injected or document-content classes instead. | @media print | document-generation-body-injected |
| 1.1.0 | breaking | Wait until no pending network requests remain; long polling network requests no longer supported. |  |  |
| 1.1.0 | breaking | Rename DocumentLayout layout to DocumentGeneration_Default. | DocumentLayout | DocumentGeneration_Default |
| 1.1.0 | migration-step | Update layout for all pages using DocumentLayout to DocumentGeneration_Default and set 'Enable PDF export' to Yes. |  |  |
| 1.1.0 | breaking | Introduce design property 'Enable PDF export'; set to Yes for pages to export as PDF. |  |  |
| 1.1.0 | migration-step | When migrating from v1.0.0, set 'Enable PDF export' to Yes for all pages previously using DocumentLayout. |  |  |
| 1.1.0 | breaking | Rename included widgets; delete mendix.DocGenRedirect.mpk and mendix.PageBreak.mpk from widgets directory. | mendix.DocGenRedirect.mpk, mendix.PageBreak.mpk |  |
| 1.1.0 | migration-step | Delete old widget files mendix.DocGenRedirect.mpk and mendix.PageBreak.mpk; update pages to use new widgets. | mendix.DocGenRedirect.mpk, mendix.PageBreak.mpk |  |
| 1.1.0 | breaking | Rename theme variable $default-margin to $document-section-padding; use @page rule for page margin. | $default-margin | $document-section-padding |
| 1.1.0 | breaking | Rename remove-margin classes to remove-padding in stylesheet; update usage accordingly. | remove-margin | remove-padding |
| 1.1.0 | known-issue | Chrome/Chromium 117+ locally may scale PDF differently than Mendix Public Cloud service. |  |  |
| 1.1.0 | fix | Support apps including Responsive Web Offline navigation profile. (Ticket #190165) |  |  |
| 1.0.0 | known-issue | Chrome/Chromium 117+ locally may scale PDF differently than Mendix Public Cloud service. |  |  |
