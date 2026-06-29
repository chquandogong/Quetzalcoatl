# Capability Matrix — 환경별 강제·역량 매핑

> 상태: **참조(reference) · as-of 2026-06-29** · 소유자: Researcher · 승인: CHENGHAO QUAN
> 신뢰도: Claude Code **85** / OpenAI Codex **72** / Google Antigravity **72**(근거·미검증: [RESEARCH_NOTES](../01-discovery/RESEARCH_NOTES.md)).
> ⚠️ **도구는 빠르게 바뀐다 — 이 표는 스냅샷이다.** 갱신은 새 조사 사이클로 이 파일을 다시 쓴다.

## 왜 이 문서인가 (D8 · D12 · R13)

SKILL.md 본문은 **모델·도구 중립**이다. 구체 도구·버전·기능명·설정 경로는 본문에 박지 않고(노후화 = `R13`) **여기에만** 둔다(`D8` 패턴만 일반화 · `D12` 외부 도구 진화 반영 규칙). 본문의 도구무관 패턴(예: §18.7 "강제 가능한 메커니즘에 바인딩")이 **각 환경에서 무엇으로 실현되는가**를 이 표가 매핑한다. 본문과 이 표가 갈리면 **본문(중립 패턴)이 기준**이고, 이 표는 그 시점의 실현 수단일 뿐이다.

3도구가 2026 상반기에 **독립 수렴**했다(라이프사이클 훅 · 안전 자동승인+위험 차단 · 범위 한정 자율 · goal 루프 · 2계층 메모리 · 권한 버블링). 그래서 다수 항목이 "한 도구의 특이기능"이 아니라 "환경이 제공하면 바인딩할 공통 강제 수단"이다. 단 **수렴≠진실**(§1.4).

## 매트릭스 (능력 × 환경)

> 셀 = 그 환경의 실현 수단(약식). "—" = 네이티브 없음 → **규율로 강등**(§15·§18.6). 일반 챗(ChatGPT/GPT 등)은 도구가 없어 거의 전부 텍스트 규율로 강등 = 중립성의 하한선.

| 능력 (SKILL §)                                              | Claude Code                                                                    | OpenAI Codex                                                               | Google Antigravity                                                           | 일반 챗(도구 없음)                       |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------ | -------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------- |
| **메모리** (§6·§19·§20)                                     | auto MEMORY.md(영속) + CLAUDE.md(권위) + `.claude/rules/`                      | Memories(생성·opt-in) + **AGENTS.md(권위·체크인)**                         | Rules(`GEMINI.md`/`.agents/rules`)+Skills; 네이티브 메모리 **퇴행**          | git/docs/대시보드 텍스트가 메모리        |
| **완료/검증** (§11·§12·§14)                                 | `/code-review`·`/ultrareview`·`/goal` 완료조건                                 | **auto-review**(LLM-judge)·`/review`·Goal "done-when"                      | **Artifacts**(스샷·**브라우저 녹화**=proof)·Walkthrough                      | 증거를 텍스트/링크로 첨부, 사람이 검토   |
| **훅** (§18.7)                                              | Stop/SubagentStop(+`additionalContext`)·PreToolUse·SessionStart·MessageDisplay | SessionStart·PreToolUse·**PermissionRequest**·Stop·PreCompact·PostCompact… | `hooks.json`: PreToolUse·PostToolUse·PreInvocation·PostInvocation·Stop       | — (규율)                                 |
| **행동 전 승인 게이트** (§1.6→§18.7)                        | auto mode 분류기(위험 차단)                                                    | `PreToolUse`/`PermissionRequest` 훅                                        | **`PreToolUse` allow/deny/ask/force_ask** + `action(target)` 엔진            | — 사람이 매번 승인                       |
| **서브에이전트** (§3·§19.2)                                 | 중첩5·worktree격리·`Agent(model:…)`·백그라운드 프롬프트 메인노출               | `.codex/agents/*.toml`(per-agent model/sandbox)·max_depth                  | `invoke_subagent`·3상태(idle 재awake)·built-in/custom·중첩10                 | 역할 기반 사고(단일 모델 내)             |
| **권한 버블링**(부모 범위 초과 불가) (§18.7)                | 백그라운드 승인 메인 노출                                                      | sandbox/권한 상속                                                          | **명시적 버블링 — Ask가 부모 UI로 상승**                                     | — (규율)                                 |
| **plan/spec 모드** (§2·§8)                                  | plan mode · Dynamic Workflows                                                  | **/plan**("안 할 것"+검증) · spec은 미출시                                 | **Planning Mode**+인라인조향 · **/grill-me** · Spec-Kit                      | §8 SPEC 템플릿을 텍스트로                |
| **자율 루프** (§1.7·§18)                                    | `/goal`·`/loop` self-pacing·auto mode                                          | **/goal**(수시간~수일·pausable·self-verify)                                | `/goal`·Sidecars+cron·`agentapi`                                             | 작업 큐+판정을 텍스트로 연속 출력(§18.6) |
| **루프 지속(중단→계속)** — _편의, 안전 아님_ (§18.3)        | Stop훅 `additionalContext` 반환                                                | Stop/SubagentStop 훅                                                       | **Stop훅 `decision:"continue"`**                                             | — (사람이 "계속")                        |
| **재개·체크포인트** (§19)                                   | background sessions·`/resume`·pinned                                           | `resume`+auto-compaction(PreCompact 훅)                                    | idle-subagent 재개·Managed Agents stateful resume(`previous_interaction_id`) | 마지막 커밋/대시보드 메모로 사람이 재개  |
| **컨텍스트 자동 압축 경계** (§19→§18.7)                     | compaction reminders                                                           | **PreCompact/PostCompact 훅**                                              | ~135k auto-compaction                                                        | — (수동 요약)                            |
| **범위 한정 자율(프로파일)** (§18.2)                        | auto mode + allowlist                                                          | **permission profiles**(`:read-only`/`:workspace`/`:danger`)               | `action(target)` Deny>Ask>Allow(workspace만 자동허용)                        | allowlist를 텍스트 약속으로              |
| **교차 도구/기기 핸드오프** (§21)                           | background sessions·/resume                                                    | **thread handoff + Claude Code import**                                    | CLI↔2.0 export·멀티 surface 동기                                             | 대시보드 텍스트를 다른 세션으로 이동     |
| **durable 상태(드리프트 방지)** (§6·§7)                     | workflow scripts·메모리                                                        | **Plan.md/Documentation.md**(스펙동결·결정감사)                            | Implementation Plan·Walkthrough artifacts                                    | docs 체계(§6)·DASHBOARD(§7)              |
| **비용 레버** (§10)                                         | `Agent(model:…)`·effort 등급                                                   | 경량 모델을 서브에이전트에 라우팅                                          | 모델 옵션(Gemini/Claude/GPT)                                                 | —                                        |
| **구조화 대안 비교·교차검증·의미검증** (§4·§5·Office Hours) | — 네이티브 부재                                                                | — 네이티브 부재                                                            | — 네이티브 부재                                                              | —                                        |

