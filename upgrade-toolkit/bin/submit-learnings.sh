#!/usr/bin/env bash
# submit-learnings.sh: send the drafts in an inbox back as one branch and one PR, after a leak check.
# Usage: submit-learnings.sh toolkit|brain [--inbox DIR] [--dry-run] [--no-pr]
#   toolkit  <toolkit>/contrib/inbox/*.md         -> the toolkit repo (GitHub PR via gh)
#   brain    ${UPG_BRAIN}/inbox/*.md              -> the brain repo (GitHub PR via gh, GitLab MR via push options)
# The drafts come from bin/harvest.py or are written by hand (contrib/inbox/TEMPLATE.md). Only new or changed files
# count; README.md and TEMPLATE.md never do.
# Checks, any hit refuses and nothing is pushed:
#   - a name from the private denylist (bin/private_names.sh)
#   - a credential or a private key
#   - a home folder path (/Users/<name>, /home/<name>)
#   - toolkit only: a file marked 'confidentiality: internal' (internal brain text never goes to the toolkit)
#   - brain only: an inbox that sits in the toolkit repo (the brain drafts belong in the brain)
# Then: a branch learnings/<date>-<first file>, cut from the remote's default branch in a temporary worktree, so your
# checkout is not touched; the files are committed there, pushed, and the PR (or MR) is opened. The submitted files
# leave the inbox. A failed push (no write access) prints how to send it from a fork instead.
# --dry-run runs the checks and prints the plan, no git writes. --no-pr pushes the branch without opening a PR.
# Exit 0 submitted, dry run passed or nothing to submit, 1 a check refused, 2 bad call, 3 git or push failed.
set -u
B=$(cd "$(dirname "$0")" && pwd); TK=$(dirname "$B")
MODE=${1:-}; shift || true
case $MODE in toolkit|brain) ;; *) echo "usage: submit-learnings.sh toolkit|brain [--inbox DIR] [--dry-run] [--no-pr]" >&2; exit 2;; esac
INBOX=""; DRY=0; PR=1
while [ $# -gt 0 ]; do
  case $1 in
    --inbox) INBOX=${2:-}; shift 2;;
    --dry-run) DRY=1; shift;;
    --no-pr) PR=0; shift;;
    *) echo "submit-learnings: unknown option $1" >&2; exit 2;;
  esac
done
if [ -z "$INBOX" ]; then
  if [ "$MODE" = toolkit ]; then INBOX=$TK/contrib/inbox
  else [ -n "${UPG_BRAIN:-}" ] || { echo "submit-learnings: set UPG_BRAIN or pass --inbox <brain>/inbox" >&2; exit 2; }; INBOX=$UPG_BRAIN/inbox; fi
fi
[ -d "$INBOX" ] || { echo "submit-learnings: no inbox at $INBOX" >&2; exit 2; }
INBOX=$(cd "$INBOX" && pwd)
REPO=$(git -C "$INBOX" rev-parse --show-toplevel 2>/dev/null) || { echo "submit-learnings: $INBOX is not in a git repo" >&2; exit 2; }
REL=${INBOX#"$REPO"}; REL=${REL#/}

if [ "$MODE" = brain ]; then
  TKREPO=$(git -C "$TK" rev-parse --show-toplevel 2>/dev/null || true)
  [ "$REPO" = "$TKREPO" ] && { echo "REFUSED: the brain inbox $INBOX is inside the toolkit repo; brain drafts go to the brain" >&2; exit 1; }
fi

files=$(git -C "$REPO" status --porcelain --untracked-files=all -- "$INBOX" | sed 's/^...//' | grep -E '\.md$' | grep -vE '(^|/)(README|TEMPLATE)\.md$' || true)
[ -n "$files" ] || { echo "submit-learnings: nothing to submit in $INBOX"; exit 0; }

source "$B/private_names.sh"
hits=""
for f in $files; do
  p=$REPO/$f
  [ -n "$DENY" ] && h=$(grep -nIHE "$DENY" -- "$p" | sed "s|^$REPO/||" | sed 's/$/  (denylisted name)/') && hits="$hits$h"$'\n'
  h=$(grep -nIHE 'ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|glpat-[A-Za-z0-9_-]{10,}|AKIA[0-9A-Z]{16}|BEGIN (RSA|OPENSSH|EC |DSA |)PRIVATE KEY' -- "$p" | sed "s|^$REPO/||" | sed 's/$/  (credential)/') && hits="$hits$h"$'\n'
  h=$(grep -nIHE '/(Users|home)/[A-Za-z0-9._-]+' -- "$p" | grep -vE '/(Users|home)/<user>' | sed "s|^$REPO/||" | sed 's/$/  (home folder path)/') && hits="$hits$h"$'\n'
  if [ "$MODE" = toolkit ]; then
    h=$(grep -nIHE '^confidentiality: *internal' -- "$p" | sed "s|^$REPO/||" | sed 's/$/  (internal text, belongs in the brain)/') && hits="$hits$h"$'\n'
  fi
done
hits=$(echo "$hits" | grep -v '^$' | cut -c1-220 || true)
if [ -n "$hits" ]; then echo "$hits"; echo "REFUSED: fix or remove the lines above, then submit again. Nothing pushed." >&2; exit 1; fi
[ -n "$DENY" ] || echo "submit-learnings: no private list (set UPG_PRIVATE_NAMES); names not checked"

REMOTE=$(git -C "$REPO" remote | grep -x origin || git -C "$REPO" remote | head -1)
[ -n "$REMOTE" ] || { echo "submit-learnings: $REPO has no remote" >&2; exit 3; }
URL=$(git -C "$REPO" remote get-url "$REMOTE")
DEF=$(git -C "$REPO" symbolic-ref --short "refs/remotes/$REMOTE/HEAD" 2>/dev/null | sed "s|^$REMOTE/||")
[ -n "$DEF" ] || DEF=main
first=$(basename "$(echo "$files" | head -1)" .md)
BR="learnings/$(date +%Y-%m-%d)-$(echo "$first" | sed 's/^[0-9-]*//' | tr -c 'A-Za-z0-9_.-' '-' | sed 's/-*$//' | cut -c1-40)"
n=$(echo "$files" | wc -l | tr -d ' ')
case $URL in *github.com*) HOST=github;; *gitlab*) HOST=gitlab;; *) HOST=other;; esac
TITLE="learnings: $n draft(s) from $first"

