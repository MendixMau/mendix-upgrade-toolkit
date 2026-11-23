#!/usr/bin/env python3
"""smoke_users.py: give a DATABASE COPY one login per user role, and clear persisted sessions, for the smoke walk.

Why: the smoke walk needs one login per role; seeded data has users for 2 of 7 roles (E1 3), seed_pg.py skips System
associations on purpose (E5 F11), and sessions left by an interrupted walk survive a restart and eat the 6-session
trial limit (E5 F10).

  smoke_users.py <db> [--password P] [--roles R1,R2] [--entity Module.Entity] [--sole-target] [--apply] [--container mig-pg] [--ledger $W/db-ledger.txt] [--any-db]

Per user role (all rows of system$userrole unless --roles) it creates user smoke_<role> (lower case) with the password
(default Smoke-only-1!; an empty one is refused, T3F-2), active, not blocked, and links the role. The user is created as
--entity Module.Entity (one row per inheritance level, the id carries the LEAF entity's short id: a home microflow that
retrieves CustomAdminModule.UserAccount sends a plain Administration.Account user to the login page, T3-6). Default: the
one specialization below Administration.Account that has users; several -> exit 2 and the candidates; none ->
Administration.Account when that entity exists, else (GF-17: no Administration.Account, or no users under it) the System.User
specialization that has rows (any module; several -> the most used, a tie -> exit 2), else System.User. Without --entity and with no single
specialization below Administration.Account, each role's user is the entity that role's existing (non-smoke, non
System.User) users all share (PR-F28: Purchase Request's approvers are MendixSSO.MendixSSOUser and its workflow assigns
tasks to MendixSSOUser by role, so an Account smoke_approver never got a task); a role whose users are mixed, or that has
none, takes the generic entity. Ids are <entity short id> << 48 | 2^40 + n: far above anything the runtime allocates. Existing smoke_
users are updated, not duplicated. Then it deletes system$session rows and their association rows.
--sole-target (PR-F32): also take each listed role away from every other (non smoke_) user, so the smoke user is the role's
only holder. A workflow that targets "all users with role X" then gives every task to smoke_x: on Purchase Request it
picked demo_ or smoke_ users run by run, and steps behind an assignee check (Select Vendor) passed or failed by chance
(D29-D32). Run it AFTER the app started (a demo-user resync at startup re-adds roles), on journey copies only; old and
new copies get the same treatment, so the comparison stays fair.
Without --apply it prints the SQL. With --apply it runs it through `docker exec <container> psql` (or --psql CMD).

Safety: refuses a database whose name does not start with fx_ or contain _copy/_smoke (a frozen baseline must never get
test users), unless the run ledger (--ledger, snapshot.py's db-ledger.txt) lists it (the gate's own journey copies such
as X_jold, X_after: T1-27, T2-15, T6-16) or --any-db. A *_frozen name is always refused. Note: in DTAP mode D a model update resyncs DEMO users (passwords reset); smoke_ users are
not demo users, so they survive a restart. Run this AFTER the app has started once on the copy (tables must exist).
Exit: 0 = done/printed, 1 = psql failed, 2 = refused or input error.
"""
import argparse, re, shlex, subprocess, sys

DEFAULT_PW = "Smoke-only-1!"


def bcrypt_hash(pw):
    # T3F-2: a hash of an empty string is a login nobody meant to create; refuse before anything else is generated
    if not pw or not pw.strip():
        print("smoke_users: REFUSED: the password is empty; a smoke user with a hash of nothing is not a login (pass --password P)",
              file=sys.stderr); sys.exit(2)
    try:
        import bcrypt
    except ImportError:
        sys.exit("smoke_users: needs the 'bcrypt' module (pip install bcrypt)")
    return "{BCrypt}" + bcrypt.hashpw(pw.encode(), bcrypt.gensalt(10, prefix=b"2a")).decode()


def qlit(s):
    return "'" + s.replace("'", "''") + "'"


