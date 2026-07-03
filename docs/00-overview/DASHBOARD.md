# DASHBOARD — Quetzalcoatl v3.0.0

> 상태: **v3.0.0 released — 소스 분리 + 완결성 + 행동 테스트 복귀 (재설치 완료 — 사이클 종료)** · 날짜: 2026-07-03 · 소유자: Quetzalcoatl OS · 승인: CHENGHAO QUAN
> 정본(SSOT): 이 파일 · 보기 좋은 미러: live artifact(읽기용, §7.2)
> 이 보드는 **현재 상태**를 보여준다(작업량 아님, §7). 사이클별 상세는 아래 "릴리스 히스토리"의 링크로.

## 현재 상태

- 단계: **v3.0.0 배포** — `SKILL.md`(규칙 963줄) / `TEMPLATES.md`(양식 C-1~C-25) / `dist` 페이스트 번들 분리(D13) + 모드 백킹 완성(D15) + §13 크기 라우터 + **규모 적합성 scale envelope**(사용자 요청, D14) + CI 가드 6종.
- 전체 판단: **배포 가능** — 실제 GPT-5.5 diff 적대 검토(ACCEPT-WITH-CHANGES 78, 9/10 반영·1 기각) + **행동 테스트 복귀**: 프레이밍 흔들기 RED 0/4 vs GREEN 5/5(전제 깨는 후보를 표에), A/B 준수 4/4·4/4, 라우터 과잉 프로세스 0. Claude 플러그인 재설치 완료(캐시 3.0.0, SKILL+TEMPLATES 한 세트 확인).
- 자율 수준: L2 · 마지막 업데이트: 2026-07-03 (v3.0.0)

## 릴리스 히스토리 (압축 — 상세는 링크)

| 버전       | 날짜     | 한 줄                                                                                         | 교차검증                                                  |
| ---------- | -------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| v1.0.0/.1  | 06-19    | 최초 공개 + Claude Code 플러그인·마켓플레이스 패키징                                          | —                                                         |
| v1.2.0     | 06-23    | 자율 실행·재개·문서체계·Git·핸드오프(5능력)                                                   | 단일모델(GPT 미접속)                                      |
| v1.3.0/.1  | 06-23    | §4.2 앵커된 선호 + 대안비교 §4 승격 + repo 전문화(CI)                                         | —                                                         |
| v1.4.0~.2  | 06-23~24 | 대시보드 HTML 미러·`/dashboard`(§7.2) · §1.6 6문 pre-check · CI 드리프트 가드                 | **실제 Claude–GPT**(`b648d70`)                            |
| v1.5.0     | 06-29    | §18.7 강제 바인딩 + §12/§14 증거기반 완료 + capability matrix(외부 도구 진화)                 | **실제 GPT-5.5** — §1.6 구멍 적발                         |
| v1.6.0     | 06-29    | §24 `/context` 벤더-중립 휴대용 브리핑(mission-spec 이식)                                     | **실제 GPT-5.5** — R13 위반 적발                          |
| v2.0.0     | 06-29    | P2 Core Contract 분리 — 템플릿 21개 → §22 부록 C + P3 본문 중립화(동작 호환)                  | **실제 GPT-5.5**(diff) — §18.2 회귀 적발                  |
| v2.0.1     | 06-30    | 로컬 미니멈 탈출 — §3 Phase 1-7 프레이밍 흔들기 + §4.1 골짜기 점검 + §4.2 깊이·폭 다이얼      | **실제 GPT-5.5**(적대적 diff) — 78, 형식주의 위험 적발    |
| **v3.0.0** | 07-03    | **소스 분리(코어/양식/번들) + 모드 백킹 완성 + 크기 라우터 + 규모 적합성 + 행동 테스트 복귀** | **실제 GPT-5.5**(diff 첨부) — 78, §13 의미-먼저 구멍 적발 |

> 상세: [CHANGELOG](../../CHANGELOG.md) · [DECISION_LOG](../02-decisions/DECISION_LOG.md) · [RETRO](../05-ops/RETRO.md) · [CROSS_VALIDATION_LOG](../02-decisions/CROSS_VALIDATION_LOG.md) · [TEST_PLAN](../04-quality/TEST_PLAN.md)

## 상위 리스크

