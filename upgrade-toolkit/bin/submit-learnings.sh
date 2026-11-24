#!/usr/bin/env bash
# submit-learnings.sh: send the drafts in an inbox back as one branch and one PR, after a leak check.
# Usage: submit-learnings.sh toolkit|brain [--inbox DIR] [--repo DIR] [--dry-run] [--no-pr]
#   toolkit  <toolkit>/contrib/inbox/*.md         -> the public toolkit repo (GitHub PR via gh)
#   brain    ${UPG_BRAIN}/inbox/*.md              -> your private brain repo (GitHub PR via gh, GitLab MR via push options)
#            With no private brain (UPG_BRAIN unset, a folder with no git remote, or the brain this repo ships) the
#            notes go to the public toolkit's contrib/inbox like a toolkit draft: one central intake for everyone.
# --inbox may be a plain folder outside any git repo (a run's learnings/ folder): its drafts are copied into the target
# repo's contrib/inbox on the PR branch. --repo DIR names the git checkout of the toolkit to send from (default: this one).
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
# leave the inbox. A failed push to the public toolkit (no write access) forks it with `gh repo fork --remote` and opens the
# PR from the fork against the public main; without a usable gh it prints the exact manual steps and keeps the branch.
# --dry-run runs the checks and prints the plan, no git writes. --no-pr pushes the branch without opening a PR.
# Exit 0 submitted, dry run passed or nothing to submit, 1 a check refused, 2 bad call, 3 git or push failed.
set -u
B=$(cd "$(dirname "$0")" && pwd); TK=$(dirname "$B")
PUBLIC_SLUG=MendixMau/mendix-upgrade-toolkit
MODE=${1:-}; shift || true
case $MODE in toolkit|brain) ;; *) echo "usage: submit-learnings.sh toolkit|brain [--inbox DIR] [--repo DIR] [--dry-run] [--no-pr]" >&2; exit 2;; esac
INBOX=""; DRY=0; PR=1; TKR_ARG=""
slug_of() { sed -E 's#.*github\.com[:/]##; s#\.git$##' <<< "$1"; }
while [ $# -gt 0 ]; do
  case $1 in
    --inbox) INBOX=${2:-}; shift 2;;
    --dry-run) DRY=1; shift;;
    --no-pr) PR=0; shift;;
    --repo) TKR_ARG=${2:-}; shift 2;;
    *) echo "submit-learnings: unknown option $1" >&2; exit 2;;
  esac