def sql(pw_hash, roles, entity=None, sole=False, fallback=None):
    """entity None = generic: Administration.Account when that table exists, else System.User, and the SQL itself raises
    when a deeper specialization has rows (so a printed script applied by hand cannot guess either, T3-6)."""
    q = qlit
    role_filter = f"WHERE name IN ({', '.join(q(r) for r in roles)})" if roles else ""
    leaf = q(entity) if entity else "NULL"
    fb = q(fallback) if fallback else "'System.User'"   # GF-17: the generic user when there is no Administration.Account
    per_role = "false" if entity else "true"
    return f"""-- smoke_users.py: one login per role on a DATABASE COPY; sessions cleared
-- user entity: {entity or '(generic: Administration.Account if present, else System.User; raises if a deeper specialization has rows)'}
DO $$
DECLARE
  r record; uid bigint; given text := {leaf}; leaf text; sid bigint; n int := 0; has_acc boolean; cur text; tbl text;
  sup text; chain text[]; t text; deeper text; have text; mine text; nmine int;
  donor bigint; best int; k int; m int; moved int; a record; c record; cols text; vals text; dflt text; cn text;
BEGIN
  has_acc := to_regclass('"administration$account"') IS NOT NULL;
  FOR r IN SELECT id, name FROM "system$userrole" {role_filter} ORDER BY name LOOP
    n := n + 1;
    leaf := given;
    IF {per_role} THEN
      -- PR-F28: the entity this role's own users are (Purchase Request: approvers are MendixSSO.MendixSSOUser and the
      -- workflow targets MendixSSOUser by role, so a plain Account smoke_approver never got a task)
      SELECT min(u.submetaobjectname), count(DISTINCT u.submetaobjectname) INTO mine, nmine FROM "system$user" u
        JOIN "system$userroles" ur ON ur."system$userid" = u.id
       WHERE ur."system$userroleid" = r.id AND u.name NOT LIKE 'smoke\\_%' AND u.submetaobjectname <> 'System.User';
      IF nmine = 1 THEN leaf := mine; END IF;   -- plain System.User rows (MxAdmin) do not vote; a mixed role stays generic
    END IF;
    IF leaf IS NULL THEN
      leaf := CASE WHEN has_acc THEN 'Administration.Account' ELSE {fb} END;
      IF has_acc THEN
        WITH RECURSIVE d AS (SELECT id FROM "mendixsystem$entity" WHERE entity_name = 'Administration.Account'
                             UNION SELECT e.id FROM "mendixsystem$entity" e JOIN d ON e.superentity_id = d.id)
        SELECT string_agg(DISTINCT u.submetaobjectname, ', ') INTO deeper FROM "system$user" u
          JOIN "mendixsystem$entity" e ON e.entity_name = u.submetaobjectname
         WHERE e.id IN (SELECT id FROM d) AND e.entity_name <> 'Administration.Account';
        IF deeper IS NOT NULL THEN
          RAISE EXCEPTION 'users exist as % (a specialization of Administration.Account): rerun with --entity Module.Entity (T3-6)', deeper;
        END IF;
      END IF;
    END IF;
    sid := NULL; chain := '{{}}';
    SELECT e.id, i.short_id INTO cur, sid FROM "mendixsystem$entity" e JOIN "mendixsystem$entityidentifier" i ON i.id = e.id
     WHERE e.entity_name = leaf;
    IF sid IS NULL THEN RAISE EXCEPTION 'no short id for % (entity not in this database)', leaf; END IF;
    WHILE cur IS NOT NULL LOOP   -- leaf .. System.User; one row per level, root first (the Mendix id encodes the LEAF entity)
      SELECT table_name, superentity_id INTO tbl, sup FROM "mendixsystem$entity" WHERE id = cur;
      chain := tbl || chain; cur := sup;
    END LOOP;
    IF chain[1] IS DISTINCT FROM 'system$user' THEN RAISE EXCEPTION '% is not a System.User specialization', leaf; END IF;
    SELECT id, submetaobjectname INTO uid, have FROM "system$user" WHERE name = 'smoke_' || lower(r.name);
    IF uid IS NULL THEN
      uid := (sid << 48) + (1::bigint << 40) + n;
      WHILE EXISTS (SELECT 1 FROM "system$user" WHERE id = uid) LOOP uid := uid + 1000; END LOOP;
      FOREACH t IN ARRAY chain LOOP
        IF t = 'system$user' THEN
          INSERT INTO "system$user" (id, name, password, active, blocked, webserviceuser, isanonymous, failedlogins,
                                     createddate, changeddate, submetaobjectname)
          VALUES (uid, 'smoke_' || lower(r.name), {q(pw_hash)}, true, false, false, false, 0, now(), now(), leaf);
        ELSE
          -- GM-30: every column of this level gets a value, never a bare id. The model's attribute default; a Boolean with
          -- none is false; a column the table itself marks NOT NULL (no database default) gets the type's zero value. A NULL
          -- Boolean made the home microflow throw and the walk said "login failed" with a live session.
          cols := '"id"'; vals := '$1';
          IF t = 'administration$account' THEN
            cols := cols || ', "fullname", "islocaluser"'; vals := vals || ', ' || quote_literal('Smoke ' || r.name) || ', true';
          END IF;
          IF to_regclass('"mendixsystem$attribute"') IS NOT NULL THEN
            FOR a IN SELECT at.column_name AS col, at.type AS ty, at.default_value AS dv,
                            EXISTS (SELECT 1 FROM information_schema.columns ic WHERE ic.table_name = t AND ic.column_name = at.column_name
                                      AND ic.is_nullable = 'NO' AND ic.column_default IS NULL) AS req
                       FROM "mendixsystem$attribute" at JOIN "mendixsystem$entity" e ON e.id = at.entity_id
                      WHERE e.table_name = t AND at.column_name <> 'id'
                        AND NOT (t = 'administration$account' AND at.column_name IN ('fullname', 'islocaluser'))
                        AND EXISTS (SELECT 1 FROM information_schema.columns ic WHERE ic.table_name = t AND ic.column_name = at.column_name) LOOP
              dflt := nullif(a.dv, '');
              IF left(dflt, 2) = '[%' THEN dflt := NULL; END IF;   -- dynamic default ([%CurrentDateTime%]): not a literal, treated as none
              IF dflt IS NULL AND a.ty = 10 THEN dflt := 'false'; END IF;
              IF dflt IS NULL AND a.req THEN
                dflt := CASE WHEN a.ty IN (0, 3, 4, 5) THEN '0' WHEN a.ty = 30 THEN '' WHEN a.ty = 20 THEN to_char(now(), 'YYYY-MM-DD HH24:MI:SS') ELSE NULL END;
              END IF;
              IF dflt IS NOT NULL THEN cols := cols || ', ' || format('%I', a.col); vals := vals || ', ' || quote_literal(dflt); END IF;
            END LOOP;
          END IF;
          BEGIN
            EXECUTE format('INSERT INTO %I (%s) VALUES (%s)', t, cols, vals) USING uid;
          EXCEPTION WHEN not_null_violation THEN
            GET STACKED DIAGNOSTICS cn = COLUMN_NAME;
            RAISE EXCEPTION 'smoke_users: % column % is required and has no usable default (an enumeration is never invented): give the model a default or fill it by hand (GM-30)', t, cn;
          END;
        END IF;
      END LOOP;
    ELSE
      IF have IS DISTINCT FROM leaf THEN
        RAISE EXCEPTION 'smoke_% exists as %, not %: use a fresh copy or delete the smoke_ users first', lower(r.name), have, leaf;
      END IF;
      UPDATE "system$user" SET password = {q(pw_hash)}, active = true, blocked = false, failedlogins = 0 WHERE id = uid;
      -- GM-30: a smoke user from an earlier run keeps NULL Booleans: set them to the model default, else false
      IF to_regclass('"mendixsystem$attribute"') IS NOT NULL THEN
        FOREACH t IN ARRAY chain LOOP
          CONTINUE WHEN t LIKE 'system$%';
          FOR a IN SELECT at.column_name AS col, nullif(at.default_value, '') AS dv FROM "mendixsystem$attribute" at
                     JOIN "mendixsystem$entity" e ON e.id = at.entity_id
                    WHERE e.table_name = t AND at.type = 10 AND at.column_name <> 'id'
                      AND EXISTS (SELECT 1 FROM information_schema.columns ic WHERE ic.table_name = t AND ic.column_name = at.column_name) LOOP
            dflt := a.dv;
            IF dflt IS NULL OR left(dflt, 2) = '[%' THEN dflt := 'false'; END IF;
            EXECUTE format('UPDATE %I SET %I = %L WHERE id = $1 AND %I IS NULL', t, a.col, dflt, a.col) USING uid;
          END LOOP;
        END LOOP;
      END IF;
      DELETE FROM "system$userroles" WHERE "system$userid" = uid;
    END IF;
    INSERT INTO "system$userroles" ("system$userid", "system$userroleid") VALUES (uid, r.id);
    RAISE NOTICE 'smoke user % -> role % (%)', 'smoke_' || lower(r.name), r.name, leaf;
    IF {'true' if sole else 'false'} THEN   -- PR-F32: the smoke user is the role's only holder
      -- the smoke user takes over the domain links of the holder with the most (FSM: a Mechanic sees only the
      -- appointments of the Technician its Account links to; a bare smoke_mechanic saw an empty Scheduler)
      donor := NULL; best := 0;
      FOR c IN SELECT u.id FROM "system$user" u JOIN "system$userroles" ur ON ur."system$userid" = u.id
                WHERE ur."system$userroleid" = r.id AND u.name NOT LIKE 'smoke\\_%' AND u.id <> uid LOOP
        k := 0;
        FOR a IN SELECT x.table_name, CASE WHEN pe.table_name = ANY(chain) THEN x.parent_column_name ELSE x.child_column_name END AS col
                   FROM "mendixsystem$association" x JOIN "mendixsystem$entity" pe ON pe.id = x.parent_entity_id
                   JOIN "mendixsystem$entity" ce ON ce.id = x.child_entity_id
                  WHERE (pe.table_name = ANY(chain) OR ce.table_name = ANY(chain)) AND x.table_name NOT LIKE 'system$%' LOOP
          EXECUTE format('SELECT count(*) FROM %I WHERE %I = $1', a.table_name, a.col) INTO m USING c.id; k := k + m;
        END LOOP;
        IF k > best THEN best := k; donor := c.id; END IF;
      END LOOP;
      IF donor IS NOT NULL THEN
        moved := 0;
        FOR a IN SELECT x.table_name, CASE WHEN pe.table_name = ANY(chain) THEN x.parent_column_name ELSE x.child_column_name END AS col
                   FROM "mendixsystem$association" x JOIN "mendixsystem$entity" pe ON pe.id = x.parent_entity_id
                   JOIN "mendixsystem$entity" ce ON ce.id = x.child_entity_id
                  WHERE (pe.table_name = ANY(chain) OR ce.table_name = ANY(chain)) AND x.table_name NOT LIKE 'system$%' LOOP
          BEGIN
            EXECUTE format('UPDATE %I SET %I = $1 WHERE %I = $2', a.table_name, a.col, a.col) USING uid, donor;
            GET DIAGNOSTICS m = ROW_COUNT; moved := moved + m;
          EXCEPTION WHEN unique_violation THEN NULL;   -- a one-to-one the smoke user already holds: keep its own
          END;
        END LOOP;
        RAISE NOTICE 'sole target: smoke_% took % domain link(s) of user id %', lower(r.name), moved, donor;
      END IF;
      DELETE FROM "system$userroles" ur USING "system$user" u
       WHERE ur."system$userroleid" = r.id AND u.id = ur."system$userid" AND u.name NOT LIKE 'smoke\\_%';
      GET DIAGNOSTICS nmine = ROW_COUNT;
      RAISE NOTICE 'sole target: role % taken from % other user(s)', r.name, nmine;
    END IF;
  END LOOP;
  IF to_regclass('"system$session_user"') IS NOT NULL THEN DELETE FROM "system$session_user"; END IF;
  IF to_regclass('"system$backgroundjob_session"') IS NOT NULL THEN DELETE FROM "system$backgroundjob_session"; END IF;
  IF to_regclass('"system$changehash_session"') IS NOT NULL THEN DELETE FROM "system$changehash_session"; END IF;
  DELETE FROM "system$session";
END $$;
"""


