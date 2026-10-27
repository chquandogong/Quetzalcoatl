# VERIFY — Quetzalcoatl 스킬 (저장소 자신에 C-29 적용 · dogfooding)

> 문서 상태(기준·절차 명세의 완성 여부): 작성 완료 · 절차 구동 확인: V-1·V-2·V-7(실행 기록 R1) · 날짜: 2026-10-27 · 소유자: QA Evaluator · 기준 정본: [RUNBOOK 배포·검증 절](../05-ops/RUNBOOK.md) · [TEST_PLAN](TEST_PLAN.md) · [README 설치 절](../../README.md) · 실행 기록 정본: [verify-runs/2026-10-27-v3.3.0.md](verify-runs/2026-10-27-v3.3.0.md)
> 실행 현황(판정 범위 = 이 호스트 · 각 실행 기록의 커밋, 행별 기록에서 집계): 대상 7건 — 통과 3 · 실패 0 · 차단 0 · 미실행 4 · 재검증 필요 0 · 최신 실행: R1 · 2026-10-27 · e379678+작업 트리(릴리스 후 R2로 갱신)
> 범위: 이 표가 확인하는 조건 = 이 호스트(로컬 리눅스, bash·python3·jq·prettier·Claude Code 플러그인 CLI) · 대상 판 = 각 실행 기록의 커밋. 확인하지 않는 것 = 다른 OS·챗 환경(ChatGPT 등)에서의 번들 붙여넣기 동작(미검증), 스킬 규칙의 행동 효과(그건 [TEST_PLAN v3.3.0](TEST_PLAN.md)의 행동 테스트).

## 표면과 구동 수단

- 주 표면: **에이전트 스킬 파일**(플러그인 설치 → `/quetzalcoatl:Quetzalcoatl` 호출 시 `SKILL.md`+`TEMPLATES.md` 로드) · 그 외: **챗 페이스트 번들**(`dist/Quetzalcoatl-FULL.md`) · **CLI**(빌드·검증 스크립트) · **웹 화면**(대시보드 HTML 미러, live artifact)
- 구동 수단(기존 하네스 우선): `scripts/build-paste-bundle.sh` · `scripts/validate-local.sh`(CI `validate.yml`과 동등) · `claude plugin update quetzalcoatl@quetzalcoatl`(마켓플레이스 클론 ff-only 후) · 서브에이전트에 번들/플러그인을 읽혀 호출 · Artifact 같은 URL redeploy · 격리: V-1·V-2는 실행마다 `mktemp -d`로 만든 임시 디렉터리에만 쓰므로 그 조건에서 병행 가능(확인: R1) · 플러그인 업데이트(V-3)의 병행 안전성은 **미확인**(확인 전까지 단일 실행)
- 기기·외부 영향이 있는 수단과 승인 근거: push·태그·GitHub Release·플러그인 재설치·미러 redeploy — **사전승인**(사용자 지시 2026-10-06, [RUNBOOK 사전승인 목록](../05-ops/RUNBOOK.md)) · 승인 없는 것 → 강제 푸시(`--force`)·히스토리 재작성·새 공개 저장소·삭제·유료 외부 API: 차단(사람 승인 전 미실행)

## 실행

- 시작: `bash scripts/validate-local.sh [--no-living]` · 준비 완료 신호: `ALL OK` 출력(종료 코드 0) · 환경: 저장소 루트, 의존성 jq·python3(yaml)·bash
- 상태 점검(doctor): `git status --short`(작업 트리) · `grep '^version:' skills/Quetzalcoatl/SKILL.md` · `ls ~/.claude/plugins/cache/quetzalcoatl/quetzalcoatl/` — 실행 전 · 실패 후
- 상태 변화(실행별로 기록 — 실제 변경은 각 실행 기록 참조): R1(검사) = 임시 디렉터리 생성 → 정리, 저장소 변경 없음 · V-3(미실행) 예상 변경 = 플러그인 캐시에 새 버전 디렉터리·설치 상태 갱신, 실행 후 실제 변경을 R2에 기록 · 잔여물 = 플러그인 캐시의 구버전 디렉터리(의도적 보존, 롤백용)
- 정리: 시작한 것만 종료(스크립트는 자체 종료) · 증거 보존 위치: `docs/04-quality/verify-runs/`

## 기능 지도 (항목 선정: 변경 영향 · 실패 피해 · 사용 빈도 — 핵심 경로 + 해당되는 실패 · 경계 조건)