done
# The public toolkit checkout the drafts go to (default: the one this script lives in).
TKROOT=$(git -C "${TKR_ARG:-$TK}" rev-parse --show-toplevel 2>/dev/null || true)
if [ -n "$TKROOT" ]; then
  if [ -d "$TKROOT/upgrade-toolkit/contrib" ]; then TKINBOX_REL=upgrade-toolkit/contrib/inbox
  elif [ -n "$TKR_ARG" ]; then TKINBOX_REL=contrib/inbox
  else TKINBOX_REL=$(cd "$TK" && pwd -P); TKINBOX_REL=${TKINBOX_REL#"$(cd "$TKROOT" && pwd -P)"/}/contrib/inbox; fi
fi
# Where does it go? toolkit: always the public repo. brain: your private brain when it is a git repo with a remote that
# is not this toolkit's, else the public repo too (a user with no private brain still has somewhere to send a note).
PUBLIC=1; BREPO=""
if [ "$MODE" = brain ] && [ -n "${UPG_BRAIN:-}" ]; then
  BREPO=$(git -C "$UPG_BRAIN" rev-parse --show-toplevel 2>/dev/null || true)
  TKSELF=$(git -C "$TK" rev-parse --show-toplevel 2>/dev/null || true)
  if [ -n "$BREPO" ] && [ "$BREPO" != "$TKROOT" ] && [ "$BREPO" != "$TKSELF" ] && [ -n "$(git -C "$BREPO" remote)" ]; then PUBLIC=0; fi
fi
if [ -z "$INBOX" ]; then
  if [ "$MODE" = toolkit ] || [ $PUBLIC = 1 ]; then
    [ -n "$TKROOT" ] || { echo "submit-learnings: the toolkit at $TK is not a git checkout. Clone https://github.com/$PUBLIC_SLUG or open an issue and paste the drafts." >&2; exit 2; }
    INBOX=$TKROOT/$TKINBOX_REL
    [ "$MODE" = brain ] && echo "submit-learnings: no private brain repo with a remote: sending these brain-format notes to the public toolkit inbox (https://github.com/$PUBLIC_SLUG)"
  else INBOX=$UPG_BRAIN/inbox; fi
fi
[ -d "$INBOX" ] || { echo "submit-learnings: no inbox at $INBOX" >&2; exit 2; }
INBOX=$(cd "$INBOX" && pwd)
REPO=$(git -C "$INBOX" rev-parse --show-toplevel 2>/dev/null || true)
LOOSE=0
if [ -z "$REPO" ]; then   # a plain folder (a run's learnings/): copy its drafts into the target repo
  LOOSE=1
  if [ $PUBLIC = 1 ]; then REPO=$TKROOT; DESTREL=$TKINBOX_REL; else REPO=$BREPO; DESTREL=${UPG_BRAIN#"$BREPO"}/inbox; DESTREL=${DESTREL#/}; fi
  [ -n "$REPO" ] || { echo "submit-learnings: $INBOX is not in a git repo and the toolkit is no git checkout either; open an issue at https://github.com/$PUBLIC_SLUG/issues/new and paste the drafts" >&2; exit 2; }
else
  REL=${INBOX#"$REPO"}; REL=${REL#/}; IREL=$REL; DESTREL=$REL
  # a public-route inbox that is not a contrib/inbox (the shipped brain's inbox): land in the toolkit's contrib/inbox
  if [ $PUBLIC = 1 ] && [ "$MODE" = brain ] && [ -n "$TKROOT" ] && [ "$REPO" = "$TKROOT" ] && [ "$REL" != "$TKINBOX_REL" ]; then DESTREL=$TKINBOX_REL; fi
fi
REL=${DESTREL:-}

if [ "$MODE" = brain ] && [ $PUBLIC = 0 ]; then
  [ "$REPO" = "$TKROOT" ] && { echo "REFUSED: the brain inbox $INBOX is inside the toolkit repo; brain drafts go to the brain" >&2; exit 1; }
fi

if [ $LOOSE = 1 ]; then
  names=$(find "$INBOX" -maxdepth 1 -type f -name '*.md' ! -name README.md ! -name TEMPLATE.md -exec basename {} \; | sort)
else
  names=$(git -C "$REPO" status --porcelain --untracked-files=all -- "$INBOX" | sed 's/^...//' | grep -E '\.md$' | grep -vE '(^|/)(README|TEMPLATE)\.md$' | sed "s|^$IREL/||" || true)
fi
[ -n "$names" ] || { echo "submit-learnings: nothing to submit in $INBOX"; exit 0; }
files=$(echo "$names" | sed "s|^|$REL/|")
SRC() { echo "$INBOX/${1#"$REL"/}"; }   # the file in the inbox for a path under $REL

source "$B/private_names.sh"
hits=""
for f in $files; do
  p=$(SRC "$f")
  [ -n "$DENY" ] && h=$(grep -nIHE "$DENY" -- "$p" | sed "s|^$INBOX/|$REL/|" | sed 's/$/  (denylisted name)/') && hits="$hits$h"$'\n'
  h=$(grep -nIHE 'ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|glpat-[A-Za-z0-9_-]{10,}|AKIA[0-9A-Z]{16}|BEGIN (RSA|OPENSSH|EC |DSA |)PRIVATE KEY' -- "$p" | sed "s|^$INBOX/|$REL/|" | sed 's/$/  (credential)/') && hits="$hits$h"$'\n'
  h=$(grep -nIHE '/(Users|home)/[A-Za-z0-9._-]+' -- "$p" | grep -vE '/(Users|home)/<user>' | sed "s|^$INBOX/|$REL/|" | sed 's/$/  (home folder path)/') && hits="$hits$h"$'\n'
  if [ $PUBLIC = 1 ]; then
    h=$(grep -nIHE '^confidentiality: *internal' -- "$p" | sed "s|^$INBOX/|$REL/|" | sed 's/$/  (internal text, belongs in the brain)/') && hits="$hits$h"$'\n'
  fi
done
hits=$(echo "$hits" | grep -v '^$' | cut -c1-220 || true)
if [ -n "$hits" ]; then echo "$hits"; echo "REFUSED: fix or remove the lines above, then submit again. Nothing pushed." >&2; exit 1; fi
[ -n "$DENY" ] || echo "submit-learnings: no private list (set UPG_PRIVATE_NAMES); names not checked"

REMOTE=$(git -C "$REPO" remote | grep -x origin || git -C "$REPO" remote | head -1)
[ -n "$REMOTE" ] || { echo "submit-learnings: $REPO has no remote" >&2; exit 3; }
URL=$(git -C "$REPO" config --get "remote.$REMOTE.url" || git -C "$REPO" remote get-url "$REMOTE")
DEF=$(git -C "$REPO" symbolic-ref --short "refs/remotes/$REMOTE/HEAD" 2>/dev/null | sed "s|^$REMOTE/||")
[ -n "$DEF" ] || DEF=main
first=$(basename "$(echo "$files" | head -1)" .md)
BR="learnings/$(date +%Y-%m-%d)-$(echo "$first" | sed 's/^[0-9-]*//' | tr -c 'A-Za-z0-9_.-' '-' | sed 's/-*$//' | cut -c1-40)"
BR0=$BR; i=2; while git -C "$REPO" rev-parse -q --verify "refs/heads/$BR" >/dev/null; do BR="$BR0-$i"; i=$((i + 1)); done   # an earlier failed try keeps its branch
n=$(echo "$files" | wc -l | tr -d ' ')
case $URL in *github.com*) HOST=github;; *gitlab*) HOST=gitlab;; *) HOST=other;; esac
TITLE="learnings: $n draft(s) from $first"
slug=""; [ $HOST = github ] && slug=$(slug_of "$URL")
lc() { printf '%s' "$1" | tr 'A-Z' 'a-z'; }
ISPUBLIC=0; [ $HOST = github ] && [ "$(lc "$slug")" = "$(lc "$PUBLIC_SLUG")" ] && ISPUBLIC=1

