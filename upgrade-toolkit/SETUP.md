# Setting up the upgrade toolkit

Who can use it: anyone with this repo and a Mendix account. Nothing else private is needed.

## What you need

| need | why | where it comes from |
|---|---|---|
| this repo, cloned anywhere | every path in SKILL.md starts at `TK`, the folder that holds SKILL.md | `git clone`; no fixed location (setup-container.sh still makes an old-style link `~/Mendix/mendix-upgrade-toolkit` for run folders from before, and warns when that path is another checkout; it never touches `~/Mendix/mxcli-project-toolkit`, where the separate build toolkit lives; `setup-container.sh --plan` lists it) |
| `MENDIX_PAT` (a Mendix personal access token, Marketplace scope) | module updates and template downloads | Mendix Portal, user settings. Keep it in the environment, never in a file or a command line in a log |
| Docker | mxbuild, mx check, app start, Postgres run in containers (Apple Silicon: amd64 must run through Rosetta, see below) | images: eclipse-temurin 11/21, postgres:16 (pulled), mig-mx10/e5-mx9 (built from `bin/docker/`; e5-mx9-mono for Mendix 9 below 9.20, see below) |
| mxcli | Marketplace updates, model reads, diffs | public repo `mendixlabs/mxcli`, built from source at `MXCLI_REF` (default the commit `78bdfa5`; see "The mxcli version" below), or a release binary at `tools/mxcli-linux` |
| mxbuild + runtime per Mendix version on the path | build and run old and new app | `cdn.mendix.com/runtime/` (public) |
| python3 with pymongo, bcrypt; node with Playwright; zsh | the scripts | pip / npm / apt |

Not needed: `MendixMau/mxcli-project-toolkit` (the journey engine is vendored in `vendor/e2e`; set `TOOLKIT_E2E` to
use a live clone instead). The release-note "brain" is in this repo (`company-brain-test/brain/baseline/versions`);
`UPG_BRAIN` points elsewhere (without it `brainpath.py` falls back to that shipped folder). Optional and not shipped: an upgrade scanner (`UPG_SCANNER`, its folder with `scripts/scan.py`); without it the
scanner rows are INVALID, said as such.

## One command

```
MENDIX_PAT=... bash upgrade-toolkit/bin/setup-container.sh ~/run1 <old full version> <new full version> [...]
source ~/run1/env.sh
```

**Which script, which env file.** `bin/setup-container.sh` is for a laptop and any Linux box; `bin/cloud/setup.sh` is for a Claude Code
cloud container (it also links toolsets under `~/.mxcli`). Both write the one file `<run>/env.sh`, the one the pipeline sources, and
each keeps the other's lines when it rewrites it; `upg-env.sh` is only a line that sources `env.sh`. A laptop uses `setup-container.sh`
and `source <run>/env.sh`.

**Apple Silicon.** The Linux mxcli and mxbuild are amd64. Under qemu the Go mxcli crashes at random (all 10 module updates exit 2 in the
cold test that found it), so `bin/dockerhost.sh` refuses any Docker whose amd64 containers do not run through Rosetta, and setup runs it in
step 3 and stops there, before it pulls images. Two Dockers pass: Docker Desktop with "Use Rosetta for x86_64/amd64 emulation on Apple
Silicon" ticked (Settings, General; an amd64 container then shows `/proc/sys/fs/binfmt_misc/rosetta` or a "VirtualApple" cpu; this probe is
ASSUMED from that documented behaviour, not yet run on a Mac by this toolkit), or a colima VM with Rosetta:
`colima start -p upgrade --vm-type vz --vz-rosetta --cpu 6 --memory 12 --disk 60` (mxbuild and the runtime of two Mendix versions plus
Postgres). `colima start` switches the machine's docker context to `colima-upgrade`; run `docker context use <the previous one>` right
after, and give the pipeline the VM through `export DOCKER_HOST=unix://$HOME/.colima/upgrade/docker.sock` so other Docker users on the
laptop are not moved. The java for the ANTLR step must be a host JDK: setup smoke-tests the jar with `java -cp <jar> org.antlr.v4.Tool`
and, when the java on PATH is a wrapper that runs Java elsewhere, stops and says to set `JAVA_HOME`.