def psql_rows(cmd, query):
    """Rows of one query as lists; None when the database cannot be asked (print mode then stays generic)."""
    try:
        p = subprocess.run(shlex.split(cmd) + ["-tA", "-F", "\t", "-v", "ON_ERROR_STOP=1"], input=query, capture_output=True, text=True)
    except OSError:
        return None
    if p.returncode:
        return None
    return [l.split("\t") for l in p.stdout.splitlines() if l.strip()]


def pick_entity(ents, counts):
    """ents {id: (name, super_id)}, counts {entity name: rows in system$user}. Returns (entity|None, candidates).
    Specializations strictly below Administration.Account that have users: exactly one -> it; none -> None (generic,
    Account else System.User); several -> candidates, the caller exits 2 (T3-6: never guess which one the home
    microflow retrieves)."""
    by_name = {n: i for i, (n, _) in ents.items()}
    acc = by_name.get("Administration.Account")
    if not acc:
        return None, []
    def below(i):
        while i in ents:
            i = ents[i][1]
            if i == acc: return True
        return False
    cands = sorted(n for n, c in counts.items() if c > 0 and n in by_name and below(by_name[n]))
    return (cands[0] if len(cands) == 1 else None), cands


def pick_user_leaf(ents, counts):
    """GF-17: an app with its own account entity has no Administration.Account (or no users below it), and every smoke
    user became a plain System.User: the login post worked and the home microflow, which changes the app's own user
    entity, failed on an object that was not there. The leaf is read from the System.User specializations that have
    rows (any module, never System.User itself). Returns (entity|None, candidates, why): one candidate -> it; several ->
    the one with the most rows when that is unique (ASSUMED: the entity most users are; --entity overrides), a tie ->
    (None, candidates, 'tie'); none -> (None, [], '')."""
    names = {n for n, _ in ents.values()}
    cands = sorted(((n, c) for n, c in counts.items() if c > 0 and n in names and n != "System.User"), key=lambda x: (-x[1], x[0]))
    if not cands:
        return None, [], ""
    if len(cands) == 1 or cands[0][1] > cands[1][1]:
        return cands[0][0], [n for n, _ in cands], ("only" if len(cands) == 1 else "most")
    return None, [n for n, _ in cands], "tie"


