#!/usr/bin/env bash
# doctor.sh [VERSION ...]: is this machine ready for an upgrade run? One line per check, each failure with its fix.
# Why (cold test WM1): a fresh clone on a Mac hit three setup failures and a five-hour silent hang before any tool named
# what was missing; toolcheck.sh --host covers only the Python modules and a few host tools, the rest failed mid-run.
#
# Checks: bash, git, python (UPG_PYTHON) with its modules (toolcheck.sh --host), mxcli (the run's container binary
# $UPG_TOOLS/mxcli-linux or the host one, and the Marketplace login), docker (CLI, daemon, the toolkit images), node and the
# Playwright module and Chromium for the walks, the mxbuild toolset per VERSION (toolcheck.sh), free disk (diskcheck.sh),
# and the old shared-checkout link (SETUP.md before the split). Reads env.sh values from the environment (source it first).
# Never prints a token. Never changes anything.
# Exit: 0 ready (WARN lines are fine), 1 one or more FAIL lines.
set -u
B=$(cd "$(dirname "$0")" && pwd)
PY=${UPG_PYTHON:-python3}; TOOLS=${UPG_TOOLS:-}; nfail=0; nwarn=0
ok()   { printf 'ok    %-11s %s\n' "$1" "$2"; }
warn() { printf 'WARN  %-11s %s\n      fix: %s\n' "$1" "$2" "$3"; nwarn=$((nwarn + 1)); }
fail() { printf 'FAIL  %-11s %s\n      fix: %s\n' "$1" "$2" "$3"; nfail=$((nfail + 1)); }
have() { command -v "$1" > /dev/null 2>&1; }
# bounded SECS CMD...: a probe that cannot hang (a stopped Docker Desktop makes `docker info` sit silent for minutes; the
# mxcli project toolkit's doctor bounds it the same way). perl ships with macOS; GNU timeout does not.
bounded() { local s=$1; shift; perl -e 'alarm shift; exec @ARGV or exit 127' "$s" "$@"; }

[ -n "$TOOLS" ] || echo "note: UPG_TOOLS is not set; for a run folder made by setup, source <run dir>/env.sh first (toolsets and the run's mxcli are then checked too)"

# shell and git
if [ "${BASH_VERSINFO[0]}" -gt 4 ] || { [ "${BASH_VERSINFO[0]}" = 4 ] && [ "${BASH_VERSINFO[1]}" -ge 4 ]; }; then ok bash "$BASH_VERSION"
else warn bash "bash $BASH_VERSION (macOS ships 3.2; the pipeline and toolcheck refuse bash older than 4.4)" "brew install bash, then put it first on PATH: export PATH=\"\$(brew --prefix)/bin:\$PATH\""; fi
have zsh || fail zsh "no zsh (toolcheck.sh and several helpers are zsh scripts)" "install zsh (apt install zsh)"
if have git; then ok git "$(git --version | cut -d' ' -f3)"; else fail git "no git" "install git"; fi

# python and its modules
if have "$PY"; then
  ok python "$("$PY" -c 'import sys; print(sys.version.split()[0])') ($PY)"
  if out=$(bash "$B/toolcheck.sh" --host 2>&1); then ok host-tools "$(echo "$out" | grep -m1 'host OK' | cut -c1-90)"
  else fail host-tools "$(echo "$out" | grep -m1 -E 'REFUSED|missing' | cut -c1-120)" \
    "on macOS make a venv (PEP 668): python3 -m venv ~/upg-venv && ~/upg-venv/bin/pip install pymongo bcrypt, then export UPG_PYTHON=~/upg-venv/bin/python"; fi
  echo "$out" | grep WARNING | sed 's/^toolcheck: //' | while IFS= read -r l; do printf 'WARN  %-11s %s\n' host-tools "$l"; done
else fail python "no $PY" "install python3, or set UPG_PYTHON"; fi

