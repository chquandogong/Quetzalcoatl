# 🪶 Quetzalcoatl — Meaning-First AI Project OS

> `/Quetzalcoatl` 한 번으로 켜지는 **의미 우선 AI 프로젝트 운영체제** 스킬. 바로 만들지 않고 의미부터 검증한 뒤, 조사·기획·설계·구현·검증·배포·회고까지 한 워크플로우로 운영한다. 모델 중립(Claude · Claude Code · ChatGPT/GPTs · 일반 LLM 에이전트).

**현재 버전 v3.3.0** (2026-10-27) · [저장소](https://github.com/chquandogong/Quetzalcoatl) · [릴리스](https://github.com/chquandogong/Quetzalcoatl/releases) · [CHANGELOG](https://github.com/chquandogong/Quetzalcoatl/blob/main/CHANGELOG.md)

## 한 문장으로

AI는 사용자의 의도를 반사하고 증폭하는 거울 같은 실행 파트너다. **방향·책임·최종 판단은 사람이 가진다.** 이 스킬은 그 경계를 지키면서 AI의 조사력·생성력·비평력·실행력을 조직화한다.

## 무엇이 다른가

| 흔한 실패 | 이 스킬의 답 | 어디에 |
| --- | --- | --- |
| 요청을 그대로 만든다 | 먼저 **왜 중요한가 · 누구에게 가치인가 · 안 하면 무엇이 남는가**를 묻고, 가장 작은 쐐기부터 | [원칙](Principles) · [워크플로우](Workflow) |
| 사용자 선호에 맹종하거나, 반대로 멋대로 바꾼다 | 선호는 **기본값(prior)** — 근거가 이길 때만 투명하게 뒤집고, 근소하면 유지. 같은 전제 안에 갇히면 프레이밍을 흔든다 | [워크플로우](Workflow) · [설계 의도](Design-Intent) |
| 모델 둘이 같은 말을 하면 맞다고 믿는다 | **AI끼리의 합의는 검증이 아니다.** 근거·데이터·테스트·실행 결과·사람 판단으로 검증 | [교차검증](Cross-Validation) |
| "테스트 통과"를 "동작함"으로 읽는다 | 실제 산출물을 사용자 경로로 구동해 기대와 관측을 대조하는 **검증표**, 증거는 검사한 범위까지만 | [검증표](Verification-Map) |
| 자율 실행이 위험한 일까지 해 버린다 | 자율은 확인 질문을 줄일 뿐 — 외부 발송·결제·삭제·배포·공개는 **사람 승인 게이트** | [자율과 게이트](Autonomy-and-Gates) |
| 결정이 대화 속에 묻힌다 | 결정 로그·가정·리스크·대시보드로 **판단을 추적 가능하게** | [문서 체계](Documentation-System) |

## 바로 시작

1. [설치](Installation) — Claude Code 플러그인 2줄, 개인 스킬, 또는 챗 환경용 페이스트 번들.
2. [빠른 시작](Quick-Start) — 첫 호출 문장 3개와 첫 응답이 어떻게 생겼는지.
3. [모드](Modes) — `/office-hours`부터 `/retro`까지 22개 입구.

## 페이지 지도

- 개념: [원칙](Principles) · [워크플로우](Workflow) · [설계 의도](Design-Intent)
- 운영: [교차검증](Cross-Validation) · [문서 체계](Documentation-System) · [명세·계획·리뷰](Spec-Plan-Review) · [검증표](Verification-Map) · [자율과 게이트](Autonomy-and-Gates)
- 참조(생성물): [모드](Modes) · [템플릿 C-1~C-29](Templates) · [용어집](Glossary) · [릴리스 이력](Release-History)
- [FAQ](FAQ)

## 이 위키의 지위

정본은 저장소의 [`SKILL.md`](https://github.com/chquandogong/Quetzalcoatl/blob/main/skills/Quetzalcoatl/SKILL.md)(규칙 §0~§24)와 [`TEMPLATES.md`](https://github.com/chquandogong/Quetzalcoatl/blob/main/skills/Quetzalcoatl/TEMPLATES.md)(양식 C-1~C-29)다. 이 위키는 그 **파생 뷰**로, 저장소의 `wiki/` 디렉터리에서 관리하고 `scripts/publish-wiki.sh`로 발행한다. 둘이 갈리면 정본이 이긴다(스킬 자신의 §6.4 규칙).
