# 설치

세 경로가 있다. 어느 경로든 **`SKILL.md`(규칙)와 `TEMPLATES.md`(양식)는 한 세트**다.

## 1) Claude Code 플러그인 (권장)

```text
/plugin marketplace add chquandogong/Quetzalcoatl
/plugin install quetzalcoatl@quetzalcoatl
```

새 세션에서 플러그인 네임스페이스로 호출한다.

```text
/quetzalcoatl:Quetzalcoatl 아래 아이디어를 의미 검토부터 배포까지 운영해줘. [아이디어]
```

- 플러그인 캐시(`~/.claude/plugins/cache/quetzalcoatl/quetzalcoatl/<버전>/`)는 **버전별 사본**이다. GitHub에 새 버전이 올라가도 자동 반영되지 않는다.
- 최신으로 올리기: `/plugin marketplace update quetzalcoatl` → `/plugin install quetzalcoatl@quetzalcoatl`(또는 `claude plugin update quetzalcoatl@quetzalcoatl`) → **세션 재시작**.
- 마켓플레이스 클론이 오래되면 재설치가 구버전을 다시 깔 수 있다. 증상은 캐시에 새 버전 디렉터리가 안 생기는 것이고, 조치는 `git -C ~/.claude/plugins/marketplaces/quetzalcoatl merge --ff-only origin/main` 뒤 업데이트 재실행이다.

## 2) 개인 스킬 (Claude Code · Codex CLI)

```bash
git clone https://github.com/chquandogong/Quetzalcoatl /tmp/quetzalcoatl-src
cp -r /tmp/quetzalcoatl-src/skills/Quetzalcoatl ~/.claude/skills/Quetzalcoatl   # Claude Code
cp -r /tmp/quetzalcoatl-src/skills/Quetzalcoatl ~/.codex/skills/Quetzalcoatl    # Codex CLI (별도 경로)
```

네임스페이스 없이 `/Quetzalcoatl`로 호출된다(새 세션 필요). 폴더째 복사해야 `TEMPLATES.md`가 함께 간다.

## 3) 도구 없는 챗 환경 (ChatGPT · GPTs · 일반 LLM)

본문과 양식을 합친 **페이스트 번들** [`dist/Quetzalcoatl-FULL.md`](https://github.com/chquandogong/Quetzalcoatl/blob/main/dist/Quetzalcoatl-FULL.md)를 쓴다.

1. ChatGPT 프로젝트 지침 또는 GPT Builder의 Instructions에 번들 내용을 붙여넣는다.
2. 일반 채팅에서는 번들 전체를 첫 메시지나 프로젝트 설명으로 붙여넣는다.
3. 스킬 업로드를 지원하는 환경에서는 `SKILL.md` + `TEMPLATES.md` 폴더를 zip으로 올린다.

번들은 `scripts/build-paste-bundle.sh`가 만들고 CI가 소스와의 일치(신선도)를 검사한다.

## 설치 확인

- 플러그인: 캐시 디렉터리에 `SKILL.md` · `TEMPLATES.md` · `USAGE.md`가 있고 `SKILL.md`의 `version:`이 설치하려던 버전인지 본다.
- 첫 호출에서 첫 응답 미니 템플릿(목표 · 핵심 질문 · 전제 · 대안 · 첫 단계)이 나오면 켜진 것이다 — [빠른 시작](Quick-Start).

## 요구사항

마크다운 스킬이라 실행 코드·네트워크·비밀값이 없다. 교차검증을 **실제로** 하려면 다른 모델을 호출할 수단(예: 로컬 Codex CLI)이 따로 있어야 하고, 없으면 스킬이 "실제 교차검증 아님"으로 강등해 표시한다 — [교차검증](Cross-Validation).
