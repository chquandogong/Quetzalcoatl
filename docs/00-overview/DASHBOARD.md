# DASHBOARD — Quetzalcoatl v3.1.0

> 상태: **v3.1.0 released — 산출물 3층(확인·설명·기계) · 재설치 완료 · 미러 동기 · GitHub Release 게시 완료 (사이클 종료)** · 날짜: 2026-10-06 · 소유자: Quetzalcoatl OS · 승인: CHENGHAO QUAN
> 정본(SSOT): 이 파일 · 보기 좋은 미러: live artifact(읽기용, §7.2)
> 이 보드는 **현재 상태**를 보여준다(작업량 아님, §7). 사이클별 상세는 아래 "릴리스 히스토리"의 링크로.

## 현재 상태

- 단계: **v3.1.0 배포** — 사용자 제안("Word=고객 확인 원본 / md=사람 설명 / JSON=프로그램 판독 `task.json`")을 **§6.4 산출물 3층 + C-26**으로 반영(D16). 원안 그대로가 아니라 **원본≠정본**: 확인층=고객이 확인한 **승인 기준선**(변경 금지 스냅샷), 편집 정본은 사실마다 하나(기계층은 선언된 범위만), 안정 ID+원천 리비전+내용 대조, 기계층 스키마 검증, 층은 필요할 때만(§15).
- 전체 판단: **배포 가능(배포됨)** — 실제 GPT diff 적대 검토 **ACCEPT-WITH-CHANGES 95**, 12건 전부 반영(승인 기준선 혼동 QZ-11 · §7.2 모순 QZ-12 · 확인 파일 변조 QZ-15 등). 구조 검사(CI 동등 6종) 통과. **행동 테스트는 미수행**(정직 기록 — 다음 사이클).
- 같은 세션: **TypeSafe(Jev) 공식 스킬 설치**(`typesafe@typesafe-ai` 0.5.7, 사용자 요청) — 기계층(`task.json`)은 이런 판정 전용 모델이 읽는 "state"의 자리(D16).
- 자율 수준: L2 · 마지막 업데이트: 2026-10-06 (v3.1.0)

## 릴리스 히스토리 (압축 — 상세는 링크)

| 버전       | 날짜     | 한 줄                                                                                     | 교차검증                                                            |
| ---------- | -------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| v1.0.0/.1  | 06-19    | 최초 공개 + Claude Code 플러그인·마켓플레이스 패키징                                      | —                                                                   |
| v1.2.0     | 06-23    | 자율 실행·재개·문서체계·Git·핸드오프(5능력)                                               | 단일모델(GPT 미접속)                                                |
| v1.3.0/.1  | 06-23    | §4.2 앵커된 선호 + 대안비교 §4 승격 + repo 전문화(CI)                                     | —                                                                   |
| v1.4.0~.2  | 06-23~24 | 대시보드 HTML 미러·`/dashboard`(§7.2) · §1.6 6문 pre-check · CI 드리프트 가드             | **실제 Claude–GPT**(`b648d70`)                                      |
| v1.5.0     | 06-29    | §18.7 강제 바인딩 + §12/§14 증거기반 완료 + capability matrix(외부 도구 진화)             | **실제 GPT-5.5** — §1.6 구멍 적발                                   |
| v1.6.0     | 06-29    | §24 `/context` 벤더-중립 휴대용 브리핑(mission-spec 이식)                                 | **실제 GPT-5.5** — R13 위반 적발                                    |
| v2.0.0     | 06-29    | P2 Core Contract 분리 — 템플릿 21개 → §22 부록 C + P3 본문 중립화(동작 호환)              | **실제 GPT-5.5**(diff) — §18.2 회귀 적발                            |
| v2.0.1     | 06-30    | 로컬 미니멈 탈출 — §3 Phase 1-7 프레이밍 흔들기 + §4.1 골짜기 점검 + §4.2 깊이·폭 다이얼  | **실제 GPT-5.5**(적대적 diff) — 78, 형식주의 위험 적발              |
| v3.0.0     | 07-03    | 소스 분리(코어/양식/번들) + 모드 백킹 완성 + 크기 라우터 + 규모 적합성 + 행동 테스트 복귀 | **실제 GPT-5.5**(diff 첨부) — 78, §13 의미-먼저 구멍 적발           |
| **v3.1.0** | 10-06    | **산출물 3층(확인층·설명층·기계층) — 정본은 사실마다 하나 · 승인 기준선 · C-26**          | **실제 GPT**(Codex, diff+전문 첨부) — **95**, 승인 기준선 혼동 적발 |

> 상세: [CHANGELOG](../../CHANGELOG.md) · [DECISION_LOG](../02-decisions/DECISION_LOG.md) · [RETRO](../05-ops/RETRO.md) · [CROSS_VALIDATION_LOG](../02-decisions/CROSS_VALIDATION_LOG.md) · [TEST_PLAN](../04-quality/TEST_PLAN.md)

## 상위 리스크

