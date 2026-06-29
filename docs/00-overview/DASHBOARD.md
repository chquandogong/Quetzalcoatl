# DASHBOARD — Quetzalcoatl v2.0.0

> 상태: **v2.0.0 배포 완료 (재설치 대기)** · 날짜: 2026-06-29 · 소유자: Quetzalcoatl OS · 승인: CHENGHAO QUAN
> 정본(SSOT): 이 파일 · 보기 좋은 미러: live artifact(읽기용, §7.2)
> 이 보드는 **현재 상태**를 보여준다(작업량 아님, §7). 사이클별 상세는 아래 "릴리스 히스토리"의 링크로.

## 현재 상태

- 단계: **v2.0.0 배포 완료** — P2 Core Contract 분리 + P3 본문 중립화. latest released.
- 전체 판단: **v2.0.0 배포 완료** — 템플릿 21개 → §22 부록 C(규칙 무손상·동작 호환) + P3 강등 관용구 중립화. tag `v2.0.0` · GitHub Release(latest) · CI green · 실제 Claude↔GPT-5.5 교차검증 반영(§18.2 안전 회귀 수정). 남은 것: 재설치(사람).
- 자율 수준: L2 · 마지막 업데이트: 2026-06-29 (v2.0.0 배포)

## 릴리스 히스토리 (압축 — 상세는 링크)

| 버전       | 날짜     | 한 줄                                                                                 | 교차검증                                 |
| ---------- | -------- | ------------------------------------------------------------------------------------- | ---------------------------------------- |
| v1.0.0/.1  | 06-19    | 최초 공개 + Claude Code 플러그인·마켓플레이스 패키징                                  | —                                        |
| v1.2.0     | 06-23    | 자율 실행·재개·문서체계·Git·핸드오프(5능력)                                           | 단일모델(GPT 미접속)                     |
| v1.3.0/.1  | 06-23    | §4.2 앵커된 선호 + 대안비교 §4 승격 + repo 전문화(CI)                                 | —                                        |
| v1.4.0~.2  | 06-23~24 | 대시보드 HTML 미러·`/dashboard`(§7.2) · §1.6 6문 pre-check · CI 드리프트 가드         | **실제 Claude–GPT**(`b648d70`)           |
| **v1.5.0** | 06-29    | **§18.7 강제 바인딩** + **§12/§14 증거기반 완료** + capability matrix(외부 도구 진화) | **실제 GPT-5.5** — §1.6 구멍 적발        |
| **v1.6.0** | 06-29    | **§24 `/context`** 벤더-중립 휴대용 브리핑(mission-spec 이식)                         | **실제 GPT-5.5** — R13 위반 적발         |
| **v2.0.0** | 06-29    | **P2 Core Contract 분리** — 템플릿 21개 → §22 부록 C + P3 본문 중립화(동작 호환)      | **실제 GPT-5.5**(diff) — §18.2 회귀 적발 |

> 상세: [CHANGELOG](../../CHANGELOG.md) · [DECISION_LOG](../02-decisions/DECISION_LOG.md) · [RETRO](../05-ops/RETRO.md) · [CROSS_VALIDATION_LOG](../02-decisions/CROSS_VALIDATION_LOG.md)

## 상위 리스크

| 리스크                 | 가능성 | 영향도 | 대응책                                             | 상태   |
| ---------------------- | -----: | -----: | -------------------------------------------------- | ------ |
| living-doc stale 재발  |   낮음 |   낮음 | CI 드리프트 가드(규율→강제)                        | 완화됨 |
| 자율이 게이트 회색화   |   낮음 |   중간 | §1.6 행동 전 6문 pre-check · L2/L3 면제 없음       | 완화됨 |
| 본문 비대 준수 희석    |   중간 |   중간 | **P2 Core Contract 분리(v2.0.0)** — 규칙/양식 분리 | 완화됨 |
| R13 본문 도구명 재노출 |   낮음 |   중간 | 교차검증이 §24에서 실제 적발·수정 → §5 게이트 상시 | 완화됨 |

## 품질 지표

- **CI**: `validate` green — 3중 버전 2.0.0 · JSON · 섹션 §0~§24 연속 · living-doc 드리프트 가드
- **교차검증**: ✅ **실제 Claude↔GPT-5.5**(Codex exec) ×3 — v1.5.0 §1.6 구멍 · v1.6.0 R13 위반 · v2.0.0 P2 diff(§18.2 회귀 적발)
- **중립성**: SKILL 본문 도구명 0 (R13 + P3 강등 관용구 중립화) · 구체 기술은 CAPABILITY_MATRIX(docs)
- **설치**: v2.0.0 — Claude 플러그인 재설치 대기 · Codex 사본 동기 예정

## 재개 지점 (체크포인트)

- 마지막 성공 커밋: **v2.0.0 배포** — tag `v2.0.0` · GitHub Release(latest) · `8fe5c19` · CI green.
- 다음 작업: 재설치(Claude 플러그인 + Codex 사본) · 미러 redeploy. 그 외 유휴.

## 사람 결정 대기

- 그 외 대기 없음(v2.0.0 배포 완료 · 재설치만 사람).
- (후속·선택) GPT·Codex 제안: evals(trigger·행동) · 설치 동기 자동 체크 · 누락 패턴(capability discovery·2계층 메모리 규칙).

## 다음 액션

1. **(사람) 재설치** — Claude: `/plugin marketplace update quetzalcoatl` → `install` → `/reload-plugins`. Codex 사본은 자동 동기됨.
2. (후속·선택) evals · 설치 동기 자동 체크.
3. (유지) 외부 도구 진화 시 **capability matrix만 갱신**(본문 불변, D12).

## 링크

- 저장소: https://github.com/chquandogong/Quetzalcoatl · 태그 `v2.0.0`(latest) · [Release v2.0.0](https://github.com/chquandogong/Quetzalcoatl/releases/tag/v2.0.0)
- 문서 지도: [`docs/`](../README.md) · [DECISION_LOG](../02-decisions/DECISION_LOG.md) · [CROSS_VALIDATION_LOG](../02-decisions/CROSS_VALIDATION_LOG.md) · [CAPABILITY_MATRIX](../appendix/CAPABILITY_MATRIX.md)
- 보기 좋은 미러(읽기용): live artifact · 소스 [`docs/assets/dashboard.html`](../assets/dashboard.html) · 정본이 SSOT(§7.2 / §21.3)
