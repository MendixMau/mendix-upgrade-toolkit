#!/bin/bash
# editroute_control.sh CASE: controls of bin/editroute.py (kept modules routed to an update) and the cockpitcheck keep-recommended
# rule. A stub mxcli answers describe and refs, so no project or network is needed.
#   unread-config  an unreadable module with a constant/jar edit is HELD, not forced (GM-11)
#   plan     one kept module per route; prints the ROUTE lines and the files editroute writes
#   collect  the replay files after the routed update: the app's change merged onto the new element, never the saved whole element
#   score    did each route work: on the plan's version, held, or replay failed; one ledger line per module across runs
#   brain    each route carries the company brain's notes for it, shown on the card; hit@k measured on a labelled set
#   reset    a rerun of the update step drops an earlier routing's own lines (a person's stay) and moves its files aside
#   reroute  a routed update keeps a module for a second reason: routed again, routes add up; the same reason twice is a HOLD
#   gate     cockpitcheck on a module card that recommends the old version, with and without an end date
set -u
B=$(cd "$(dirname "$0")/../bin" && pwd)
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
W=$T/work; A=$T/app; S=$A/.stepupdate; C=$T/cache
mkdir -p "$W" "$S" "$C/7-1.0.0" "$T/orig"
touch "$A/App.mpr" "$T/orig/App.mpr" "$C/7-1.0.0.mpk" "$C/7-1.0.0/project.mpr"
cat > "$T/mxcli" <<'PY'
#!/usr/bin/env python3
import sys
import os
a = sys.argv[1:]
nav = os.environ.get("NAVCOPY")   # navcopy cases: a Marketplace page on the redirected layout, opened from the menu
if nav and a[0] == "-p":
    q = a[3]
    if q == "SHOW MODULES":
        print("| Module | Source |\n|---|---|\n| Uimod | Marketplace v1.0.0 |\n| Brand |  |")
    elif q == "SHOW PAGES":
        print("| Qualified Name | Module | Name | Folder | Title |\n|---|---|---|---|---|\n| Uimod.Acct | Uimod | Acct | Admin | Accounts |\n"
              "| Uimod.Edit | Uimod | Edit | Admin | Edit Account |\n"
              f"| Brand.MyEdit | Brand | MyEdit | Pages | {'Something else' if nav == 'nohome' else 'Edit Account'} |")
    elif q == "SHOW MODULE ROLES IN Brand":
        print("| Qualified Name | Module | Role |\n|---|---|---|\n| Brand.Administrator | Brand | Administrator |")
    sys.exit(0)
if nav and a[0] == "refs" and a[3] in ("Uimod.Redir", "Uimod.Acct"):
    print("| SourceType | SourceName | RefKind |\n|---|---|---|\n" + ("| PAGE | Uimod.Acct | layout |" if a[3] == "Uimod.Redir"
          else "| NAVIGATION | Navigation.Responsive | menu_item |"))
    sys.exit(0)
if nav and a[0] == "describe" and a[3] in ("page", "navigation"):
    grid = "  -- Forms$DataGrid (grid12)  -- NOT re-executable: mxcli cannot author this widget\n" if nav in ("grid", "refuse") else ""
    print("mdl 1;\ncreate or modify page Uimod.Acct folder 'Admin' (\n  Title: 'Accounts',\n  Layout: Uimod.Redir\n) {\n" + grid + "};\n"
          "grant view on page Uimod.Acct to Uimod.Administrator, Uimod.Auditor;" if a[3] == "page" else
          "mdl 1;\ncreate or modify navigation Responsive\n  app title 'Uimod App'\n  app icon Brand.Icons.Logo\n{\n  menu item 'Accounts' ( OnClick: show page Uimod.Acct with (DisabledDuringExecution: false) )\n}")
    sys.exit(0)
