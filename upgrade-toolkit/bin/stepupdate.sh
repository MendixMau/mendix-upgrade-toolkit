#!/bin/bash
# stepupdate.sh: run module updates one at a time, each followed by a step idcheck, and stop on the first new finding.
#
# Applies to: any Mendix app in a git work tree (the run's own repo), Mendix 10.x and later (module-import exists).
# Purpose (E1 15, E1 0b, E1 25): every run hand-rolled this loop; a helper edited mid-batch broke a run (bash and zsh
# read scripts lazily), and an idcheck against the original went blind after the first accepted finding.
#
#   stepupdate.sh <app dir> <plan.txt> [--approved approved.txt] [--baseline original.mpr] [--dry-run]
#                 [--force-ui Mod,Mod] [--port-java Mod,Mod] [--saved-edits DIR] [--from N|Module] [--skip Mod,Mod] [--skip-reason Mod=why] [--unattended] [--no-fallback]
#                 [--accept-unsaved Mod,Mod] [--accept-drop Mod,Mod] [--no-convert-made] [--localedits work/localedits.json]
#
# plan.txt: one update per line, "<content id> <version> <ModuleName>", # comments allowed. Order matters: put the
# TARGET modules of cross-module associations last (idcheck.py <app> --xmod lists them); but a target goes BEFORE the
# planned module that OWNS an association into it (planorder.py checks, PV-2, and prints PLAN-ORDER lines at the start).
# Per line:
#   1. git archive HEAD <mpr> and its mprcontents/ into .stepupdate/prevtree/   (the previous step, not the original;
#      an MPR v2 .mpr alone holds no units, NR2-7)
#   2. the update, under heavy-lock.sh; command from UPG_UPDATE_CMD, default:
#        <bin>/mxcli-container.sh marketplace update {cid} --to {version} --module {module} -p {mpr}
#      {cid} {version} {module} {mpr} are replaced by SHELL-QUOTED values (printf %q), so an MPR named
#      "Purchase Request.mpr" stays one argument; quotes already written around a placeholder ('{mpr}', the old
#      workaround) are dropped first (T1-11, T4-1, T8-10). It runs in <app dir>.
#   3. idcheck.py prev.mpr <mpr> --approved <approved> --baseline <original>   (net-zero findings are auto-approved)
#   4. exit 0: git commit "step: <module> <version>"; exit 1: STOP, nothing committed, the tree is left as is for
#      inspection (`git checkout -- . && git clean -fd` reverts it); exit 2 or a failed update: STOP.
# The bin folder is copied to .stepupdate/bin before the first step and everything runs from that copy, so editing the
# toolkit during a batch cannot change a running batch.
# Recognised update refusals (the log is read, so these are not reported as a generic failure):
#   installed version not usable as the local-edit baseline (a package made before 9.18: "range from 9.18.0 to 9.24.99";
#   not published any more: "re-run with --no-baseline", "expected redirect", HTTP 500): retried once with --no-baseline,
#   logged in .stepupdate/no-baseline.txt with a WARNING (local edits in that module are unproven: localedits must have
#   said the domain layer is unchanged) (E5b 27, E5b 26). --no-fallback turns the retry off.
#   the retry refuses with the same 9.18 message: the TARGET package is pre-9.18 and cannot be imported on this
#   version: the line is skipped, the module kept, logged in .stepupdate/kept.txt (E4 16).
#   "Save them first: --save-edits": the module has local edits the update would discard. A module named in
#   --force-ui is updated with "--save-edits <saved-edits>/<Module> --force" (pages, layouts and snippets you will
#   replay from the saved files after the step, E4 13); otherwise STOP and say so.
#   "N element(s) could not be read, so it cannot be shown that the module is unedited": a refusal like the one above
#   (E6), not a generic failure.
# Convert-made edits (E6-13): when a refusal comes after mx convert and the module was installed pristine by an
#   earlier "step:" commit with only step and convert commits since (bin/convertmade.sh), the differences are the
#   convert's own rewrite, not a person's edit. The update is retried once with
#   "--save-edits <saved-edits>/<Module>.convert-made --force" and the step says CONVERT-MADE (nothing to replay; the
#   saved files are kept for reference). --no-convert-made turns this off.
#   --localedits <pre-convert localedits.json> is passed to convertmade.sh: a module with NO "step:" commit (a 9.x
#   source, or a 10.x run without the pre-convert pass) is CONVERT-MADE when only step/convert/build/jar commits follow
#   the original commit and that report (made with --mxcli-diff) showed it clean (T1-15, T3-10, T4-3, T7-12). "build:" commits that leave the
#   model alone and userlib/vendorlib-only commits never break the chain (T5-9, T6-10).
# Refusal kinds that are not a person's edit (T7-15, T5-9, T8-12), forced with --save-edits <saved-edits>/<Module>.<why>:
#   only JAR_DEPENDENCY rows: package-owned (mx convert and Studio Pro rewrite the managed dependency rows; the new
#   package carries its own list), forced with ".package-owned".
#   only JAVA_ACTION rows: bin/usercode.py compares the USER CODE blocks of javasource/<module> with the installed
#   package (.mpk cache); identical code = the convert's parameter metadata, forced with ".convert-made"; different or
#   not comparable = LOGIC edits, keep. Any other mix keeps the LOCAL rule. --no-convert-made turns both off.
# UNSAVED (E7-1): a --force-ui module that only updated through the --no-baseline retry saved nothing (the update has
#   no baseline to tell an edit from the package, so its --save-edits folder stays empty) while localedits listed UI
#   edits. Such a step is not committed: STOP (exit 2), or with --unattended the module is kept. --accept-unsaved Mod
#   commits it anyway; the module is then listed in .stepupdate/unsaved.txt and in the summary, and its UI edits must
#   be replayed by hand from the localedits report of the previous commit.
# The closing "no-baseline" lines list only the modules this invocation retried (no-baseline.txt itself keeps the
#   earlier passes' lines as a record; N1-5: a stale line from a pass that never touched the module was reported).
# kept.txt and no-baseline.txt hold one line per module (the latest reason); a module a later pass commits is removed
#   from kept.txt (E6-12).
# WIDGETS (NS-6): after each update, widgetdiff.py lists the widgets/*.mpk the step changed (name, old -> new version);
#   printed, kept in .stepupdate/widgets.txt and repeated in the summary. A module import replaces shared widgets silently.
# MODULE_RECREATED (NS-7): idcheck's warn lines are printed: every unit id of a module new = deleted and re-imported.
# FILES (T5-17, T3-21, T3F-9): the model check of the update does not see themesource/<module>/, javascriptsource/<module>/ or
#   the Java user code of a module, and the --no-baseline route replaces them without a word (11 brand colours of Atlas_Core
#   _variables.scss were lost, only the screenshots showed it). Before each update of a module that has such folders,
#   localedits.py --files-only compares them with the installed package (.mpk cache) and the folders are copied to
#   .stepupdate/saved/<Module>/. Edited theme/JavaScript files = UI edits: refused like the other UI edits, forced with
#   --force-ui <Module>; after the update every file the update replaced prints "FILES-OVERWRITTEN <path> (saved: ...)", the
#   changed "$var: value;" lines of SCSS files are appended to theme/web/custom-variables.scss when that file exists
#   (REPLAYED-VARS), and the module is listed in the summary. Edited Java user code = logic edit: keep the module. Not
#   comparable (installed package not cached or unreadable): the update may go ahead only when it replaced no saved file;
#   otherwise STOP (FILES-UNKNOWN), or --accept-unsaved <Module> after you have the saved copies.
#   The plan line's content id goes along as --cid <Module>=<id> (B4N1-4: an 11.x MPR records none, so every module with
#   files was FILES-UNKNOWN).
# Tool and network errors are never a verdict on the module (batch 1: T1-11..13, T3-7, T4-1/2, T6-6, T7-13, T8-10/11/21):
#   TOOL ERROR (the update command itself is broken: "accepts 1 arg(s), received N", x509 / certificate, "no
#   credential for profile", "command not found", "proxyconnect tcp" (proxy unreachable), "Cannot connect to the
#   Docker daemon", an mxcli-container.sh refusal, exit 125/126/127): STOP at once, attended or not, tree reverted, nothing recorded in kept.txt, exit 3.
#   NETWORK (TLS handshake timeout, i/o timeout, connection reset, HTTP 5xx except the baseline refusal above, HTTP 429):
#   the update is retried 3 times after 5, 15 and 45 s (UPG_RETRY_SLEEP="5 15 45"). Still failing: STOP (exit 2), or
#   with --unattended the module goes to kept.txt with a NETWORK reason (rerun it, it is not a refusal). The same
#   network error on two modules in a row is the infrastructure: STOP, exit 3.
#   The summary reads "N steps: N run, N committed, N kept, N network".
#   mxcli v0.28.0 (real log: controls/fixtures/mxcli-0.28.0/): "open package target.mpk: open /tmp/mxuNNN/target.mpk: no such
#   file or directory" is a TOOL ERROR too: the update got past the local-edit gate, dropped the module and then could not
#   find the package it had just fetched (the Marketplace update of v0.28.0 reads target.mpk, the download writes t.mpk).
#   The tree is reverted (the module comes back from git), nothing is kept or recorded, exit 3: another mxcli build, not a verdict.
# Associations of OTHER modules (mxcli v0.28.0, #1502): "refusing to update: the update would discard N local element(s) (M
#   association(s) in other modules reach into <Module> and are removed with it)" lists them as ASSOCIATION <Owner>.<Name>
#   rows, and --save-edits writes each as association-<Owner>_<Name>.mdl next to the entity files. They are the PROJECT's own
#   domain model, not the module's: the convert-made and package-owned routes never force over them (an update that "has
#   nothing to replay" would drop them for good); --force-ui <Module> saves them, and after the step they are listed
#   (ASSOCIATIONS-SAVED, .stepupdate/assoc-saved.txt, the summary) with the replay command. Each comes back with a NEW GUID:
#   restore_guid.py puts the original back (pipeline: replay/<Module>.guids). The pipeline notes a saved association that no
#   replay/<Module>.mdl covers.
# One mxcli version per run: when UPG_MXCLI_STATE names the state file the pipeline wrote at triage (<work>/state/mxcli-version),
#   bin/mxcli_pin.sh compares the mxcli in use with it before anything runs; a different version = exit 3 (REFUSED).
# Flags are appended to the end of the update command, so a custom UPG_UPDATE_CMD must end with the mxcli call.
# --from N|Module starts at that plan line, --skip leaves modules out (both logged), so a STOP needs no new plan file
# (E4 7, E4 32, E5b 26). --unattended applies the SKILL stop rule mechanically: a STOP reverts the tree
# (tracked files restored, files the update created removed), records the module in kept.txt and continues with the next line.
# Kept-module dependencies (T6R-7): when kept.txt is not empty at the end of a pass, bin/keptdeps.py checks every module
#   with a "step:" commit against every kept module, both ways (the updated one needs a name the kept one lacks; the kept
#   one calls a name the update removed): FAIL / REVIEW lines with the pair, in .stepupdate/keptdeps.txt; exit 1.
# Model check per step (GM-23, A-1): when UPG_STEPCHECK_CMD is set (the pipeline sets it to bin/stepcheck-run.sh), `mx check` runs on
#   the app before the first step and after every step, BEFORE the commit; bin/stepcheck.py compares the two. An error the step
#   added (a line the check before did not have) undoes the step, writes .stepupdate/stepcheck-stop.txt (the question, the options
#   and what each writes, in the shape bin/widgetfix.py prints) and exits 4: nothing is committed. --unattended does not keep the
#   module for this; a person answers (keep the module, or accept the errors for it: --check-accepted FILE, lines `<Module> <CODE,..>`).
#   A check that cannot finish (mx died, no toolset) is NOT RUN, never "0 errors": said in the output and in the summary, exit 1.
# Batch end (GM-24): with --baseline, idcheck ORIGINAL -> NOW runs when the batch ends, over --approved-total FILE (default
#   --approved; the pipeline passes approved.txt without the step-only acceptances). A finding is printed as BATCH-IDCHECK and exits 1.
# Exit: 0 = every line done, 1 = stopped on a finding (or, with --unattended, at least one module kept or NETWORK,
#       or a kept-module dependency FAIL / REVIEW / INVALID, or a BATCH-IDCHECK finding, or a model check that did not run),
#       2 = input error or a failed update, 3 = TOOL ERROR (fix the toolchain and rerun with --from <Module>),
#       4 = a step added model errors (stepcheck-stop.txt; the step is undone, a person decides).
set -u
if [ "${STEPUPDATE_SNAPSHOT:-}" = "" ]; then
  [ $# -ge 2 ] || { sed -n '2,120p' "$0" | sed 's/^# \{0,1\}//'; exit 2; }
  app=$(cd "$1" 2>/dev/null && pwd) || { echo "stepupdate: no app dir $1" >&2; exit 2; }
  src=$(cd "$(dirname "$0")" && pwd)
  mkdir -p "$app/.stepupdate"
  rm -rf "$app/.stepupdate/bin"; cp -R "$src" "$app/.stepupdate/bin"
  STEPUPDATE_SNAPSHOT=1 STEPUPDATE_SRC="$src" exec bash "$app/.stepupdate/bin/stepupdate.sh" "$@"
fi
bin=$(cd "$(dirname "$0")" && pwd)
# steptrailer KIND: a newline and "Upgrade-Step: S-n" when the run keeps step records (UPG_STEPS_WORK = its work folder) and a step fits this
# kind of commit, else nothing (STEP-RECORDS-PLAN.md slice 5; bin/changelog.py reads it)
steptrailer() { local t; t=$(python3 "$bin/steps.py" trailer --kind "$1" 2> /dev/null); [ -z "$t" ] || printf '\n%s' "$t"; }
app=$(cd "$1" && pwd); plan=$2; shift 2
approved=""; baseline=""; dry=0; portjava=","; forceui=","; saved=""; from=""; skipm=","; skipr=""; unattended=0; fallback=1; acceptun=","; acceptdrop=","; convmade=1; ledits=""; chkacc=""; apptotal=""
while [ $# -gt 0 ]; do
  case "$1" in
    --approved) approved=$2; shift 2;;
    --baseline) baseline=$2; shift 2;;
    --dry-run) dry=1; shift;;
    --force-ui) forceui=",$2,"; shift 2;;
    --port-java) portjava=",$2,"; shift 2;;
    --saved-edits) saved=$2; shift 2;;
    --from) from=$2; shift 2;;
    --skip) skipm=",$2,"; shift 2;;
    --skip-reason) case "$2" in ?*=?*) skipr="$skipr$2"$'\n';; *) echo "stepupdate: --skip-reason wants 'Module=reason', got: $2" >&2; exit 2;; esac; shift 2;;
    --unattended) unattended=1; shift;;
    --no-fallback) fallback=0; shift;;
    --accept-unsaved) acceptun=",$2,"; shift 2;;
    --accept-drop) acceptdrop=",$2,"; shift 2;;
    --no-convert-made) convmade=0; shift;;
    --localedits) ledits=$2; shift 2;;
    --check-accepted) chkacc=$2; shift 2;;
    --approved-total) apptotal=$2; shift 2;;
    *) echo "stepupdate: unknown option $1" >&2; exit 2;;
  esac
