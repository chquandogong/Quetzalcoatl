# Quetzalcoatl 사용법

`/Quetzalcoatl` 한 번으로 "Meaning-First AI Project OS" 전체를 호출하는 **모델 중립형** 스킬이다.
의미·가치 검증 → GarryTan Office Hours → feasibility → 3~5개 대안 → Claude-GPT 교차검증 →
문서·대시보드 → Ship → 회고까지 하나의 워크플로우로 운영한다.

## Claude Code

### 1) 플러그인으로 설치 (권장)

```text
/plugin marketplace add chquandogong/Quetzalcoatl
/plugin install quetzalcoatl@quetzalcoatl
```

새 세션을 시작하면 **플러그인 네임스페이스** 명령으로 호출한다.

```text
/quetzalcoatl:Quetzalcoatl
```

```text
/quetzalcoatl:Quetzalcoatl 아래 아이디어를 의미 검토부터 배포까지 운영해줘. [아이디어]
```

> 플러그인 캐시는 **버전별 사본**이라, GitHub에 새 버전이 올라가도 자동 반영되지 않는다.
> 최신으로 올리려면 `marketplace update` 후 재설치한다(자세히는 `docs/05-ops/RUNBOOK.md`).

### 2) 개인 스킬로 설치 (수동)

```bash
git clone https://github.com/chquandogong/Quetzalcoatl /tmp/quetzalcoatl-src
cp -r /tmp/quetzalcoatl-src/skills/Quetzalcoatl ~/.claude/skills/Quetzalcoatl
```

개인 스킬로 두면 네임스페이스 없이 `/Quetzalcoatl`로 호출된다(새 세션 필요).

### 세부 단계(하위 모드) 호출

세부 단계로 바로 가고 싶으면 하위 모드를 쓴다: `/office-hours`, `/feasibility`,
`/alternatives`, `/cross-check`, `/spec`, `/plan`, `/risk-review`, `/test-plan`,
`/dashboard`, `/ship`, `/retro`, `/handoff`, `/resume`, `/autonomy` … (전체는 `SKILL.md` §2)

> ⚠️ 하위 모드는 **Claude Code에 등록된 별도 슬래시 명령이 아니라** `SKILL.md` §2에 정의된
> "모드"다. 따라서 슬래시 자동완성 메뉴에는 마스터(`/quetzalcoatl:Quetzalcoatl`)만 보인다.
> 스킬이 켜진 세션에서 `/dashboard`처럼 그냥 입력하면(앞의 `/`는 관례, 없어도 됨) 해당 모드로
> 전환된다. 명령을 정확히 쓰지 않아도 의도가 비슷하면 자동 적용된다.

## ChatGPT / GPT

이 스킬은 모델 중립형이다. 다음 중 하나로 사용한다.

1. ChatGPT 프로젝트 지침에 `SKILL.md` 내용을 붙여넣기
2. GPT Builder의 Instructions에 붙여넣기
3. ChatGPT Skills 업로드 기능이 있는 환경에서는 이 폴더를 zip으로 업로드
4. 일반 채팅에서는 `SKILL.md` 전체를 첫 메시지 또는 프로젝트 설명으로 붙여넣기

> 슬래시 명령이 없는 환경에서는 `SKILL.md` 내용을 프로젝트 지침/문맥에 붙여넣고 아래 문장으로 호출한다.

## 추천 첫 호출

```text
/quetzalcoatl:Quetzalcoatl 아래 아이디어를 의미 검토 → GarryTan Office Hours → feasibility →
대안 3~5개 → Claude-GPT 교차검증 프롬프트 → 대시보드 초안 순서로 처리해줘.

[아이디어 입력]
```

> 개인 스킬·ChatGPT 등 네임스페이스가 없는 환경에서는 `/Quetzalcoatl`로 호출한다.