if a[0] == "describe":
    mpr, kind, qn = a[2], a[3], a[4]
    pkg = mpr.endswith("project.mpr")
    side = "base" if pkg else "ours" if "/orig/" in mpr else "theirs"
    if kind in ("layout", "snippet", "constant"):   # base = installed package, ours = original app, theirs = updated app
        el = {"Uimod.L1": {"base": ["class: 'a',", "title: 'x'"], "ours": ["class: 'mine',", "title: 'x'"], "theirs": ["class: 'a',", "title: 'y'"]},
              "Uimod.K": {"base": ["value: '1'"], "ours": ["value: '2'"], "theirs": ["value: '1'"]},
              "Uimod.Added": {"ours": ["class: 'own'"]},
              "Uimod.Bad": {"base": ["class: 'a'"], "ours": ["class: 'BROKEN'"], "theirs": ["class: 'a'"]},
              # layouts: one redirected to the app's design module, one the app added and nothing uses, one edited and used
              "Uimod.Redir": {"base": ["class: 'a',", "title: 'x'"], "ours": ["Layout: Brand.Main"], "theirs": ["class: 'a',", "title: 'y'"]},
              "Uimod.Spare": {"ours": ["class: 'copy'"]},
              "Uimod.UsedOwn": {"base": ["class: 'a'"], "ours": ["class: 'own'"], "theirs": ["class: 'a'"]}}.get(qn, {}).get(side)
        if el:
            print(f"mdl 1;\ncreate or modify {kind} {qn} (\n" + "\n".join("  " + x for x in el) + "\n) {\n};")
        sys.exit(0)
    if kind == "association":   # only the original model still has it
        if "/orig/" in mpr and qn == "Other.A_B":
            print(f"mdl 1;\ncreate or modify association {qn}\nfrom Other.X to Target.Y;")
        sys.exit(0)
    acc = {"Accmod.Acct": {"ours": "grant read (Name, Emp_Acct) on entity Accmod.Acct to Accmod.User;",
                           "base": "grant read (Name) on entity Accmod.Acct to Accmod.User;"},
           "Holdmod.H": {"ours": "grant read (Name, Secret, Emp_H) on entity Holdmod.H to Holdmod.User;",
                         "base": "grant read (Name) on entity Holdmod.H to Holdmod.User;"}}.get(qn, {}).get(side)
    if kind == "entity" and acc:
        print(f"mdl 1;\ncreate or modify entity {qn} (\n  Name: String\n);\n{acc}")
        sys.exit(0)
    if kind == "entity" and qn == "Other.X":
        print("create or modify entity Other.X (\n);\ngrant read (A_B, Name), write (A_B) on entity Other.X to Other.User;\ngrant read (Name) on entity Other.X to Other.Guest;")
        sys.exit(0)
    if kind == "entity" and qn == "Target.Y":
        print("create or modify entity Target.Y (\n);\ngrant create, read (Code, A_B), write (Code) on entity Target.Y to Target.User where [Code='x'];\ngrant read (Code) on entity Target.Y to Target.Guest;")
        sys.exit(0)
    body = "logic A" if pkg or "Cosmetic" in qn else "logic B"
    print(("@position(1, 1)\n" if pkg else "@position(9, 9)\n@anchor(from: right, to: left)\n") + body)
elif a[0] == "check":
    t = open(a[1]).read()
    bad = "BROKEN" in t or (nav == "refuse" and "ALTER PAGE" in t)   # refuse: mxcli check says no to the in-place layout
    print("  ✗ class BROKEN is not a class [MDL000]" if bad else "ok")
    sys.exit(1 if bad else 0)
elif a[0] == "refs":
    print(f"References to {a[3]}\n| Caller |" if "Used" in a[3] else f"(no references found to attribute {a[3]})")
PY
chmod +x "$T/mxcli"
export UPG_MXCLI=$T/mxcli UPG_CACHE=$C
refuse() { printf 'refusing to update: %s element(s) have been changed locally and the update would discard them:\n' "$#" > "$S/step$1-$2.log"
  local m=$2; shift 2; for e in "$@"; do printf '    %s\n' "$e" >> "$S/step$n-$m.log"; done; printf '\n  - Save them first:  --save-edits <dir>\n' >> "$S/step$n-$m.log"; }