# mxcli: the binary the run uses and the login
mx=""; [ -n "$TOOLS" ] && [ -e "$TOOLS/mxcli-linux" ] && mx=$TOOLS/mxcli-linux
if [ -n "$mx" ]; then ok mxcli "run binary $mx ($(bash "$B/mxcli_pin.sh" show "$mx" 2> /dev/null | head -1 | cut -d" " -f1))"
elif have mxcli; then warn mxcli "no \$UPG_TOOLS/mxcli-linux; only the host mxcli ($(command -v mxcli))" "run bin/setup-container.sh, or source run/env.sh"
else fail mxcli "no mxcli (neither \$UPG_TOOLS/mxcli-linux nor mxcli on PATH)" "run bin/setup-container.sh <run dir> <versions> (SETUP.md)"; fi
if [ -n "${MENDIX_PAT:-}" ] || [ -s "$HOME/.mxcli/auth.json" ]; then ok login "Marketplace token present (not shown)"
else fail login "no MENDIX_PAT and no ~/.mxcli/auth.json: module updates (marketplace update) cannot download" "export MENDIX_PAT=<personal access token> and rerun setup (step auth)"; fi

# container runtime: docker OR podman. Podman is docker-CLI compatible (same `info`,
# `image inspect` syntax), so every check below runs through $RT instead of a hardcoded
# `docker` — a Podman-only machine (no licence for Docker Desktop) used to be told "no docker
# CLI" even though the pipeline's own images and commands work unchanged under podman.
# UPG_CONTAINER_RUNTIME=<name> forces one; default is docker first (incl. when it IS a podman
# shim, which is transparent and correct), else podman.
RT=${UPG_CONTAINER_RUNTIME:-}
if [ -z "$RT" ]; then
  if have docker; then RT=docker; elif have podman; then RT=podman; fi
fi
if [ -z "$RT" ]; then
  fail docker "no docker or podman CLI" "install Docker Desktop, colima (brew install colima docker && colima start), or Podman (brew install podman && podman machine init && podman machine start)"
elif ! bounded 8 "$RT" info > /dev/null 2>&1; then
  if [ "$RT" = podman ]; then
    fail docker "podman is installed but not answering within 8 s" "podman machine init (first time only), then podman machine start"
  else
    fail docker "the docker daemon does not answer within 8 s (DOCKER_HOST=${DOCKER_HOST:-unset})" "start it: Apple Silicon colima with Rosetta (colima start -p upgrade --vm-type vz --vz-rosetta, then export DOCKER_HOST=unix://\$HOME/.colima/upgrade/docker.sock), or Docker Desktop"
  fi
elif [ "$RT" = podman ] && ! { have docker && bounded 8 docker info > /dev/null 2>&1; }; then
  # the pipeline scripts and the step docs call `docker` by name, so podman alone is not enough
  fail docker "podman answers but docker info does not: the pipeline calls docker" "install the docker shim (the podman-docker package) or alias docker to podman (put a docker symlink to podman on PATH), then rerun"
