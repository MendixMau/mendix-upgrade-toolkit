# Dojo to React client: react-app

Target 11.12.7: the React client is advised on 11, not required; Mendix 12 removes the Dojo client. Plan the open items before any 12 attempt.

## Widget packages (67)

| status | package | version | Dojo widgets in use (uses) | React path | source |
|---|---|---|---|---|---|
| can move | HTMLSnippet.mpk | 3.9.7 | HTMLSnippet.widget.HTMLSnippet (1) | successor: HTML Element (com.mendix.widget.web.htmlelement.HTMLElement, Marketplace 204843, 1.2.12) for HTML; JavaScript actions called from a nanoflow, triggered by the Events widget, for JS (Mendix 9.12.0+) | https://docs.mendix.com/refguide/mendix-client/react/ ; https://docs.mendix.com/appstore/widgets/html-javascript-snippet/ ; https://github.com/mendix/web-widgets/tree/main/packages/pluggableWidgets/html-element-web/package.json |
| can move | MicroflowTimer.mpk | 4.0.3 | MicroflowTimer.widget.MicroflowTimer (2) | successor: Events (com.mendix.widget.web.events.Events, Marketplace 224259, 1.3.1, reactReady), using Delay/Repeat (Mendix 9.24.0+) | https://docs.mendix.com/appstore/widgets/microflow-timer/ ; https://docs.mendix.com/appstore/widgets/events/ ; https://github.com/mendix/web-widgets/tree/main/packages/pluggableWidgets/events-web/package.json |
| can move | ShowByCondition.mpk | 1.4.0 | ShowByCondition.widget.ShowByCondition (2) | platform: Conditional visibility 'Based on expression' (common widget properties) | https://docs.mendix.com/refguide/common-widget-properties/ ; https://github.com/tieniber/ShowByCondition (README.md) [partial] |
| can move | snippetjs.mpk | 1.3.1 | snippetjs.widget.snippetjs (1) | successor: JavaScriptSnippet pluggable rebuild (incentro.javascriptsnippet.JavaScriptSnippet, 2.2.2); or the platform route: JavaScript action + nanoflow + Events, as the React guide advises for JS snippets | https://github.com/TimvanSteenbergen/JavaScript-Snippet (src/package.xml) ; https://github.com/mrgroen/mendix-JavaScriptSnippet ; https://docs.mendix.com/refguide/mendix-client/react/ [partial] |
| can move | URLRedirector.mpk | 1.1 | URLRedirector.widget.URLRedirector (2) | successor: Nanoflow Commons 'Open URL' JavaScript action called from a nanoflow, e.g. via the Events widget | https://docs.mendix.com/appstore/modules/nanoflow-commons/ ; https://community.mendix.com/link/space/widgets/questions/109887 [partial] |
| ready | Badge.mpk | 3.2.3 | none (all pluggable) |  |  |
| ready | bizzomate.BizzomateScheduler.mpk | 1.1.1 | none (all pluggable) |  |  |
| ready | Charts.mpk | 6.3.2 | none (all pluggable) |  |  |
| ready | com.mendix.widget.native.Accordion.mpk | 2.4.0 | none (all pluggable) |  |  |
| ready | com.mendix.widget.native.ActivityIndicator.mpk | 2.4.0 | none (all pluggable) |  |  |
| ready | com.mendix.widget.native.Animation.mpk | 3.4.0 | none (all pluggable) |  |  |
| ready | com.mendix.widget.native.AppEvents.mpk | 5.1.0 | none (all pluggable) |  |  |
| ready | com.mendix.widget.native.BackgroundGradient.mpk | 2.3.1 | none (all pluggable) |  |  |
| ready | com.mendix.widget.native.BackgroundImage.mpk | 2.3.1 | none (all pluggable) |  |  |
| ready | com.mendix.widget.native.Badge.mpk | 2.4.0 | none (all pluggable) |  |  |
| ready | com.mendix.widget.native.BarChart.mpk | 3.3.0 | none (all pluggable) |  |  |
| ready | com.mendix.widget.native.BarcodeScanner.mpk | 4.5.0 | none (all pluggable) |  |  |
| ready | com.mendix.widget.native.BottomSheet.mpk | 5.3.5 | none (all pluggable) |  |  |
| ready | com.mendix.widget.native.Carousel.mpk | 3.4.0 | none (all pluggable) |  |  |
| ready | com.mendix.widget.native.ColorPicker.mpk | 2.4.1 | none (all pluggable) |  |  |
| ready | com.mendix.widget.native.ColumnChart.mpk | 2.3.0 | none (all pluggable) |  |  |
| ready | com.mendix.widget.native.Feedback.mpk | 3.6.2 | none (all pluggable) |  |  |
| ready | com.mendix.widget.native.FloatingActionButton.mpk | 4.3.0 | none (all pluggable) |  |  |
| ready | com.mendix.widget.native.Gallery.mpk | 2.3.0 | none (all pluggable) |  |  |
| ready | com.mendix.widget.native.GalleryTextFilter.mpk | 2.1.1 | none (all pluggable) |  |  |
| ready | com.mendix.widget.native.Image.mpk | 3.2.0 | none (all pluggable) |  |  |
| ready | com.mendix.widget.native.IntroScreen.mpk | 4.6.0 | none (all pluggable) |  |  |
| ready | com.mendix.widget.native.LineChart.mpk | 3.3.0 | none (all pluggable) |  |  |
| ready | com.mendix.widget.native.ListViewSwipe.mpk | 3.5.0 | none (all pluggable) |  |  |
| ready | com.mendix.widget.native.Maps.mpk | 5.2.1 | none (all pluggable) |  |  |
| ready | com.mendix.widget.native.Notifications.mpk | 5.3.0 | none (all pluggable) |  |  |
| ready | com.mendix.widget.native.PieDoughnutChart.mpk | 2.3.0 | none (all pluggable) |  |  |
| ready | com.mendix.widget.native.PopupMenu.mpk | 4.1.1 | none (all pluggable) |  |  |
| ready | com.mendix.widget.native.ProgressBar.mpk | 4.5.0 | none (all pluggable) |  |  |
| ready | com.mendix.widget.native.ProgressCircle.mpk | 3.4.0 | none (all pluggable) |  |  |
| ready | com.mendix.widget.native.QRCode.mpk | 4.1.1 | none (all pluggable) |  |  |
| ready | com.mendix.widget.native.RadioButtons.mpk | 1.3.0 | none (all pluggable) |  |  |
| ready | com.mendix.widget.native.RangeSlider.mpk | 3.1.0 | none (all pluggable) |  |  |
| ready | com.mendix.widget.native.Rating.mpk | 5.3.0 | none (all pluggable) |  |  |
| ready | com.mendix.widget.native.Repeater.mpk | 2.4.0 | none (all pluggable) |  |  |
| ready | com.mendix.widget.native.SafeAreaView.mpk | 3.2.0 | none (all pluggable) |  |  |
| ready | com.mendix.widget.native.Signature.mpk | 3.1.0 | none (all pluggable) |  |  |
| ready | com.mendix.widget.native.Slider.mpk | 4.1.0 | none (all pluggable) |  |  |
| ready | com.mendix.widget.native.Switch.mpk | 1.2.0 | none (all pluggable) |  |  |
| ready | com.mendix.widget.native.ToggleButtons.mpk | 2.5.0 | none (all pluggable) |  |  |
| ready | com.mendix.widget.native.VideoPlayer.mpk | 6.5.0 | none (all pluggable) |  |  |
| ready | com.mendix.widget.native.WebView.mpk | 4.4.0 | none (all pluggable) |  |  |
| ready | com.mendix.widget.web.Combobox.mpk | 2.10.0 | none (all pluggable) |  |  |
| ready | com.mendix.widget.web.Datagrid.mpk | 3.11.8 | none (all pluggable) |  |  |
| ready | com.mendix.widget.web.DatagridDateFilter.mpk | 3.11.8 | none (all pluggable) |  |  |
| ready | com.mendix.widget.web.DatagridDropdownFilter.mpk | 3.11.8 | none (all pluggable) |  |  |
| ready | com.mendix.widget.web.DatagridNumberFilter.mpk | 3.11.8 | none (all pluggable) |  |  |
| ready | com.mendix.widget.web.DatagridTextFilter.mpk | 3.11.8 | none (all pluggable) |  |  |
| ready | com.mendix.widget.web.DropdownSort.mpk | 3.11.8 | none (all pluggable) |  |  |
| ready | com.mendix.widget.web.Gallery.mpk | 3.11.8 | none (all pluggable) |  |  |
| ready | com.mendix.widget.web.Image.mpk | 1.5.0 | none (all pluggable) |  |  |
| ready | com.mendix.widget.web.LanguageSelector.mpk | 1.0.1 | none (all pluggable) |  |  |
| ready | com.mendix.widget.web.PopupMenu.mpk | 3.2.2 | none (all pluggable) |  |  |
| ready | com.mendix.widget.web.SelectionHelper.mpk | 3.11.8 | none (all pluggable) |  |  |
| ready | com.mendix.widget.web.Timeline.mpk | 3.2.3 | none (all pluggable) |  |  |
| ready | com.mendix.widget.web.TreeNode.mpk | 3.11.8 | none (all pluggable) |  |  |
| ready | cpf.ImageBase.mpk | 1.0.0 | none (all pluggable) |  |  |
| ready | Maps.mpk | 4.0.0 | none (all pluggable) |  |  |
| ready | mendix.DropdownContainer.mpk | 1.2.0 | none (all pluggable) |  |  |
| ready | ProgressBar.mpk | 3.2.3 | none (all pluggable) |  |  |
| ready | ProgressCircle.mpk | 3.3.3 | none (all pluggable) |  |  |
| ready | SprintrFeedbackWidget.mpk | 12.0.4 | none (all pluggable) |  |  |