n=1; refuse 1 Cosmo "MICROFLOW CosmeticFlow"
n=2; refuse 2 Realmod "MICROFLOW RealFlow"
n=3; refuse 3 Uimod "SNIPPET L1" "CONSTANT K" "SNIPPET Added" "SNIPPET Bad" "LAYOUT Redir" "LAYOUT Spare" "LAYOUT UsedOwn"
printf '5 element(s) could not be read, so it cannot be shown that the module is unedited.\n' > "$S/step4-Unread.log"
touch "$S/step5-Filesmod.log" "$S/step6-Vendmod.log" "$S/step7-Usedmod.log" "$S/step8-Target.log" "$S/step9-Javamod.log"
printf 'RED  REMOVED      attribute   Vendmod.E.Gone  (column/table dropped; intended?)\n' > "$S/step6-Vendmod.idcheck"
printf 'RED  REMOVED      attribute   Usedmod.E.Used  (column/table dropped; intended?)\n' > "$S/step7-Usedmod.idcheck"
printf 'RED  REMOVED      association Other.A_B  (column/table dropped; intended?)\ninfo REMOVED      association Other.Np_B  (no data)\n' > "$S/step8-Target.idcheck"
printf 'refusing to update: 1 element(s) have been changed locally\n' > "$S/step12-Target.log"   # a later step, no idcheck (WM1)
cat > "$S/kept.txt" <<'K'
Cosmo local edits refuse the update
Realmod local edits refuse the update
Uimod local edits refuse the update
Unread elements could not be read, module not shown unedited
Filesmod FILES-UNKNOWN: update replaced 1 theme/javascript/java file(s), unproven unedited
Vendmod idcheck REVIEW (persistence loss or removal: accept it in approved.txt with a reason, or keep), see x
Usedmod idcheck REVIEW (persistence loss or removal: accept it in approved.txt with a reason, or keep), see x
Target idcheck REVIEW (persistence loss or removal: accept it in approved.txt with a reason, or keep), see .stepupdate/step8-Target.idcheck
Javamod local Java user code edits (FILES-EDITED javasource)
K
python3 - "$W/localedits.json" <<'PY'
import json, sys
mods = ["Cosmo", "Realmod", "Uimod", "Unread", "Filesmod", "Vendmod", "Usedmod", "Target", "Javamod"]
json.dump([{"name": m, "cid": 7, "version": "1.0.0", "domain": [], "ui": [], "logic": []} for m in mods], open(sys.argv[1], "w"))
PY
for m in Cosmo Realmod Uimod Unread Filesmod Vendmod Usedmod Target Javamod; do echo "7 2.0.0 $m"; done > "$W/plan.txt"
case "${1:-}" in
  plan) python3 "$B/editroute.py" plan --work "$W" --app "$A" --original "$T/orig/App.mpr" --plan "$W/plan.txt"; echo "rc=$?"
        for f in route-plan.txt force-ui.txt accept-unsaved.txt approved.txt approved-step.txt; do sed "s/^/$f: /" "$W/$f"; done ;;
  unread-config) # GM-11: the same unreadable module, but localedits shows a changed constant default: kept (HOLD), not forced as UNREAD
        python3 - "$W/localedits.json" <<'PY'
import json, sys
rep = json.load(open(sys.argv[1]))
for e in rep:
    if e["name"] == "Unread":
        e["config"] = [{"change": "CHANGED", "kind": "constant", "name": "Unread.K", "detail": "default '1' -> '2'"}]
