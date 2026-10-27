#!/usr/bin/env bash
# CI(.github/workflows/validate.yml)와 동등한 구조 검사를 로컬에서 실행한다 — VERIFY.md V-2의 구동 수단.
# 사용: bash scripts/validate-local.sh [--no-living]   (--no-living: 릴리스 커밋 전, living-doc 드리프트 가드 생략)
set -uo pipefail
cd "$(dirname "$0")/.."
fail=0; ok() { echo "OK: $*"; }; err() { echo "FAIL: $*"; fail=1; }
S=skills/Quetzalcoatl/SKILL.md; T=skills/Quetzalcoatl/TEMPLATES.md

PLUGIN=$(jq -r '.version' .claude-plugin/plugin.json); MARKET=$(jq -r '.plugins[0].version' .claude-plugin/marketplace.json)
SKILL=$(grep -E '^version:' $S | head -1 | sed -E 's/version:[[:space:]]*//')
[ "$PLUGIN" = "$MARKET" ] && [ "$PLUGIN" = "$SKILL" ] && ok "3중 버전 = $PLUGIN" || err "버전 불일치 plugin=$PLUGIN market=$MARKET skill=$SKILL"
jq empty .claude-plugin/plugin.json .claude-plugin/marketplace.json 2>/dev/null && ok "JSON 유효" || err "JSON 무효"

nums=$(awk '/^```/ { infence = !infence; next } !infence && /^## [0-9]+\./ { match($0, /[0-9]+/); print substr($0, RSTART, RLENGTH) }' $S | tr "\n" " ")
expected=0; cont=1; for n in $nums; do [ "$n" -ne "$expected" ] && cont=0; expected=$((expected + 1)); done
[ "$cont" -eq 1 ] && ok "섹션 연속 ($nums)" || err "섹션 불연속: $nums"

refs=$(grep -oE '부록 C-[0-9]+' $S | grep -oE '[0-9]+' | sort -un); anchors=$(grep -oE '^#### C-[0-9]+\.' $T | grep -oE '[0-9]+' | sort -un)
dups=$(grep -oE '^#### C-[0-9]+\.' $T | sort | uniq -d); [ -z "$dups" ] && ok "중복 앵커 0" || err "중복 앵커: $dups"
idx=$(grep -cE '^\| C-[0-9]+ ' $S); n_anchor=$(grep -cE '^#### C-[0-9]+\.' $T)
[ "$idx" -eq "$n_anchor" ] && ok "§22 색인 $idx행 = 앵커 $n_anchor" || err "색인 $idx ≠ 앵커 $n_anchor"
expected=1; contig=1; for a in $anchors; do [ "$a" -ne "$expected" ] && contig=0; expected=$((expected + 1)); done
[ "$contig" -eq 1 ] && ok "앵커 연속 C-1..C-$((expected - 1))" || err "앵커 불연속"
missing=""; for r in $refs; do echo "$anchors" | grep -qx "$r" || missing="$missing C-$r"; done
[ -z "$missing" ] && ok "포인터 ⊆ 앵커 ($(echo $refs | wc -w)개)" || err "앵커 없는 참조:$missing"

n=$(awk '/^---$/{c++; next} c==1{print}' $S | wc -m); [ "$n" -le 1024 ] && ok "frontmatter ${n}자 ≤ 1024" || err "frontmatter ${n}자 > 1024"
python3 -I - <<'PY' && ok "frontmatter YAML 유효" || err "frontmatter YAML 무효"
import yaml
txt = open('skills/Quetzalcoatl/SKILL.md', encoding='utf-8').read()
d = yaml.safe_load(txt.split('---\n')[1]); assert isinstance(d, dict)
for k in ('name', 'description', 'version'): assert d.get(k), k
PY

tmp=$(mktemp); bash scripts/build-paste-bundle.sh "$tmp" >/dev/null; diff -q "$tmp" dist/Quetzalcoatl-FULL.md >/dev/null && ok "번들 신선도 (dist = SKILL+TEMPLATES)" || err "번들 stale — scripts/build-paste-bundle.sh 재실행"; rm -f "$tmp"

if [ "${1:-}" != "--no-living" ]; then
  SSOT=$PLUGIN
  RUNBOOK=$(grep -oE '현재: v[0-9]+\.[0-9]+\.[0-9]+' docs/05-ops/RUNBOOK.md | head -1 | grep -oE '[0-9]+\.[0-9]+\.[0-9]+' || true)
  DASH=$(grep -oE 'Quetzalcoatl v[0-9]+\.[0-9]+\.[0-9]+' docs/00-overview/DASHBOARD.md | head -1 | grep -oE '[0-9]+\.[0-9]+\.[0-9]+' || true)
  MIRROR=$(grep -oE 'Quetzalcoatl[^0-9]+[0-9]+\.[0-9]+\.[0-9]+ Dashboard' docs/assets/dashboard.html | head -1 | grep -oE '[0-9]+\.[0-9]+\.[0-9]+' || true)
  for pair in "RUNBOOK:$RUNBOOK" "DASHBOARD:$DASH" "mirror:$MIRROR"; do
    name=${pair%%:*}; v=${pair#*:}
    [ "$v" = "$SSOT" ] && ok "living-doc $name = v$v" || err "living-doc $name = v${v:-없음} (SSOT v$SSOT)"
  done
fi
[ "$fail" -eq 0 ] && echo "ALL OK" || { echo "SOME CHECKS FAILED"; exit 1; }