done
[ -f "$plan" ] || { echo "stepupdate: no plan file $plan" >&2; exit 2; }
if [ -n "$ledits" ]; then
  [ -f "$ledits" ] || { echo "stepupdate: no localedits file $ledits" >&2; exit 2; }
  ledits=$(cd "$(dirname "$ledits")" && pwd)/$(basename "$ledits")
fi
plan=$(cd "$(dirname "$plan")" && pwd)/$(basename "$plan")
# one mxcli version per run (bin/mxcli_pin.sh): a dry run only prints commands, so it needs no binary
if [ -n "${UPG_MXCLI_STATE:-}" ] && [ -s "$UPG_MXCLI_STATE" ] && [ $dry = 0 ]; then
  bash "$bin/mxcli_pin.sh" check "$UPG_MXCLI_STATE" || { echo "stepupdate: not run: the mxcli differs from the one this run started with ($UPG_MXCLI_STATE)" >&2; exit 3; }
fi
mpr=$(cd "$app" && ls *.mpr 2>/dev/null)
[ "$(echo "$mpr" | grep -c .)" = 1 ] || { echo "stepupdate: $app: expected one .mpr" >&2; exit 2; }
bash "$bin/apptree.sh" "$app" || { echo "stepupdate: STOP, nothing changed (GM-10)" >&2; exit 2; }
# run by hand (repair row 32) under a HOME with no git identity, every commit failed ("Author identity unknown", cold CMM
# DataWidgets step): the same fallback identity as upgrade-pipeline.sh git_identity
if [ -z "$(git -C "$app" config user.email 2> /dev/null || true)" ]; then
  export GIT_AUTHOR_NAME="${GIT_AUTHOR_NAME:-upgrade-pipeline}" GIT_AUTHOR_EMAIL="${GIT_AUTHOR_EMAIL:-upgrade-pipeline@localhost}"
  export GIT_COMMITTER_NAME="${GIT_COMMITTER_NAME:-upgrade-pipeline}" GIT_COMMITTER_EMAIL="${GIT_COMMITTER_EMAIL:-upgrade-pipeline@localhost}"
fi
if [ -n "$(git -C "$app" status --porcelain --untracked-files=no)" ]; then
  echo "stepupdate: $app has uncommitted changes; commit or stash first" >&2; exit 2
