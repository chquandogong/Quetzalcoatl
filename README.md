# 🪶 Quetzalcoatl — Meaning-First AI Project OS

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
`/dashboard`, `/ship`, `/retro` …
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
├── README.md
└── LICENSE
```

## 라이선스

MIT — [`LICENSE`](./LICENSE) 참고.