def ledger_dbs(path):
    """Databases the run ledger lists (first word of each line, snapshot.py format); every one is a copy of X_frozen,
    because snapshot.py refuses *_frozen and the steps only ever record `createdb -T X_frozen <name>` copies."""
    if not path:
        return set()
    try:
        return {l.split()[0] for l in open(path) if l.split() and not l.startswith("#") and not l.split()[0].endswith("_frozen")}
    except OSError as e:
        print(f"smoke_users: cannot read ledger {path}: {e}", file=sys.stderr); sys.exit(2)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("db"); ap.add_argument("--password", default=DEFAULT_PW); ap.add_argument("--roles")
    ap.add_argument("--apply", action="store_true"); ap.add_argument("--container", default="mig-pg")
    ap.add_argument("--any-db", action="store_true")
    ap.add_argument("--sole-target", action="store_true", help="take each listed role away from every non-smoke user (PR-F32)")
    ap.add_argument("--ledger", help="the run's db-ledger.txt: a database it lists is a copy of X_frozen (T1-27, T2-15, T6-16)")
    ap.add_argument("--entity", help="Module.Entity the users are created as (default: the one System.User specialization below "
                    "Administration.Account that has rows; several -> exit 2; none -> Administration.Account, else System.User)")
    ap.add_argument("--psql", help="command that reaches the database (default: docker exec -i <container> psql -U mendix -d <db>)")
    a = ap.parse_args()
    if not re.match(r"^[A-Za-z0-9_]+$", a.db):
        print(f"smoke_users: bad database name {a.db!r}", file=sys.stderr); sys.exit(2)
    if a.db.endswith("_frozen"):
        print(f"smoke_users: REFUSED {a.db}: a frozen baseline never gets test users (make a copy: createdb -T {a.db} <name>)",
              file=sys.stderr); sys.exit(2)
    ledger = ledger_dbs(a.ledger)
    if not a.any_db and not (a.db.startswith("fx_") or "_copy" in a.db or "_smoke" in a.db or a.db in ledger):
        print(f"smoke_users: REFUSED {a.db}: not a copy (name must start with fx_ or contain _copy/_smoke, or the run ledger "
              f"must list it: snapshot.py --ledger $W/db-ledger.txt --mark-used {a.db} --use journeys, then "
              f"--ledger $W/db-ledger.txt here; --any-db to force)" + (f"; {a.ledger} does not list it" if a.ledger else ""),
              file=sys.stderr); sys.exit(2)
    entity = a.entity
    fallback = None
    if entity and not re.match(r"^[A-Za-z][A-Za-z0-9_]*\.[A-Za-z][A-Za-z0-9_]*$", entity):
        print(f"smoke_users: bad --entity {entity!r} (want Module.Entity)", file=sys.stderr); sys.exit(2)
    pw_hash = bcrypt_hash(a.password)  # after the argument checks: a bad argument is exit 2 also without bcrypt
    cmd = a.psql or f"docker exec -i {a.container} psql -U mendix -d {a.db}"
    if not entity:
        er = psql_rows(cmd, 'select id, entity_name, table_name, superentity_id from "mendixsystem$entity" where not coalesce(remote,false)')
        cr = psql_rows(cmd, 'select submetaobjectname, count(*) from "system$user" group by 1')
        if er is None or cr is None:
            if a.apply:
                print("smoke_users: cannot read the model tables to choose the user entity; pass --entity Module.Entity", file=sys.stderr); sys.exit(1)
            print("smoke_users: NOTE database not reachable: entity not resolved; the SQL raises if a deeper specialization has rows "
                  "(pass --entity Module.Entity to fix it)", file=sys.stderr)
        else:
            ents = {r[0]: (r[1], r[3] if len(r) > 3 and r[3] else None) for r in er}
            counts = {r[0]: int(r[1]) for r in cr if r[0]}
            entity, cands = pick_entity(ents, counts)
            if len(cands) > 1:
                print("smoke_users: AMBIGUOUS: users exist as several specializations of Administration.Account: " + ", ".join(cands) +
                      "; pick the one the home microflow retrieves: --entity Module.Entity", file=sys.stderr); sys.exit(2)
            if entity:
                print(f"smoke_users: user entity {entity} (the only specialization of Administration.Account with rows)", file=sys.stderr)
            elif "Administration.Account" not in {n for n, _ in ents.values()} or counts.get("Administration.Account", 0) == 0:
                # GF-17: no Administration.Account users to follow: the leaf comes from every System.User specialization with rows
                leaf, lc, why = pick_user_leaf(ents, counts)
                if why == "tie":
                    print("smoke_users: AMBIGUOUS: users exist as several System.User specializations in equal number: " + ", ".join(lc) +
                          "; pick the one the home microflow retrieves: --entity Module.Entity (the pipeline: UPG_SMOKE_ENTITY or $WORK/smoke-entity.txt)",
                          file=sys.stderr); sys.exit(2)
                if leaf:
                    fallback = leaf
                    print(f"smoke_users: user entity {leaf} ({'the only' if why == 'only' else 'the most used'} System.User specialization with rows"
                          + (f"; others: {', '.join(n for n in lc if n != leaf)}; a role whose users all share another one gets that one" if why == "most" else "")
                          + "; --entity overrides)", file=sys.stderr)
                else:
                    print("smoke_users: user entity Administration.Account if present, else System.User (no specialization has rows)", file=sys.stderr)
            else:
                print("smoke_users: user entity Administration.Account if present, else System.User (no deeper specialization has rows)", file=sys.stderr)
    else:
        print(f"smoke_users: user entity {entity} (--entity)", file=sys.stderr)
    text = sql(pw_hash, [r for r in (a.roles or "").split(",") if r], entity, a.sole_target, fallback)
    if not a.apply:
        print(text); return
    p = subprocess.run(shlex.split(cmd) + ["-v", "ON_ERROR_STOP=1"],
                       input=text, capture_output=True, text=True)
    print(p.stdout + p.stderr)
    sys.exit(0 if p.returncode == 0 else 1)


if __name__ == "__main__":
    main()
