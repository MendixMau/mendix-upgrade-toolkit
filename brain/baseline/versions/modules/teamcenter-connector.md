# Teamcenter Connector (Marketplace component 111627)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/111627)

| version | published | min Mendix |
|---|---|---|
| 2606.0.1 | 2026-09-23 | 11.12.1 |
| 2606.0.0 | 2026-07-31 | 11.12.1 |
| 2512.1.2 | 2026-09-11 | 10.24.8 |
| 2512.1.1 | 2026-05-22 | 10.24.8 |
| 2512.1.0 | 2026-03-30 | 10.24.8 |
| 2512.0.1 | 2026-02-23 | 10.24.8 |
| 2512.0.0 | 2026-02-16 | 10.24.8 |
| 2506.0.1 | 2026-05-22 | 10.24.8 |
| 2506.0.0 | 2025-08-21 | 10.20.0 |
| 2412.225.0 | 2025-05-13 | 10.4.0 |
| 2412.3.0 | 2026-05-22 | 10.24.8 |
| 2412.0.0 | 2025-02-11 | 10.4.0 |
| 2406.3.1 | 2026-05-22 | 10.24.8 |
| 2406.3.0 | 2024-09-13 | 10.0.0 |
| 3.7.0 | 2026-04-28 | 9.24.41 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2606.0.1 | improvement | Upgraded to latest version of Studio Pro Design System for better alignment and accessibility. | Studio Pro Design System |  |
| 2606.0.1 | fix | Fixed BOM component unable to retrieve Teamcenter information due to incorrect session cookie lookup on Mendix Cloud. | Connector, BOM component |  |
| 2606.0.1 | fix | Fixed regression where Operation Mapping could no longer be supplied as JSON document. | Connector, Operation Mapping |  |
| 2606.0.1 | security | Updated Java dependencies to resolve vulnerabilities. | Java dependencies |  |
| 2606.0.1 | fix | Fixed bug where integration linked to excluded microflow could not be edited or regenerated. | Service document |  |
| 2606.0.1 | breaking | ConfigurationName parameter of RULE_TeamcenterConfiguration_IsLoggedIn is required again (was optional in 2606.0.0). | RULE_TeamcenterConfiguration_IsLoggedIn |  |
| 2606.0.0 | requirement | Mendix Studio Pro 11.12.1 or higher required. |  |  |
| 2606.0.0 | breaking | Removed Create and Delete rights from all entities. Administrator role no longer has direct entity-level access except Teamcenter Configuration. | Create rights, Delete rights |  |
| 2606.0.0 | improvement | Improved SSO configuration error logging with field names and messages matching Teamcenter Extension behavior. | SSO configuration error logging |  |
| 2606.0.0 | improvement | Rebuilt Teamcenter Extension using Mendix Web Extensibility Framework (TypeScript) replacing discontinued C# framework for future compatibility. | Teamcenter Extension |  |
| 2606.0.0 | fix | Fixed blocking (locked) state when calling multiple Teamcenter Java actions within one transaction preventing user operations. | Teamcenter Java actions, transaction |  |
| 2606.0.0 | fix | Fixed error when Teamcenter response contained array mixing empty strings and valid Model Object UIDs. (Ticket 269666) | Teamcenter response |  |
| 2606.0.0 | breaking | Updated entity attributes to match Teamcenter defaults: BOMLine bl_rev_object_name (128), bl_quantity (24), bl_plmxml_abs_xform (240); ReviseItemRevision.item_revision_id (32); User.userid (32); WorkspaceObject.checked_out (32). | BOMLine, BOMLine.bl_rev_object_name, BOMLine.bl_quantity, BOMLine.bl_plmxml_abs_xform, ReviseItemRevision.item_revision_id, User.userid, WorkspaceObject.checked_out |  |
| 2606.0.0 | fix | Fixed misleading error "Entity does not exist: ListOfValues" from GetAttachedLOV and GetAttachedPropDescs2. | GetAttachedLOV, GetAttachedPropDescs2 |  |
| 2606.0.0 | breaking | Renamed FileType/File Type to NamedReference/Named Reference for consistency with Teamcenter naming conventions. | FileType, File Type | NamedReference |
| 2606.0.0 | deprecation | Deprecated DownloadFile microflow; use DownloadFile/DownloadImage Java actions instead. | DownloadFile | DownloadFile |
| 2606.0.0 | deprecation | Deprecated ExecuteLogin microflow; use Login microflow instead. | ExecuteLogin | Login |
| 2606.0.0 | deprecation | Deprecated ExecuteLogout microflow; use Logout microflow instead. | ExecuteLogout | Logout |
| 2606.0.0 | deprecation | Deprecated AreMultipleTcConfigActive microflow; see annotation for guidance. | AreMultipleTcConfigActive |  |
| 2606.0.0 | deprecation | Deprecated CloseBOMWindow microflow; see annotation for guidance. | CloseBOMWindow |  |
| 2606.0.0 | deprecation | Deprecated HandleActiveConfigErrors microflow; see annotation for guidance. | HandleActiveConfigErrors |  |
| 2606.0.0 | deprecation | Deprecated HandleServiceErrors microflow; see annotation for guidance. | HandleServiceErrors |  |
| 2606.0.0 | deprecation | Deprecated RetrieveConfigNameFromSingleActiveConfiguration microflow; see annotation for guidance. | RetrieveConfigNameFromSingleActiveConfiguration |  |
| 2606.0.0 | deprecation | Deprecated RetrieveHttpHeaderList microflow; see annotation for guidance. | RetrieveHttpHeaderList |  |
| 2606.0.0 | deprecation | Deprecated RetrieveTcSessionBasedOnConfigName microflow; see annotation for guidance. | RetrieveTcSessionBasedOnConfigName |  |
| 2606.0.0 | deprecation | Deprecated RetrieveTeamcenterConfigurationByName microflow; see annotation for guidance. | RetrieveTeamcenterConfigurationByName |  |
| 2606.0.0 | deprecation | Deprecated RetrieveTeamcenterConfigurationFromTcSession microflow; see annotation for guidance. | RetrieveTeamcenterConfigurationFromTcSession |  |
| 2606.0.0 | deprecation | Deprecated ShowPartialErrors microflow; see annotation for guidance. | ShowPartialErrors |  |
| 2606.0.0 | deprecation | Deprecated UpdateSession microflow; see annotation for guidance. | UpdateSession |  |
| 2606.0.0 | deprecation | Deprecated CreateBOMWindows Java action; see documentation for successor. | CreateBOMWindows |  |
| 2606.0.0 | deprecation | Deprecated CreateBOMWindows2 Java action; see documentation for successor. | CreateBOMWindows2 |  |
| 2606.0.0 | deprecation | Deprecated ExpandPSOneLevel Java action; see documentation for successor. | ExpandPSOneLevel |  |
| 2606.0.0 | deprecation | Deprecated GetItemFromId Java action; see documentation for successor. | GetItemFromId |  |
| 2606.0.0 | deprecation | Deprecated GetTcSessionInfo Java action; see documentation for successor. | GetTcSessionInfo |  |
| 2606.0.0 | deprecation | Deprecated GetWorkflowTemplates Java action; see documentation for successor. | GetWorkflowTemplates |  |
| 2606.0.0 | deprecation | Deprecated PerformAction Java action; see documentation for successor. | PerformAction |  |
| 2606.0.0 | deprecation | Deprecated RetrieveCookie Java action; see documentation for successor. | RetrieveCookie |  |
| 2606.0.0 | deprecation | Deprecated WhereUsed Java action; see documentation for successor. | WhereUsed |  |
| 2606.0.0 | deprecation | Deprecated CreateBomWindowInput entity (renamed with underscore prefix). | CreateBomWindowInput |  |
| 2606.0.0 | deprecation | Deprecated CreateBomWindowInput_CreateBomWindowResponse entity (renamed with underscore prefix). | CreateBomWindowInput_CreateBomWindowResponse |  |
| 2606.0.0 | deprecation | Deprecated CreateBomWindowResponse entity (renamed with underscore prefix). | CreateBomWindowResponse |  |
| 2606.0.0 | deprecation | Deprecated ExpandPSOneLevelResponse entity (renamed with underscore prefix). | ExpandPSOneLevelResponse |  |
| 2606.0.0 | deprecation | Deprecated GetItemFromIdInput entity (renamed with underscore prefix). | GetItemFromIdInput |  |
| 2606.0.0 | deprecation | Deprecated GetItemFromIdResponse entity (renamed with underscore prefix). | GetItemFromIdResponse |  |
| 2606.0.0 | deprecation | Deprecated GetWorkflowTemplatesInput entity (renamed with underscore prefix). | GetWorkflowTemplatesInput |  |
| 2606.0.0 | deprecation | Deprecated ItemRevisionOutput entity (renamed with underscore prefix). | ItemRevisionOutput |  |
| 2606.0.0 | deprecation | Deprecated RevisionIDs entity (renamed with underscore prefix). | RevisionIDs |  |
| 2606.0.0 | deprecation | Deprecated SessionUser entity (renamed with underscore prefix). | SessionUser |  |
| 2606.0.0 | deprecation | Deprecated TcServerInfo entity (renamed with underscore prefix). | TcServerInfo |  |
| 2606.0.0 | deprecation | Deprecated WhereUsedInput entity (renamed with underscore prefix). | WhereUsedInput |  |
| 2606.0.0 | deprecation | Deprecated WhereUsedResponseInfo entity (renamed with underscore prefix). | WhereUsedResponseInfo |  |
| 2606.0.0 | breaking | Moved Login Java action to private; use Login microflow instead. | Login Java action | Login |
| 2606.0.0 | breaking | Moved Logout Java action to private; use Logout microflow instead. | Logout Java action | Logout |
| 2606.0.0 | breaking | Moved LoginSSO Java action to private; set up SSO login flow as described in documentation. | LoginSSO Java action |  |
| 2606.0.0 | migration-step | Move all custom Operation Mapping JSONs to Resources/TcConnector/OperationMapping and remove old Resources/OperationMapping folder. | Resources/OperationMapping |  |
| 2606.0.0 | migration-step | Remove Resources/TeamcenterCommon folder after upgrade. | Resources/TeamcenterCommon |  |
| 2606.0.0 | migration-step | Remove Resources/TeamcenterConnector folder after upgrade. | Resources/TeamcenterConnector |  |
| 2606.0.0 | migration-step | Regenerate integration with Teamcenter Extension to resolve references to Toolkit microflows and entities now in Connector. | Teamcenter Toolkit |  |
| 2606.0.0 | removal | Removed ModelObject_AddToExistingOrNewList microflow; retain old TeamcenterToolkit module until migrated. | ModelObject_AddToExistingOrNewList |  |
| 2606.0.0 | removal | Removed JA_CopyModelObjectToNewCreateInput Java action; retain old TeamcenterToolkit module until migrated. | JA_CopyModelObjectToNewCreateInput |  |
| 2606.0.0 | removal | Removed JA_CreateDatasetSpecialization Java action; retain old TeamcenterToolkit module until migrated. | JA_CreateDatasetSpecialization |  |
| 2606.0.0 | removal | Removed pre-configured CreateBOMWindow variants; use CreateBOMWindow or CreateBOMWindow_ByConfigurationContext instead. | CreateBOMWindow_Default, CreateBOMWindow_RevisionRule, CreateBOMWindow_VariantRule | CreateBOMWindow |
| 2606.0.0 | breaking | Removed Create and Delete rights on all entities. Administrator role now has access only to Teamcenter Configuration; use User role for integrations. | Administrator role, Teamcenter Configuration |  |
| 2606.0.0 | breaking | Changed error handling behavior: Connector no longer shows in-app error messages; all errors throw exceptions for microflow control. | error handling |  |
| 2606.0.0 | breaking | Fixed bug where ConfigurationName parameter changes behavior; ModelObject Java class now consistently requires ConfigurationName in all cases. | ModelObject Java class, ConfigurationName |  |
| 2606.0.0 | breaking | Removed LastError attribute from Credentials entity; use exception handling instead. | Credentials, LastError |  |
| 2606.0.0 | breaking | Introduced new naming convention for CreateInput and CompoundCreateInput specializations; regenerate integrations by creating new Teamcenter Service document. | CreateInput, CompoundCreateInput |  |
| 2512.1.2 | security | Updated Java Dependencies to remove vulnerabilities |  |  |
| 2512.1.1 | security | Updated com.fasterxml.jackson.core:jackson-databind com.fasterxml.jackson.core:jackson-core to 2.21.2 to resolve vulnerabilities | com.fasterxml.jackson.core:jackson-databind, com.fasterxml.jackson.core:jackson-core |  |
| 2512.1.0 | improvement | Added TC SSO compatibility with TC2406 and TC2312 |  |  |
| 2512.1.0 | security | Updated Java Dependencies to remove vulnerabilities in the dependencies |  |  |
| 2512.1.0 | breaking | User provisioning for TC SSO has changed. TcSSOUserInformation now only contains User and Locale. Use 'User' instead of 'sub' for Teamcenter Username | TcSSOUserInformation |  |
| 2512.0.1 | breaking | Made the FMS URL configuration field optional | FMS URL configuration |  |
| 2512.0.0 | improvement | Reimplemented Teamcenter X SSO to remove the OIDC module dependency | Teamcenter X SSO, OIDC module |  |
| 2512.0.0 | improvement | Reimplemented Teamcenter SSO to be consistent with Teamcenter X SSO | Teamcenter SSO |  |
| 2512.0.0 | improvement | Improved the overall SSO setup experience to remove the need for startup microflow and custom home pages |  |  |
| 2512.0.0 | improvement | Teamcenter SSO now supports user provisioning and anonymous user authentication from the login page | Teamcenter SSO |  |
| 2512.0.0 | improvement | Aligned and simplified the authentication process - Credentials, Tc SSO and TcX SSO are now consistent | Credentials, Tc SSO, TcX SSO |  |
| 2512.0.0 | breaking | Updated fmsutils.jar to Tc2512 compatible version | fmsutils.jar |  |
| 2512.0.0 | removal | Removed UserLogin microflow, use NAV_UserLogin navigation microflow instead | UserLogin | NAV_UserLogin |
| 2512.0.0 | removal | Removed ShowLoginPage microflow, use NAV_UserLogin navigation microflow instead | ShowLoginPage | NAV_UserLogin |
| 2512.0.0 | removal | Removed LoginToMultipleTeamcenters microflow, use NAV_UserLoginMultipleActive navigation microflow instead | LoginToMultipleTeamcenters | NAV_UserLoginMultipleActive |
| 2512.0.0 | removal | Removed AdminLogin microflow, use User module role instead | AdminLogin | User module role |
| 2512.0.0 | removal | Removed AdminHomePage page, use NAV_AdminHomePage navigation microflow instead | AdminHomePage | NAV_AdminHomePage |
| 2512.0.0 | removal | Removed SSO_RegisterRequestHandlers after startup microflow, no longer required | SSO_RegisterRequestHandlers |  |
| 2512.0.0 | breaking | Removed TeamcenterConfiguration event handlers, if you have custom logic for TeamcenterConfiguration objects, confirm it has the correct validations | TeamcenterConfiguration |  |
| 2512.0.0 | removal | Deleted HomePage entity, no longer required | HomePage |  |
| 2512.0.0 | breaking | Multiple microflows and pages deleted from the Private folder |  |  |
| 2512.0.0 | breaking | Multiple microflows and pages moved from Public to Private folder, check these are no longer directly referenced |  |  |
| 2506.0.1 | requirement | Upgraded to Mendix 10.24.8 |  |  |
| 2506.0.1 | security | Updated Java dependencies to resolve vulnerabilities |  |  |
| 2506.0.1 | improvement | Ensured compatibility with OIDC 4.3.0 and OIDC 4.4.0 | OIDC |  |
| 2506.0.0 | improvement | Cleaned up unused jars |  |  |
| 2506.0.0 | improvement | Upgraded FMS/TcSS jars to 2506 version | fmsutils.jar |  |
| 2506.0.0 | feature | Added support for using authenticated FSC for TcX |  |  |
| 2506.0.0 | improvement | Updated string property length of TcConnector Domain Model entities to align with corresponding Teamcenter property length |  |  |
| 2506.0.0 | improvement | Configured Managed dependencies for jackson-annotations-2.19.0.jar, jackson-core-2.19.0.jar, jackson-databind-2.19.0.jar, log4j-api-2.24.3.jar, log4j-core-2.24.3.jar and Apache HTTP Components | jackson-annotations, jackson-core, jackson-databind, log4j-api, log4j-core, httpmime, httpcore, httpclient |  |
| 2506.0.0 | migration-step | Userlib exclusions: TcLogging.jar, fmsutil.jar, fscjavaclientproxy.jar, teamcenter_sso_applib.jar, teamcenter_sso_common.jar | TcLogging.jar, fmsutil.jar, fscjavaclientproxy.jar, teamcenter_sso_applib.jar, teamcenter_sso_common.jar |  |
| 2506.0.0 | known-issue | When setting up Teamcenter X, if error occurs about FriendlyName being required, add an empty check as workaround at CreateClaimwithFriendlyName microflow | CreateClaimwithFriendlyName |  |
| 2412.225.0 | improvement | Cleaned up some unused jars |  |  |
| 2412.225.0 | fix | Fixed Mendix-Teamcenter SSO connection issue by upgrading TCSS jars to TCSS2412 |  |  |
| 2412.225.0 | improvement | Updated log4j from 2.17.1 to 2.23.1 for managing conflicts with Excel Export Module | log4j |  |
| 2412.225.0 | known-issue | When setting up Teamcenter X, if error occurs about FriendlyName being required, add an empty check as workaround at CreateClaimwithFriendlyName microflow | CreateClaimwithFriendlyName |  |
| 2412.3.0 | requirement | Upgraded to Mendix 10.24.8 |  |  |
| 2412.3.0 | security | Updated Java dependencies to remove unused jar files and to resolve vulnerabilities |  |  |
| 2412.3.0 | improvement | Ensured compatibility with OIDC 4.3.0 and OIDC 4.4.0 | OIDC |  |
| 2412.0.0 | feature | Provided support for connection to TcX using SAM Auth |  |  |
| 2412.0.0 | improvement | Cleaned up some unused jars |  |  |
| 2412.0.0 | known-issue | Due to limitations with SAMAuth registration in 2412, TcConnector is not supported with Teamcenter X version 2412 and lower |  |  |
| 2412.0.0 | known-issue | When setting up Teamcenter X, if error occurs about FriendlyName being required, add an empty check as workaround at CreateClaimwithFriendlyName microflow | CreateClaimwithFriendlyName |  |
| 2406.3.1 | requirement | Upgraded to Mendix 10.24.8 |  |  |
| 2406.3.1 | security | Updated Java dependencies to remove unused jar files and to resolve vulnerabilities |  |  |
| 2406.3.1 | improvement | Dependencies now implemented using managed dependencies (vendorlib) |  |  |
| 2406.3.1 | migration-step | Before updating this module, make sure to remove all old .jar files of the previous version from the userlib folder |  |  |
| 2406.3.0 | improvement | Upgraded TcSS jars and modified SSORedirectRequestHandler.processCallback to allow create SSO App session using JSON type |  |  |
| 2406.3.0 | breaking | XML Type is no more supported for SSO App session creation |  |  |
| 2406.3.0 | improvement | Added Access Rules for TcConnector.Image and TcConnector.ImanFile entity | TcConnector.Image, TcConnector.ImanFile |  |
| 2406.3.0 | breaking | Changed length of POM_application_object.object_string and BOMLine.object_string to 4000 to match with Teamcenter data model | POM_application_object.object_string, BOMLine.object_string |  |
| 2406.3.0 | improvement | Cleaned up userlib folder by removing unrequired jars |  |  |
| 3.7.0 | requirement | Upgraded to 9.24.41 |  |  |
| 3.7.0 | improvement | Updated Java Dependencies to remove unused jar files and remove vulnerabilities in the dependencies |  |  |