fi
grep -qx '.stepupdate/' "$app/.gitignore" 2>/dev/null || echo '.stepupdate/' >> "$app/.gitignore"
grep -qx '.claude/' "$app/.gitignore" 2>/dev/null || echo '.claude/' >> "$app/.gitignore"   # mxcli writes .claude/ into the app (E5b 17)
grep -qx '.mxcli/' "$app/.gitignore" 2>/dev/null || echo '.mxcli/' >> "$app/.gitignore"     # and its catalog into .mxcli/ (E6-4, E7-21)
git -C "$app" add .gitignore >/dev/null 2>&1; git -C "$app" diff --cached --quiet || git -C "$app" commit -qm "stepupdate: ignore .stepupdate/" -m "$(printf 'Changed-By: toolkit\nUpgrade-Change: config stepupdate-gitignore')"
idargs=()
[ -n "$approved" ] && idargs+=(--approved "$(cd "$(dirname "$approved")" && pwd)/$(basename "$approved")")
[ -n "$baseline" ] && idargs+=(--baseline "$(cd "$(dirname "$baseline")" && pwd)/$(basename "$baseline")")
tmpl=${UPG_UPDATE_CMD:-"$(printf %q "$bin/mxcli-container.sh") marketplace update {cid} --to {version} --module {module} -p {mpr}"}
saved=${saved:-$app/.stepupdate/saved-edits}
mkdir -p "$saved"; saved=$(cd "$saved" && pwd)
st="$app/.stepupdate"
# GF-31: .stepupdate/ran.txt names the modules THIS invocation really ran an update for; editroute.py plan holds a module as
# "kept again for the same reason" only when it ran (a module the pass never reached keeps its stale kept.txt line)
[ "$dry" = 0 ] && { mkdir -p "$st"; : > "$st/ran.txt"; }
jcids=(); nkept=0; nnet=0; nrun=0; ncommit=0; files_run=""; lastnet=""; lastnetn=0; lastnetmod=""; nobase_run=""; widg_run=""; roles_run=""; assoc_run=""
# PV-2: a target of a cross-module association updated AFTER the module that owns it loses the association (the owner's
# import would have restored it); planorder.py says so before anything runs. A warning, not a stop: the cheap fix after
# the fact is to reimport the owner (steps/upgrade.md item 1).
python3 "$bin/planorder.py" "$app/$mpr" "$plan" 2>&1 | grep -E '^(ORDER|CYCLE|NOTE)' | sed 's/^/PLAN-ORDER: /'
waived_roles=(); [ -f "$st/roles-waived.txt" ] && waived_roles=(--waive "$st/roles-waived.txt")
rs=${UPG_RETRY_SLEEP:-5 15 45}; read -r -a backoff <<< "${rs//,/ }"   # seconds before each retry; "5,15,45" works too
subst() {  # subst TEMPLATE KEY VALUE: every {KEY} (also '{KEY}' and "{KEY}") becomes the shell-quoted VALUE (T1-11)
  local s=$1 k="{$2}" v out=""
  v=$(printf %q "$3")
  s=${s//\'$k\'/$k}; s=${s//\"$k\"/$k}
  while [[ $s == *"$k"* ]]; do out+=${s%%"$k"*}$v; s=${s#*"$k"}; done
  printf '%s' "$out$s"
}
# TOOL ERROR: the update command cannot work at all; NETWORK: worth a retry. Read from ONE attempt's output.
TOOL_ERR='accepts [0-9]+ arg\(s\), received [0-9]+|x509: |certificate signed by unknown authority|tls: failed to verify certificate|no credential for profile|command not found|proxyconnect tcp|Cannot connect to the Docker daemon|^mxcli-container\.sh: |^docker: |open package [a-z]+\.mpk: open [^ ]+: no such file or directory'
TRANSIENT='TLS handshake timeout|i/o timeout|connection reset|HTTP 5[0-9][0-9]|HTTP 429|Too Many Requests'
netfail=""
runupd() {  # runupd LABEL CMD: the update under the heavy lock, retried on a NETWORK error, STOP on a TOOL ERROR
  local i=0 one="$st/attempt.out" why
  netfail=""
  while :; do
    (cd "$app" && UPG_NAME="${UPG_NAME:-stepupdate}" "$bin/heavy-lock.sh" "stepupdate $mod" bash -c "$2") > "$one" 2>&1
    rc=$?
    cat "$one" >> "$log"
    [ $rc = 0 ] && return 0
    why=$(grep -Eo "$TOOL_ERR" "$one" | head -1)
    [ -z "$why" ] && case $rc in 125|126|127) why="exit $rc from the update command";; esac
    if [ -n "$why" ]; then
      revert
      grep -E "$TOOL_ERR" "$one" | head -2 | sed 's/^/   /'
      echo "STOP: TOOL ERROR in the update of $mod ($why; $log). The toolchain failed, not the module:"
      echo "      nothing kept, tree reverted. Fix it (quoting, proxy CA, credential, docker) and rerun with --from $mod."
      exit 3
    fi
    grep -Eq "$BASELINE_GONE" "$one" && return $rc     # a recognised refusal, not a network error
    why=$(grep -Eo "$TRANSIENT" "$one" | head -1)
    [ -z "$why" ] && return $rc
    if [ $i -ge ${#backoff[@]} ]; then netfail=$why; return $rc; fi
    echo "   network error on $mod ($why): retry $((i + 1)) of ${#backoff[@]} in ${backoff[$i]} s ($1)"
    revert; sleep "${backoff[$i]}"; i=$((i + 1))
  done
}
git -C "$app" ls-files --others --exclude-standard | sort > "$st/untracked-at-start"
revert() {  # back to HEAD: tracked files restored, files the update created removed (untracked files from before stay)
  git -C "$app" checkout -- . 2>/dev/null
  git -C "$app" ls-files --others --exclude-standard | sort | comm -13 "$st/untracked-at-start" - |
    while IFS= read -r f; do case "$app/$f" in "$saved"/*) ;; *) rm -f "$app/$f";; esac; done
}
rec() {  # file module line: one line per module, the latest wins (E6-12: kept.txt was append-only across passes)
  unrec "$1" "$2"; echo "$3" >> "$st/$1"
}
unrec() {  # file module: drop the module's line
  [ -f "$st/$1" ] || return 0
  awk -v m="$2" '$1 != m' "$st/$1" > "$st/$1.tmp" && mv "$st/$1.tmp" "$st/$1"
}
keep() {  # module, reason: unattended keep-and-continue, or STOP
  if [ $unattended = 1 ]; then
    revert; rec kept.txt "$1" "$1 $2"; nkept=$((nkept + 1)); echo "   KEPT: $1 stays at the installed version ($2); tree reverted, next line"
    return 0
  fi
  return 1
}
hasfiles() {  # hasfiles MODULE: does the app carry themesource/javascriptsource/javasource files of this module (T5-17)
  local d
  for d in themesource javascriptsource javasource; do
    [ -d "$app/$d" ] && [ -n "$(find "$app/$d" -maxdepth 1 -mindepth 1 -type d -iname "$1" 2>/dev/null | head -1)" ] && return 0
  done
  return 1
}
assoc_other() {  # assoc_other LOG MODULE: ASSOCIATION rows of the refusal that another module OWNS (mxcli v0.28.0, #1502)
  sed -n '/refusing to update/,/Save them first/p' "$1" | awk -v m="$2" '$1 == "ASSOCIATION" { split($2, a, "."); if (a[1] != m) print $2 }'
}
# GM-23: the model check around each step. stepcheck_run LOG runs UPG_STEPCHECK_CMD ({mpr} and {log} filled in, quoted).
stepchk=${UPG_STEPCHECK_CMD:-}; nchknot=0; chknotrun=""
stepcheck_run() {
  local c; c=$(subst "$stepchk" mpr "$app/$mpr"); c=$(subst "$c" log "$1")
  rm -f "$1"; (cd "$app" && bash -c "$c") > "$st/stepcheck-run.out" 2>&1 || true
  [ -s "$1" ] || printf '[error] [MXCHECK] the check command wrote no log: %s\n' "$(head -1 "$st/stepcheck-run.out" | cut -c1-200)" > "$1"
}
stepcheck_before() {  # the log of the app as it stands now (HEAD, nothing of this step yet); reused when the last step's check was of this HEAD
  [ -n "$stepchk" ] || return 0
  local head; head=$(git -C "$app" rev-parse HEAD 2> /dev/null)
  if [ "$(cat "$st/check-head" 2> /dev/null)" != "$head" ] || [ ! -s "$st/check-prev.log" ]; then
    stepcheck_run "$st/check-prev.log"
    # a crashed check says nothing about this HEAD: do not remember it, so the next step checks again
    if grep -q '\[MXCHECK\]' "$st/check-prev.log" || ! grep -q 'The app contains:' "$st/check-prev.log"; then rm -f "$st/check-head"
    else echo "$head" > "$st/check-head"; fi
  fi
}
BASELINE_GONE='range from 9.18.0 to 9.24.99|range from 10.21.0 to 10.24.99|expected redirect|re-run with --no-baseline|HTTP 500'
n=0; started=0
[ -z "$from" ] && started=1
while read -r cid ver mod rest; do
  case "$cid" in ''|'#'*) continue;; esac
  [ -n "${mod:-}" ] || { echo "stepupdate: plan line needs '<cid> <version> <Module>': $cid $ver" >&2; exit 2; }
  n=$((n + 1))
  if [ $started = 0 ]; then
    if [ "$from" = "$n" ] || [ "$from" = "$mod" ]; then started=1; else echo "== step $n: $mod $ver skipped (before --from $from)"; continue; fi
  fi
  case "$skipm" in *",$mod,"*)
    # why the owner keeps it (--skip-reason Mod=why): carried on the kept line; none given = the line as before
    skipwhy=$(printf '%s' "$skipr" | awk -v m="$mod" 'index($0, m "=") == 1 { r = substr($0, length(m) + 2) } END { print r }')
    echo "== step $n: $mod $ver skipped (--skip)"; rec kept.txt "$mod" "$mod skipped by --skip${skipwhy:+: $skipwhy}"; continue;; esac
  cmd=$(subst "$tmpl" cid "$cid"); cmd=$(subst "$cmd" version "$ver"); cmd=$(subst "$cmd" module "$mod"); cmd=$(subst "$cmd" mpr "$app/$mpr")
  case "$forceui" in *",$mod,"*) cmd="$cmd --save-edits $(printf %q "$saved/$mod") --force";; esac
  echo "== step $n: $mod $ver (content $cid)"
  case "$cid" in *[!0-9]*|0) ;; *) jcids+=(--cid "$mod=$cid");; esac   # B4N1-7: jardedupe reads the installed package by it
  if [ $dry = 1 ]; then echo "   would run: $cmd"; continue; fi
  # GM-10: the app's git tree is checked at the start of EVERY step, not only once at the run start (a worktree whose main clone was deleted mid-run)
  bash "$bin/apptree.sh" "$app" || { echo "stepupdate: STOP at step $n ($mod): the app's git tree is gone; $((n - 1)) step(s) were done, nothing recorded for this one. Fix it and rerun with --from $mod." >&2; exit 2; }
  # NR2-7: an MPR v2 project keeps its units in mprcontents/ beside the .mpr: snapshot both, or idcheck reads no units
  rm -rf "$st/prevtree"; mkdir -p "$st/prevtree"
  mcdir=$(dirname "$mpr")/mprcontents; mcdir=${mcdir#./}
  prevp=("$mpr"); [ -n "$(git -C "$app" ls-tree HEAD -- "$mcdir" 2> /dev/null)" ] && prevp+=("$mcdir")
  git -C "$app" archive HEAD -- "${prevp[@]}" | tar -x -C "$st/prevtree" || exit 2
  prevmpr="$st/prevtree/$mpr"
  fstate=none; authored=0; arc=9
  stepcheck_before
  if hasfiles "$mod"; then
    # T5-17: files outside the model, compared with the installed package BEFORE the update, and kept as a snapshot
    # B4N1-4: the plan's content id goes along (an 11.x MPR records none: every module with files was FILES-UNKNOWN)
    cidarg=(); case "$cid" in *[!0-9]*|0) ;; *) cidarg=(--cid "$mod=$cid");; esac
    # F16: a package can import with a stale AppStoreVersion (WorkflowCommons 3.12.1 records 2.4.0); the version this
    # tool's own last idcheck-PASS step commit installed is the proven one
    iv=$(git -C "$app" log --format=%s 2> /dev/null | sed -n "s/^step: $mod \([^ ]*\) (stepupdate.*/\1/p" | head -1)
    [ -z "$iv" ] || cidarg+=(--installed "$mod=$iv")
    python3 "$bin/localedits.py" "$app/$mpr" --module "$mod" --files-only ${cidarg[@]+"${cidarg[@]}"} --json "$st/step$n-$mod.files.json" > "$st/step$n-$mod.files" 2>&1; frc=$?
    case $frc in 0) fstate=clean;; 1) fstate=edited;; *) fstate=unknown;; esac
    if [ $fstate = unknown ]; then
      # QW-3 (#31): the package could not be compared (HTTP 500, no download): git can still prove the files unedited since
      # the install commit. Anything git cannot prove stays FILES-UNKNOWN. An edit found this way is an edit like any other
      python3 "$bin/themefiles.py" history "$app" "$mod" --mpr "$mpr" --json "$st/step$n-$mod.history.json" > "$st/step$n-$mod.history" 2>&1; hrc=$?
      case $hrc in
        0) fstate=clean-history; echo "   FILES: the package could not be compared; git proves it instead:"; sed 's/^/   /' "$st/step$n-$mod.history";;
        1) fstate=edited; cp "$st/step$n-$mod.history.json" "$st/step$n-$mod.files.json"
           { echo "(by git history, the package could not be compared)"; cat "$st/step$n-$mod.history"; } > "$st/step$n-$mod.files";;
        *) { echo; cat "$st/step$n-$mod.history"; } >> "$st/step$n-$mod.files"
           # GF-55: neither package nor history could prove the files; git still shows WHO changed them last. A file whose
           # newest commit is the app's own (not a "step:" commit, not the first commit) is an edit, not "unknown"
           python3 "$bin/themefiles.py" authored "$app" "$mod" > "$st/step$n-$mod.authored" 2>&1; arc=$?
           [ $arc = 3 ] && sed 's/^/   /' "$st/step$n-$mod.authored"
           if [ $arc = 1 ]; then
             fstate=edited; authored=1; echo "[]" > "$st/step$n-$mod.files.json"
             { echo "(by git authorship, the package could not be compared)"; cat "$st/step$n-$mod.authored"; } > "$st/step$n-$mod.files"
           fi;;
      esac
    fi
    python3 "$bin/themefiles.py" snapshot "$app" "$mod" "$st/saved/$mod" > /dev/null
    if [ $fstate = edited ]; then
      grep '^FILES-EDITED ' "$st/step$n-$mod.files" | sed 's/^/   /'
      jlogic=1; jgone=0
      if grep -q '^FILES-EDITED javasource/' "$st/step$n-$mod.files"; then
        read -r jlogic jgone <<< "$(python3 "$bin/themefiles.py" javalogic "$st/step$n-$mod.files.json" 2> /dev/null || echo "1 0")"
      fi
      if grep -q '^FILES-EDITED javasource/' "$st/step$n-$mod.files" && [ "${jlogic:-1}" = 0 ]; then
        # GF-37: the only Java "edit" is a package file that is gone. A deleted file holds no user code: the update may restore it
        echo "   $mod: $jgone package Java file(s) are deleted in the app; they hold no user code, so this is a FILES edit the update may restore (not Java logic)"
      elif grep -q '^FILES-EDITED javasource/' "$st/step$n-$mod.files"; then
        if [ -n "$(echo "$portjava" | grep ",$mod,")" ]; then
          # cold rfq: a kept module's Java no longer compiled on 11 and its newer version had to come in; its one Java edit
          # (a forced Accept header) is ported by hand onto the new code. The snapshot holds no javasource: copy the edited files.
          for jf in $(grep '^FILES-EDITED javasource/' "$st/step$n-$mod.files" | awk '{ print $2 }'); do
            mkdir -p "$(dirname "$st/saved/$mod/$jf")"; cp "$app/$jf" "$st/saved/$mod/$jf"
          done
          grep '^FILES-EDITED javasource/' "$st/step$n-$mod.files" | awk -v m="$mod" -v d="$st/saved/$mod" '{ print "   PORT-JAVA " m " " $2 " (old file under " d "): the update replaces it, port the edit by hand before the build" }'
        else
          echo "   $mod has local Java USER CODE edits (logic): keep the module at the installed version, or port the edits by hand (--port-java $mod)"
          keep "$mod" "local Java user code edits (FILES-EDITED javasource)" && continue
          echo "STOP: update of $mod refused for local file edits ($st/step$n-$mod.files); nothing changed"; exit 2
        fi
      fi
      if ! grep '^FILES-EDITED ' "$st/step$n-$mod.files" | grep -qv '^FILES-EDITED javasource/'; then
        :
      elif [ -z "$(echo "$forceui" | grep ",$mod,")" ] && [ $authored = 1 ]; then
        # GF-55: git says the team changed these files, but nothing says WHICH lines: forcing would replace them with the package's
        echo "   $mod has theme/JavaScript files the app's own commits changed (the package could not be compared, so which lines is unknown)."
        echo "   The update would replace them: keep $mod at the installed version, or take the update by hand from a copy ($st/saved/$mod)."
        keep "$mod" "own theme/javascript files (git authorship); the update would replace them and the package cannot show what changed" && continue
        echo "STOP: update of $mod refused: its files are the app's own and cannot be compared ($st/step$n-$mod.files); nothing changed"; exit 2
      elif [ -z "$(echo "$forceui" | grep ",$mod,")" ]; then
        echo "   $mod has local theme/JavaScript file edits (UI edits the update replaces silently): rerun with --force-ui $mod; the files"
        echo "   are saved under $st/saved/$mod, the changed SCSS variables go to theme/web/custom-variables.scss (if it exists)."
        keep "$mod" "local theme/javascript file edits refuse the update (FILES-EDITED)" && continue
        echo "STOP: update of $mod refused for local file edits ($st/step$n-$mod.files); nothing changed"; exit 2
      fi
      echo "   FILES edits in $mod are saved under $st/saved/$mod before the update (--force-ui)"
    elif [ $fstate = unknown ]; then
      echo "   FILES-UNKNOWN: $mod has theme/JavaScript/Java files but they cannot be compared with the installed package:"
      sed 's/^/   /' "$st/step$n-$mod.files" | head -3
      echo "   snapshot kept under $st/saved/$mod; a file the update replaces is listed afterwards and stops the step"
    fi
  fi
  log="$st/step$n-$mod.log"; : > "$log"; nrun=$((nrun + 1))
  [ "$dry" = 0 ] && echo "$mod" >> "$st/ran.txt"
  runupd update "$cmd"
  nobase=0; conv=0
  if [ $rc != 0 ] && [ $fallback = 1 ] && grep -Eq "$BASELINE_GONE" "$log"; then
    echo "   installed $mod cannot serve as the local-edit baseline ($(grep -Eo "$BASELINE_GONE" "$log" | head -1)): retry with --no-baseline"
    echo "   WARNING: local edits in $mod are unproven by the update; localedits must show its domain layer unchanged"
    [ $fstate != none ] && echo "   FILES: this route replaces $mod's themesource/javascriptsource files without a check; pre-check: $fstate, snapshot $st/saved/$mod"
    rec no-baseline.txt "$mod" "$mod $ver $(grep -Eo "$BASELINE_GONE" "$log" | head -1)"
    nobase_run="$nobase_run $mod "   # N1-5: the closing summary lists only the modules of THIS invocation
    revert
    refused1=$(grep -Eo 'range from (9\.18\.0 to 9\.24\.99|10\.21\.0 to 10\.24\.99)' "$log" | head -1)   # GF-29: what the FIRST attempt (the installed package) was refused for
    runupd --no-baseline "$cmd --no-baseline"
    nobase=1
    # GF-29: judge the RETRY's own output ($st/attempt.out). $log holds both attempts, so the first attempt's refusal of the
    # installed package was read as the target's and kept.txt said "3.0.0 target package made before 10.21" when it was not
    retry=$(tail -20 "$st/attempt.out" 2> /dev/null)
    if [ $rc != 0 ] && [ -n "$refused1" ] && ! printf '%s\n' "$retry" | grep -q 'range from '; then
      echo "   NOTE: the INSTALLED $mod package was refused as the local-edit baseline ($refused1); the $ver package was not refused:"
      echo "   the --no-baseline retry failed for another reason (last lines below), not because of the target's age"
    fi
    if [ $rc != 0 ] && printf '%s\n' "$retry" | grep -q 'range from 9.18.0 to 9.24.99'; then
      echo "   SKIP: the $mod $ver package itself was made before Studio Pro 9.18 and cannot be imported here (take a later version)"
      revert; rec kept.txt "$mod" "$mod $ver target package made before 9.18"; nkept=$((nkept + 1)); continue
    fi
    # F13 (Purchase Request 10.24, real run): on 11, mx imports no package made before Studio Pro 10.21. The first
    # refusal is the INSTALLED package (the local-edit baseline: Atlas_Core 4.5.0 needs 11, yet "made with 10.5.0");
    # only a refusal on the --no-baseline retry is the target itself, whose update then belongs before the convert
    if [ $rc != 0 ] && printf '%s\n' "$retry" | grep -q 'range from 10.21.0 to 10.24.99'; then
      echo "   SKIP: the $mod $ver package itself was made before Studio Pro 10.21 and Mendix 11 cannot import it: on a 10.x"
      echo "   source this update belongs in the pre-convert plan (plan-pre.txt, steps/triage.md), before the convert"
      revert; rec kept.txt "$mod" "$mod $ver target package made before 10.21 (pre-convert plan)"; nkept=$((nkept + 1)); continue
    fi
  fi
  UNREAD='element\(s\) could not be read, so it cannot be shown that the module is unedited'
  cmrc=1
  if [ $rc != 0 ] && [ $convmade = 1 ] && { grep -q -- '--save-edits' "$log" || grep -Eq "$UNREAD" "$log"; }; then
    "$bin/convertmade.sh" "$app" "$mod" HEAD ${ledits:+--localedits "$ledits"} > "$st/step$n-$mod.convertmade" 2>&1; cmrc=$?
    sed 's/^/   /' "$st/step$n-$mod.convertmade"
  fi
  # mxcli v0.28.0: associations of other modules that point into this one are listed in the same refusal. The convert did not
  # make them and the force-over would drop them with the entity: never forced on a convert-made verdict, --force-ui only.
  oassoc=""; [ $rc != 0 ] && oassoc=$(assoc_other "$log" "$mod" | paste -sd, -)
  if [ -n "$oassoc" ] && [ $cmrc = 0 ]; then
    echo "   CONVERT-MADE does not cover $mod: association(s) of OTHER modules reach into it ($oassoc) and the update removes them;"
    echo "   the convert did not make them, so the update is not forced as convert-made. Use --force-ui $mod (they are saved as association-*.mdl)."
    cmrc=1
  fi
  why="convert-made"; forced="convert-made edits forced"
  if [ $rc != 0 ] && [ $cmrc != 0 ] && [ $convmade = 1 ] && grep -q -- '--save-edits' "$log"; then
    kinds=$(sed -n '/refusing to update/,/Save them first/p' "$log" | awk '/^ +[A-Z_]+ /{print $1}' | sort -u | tr '\n' ' ')
    if [ "$kinds" = "JAR_DEPENDENCY " ]; then
      echo "   PACKAGE-OWNED: $mod is refused for JAR_DEPENDENCY rows only; the managed dependency list belongs to the package"
      echo "   (mx convert and Studio Pro rewrite it, the new version brings its own), so this is not a person's edit"
      cmrc=0; why="package-owned"; forced="package-owned jar dependencies forced"
    elif [ "$kinds" = "JAVA_ACTION " ]; then
      python3 "$bin/usercode.py" "$app" "$mod" --cid "$cid" ${ledits:+--localedits "$ledits"} > "$st/step$n-$mod.usercode" 2>&1; ucrc=$?
      sed 's/^/   /' "$st/step$n-$mod.usercode"
      if [ $ucrc = 0 ]; then
        echo "   CONVERT-MADE: $mod is refused for JAVA_ACTION rows only and its Java user code equals the installed package:"
        echo "   the differences are the Java action metadata the convert rewrote"
        cmrc=0; why=convert-made.java; forced="convert-made Java action metadata forced, user code identical"
      fi
    fi
  fi
  if [ $cmrc = 0 ]; then
    [ "$why" = convert-made ] && echo "   CONVERT-MADE: the refused differences in $mod come from mx convert, not from a person; updating with --force"
    [ "$why" != convert-made ] && echo "   updating $mod with --force"
    why=${why%.java}
    echo "   (saved for reference under $saved/$mod.$why, nothing to replay)"
    [ -n "$(find "$saved/$mod" -type f 2>/dev/null | head -1)" ] && echo "   note: earlier saved edits in $saved/$mod still need their replay"
    revert
    runupd "$why" "${cmd% --save-edits * --force} --save-edits $(printf %q "$saved/$mod.$why") --force"
    conv=1
  fi
  if [ $rc != 0 ] && [ -n "$netfail" ]; then
    # NETWORK: retries exhausted. Not a refusal: the module is not judged. Twice in a row = the infrastructure.
    tail -3 "$log" | sed 's/^/   /'
    if [ "$lastnet" = "$netfail" ] && [ "$lastnetn" = $((n - 1)) ]; then
      revert; rec kept.txt "$mod" "$mod NETWORK: $netfail after ${#backoff[@]} retries (rerun --from $mod)"
      echo "STOP: TOOL ERROR: the same network error ($netfail) on $lastnetmod and $mod in a row, after retries: the"
      echo "      network or proxy is down, not the modules. Tree reverted. Fix it and rerun with --from $lastnetmod."
      exit 3
    fi
    lastnet=$netfail; lastnetn=$n; lastnetmod=$mod
    if [ $unattended = 1 ]; then
      revert; rec kept.txt "$mod" "$mod NETWORK: $netfail after ${#backoff[@]} retries (rerun --from $mod)"; nnet=$((nnet + 1))
      echo "   NETWORK: $mod not updated ($netfail after ${#backoff[@]} retries); not a refusal, rerun it; tree reverted, next line"
      continue
    fi
    revert
    echo "STOP: NETWORK error on $mod ($netfail) after ${#backoff[@]} retries ($log); tree reverted. Rerun with --from $mod."; exit 2
  fi
  if [ $rc != 0 ] && grep -Eq "$UNREAD" "$log"; then
    grep -E "$UNREAD" "$log" | head -1 | sed 's/^/   /'
    echo "   $mod: mxcli cannot read some elements, so it cannot show the module is unedited. Check it with localedits;"
    if [ -n "$ledits" ] && python3 - "$ledits" "$mod" <<'PY'