| ID  | 항목 · 기준 참조                                                         | 전제 · 입력                                      | 사용자 경로 · 구동 절차                                                                                                                                                                                                                                            | 기대 결과 (끝 상태 · 기대 부수효과 · 금지 부수효과)                                                                      | 실제 관측                      | 증거 위치      | 적용 가능한 최신 실행 (ID · 시각 · 대상 판 · 환경) | 판정              |
| --- | ------------------------------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------ | -------------- | -------------------------------------------------- | ----------------- |
| V-1 | 챗 사용자가 붙여넣는 번들이 소스와 같다 — README 설치 절 · RUNBOOK 5     | 소스 두 파일 존재                                | `d=$(mktemp -d) && bash scripts/build-paste-bundle.sh $d/bundle.md && diff -q $d/bundle.md dist/Quetzalcoatl-FULL.md`(실행 ID에 디렉터리 연결, 자신이 만든 것만 정리)                                                                                              | diff 0 · 번들 머리 = frontmatter · 템플릿 29개 포함 · 금지: 소스 변경 없음                                               | diff 0 · 29개 · 소스 변경 없음 | verify-runs R1 | R1 · 2026-10-27 · e379678+tree · 로컬              | 통과              |
| V-2 | 구조 불변식 10항목(CI 동등) — TEST_PLAN 구조 검사                        | 저장소 루트                                      | `bash scripts/validate-local.sh --no-living`                                                                                                                                                                                                                       | `ALL OK` · 종료 0 · 금지: 파일 변경 없음                                                                                 | ALL OK(10 OK)                  | verify-runs R1 | R1 · 2026-10-27 · e379678+tree · 로컬              | 통과              |
| V-7 | 실패 경로 — living-doc 드리프트 가드가 불일치를 **적발**하는가 (R16·R17) | 릴리스 동기 전(RUNBOOK·DASHBOARD·미러=이전 버전) | `bash scripts/validate-local.sh`                                                                                                                                                                                                                                   | 3곳 FAIL + `SOME CHECKS FAILED` + 종료 1                                                                                 | 3곳 FAIL · 종료 1              | verify-runs R1 | R1 · 2026-10-27 · e379678+tree · 로컬              | 통과(적발 확인)   |
| V-3 | 플러그인 사용자가 새 버전을 받아 호출하면 새 규칙이 보인다 — RUNBOOK 2   | push 완료 · 마켓플레이스 클론 ff-only            | 클론 `merge --ff-only origin/main` → `claude plugin update quetzalcoatl@quetzalcoatl` → 새 세션(서브에이전트)에서 스킬 호출                                                                                                                                        | 캐시 `…/3.3.0/`에 SKILL+TEMPLATES · 호출 결과에 version 3.3.0·§11 검증표·C-29 보임 · 금지: 구버전 재설치(RUNBOOK gotcha) | (릴리스 후)                    | verify-runs R2 | —                                                  | 미실행(릴리스 후) |
| V-4 | 챗 강등 경로 — 번들만 읽은 에이전트가 검증표(C-29)를 실제로 산출한다     | 번들 사본 · 실행 가능한 프로젝트 스냅샷          | 행동 테스트 GREEN 아암(TEST_PLAN v3.3.0 시나리오)                                                                                                                                                                                                                  | VERIFY 문서 산출 · 기기 미구동 · 완료 상태 구분 · 무응답≠승인                                                            | (행동 테스트 결과 참조)        | TEST_PLAN      | —                                                  | 미실행(진행 중)   |
| V-5 | 대시보드 미러가 같은 URL에 redeploy되고 정본과 버전이 맞다 — §7.2        | 정본 DASHBOARD 갱신 완료                         | Artifact publish(url 고정) → 미러 제목·버전 확인                                                                                                                                                                                                                   | 같은 URL · 제목 v3.3.0 · 금지: 새 URL 발급                                                                               | (릴리스 후)                    | verify-runs R2 | —                                                  | 미실행(릴리스 후) |
| V-6 | 원격 CI `validate`가 실제로 green — RUNBOOK 검증                         | push 완료                                        | `gh run list --workflow validate --commit <릴리스 SHA> --branch main --json databaseId,conclusion,status` → 대상 SHA·브랜치·workflow가 일치하는 실행의 ID 기록 · `status=completed` + `conclusion=success` 확인 · 일치하는 완료 실행이 없으면 통과로 판정하지 않음 | success                                                                                                                  | (릴리스 후)                    | verify-runs R2 | —                                                  | 미실행(릴리스 후) |

## 증거 범위 요약

- V-1·V-2·V-7: **실제 대상에서 동작**(이 저장소·이 호스트) — 다른 호스트·OS는 미확인.
- V-3·V-5·V-6: 릴리스 후 실행 — 그 전까지 "빌드 가능"까지만.
- V-4: 스킬 규칙의 행동 효과는 **대역(서브에이전트·합성 프로젝트)**에서의 관측 — 실제 사용자 프로젝트(로보틱스·카메라)는 미검증(A23).

## 주의점 (gotchas)

- 마켓플레이스 클론이 stale이면 재설치가 구버전을 다시 깐다(RUNBOOK 2) — V-3 전제의 ff-only가 그 때문.
- 미러 redeploy는 Artifact 도구에 **기존 URL을 넘겨야** 같은 URL(새 세션 gotcha, DASHBOARD 링크의 URL 사용).
- `validate-local.sh`의 living-doc 가드는 릴리스 커밋 전에 의도적으로 FAIL한다(`--no-living`으로 구조만).

## 드리프트 · 결함 기록 (유지 패스마다)

| 날짜       | 종류 (문서 드리프트 / 하네스 공백 / 제품 결함) | 내용                                                                 | 처리                                             |
| ---------- | ---------------------------------------------- | -------------------------------------------------------------------- | ------------------------------------------------ |
| 2026-10-27 | 하네스 공백                                    | CI 동등 검사가 로컬에 스크립트로 없어 매 사이클 ad hoc 셸로 재현했음 | `scripts/validate-local.sh` 추가(구동 수단 수정) |
