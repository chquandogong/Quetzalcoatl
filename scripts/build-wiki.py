#!/usr/bin/env python3
"""wiki/ 생성 페이지 빌더 — SKILL.md · TEMPLATES.md · CHANGELOG.md(정본)에서 파생 뷰를 만든다.

생성 대상(손으로 고치지 않는다 — 이 스크립트가 출처):
  wiki/Modes.md            ← SKILL.md §2 모드 표
  wiki/Templates.md        ← SKILL.md §22 부록 C 색인 + TEMPLATES.md 앵커
  wiki/Glossary.md         ← SKILL.md §22 부록 A 용어집
  wiki/Release-History.md  ← CHANGELOG.md 버전 헤더 + 첫 단락
사용:  python3 scripts/build-wiki.py [--check]   (--check: 생성 결과가 wiki/와 다르면 exit 1)
"""
import io, os, re, sys, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARGS = sys.argv[1:]
CHECK = "--check" in ARGS
OUT = os.path.join(ROOT, "wiki")
if "--out" in ARGS:
    OUT = os.path.abspath(ARGS[ARGS.index("--out") + 1])
if CHECK:
    import tempfile
    OUT = tempfile.mkdtemp(prefix="wiki-check-")
os.makedirs(OUT, exist_ok=True)
GENERATED = ("Modes.md", "Templates.md", "Glossary.md", "Release-History.md")
def write(name, content):
    io.open(os.path.join(OUT, name), "w", encoding="utf-8").write(content)
S = io.open(os.path.join(ROOT, "skills/Quetzalcoatl/SKILL.md"), encoding="utf-8").read()
T = io.open(os.path.join(ROOT, "skills/Quetzalcoatl/TEMPLATES.md"), encoding="utf-8").read()
C = io.open(os.path.join(ROOT, "CHANGELOG.md"), encoding="utf-8").read()
VER = json.load(io.open(os.path.join(ROOT, ".claude-plugin/plugin.json"), encoding="utf-8"))["version"]
SKILL_URL = "https://github.com/chquandogong/Quetzalcoatl/blob/main/skills/Quetzalcoatl/SKILL.md"
TPL_URL = "https://github.com/chquandogong/Quetzalcoatl/blob/main/skills/Quetzalcoatl/TEMPLATES.md"
CL_URL = "https://github.com/chquandogong/Quetzalcoatl/blob/main/CHANGELOG.md"

def section(text, start_pat, end_pat):
    a = re.search(start_pat, text, re.M); assert a, start_pat
    b = re.search(end_pat, text[a.end():], re.M)
    return text[a.end(): a.end() + b.start()] if b else text[a.end():]

def table_rows(block):
    rows = [l for l in block.split("\n") if l.startswith("|")]
    return [r for r in rows if not re.match(r"^\|\s*-", r)]

def cells(row):
    return [c.strip() for c in row.strip().strip("|").split("|")]

footer = f"\n\n---\n\n> 이 페이지는 **생성물**이다(`scripts/build-wiki.py`, v{VER} 기준). 정본은 [`SKILL.md`]({SKILL_URL})·[`TEMPLATES.md`]({TPL_URL})·[`CHANGELOG.md`]({CL_URL}) — 고치려면 정본을 고친 뒤 다시 생성한다.\n"

# --- Modes ---
blk = section(S, r"^## 2\. 사용 모드\s*$", r"^---\s*$")
rows = table_rows(blk)
hdr, body = rows[0], rows[1:]
out = [f"# 모드 (§2) — v{VER}", "",
       "`/Quetzalcoatl` 하나가 전체 워크플로우를 켜는 **마스터 명령**이고, 아래 하위 모드는 그 안의 단계로 바로 들어가는 입구다. 모드는 Claude Code에 등록된 별도 슬래시 명령이 아니라 **스킬 본문 §2의 약속**이다 — 스킬이 켜진 세션에서 `/office-hours`처럼 쓰면 그 단계로 전환되고, 명령을 정확히 쓰지 않아도 의도가 비슷하면 적용된다.", "",
       "| 모드 | 목적 |", "| --- | --- |"]
for r in body:
    c = cells(r)
    if len(c) >= 2: out.append(f"| {c[0]} | {c[1]} |")