import json, sys
try:
    e = next((x for x in json.load(open(sys.argv[1])) if isinstance(x, dict) and x.get("name") == sys.argv[2]), None)
except Exception:
    e = None
sys.exit(0 if e and e.get("domain") == [] and e.get("ui") == [] and e.get("logic") == [] else 1)
PY
    then
      # MC-6: the pre-convert localedits report already shows the module unedited: say so, the refusal is the reader's limit
      echo "   localedits ($ledits) shows $mod UNEDITED (no domain, UI or logic edits): the refusal is mxcli's reading limit,"
      echo "   not an edit. Safe route: rerun with --force-ui $mod (nothing to replay)."
    else
      echo "   UI edits only: rerun with --force-ui $mod (saved and replayed); logic edits: keep the module."
    fi
    keep "$mod" "elements could not be read, module not shown unedited" && continue
    echo "STOP: update of $mod refused, elements could not be read ($log); tree left as is"; exit 2
  fi
  if [ $rc != 0 ] && grep -q -- '--save-edits' "$log"; then
    sed -n '/refusing to update/,/--force/p' "$log" | sed 's/^/   /'
    kinds=$(sed -n '/refusing to update/,/Save them first/p' "$log" | awk '/^ +[A-Z_]+ /{print $1}' | sort -u | tr '\n' ' ')
    logic=$(echo "$kinds" | tr ' ' '\n' | grep . | grep -Ev '^(PAGE|LAYOUT|SNIPPET|IMAGE|IMAGECOLLECTION)$' | tr '\n' ' ')
    if [ -n "$oassoc" ]; then
      echo "   ASSOCIATIONS: $(echo "$oassoc" | tr ',' '\n' | grep -c .) association(s) owned by other modules reach into $mod ($oassoc); the update removes them with the entity."
      echo "   They are the app's own domain model. --force-ui $mod saves each as association-<Module>_<Name>.mdl; replay after the updates"
      echo "   (new GUID each: restore_guid.py, or the data in its table is orphaned). Otherwise keep $mod."
    fi
    if [ "$kinds" = "JAR_DEPENDENCY " ]; then
      echo "   $mod is refused for JAR_DEPENDENCY rows only: package-owned, not a logic edit (T7-15). It was not forced"
      echo "   (--no-convert-made, or the forced update failed: see $log)."
    elif [ -n "$logic" ]; then
      echo "   $mod has local LOGIC edits ($logic): keep the module at the installed version, or port the edits"
      echo "   by hand after the update (localedits RED rule). --force-ui is only for pages, layouts and snippets."
    else
      echo "   $mod has local UI edits only (${kinds:-kinds not listed}): rerun with --force-ui $mod to save them under"
      echo "   $saved/$mod and replay them after the step."
    fi
    keep "$mod" "local edits refuse the update" && continue
    echo "STOP: update of $mod refused for local edits ($log); tree left as is"; exit 2
  fi
  if [ $rc != 0 ]; then
    tail -5 "$log"
    # a crash of the tool is not a fact about the module: never record it as kept (cold test WM1: mxcli under qemu
    # crashed on all 10 updates and every module was "kept")
    if grep -qE '^(panic: |fatal error: )|SIGSEGV' "$log"; then
      revert; echo "STOP: mxcli crashed while updating $mod (a tool fault, not the module: $(grep -m1 -E '^(panic: |fatal error: )' "$log")); tree reverted. On Apple Silicon run the containers through Rosetta (bin/dockerhost.sh), then rerun"; exit 3
    fi
    keep "$mod" "update failed, exit $rc" && continue
    echo "STOP: update of $mod failed (exit $rc, $log); tree left as is"; exit 2
  fi
  case "$forceui" in *",$mod,"*)
    nsaved=$(find "$saved/$mod" -type f 2>/dev/null | wc -l | tr -d ' ')
    if [ $nobase = 1 ] && [ "$nsaved" = 0 ] && [ -n "$ledits" ] && python3 - "$ledits" "$mod" <<'PY'
