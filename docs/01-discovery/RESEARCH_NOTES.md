# RESEARCH NOTES — 외부 에이전트 도구 진화 (2026 상반기)

> 상태: **스냅샷(동결, §12)** · 날짜: 2026-06-29 · 소유자: Researcher · 승인: CHENGHAO QUAN
> 조사: Claude(Quetzalcoatl) 병렬 3에이전트 · 출처: 공식 changelog/docs 우선
> ⚠️ 도구는 빠르게 바뀐다. 이 문서는 **as-of 2026-06-29 스냅샷**이며 갱신은 새 조사로 한다(이 파일은 동결).
> 신뢰도: Claude Code **85** / OpenAI Codex **72** / Google Antigravity **72**.

이 문서는 SKILL v1.5.0 사이클의 근거 기록이다(§4.2#2 — N개 조사는 근거·출처를 남긴다). 본문(SKILL.md) 반영 여부와 위치 판단은 [CAPABILITY_MATRIX](../appendix/CAPABILITY_MATRIX.md)·[DECISION_LOG D12](../02-decisions/DECISION_LOG.md)·[CROSS_VALIDATION_LOG v1.5.0](../02-decisions/CROSS_VALIDATION_LOG.md) 참조.

## 목적

Claude Code · OpenAI Codex · Google Antigravity의 **컷오프(2026-01) 이후** 변화를 6영역에서 조사: 메모리 · 완료/검증 체크리스트 · 훅 · 서브에이전트 · plan/spec 모드 · 자율 루프. "추측 금지(§15)"라 실제 조사로 확인.

## 가장 큰 발견 — 3도구 독립 수렴

세 도구가 독립적으로 **같은 소수 패턴**으로 수렴했다. 도구별 특이사항이 아니라 **업계 수렴 패턴**이라는 신호 → 모델 중립 본문에 넣을 자격이 있는 후보(단, **수렴≠진실 §1.4** — 본문 반영은 패턴 자체 근거로).

| 패턴                             | Claude Code                                               | OpenAI Codex                                                                | Google Antigravity                                       |
| -------------------------------- | --------------------------------------------------------- | --------------------------------------------------------------------------- | -------------------------------------------------------- |
| 라이프사이클 훅                  | Stop·SubagentStop·PreToolUse·SessionStart…                | SessionStart·PreToolUse·**PermissionRequest**·Stop·SubagentStop·PreCompact… | PreToolUse·PostToolUse·PreInvocation·PostInvocation·Stop |
| 행동 전 승인 게이트(훅)          | (auto mode 분류기)                                        | `PreToolUse`/`PermissionRequest`                                            | **`PreToolUse` decision: allow/deny/ask/force_ask**      |
| 안전 자동승인 / 위험 차단        | **Auto mode 분류기**(안전 승인·위험 차단·파괴적 git 차단) | **auto-review**(별도 LLM-judge, 역할분리 명시)                              | Deny>Ask>Allow 권한엔진(rm -rf/sudo/.git deny)           |
| 범위 한정 자율                   | auto mode + allowlist                                     | `--full-auto` **폐기**→permission profiles                                  | read-only/workspace/danger profiles                      |
| 목표지향 자율 루프               | /goal · /loop self-pacing                                 | **/goal**(GA, 수시간~수일, pausable, self-verify)                           | **/goal** · Stop훅 `continue` · Sidecars+cron            |
| 루프 지속(중단→계속) 훅          | Stop훅 `additionalContext` 반환                           | Stop/SubagentStop 훅                                                        | **Stop훅 `decision:"continue"`**                         |
| 2계층 메모리                     | MEMORY.md(자동) + CLAUDE.md(권위)                         | **Memories(생성·opt-in) + AGENTS.md(권위·체크인)**                          | Rules/Skills(durable) + (네이티브 메모리 퇴행)           |
| config 정의 서브에이전트         | Agent(name/model), 중첩 5단계, worktree 격리              | `.codex/agents/*.toml`(per-agent model/sandbox)                             | `define_subagent`(prompt/scope), 중첩 10                 |
| 권한 버블링(부모 범위 초과 불가) | 백그라운드 프롬프트 메인 노출                             | (sandbox 상속)                                                              | **명시적 버블링 — Ask가 부모 UI로 상승**                 |
| 컨텍스트 자동 압축               | (compaction reminders)                                    | resume + auto-compaction(PreCompact/PostCompact 훅)                         | Managed Agents ~135k 자동 compaction                     |
| durable 마크다운 상태            | (workflow scripts·메모리)                                 | **Plan.md/Documentation.md**(스펙동결·결정감사)                             | Implementation Plan·Walkthrough artifacts                |
| plan-before-exec                 | plan mode / Dynamic Workflows                             | **/plan**("안 할 것"+검증 내장)                                             | **Planning Mode** + 인라인 코멘트 조향                   |
| clarify-before-build             | (plan mode 질의)                                          | (/plan)                                                                     | **/grill-me**                                            |
| 검증 = 증거                      | /code-review·/ultrareview                                 | /review(읽기전용) · in-app 브라우저 시각검증                                | **Artifacts: 스샷·브라우저 녹화 = proof-of-work**        |
| 교차 도구/기기 핸드오프          | background sessions·/resume                               | thread handoff + **Claude Code import**                                     | CLI↔2.0 export · 멀티 surface 동기                       |

**함의 요약:** Quetzalcoatl은 위 패턴의 _방법론_(게이트·범위내자율·문서=상태·에이전트역할·교차검증)을 이미 보유. 새로 생긴 건 그걸 **강제할 메커니즘**(훅·분류기·권한 프로파일·버블링). → 스킬의 #1 약점("규율≠보장")을 환경 강제 수단에 **바인딩**할 외부 지렛대.

---

## 1. Claude Code (신뢰도 85 — 공식 changelog 기반)

출처: code.claude.com/docs/en/{changelog, whats-new, memory, hooks, sub-agents, workflows, agent-view} (fetch 2026-06-29) · Anthropic blog(Dynamic Workflows).

- **메모리**: auto memory(MEMORY.md, `~/.claude/projects/<proj>/memory/` 영속; 세션당 ~200줄/25KB) `[2026-01]` · CLAUDE.md `@import`(재귀 4-hop) · path-scoped rules(`.claude/rules/`) · 압축 리마인더(2026-05).
- **완료/검증**: `/goal`(완료 조건까지 실행) `[2026-05]` · `/code-review`(동적, `--comment`/`--fix`) · `/ultrareview`(버그헌팅 에이전트 fleet, preview).
- **훅**: Stop/SubagentStop이 `background_tasks`·`session_crons` 수신 `[2026-01]` · Stop/SubagentStop `additionalContext` 반환(루프백) · SessionStart `reloadSkills` · MessageDisplay 훅.
- **서브에이전트**: 중첩 5단계 `[2026-06]` · worktree 격리 강제 · 백그라운드 서브에이전트 프롬프트 메인 세션 노출(human gate) · `Agent(model:opus)` 파라미터 문법 · Agent Teams.
- **plan/워크플로우**: **Dynamic Workflows**(JS로 수십~수백 에이전트 오케스트레이션·백그라운드·resumable·비용 한정 16동시/1K최대) `[2026-05]` · `/effort ultracode` · `/deep-research` 번들 · 워크플로우 스크립트 저장(`.claude/workflows/`).
- **자율 루프**: `/goal` · **auto mode**(안전 자동승인/위험 차단, 파괴적 git 차단) `[2026-03]` · agent view(`claude agents`) · background sessions in `/resume` · pinned sessions · `/loop` self-pacing.

**Top 5(방법론):** Dynamic Workflows · auto mode 분류기 · /goal+/loop · 중첩 서브에이전트+worktree+권한노출 · agent view+resume.
**미검증:** 전용 "verification-before-completion 훅"(없음 — /goal+Stop context로 근사) · 네이티브 교차모델 검증 워크플로우(없음, fallback chain만) · 레이트리밋/재개 회복력(MCP retry 외).

## 2. OpenAI Codex (신뢰도 72 — 기능 高·정확한 날짜/버전 中低)

출처: developers.openai.com/codex/{memories, hooks, subagents, permissions, concepts/sandboxing/auto-review, config-reference} · alignment.openai.com · OpenAI blog. ⚠️ canonical `openai/codex` CHANGELOG/releases 로드 실패 → CLI semver↔기능 매핑은 docs/2차 출처.

- **메모리(2계층)**: **AGENTS.md(권위·체크인) vs Memories(생성·opt-in, `~/.codex/memories/`, idle-time)** `[2026-06-16 GA]`. 공식 문구: "반드시 적용돼야 하는 규칙은 AGENTS.md에; memories는 local recall layer일 뿐." · `.codex/` 팀 config.
- **완료/검증(3면)**: **auto-review**(`approvals_reviewer="auto_review"`, 별도 LLM-judge 승인게이트, 수동대비 ~200× 덜 멈춤, "리뷰어 교체지 권한 부여 아님") `[2026-04-30]` · **/review**(읽기전용 diff 리뷰어) · **Goal-mode "done-when"**(plan→edit→test→observe→repair→docs 루프, 마일스톤마다 self-audit) · in-app 브라우저 시각검증 `[2026-04]`.
- **훅**: 라이프사이클 훅 GA `[~2026-05]` — SessionStart·UserPromptSubmit·PreToolUse·PostToolUse·**PermissionRequest**·SubagentStart·SubagentStop·PreCompact·PostCompact·Stop. trust 모델(managed 자동신뢰). `notify`는 별개(현재 agent-turn-complete만).
- **서브에이전트**: 런칭 `[2026-03-17]`, config 정의(`~/.codex/agents/*.toml`, per-agent model/sandbox/skills) · `max_threads=6`/`max_depth=1` · **cross-host thread handoff + Claude Code import** `[2026-06]` · 경량 모델을 서브에이전트에 라우팅(비용).
- **plan/spec**: **/plan**("무엇을 안 할지"+검증 내장) `[2026-04-17]` · **`--full-auto` 폐기→permission profiles**(`:read-only`/`:workspace`/`:danger-full-access`), `exec` 읽기전용 기본 `[2026-04-30]` · spec 모드는 **미출시**("탐색 중").
- **자율 루프**: **Goal mode `/goal` GA**(수시간~수일, pausable, self-verify, durable markdown `Plan.md`/`Documentation.md`) `[~2026-05-21]` · 클라우드 백그라운드/병렬 · Thread Automations(스케줄) · resume + auto-compaction.

**Top 5:** auto-review(LLM-judge 게이트·역할분리) · Goal mode + done-when · permission profiles(범위 한정) · 서브에이전트+cross-tool import · 2계층 메모리.
**미검증:** canonical CHANGELOG(로드 실패) → 정확한 날짜/CLI 버전 · 앱 빌드번호(v26.xxx, 2차출처) · 훅 GA 정확일 · automations=로컬 cron 제약(2차) · GPT-5.x 모델명(컷오프 이후·독립확인 불가).

## 3. Google Antigravity (신뢰도 72 — 라이브 docs 직독·세부 착지버전 中)

출처: antigravity.google/docs/{home, artifacts, implementation-plan, walkthrough, hooks, subagents, sidecars, permissions, rules-workflows} · developers.googleblog · ai.google.dev/gemini-api · 구글 AI 포럼.

- **정체성/대전환**: 1.0 런칭 `[2025-11-18]`(Gemini 3). **Antigravity 2.0**(`v2.0.1, 2026-05-19`) = standalone 데스크탑 + CLI(Gemini CLI 대체) + SDK(`pip install google-antigravity`) + IDE 4 surface, 단일 harness(Gemini 3.5 Flash). 현재 `2.2.1 (2026-06-25)`.
- **메모리(교훈)**: 1.0 "Knowledge Base(learning primitive)" → 2.0에서 **퇴행/문서 부재**(구글 포럼: 빈 `brain/`, "Knowledge 실패"). 실사용 대안 = **Rules(`GEMINI.md`/`.agents/rules`) + Skills + Artifacts** + 3rd-party Mem0. → **도구 네이티브 메모리에 의존 말고 버전관리 파일로** (Quetzalcoatl SSOT 역검증).
- **완료/검증(핵심)**: **Artifacts** = 검증 가능한 산출물(Implementation Plan→code diff→**Walkthrough**→스샷→**브라우저 녹화**). "도구 호출을 지켜보는 대신 마일스톤에서 deliverable 검토." Artifact review policy(Always Proceed vs 마일스톤 정지). CLI "verification loops" best practice.
- **훅**: `hooks.json`, 5 이벤트(PreToolUse·PostToolUse·PreInvocation·PostInvocation·Stop). **`PreToolUse` 프로그래머블 승인게이트**(allow/deny/ask/force_ask + permissionOverrides). **`Stop` 훅 `decision:"continue"` = 루프 지속**. `PreInvocation` injectSteps. SDK 3범주(Inspect/Decide/Transform).
- **서브에이전트**: `invoke_subagent`(clean context) · 3상태(Running/Idle/Killed, **idle 재awake=재개**) · worktree 격리 · ID 기반 inter-agent 메시징 · built-in(research/browser/self)+custom(`define_subagent`) · **권한 상속+버블링**(부모 승인 초과 불가, Ask가 UI로 상승) · 중첩 10 · `/teamwork-preview`(Ultra).
- **plan/spec**: Planning Mode→artifact 먼저 · **`/grill-me`**(빌드 전 질의) · `/goal` · Workflows(`/name`, 저장 markdown 시퀀스) · **Spec-Driven Development**(specify→clarify→plan→tasks→analyze→implement, Spec-Kit codelabs).
- **자율 루프**: **Sidecars**(관리 백그라운드, restart_policy) · `schedule` cron + `/schedule` · `agentapi`(프로그래밍 루프) · async 실행 · Stop훅 continue · idle-subagent 재개 · HITL 체크포인트(`ask_question`) · Managed Agents(Gemini API, `background=True`, `previous_interaction_id` stateful resume, ~135k auto-compaction).
- **권한엔진(횡단)**: `action(target)` Deny>Ask>Allow. workspace 파일 R/W 자동허용, 그 외(command/MCP/web/non-workspace) **기본 Ask**. deny 예시 `rm -rf`/`sudo`/`.git`/`~/.ssh`.

**Top 5:** 검증-artifact 모델(meaning-first 검증의 외부 검증) · 계층형 승인게이트(action(target)+PreToolUse+SDK deny-by-default) · 네이티브 메모리 불신→파일로 · /goal+Stop continue+Sidecars+idle재개 · 멀티에이전트 핸드오프+clarify(/grill-me).
**미검증:** 2.0.1~2.2.1 사이 기능 도입 시점 · Knowledge "공식 제거" 여부(포럼 근거) · Gemini CLI cutoff 정확일 · /teamwork-preview·Managed Agents 가격티어 · SDK "9 lifecycle points" 열거 · (직접 설치·실행 안 함 — docs/블로그 기반).

**도구가 안 채우는 Quetzalcoatl 차별점:** 3사 모두 **구조화된 3~5개 대안 비교 · Claude–GPT 교차검증 · GarryTan 의미검증 · feasibility 점수**는 네이티브 부재. → 전략: 새 실행 primitives는 강제에 활용, 의미 레이어는 차별점으로 유지.

---

## 종합 출처

- Claude Code: https://code.claude.com/docs/en/changelog · /whats-new · /memory · /hooks · /sub-agents · /workflows · /agent-view · https://claude.com/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code
- OpenAI Codex: https://developers.openai.com/codex/{memories,hooks,subagents,permissions,changelog} · https://developers.openai.com/codex/concepts/sandboxing/auto-review · https://alignment.openai.com/auto-review/ · https://developers.openai.com/blog/run-long-horizon-tasks-with-codex
- Google Antigravity: https://antigravity.google/docs/{home,artifacts,implementation-plan,walkthrough,hooks,subagents,sidecars,permissions,rules-workflows} · https://developers.googleblog.com/build-with-google-antigravity-our-new-agentic-development-platform/ · https://ai.google.dev/gemini-api/docs/antigravity-agent