json.dump(rep, open(sys.argv[1], "w"))
PY
        python3 "$B/editroute.py" plan --work "$W" --app "$A" --original "$T/orig/App.mpr" --plan "$W/plan.txt"; echo "rc=$?" ;;
  collect) python3 "$B/editroute.py" plan --work "$W" --app "$A" --original "$T/orig/App.mpr" --plan "$W/plan.txt" > /dev/null
        mkdir -p "$W/saved-edits/Uimod" "$W/saved-edits/Target"
        for e in snippet-L1 constant-K snippet-Added snippet-Bad layout-Redir layout-Spare layout-UsedOwn page-NotRefused entity-Whole; do printf 'mdl 1;\n-- saved whole element %s\n' "$e" > "$W/saved-edits/Uimod/$e.mdl"; done
        printf 'mdl 1;\ncreate or modify association Other.A_B from Other.X to Target.Y;\n' > "$W/saved-edits/Target/association-Other_A_B.mdl"
        python3 "$B/editroute.py" collect --work "$W"; echo "rc=$?"
        sed 's/^/Uimod.mdl: /' "$W/replay/Uimod.mdl"; sed 's/^/Target.mdl: /' "$W/replay/Target.mdl"; sed 's/^/Target.guids: /' "$W/replay/Target.guids" ;;
  score) python3 "$B/editroute.py" plan --work "$W" --app "$A" --original "$T/orig/App.mpr" --plan "$W/plan.txt" > /dev/null
        git -C "$A" init -q; git -C "$A" commit -q --allow-empty -m "step: Cosmo 2.0.0 (stepupdate, idcheck PASS, forced)"
        sed -i.bak '/^Cosmo /d' "$S/kept.txt"   # stepupdate takes a module it committed out of kept.txt (E6-12)
        printf '7 2.0.0 Cosmo\n7 2.0.0 Uimod\n' >> "$W/plan.txt"
        mkdir -p "$W/replay"; echo x > "$W/replay/Uimod.mdl"; echo "MDL081" > "$W/replay-Uimod.out"
        python3 "$B/editroute.py" score --work "$W" --app "$A" --plan "$W/plan.txt" --ledger "$T/ledger.tsv" --label app1; echo "rc=$?"
        sed 's/^/ledger: /' "$T/ledger.tsv" | cut -f1-3,5,6,11 | head -3 ;;
  brain) Bd="$T/fake-brain"; mkdir -p "$Bd/baseline/versions" "$Bd/internal/architecture" "$Bd/internal/ux-ui" "$Bd/internal/upgrade"
        touch "$Bd/baseline/versions/studio-pro-upgrade-10.md"
        printf -- '---\ntitle: Never edit Marketplace modules, use an extension module\nkeywords: [extension module, local edits]\n---\nPut changes in a separate module.\n' > "$Bd/internal/architecture/ext.md"
        printf -- '---\ntitle: Hide Atlas layouts in the company UI module\nkeywords: [Atlas_Core layouts, design system]\n---\nsettings.json excludes.\n' > "$Bd/internal/ux-ui/atlas.md"
        printf -- '---\ntitle: Java dependency sync behind a proxy\nkeywords: [gradle, proxy]\n---\nSet the proxy.\n' > "$Bd/internal/upgrade/proxy.md"
        printf 'id\tslugs\twhy\nS1\tarchitecture/ext\tx\nS2\tux-ui/atlas\tx\nS3\tNONE\tx\n' > "$T/gold.tsv"
        printf 'S1 | edited Marketplace module, local edits refuse the update\nS2 | Atlas_Core layouts point at the company design system\nS3 | nothing like this\n' > "$T/q.txt"
        UPG_BRAIN="$Bd" python3 "$B/editroute.py" plan --work "$W" --app "$A" --original "$T/orig/App.mpr" --plan "$W/plan.txt" > /dev/null
        python3 -c "import json,sys; [print('brain:', x['module'], [b['path'] for b in x['brain']]) for x in json.load(open(sys.argv[1])) if x['module'] in ('Realmod','Uimod')]" "$W/edit-routes.json"
        UPG_BRAIN="$Bd" python3 "$B/evidence.py" --work "$W" Realmod | head -3
        UPG_BRAIN="$Bd" python3 "$B/brainnotes.py" --eval "$T/gold.tsv" --queries "$T/q.txt"; echo "rc=$?"
        UPG_BRAIN="$T/none" python3 "$B/brainnotes.py" "anything"; echo "no brain rc=$?" ;;
  reset) python3 "$B/editroute.py" plan --work "$W" --app "$A" --original "$T/orig/App.mpr" --plan "$W/plan.txt" > /dev/null
        echo "Handmod # a person forced this" >> "$W/force-ui.txt"; mkdir -p "$W/replay"
        python3 "$B/editroute.py" reset --work "$W"; echo "rc=$?"
        sed 's/^/force-ui.txt: /' "$W/force-ui.txt"; grep -c 'editroute' "$W/approved-step.txt" | sed 's/^/approved-step editroute lines: /'
        ls "$W" | sed 's/^/work: /' ;;
  reroute) python3 "$B/editroute.py" plan --work "$W" --app "$A" --original "$T/orig/App.mpr" --plan "$W/plan.txt" > /dev/null
        # the routed update keeps Cosmo again, now for associations another module owns into it
        printf 'Cosmo idcheck REVIEW (persistence loss or removal: accept it in approved.txt with a reason, or keep), see x\n' > "$S/kept.txt"
        printf 'RED  REMOVED      association Other.C_D  (column/table dropped; intended?)\n' > "$S/step10-Cosmo.idcheck"; touch "$S/step10-Cosmo.log"
        python3 "$B/editroute.py" plan --work "$W" --app "$A" --original "$T/orig/App.mpr" --plan "$W/plan.txt"; echo "rc=$?"
        python3 -c "import json,sys; [print('routes:', x['module'], x['route']) for x in json.load(open(sys.argv[1])) if x['module'] in ('Cosmo','Uimod')]" "$W/edit-routes.json"
        sed 's/^/route-plan.txt: /' "$W/route-plan.txt"
        python3 "$B/editroute.py" plan --work "$W" --app "$A" --original "$T/orig/App.mpr" --plan "$W/plan.txt"; echo "rc=$?" ;;
  access) # cold rfq: the update refused an entity whose only difference is a grant member, an association another module
        # owns into it; a second entity also reads an attribute the package lacks (a real edit)
        O=$T/acc/orig; mkdir -p "$O"
        cat > "$T/acc.json" <<'J'
{"modules": [{"name": "Accmod", "entities": [{"name": "Acct", "persistent": true}]},
             {"name": "Holdmod", "entities": [{"name": "H", "persistent": true}]},
             {"name": "Emp", "entities": [{"name": "E", "persistent": true}],
              "cross": [{"name": "Emp_Acct", "parent": "E", "child": "Accmod.Acct"}, {"name": "Emp_H", "parent": "E", "child": "Holdmod.H"}]},
             {"name": "Demo", "entities": [{"name": "D", "persistent": true}],
              "cross": [{"name": "Demo_Acct", "parent": "D", "child": "Accmod.Acct"}]}]}