# trailing note (blockquote) in §2
note = [l for l in blk.split("\n") if l.startswith(">")]
if note: out += ["", *note]
write("Modes.md", "\n".join(out) + footer)

# --- Templates ---
idx_blk = section(S, r"^### 부록 C\. 템플릿 모음", r"^---\s*$")
rows = [r for r in table_rows(idx_blk) if re.match(r"^\| C-\d+ ", r)]
# TEMPLATES.md anchors: "#### C-N. Title (§...)"
anchors = {}
for m in re.finditer(r"^#### (C-(\d+))\. (.+?)\s*$", T, re.M):
    title = m.group(3)
    slug = re.sub(r"[^\w\- ]", "", f"{m.group(1)} {title}".lower()).strip().replace(" ", "-")
    anchors[m.group(1)] = (title, slug)
out = [f"# 템플릿 C-1~C-{len(anchors)} (§22 부록 C) — v{VER}", "",
       f"규칙(본문)이 쓰는 **양식**은 [`TEMPLATES.md`]({TPL_URL})에 있다. 에이전트 환경에서는 필요한 C-N만 그때 읽고(규율), 도구 없는 챗 환경에서는 페이스트 번들 끝에 전부 포함된다. 템플릿 파일도 번들도 없으면 아래 색인의 이름과 \"쓰는 절\"이 최소 명세다(즉석 생성).", "",
       "| 색인 | 템플릿 | 쓰는 절 | 파일 위치 |", "| --- | --- | --- | --- |"]
for r in rows:
    c = cells(r)
    cid = c[0]
    title, slug = anchors.get(cid, (c[1], ""))
    link = f"[{cid}]({TPL_URL}#{slug})" if slug else cid
    out.append(f"| {link} | {c[1]} | {c[2]} | `TEMPLATES.md` `#### {cid}.` |")
write("Templates.md", "\n".join(out) + footer)

# --- Glossary ---
g_blk = section(S, r"^### 부록 A\. 용어집", r"^### 부록 B")
rows = table_rows(g_blk)
out = [f"# 용어집 (§22 부록 A) — v{VER}", "",
       "스킬 용어의 정본은 본문 부록 A다. 프로젝트별 보조 용어는 각 프로젝트의 `docs/appendix/GLOSSARY.md`에 둔다(원천은 하나, 배포본에는 필요한 정의만 복사 — §6.2).", "",
       "| 용어 | 뜻 |", "| --- | --- |"]
for r in rows[1:]:
    c = cells(r)
    if len(c) >= 2: out.append(f"| {c[0]} | {c[1]} |")
write("Glossary.md", "\n".join(out) + footer)

# --- Release history ---
entries = re.findall(r"^## \[(\d+\.\d+\.\d+)\] - (\d{4}-\d{2}-\d{2})\s*\n\n(.+?)\n", C, re.M)
out = [f"# 릴리스 이력 — 최신 v{VER}", "",
       f"각 항목의 첫 문장만 모았다. 전문(Added / Changed / Verified / Note)은 [`CHANGELOG.md`]({CL_URL}), 릴리스 노트는 [GitHub Releases](https://github.com/chquandogong/Quetzalcoatl/releases).", "",
       "| 버전 | 날짜 | 한 줄 |", "| --- | --- | --- |"]
for v, d, first in entries:
    first = re.sub(r"\s+", " ", first).strip()
    m = re.match(r"\*\*(.+?)\*\*", first)
    one = m.group(1) if m else re.sub(r"^-\s*", "", first)[:140]
    out.append(f"| [v{v}](https://github.com/chquandogong/Quetzalcoatl/releases/tag/v{v}) | {d} | {one} |")
write("Release-History.md", "\n".join(out) + footer)
if CHECK:
    import filecmp
    stale = [n for n in GENERATED if not filecmp.cmp(os.path.join(OUT, n), os.path.join(ROOT, "wiki", n), shallow=False)]
    if stale:
        print("wiki 생성 페이지 stale:", ", ".join(stale), "— python3 scripts/build-wiki.py 재실행 후 커밋"); sys.exit(1)
    print("OK: wiki 생성 페이지 신선 (", ", ".join(GENERATED), ")")
else:
    print(f"built {OUT}: Modes.md ({len(body)} modes) · Templates.md · Glossary.md · Release-History.md ({len(entries)} releases)")