import json, sys
try:
    e = next((x for x in json.load(open(sys.argv[1])) if isinstance(x, dict) and x.get("name") == sys.argv[2]), None)
except Exception:
    e = None
sys.exit(0 if e and e.get("ui") == [] else 1)
PY
    then
      # cold CMM 2026-11-17: Administration was forced for the XASSOC route only; localedits listed no UI edit in it, so
      # saving 0 files lost nothing. It was KEPT as UNSAVED, MendixSSO moved on without it and mx check had 2 CE0117
      echo "   $mod: the --no-baseline route saved 0 files, and localedits ($ledits) lists no UI edits in $mod: nothing to save"
    elif [ $nobase = 1 ] && [ "$nsaved" = 0 ]; then
      # E7-1: the --no-baseline route has no baseline to tell an edit from the package: it saved nothing
      [ $fstate = edited ] && echo "   (its theme/JavaScript FILE edits ARE saved: $st/saved/$mod)"
      echo "   UNSAVED: $mod updated through --no-baseline and saved 0 files; its UI edits (localedits, --force-ui) are NOT saved"
      echo "   and the update has discarded them. Replay them by hand from the localedits report of the previous commit."
      case "$acceptun" in
        *",$mod,"*) rec unsaved.txt "$mod" "$mod $ver no-baseline route saved 0 files (--accept-unsaved): replay its UI edits by hand"
                    echo "   accepted (--accept-unsaved $mod): committing; listed in .stepupdate/unsaved.txt";;
        *) keep "$mod" "UNSAVED: no-baseline route saved 0 of its UI edits" && continue
           echo "STOP: $mod would lose its UI edits unsaved ($log). Keep the module (git checkout -- . && git clean -fd), or rerun"
           echo "      with --accept-unsaved $mod after you have the edits listed for a hand replay. Nothing committed."
           exit 2;;
      esac
    elif [ $conv = 0 ]; then
      echo "   saved edits for replay: $saved/$mod ($nsaved files); replay them before the gate"
    fi
    # GF-48: --force replaces every locally changed element the log lists, saved or not. When the log names elements the
    # save step could not keep (constants), they are gone: STOP before the commit, whatever else was saved. JAR_DEPENDENCY rows
    # never count: the log itself says they are "not evidence of an edit" (ASSUMED: only the other element kinds are lost work)
    nlost=$(python3 - "$log" <<'PY'
import re, sys
t = open(sys.argv[1], errors="replace").read()
m = re.search(r"Proceeding under --force; (\d+) locally changed element\(s\) will be replaced:\n((?:[ \t]+\S.*\n?)*)", t)
s = re.search(r"Saved (\d+) locally changed element", t)
if not m:
    print(0); sys.exit()
rows = [r.split() for r in m.group(2).splitlines() if r.strip()]
jar = sum(1 for r in rows if r and r[0] == "JAR_DEPENDENCY")
print(max(0, int(m.group(1)) - jar - (int(s.group(1)) if s else 0)))
PY
)
    if [ "${nlost:-0}" -gt 0 ] && [ $nobase = 0 ]; then
      echo "   UNSAVED-FORCED: the forced update of $mod replaced $nlost locally changed element(s) that were saved nowhere (constants), whatever else it saved."
      echo "   Their values were reset by the update."
      case "$acceptun" in
        *",$mod,"*) rec unsaved.txt "$mod" "$mod $ver --force replaced $nlost element(s) it did not save (--accept-unsaved): set them again by hand"
                    echo "   accepted (--accept-unsaved $mod): committing; listed in .stepupdate/unsaved.txt";;
        *) keep "$mod" "FORCED-UNSAVED: --force replaced $nlost element(s) and did not save them" && continue
           echo "STOP: $mod would lose $nlost element(s) unsaved ($log). Keep the module (git checkout -- . && git clean -fd), or note the values"
           echo "      from the log, rerun with --accept-unsaved $mod and set them again by hand. Nothing committed."; exit 2;;
      esac
    fi
    # mxcli v0.28.0 (#1502): associations of other modules are saved beside the entity files, one per association
    nas=$(find "$saved/$mod" -maxdepth 1 -type f -name 'association-*.mdl' 2>/dev/null | wc -l | tr -d ' ')
    if [ "${nas:-0}" -gt 0 ]; then
      echo "   ASSOCIATIONS-SAVED: $nas association(s) of other modules reached into $mod and the update removed them; saved as"
      find "$saved/$mod" -maxdepth 1 -type f -name 'association-*.mdl' | sort | sed 's/^/      /'
      echo "      replay after the updates: mxcli exec <file> -p $mpr (each gets a NEW GUID: restore_guid.py puts the original back,"
      echo "      or the rows in its table are orphaned). A saved file nobody replays is a lost association."
      rec assoc-saved.txt "$mod" "$mod $ver: $nas association(s) in $saved/$mod/association-*.mdl"; assoc_run="$assoc_run $mod "
    fi;;
  esac
  if [ $fstate != none ]; then
    ov=$(python3 "$bin/themefiles.py" report "$app" "$mod" "$st/saved/$mod"); orc=$?
    nov=$(echo "$ov" | grep -c . )
    case $fstate in
      clean) [ $orc = 1 ] && echo "   files: $nov file(s) of $mod changed by the new package itself (the installed copy was unedited, nothing lost)";;
      clean-history)
        if [ $orc = 1 ]; then
          echo "   files: $nov file(s) of $mod changed by the new package itself (unedited by git history; saved under $st/saved/$mod)"
          rec overwritten.txt "$mod" "$mod $ver $nov file(s) replaced, unedited proven by git, not by the package, saved under $st/saved/$mod"
        fi;;
      edited)
        if [ $orc = 1 ]; then
          echo "$ov" | sed 's/^/   /'
          python3 "$bin/themefiles.py" replay "$app" "$mod" "$st/step$n-$mod.files.json" | sed 's/^/   /'
          rec overwritten.txt "$mod" "$mod $ver $nov file(s) replaced, saved under $st/saved/$mod (replay by hand what the variable replay above did not)"; files_run="$files_run $mod "
        else echo "   files: the update left the edited files of $mod as they were"; fi;;
      unknown)
        if [ $orc = 1 ]; then
          echo "$ov" | sed 's/^/   /'
          echo "   FILES-UNKNOWN: the update replaced $nov file(s) of $mod and the installed package could not prove they were unedited"
          # GF-55: a big drop in the file count (35 -> 4) is a lost folder, not a package refresh: it is an edit, and
          # --accept-unsaved does not cover it (a field run accepted it and got a 4-file skeleton for 35 own SCSS files)
          nbefore=$(find "$st/saved/$mod" -type f 2>/dev/null | wc -l | tr -d ' ')
          nafter=$(python3 "$bin/themefiles.py" count "$app" "$mod" 2> /dev/null || echo "$nbefore")
          # git proved every file was last installed by a step: commit (authored arc 0): a real package restructure, not a dead end.
          # The backstop applies whenever git could not prove that (arc 2 unknown, arc 3 no own commit but only the first/replay
          # commit behind the files) and --accept-drop <Module> has not been given (ASSUMED: half and 8 files)
          if [ "$nbefore" -ge 8 ] && [ $((nafter * 2)) -le "$nbefore" ] && [ "$arc" != 0 ] && [ -z "$(echo "$acceptdrop" | grep ",$mod,")" ]; then
            echo "   FILES-DROP: $mod had $nbefore theme/JavaScript file(s) before the update and has $nafter after it: that is own work lost, not a package refresh"
            keep "$mod" "FILES-DROP: the update cut $mod's files from $nbefore to $nafter (unproven, treated as edited)" && continue
            echo "STOP: $mod went from $nbefore to $nafter files ($log); --accept-unsaved does not cover this. Keep the module at the installed version"
            echo "      (git checkout -- . && git clean -fd) or merge the saved copies in $st/saved/$mod by hand."
            echo "      (git could not show whether these files are the app's own, so the backstop applies.) If the drop is a real package"
            echo "      restructure, rerun with --accept-drop $mod. Nothing committed."; exit 2
          fi
          case "$acceptun" in
            *",$mod,"*) rec overwritten.txt "$mod" "$mod $ver $nov file(s) replaced, UNPROVEN (--accept-unsaved), saved under $st/saved/$mod"; files_run="$files_run $mod "
                        echo "   accepted (--accept-unsaved $mod): committing; the saved copies are in $st/saved/$mod";;
            *) keep "$mod" "FILES-UNKNOWN: update replaced $nov theme/javascript/java file(s), unproven unedited" && continue
               echo "STOP: $mod lost $nov file(s) that cannot be shown unedited ($log). Compare them with the saved copies in $st/saved/$mod,"
               echo "      or rerun with --accept-unsaved $mod. Nothing committed."; exit 2;;
          esac
        else echo "   files: installed package not comparable, but the update replaced none of the files of $mod"; fi;;
    esac
  fi
  # shellcheck disable=SC2086
  python3 "$bin/idcheck.py" "$prevmpr" "$app/$mpr" ${idargs[@]+"${idargs[@]}"} > "$app/.stepupdate/step$n-$mod.idcheck" 2>&1
  rc=$?
  grep -E '^(RED|FINDINGS|findings|verdict)' "$app/.stepupdate/step$n-$mod.idcheck" | sed 's/^/   /'
  if [ $rc = 1 ]; then
    # E6-7: say REVIEW when idcheck says REVIEW (persistence loss or removal), as upgrade.md and the legend do
    if grep -q '^ *verdict: REVIEW' "$app/.stepupdate/step$n-$mod.idcheck"; then
      why="idcheck REVIEW (persistence loss or removal: accept it in approved.txt with a reason, or keep), see .stepupdate/step$n-$mod.idcheck"
    else why="idcheck finding, see .stepupdate/step$n-$mod.idcheck"; fi
    keep "$mod" "$why" && continue
    echo "STOP: new data-bearing finding after $mod $ver (see .stepupdate/step$n-$mod.idcheck). Nothing committed."
    echo "      Decide: keep the old module (git checkout -- . && git clean -fd), or approve the line with a reason and rerun."
    exit 1
  elif [ $rc != 0 ]; then
    echo "STOP: idcheck input error after $mod"; exit 2
  fi
  # NS-7: idcheck warns when the update re-created a module (every unit id new) instead of updating it in place
  grep -E '^(warn|info MODULE_RECREATED) ' "$app/.stepupdate/step$n-$mod.idcheck" | sed 's/^/   /'
  # NS-6: a module import also replaces shared widgets/*.mpk (notification-service cdd62cc5: the Email Connector import
  # swapped Datagrid 2.28.3 -> 2.30.6 and 8 more; reverted on day 111). Name every widget the step changed.
  # GF-41: a step to a LOWER module version keeps the newer widgets/*.mpk; the package's own widgets go back first, so the
  # WIDGETS lines below show the net change and update-widgets never binds the widget to the newer version's properties
  mpkc="${UPG_CACHE:-$HOME/.cache/upgrade-toolkit/mpk}/$cid-$ver.mpk"; case "$cid" in *[!0-9]*|0|'') mpkc="";; esac
  oldv=$(git -C "$app" log --format=%s 2> /dev/null | sed -n "s/^step: $mod \([^ ]*\) .*/\1/p" | head -1)
  wrest=$(python3 "$bin/widgetpkgfix.py" restore "$app" --module "$mod" --new-version "$ver" --package "$mpkc" ${oldv:+--old-version "$oldv"} --prev "$prevmpr" 2>&1)
  wout=$(python3 "$bin/widgetdiff.py" "$app" 2>/dev/null)
  [ -z "$wrest" ] || { echo "$wrest" | sed 's/^/   WIDGETS: /'; }
  # GF-43: the widget definitions mxcli cached for a package this step changed are stale (12's def judged 10.0.0's properties)
  wdefs=$(python3 "$bin/widgetpkgfix.py" defs "$app" 2>&1); [ -z "$wdefs" ] || echo "$wdefs" | sed 's/^/   WIDGETS: /'
  if [ -n "$wout" ]; then
    echo "   WIDGETS: the $mod update changed $(echo "$wout" | wc -l | tr -d ' ') widget package(s) in widgets/ (check each one is meant; widgets.md section 3):"
    echo "$wout" | sed 's/^/      /'
    rec widgets.txt "$mod" "$mod $ver: $(echo "$wout" | sed 's/^widgets\///' | paste -sd ';' - | sed 's/;/; /g')"; widg_run="$widg_run $mod "
  fi
  # PLM-26: a module role the update added and no user role holds. mx check is clean and the build is green; the smoke rung
  # then fails with "Executing action failed for security reasons" (Atlas_Core 3.21 User/Administrator, 13 of 15 pages).
  # Listed now, repeated in the summary (exit 1) until each role is mapped or waived in .stepupdate/roles-waived.txt.
  python3 "$bin/rolecheck.py" "$prevmpr" "$app/$mpr" ${waived_roles[@]+"${waived_roles[@]}"} > "$st/step$n-$mod.roles" 2>&1; rcr=$?
  rout=$(grep -E '^(UNMAPPED|REMOVED-MAPPED|DANGLING)' "$st/step$n-$mod.roles")   # MC-9: also mapped roles the update removed
  [ $rcr = 2 ] && echo "   NEW-ROLES: rolecheck could not judge $mod ($(head -1 "$st/step$n-$mod.roles")); module roles NOT checked"
  unrec newroles.txt "$mod"
  if [ -n "$rout" ]; then
    echo "   NEW-ROLES: the $mod update left module role(s) unmapped, or mapped to a role that no longer exists (fix before the smoke rung):"
    echo "$rout" | sed 's/^/      /'
    # MC-2: a role mapping is a model commit; before the convert it breaks convertmade's neutral chain for every module
    echo "      (before a convert: map after the post-convert pass, or waive now; a model commit between the last step and the convert, see convertpre.py)"
    rec newroles.txt "$mod" "$mod $ver: $(echo "$rout" | sed -E 's/^(UNMAPPED|REMOVED-MAPPED|DANGLING) */\1 /' | paste -sd ';' - | sed 's/;/; /g')"; roles_run="$roles_run $mod "
  fi
  # NR2-22: the Linux mxcli writes mpk entries named with Windows separators (OQL 4.2.0 and 5.1.0) as literal files such as
  # `javasource\oql\actions\X.java` in the app root; the real javasource/oql goes missing, idcheck and mx check stay green and
  # mxbuild turns every OQL action into a "not implemented" stub. Move them home before the commit; a refusal stops the batch.
  bsl=$(python3 "$bin/repair/backslash_paths.py" "$app" 2> /dev/null | grep -c '^BACKSLASH')
  if [ "${bsl:-0}" -gt 0 ]; then
    if python3 "$bin/repair/backslash_paths.py" "$app" --apply > "$st/step$n-$mod.backslash" 2>&1; then
      echo "   BACKSLASH: $bsl file(s) of $mod were written with Windows separators in their name and moved to their real path (.stepupdate/step$n-$mod.backslash)"
      rec backslash.txt "$mod" "$mod $ver: $bsl file(s) moved home from backslash names"
    else
      echo "STOP: $mod wrote $bsl file(s) with a backslash in the name and the move was refused (see .stepupdate/step$n-$mod.backslash). Nothing committed."; exit 2
    fi
  fi
  # GM-23 / A-1: read the model check before the commit, never after it (a chained "update && git commit" committed 31 CE1613)
  if [ -n "$stepchk" ]; then
    stepcheck_run "$st/step$n-$mod.check"
    python3 "$bin/stepcheck.py" "$st/check-prev.log" "$st/step$n-$mod.check" --module "$mod" --version "$ver" ${chkacc:+--accepted "$chkacc"} ${forceui:+--force-ui "$forceui"} --fields > "$st/step$n-$mod.stepcheck" 2>&1; crc=$?
    grep -E '^(NEW|stepcheck:)' "$st/step$n-$mod.stepcheck" | sed 's/^/   /'
    case $crc in
      0) cp "$st/step$n-$mod.check" "$st/check-prev.log.next";;
      1) grep -E '^[QROWB]	' "$st/step$n-$mod.stepcheck" > "$st/stepcheck-stop.txt"
         revert; rm -f "$st/check-prev.log.next"
         echo "STOP: $mod $ver adds model errors (see .stepupdate/step$n-$mod.stepcheck). Step undone, nothing committed; a person decides (.stepupdate/stepcheck-stop.txt)."; exit 4;;
      *) echo "   STEPCHECK NOT RUN: the model check after $mod did not finish ($(head -1 "$st/step$n-$mod.stepcheck" | cut -c1-160)); the step is committed on the data check alone"
         nchknot=$((nchknot + 1)); chknotrun="${chknotrun:+$chknotrun,}$mod"; rm -f "$st/check-prev.log.next";;
    esac
  fi
  # GF-42: a step never changes the storage format (MPR v2 -> v1 is what a rewriting tool does); refused and undone, not committed
  # exit 1 = collapsed; exit 2 = could not tell (no .mpr): not a collapse, nothing is undone for it
  smsg=$(bash "$bin/mprstorage.sh" guard "$app" 2> /dev/null); grc=$?
  if [ $grc = 1 ]; then
    revert; rm -f "$st/check-prev.log.next"
    # an old stepcheck-stop.txt (an earlier model-check stop) would be shown as THIS stop's question: cleared, the STOP line below is the reason
    rm -f "$st/stepcheck-stop.txt"
    echo "STOP: $mod $ver: $smsg Step undone, nothing committed."; exit 4
  fi
  git -C "$app" add -A . || { echo "STOP: git add failed"; exit 2; }
  if git -C "$app" diff --cached --quiet; then
    echo "   no change to commit"
  else
    git -C "$app" commit -qm "step: $mod $ver (stepupdate, idcheck PASS$([ $conv = 1 ] && echo ", $forced"))" -m "$(printf 'Changed-By: toolkit\nUpgrade-Change: module-update stepupdate'; steptrailer module-update)" || { echo "STOP: git commit failed"; exit 2; }
    echo "   committed $(git -C "$app" rev-parse --short HEAD)"; ncommit=$((ncommit + 1))
    if [ -f "$st/check-prev.log.next" ]; then mv "$st/check-prev.log.next" "$st/check-prev.log"; git -C "$app" rev-parse HEAD > "$st/check-head"; fi
    updated="${updated:+$updated,}$mod"
  fi
  unrec kept.txt "$mod"   # E6-12: a module a later pass commits is not kept any more
