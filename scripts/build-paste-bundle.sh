#!/usr/bin/env bash
# SKILL.md(규칙) + TEMPLATES.md(양식) → 페이스트 번들 (도구 없는 챗 환경용 합본).
# 사용: scripts/build-paste-bundle.sh [출력경로]   기본: dist/Quetzalcoatl-FULL.md
set -euo pipefail
cd "$(dirname "$0")/.."
OUT="${1:-dist/Quetzalcoatl-FULL.md}"
mkdir -p "$(dirname "$OUT")"
{
  cat skills/Quetzalcoatl/SKILL.md
  printf '\n---\n\n'
  cat skills/Quetzalcoatl/TEMPLATES.md
} > "$OUT"
echo "built $OUT ($(wc -l < "$OUT") lines)"