echo "submit-learnings: checks clean, $n file(s)"
echo "$files" | sed 's/^/  /'
echo "  repo $REPO, remote $REMOTE ($HOST), branch $BR off $DEF"
if [ $DRY = 1 ]; then echo "dry run: nothing committed or pushed"; exit 0; fi

git -C "$REPO" fetch -q "$REMOTE" "$DEF" || { echo "submit-learnings: fetch of $REMOTE/$DEF failed" >&2; exit 3; }
WT=$(mktemp -d "${TMPDIR:-/tmp}/submit-learnings.XXXXXX"); rmdir "$WT"
cleanup() { git -C "$REPO" worktree remove --force "$WT" >/dev/null 2>&1; }
trap cleanup EXIT
git -C "$REPO" worktree add -q -b "$BR" "$WT" "$REMOTE/$DEF" || { echo "submit-learnings: could not cut $BR" >&2; exit 3; }
for f in $files; do mkdir -p "$WT/$(dirname "$f")"; cp "$(SRC "$f")" "$WT/$f"; done
git -C "$WT" add -- $files
git -C "$WT" commit -q -m "$TITLE" -m "Submitted with bin/submit-learnings.sh $MODE from $REL/. Drafts: review, promote into steps/, playbooks/, BACKLOG.md or bin/, then delete them from the inbox." || { echo "submit-learnings: commit failed" >&2; exit 3; }
PUSHOPT=()
[ $HOST = gitlab ] && [ $PR = 1 ] && PUSHOPT=(-o merge_request.create -o "merge_request.target=$DEF" -o "merge_request.title=$TITLE")
PRREPO=$slug; HEAD=$BR
if ! git -C "$WT" push -q ${PUSHOPT[@]+"${PUSHOPT[@]}"} "$REMOTE" "$BR"; then
  if [ $ISPUBLIC = 1 ]; then
    # no write access to the public toolkit: send it from the contributor's own fork (central intake stays one place)
    if command -v gh >/dev/null 2>&1 && gh auth status >/dev/null 2>&1; then
      git -C "$REPO" remote | grep -qx fork || (cd "$REPO" && gh repo fork "$PUBLIC_SLUG" --remote --remote-name fork) >&2 || true
      FURL=$(git -C "$REPO" config --get remote.fork.url || true)
      if [ -n "$FURL" ] && { git -C "$WT" push -q fork "$BR" || { sleep 3; git -C "$WT" push -q fork "$BR"; }; }; then
        PRREPO=$PUBLIC_SLUG; HEAD="$(slug_of "$FURL" | cut -d/ -f1):$BR"
        echo "submit-learnings: no write access to $PUBLIC_SLUG: pushed to your fork instead ($(slug_of "$FURL"))"
      else FORKFAIL=1; fi
    else FORKFAIL=1; fi
    if [ "${FORKFAIL:-0}" = 1 ]; then
      echo "submit-learnings: no write access to $PUBLIC_SLUG, and the GitHub CLI (gh) is missing, not signed in, or the fork failed. Send it from a fork by hand:" >&2
      echo "  1. Open https://github.com/$PUBLIC_SLUG and press Fork." >&2
      echo "  2. git -C $REPO remote add fork https://github.com/<your-user>/$(basename "$PUBLIC_SLUG").git" >&2
      echo "  3. git -C $REPO push fork $BR      (the commit is kept on that branch)" >&2
      echo "  4. Open https://github.com/<your-user>/$(basename "$PUBLIC_SLUG")/pull/new/$BR and set the base to $PUBLIC_SLUG $DEF." >&2
      echo "  No git? Open https://github.com/$PUBLIC_SLUG/issues/new and paste each file after you have read it for names." >&2
      exit 3
    fi
  else
    git -C "$REPO" branch -D "$BR" >/dev/null 2>&1
    echo "submit-learnings: push to $REMOTE failed. No write access? Fork the repo, then:" >&2
    echo "  git remote add fork <your fork url> && bin/submit-learnings.sh $MODE  (with the fork as origin), or open a PR from the fork by hand" >&2
    exit 3
  fi
