#!/usr/bin/env bash
# apptree.sh <app dir>: exit 0 when the app dir is a working git tree, else 1 with a message that names the dir, quotes the git error
# and gives the likely cause (GM-10: app/ was a git worktree of a deleted clone, every git call failed and nothing said why).
# Callers choose their own exit code; they run it at the START OF EVERY STEP, not once per run, because the clone can vanish between steps.
# Producers of the call (mandatory chain): bin/stepupdate.sh (run start and each module step), bin/cloud/upgrade-pipeline.sh run_step.
[ $# -eq 1 ] || { echo "usage: apptree.sh <app dir>" >&2; exit 2; }
app=$1
err=$(git -C "$app" rev-parse --is-inside-work-tree 2>&1) && [ "$err" = true ] && exit 0
[ -d "$app" ] || err="no such directory"
{
  echo "$(basename "$0"): $app is not a working git tree."
  echo "  git said: $(printf '%s' "$err" | head -3 | tr '\n' ' ')"
  echo "  Likely cause: a worktree whose main clone was deleted or moved? Run \`git worktree prune\` in the main clone, or re-clone app/."
} >&2
exit 1