echo "submit-learnings: checks clean, $n file(s)"
echo "$files" | sed 's/^/  /'
echo "  repo $REPO, remote $REMOTE ($HOST), branch $BR off $DEF"
if [ $DRY = 1 ]; then echo "dry run: nothing committed or pushed"; exit 0; fi

git -C "$REPO" fetch -q "$REMOTE" "$DEF" || { echo "submit-learnings: fetch of $REMOTE/$DEF failed" >&2; exit 3; }
WT=$(mktemp -d "${TMPDIR:-/tmp}/submit-learnings.XXXXXX"); rmdir "$WT"
cleanup() { git -C "$REPO" worktree remove --force "$WT" >/dev/null 2>&1; }
trap cleanup EXIT
git -C "$REPO" worktree add -q -b "$BR" "$WT" "$REMOTE/$DEF" || { echo "submit-learnings: could not cut $BR (does it exist already?)" >&2; exit 3; }
for f in $files; do mkdir -p "$WT/$(dirname "$f")"; cp "$REPO/$f" "$WT/$f"; done
git -C "$WT" add -- $files
git -C "$WT" commit -q -m "$TITLE" -m "Submitted with bin/submit-learnings.sh $MODE from $REL/. Drafts: review, promote into steps/, playbooks/, BACKLOG.md or bin/, then delete them from the inbox." || { echo "submit-learnings: commit failed" >&2; exit 3; }
PUSHOPT=()
[ $HOST = gitlab ] && [ $PR = 1 ] && PUSHOPT=(-o merge_request.create -o "merge_request.target=$DEF" -o "merge_request.title=$TITLE")
if ! git -C "$WT" push -q "${PUSHOPT[@]}" "$REMOTE" "$BR"; then
  git -C "$REPO" branch -D "$BR" >/dev/null 2>&1
  echo "submit-learnings: push to $REMOTE failed. No write access? Fork the repo, then:" >&2
  echo "  git remote add fork <your fork url> && bin/submit-learnings.sh $MODE  (with the fork as origin), or open a PR from the fork by hand" >&2
  exit 3
fi
if [ $PR = 1 ] && [ $HOST = github ]; then
  slug=$(echo "$URL" | sed -E 's#.*github.com[:/]##; s#\.git$##')
  gh pr create -R "$slug" --head "$BR" --base "$DEF" --title "$TITLE" \
    --body "Learnings submitted with \`bin/submit-learnings.sh $MODE\`:"$'\n\n'"$(echo "$files" | sed 's/^/- /')"$'\n\n'"Triage: promote what holds into steps/, playbooks/, BACKLOG.md or bin/ (with a control), then delete the draft." \
    || echo "submit-learnings: branch pushed, PR not opened (gh failed); open it from $BR by hand" >&2
fi
for f in $files; do rm -f "$REPO/$f"; done
echo "submitted: $BR ($n file(s) left the inbox)"
