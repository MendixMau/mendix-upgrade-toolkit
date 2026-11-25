# Rich Text (Marketplace component 74889)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Widget, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/74889)

| version | published | min Mendix |
|---|---|---|
| 5.1.0 | 2026-10-01 | 9.24.0 |
| 5.0.0 | 2026-08-21 | 9.24.0 |
| 4.12.0 | 2026-04-23 | 9.24.0 |
| 4.11.2 | 2026-03-09 | 9.24.0 |
| 4.11.1 | 2026-01-30 | 9.24.0 |
| 4.11.0 | 2025-11-10 | 9.24.0 |
| 4.10.0 | 2025-10-08 | 9.24.0 |
| 4.9.0 | 2025-09-04 | 9.24.0 |
| 4.8.1 | 2025-07-29 | 9.24.0 |
| 4.8.0 | 2025-07-01 | 9.24.0 |
| 4.7.0 | 2025-06-02 | 9.24.0 |
| 4.6.1 | 2025-05-21 | 9.24.0 |
| 4.5.0 | 2025-04-03 | 9.24.0 |
| 4.4.0 | 2025-04-01 | 9.24.0 |
| 4.3.1 | 2025-03-19 | 9.24.0 |
| 4.3.0 | 2025-02-14 | 9.24.0 |
| 4.2.0 | 2025-01-16 | 9.24.0 |
| 4.1.0 | 2024-12-13 | 9.24.0 |
| 4.0.0 | 2024-10-29 | 9.24.0 |
| 3.3.1 | 2024-08-28 | 9.24.0 |
| 3.3.0 | 2024-08-16 | 9.24.0 |
| 3.2.4 | 2024-07-16 | 9.24.0 |
| 3.2.3 | 2024-06-25 | 9.24.0 |
| 3.2.2 | 2024-06-05 | 9.24.0 |
| 3.2.1 | 2024-05-27 | 9.24.0 |
| 3.2.0 | 2024-05-21 | 9.24.0 |
| 3.1.2 | 2024-05-10 | 9.24.0 |
| 3.1.1 | 2024-05-02 | 9.24.0 |
| 3.1.0 | 2024-04-23 | 9.24.0 |
| 3.0.2 | 2024-04-04 | 9.24.0 |
| 3.0.1 | 2024-03-12 | 9.24.0 |
| 3.0.0 | 2024-02-28 | 9.24.0 |
| 2.3.0 | 2024-02-08 | 9.6.0 |
| 2.2.4 | 2023-11-29 | 9.6.0 |
| 2.2.3 | 2023-10-30 | 9.6.0 |
| 2.2.2 | 2023-10-12 | 9.6.0 |
| 2.2.1 | 2023-09-27 | 9.6.0 |
| 2.2.0 | 2023-06-06 | 9.6.0 |
| 2.1.6 | 2023-04-18 | 9.6.0 |
| 2.1.5 | 2023-03-24 | 9.6.0 |
| … 22 older versions | | |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 5.1.0 | fix | Fixed issue where images resized in version 4 lost their size after upgrading to version 5. |  |  |
| 5.0.0 | breaking | Changed rich text internal WYSIWYG engine from Quill to Tiptap for better nested table support. Users should review configurations. | WYSIWYG engine | Tiptap |
| 5.0.0 | removal | Removed codemirror from code dialog viewer due to unsupported strict CSP policy, replaced with internally built code editor using highlightjs. | codemirror | highlightjs-based internal code editor |
| 4.12.0 | improvement | Added trimEnd functionality to make character count on status bar correctly count characters without new line and empty character. |  |  |
| 4.11.0 | breaking | Changed Tab keyboard behavior to add indentation instead of exiting focus from editor. | Tab keyboard behavior |  |
| 4.11.0 | breaking | Changed empty line mark from space to <br> break tag. | empty line mark |  |
| 4.10.0 | improvement | Allow white-space inline styling parsing in the widget. |  |  |
| 4.3.0 | fix | Fixed rich text accessibility with tab keypress allowing direct focus on editor. |  |  |
| 4.2.0 | breaking | Changed dimension configurations to better match CSS formats. | dimension configurations |  |
| 4.2.0 | improvement | Changed DOM order to show editor before toolbar for easier focus order. | DOM order |  |
| 4.0.0 | breaking | Updated Rich Text widget to use Quill V2 due to license change in TinyMCE. Review and adjust widget configurations after updating. | WYSIWYG engine | Quill V2 |
| 3.2.4 | improvement | Allow users to turn off sandbox_iframes through configurations. |  |  |
| 3.2.3 | security | Upgraded TinyMCE dependency to version 6.8.4 to solve CVE-2024-38357. | TinyMCE |  |
| 3.2.2 | improvement | Optimized rich text bundle size. |  |  |
| 3.1.2 | improvement | Added more options to rich text context menu with option to use native context menu. |  |  |
| 3.1.1 | security | Fixed security issue by setting sandbox_iframes and convert_unsafe_embeds to true. |  |  |
| 3.1.0 | improvement | Allow user to disable quick toolbar. |  |  |
| 3.0.0 | breaking | Built new rich text editor using TinyMCE editor replacing CKEditor 4 which reached end of life. Review configuration after updating. | editor engine | TinyMCE |
| 2.2.2 | breaking | Added Insert toolbar group as option for custom toolbar. | toolbar configuration |  |
| 2.1.6 | security | Updated ckeditor4 to version 4.21.0. | ckeditor4 |  |
| 2.1.3 | improvement | Added 1MB file size limit for pasted and dropped images. |  |  |
| 2.1.2 | breaking | Changed openlink action to open links just on mouse click without ctrl. | link behavior |  |
| 2.1.0 | security | Updated ckeditor4 to version 4.20.0 to prevent XSS. | ckeditor4 |  |
| 2.1.0 | removal | Removed CSS file for WebSpellChecker Dialog plugin as it reached end of support from ckeditor4. | CSS file for WebSpellChecker Dialog plugin |  |
| 2.0.1 | breaking | Changed behavior on clicking links in rich text editor. CMD/CTRL + Click will open link in new tab. | link behavior |  |
| 2.0.0 | breaking | Core library changed from Quill to CKEditor4. | core library |  |
| 1.3.9 | fix | Changed behavior where Rich Text could steal focus while updating content. |  |  |
| 1.3.8 | security | Improved security to comply with latest exploits. |  |  |
| 1.3.1 | known-issue | Content translatable by Chrome when Readonly-style is Rich text and Editable is Never, or Data view Editable is No. |  |  |
