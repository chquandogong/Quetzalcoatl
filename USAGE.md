# Quetzalcoatl 사용법

`/Quetzalcoatl`로 "Meaning-First AI Project OS" 전체를 호출하는 모델 중립형 스킬이다.

## Claude Code

설치 위치 (개인 스킬):

```bash
~/.claude/skills/Quetzalcoatl/SKILL.md
```

설치 후 세션을 새로 시작하면 슬래시 명령으로 스킬 전체를 호출한다.

```text
/Quetzalcoatl
```

```text
/Quetzalcoatl 아래 아이디어를 의미 검토부터 배포까지 운영해줘. [아이디어]
```

세부 단계만 바로 부르고 싶으면 하위 모드를 함께 쓴다.

```text
/Quetzalcoatl GarryTan 오피스아워로 이 아이디어를 압박 검토해줘.
```

```text
/Quetzalcoatl Claude-GPT 교차검증 프롬프트까지 만들어줘.
```

> 슬래시 명령이 없는 환경에서는 `SKILL.md` 내용을 프로젝트 지침/문맥에 붙여넣고 위 문장으로 호출한다.

## ChatGPT / GPT

이 스킬은 모델 중립형이다. 다음 중 하나로 사용한다.

1. ChatGPT 프로젝트 지침에 `SKILL.md` 내용을 붙여넣기
2. GPT Builder의 Instructions에 붙여넣기
3. ChatGPT Skills 업로드 기능이 있는 환경에서는 이 폴더를 zip으로 업로드
4. 일반 채팅에서는 `SKILL.md` 전체를 첫 메시지 또는 프로젝트 설명으로 붙여넣기

## 추천 첫 호출

```text
/Quetzalcoatl 아래 아이디어를 의미 검토 → GarryTan Office Hours → feasibility → 대안 3~5개 → Claude-GPT 교차검증 프롬프트 → 대시보드 초안 순서로 처리해줘.

[아이디어 입력]
```
