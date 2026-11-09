#!/usr/bin/env python3
"""Build readable bilingual HTML pages from the Geography Markdown chapters.

Source of truth stays in geography/chapters/*.md. This script renders each
chapter to geography/read/<same-name>.html with:
  * a RU/EN switch (blocks are tagged by language; "RU / EN" headings and
    captions are split into two spans);
  * internal production sections (editorial notes, visual briefs, registers)
    left out of the learner-facing page;
  * a table of contents, previous/next navigation and responsive tables.

Usage:  python3 geography/scripts/build_reader.py
"""
import html
import json
import re
from pathlib import Path

import markdown
import warnings
from bs4 import BeautifulSoup, MarkupResemblesLocatorWarning, NavigableString, Tag
warnings.filterwarnings("ignore", category=MarkupResemblesLocatorWarning)

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "chapters"
OUT = ROOT / "read"

CYR = re.compile(r"[А-Яа-яЁё]")
LAT = re.compile(r"[A-Za-z]")
RAW_PREFIX = re.compile(
    r"https://raw\.githubusercontent\.com/Ajokendo/Atlas-of-Knowledge/[^/]+/geography/", re.I)

# Sections written for the production team, not for learners.
INTERNAL = re.compile(
    r"(примечани|editorial|brief|техническ\w* задани|visual register|реестр|production"
    r"|визуальные материалы|visual materials|статус|status|checklist|чек-лист)", re.I)
# Headings that only announce "the English text starts here".
EN_MARKER = re.compile(r"^((expanded |full )?english\b|английская версия)", re.I)

# Status notes and placeholders for illustrations that do not exist yet.
DROP_NOTE = re.compile(r"^(\[?МЕТКА ИЛЛЮСТРАЦИИ|\[?IMAGE PLACEHOLDER|Статус(?! данных)|Status(?! of data)|Production status)", re.I)

INTERNAL_TABLE = re.compile(r"(Claim checked|Проверяемое положение|Visual ID|ID визуал|QA status)", re.I)

HEADINGS = {"h1", "h2", "h3", "h4", "h5", "h6"}


def lang_of(text):
    c = len(CYR.findall(text))
    l = len(LAT.findall(text))
    if c == 0 and l == 0:
        return None
    return "ru" if c >= 0.3 * (c + l) else "en"


def split_bilingual(inner_html):
    """Split 'русский / English' markup into (ru, en); None if not bilingual."""
    # candidate split points: ' / ' outside of tags
    best = None
    depth = 0
    for i, ch in enumerate(inner_html):
        if ch == "<":
            depth += 1
        elif ch == ">":
            depth -= 1
        elif depth == 0 and (inner_html.startswith(" / ", i) or inner_html.startswith(". ", i)):
            if inner_html[i] == ".":
                left, right = inner_html[:i + 1], inner_html[i + 2:]
            else:
                left, right = inner_html[:i], inner_html[i + 3:]
            lt = BeautifulSoup(left, "html.parser").get_text()
            rt = BeautifulSoup(right, "html.parser").get_text()
            a, b = lang_of(lt), lang_of(rt)
            if {a, b} == {"ru", "en"}:
                score = abs(len(lt) - len(rt))
                if best is None or score < best[0]:
                    best = (score, left, right) if a == "ru" else (score, right, left)
    if not best:
        return None
    return best[1].strip(), best[2].strip()


def make_bilingual(soup, el):
    parts = split_bilingual(el.decode_contents())
    if not parts:
        return False
    ru, en = (re.sub(r"^\s*/\s*|\s*/\s*$", "", x) for x in parts)
    el.clear()
    for cls, frag in (("ru", ru), ("en", en)):
        span = soup.new_tag("span", attrs={"class": cls})
        span.append(BeautifulSoup(frag, "html.parser"))
        el.append(span)
    el["class"] = el.get("class", []) + ["both"]
    return True


def tag_block(soup, el):
    """Assign language classes to one top-level block."""
    if el.name in HEADINGS:
        if not make_bilingual(soup, el):
            lg = lang_of(el.get_text()) or "both"
            el["class"] = el.get("class", []) + [lg]
        return
    imgs = el.find_all("img")
    text = el.get_text(" ", strip=True)
    if imgs and len(text) < 3:
        el["class"] = el.get("class", []) + ["both", "fig"]
        for img in imgs:
            img["loading"] = "lazy"
            img["decoding"] = "async"
            alt = img.get("alt", "")
            if " / " in alt:
                ru, _, en = alt.partition(" / ")
                img["alt"] = ru.strip()
                img["data-alt-en"] = en.strip()
        return
    if el.name in ("ul", "ol"):
        langs = {lang_of(li.get_text()) for li in el.find_all("li", recursive=False)} - {None}
        if len(langs) > 1:
            for li in el.find_all("li", recursive=False):
                if not make_bilingual(soup, li):
                    li["class"] = li.get("class", []) + [lang_of(li.get_text()) or "both"]
            el["class"] = el.get("class", []) + ["both"]
            return
    if el.name == "p" and make_bilingual(soup, el):
        return
    lg = lang_of(text) or "both"
    if el.name == "table":
        c, l = len(CYR.findall(text)), len(LAT.findall(text))
        if min(c, l) > 0.25 * (c + l):
            lg = "both"
    el["class"] = el.get("class", []) + [lg]