| 리스크                                         | 가능성 | 영향도 | 대응책                                                                                               | 상태                       |
| ---------------------------------------------- | -----: | -----: | ---------------------------------------------------------------------------------------------------- | -------------------------- |
| 3층 규칙이 작은 프로젝트에 과잉 적용(형식주의) |   중간 |   중간 | "층은 필요할 때만 + 검사는 사용한 층에만 + 한 줄 정본 선언으로 C-26 대체"(§15, QZ-19 반영)           | 완화됨(설계) — 행동 미측정 |
| 확인층 파일 변조·승인 기준선 혼동              |   낮음 |   높음 | 규칙 2·3(확인된 판 불변·메타데이터는 별도 기록·반환본 보존·미확인 후보판) + C-26 확인 기록(QZ-11·15) | 완화됨                     |
| 기계층↔DASHBOARD 이중 정본                     |   낮음 |   중간 | §7.2 개정 — 선언된 보드 필드만 기계층 정본, `/dashboard`는 각 정본에서 갱신(QZ-12)                   | 완화됨                     |
| 분리 구조에서 TEMPLATES.md 미로드              |   낮음 |   중간 | §22.C 로딩·강등 규칙 + v3.0.0 행동 테스트 실동작 증명                                                | 완화됨                     |
| living-doc stale 재발                          |   낮음 |   낮음 | CI 드리프트 가드(규율→강제)                                                                          | 완화됨                     |

## 품질 지표

- **CI**: `validate` — 3중 버전 3.1.0 · JSON · 섹션 §0~§24 연속 · 포인터 무결성(26 ⊆ 26, 중복 0, 색인 26행) · frontmatter 856자+YAML · 번들 신선도(1,806줄) · living-doc 드리프트 가드 — 로컬 동등 검사 전부 통과([TEST_PLAN v3.1.0](../04-quality/TEST_PLAN.md))
- **행동 테스트**: v3.1.0 **미수행**(정직 기록) · 직전 v3.0.0 기록 유지(프레이밍 RED 0/4 vs GREEN 5/5 · A/B 4/4·4/4 · 라우터 2/2)
- **교차검증**: ✅ 실제 Claude↔GPT ×6 — §1.6 구멍 · R13 위반 · §18.2 회귀 · 형식주의 · §13 의미-먼저 구멍 · **승인 기준선 혼동(QZ-11)·확인 파일 변조(QZ-15)**
- **설치**: v3.1.0 — 에이전트 = `SKILL.md`(989줄)+`TEMPLATES.md`(C-1~C-26) 한 세트 · 챗 = `dist/Quetzalcoatl-FULL.md` · Claude 플러그인 **3.1.0 설치 완료**(클론 ff-only 후 `claude plugin update` → "updated from 3.0.0 to 3.1.0", 캐시에 SKILL+TEMPLATES+USAGE 확인 — 새 세션부터 적용) · Codex 사본 동기 완료(diff 없음)

## 재개 지점 (체크포인트)

- 마지막 성공 커밋: **v3.1.0 released** — tag `v3.1.0` · push 완료 · GitHub Release(latest) 게시 완료 — 사용자 승인 2026-10-06.
- 다음 작업: 없음 — 유휴(다음 사이클 대기).

## 사람 결정 대기

- (완료) GitHub Release v3.1.0 게시 — §1.6 게이트에서 멈춘 뒤 사용자 승인("릴리스 게시해줘")으로 게시(2026-10-06, latest).
- **§6.4 문구 확인(A9~A11)**: 본문의 "Word"는 "워드프로세서 문서"(R13 — 교차검증 QZ-22)로, 확인층은 "원본"이 아니라 "승인 기준선"으로 보정됨 — 사용자 의도와 맞는지 확인.
- (선택) TypeSafe 스킬용 `TYPESAFE_API_KEY` 발급·설정(console.typesafe.ai/keys) — 실제 API 호출 시에만 필요.

## 다음 액션

1. **(완료)** 플러그인 3.1.0 재설치(클론 `merge --ff-only origin/main` → `claude plugin update quetzalcoatl@quetzalcoatl`) — 캐시 SKILL+TEMPLATES 확인 · Codex 사본 동기(RUNBOOK 2·4).
2. **(완료)** 미러 redeploy(같은 URL, §7.2) + 문서 동기 커밋.
3. (후속) §6.4 행동 테스트("고객 확인 + 자동화" 시나리오) · 강등 규칙 테스트 · evals.

## 링크

- 저장소: https://github.com/chquandogong/Quetzalcoatl · 태그 `v3.1.0`(latest) · [Release v3.1.0](https://github.com/chquandogong/Quetzalcoatl/releases/tag/v3.1.0)
- 문서 지도: [`docs/`](../README.md) · [DECISION_LOG](../02-decisions/DECISION_LOG.md) · [CROSS_VALIDATION_LOG](../02-decisions/CROSS_VALIDATION_LOG.md) · [TEST_PLAN](../04-quality/TEST_PLAN.md) · [CAPABILITY_MATRIX](../appendix/CAPABILITY_MATRIX.md)
- 보기 좋은 미러(읽기용): [live artifact](https://claude.ai/code/artifact/3a1da038-a3d6-4146-9f55-0f54e7063443) · 소스 [`docs/assets/dashboard.html`](../assets/dashboard.html) · 정본이 SSOT(§7.2 / §21.3)