> 마지막 행이 **Quetzalcoatl의 차별점**: 3사 모두 §4 대안 비교·§5 Claude–GPT 교차검증·GarryTan 의미검증·feasibility 점수를 네이티브로 제공하지 않는다. 새 실행 primitives는 **강제에 활용**하고, 의미 레이어는 스킬의 고유가치로 유지한다.

> **과대주장 금지(§15 · 적대검토 F2/F3):** 표의 "강제 수단"은 그 환경에 **실제로 존재하고 켜져 있을 때만** 강제다 — 확인 전엔 "강제됨"으로 가정하지 않는다. 바인딩 대상은 **안전 규율(게이트·체크포인트·하위 에이전트 범위)**이며, 루프 "지속"은 **편의일 뿐 안전 속성이 아니다**(자율-증폭 쪽을 "강제 지속"으로 표기하면 §1.6 우회 구멍이 된다, §18.7).

## 수렴이 스킬에 주는 함의 (반영 위치)

| 함의                                                              | 본문 반영                                 | 상태                           |
| ----------------------------------------------------------------- | ----------------------------------------- | ------------------------------ |
| 환경 강제 수단에 게이트·재개·하위범위 **바인딩**(루프 지속 제외)  | **§18.7 신설**(중립 패턴; 도구명은 이 표) | v1.5.0 (B, 게이트 대기)        |
| 완료는 **증거**로, 검증은 **분리된 리뷰어**                       | **§12·§14 보강**                          | v1.5.0 (B, 게이트 대기)        |
| **2계층 메모리** — 권위(버전관리 docs) vs 생성(편의 recall, 불신) | "프로젝트 메모리" 개념(§6/§19 인근)       | **P2로 흡수 예정**             |
| 서브에이전트 **실제 dispatch** + idle/killed 점검                 | §3/§19.2 확장                             | **P2로 흡수 예정**             |
| **컨텍스트 압축=체크포인트 트리거**                               | §19 보강                                  | **P2(부분은 §18.7 표에 반영)** |
| plan/spec 용어 정렬·clarify-before-build                          | §8/§2/§17 경미                            | **P2(낮은 우선순위)**          |

> 본문 추가는 **최소화**한다 — P2 Core Contract(본문 축소) 목표와의 긴장. 그래서 v1.5.0은 강제-바인딩(§18.7)·증거기반 완료만 본문에 넣고, 나머지 패턴은 P2 lean core 재구조 때 흡수한다(D12·[CROSS_VALIDATION_LOG v1.5.0](../02-decisions/CROSS_VALIDATION_LOG.md)).

## 신뢰도·미검증 (§1.4)

- **Claude Code 85**: 공식 changelog/docs 직독. 미검증: 전용 verification-before-completion 훅(없음) · 네이티브 교차모델 검증.
- **Codex 72**: 기능·의미 高, **정확한 날짜/CLI 버전 中低**(canonical CHANGELOG 로드 실패) · GPT-5.x 모델명 컷오프 이후 독립확인 불가.
- **Antigravity 72**: 라이브 docs 직독 高, **2.0.1~2.2.1 기능 도입 시점 中** · Knowledge "공식 제거" 여부 포럼 근거 · 직접 실행 안 함.

## 유지보수 (이 표를 어떻게 갱신하나)

1. 새 조사 사이클에서 [RESEARCH_NOTES](../01-discovery/RESEARCH_NOTES.md)를 **새 스냅샷**으로 추가(과거는 동결).
2. 이 표의 셀을 갱신하고 머리말 **as-of 날짜·신뢰도**를 바꾼다.
3. 새 수렴이 **도구무관 패턴**이면 본문에 추가하되 §15·R13(과대주장·하드코딩 금지) 통과 + 중요 시 §5 교차검증. 도구특이면 이 표에만 둔다.
4. 본문 §18.7이 가리키는 "환경 강제 수단"의 실현이 바뀌면(예: 어떤 도구가 훅 폐기) 이 표만 고치면 된다 — 본문은 불변.