Re-runnable. Versions are full CDN names (`10.24.26.123458`; Mendix 11 may be three-part, `11.15.0`). It handles the
cloud-container traps (dockerd not running, Docker Hub 429, GitHub release downloads blocked, the agent proxy CA). Then
put the app under `~/run1/app` (its own git) and follow [SKILL.md](SKILL.md) step 1. It pre-places the ANTLR jar for
the mxcli build (Maven Central 429: mirror fallback; `UPG_MAVEN_MIRROR` adds your own, credentials in `~/.netrc`, never
in the URL), installs pymongo, bcrypt and rsync, and ends with `toolcheck.sh --host`: exit non-zero = not ready, the
last lines say what is missing (B4T2-1, B4N1-3). Add a 10.24.x version to the list for the controls.

## The mxcli version

`MXCLI_REF` (environment, default the full commit id of `78bdfa5`, the build every pipeline run so far used) is the mxcli tag, branch or commit that `bin/setup-container.sh` (step 5) and
`bin/cloud/setup.sh` (step `mxcli`) fetch at depth 1 and build; never HEAD. The binary is stamped with the ref (`make build VERSION=<ref>`),
`mxcli --version` is logged and must report it (a full commit id is stamped and matched as its 7-digit form, `78bdfa5`, which is what that build prints), and a binary an earlier setup built from another ref in the run folder is rebuilt. A binary
you put at `tools/mxcli-linux` yourself is kept and warned about. Build recipe (what the scripts do, for a hand build):

```
git init mxcli && cd mxcli && git remote add origin https://github.com/mendixlabs/mxcli
git fetch --depth 1 origin 78bdfa51a2e0a84b971093ebd7b6b82e7596c950 && git checkout --detach FETCH_HEAD   # a tag, branch or FULL commit id
make -C mdl/grammar generate                       # the checkout ships no generated parser (needs ANTLR 4.13.2, a Java runtime)
make sync-all completions                         # natively: these `go run` a generator that must run on this host
CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build   # only this final build is cross-built (GOOS/GOARCH on the whole make breaks a Mac) -trimpath -ldflags "-s -w -X main.Version=78bdfa5" ./cmd/mxcli
```

`make build VERSION=78bdfa5 BUILD_DIR=<dir>` does all of it (its prerequisites are `grammar sync-all completions`, checked on the v0.28.0
Makefile); the scripts use that. A depth-1 checkout has no tag for `git describe`, which is why the version is passed in.

One run, one version. The pipeline records the mxcli version at triage (`<work>/state/mxcli-version`) and every later step that uses mxcli
compares it; another version is REFUSED with exit 3 and the reason on stderr (`bin/mxcli_pin.sh`; `stepupdate.sh` checks it too when
`UPG_MXCLI_STATE` names the file). Why: DESCRIBE output changed between versions (widgets gain `readOnlyStyle`, microflow anchors are written
in full, context comments are qualified), and the triage localedits.json, the catalog and the replay scripts are compared with what a later
step reads. The container binary and the host binary of `UPG_UPDATE_CMD` (setup.sh T8) must be the same version too. To move a run to another
version on purpose: rerun with `--from triage` (re-records the version and redoes what depends on it), or start a new run.

v0.28.0 is BLOCKED, which is why it is not the default (field log: `controls/fixtures/mxcli-0.28.0/`): `mxcli marketplace update`
fails AFTER its local-edit gate with "install the new version's bundled files: open package target.mpk: ... no such file or directory",
having dropped the module already. `referenceFor` writes `<slot>.mpk` (`cmd/mxcli/cmd_marketplace_diff.go:216`), the target is fetched with slot
`"t"`, and the update reads `target.mpk` (`cmd/mxcli/cmd_marketplace_update.go:177`, slot passed at line 170); the same code is on main.
stepupdate treats the message as a TOOL ERROR (exit 3, tree reverted). The v0.28.0 changes the toolkit already handles (association
refusal, `association-*.mdl` files, all-or-nothing `exec`, no automatic `<Module>.User`) are in place and tested against the real logs.

Condition to move the default to a newer mxcli: (1) a tag that contains the fix, built with `MXCLI_REF=<that tag>`, and (2) one successful
real `marketplace update` with it on a copy of an app (ideally `--save-edits ... --force` on a module with incoming associations), its log
replacing `controls/fixtures/mxcli-0.28.0/update-force-saveedits.log` (FEEDBACK MX28-5). Then change the default in both setup scripts.

