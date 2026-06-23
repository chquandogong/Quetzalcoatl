# Changelog

이 프로젝트의 주요 변경 사항을 기록한다. 형식은 [Keep a Changelog](https://keepachangelog.com/),
버전은 [SemVer](https://semver.org/)를 따른다.

## [1.4.0] - 2026-06-23

### Added

- **§7.2 대시보드 HTML 미러 + `/dashboard` 갱신** — 정본(`DASHBOARD.md`)은 SSOT로 두고, 보기 좋은 HTML 미러를 live artifact의 같은 URL에 redeploy. 수동(`/dashboard`)·자동(자율 루프 규율) 두 경로.
- **§2 `/dashboard` 모드 확장 · §18.3 루프** — 의미 있는 커밋 후 미러 redeploy를 연속 실행 루프에 반영.

### Note

- MINOR — 새 갱신 경로 추가, 기존 동작 보존. "자동"은 강제 락이 아니라 **에이전트 규율**임을 명시(§15 정직성); 세션 밖 자동은 외부 CI·공개 게이트로 분리. 미러 디자인은 스킬에 하드코딩하지 않음(주제별).

## [1.3.1] - 2026-06-23

### Added

- **용어집 동기** — `§22 부록 A`와 `docs/appendix/GLOSSARY.md`에 **"앵커된 선호(Anchored Preference)"** 항목 추가(§4.2 규칙의 용어 정의). v1.3.0에서 deferred했던 GLOSSARY↔§22 동기화를 완결.

### Note

- PATCH — 새 동작 없이 기존 §4.2 개념의 용어 정의만 보강. SKILL `§22`가 배포본이므로 버전 상승.

## [1.3.0] - 2026-06-23

사용자 선호를 다루는 규칙을 추가하고, 대안 비교를 독립 섹션으로 승격하며, 저장소를 전문가용으로 정비.

### Added

- **§4.2 앵커된 선호 처리** — 사용자가 선호를 제시하며 "근거가 충분하면 바꿔도 좋다"고 위임할 때의 규칙. 선호=기본값(prior), 근소하면 선호 유지(tie→user), 뒤집을 땐 근거를 표로 제시하고 비가역 전환은 §1.6 게이트. 맹종↔독단 사이 중도. 구체 기술 선택(언어·UI 프레임워크)은 모델·도메인 중립성을 위해 본문에 넣지 않고 **패턴만 일반화**.
- **저장소 전문화** — README 배지(release·license), `.gitattributes`(eol·linguist), `SECURITY.md`, GitHub Actions CI(매니페스트·frontmatter 버전 일치 검증), repo topics.

### Changed

- **§4 신설** — "대안 3~5개 비교"를 §3의 Phase 4에서 독립 `## 4. 대안 비교 및 선호 처리`로 승격. 이로써 최상위 섹션 번호 누락(§3 다음이 §5였던 문제)을 정정. §5~§23 번호 불변.

## [1.2.0] - 2026-06-23

의미·가치 검증을 거쳐(`docs/01-discovery/`) 채택한 5개 능력 추가.
Quetzalcoatl을 단일 세션 자문 OS에서 **지속·재개 가능한 다중 에이전트/다중 기기 실행 OS**로 확장.

### Added

- **§1.7 + §18 지속 자율 실행** — "승인된 계획 범위 안에서" 확인 질문 없이 끝까지 실행. 실행 허용목록(allowlist), 자율 수준 L0~L3, 연속 실행 루프, 합리화 차단표.
- **§19 레이트리밋·하위 에이전트 회복력** — 한도/중단 시 대기 후 재개. 체크포인트 = 마지막 성공 커밋. 외부 발송·결제는 자동 재개 제외.
- **§6 문서 체계** — 표준 디렉터리 구조(`docs/00-overview … 05-ops · appendix · assets`), 마크다운·그림·표 우선, 용어 부록(§22 부록 A).
- **§20 Git 저장소 프로토콜** — `git init` 가드, Conventional Commits, 의미 단위 커밋, SemVer 주석 태그.
- **§7.1 + §21 교차 에이전트/기기 핸드오프** — 대시보드를 공유 작업 표면으로. 단일 라이터/commit-as-CAS, git repo가 단일 진실 원천, live artifact는 읽기 미러.
- **§22 부록** — 용어집(Glossary) + 문서·Git 컨벤션 요약.
- **CHANGELOG.md / docs/** — 프로젝트 문서 체계를 스킬 자신에게 적용(dogfooding).

### Changed

- **§1.6 안전 게이트** 강화 — 카테고리별 경계 예시 표, "애매하면 멈춘다" 규칙.
- **§2 사용 모드** — `/handoff`, `/resume`, `/autonomy` 추가.
- **§14 / §15** — 자율 실행과 "과한 자동화 경계"를 정합화, 문서 체계 혼용 금지·강제되지 않는 메커니즘 과대주장 금지 추가.

### Verified

- 자율 실행 안전성: 독립 에이전트 RED/GREEN 행동 테스트(블래턴트·그레이존 모두 안전 게이트에서 정지 확인).
- 설계: 독립 에이전트 적대적 검토(확신도 82) 반영 — 7개 must-fix 채택.
- 상세: `docs/02-decisions/CROSS_VALIDATION_LOG.md`, `docs/04-quality/TEST_PLAN.md`.

## [1.1.0] - 2026-06-19

- Claude Code 플러그인 + 마켓플레이스로 패키징.

## [1.0.0] - 2026-06-19

- Quetzalcoatl — Meaning-First AI Project OS 스킬 최초 공개.
