-- GM-30 fixture (synthetic): a user specialization below Administration.Account with columns the old smoke_users.py left NULL:
-- a Boolean with no default, a Boolean whose model default is true, a required integer (NOT NULL, no database default), an
-- optional string with a model default, an optional string with none, and the Account's own extra Boolean.
CREATE TABLE "mendixsystem$entity" (id varchar(36) PRIMARY KEY, entity_name varchar(511), table_name varchar(255), superentity_id varchar(255), remote boolean);
CREATE TABLE "mendixsystem$entityidentifier" (id varchar(36) PRIMARY KEY, short_id smallint);
CREATE TABLE "mendixsystem$attribute" (id varchar(36) PRIMARY KEY, entity_id varchar(36), attribute_name varchar(255), column_name varchar(255), type int, length int, default_value varchar(2000));
CREATE TABLE "system$user" (id bigint PRIMARY KEY, name varchar(100), password varchar(200), active boolean, blocked boolean,
  webserviceuser boolean, isanonymous boolean, failedlogins int, createddate timestamp, changeddate timestamp, submetaobjectname varchar(255));
CREATE TABLE "administration$account" (id bigint PRIMARY KEY, fullname varchar(200), islocaluser boolean, ismanager boolean);
CREATE TABLE "spec$staff" (id bigint PRIMARY KEY, isactive boolean, notify boolean, grade int NOT NULL, region varchar(50), badge varchar(50));
CREATE TABLE "system$userrole" (id bigint PRIMARY KEY, name varchar(100));
CREATE TABLE "system$userroles" ("system$userid" bigint, "system$userroleid" bigint);
CREATE TABLE "system$session" (id bigint PRIMARY KEY);
INSERT INTO "mendixsystem$entity" VALUES ('u', 'System.User', 'system$user', NULL, false),
  ('a', 'Administration.Account', 'administration$account', 'u', false), ('s', 'Spec.Staff', 'spec$staff', 'a', false);
INSERT INTO "mendixsystem$entityidentifier" VALUES ('u', 1), ('a', 2), ('s', 3);
INSERT INTO "mendixsystem$attribute" VALUES ('1', 'a', 'FullName', 'fullname', 30, 200, NULL), ('2', 'a', 'IsLocalUser', 'islocaluser', 10, 0, NULL),
  ('3', 'a', 'IsManager', 'ismanager', 10, 0, NULL),
  ('4', 's', 'IsActive', 'isactive', 10, 0, NULL), ('5', 's', 'Notify', 'notify', 10, 0, 'true'), ('6', 's', 'Grade', 'grade', 3, 0, NULL),
  ('7', 's', 'Region', 'region', 30, 50, 'North'), ('8', 's', 'Badge', 'badge', 30, 50, NULL);
INSERT INTO "system$userrole" VALUES (1, 'Clerk');