J
        python3 "$B/../controls/lib/mkmodel.py" "$T/acc.json" "$O" > /dev/null
        rm -f "$S"/step*; n=1; refuse 1 Accmod "ENTITY Acct"; n=2; refuse 2 Holdmod "ENTITY H"
        printf 'Accmod local edits refuse the update\nHoldmod local edits refuse the update\n' > "$S/kept.txt"
        printf '7 2.0.0 Accmod\n7 2.0.0 Holdmod\n' > "$W/plan.txt"
        python3 - "$W/localedits.json" <<'PY'
import json, sys
json.dump([{"name": m, "cid": 7, "version": "1.0.0", "domain": [{"change": "CHANGED", "kind": "entity", "name": m + ".X",
           "detail": "access rules (security, not data; lost on update)"}], "ui": [], "logic": []} for m in ("Accmod", "Holdmod")],
          open(sys.argv[1], "w"))
PY
        python3 "$B/editroute.py" plan --work "$W" --app "$A" --original "$O/App.mpr" --plan "$W/plan.txt"; echo "rc=$?"
        for f in route-plan.txt force-ui.txt approved-step.txt; do sed "s/^/$f: /" "$W/$f"; done ;;
  gate) python3 - "$B" <<'PY'
import sys
sys.path.insert(0, sys.argv[1])
import cockpitcheck, cockpitpage, cockpitmatrix, steps
def card(rec):
    return {"id": "P-1", "kind": "plan-choice", "title": "Oldmod (module)", "rec_text": rec, "options": [{"label": "x"}],
            "evidence": {"what": ["layout L1: changed in this app"]}}
for rec in ("keep old version (kept list); effort M", "keep old version until 2027-03-01: the vendor fix for X is not out",
            "update to the latest version and carry the edits over"):
    cockpitpage.build_model = lambda w: {"items": [], "signed": True}
    cockpitmatrix.build = lambda w, m: {"rows": [], "band": {"open": {"items": []}}}
    cockpitmatrix.open_questions = lambda m, r=rec: [card(r)]
    steps.load = lambda w: ([], None)
    out = [x for x in cockpitcheck.check("/nonexistent") if x.startswith("keep-recommended")]
    print(f"{rec[:30]!r}: {'CAUGHT' if out else 'ok'}")
PY
  ;;
  *) echo "unknown case ${1:-}"; exit 2 ;;
esac