else
  ok docker "$RT daemon up ($(bounded 8 "$RT" info --format '{{.ServerVersion}} {{.Architecture}}' 2> /dev/null))"
  # Apple Silicon: the amd64 tools need Rosetta in the VM. Under qemu the Linux mxcli dies with SIGSEGV in triage
  # (cold test WM1: "unexpected fault address" in modelsdk decoding; the same commit built natively reads the app fine).
  # Podman's own VM (podman machine) runs amd64 under qemu with no Rosetta option on Apple Silicon at all, so this
  # check only applies to docker/colima; a podman user on Apple Silicon gets the SIGSEGV risk noted instead.
  if [ "$(uname -sm)" = "Darwin arm64" ]; then
    if [ "$RT" = podman ]; then
      warn rosetta "podman machine has no Rosetta profile on Apple Silicon: the Linux mxcli can crash (SIGSEGV) under qemu" \
        "prefer docker + colima with --vz-rosetta on Apple Silicon for this pipeline, or run natively (no container) where that's supported"
    else
      sock=${DOCKER_HOST:-}; [ -n "$sock" ] || sock=$(docker context inspect --format '{{.Endpoints.docker.Host}}' 2> /dev/null); sock=${sock#unix://}
      case $sock in
        */.colima/*/docker.sock)
          prof=$(basename "$(dirname "$sock")"); y=$(dirname "$sock")/colima.yaml
          if grep -q '^rosetta: true' "$y" 2> /dev/null; then ok rosetta "colima profile $prof runs amd64 through Rosetta"
          else fail rosetta "colima profile $prof has no Rosetta: amd64 runs under qemu and the Linux mxcli crashes (SIGSEGV)" \
            "use a Rosetta profile (colima start -p upgrade --vm-type vz --vz-rosetta) and point DOCKER_HOST at it"; fi ;;
        *) warn rosetta "cannot tell whether amd64 runs through Rosetta ($sock)" "Docker Desktop: Settings > General > Use Rosetta for x86_64/amd64 emulation" ;;
      esac
    fi
  fi
  miss=(); for img in mig-mx10 e5-mx9 postgres:16 eclipse-temurin:21-jdk; do "$RT" image inspect "$img" > /dev/null 2>&1 || miss+=("$img"); done
  if [ ${#miss[@]} = 0 ]; then ok images "mig-mx10 e5-mx9 postgres:16 eclipse-temurin:21-jdk ($RT)"
  else fail images "missing: ${miss[*]}" "UPG_SETUP_STEPS=images bash bin/setup-container.sh <run dir> <versions>"; fi
fi

# walks: node, the Playwright module, Chromium
if ! have node; then fail node "no node (smokewalk.js and the journeys run on node)" "install node 20+"
else
  ok node "$(node --version)"
  pw=${UPG_PW_DIR:-$HOME/mendix-playwright}
  if [ ! -d "$pw/node_modules/playwright" ]; then fail playwright "no Playwright module in $pw" "UPG_SETUP_STEPS=playwright bash bin/setup-container.sh <run dir> <versions>"
  elif out=$(cd "$pw" && bounded 60 node -e "require('playwright').chromium.launch({args:['--use-mock-keychain','--password-store=basic']}).then(b=>b.close()).then(()=>console.log('ok'))" 2>&1) && [ "$out" = ok ]; then
    ok chromium "launches (Playwright in $pw)"
  else fail chromium "Chromium does not launch: $(echo "$out" | grep -m1 -iE 'executable|error' | cut -c1-100)" \
    "cd $pw && npx playwright install chromium; if that hangs, curl the zip from playwright.download.prss.microsoft.com (SETUP.md)"; fi
fi

# toolsets per version
for v in "$@"; do
  if [ -z "$TOOLS" ]; then fail toolset "$v: UPG_TOOLS is not set" "source <run dir>/env.sh"; continue; fi
  if [ ! -d "$TOOLS/mxbuild-$v" ]; then fail toolset "$v: no $TOOLS/mxbuild-$v" "bash bin/setup-container.sh <run dir> $v (step toolsets)"
  elif out=$(zsh "$B/toolcheck.sh" "$TOOLS/mxbuild-$v" mxbuild 2>&1); then ok toolset "$v complete"
  else fail toolset "$v: $(echo "$out" | head -1 | cut -c1-110)" "extract mxbuild-$v.tar.gz again into a fresh folder"; fi
done

# disk
if out=$(bash "$B/diskcheck.sh" --need-mb 20000 "${UPG_ROOT:-$HOME}" 2>&1); then ok disk "$(df -h "${UPG_ROOT:-$HOME}" | awk 'NR==2{print $4" free"}')"
else warn disk "$(echo "$out" | head -1 | cut -c1-110)" "a two-rung run needs about 20 GB: free space or point UPG_ROOT at a bigger disk"; fi

# the old shared checkout (SETUP.md before the split): a link that points at a repo without upgrade-toolkit/
old=$HOME/Mendix/mxcli-project-toolkit
if [ -e "$old" ] && [ ! -d "$old/upgrade-toolkit" ]; then
  warn old-link "$old has no upgrade-toolkit/ (a checkout from before the split)" "use this clone's path; nothing needs to live at $old"
fi

echo "doctor: $nfail FAIL, $nwarn WARN"
[ "$nfail" = 0 ]
