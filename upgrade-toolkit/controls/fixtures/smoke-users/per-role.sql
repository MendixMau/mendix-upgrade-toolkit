-- PR-F28 fixture: the minimal Mendix user tables. Approver's users are all MendixSSO.MendixSSOUser (the workflow assigns
-- tasks to that entity by role); Admin's users are mixed (an SSO user and a Partner.PartnerUser) so the role stays generic
-- (Administration.Account, which is neither); Ops has MxAdmin, a plain System.User that does not vote, and one SSO user, so
-- Ops is SSO; Viewer has no users.
CREATE TABLE "mendixsystem$entity" (id varchar(36) PRIMARY KEY, entity_name varchar(511), table_name varchar(255), superentity_id varchar(255), remote boolean);
CREATE TABLE "mendixsystem$entityidentifier" (id varchar(36) PRIMARY KEY, short_id smallint);
CREATE TABLE "system$user" (id bigint PRIMARY KEY, name varchar(100), password varchar(200), active boolean, blocked boolean,
  webserviceuser boolean, isanonymous boolean, failedlogins int, createddate timestamp, changeddate timestamp, submetaobjectname varchar(255));
CREATE TABLE "administration$account" (id bigint PRIMARY KEY, fullname varchar(200), islocaluser boolean);
CREATE TABLE "mendixsso$mendixssouser" (id bigint PRIMARY KEY);
CREATE TABLE "partner$partneruser" (id bigint PRIMARY KEY);
CREATE TABLE "system$userrole" (id bigint PRIMARY KEY, name varchar(100));
CREATE TABLE "system$userroles" ("system$userid" bigint, "system$userroleid" bigint);
CREATE TABLE "system$session" (id bigint PRIMARY KEY);
INSERT INTO "mendixsystem$entity" VALUES ('u', 'System.User', 'system$user', NULL, false),
  ('a', 'Administration.Account', 'administration$account', 'u', false), ('s', 'MendixSSO.MendixSSOUser', 'mendixsso$mendixssouser', 'u', false),
  ('p', 'Partner.PartnerUser', 'partner$partneruser', 'u', false);
INSERT INTO "mendixsystem$entityidentifier" VALUES ('u', 1), ('a', 2), ('s', 3), ('p', 4);
INSERT INTO "system$userrole" VALUES (1, 'Admin'), (2, 'Approver'), (3, 'Viewer'), (4, 'Ops');
INSERT INTO "system$user" (id, name, submetaobjectname) VALUES (10, 'MxAdmin', 'System.User'), (11, 'demo_admin', 'MendixSSO.MendixSSOUser'),
  (12, 'partner_admin', 'Partner.PartnerUser'), (13, 'demo_approver', 'MendixSSO.MendixSSOUser'), (14, 'demo_approver_2', 'MendixSSO.MendixSSOUser'),
  (15, 'demo_ops', 'MendixSSO.MendixSSOUser');
INSERT INTO "mendixsso$mendixssouser" VALUES (11), (13), (14), (15);
INSERT INTO "partner$partneruser" VALUES (12);
INSERT INTO "system$userroles" VALUES (10, 1), (11, 1), (12, 1), (13, 2), (14, 2), (10, 4), (15, 4);
-- PR-F32: one domain association on the user (a task links to the approver who owns it); demo_approver_2 holds the most
-- links, so smoke_approver takes those over when it becomes Approver's sole holder
CREATE TABLE "mendixsystem$association" (id varchar(36) PRIMARY KEY, association_name varchar(511), table_name varchar(255),
  parent_entity_id varchar(36), child_entity_id varchar(36), parent_column_name varchar(255), child_column_name varchar(255));
INSERT INTO "mendixsystem$entity" VALUES ('t', 'App.Task', 'app$task', NULL, false);
INSERT INTO "mendixsystem$association" VALUES ('x', 'App.Task_Approver', 'app$task_approver', 't', 's', 'app$taskid', 'mendixsso$mendixssouserid');
CREATE TABLE "app$task_approver" ("app$taskid" bigint, "mendixsso$mendixssouserid" bigint);
INSERT INTO "app$task_approver" VALUES (100, 13), (101, 14), (102, 14);