done < "$plan"
# B2-JAR (N1-6, T2-14): nothing resyncs jars after module updates, and mx sync-java-dependencies cannot run behind the agent
# proxy (T2-9). Every pass that ends without a STOP cleans userlib/vendorlib itself: older duplicates and stale jars of
# modules no longer in the app go (repair/jardedupe.py --apply), the list is logged and committed as a "jar:" commit
# (neutral for convertmade). UPG_NO_JARCLEAN=1 skips it. jardedupe refuses removals that rest on vendorlib while no vendorlib
# SBOM is newer than the module update (T5-16): then the sync (repair row 2) comes first.
# UPG_VENDORLIB_SYNCED=1 states that vendorlib is current (a sync ran after this module set, e.g. the host-Maven fallback).
# Updated modules (B4T2-10, B4N1-7): this pass's commits AND every earlier "step:" commit (--updated-from-git), so a
# module committed by an earlier pass (a first pass, then a --from / --accept-unsaved rerun) does not keep its old
# version's markers as CONFLICT (CommunityCommons 10's pdfbox 2.0.24 next to vendorlib pdfbox 3: javac Misc.java:643).
# The plan's content ids go along (--cid): where the installed package is in the .mpk cache, its own userlib list says
# which markers are current, whatever the commit history says.
if [ $dry = 0 ] && [ $nrun -gt 0 ] && [ -z "${UPG_NO_JARCLEAN:-}" ] && [ -d "$app/userlib" ]; then
  python3 "$bin/repair/jardedupe.py" "$app" --apply ${UPG_VENDORLIB_SYNCED:+--vendorlib-synced} --updated "${updated:-}" --updated-from-git \
    ${jcids[@]+"${jcids[@]}"} --log "$st/jardedupe.log" > /dev/null 2>&1; jrc=$?
  if [ $jrc = 0 ]; then
    echo "stepupdate: jar cleanup (jardedupe --apply), list in $st/jardedupe.log:"; grep -E '^(REMOVE|UNMATCHED|SHADOWED|summary|shadowed)' "$st/jardedupe.log" | sed 's/^/   /'
    # a 9.x source has no vendorlib/ before the first sync-java-dependencies: `git add` with a missing pathspec stages
    # NOTHING, the jar deletions stayed uncommitted and the routed pass refused (TLT, 9.24 to 10.24). Name only what exists.
    jpaths=(); for jd in userlib vendorlib; do [ -d "$app/$jd" ] && jpaths+=("$jd"); done
    git -C "$app" add -A -- "${jpaths[@]}" >/dev/null 2>&1
    # a folder that EXISTS but git knows nothing in (an empty userlib/ on a 10.x app whose jars all live in vendorlib/) is
    # a pathspec error for `git commit -- userlib`: the whole commit failed and the vendorlib deletions stayed staged, so
    # the routed pass refused (SNOW, 10.24 to 11.12). Commit only the folders git has a file or a staged change in.
    cpaths=(); for jd in "${jpaths[@]}"; do
      [ -z "$(git -C "$app" ls-files -- "$jd")$(git -C "$app" diff --cached --name-only -- "$jd")" ] || cpaths+=("$jd")
    done
    [ ${#cpaths[@]} = 0 ] || git -C "$app" diff --cached --quiet -- "${cpaths[@]}" || git -C "$app" commit -qm "jar: jardedupe --apply after module updates" -m "$(printf 'Changed-By: toolkit\nUpgrade-Change: repair repair-row-3'; steptrailer repair)" -- "${cpaths[@]}"
  else
    if [ $jrc = 2 ]; then   # T5-16: vendorlib is not proven current; the module updates just changed the module set
      echo "stepupdate: jar cleanup REFUSED, vendorlib is stale (nothing removed): run mx sync-java-dependencies (repair row 2), then repair/jardedupe.py --apply (repair row 3)"
      echo "   no sync possible (cloud proxy, B4T2-9): the jars marked 'rests on vendorlib' in $st/jardedupe.log need their newer copy"
      echo "   in vendorlib/; check them, then UPG_VENDORLIB_SYNCED=1 or jardedupe.py --apply --vendorlib-synced (steps/upgrade.md)"
    else
      echo "stepupdate: jar cleanup FAILED; run repair/jardedupe.py by hand before the build"
    fi
  fi
fi
# GM-24: the original-to-now idcheck at the end of every batch. Step mode compares each step with the one before, so a drop one
# step accepted and a re-creation with new GUIDs at a later step each looked fine (MxModelReflection dropped 11 ExcelImporter
# associations, ExcelImporter re-created them: step idcheck PASS twice, 11 GUID_CHANGED only at the end, data gone). Here the
# comparison is against the ORIGINAL with the written approvals only (not the step-only ones).
batchfail=""
if [ $dry = 0 ] && [ $nrun -gt 0 ] && [ -n "$baseline" ] && [ -f "$baseline" ]; then
  bargs=(--approved "$(cd "$(dirname "${apptotal:-$approved}")" && pwd)/$(basename "${apptotal:-$approved}")")
  [ -n "${apptotal:-$approved}" ] && [ -f "${apptotal:-$approved}" ] || bargs=()
  python3 "$bin/idcheck.py" "$baseline" "$app/$mpr" ${bargs[@]+"${bargs[@]}"} > "$st/batch.idcheck" 2>&1; brc=$?
  if [ $brc = 1 ]; then
    batchfail=1
    echo "stepupdate: BATCH-IDCHECK original -> now has open data-bearing finding(s) (.stepupdate/batch.idcheck):"
    grep -E '^RED ' "$st/batch.idcheck" | head -12 | sed 's/^/   BATCH-IDCHECK /'
  elif [ $brc = 0 ]; then echo "stepupdate: batch idcheck original -> now: PASS"
  else echo "stepupdate: BATCH-IDCHECK could not run (idcheck exit $brc, .stepupdate/batch.idcheck); the pipeline's total idcheck still runs"; fi
fi
[ -z "$chknotrun" ] || echo "stepupdate: STEPCHECK NOT RUN after: $chknotrun (the model check did not finish; those steps were committed on the data check alone)"
# T6R-7: a module that stays while others move. An updated module that needs something the kept version lacks (T6R:
# AmazonTranslateConnector 3.1.1 committed, AWSAuthentication kept at 2.1.2: 12 CE1613 and javac) or a kept module that
# calls what the update removed showed up only at mx check. Every pass that leaves kept.txt non-empty runs keptdeps.py
# over the committed tree: updated = the modules with a "step:" commit, kept = kept.txt. FAIL, REVIEW and INVALID
# (exit 2: a kept.txt module not in the model, no git) each make the pass exit 1, with the pair named.
kdout=""
[ $dry = 0 ] && [ ! -s "$st/kept.txt" ] && rm -f "$st/keptdeps.txt" "$st/keptdeps.json"   # nothing kept: no stale report
if [ $dry = 0 ] && [ -s "$st/kept.txt" ]; then
  python3 "$bin/keptdeps.py" "$app" --kept-file "$st/kept.txt" --updated-from-git --json "$st/keptdeps.json" > "$st/keptdeps.txt" 2>&1; kdrc=$?
  case $kdrc in
    0) ;;
    1) kdout=$(grep -E '^(FAIL|REVIEW|keptdeps: verdict)' "$st/keptdeps.txt");;
    *) kdout="keptdeps: INVALID (exit $kdrc): $(head -1 "$st/keptdeps.txt"); the kept modules are NOT checked against the updated ones";;
  esac
  grep '^WARNING: skipped ' "$st/keptdeps.txt" | sed 's/^/stepupdate: keptdeps /' || true   # GF-40: a step subject that is not a module is skipped, the rest is checked