elif [ $ISPUBLIC = 0 ] && [ $PUBLIC = 1 ] && [ $HOST = github ]; then
  # origin is the contributor's own fork of the public toolkit: the PR still goes to the public repo
  PRREPO=$PUBLIC_SLUG; HEAD="$(echo "$slug" | cut -d/ -f1):$BR"
fi
if [ $PR = 1 ] && { [ $HOST = github ] || [ "$PRREPO" = "$PUBLIC_SLUG" ]; }; then
  gh pr create -R "$PRREPO" --head "$HEAD" --base "$DEF" --title "$TITLE" \
    --body "Learnings submitted with \`bin/submit-learnings.sh $MODE\`:"$'\n\n'"$(echo "$files" | sed 's/^/- /')"$'\n\n'"Leak checks run by the script: names list ($([ -n "$DENY" ] && echo yes || echo 'none set: read them by hand')), credentials, home folder paths, internal marker."$'\n\n'"Triage: promote what holds into steps/, playbooks/, BACKLOG.md or bin/ (with a control), then delete the draft." \
    || echo "submit-learnings: branch pushed, PR not opened (gh failed); open it from $BR by hand" >&2
fi
for f in $files; do rm -f "$(SRC "$f")"; done
echo "submitted: $BR ($n file(s) left the inbox)"
