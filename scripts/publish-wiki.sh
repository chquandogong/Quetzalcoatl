#!/usr/bin/env bash
# wiki/ (저장소 안 정본·파생 뷰) → GitHub Wiki(<repo>.wiki.git) 발행.
# 사용: bash scripts/publish-wiki.sh [--dry-run]
# 전제: GitHub 위키 저장소가 존재해야 한다 — 위키가 비어 있으면 GitHub 웹에서 첫 페이지를 한 번 만들어야
#       .wiki.git 이 생성된다(그 전에는 push가 "Repository not found"로 거부됨). 생성 페이지는 먼저 빌드한다.
set -euo pipefail
cd "$(dirname "$0")/.."
REMOTE="${WIKI_REMOTE:-https://github.com/chquandogong/Quetzalcoatl.wiki.git}"
WORK="${WIKI_WORKDIR:-$(mktemp -d)}"
python3 -I scripts/build-wiki.py >/dev/null
python3 -I scripts/build-wiki.py --check >/dev/null || { echo "wiki 생성 페이지가 stale — 먼저 커밋하라" >&2; exit 1; }
if ! git ls-remote --exit-code "$REMOTE" >/dev/null 2>&1; then
  echo "위키 저장소가 아직 없다: $REMOTE" >&2
  echo "→ https://github.com/chquandogong/Quetzalcoatl/wiki 에서 'Create the first page'로 아무 내용이나 저장한 뒤 다시 실행." >&2
  exit 2
fi
git clone -q "$REMOTE" "$WORK/wiki"
cp wiki/*.md "$WORK/wiki/"
cd "$WORK/wiki"
git add -A
if git diff --cached --quiet; then echo "변경 없음 — 위키가 이미 최신"; exit 0; fi
SRC=$(git -C "$OLDPWD" rev-parse --short HEAD)
git -c user.name="${GIT_AUTHOR_NAME:-CHENGHAO QUAN}" -c user.email="${GIT_AUTHOR_EMAIL:-chquan@dogu.xyz}" commit -q -m "wiki: sync from repo wiki/ @ $SRC"
if [ "${1:-}" = "--dry-run" ]; then git --no-pager show --stat HEAD | tail -n +1; echo "(dry-run: push 생략)"; exit 0; fi
git push -q origin HEAD:master 2>/dev/null || git push -q origin HEAD:main
echo "published: $(git rev-parse --short HEAD) → $REMOTE ($(ls *.md | wc -l) pages)"