fi
# U1: the kept count is what kept.txt holds (a --skip module and a pre-9.18 package are kept without passing the counter);
# NETWORK lines are counted as network, not as kept
nkept=0; [ -f "$st/kept.txt" ] && nkept=$(grep -vc ' NETWORK: ' "$st/kept.txt")
echo "stepupdate: $n steps: $nrun run, $ncommit committed, $nkept kept, $nnet network"
if [ $nkept -gt 0 ] || [ $nnet -gt 0 ] || [ -n "$nobase_run" ] || [ -s "$st/unsaved.txt" ] || [ -n "$files_run" ] || [ -n "${widg_run:-}" ]; then
  [ -s "$st/kept.txt" ] && sed 's/^/   kept: /' "$st/kept.txt"
  [ $nnet -gt 0 ] && echo "   NETWORK lines are not refusals: rerun those modules (--from / --skip) when the network is back"
  [ -n "$nobase_run" ] && while IFS= read -r l; do
    case "$nobase_run" in *" ${l%% *} "*) echo "   no-baseline (local edits unproven): $l";; esac
  done < "$st/no-baseline.txt"
  [ -s "$st/unsaved.txt" ] && sed 's/^/   UNSAVED (replay by hand): /' "$st/unsaved.txt"
  [ -n "$files_run" ] && [ -s "$st/overwritten.txt" ] && while IFS= read -r l; do
    case "$files_run" in *" ${l%% *} "*) echo "   FILES-OVERWRITTEN: $l";; esac
  done < "$st/overwritten.txt"
  [ -n "${widg_run:-}" ] && [ -s "$st/widgets.txt" ] && while IFS= read -r l; do
    case "$widg_run" in *" ${l%% *} "*) echo "   WIDGETS: $l";; esac
  done < "$st/widgets.txt"
  [ -z "$kdout" ] && { [ $nkept -gt 0 ] || [ $nnet -gt 0 ]; } && exit 1
