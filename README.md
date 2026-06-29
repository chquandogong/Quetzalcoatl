# 🪶 Quetzalcoatl — Meaning-First AI Project OS

[![release](https://img.shields.io/github/v/release/chquandogong/Quetzalcoatl?sort=semver)](https://github.com/chquandogong/Quetzalcoatl/releases)
[![license](https://img.shields.io/github/license/chquandogong/Quetzalcoatl)](./LICENSE)
![model-neutral](https://img.shields.io/badge/model-neutral-blueviolet)
![docs](https://img.shields.io/badge/docs-dogfooded-success)

`/Quetzalcoatl` 한 번으로 켜지는 **의미 우선(Meaning-First) AI 프로젝트 운영체제** 스킬.
아이디어를 "바로 실행"하기 전에 의미·가치부터 검증하고, GarryTan식 Office Hours 압박 검토 →
feasibility → 3~5개 대안 → Claude-GPT 교차검증 → 문서화·대시보드 → Ship → 회고까지
하나의 반복 가능한 워크플로우로 운영한다.

> AI 시대의 실력은 AI에게 일을 많이 시키는 능력이 아니라,
> AI가 올바른 일을 올바른 기준으로 하게 만드는 능력이다.

## 무엇을 하나

- **의미 검증 먼저, 실행은 나중** — 왜 중요한가, 누구에게 가치인가, 안 하면 무엇이 남는가
- **GarryTan Office Hours** — 진짜 문제와 가장 작은 쐐기(wedge)를 찾는 압박 검토
- **Feasibility** — Desirability / Feasibility / Viability / Risk 4축 점수화
- **3~5개 대안 비교** — 되돌리기 어려운 결정에는 항상 대안과 기준표
- **Claude-GPT 교차검증** — 모델 합의가 아니라 근거로 판단
- **문서화 & 대시보드** — 결정 로그, 리스크 레지스터, 진행 대시보드
- **사람 승인 게이트** — 외부 발송·결제·배포·삭제 등 비가역 작업은 사람이 결정
- **지속 자율 실행 (v1.2.0)** — 승인된 계획 범위 안에서 확인 질문 없이 끝까지 실행(안전 게이트는 유지)
- **레이트리밋·재개 회복력 (v1.2.0)** — 한도/중단에도 커밋 체크포인트에서 무손실 재개
- **체계적 문서·Git (v1.2.0)** — 표준 디렉터리 구조, Conventional Commits, SemVer 태그
- **교차 에이전트/기기 핸드오프 (v1.2.0)** — 대시보드를 공유 작업 표면으로(데스크탑 ↔ 모바일)
- **앵커된 선호 처리 (v1.3.0)** — 사용자 선호를 기본값으로 존중하되, 근거가 이기면 투명하게 뒤집는다(§4.2 — 맹종도 독단도 아닌 중도)
- **대시보드 HTML 미러 + `/dashboard` (v1.4.0)** — 정본(`DASHBOARD.md`)은 SSOT, 보기 좋은 HTML 미러를 같은 URL에 redeploy(읽기용 · §7.2)
- **강제 바인딩 + 증거기반 완료 (v1.5.0)** — 환경이 제공하면 게이트·체크포인트·하위 범위를 승인 훅 등에 바인딩(규율→강제, 있을 때만; 없으면 규율), 완료는 증거로 증명(§18.7·§12·§14). 외부 도구(Claude Code·Codex·Antigravity) 역량은 [capability matrix](./docs/appendix/CAPABILITY_MATRIX.md)로 관리
- **벤더-중립 휴대용 브리핑 `/context` (v1.6.0)** — 프로젝트 맥락을 1회성 벤더-중립 브리핑으로 합성해 새 에이전트/벤더(Claude·Codex·Gemini·ChatGPT)에 즉시 온보딩(§24; `/handoff`와 구분 — 보드 갱신이 아니라 휴대용 산출물)
- **Core Contract 분리 (v2.0.0)** — 본문=규칙, fill-in 템플릿 21개는 §22 부록 C로 이동(코어 전진배치·준수↑). 동작·모드·게이트·모델 중립 불변(구조 재편)

## 설치 (Claude Code)

### 1) 플러그인으로 설치 (권장)

```text
/plugin marketplace add chquandogong/Quetzalcoatl
/plugin install quetzalcoatl@quetzalcoatl
```

### 2) 개인 스킬로 설치 (수동)

```bash
git clone https://github.com/chquandogong/Quetzalcoatl /tmp/quetzalcoatl-src
cp -r /tmp/quetzalcoatl-src/skills/Quetzalcoatl ~/.claude/skills/Quetzalcoatl
```

세션을 새로 시작하면 `/Quetzalcoatl`로 호출된다.

## 사용

```text
/Quetzalcoatl 아래 아이디어를 의미 검토부터 배포까지 운영해줘. [아이디어]
```

세부 단계는 하위 모드로 바로 호출할 수 있다: `/office-hours`, `/feasibility`,
`/alternatives`, `/cross-check`, `/spec`, `/plan`, `/risk-review`, `/test-plan`,
`/dashboard`, `/ship`, `/retro`, `/handoff`, `/resume`, `/autonomy` …
전체 모드는 [`SKILL.md`](./skills/Quetzalcoatl/SKILL.md) §2, 자세한 사용법은
[`USAGE.md`](./skills/Quetzalcoatl/USAGE.md) 참고.

## 호환성

Claude / Claude Code / Claude Projects · ChatGPT / GPTs / ChatGPT Skills ·
일반 LLM 채팅 및 코딩 에이전트 — 모델 중립형.
(ChatGPT 등에서는 `skills/Quetzalcoatl/SKILL.md` 전체를 프로젝트 지침에 붙여넣는다.)

## 구조

```
Quetzalcoatl/
├── .claude-plugin/
│   ├── marketplace.json   # Claude Code 마켓플레이스 정의
│   └── plugin.json        # 플러그인 매니페스트
├── skills/
│   └── Quetzalcoatl/
│       ├── SKILL.md        # 스킬 본문 (운영체제 전체)
│       └── USAGE.md        # 호출/설치 가이드
├── docs/                   # 이 스킬을 자신에게 적용한 프로젝트 문서 (§6 구조)
│   ├── 00-overview/        # PROJECT_BRIEF · DASHBOARD
│   ├── 01-discovery/       # OFFICE_HOURS · FEASIBILITY · ASSUMPTIONS
│   ├── 02-decisions/       # DECISION_LOG · ALTERNATIVES · CROSS_VALIDATION_LOG
│   ├── 03-spec/            # SPEC
│   ├── 04-quality/         # RISK_REGISTER · TEST_PLAN
│   ├── 05-ops/             # RUNBOOK · RETRO
│   ├── appendix/           # GLOSSARY · CONVENTIONS
│   └── assets/             # 대시보드 HTML 미러(렌더)
├── CHANGELOG.md
├── README.md
└── LICENSE
```

## 라이선스

MIT — [`LICENSE`](./LICENSE) 참고.