## Mendix 9 before 9.20 (Mono-era mxbuild)

The CDN mxbuild for Mendix 9.0 to 9.19 is a .NET Framework build: `modeler/mxbuild.exe` and `mx.exe`, no native launcher, so the plain
`e5-mx9` image cannot run it (INCL 9.3, TOUR 9.4, COLLAB 9.18 stopped at the baseline with `mx9.sh: no .../modeler/mxbuild`). 9.20 and later
are not affected. The recipe, all committed, no binary:

1. Image: `docker build --network host -t e5-mx9-mono -f bin/docker/Dockerfile.mx9-mono bin/docker` (the same as `e5-mx9` plus `mono-runtime
   mono-devel`, about 300 MB more). `bin/setup-container.sh` and `bin/cloud/setup.sh` build it when the source version is 9.x below 9.20.
2. Shims: `bash bin/mono-shim.sh tools/mxbuild-<full ver>` writes the two-line `modeler/mxbuild` and `modeler/mx` (`exec mono
   "$(dirname "$0")/<tool>.exe" "$@"`). The setup runs it after the unpack; `bin/mx9.sh` runs it itself when it finds only the `.exe`.
3. `bin/mx9.sh` picks `e5-mx9-mono` when it finds a shim (`UPG_IMAGE9` overrides) and says how to build the image when it is missing.

## The run log and step timing (automatic)

At the end of the gate step the pipeline appends one row to `$WORK/FIELD-RUNS.md` by itself (`bin/runlog.py --work $WORK`). Set the
code names before the run: `UPG_APP_CODE` (the app's code name; `UPG_APP_NAME` still works), `UPG_APP_TYPE` (a short type, e.g.
`purchase request`) and, only when the gate's own run id is not what you want, `UPG_RUN_ID`. Or write them once into the run:
`echo CODE > $WORK/state/app-code` and `echo "type text" > $WORK/state/app-type`. Without an app code name the row is refused.

- **It never fails the run.** If runlog refuses (the run id is already in the log, exit 3; a customer name, exit 4; no app code
  name, exit 2) the reason is printed, written as a `Run log:` line in `gate-summary.md` and as an information section in
  `NEEDS-JUDGMENT.md`; the exit code and the verdict stay as they were. Fix the cause, then run the command in that section.
- **The row goes into the run folder, not the toolkit checkout (GF-53).** `$WORK/FIELD-RUNS.md` by default; a read-only or
  shared toolkit checkout is never written. To collect rows in the toolkit's own log, set `UPG_FIELD_RUNS=toolkit` (or a path)
  before the gate; that file reaches the toolkit only through a PR: `git commit -- FIELD-RUNS.md ...` with explicit paths, then a
  toolkit PR. The pipeline prints this hint after a row is added there.
- **Step timing.** Every attempt of every step adds a row to `$WORK/state/timing.tsv` (step, start UTC, end UTC, exit code;
  appended, never rewritten, a resumed step gets a new row). `gate-summary.md` gets one `Time:` line from it, and FIELD-RUNS.md
  two columns: `run time (machine)` (the sum of the rows) and `person wait` (from a stop for a person, exit 10 to 15 or any
  NEEDS-JUDGMENT stop, until the pipeline ran again; a stop nobody resumed yet is not counted). The gate step itself is still
  running when its row is written, so it is not in these numbers. A run without `timing.tsv` shows `not recorded`.

## After a container restart

A cloud container restart kills dockerd and the running pipeline. `bash upgrade-toolkit/bin/cloud/resume.sh ~/run1 [~/run2 ...]`
starts dockerd if needed, then relaunches `run-pipeline.sh` detached (appending to the run's log) for every run folder with no
`work/state/gate.done` and no `exit N` last log line. Finished steps are skipped by their done markers; it never uses `--from`.

Check the instruments first: `cd upgrade-toolkit/controls && make fast` (no Docker) or `make test`.

## Unattended runs (pipeline)

`pipeline/` renders one prompt per app (`pipeline/workers/*.py`) and launches it as a cloud session; each worker
pushes `runs/<slug>/` (JOURNAL, SCORECARD, COMPARE, TOOLKIT-FEEDBACK, HANDWORK). See `pipeline/README.md`.

How to read what a run ends with: [READING-THE-VERDICT.md](READING-THE-VERDICT.md).
