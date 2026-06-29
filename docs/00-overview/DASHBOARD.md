# DASHBOARD — Quetzalcoatl v1.6.0

> 상태: **v1.6.0 배포·설치 완료** · 날짜: 2026-06-29 · 소유자: Quetzalcoatl OS · 승인: CHENGHAO QUAN
> 정본(SSOT): 이 파일 · 보기 좋은 미러: live artifact(읽기용, §7.2)
> 이 보드는 **현재 상태**를 보여준다(작업량 아님, §7). 사이클별 상세는 아래 "릴리스 히스토리"의 링크로.

## 현재 상태

- 단계: **유휴(idle)** — v1.6.0 게시·재설치 완료. 다음 큰 건은 P2 Core Contract(승인 대기).
- 전체 판단: **배포 완료** — `/context`(§24) 벤더-중립 휴대용 브리핑까지 안착. 본문 §0~§24 · 3중 버전 1.6.0 · CI green · tag·Release(latest).
- 자율 수준: L2 · 마지막 업데이트: 2026-06-29 (문서 정리)

## 릴리스 히스토리 (압축 — 상세는 링크)

| 버전       | 날짜     | 한 줄                                                                                 | 교차검증                          |
| ---------- | -------- | ------------------------------------------------------------------------------------- | --------------------------------- |
| v1.0.0/.1  | 06-19    | 최초 공개 + Claude Code 플러그인·마켓플레이스 패키징                                  | —                                 |
| v1.2.0     | 06-23    | 자율 실행·재개·문서체계·Git·핸드오프(5능력)                                           | 단일모델(GPT 미접속)              |
| v1.3.0/.1  | 06-23    | §4.2 앵커된 선호 + 대안비교 §4 승격 + repo 전문화(CI)                                 | —                                 |
| v1.4.0~.2  | 06-23~24 | 대시보드 HTML 미러·`/dashboard`(§7.2) · §1.6 6문 pre-check · CI 드리프트 가드         | **실제 Claude–GPT**(`b648d70`)    |
| **v1.5.0** | 06-29    | **§18.7 강제 바인딩** + **§12/§14 증거기반 완료** + capability matrix(외부 도구 진화) | **실제 GPT-5.5** — §1.6 구멍 적발 |
| **v1.6.0** | 06-29    | **§24 `/context`** 벤더-중립 휴대용 브리핑(mission-spec 이식)                         | **실제 GPT-5.5** — R13 위반 적발  |

> 상세: [CHANGELOG](../../CHANGELOG.md) · [DECISION_LOG](../02-decisions/DECISION_LOG.md) · [RETRO](../05-ops/RETRO.md) · [CROSS_VALIDATION_LOG](../02-decisions/CROSS_VALIDATION_LOG.md)

## 상위 리스크

| 리스크                        | 가능성 | 영향도 | 대응책                                             | 상태   |
| ----------------------------- | -----: | -----: | -------------------------------------------------- | ------ |
| living-doc stale 재발         |   낮음 |   낮음 | CI 드리프트 가드(규율→강제)                        | 완화됨 |
| 자율이 게이트 회색화          |   낮음 |   중간 | §1.6 행동 전 6문 pre-check · L2/L3 면제 없음       | 완화됨 |
| 본문 비대(~1,460줄) 준수 희석 |   중간 |   중간 | **P2 Core Contract 분리**(승인 필요)               | 열림   |
| R13 본문 도구명 재노출        |   낮음 |   중간 | 교차검증이 §24에서 실제 적발·수정 → §5 게이트 상시 | 완화됨 |

## 품질 지표

- **CI**: `validate` green — 3중 버전 1.6.0 · JSON · 섹션 §0~§24 연속 · living-doc 드리프트 가드
- **교차검증**: ✅ **실제 Claude↔GPT-5.5**(Codex exec) ×2 — v1.5.0 §1.6 구멍 · v1.6.0 R13 위반을 단일모델 사각에서 적발·수정
- **중립성**: SKILL 본문 도구명 0(R13) · 구체 기술은 CAPABILITY_MATRIX(docs)
- **설치**: 플러그인 v1.6.0 재설치·reload 완료

## 재개 지점 (체크포인트)

- 마지막 성공 커밋: **v1.6.0 배포** — tag `v1.6.0` · GitHub Release(latest) · 본문 `4b0fc59` · CI green
- 다음 작업: 유휴. (선택) 미러 live redeploy · (승인) P2 Core Contract.

## 사람 결정 대기

- **P2 Core Contract 분리**(~250줄 + 부록) — 대규모 재구조, 승인 필요. v1.5.0/v1.6.0 패턴(§18.7·증거기반 완료·§24)을 lean core로 흡수 + GPT가 짚은 누락 패턴(capability discovery·2계층 메모리 규칙 등).
- 그 외 대기 없음.

## 다음 액션

1. (선택) 미러 live artifact redeploy — 이 정리된 DASHBOARD 기준 재렌더(§7.2).
2. (선택·승인) P2 Core Contract 분리 — 별도 사이클.
3. (유지) 외부 도구 추가 진화 시 **capability matrix만 갱신**(본문 불변, D12).

## 링크

- 저장소: https://github.com/chquandogong/Quetzalcoatl · 태그 `v1.6.0`(latest) · [Release v1.6.0](https://github.com/chquandogong/Quetzalcoatl/releases/tag/v1.6.0)
- 문서 지도: [`docs/`](../README.md) · [DECISION_LOG](../02-decisions/DECISION_LOG.md) · [CROSS_VALIDATION_LOG](../02-decisions/CROSS_VALIDATION_LOG.md) · [CAPABILITY_MATRIX](../appendix/CAPABILITY_MATRIX.md)
- 보기 좋은 미러(읽기용): live artifact · 소스 [`docs/assets/dashboard.html`](../assets/dashboard.html) · 정본이 SSOT(§7.2 / §21.3)