## Legacy core widgets the React client does not support (9 widget types)

| widget | count | documents | React path | source |
|---|---|---|---|---|
| Dynamic Image (core) | 14 | Form.InstanceForm_View, Form.SNIP_InstanceItemImage, Form.SNIP_ItemImage, Form.SNIP_ItemImage_View, NativeMobile.NativeTicketImageHelper_View, NativeMobile.NativeTicketNP_NewEdit, NativeMobileForm.NativeInstancePictureImage_View, NativeMobileForm.Snippet_NativeInstanceForm ... | Image widget (com.mendix.widget.web.image.Image, Marketplace 118579); right-click > Convert to Image; Studio Pro 11.4+: batch conversion (right-click > Convert all) | https://docs.mendix.com/refguide/mendix-client/react/ ; https://docs.mendix.com/refguide/mendix-client/batch-conversion/ |
| Static Image (core) | 194 | Dashboard.Grids, FSM_Specific.LeftMenuLayout, FSM_Specific.LoginLayout, FSM_Specific.Snippet_LayoutHeader, FSM_Specific.Snippet_LogoutButton, FSM_Specific.Snippet_NativeTicketCreationButton, FSM_Specific.Snippet_RefreshButton, FSM_Specific.Snippet_TakeBreak ... | Image widget; right-click > Convert to Image; Studio Pro 11.4+: batch conversion (right-click > Convert all) | https://docs.mendix.com/refguide/mendix-client/react/ ; https://docs.mendix.com/refguide/mendix-client/batch-conversion/ |
| Reference Selector (core) | 123 | Administration.Account_Edit, Administration.Account_New, Administration.MyAccount, AppSettings.Snippet_ApplicationSettings_Details, AssetManagement.Snippet_Asset_Details, CustomerManagement.Snippet_Contract_Details, CustomerManagement.Snippet_SLA_Details, MasterData.Appointment_NewEdit_MxAdmin ... | Combo box (Marketplace 219304); right-click > Convert to combo box; Studio Pro 11.4+: batch conversion (right-click > Convert all) | https://docs.mendix.com/refguide/mendix-client/react/ ; https://docs.mendix.com/refguide/mendix-client/batch-conversion/ |
| Reference Set Selector (core) | 3 | Technician.Snippet_Technician_DataTabs, Technician.TechnicianGroup_View | Combo box; Convert to combo box; Studio Pro 11.4+: batch conversion (right-click > Convert all) | https://docs.mendix.com/refguide/mendix-client/react/ ; https://docs.mendix.com/refguide/mendix-client/batch-conversion/ |
| Input Reference Set Selector (core) | 14 | Administration.Account_Edit, Administration.Account_New, CustomerManagement.Snippet_ContactPerson_Details, MasterData.Ticket_NewEdit_MxAdmin, MasterData.WorkOrder_NewEdit_MxAdmin, ModuleIntegration_Administration_Impl.Account_Edit, ModuleIntegration_Administration_Impl.Account_New, Scheduler.PageContext_View ... | Combo box; Convert to combo box; Studio Pro 11.4+: batch conversion (right-click > Convert all) | https://docs.mendix.com/refguide/mendix-client/react/ ; https://docs.mendix.com/refguide/mendix-client/batch-conversion/ |
| Drop-down (core) | 39 | CustomerManagement.Snippet_SLA_Details, Dashboard.DashboardAll, Form.FormVersion_View, Form.InstanceForm_View, MasterData.Appointment_NewEdit_MxAdmin, MasterData.Form_NewEdit_MxAdmin, MasterData.InstanceForm_NewEdit_MxAdmin, MasterData.InstanceItem_NewEdit_MxAdmin ... | Combo box; Convert to combo box; Studio Pro 11.4+: batch conversion (right-click > Convert all) | https://docs.mendix.com/refguide/mendix-client/react/ ; https://docs.mendix.com/refguide/mendix-client/batch-conversion/ |
| Data grid (legacy, core) | 152 | Administration.Account_Overview, Administration.Account_Select, Administration.ActiveSessions, Administration.RuntimeInstances, Administration.ScheduledEvents, Administration.UserRole_Select, AppSettings.Snippet_SynchronizationError_Overview, AssetManagement.Asset_AssetPart_AddToBOM ... | Data Grid 2 (Data Widgets 116540); right-click > Convert to Data Grid 2; Studio Pro 11.4+: batch conversion (right-click > Convert all) | https://docs.mendix.com/refguide/mendix-client/react/ ; https://docs.mendix.com/refguide/mendix-client/batch-conversion/ |
| Template grid (core) | 6 | Dashboard.DashboardAll, Dashboard.Grids | Gallery (Data Widgets 116540); manual replacement | https://docs.mendix.com/refguide/mendix-client/react/ |
| Sign In widgets (Username, Password, Sign In Button) | 3 | General.Login_Web | Modeled login page: non-persistent entity for credentials + nanoflow (Atlas login page template) | https://docs.mendix.com/refguide/mendix-client/react/ |

## Marketplace modules not React-ready (0)

none of the table's modules

## JavaScript on the Dojo APIs (0 files)

none

## Custom index.html (unchecked)

theme/web/index.html: compare with the React client's index.html by hand

'delete' looks at pages, snippets and layouts only: a building block or page template that still holds the widget breaks when the .mpk goes, so clear those first.

'ready' means the package declares pluginWidget="true". The React client also needs a pluggable widget built with pluggable-widget-tools 9.4.1 or later, which the .mpk does not record: update every widget (R9) and let Studio Pro's React client check have the last word.

dojo-react react-app: 67 packages, 62 ready, 5 can move, 0 delete, 0 can't move, 0 not researched, 0 unreadable; legacy core widgets 548 in 209 documents; modules not React-ready 0; Dojo JS 0 files; ADVISORY for 11.12.7
