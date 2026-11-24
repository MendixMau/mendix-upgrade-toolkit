#!/bin/bash
# dockerhost.sh: print the DOCKER_HOST the amd64 tools must use, or explain why there is none (exit 1).
# Apple Silicon only needs it: the Linux mxcli and mxbuild are amd64 and must run through Rosetta. Under qemu (a colima VM
# without Rosetta) the Go mxcli crashes at random and misreads files: cold test WM1 rung 1 had all 10 module updates fail
# with exit 2 ("growslice: len out of range", "zip: checksum error" on a widget that is fine on the host), and stepupdate
# recorded every one as "kept". The doctor knew (doctor.sh, rosetta), but nothing in the run checked it.
# Order: a DOCKER_HOST already set to a Rosetta VM; else the current docker context when it is one; else the first
# running colima profile with rosetta: true; else (GF-6) the current Docker, when an amd64 container in it runs through Rosetta
# (Docker Desktop with "Use Rosetta for x86_64/amd64 emulation" on). Not Apple Silicon: prints the current DOCKER_HOST (may be empty), exit 0.
[ "$(uname -sm)" = "Darwin arm64" ] || { echo "${DOCKER_HOST:-}"; exit 0; }

rosetta_sock() {   # $1 a unix socket path: is it a colima VM with Rosetta?
  case $1 in */.colima/*/docker.sock) grep -q '^rosetta: true' "$(dirname "$1")/colima.yaml" 2> /dev/null ;; *) return 1 ;; esac
}
sock=${DOCKER_HOST#unix://}
[ -n "${DOCKER_HOST:-}" ] || sock=$(docker context inspect --format '{{.Endpoints.docker.Host}}' 2> /dev/null)
sock=${sock#unix://}
[ -L "$sock" ] && sock=$(python3 -c 'import os,sys;print(os.path.realpath(sys.argv[1]))' "$sock")
if rosetta_sock "$sock"; then echo "unix://$sock"; exit 0; fi
# the login home, not $HOME: a run with its own HOME (the cold test) still uses the machine's colima
for home in "$HOME" "$(python3 -c 'import os,pwd;print(pwd.getpwuid(os.getuid()).pw_dir)')"; do
  for y in "$home"/.colima/*/colima.yaml; do
    s=$(dirname "$y")/docker.sock
    [ -S "$s" ] && rosetta_sock "$s" && { echo "unix://$s"; exit 0; }
  done
done
# GF-6: Docker Desktop is accepted when its amd64 containers run through Rosetta, which is what the colima check stands for.
# Rosetta shows as /proc/sys/fs/binfmt_misc/rosetta and as a "VirtualApple" cpu in /proc/cpuinfo; qemu shows neither. The probe runs in
# an image already there (setup's own, else any amd64 one that is); on a fresh Mac there is none (setup calls this at step 3, before
# step 4 pulls), so a small amd64 image is pulled for it. Every docker call here is time-bounded: amd64 under qemu may hang, and a
# probe that hangs is a refusal, not a stuck setup. The answer is the current Docker.
BOUNDED=$(dirname "$0")/bounded.sh   # KILL after the bound (a TERM-only stop leaves an attached `docker run` of a container that ignores TERM running)
probe_img=; probe_note=
# only an image that reports amd64 is a Rosetta probe: an arm64 postgres:16 runs natively and proves nothing
# (a hung Docker Desktop must not hang the pipeline start: the inspect and the rm are bounded too)
for i in eclipse-temurin:21-jdk postgres:16 eclipse-temurin:11-jdk; do
  [ "$(bash "$BOUNDED" "${UPG_PROBE_INSPECT_TIMEOUT:-15}" docker image inspect -f '{{.Architecture}}' "$i" 2> /dev/null)" = amd64 ] && { probe_img=$i; break; }
done
if [ -z "$probe_img" ]; then
  for m in "" mirror.gcr.io/library/; do   # Docker Hub answers 429 from a shared egress IP: the mirror is the second try
    bash "$BOUNDED" "${UPG_PROBE_PULL_TIMEOUT:-90}" docker pull --platform linux/amd64 -q "${m}alpine:3" > /dev/null 2>&1 && { probe_img=${m}alpine:3; break; }
  done
  [ -n "$probe_img" ] || probe_note="dockerhost: no amd64 image to probe with, and alpine:3 could not be pulled (network?): Rosetta could not be checked."
fi
probe_name=upg-rosetta-probe-$$-$RANDOM; probe_ok=
if [ -n "$probe_img" ]; then   # a named container, so a failed or timed-out probe (bounded.sh maps a KILLed probe to 124) can remove it: killing the docker CLI does not stop the container
  rc=0; bash "$BOUNDED" "${UPG_PROBE_TIMEOUT:-60}" docker run --rm --name "$probe_name" --platform linux/amd64 --entrypoint sh "$probe_img" -c 'test -e /proc/sys/fs/binfmt_misc/rosetta || grep -q VirtualApple /proc/cpuinfo' > /dev/null 2>&1 || rc=$?
  [ "$rc" -ne 0 ] || probe_ok=1
  [ "$rc" -eq 0 ] || bash "$BOUNDED" "${UPG_PROBE_INSPECT_TIMEOUT:-15}" docker rm -f "$probe_name" > /dev/null 2>&1 || true
fi
if [ -n "$probe_ok" ]; then
  echo "${DOCKER_HOST:-}"; exit 0
fi
prev=$(docker context show 2> /dev/null || echo default)
{
  echo "dockerhost: no running container VM with Rosetta (current: ${sock:-none}). The amd64 mxcli crashes under qemu."
  [ -z "$probe_note" ] || echo "$probe_note"
  echo "Two ways out:"
  echo "  1. Docker Desktop: Settings > General > tick \"Use Rosetta for x86_64/amd64 emulation on Apple Silicon\" (needs the Apple Virtualization framework), restart it, rerun."
  echo "  2. A colima VM of its own (about 6 cpu, 12 GB memory, 60 GB disk: mxbuild and the runtime of two versions, Postgres):"
  echo "       colima start -p upgrade --vm-type vz --vz-rosetta --cpu 6 --memory 12 --disk 60"
  echo "       docker context use $prev      # colima start switches the machine's docker context to colima-upgrade; put it back"
  echo "       export DOCKER_HOST=unix://\$HOME/.colima/upgrade/docker.sock     # the pipeline only needs this variable, in this shell"
} >&2
exit 1