def render(md_text):
    md_text = RAW_PREFIX.sub("../", md_text)
    body = markdown.markdown(
        md_text, extensions=["tables", "sane_lists", "attr_list", "fenced_code"],
        output_format="html5")
    soup = BeautifulSoup(body, "html.parser")
    out = []
    skip_level = None
    for el in list(soup.children):
        if isinstance(el, NavigableString):
            if el.strip():
                p = soup.new_tag("p")
                p.string = el
                el = p
            else:
                continue
        if el.name in HEADINGS:
            level = int(el.name[1])
            if skip_level is not None and level <= skip_level:
                skip_level = None
            if skip_level is None and level >= 2 and INTERNAL.search(el.get_text()):
                skip_level = level
            if skip_level is None and EN_MARKER.search(el.get_text().strip()):
                continue
        if skip_level is not None:
            continue
        if el.name == "hr":
            continue
        if el.name == "table" and INTERNAL_TABLE.search(el.get_text(" ", strip=True)[:300]):
            continue
        if el.name == "blockquote" and DROP_NOTE.search(el.get_text(" ", strip=True)[:60]):
            continue
        tag_block(soup, el)
        if el.name == "table":
            wrap = soup.new_tag("div", attrs={"class": "tableWrap " + " ".join(
                c for c in el.get("class", []) if c in ("ru", "en", "both"))})
            el.wrap(wrap)
            el = wrap
        out.append(el)
    # ids for headings
    used = set()
    for i, el in enumerate(out):
        if el.name in ("h2", "h3"):
            base = "s" + str(i)
            el["id"] = base
            used.add(base)
    # external links open in new tab
    for el in out:
        for a in el.find_all("a", href=True):
            if a["href"].startswith("http"):
                a["target"] = "_blank"
                a["rel"] = "noopener"
    return "\n".join(str(e) for e in out)


def chapter_titles(md_text):
    ru = en = ""
    for line in md_text.splitlines()[:6]:
        if line.startswith("# "):
            t = line[2:].strip()
            if lang_of(t) == "ru" and not ru:
                ru = t
            elif lang_of(t) == "en" and not en:
                en = t
    return ru, en or ru


PAGE = """<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title_ru} — Атлас географии</title>
<link rel="stylesheet" href="reader.css">
</head>
<body data-lang="ru">
<header class="top">
  <nav class="crumbs"><a href="../../portal.html">Atlas of Knowledge</a><span>/</span><a href="../index.html"><span class="ru">География</span><span class="en">Geography</span></a></nav>
  <button class="langBtn" id="langBtn" type="button" aria-label="Switch language">EN</button>
</header>
<div class="layout">
  <aside class="toc" id="toc" aria-label="Содержание главы"></aside>
  <main class="chapter">
    <p class="eyebrow"><span class="ru">Атлас географии · Глава {num}</span><span class="en">Atlas of Geography · Chapter {num}</span></p>
    <article id="article">
{body}
    </article>
    <nav class="pager">{prev}{next}</nav>
  </main>
</div>
<script>window.CHAPTER_TITLES={titles};</script>
<script src="reader.js"></script>
</body>
</html>
"""


def pager_link(info, cls, label_ru, label_en):
    if not info:
        return "<span></span>"
    return (f'<a class="{cls}" href="{info["file"]}"><small><span class="ru">{label_ru}</span>'
            f'<span class="en">{label_en}</span></small>'
            f'<span class="ru">{html.escape(info["ru"])}</span><span class="en">{html.escape(info["en"])}</span></a>')


def main():
    OUT.mkdir(exist_ok=True)
    files = sorted(SRC.glob("[0-9][0-9]-*.md"))
    infos = []
    for f in files:
        txt = f.read_text(encoding="utf-8")
        ru, en = chapter_titles(txt)
        infos.append({"src": f, "file": f.stem + ".html", "ru": ru, "en": en, "num": f.name[:2]})
    for i, info in enumerate(infos):
        txt = info["src"].read_text(encoding="utf-8")
        body = render(txt)
        prev = pager_link(infos[i - 1] if i else None, "prev", "← Предыдущая глава", "← Previous chapter")
        nxt = pager_link(infos[i + 1] if i + 1 < len(infos) else None, "next", "Следующая глава →", "Next chapter →")
        page = PAGE.format(title_ru=html.escape(info["ru"]), num=info["num"], body=body,
                           prev=prev, next=nxt,
                           titles=json.dumps({"ru": info["ru"], "en": info["en"]}, ensure_ascii=False))
        (OUT / info["file"]).write_text(page, encoding="utf-8")
    print(f"Built {len(infos)} chapter pages into {OUT.relative_to(ROOT.parent)}")


if __name__ == "__main__":
    main()
