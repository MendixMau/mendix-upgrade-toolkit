# localedits /run/app/App.mpr

## AWSAuthentication 3.0.1 (content 120333): UNKNOWN (package not readable: version "3.0.1" not found; run 'mxcli marketplace versions <id>' to list available versions)
## Administration 4.1.0 (content 23513): edited (no storage change; microflow contents not compared: --mxcli-diff)
  info CHANGED  entity      Administration.Account  access rules (security, not data; lost on update)
## AmazonTranslateConnector 2.0.0 (content 204706): RED 2
  RED  CHANGED  entity      AmazonTranslateConnector.ListLanguagesRequest  persistent True -> False
  RED  CHANGED  entity      AmazonTranslateConnector.TranslateTextRequest  persistent True -> False
## AnyChart_BuildingBlocks 3.0.3 (content 106517): UNKNOWN (package not readable: version "3.0.3" not found; run 'mxcli marketplace versions <id>' to list available versions)
## Atlas_Core 3.14.0 (content 117187): domain model unchanged
## Atlas_Web_Content 3.5.1 (content 117183): domain model unchanged
## CommunityCommons 10.0.5 (content 170): domain model unchanged
## DataWidgets 2.13.0 (content 116540): domain model unchanged
## DeepLink 10.0.8 (content 43): domain model unchanged
## DemoUserSwitcher 1.1.0 (content 120303): UNKNOWN (package not readable: no versions available for this content)
## Encryption 9.0.2 (content 1011): domain model unchanged | UI edits 2 (replay after update)
  ui   CHANGED  snippet     Encryption.ChangePasswordSnippet  content differs from the package; local: SnippetParameter PasswordData (the update puts the package version back: save with --force-ui and replay)
  ui   CHANGED  snippet     Encryption.ExampleConfiguration  content differs from the package; local: SnippetParameter ExampleConfiguration (the update puts the package version back: save with --force-ui and replay)
## MES_Atlas_Extension 2.7.0 (content 120035): UNKNOWN (package not readable: no versions available for this content)
## MendixSSO 4.2.0 (content 111349): domain model unchanged
## NanoflowCommons 4.0.2 (content 109515): domain model unchanged
## WebActions 2.10.0 (content 114337): domain model unchanged
## ZipHandling 4.5.1 (content 108292): domain model unchanged

modules: 16, RED data-bearing edits: 2, UNKNOWN (not judged): 4 ['AWSAuthentication', 'AnyChart_BuildingBlocks', 'DemoUserSwitcher', 'MES_Atlas_Extension']: use `mxcli marketplace diff` or a Studio Pro compare; UNKNOWN is never 'no edits', NETWORK (not judged, transient): 0
LOGIC edits (documents added or deleted, contents not compared): 0
FILES edits (themesource, javascriptsource, Java user code; exit 1): 0
UI edits (pages, layouts): 2
force-ui: Encryption  (stepupdate.sh --force-ui: saves the edits under $W/saved-edits and forces the update; replay them after)
RED rule: do not update and replay these edits blindly. Re-creating an element gives it a new GUID
and the runtime drops its column. Keep the module, or migrate the data, then prove it with idcheck.py
and the regression gate.