| 리스크                                         | 가능성 | 영향도 | 대응책                                                                                             | 상태   |
| ---------------------------------------------- | -----: | -----: | -------------------------------------------------------------------------------------------------- | ------ |
| 분리 구조에서 TEMPLATES.md 미로드(규율 불이행) |   낮음 |   중간 | §22.C 로딩 규칙+강등 규칙 + **행동 테스트가 실동작 증명**(B 아암이 C-6·C-17만 읽음) + RUNBOOK 확인 | 완화됨 |
| §13 라우터가 의미 검토를 우회                  |   낮음 |   중간 | 교차검증(QZ-03) 반영 — "§1.1·§1.6는 어떤 크기에서도 생략 불가" 불변식 명문화                       | 완화됨 |
| 챗 사용자가 습관적으로 SKILL.md만 페이스트     |   중간 |   낮음 | USAGE/README 번들 경로 안내 + §22.C 강등 규칙(색인=최소 명세)                                      | 완화됨 |
| living-doc stale 재발                          |   낮음 |   낮음 | CI 드리프트 가드(규율→강제)                                                                        | 완화됨 |

## 품질 지표

- **CI**: `validate` — 3중 버전 3.0.0 · JSON · 섹션 §0~§24 연속 · **포인터 무결성(중복·색인 포함)** · **frontmatter 길이+YAML** · **번들 신선도** · living-doc 드리프트 가드
- **행동 테스트**(TEST_PLAN v3.0.0, Opus 서브에이전트): 프레이밍 흔들기 **RED 0/4 vs GREEN 5/5**(전제 깨는 후보를 비교표에) · A/B(963 vs 1,712줄) §4.2 준수 4/4·4/4(차이 미검출) · §13 라우터 2/2 lite. 대조군 메모리 오염·소표본은 정직 기록.
- **교차검증**: ✅ 실제 Claude↔GPT-5.5 ×5 — §1.6 구멍 · R13 위반 · §18.2 회귀 · 형식주의 · **§13 의미-먼저 구멍(QZ-03)** 을 단일모델 사각에서 적발
- **설치**: v3.0.0 — 에이전트 = `SKILL.md`+`TEMPLATES.md` 한 세트 · 챗 = `dist/Quetzalcoatl-FULL.md` · **Claude 플러그인 3.0.0 설치 완료**(새 세션부터 적용) · Codex 사본 동기 완료

## 재개 지점 (체크포인트)

- 마지막 성공 커밋: **v3.0.0 released** — tag `v3.0.0` · GitHub Release(latest) · CI green.
- 다음 작업: 없음 — 유휴(다음 사이클 대기).

## 사람 결정 대기

- 대기 없음.
- (후속·선택) 강등 규칙 행동 테스트 · 청정 대조군 격리 경로 · P3(강등 관용구 일반화) · evals 상설화.

## 다음 액션

1. **(완료) 재설치** — 캐시 3.0.0에 `SKILL.md`+`TEMPLATES.md` 확인. ⚠️ 마켓플레이스 클론이 stale이면 재설치가 구버전을 깐다 — `git -C ~/.claude/plugins/marketplaces/quetzalcoatl merge --ff-only origin/main` 후 update(RUNBOOK 반영).
2. **(완료) 미러 동기** — 정본 v3.0.0 → HTML 미러 같은 URL redeploy(§7.2).
3. (후속·선택) 강등 규칙 행동 테스트 · evals.

## 링크

- 저장소: https://github.com/chquandogong/Quetzalcoatl · 태그 `v3.0.0`(latest) · [Release v3.0.0](https://github.com/chquandogong/Quetzalcoatl/releases/tag/v3.0.0)
- 문서 지도: [`docs/`](../README.md) · [DECISION_LOG](../02-decisions/DECISION_LOG.md) · [CROSS_VALIDATION_LOG](../02-decisions/CROSS_VALIDATION_LOG.md) · [TEST_PLAN](../04-quality/TEST_PLAN.md) · [CAPABILITY_MATRIX](../appendix/CAPABILITY_MATRIX.md)
- 보기 좋은 미러(읽기용): [live artifact](https://claude.ai/code/artifact/3a1da038-a3d6-4146-9f55-0f54e7063443) · 소스 [`docs/assets/dashboard.html`](../assets/dashboard.html) · 정본이 SSOT(§7.2 / §21.3)