fi
if [ -n "$assoc_run" ] && [ -s "$st/assoc-saved.txt" ]; then
  echo "stepupdate: ASSOCIATIONS-SAVED (owned by other modules, removed by the update, to replay: mxcli exec <file>, then restore_guid.py):"
  while IFS= read -r l; do
    case "$assoc_run" in *" ${l%% *} "*) echo "   $l";; esac
  done < "$st/assoc-saved.txt"
fi
if [ -n "$roles_run" ] && [ -s "$st/newroles.txt" ]; then
  echo "stepupdate: NEW MODULE ROLES with no user role (PLM-26; rolecheck.py; waive with a reason in $st/roles-waived.txt):"
  while IFS= read -r l; do
    case "$roles_run" in *" ${l%% *} "*) echo "   NEW-ROLES: $l";; esac
  done < "$st/newroles.txt"
  [ -z "$kdout" ] && exit 1
fi
if [ -n "$kdout" ]; then
  echo "stepupdate: kept-module dependencies ($st/keptdeps.txt; decide per pair: update the kept module too, hold the"
  echo "   updated one back, or port the missing elements; REVIEW closes with mx check and the build):"
  echo "$kdout" | sed 's/^/   /'
  exit 1
fi
[ -z "$batchfail$chknotrun" ] || exit 1
exit 0
