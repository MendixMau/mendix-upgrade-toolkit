#!/usr/bin/env bash
# setup-container.sh: make a fresh Linux container (Claude Code cloud, Ubuntu 24.04 amd64) or laptop ready for an
# upgrade run. Re-runnable: every step checks before it acts.
#
#   MENDIX_PAT=... bash setup-container.sh [--plan] <run folder> <mendix version> [<mendix version> ...]
#   e.g. bash setup-container.sh ~/run1 9.24.3.8044 10.24.26.123458 11.15.0
#
# Versions are the full CDN names (Mendix 9/10 carry a build number; see https://cdn.mendix.com/?prefix=runtime/mxbuild-).
# Then: `source <run folder>/upg-env.sh` and follow ../SKILL.md.
# The controls (`make fast`) also want a 10.24 toolset: add a 10.24.x version to the list (B4N1-3).
# Exit: 0 = ready; non-zero = NOT ready, the failing step says what is missing (B4T2-1, B4N1-3: python modules and rsync
#   used to be "installed" with `|| true` and the REFUSED toolcheck ran BEFORE the pip step, exit 0 either way).
# Env: UPG_PYTHON (default python3); UPG_MAVEN_MIRROR = an extra Maven repository base URL tried first for the ANTLR jar
#   (credentials never in the URL: they would show in ps and logs; put them in ~/.netrc, curl --netrc-optional reads it);
#   MXCLI_REF = the mxcli tag, branch or commit step 5 builds (default the commit 78bdfa5, never HEAD); the binary is stamped with it and
#   the pipeline pins the version it finds at triage (bin/mxcli_pin.sh).
#   UPG_SETUP_STEPS = comma list of steps to run (link,zsh,docker,images,antlr,mxcli,toolsets,host,playwright,auth,env,
#   check; default all; the controls run single steps).
# Outside the run folder (DV-1): a normal run first prints "This setup writes outside the run folder:", built from the variables
#   the steps use (MX_HOME, MXCLI_SRC, ANTLR_JAR, PW_DIR, ...); --plan prints only that list and exits 0 before anything is changed
#   (no folder is made, docker is only asked `docker info`).
# Docker that does not answer (GM-4, a hung Docker Desktop used to block setup for good): every SHORT docker call (info, image inspect)
#   is bounded by UPG_DOCKER_TIMEOUT seconds (default 20) and, on timeout, says "docker did not answer in 20 s: is the daemon hung?
#   restart Docker Desktop / dockerd" and stops setup (exit 1; --plan only reports it and goes on). The bound is `timeout` or `gtimeout`
#   when installed, else a background-and-kill fallback in plain bash 3.2 (macOS has no `timeout`). `docker pull` and `docker build` are
#   NOT bounded: they legitimately run for minutes, and a dead daemon is caught by the bounded calls before them.
#
# Why this file (SETUP-1): every batch-1 to batch-3 worker copied T1's runs/t1-purchase-request/setup.sh by hand and
# re-learned its traps. Each step below was needed in a real run (T1, T2, N1 JOURNAL.md):
#  1 ~/Mendix/mxcli-project-toolkit symlink (old-style link)        6 mxbuild + runtime per version from cdn.mendix.com
#  2 zsh (the bin/*.sh wrappers are zsh scripts)                7 python modules (pymongo for bson, bcrypt), rsync
#  3 dockerd (installed but not running in the cloud image)    8 Playwright module (Chromium is preinstalled there)
#  4 base images via mirror.gcr.io (Docker Hub 429), toolkit   9 mxcli marketplace auth from $MENDIX_PAT
#    images built with --network host                         10 upg-env.sh: proxy + CA for mxcli in its container
#  5 mxcli built from source (rsync is installed first: its Makefile needs it; GitHub release downloads 403); the ANTLR jar pre-placed in ~/.m2 first: Maven Central
#    answers 429 from a shared egress IP and `make build` then fails (B4T2-1); mirror fallback
#  11 check: toolcheck.sh --host AFTER step 7; REFUSED or no rsync = exit 1 (B4T2-1, B4N1-3)
# The journey engine is vendored (../vendor/e2e): no other repo is cloned except mendixlabs/mxcli (public).
set -euo pipefail
PLAN=0; [ "${1:-}" = --plan ] && { PLAN=1; shift; }
[ $# -ge 2 ] || { sed -n 2,8p "$0" >&2; exit 2; }
if [ $PLAN = 1 ]; then  # --plan changes nothing: the run folder is not made
  case $1 in /*) R=$1;; *) R=$(pwd)/$1;; esac
else
  R=$(mkdir -p "$1" && cd "$1" && pwd)
fi
shift
TK=$(cd "$(dirname "$0")/.." && pwd); REPO=$(cd "$TK/.." && pwd)
log(){ echo "[setup $(date -u +%H:%M:%S)] $*"; }
# GM-4: bounded docker. upg_timeout SECS CMD...: CMD's exit code, or 124 when it was killed at SECS (bash 3.2: no declare -A, mapfile, GNU-only flags)
UPG_DOCKER_TIMEOUT=${UPG_DOCKER_TIMEOUT:-20}
upg_timeout() {
  local secs=$1 tmo="" c pid wd flag rc; shift
  for c in timeout gtimeout; do command -v "$c" >/dev/null 2>&1 && { tmo=$c; break; }; done
  if [ -n "$tmo" ]; then "$tmo" "$secs" "$@"; return $?; fi
  flag=$(mktemp "${TMPDIR:-/tmp}/upg-timeout.XXXXXX") || return 1; rm -f "$flag"
  "$@" & pid=$!
  # the watchdog installs its TERM trap first and kills its own sleep (jobs -p) on TERM, so a command that finishes in time leaves no orphaned `sleep $secs` behind
  ( trap 'kill $(jobs -p) 2>/dev/null; exit 0' TERM; sleep "$secs" & wait; : > "$flag"; pkill -P "$pid" 2>/dev/null; kill "$pid" 2>/dev/null ) >/dev/null 2>&1 & wd=$!
  rc=0; wait "$pid" 2>/dev/null || rc=$?
  kill "$wd" 2>/dev/null; wait "$wd" 2>/dev/null || true
  if [ -e "$flag" ]; then rm -f "$flag"; return 124; fi
  return $rc
}
dk() { upg_timeout "$UPG_DOCKER_TIMEOUT" docker "$@"; }
dk_hung_msg() { echo "setup: docker did not answer in ${UPG_DOCKER_TIMEOUT} s: is the daemon hung? restart Docker Desktop / dockerd, then rerun setup" >&2; }
dk_hung_die() { dk_hung_msg; exit 1; }
# have_image IMG: 0 = present, 1 = absent; a hung daemon stops setup (a pull or build against it would hang too)
have_image() { local rc=0; dk image inspect "$1" >/dev/null 2>&1 || rc=$?; [ "$rc" != 124 ] || dk_hung_die; [ "$rc" = 0 ]; }
want(){ [ -z "${UPG_SETUP_STEPS:-}" ] || [[ ",$UPG_SETUP_STEPS," == *",$1,"* ]]; }
PY=${UPG_PYTHON:-python3}
MX_HOME=$HOME/Mendix; TK_LINK=$MX_HOME/mxcli-project-toolkit   # step 1
MXCLI_SRC=${MXCLI_SRC:-$HOME/mendixlabs/mxcli}                   # step 5: the mxcli source build folder
MXCLI_REF=${MXCLI_REF:-78bdfa51a2e0a84b971093ebd7b6b82e7596c950}
MXCLI_HOSTBIN=$HOME/.local/bin/mxcli                             # step 5: only a Linux host with no mxcli gets this link
PW_DIR=$HOME/mendix-playwright                                   # step 8
MXCLI_AUTH=$HOME/.mxcli/auth.json                                # step 9
ANTLR_VER=4.13.2
ANTLR_JAR=$HOME/.m2/repository/org/antlr/antlr4/$ANTLR_VER/antlr4-$ANTLR_VER-complete.jar   # where antlr4-tools 0.2.2 looks first (the Maven cache)
# DV-1: every place the selected steps write outside the run folder, printed before anything changes (--plan prints only this)
outside_plan() {
  echo "This setup writes outside the run folder ($R):"
  want link && echo "  - $TK_LINK (old-style link to this clone; created only if absent) in $MX_HOME"
  want zsh && ! command -v zsh >/dev/null && echo "  - system packages: zsh (apt-get install)"
  if want docker; then
    prc=0; dk info >/dev/null 2>&1 || prc=$?
    if [ $prc = 0 ]; then echo "  - dockerd: already running, not started (docker images are added to its store)"
    elif [ $prc = 124 ]; then [ $PLAN = 0 ] || dk_hung_msg; echo "  - dockerd: did not answer in ${UPG_DOCKER_TIMEOUT} s (hung?); a real run stops here until it is restarted"
    else echo "  - dockerd: will be started (nohup dockerd; its log goes to the run folder)"; fi
  fi
  want images && echo "  - docker images in the docker store: eclipse-temurin:11-jdk, eclipse-temurin:21-jdk, postgres:16, mig-mx10, e5-mx9 (and e5-mx9-mono for Mendix 9 below 9.20)"
  want antlr && [ ! -x "$R/tools/mxcli-linux" ] && echo "  - Maven cache: $ANTLR_JAR"
  if want mxcli && { [ ! -x "$R/tools/mxcli-linux" ] || [ "$(readlink -f "$R/tools/mxcli-linux")" = "$(readlink -f "$R/tools/mxcli-bin/mxcli" 2>/dev/null || echo -)" ]; }; then
    echo "  - mxcli source build folder: $MXCLI_SRC (git checkout of mendixlabs/mxcli; the binary itself lands in the run folder)"
    echo "  - Go caches of the mxcli build: ${GOMODCACHE:-$HOME/go/pkg/mod} (modules), ${GOCACHE:-$HOME/.cache/go-build} (build cache); GOTOOLCHAIN=auto may also download a Go toolchain into the module cache"
    [ -x "$R/tools/mxcli-linux" ] && echo "  - note: $R/tools/mxcli-linux is a build made here; if it is not MXCLI_REF ($MXCLI_REF) it is deleted and rebuilt (checked when the step runs)"
    command -v rsync >/dev/null || echo "  - system packages: rsync (apt-get install)"
    echo "  - python packages: antlr4-tools (pip, $PY)"
  fi
  want mxcli && [ "$(uname -s)" = Linux ] && ! command -v mxcli >/dev/null && { [ ! -e "$MXCLI_HOSTBIN" ] || [ -L "$MXCLI_HOSTBIN" ]; } && echo "  - $MXCLI_HOSTBIN (link to the run folder's mxcli, a Linux host with no mxcli)"
  want host && echo "  - python packages for $PY (pip): pymongo, bcrypt, pillow when missing; rsync (apt-get) when missing"
  want playwright && [ ! -d "$PW_DIR/node_modules/playwright" ] && echo "  - $PW_DIR (npm install playwright; npm cache ${npm_config_cache:-$HOME/.npm})"
  want playwright && [ ! -d "${UPG_PW_OPT:-/opt/pw-browsers}" ] && [ -z "${PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD:-}" ] && echo "  - Chromium in the Playwright browser cache (${PLAYWRIGHT_BROWSERS_PATH:-$HOME/.cache/ms-playwright}; npx playwright install chromium)"
  want auth && [ -n "${MENDIX_PAT:-}" ] && [ ! -f "$MXCLI_AUTH" ] && command -v mxcli >/dev/null && echo "  - $MXCLI_AUTH (mxcli auth login)"
  return 0
}
outside_plan
[ $PLAN = 0 ] || exit 0
mkdir -p "$R"/{tools,work,dl} "$MX_HOME"
antlr_jar() {  # B4T2-1: pre-place the jar; repo1.maven.org answers 429, so try mirrors; a non-zip answer (proxy page) is no jar
  local rel=org/antlr/antlr4/$ANTLR_VER/antlr4-$ANTLR_VER-complete.jar base bases=() tried=()
  if [ -s "$ANTLR_JAR" ] && [ "$(head -c 2 "$ANTLR_JAR")" = PK ]; then log "antlr jar present: $ANTLR_JAR"; return 0; fi
  if [ -n "${UPG_MAVEN_MIRROR:-}" ]; then
    case $UPG_MAVEN_MIRROR in
      *://*@*) echo "setup: REFUSED, UPG_MAVEN_MIRROR carries credentials in the URL (they would show in ps and logs); put them in ~/.netrc (machine <host> login <user> password <pw>) and give the plain URL" >&2; exit 2;;
    esac
    bases+=("${UPG_MAVEN_MIRROR%/}")
  fi
  bases+=(https://repo1.maven.org/maven2 https://maven-central.storage-download.googleapis.com/maven2 https://repo.maven.apache.org/maven2)
  mkdir -p "$(dirname "$ANTLR_JAR")"
  for base in "${bases[@]}"; do
    rm -f "$ANTLR_JAR.part"
    if curl -sS -f -L --retry 2 --netrc-optional -o "$ANTLR_JAR.part" "$base/$rel" && [ "$(head -c 2 "$ANTLR_JAR.part" 2>/dev/null)" = PK ]; then
      mv "$ANTLR_JAR.part" "$ANTLR_JAR"; log "antlr jar placed from $base"; return 0
    fi
    tried+=("$base"); log "antlr jar: $base failed (429, unreachable or not a jar), next"
  done
  rm -f "$ANTLR_JAR.part"
  echo "setup: REFUSED, antlr4-$ANTLR_VER-complete.jar could not be fetched from ${tried[*]}; put it at $ANTLR_JAR by hand (or set UPG_MAVEN_MIRROR) and rerun" >&2
  exit 1
}

# 1 toolkit path
if want link; then
  [ -e "$TK_LINK" ] || ln -sfn "$REPO" "$TK_LINK"
  log "toolkit at $(readlink -f "$TK_LINK")"
fi

# 2 zsh
if want zsh && ! command -v zsh >/dev/null; then
  apt-get update -q >/dev/null 2>&1 || true
  apt-get install -y -q zsh >/dev/null 2>&1 || true   # dpkg postinst may report an error; the binary still works
fi
command -v zsh >/dev/null || { echo "setup: zsh missing and apt-get could not install it" >&2; exit 1; }

# 3 docker daemon
if want docker; then
  irc=0; dk info >/dev/null 2>&1 || irc=$?
  [ $irc != 124 ] || dk_hung_die   # a daemon that is there but hung: starting a second dockerd would not help
  if [ $irc != 0 ]; then
    log "starting dockerd"
    (nohup dockerd > "$R/dockerd.log" 2>&1 &)
    for _ in $(seq 1 30); do dk info >/dev/null 2>&1 && break; sleep 1; done
  fi
  dk info --format 'docker {{.ServerVersion}} {{.Driver}}' || { [ $? != 124 ] || dk_hung_die; echo "setup: docker is not answering (dockerd did not start; log $R/dockerd.log)" >&2; exit 1; }
fi

# 4 images: Docker Hub answers 429 from a shared egress IP, so pull from a mirror and retag
want images && for img in eclipse-temurin:11-jdk eclipse-temurin:21-jdk postgres:16; do
  have_image $img && continue
  docker pull --platform linux/amd64 -q $img >/dev/null 2>&1 && continue   # S2: mxrun.sh runs linux/amd64; an arm64 pull (Apple Silicon) would not match
  for m in mirror.gcr.io/library public.ecr.aws/docker/library; do
    docker pull --platform linux/amd64 -q $m/$img >/dev/null 2>&1 && docker tag $m/$img $img && break
  done
  have_image $img || { echo "setup: could not pull $img" >&2; exit 1; }
done
# apt inside the build: plain http through the agent proxy is 405, direct port 80 works with --network host
want images && { have_image mig-mx10 || docker build --platform linux/amd64 -q --network host -t mig-mx10 -f "$TK/bin/docker/Dockerfile.mx10" "$TK/bin/docker"
have_image e5-mx9 || docker build --platform linux/amd64 -q --network host -t e5-mx9  -f "$TK/bin/docker/Dockerfile.mx9"  "$TK/bin/docker"
# BT-1: Mendix 9 before 9.20 has a Mono-era mxbuild: the same image plus Mono
for v in "$@"; do [ "${v%%.*}" = 9 ] && [ "$(echo "$v" | cut -d. -f2)" -lt 20 ] && { have_image e5-mx9-mono || docker build --platform linux/amd64 -q --network host -t e5-mx9-mono -f "$TK/bin/docker/Dockerfile.mx9-mono" "$TK/bin/docker"; break; }; done; }

# rsync before the first thing that needs it: mxcli's Makefile calls it (step 5), design_props_guard.sh does (step 7). A fresh
# container has none: "make: rsync: No such file or directory", exit 2, at the mxcli build. Idempotent; step 11 still refuses a run without it.
ensure_rsync() {
  command -v rsync >/dev/null && return 0
  { apt-get update -q && apt-get install -y -q rsync; } >/dev/null 2>&1 || log "apt-get install rsync failed"
  command -v rsync >/dev/null && log "rsync installed"
  return 0
}
# 5 mxcli from source (public repo mendixlabs/mxcli; a release binary works too: put it at tools/mxcli-linux), at MXCLI_REF
# default: 78bdfa5, the build the pipeline ran on. v0.28.0 is blocked (SETUP.md, "Known problem of v0.28.0")
MXCLI_VER=$MXCLI_REF; [[ $MXCLI_REF =~ ^[0-9a-f]{40}$ ]] && MXCLI_VER=${MXCLI_REF:0:7}   # a full commit id reports as its 7-digit form
# ref_state BIN: 0 = BIN reports MXCLI_REF, 1 = another version, 2 = cannot tell (does not run here, e.g. a Linux binary on a Mac)
ref_state() {
  local v; v=$("$1" --version 2>/dev/null | head -1) || v=""
  [ -n "$v" ] || return 2
  case " $v " in *" $MXCLI_VER "*) return 0;; *) return 1;; esac
}
mxcli_checkout() {  # $1 = source dir: MXCLI_REF (tag, branch or commit) at depth 1, no HEAD
  mkdir -p "$1"; [ -d "$1/.git" ] || git -C "$1" init -q
  git -C "$1" remote get-url origin >/dev/null 2>&1 || git -C "$1" remote add origin https://github.com/mendixlabs/mxcli
  GIT_LFS_SKIP_SMUDGE=1 git -C "$1" fetch -q --depth 1 origin "$MXCLI_REF" && git -C "$1" checkout -q -f --detach FETCH_HEAD
}
if want antlr && [ ! -x "$R/tools/mxcli-linux" ]; then antlr_jar; fi
if want mxcli; then
  # our own earlier build of another ref is rebuilt; a binary somebody put at tools/mxcli-linux is theirs: warned, not replaced
  if [ -x "$R/tools/mxcli-linux" ] && [ "$(readlink -f "$R/tools/mxcli-linux")" = "$(readlink -f "$R/tools/mxcli-bin/mxcli" 2>/dev/null || echo -)" ]; then
    ref_state "$R/tools/mxcli-linux" || [ $? = 2 ] || { log "tools/mxcli-linux is not $MXCLI_VER ($("$R/tools/mxcli-linux" --version 2>/dev/null | head -1)): rebuilding"; rm -f "$R/tools/mxcli-linux" "$R/tools/mxcli-bin/mxcli"; }
  fi
  if [ ! -x "$R/tools/mxcli-linux" ]; then
    ensure_rsync   # the Makefile's build copies with rsync
    src=$MXCLI_SRC
    mxcli_checkout "$src" || { echo "setup: could not fetch mxcli $MXCLI_REF from github.com/mendixlabs/mxcli" >&2; exit 1; }
    "$PY" -m pip install -q 'antlr4-tools==0.2.2'
    # S1: tools/mxcli-linux runs in the linux/amd64 container (mxcli-container.sh), so cross-build it even on a Mac.
    # `make build` runs the generate steps itself (prerequisites grammar = make -C mdl/grammar generate, sync-all, completions;
    # the checkout ships no generated parser). VERSION= stamps the binary: a depth-1 checkout has no tag to describe.
    (cd "$src" && GOOS=linux GOARCH=amd64 ANTLR4_TOOLS_ANTLR_VERSION=$ANTLR_VER GOTOOLCHAIN=auto make build VERSION="$MXCLI_VER" BUILD_DIR="$R/tools/mxcli-bin")
    ln -sfn "$R/tools/mxcli-bin/mxcli" "$R/tools/mxcli-linux"
  fi
  rs=0; ref_state "$R/tools/mxcli-linux" || rs=$?
  case $rs in
    0) log "mxcli: $("$R/tools/mxcli-linux" --version 2>/dev/null | head -1) (MXCLI_REF=$MXCLI_REF)";;
    1) log "WARNING: tools/mxcli-linux reports '$("$R/tools/mxcli-linux" --version 2>/dev/null | head -1)', MXCLI_REF is $MXCLI_REF: the pipeline pins whatever it finds at triage (bin/mxcli_pin.sh)";;
    *) log "mxcli: tools/mxcli-linux does not run on this host ($(uname -s)); its version is checked inside the container";;
  esac
  # S1: the host mxcli is the user's own; only a Linux host with none gets this (Linux) binary, never a Mac or a host that has one
  if [ "$(uname -s)" = Linux ] && ! command -v mxcli >/dev/null && { [ ! -e "$MXCLI_HOSTBIN" ] || [ -L "$MXCLI_HOSTBIN" ]; }; then
    mkdir -p "$(dirname "$MXCLI_HOSTBIN")" && ln -sfn "$(readlink -f "$R/tools/mxcli-linux")" "$MXCLI_HOSTBIN"
  else
    log "host mxcli left alone ($(command -v mxcli || echo "none on PATH; $(uname -s) host")); the container uses $R/tools/mxcli-linux"
  fi
fi

# 6 toolsets per version
want toolsets && for v in "$@"; do
  for kind in mxbuild runtime; do
    tgz=$([ $kind = mxbuild ] && echo "mxbuild-$v.tar.gz" || echo "mendix-$v.tar.gz")
    # GM-1: a non-empty runtime dir is reused only when its runtimelauncher.jar opens as a zip; a truncated extract is redone
    if [ $kind = runtime ] && [ -n "$(ls -A "$R/tools/$kind-$v" 2>/dev/null)" ] && ! "$PY" -I "$TK/bin/zipcheck.py" --find runtimelauncher.jar "$R/tools/$kind-$v" >/dev/null 2>&1; then
      log "$kind-$v: no readable runtimelauncher.jar (corrupt or truncated extract): extracting again"
      rm -rf "$R/tools/$kind-$v"
    fi
    if [ -z "$(ls -A "$R/tools/$kind-$v" 2>/dev/null)" ]; then
      # GM-1: a cached tgz is reused only when gzip -t and tar -tzf read it to the end; else it is deleted and fetched again
      if [ -f "$R/dl/$tgz" ] && ! { gzip -t "$R/dl/$tgz" && tar -tzf "$R/dl/$tgz" >/dev/null; } 2>/dev/null; then
        log "$tgz in dl/ is truncated or corrupt: deleting it and downloading again"
        rm -f "$R/dl/$tgz"
      fi
      [ -f "$R/dl/$tgz" ] || { curl -sS -f -o "$R/dl/$tgz.part" "https://cdn.mendix.com/runtime/$tgz" && mv "$R/dl/$tgz.part" "$R/dl/$tgz"; } \
        || { rm -f "$R/dl/$tgz.part"; echo "setup: $tgz not on the CDN or the download failed (offline?); check the full version name and the network" >&2; exit 1; }
      if ! { gzip -t "$R/dl/$tgz" && tar -tzf "$R/dl/$tgz" >/dev/null; } 2>/dev/null; then
        rm -f "$R/dl/$tgz"; echo "setup: $tgz downloaded but is truncated or corrupt (deleted); rerun setup" >&2; exit 1
      fi
      mkdir -p "$R/tools/$kind-$v" && tar -xzf "$R/dl/$tgz" -C "$R/tools/$kind-$v"
      if [ $kind = runtime ] && ! "$PY" -I "$TK/bin/zipcheck.py" --find runtimelauncher.jar "$R/tools/$kind-$v" >&2; then
        rm -rf "$R/tools/$kind-$v" "$R/dl/$tgz"; echo "setup: $kind-$v extracted without a readable runtimelauncher.jar (removed with its tgz); rerun setup" >&2; exit 1
      fi
    fi
  done
  # BT-1: a Mono-era mxbuild (9.0 to 9.19) gets its mono shim
  [ ! -f "$R/tools/mxbuild-$v/modeler/mxbuild.exe" ] || [ -e "$R/tools/mxbuild-$v/modeler/mxbuild" ] || bash "$TK/bin/mono-shim.sh" "$R/tools/mxbuild-$v"
done

# 7 python modules ($PY -m pip: plain pip may install into another python), rsync (design_props_guard). A failure here is
#   not hidden: step 11 runs toolcheck.sh --host afterwards and exits non-zero (B4T2-1, B4N1-3)
if want host; then
  for m in bson:pymongo bcrypt:bcrypt PIL:pillow; do
    "$PY" -c "import ${m%%:*}" >/dev/null 2>&1 || "$PY" -m pip install -q "${m#*:}" || log "pip install ${m#*:} failed"
  done
  ensure_rsync
fi

# 8 Playwright module for smokewalk.js and the journeys (browsers: /opt/pw-browsers in the cloud image)
if want playwright && [ ! -d "$PW_DIR"/node_modules/playwright ]; then
  mkdir -p "$PW_DIR" && (cd "$PW_DIR" && npm init -y >/dev/null && \
    PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=${PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD:-1} npm install -q playwright@1.56.1 >/dev/null 2>&1)
fi
# S3: no /opt/pw-browsers (not the cloud image) = no Chromium: fetch it, unless the caller set PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD
if want playwright && [ ! -d "${UPG_PW_OPT:-/opt/pw-browsers}" ]; then
  if [ -n "${PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD:-}" ]; then
    log "NEXT-STEP: Chromium not installed (PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD is set): cd $PW_DIR && npx --yes playwright@1.56.1 install chromium"
  else
    log "no /opt/pw-browsers: installing Chromium"
    (cd "$PW_DIR" && npx --yes playwright@1.56.1 install chromium)
  fi
fi

# 9 marketplace auth (host and container both read ~/.mxcli/auth.json); the token never lands in a file here, nor on a
#   command line (ps shows argv to every user): `mxcli auth login` without --token reads it from stdin (B4T2-1)
if want auth && [ -n "${MENDIX_PAT:-}" ] && [ ! -f "$MXCLI_AUTH" ] && ! command -v mxcli >/dev/null; then
  log "NEXT-STEP: no host mxcli on PATH: install one, then: printf %s \"\$MENDIX_PAT\" | mxcli auth login"
elif want auth && [ -n "${MENDIX_PAT:-}" ] && [ ! -f "$MXCLI_AUTH" ]; then
  printf '%s\n' "$MENDIX_PAT" | mxcli auth login >/dev/null
fi
want auth && [ ! -f "$MXCLI_AUTH" ] && log "WARNING: no MENDIX_PAT and no $MXCLI_AUTH: Marketplace downloads and module updates will fail"

# 10 environment for the container wrappers (cloud: the agent proxy and its CA; harmless where they are absent)
ca=/root/.ccr/ca-bundle.crt
want env && {
  echo "export UPG_ROOT=$R UPG_TOOLS=$R/tools WORKDIR=$R/work"
  if [ -f $ca ]; then
    echo "export UPG_EXTRA=\"--network host -e HTTPS_PROXY=\${HTTPS_PROXY:-} -e SSL_CERT_FILE=/etc/upg-ca.crt -v $ca:/etc/upg-ca.crt:ro\""
  fi
  echo "export UPG_SESSION_TIMEOUT=30000"
} > "$R/upg-env.sh"

# 11 check, AFTER step 7 (B4T2-1: it ran before the pip step and printed REFUSED for modules installed a step later;
#   B4N1-3: REFUSED and no rsync were only printed, exit 0)
if want check; then
  UPG_PYTHON=$PY bash "$TK/bin/toolcheck.sh" --host || { echo "setup: NOT READY: toolcheck.sh --host refused (above); install what it names and rerun" >&2; exit 1; }
  command -v rsync >/dev/null || { echo "setup: NOT READY: rsync missing (apt-get install rsync failed); design_props_guard.sh needs it" >&2; exit 1; }
  ls -d "$R"/tools/mxbuild-10.24.* >/dev/null 2>&1 || log "NOTE: no 10.24 toolset in $R/tools: the controls (make fast) want one; rerun with a 10.24.x version added"
fi
log "done: source $R/upg-env.sh, then follow $TK/SKILL.md"
