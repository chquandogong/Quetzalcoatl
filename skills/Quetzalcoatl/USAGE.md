# Quetzalcoatl 사용법 (v3.3.0)

`/Quetzalcoatl` 한 번으로 "Meaning-First AI Project OS" 전체를 호출하는 **모델 중립형** 스킬이다. 이 폴더의 `SKILL.md`(규칙 §0~§24)와 `TEMPLATES.md`(양식 C-1~C-29)는 **한 세트**다. 개념 설명은 [Wiki](https://github.com/chquandogong/Quetzalcoatl/wiki)에 있다.

## 1. 설치

### Claude Code — 플러그인 (권장)

```text
/plugin marketplace add chquandogong/Quetzalcoatl
/plugin install quetzalcoatl@quetzalcoatl
```

새 세션에서 **플러그인 네임스페이스**로 호출한다.

```text
/quetzalcoatl:Quetzalcoatl 아래 아이디어를 의미 검토부터 배포까지 운영해줘. [아이디어]
```

### Claude Code · Codex CLI — 개인 스킬

```bash
git clone https://github.com/chquandogong/Quetzalcoatl /tmp/quetzalcoatl-src
cp -r /tmp/quetzalcoatl-src/skills/Quetzalcoatl ~/.claude/skills/Quetzalcoatl   # Claude Code
cp -r /tmp/quetzalcoatl-src/skills/Quetzalcoatl ~/.codex/skills/Quetzalcoatl    # Codex CLI
```

네임스페이스 없이 `/Quetzalcoatl`로 호출된다(새 세션 필요). 폴더째 복사해야 `TEMPLATES.md`가 같이 간다.

### ChatGPT · GPTs · 일반 LLM — 페이스트 번들

도구 없는 챗 환경에는 본문+양식 합본 [`dist/Quetzalcoatl-FULL.md`](../../dist/Quetzalcoatl-FULL.md)를 쓴다. 프로젝트 지침 또는 GPT Builder Instructions에 붙여넣거나, 일반 채팅의 첫 메시지로 붙여넣는다. 스킬 업로드를 지원하면 이 폴더를 zip으로 올린다.

## 2. 호출

### 마스터 모드

```text
/quetzalcoatl:Quetzalcoatl [요청]
```

의미 검증 → Office Hours → feasibility → 대안 → 교차검증 → 문서·대시보드 → Spec/Plan → 구현 → 검증표 → Ship → Retro를 순서대로 적용한다. 요청 크기에 따라 형식을 줄인다(§13): 간단한 질문은 바로 답하고, 중간 작업은 목표·가정·리스크 1~3줄 뒤 바로 실행한다.

### 하위 모드

세부 단계로 바로 가려면 모드를 쓴다: `/office-hours` `/feasibility` `/alternatives` `/agent-team` `/cross-check` `/spec` `/plan` `/design-review` `/eng-review` `/risk-review` `/test-plan` `/dashboard` `/decision-log` `/report` `/present` `/ship` `/retro` `/handoff` `/resume` `/autonomy` `/context`.

> ⚠️ 하위 모드는 **Claude Code에 등록된 별도 슬래시 명령이 아니라** `SKILL.md` §2의 모드다. 자동완성에는 마스터만 보인다. 스킬이 켜진 세션에서 `/dashboard`처럼 입력하면(앞의 `/`는 관례) 전환되고, 정확히 쓰지 않아도 의도가 비슷하면 적용된다.

### 자주 쓰는 세션 세 가지

| 상황         | 호출                                    | 무엇이 일어나나                                                                                                                         |
| ------------ | --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| 새 아이디어  | `/quetzalcoatl:Quetzalcoatl [아이디어]` | 첫 응답 미니 템플릿(목표·핵심 질문·전제·대안·첫 단계) → Office Hours → feasibility → 대안·교차검증 → 대시보드                           |
| 긴 자율 작업 | `… 이 계획대로 묻지 말고 끝까지 진행해` | 허용목록(C-19)을 세우고 가역 작업은 확인 없이 연속 실행. 외부 발송·결제·삭제·배포·공개 등 게이트는 멈추고 결정 대기에 올린다            |
| 검증·배포    | `/test-plan` → `/ship`                  | 검증표(`VERIFY.md`, C-29)를 만들고 실제 사용자 경로로 구동해 증거를 남긴 뒤, 완료 상태(검증됨/PR 열림/병합됨/배포됨)를 구분해 배포 판단 |

## 3. 환경별 강등

파일·git·live artifact가 없는 환경에서는 같은 규율을 **텍스트로** 수행한다 — 문서는 같은 이름의 마크다운을 출력, git 대신 변경 요약·체크포인트 메모, 대시보드는 붙여넣는 텍스트, 자율 루프는 "작업 큐 + 실행/정지 판정 + 가정"의 연속 출력. 교차검증에 다른 모델을 쓸 수 없으면 같은 모델 안에서 반박 관점을 시뮬레이션하고 **"실제 교차검증 아님"**을 표시한다.

## 4. 업데이트와 문제 해결

| 증상                | 원인                        | 조치                                                                                                                    |
| ------------------- | --------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| 새 버전이 안 보임   | 플러그인 캐시는 버전별 사본 | `/plugin marketplace update quetzalcoatl` → 재설치(또는 `claude plugin update quetzalcoatl@quetzalcoatl`) → 세션 재시작 |
| 재설치했는데 구버전 | 마켓플레이스 클론이 stale   | `git -C ~/.claude/plugins/marketplaces/quetzalcoatl merge --ff-only origin/main` 뒤 업데이트 재실행                     |
| 템플릿을 못 찾는다  | `SKILL.md`만 복사됨         | 폴더째 복사(`TEMPLATES.md` 동반). 둘 다 없으면 §22 색인이 최소 명세 — 즉석 생성                                         |
| 자율 중 멈춤        | 게이트 또는 허용목록 밖     | 의도된 동작. 사전승인 범위(대상·환경·행동·데이터·비용)를 허용목록에 적어 승인하면 멈추지 않는다                         |
| 버전 확인           | —                           | `grep '^version:' SKILL.md` · 플러그인은 캐시 디렉터리 이름                                                             |

운영 절차(배포·롤백·검증)는 저장소의 [`docs/05-ops/RUNBOOK.md`](../../docs/05-ops/RUNBOOK.md).
