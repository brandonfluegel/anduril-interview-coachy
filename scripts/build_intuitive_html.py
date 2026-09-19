"""Render an Intuitive interview doc into a print-ready HTML file.

Run: python scripts/build_intuitive_html.py [guide|screen|all]
Output: intuitive/print/*.html — open in a browser and Ctrl+P.

Print layout is two-column at ~9.8pt.
"""

from __future__ import annotations

import html
import re
import sys
from pathlib import Path

from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "intuitive" / "print"

# break_before_part1 costs up to a page, so the short screen doc runs continuous.
DOCS = {
    "guide": {
        "src": ROOT / "intuitive" / "intuitive-interview-guide.md",
        "out": OUT / "intuitive-interview-guide.html",
        "title": "Intuitive Surgical — Senior Human Factors Analyst",
        "break_before_part1": True,
        "body_class": "",
    },
    "screen": {
        "src": ROOT / "intuitive" / "technical-screen-guide.md",
        "out": OUT / "technical-screen-guide.html",
        "title": "Intuitive Surgical — Technical Round",
        "break_before_part1": False,
        "body_class": "compact",
        # Spanning headings leave more partial columns, so beats must break more readily.
        "flow_chars": 300,
    },
}

CSS = """
:root { color-scheme: light; }
* { box-sizing: border-box; }
body {
  font-family: Georgia, "Times New Roman", serif;
  font-size: 12pt; line-height: 1.55; color: #111;
  background: #f4f4f2; margin: 0; padding: 2rem 1rem 4rem;
}
main {
  max-width: 44em; margin: 0 auto; background: #fff;
  padding: 3rem 3.25rem; box-shadow: 0 1px 4px rgba(0,0,0,.12);
}
h1, h2, h3, h4 { font-family: Helvetica, Arial, sans-serif; line-height: 1.25; }
h1 { font-size: 1.7rem; margin: 0 0 .3em; }
h2 { font-size: 1.28rem; margin: 2.2em 0 .5em; padding-top: .45em; border-top: 2px solid #111; }
h3 { font-size: 1.05rem; margin: 1.6em 0 .4em; }
h4 { font-size: .95rem; margin: 1.3em 0 .3em; color: #333; }
p, li { orphans: 3; widows: 3; }

/* The three blockquote kinds are the whole navigation system of this document. */
blockquote { margin: .8em 0; padding: .3em 0 .3em 1em; border-left: 3px solid #555; }
blockquote.say { background: #f1f1ef; border-left-color: #222; padding: .6em .9em; }
blockquote.warn { background: #fdf8ea; border: 1px dashed #8a6d1f; border-left-width: 4px; padding: .55em .9em; }
blockquote.note { background: #eef3f7; border-left-color: #35637f; padding: .55em .9em; }
blockquote p { margin: .35em 0; }

/* The model answer is what gets memorized: numbered beats, chunked, never split. */
.answer {
  background: #fafaf9; border-left: 4px solid #222;
  padding: .55em 1.1em; margin: .9em 0 1.1em;
  counter-reset: beat;
}
.answer p { margin: 0; padding: .55em 0; counter-increment: beat; }
.answer p + p { border-top: 1px solid #e4e4de; }
.answer p > strong:first-child {
  display: block; font-family: Helvetica, Arial, sans-serif;
  font-size: .7em; text-transform: uppercase; letter-spacing: .09em;
  color: #6a6a6a; margin-bottom: .2em;
}
.answer p > strong:first-child::before {
  content: counter(beat); display: inline-block; width: 1.4em; color: #b0b0a8;
}

table { border-collapse: collapse; width: 100%; font-size: .87rem; margin: 1em 0; }
th, td { border: 1px solid #999; padding: 5px 8px; text-align: left; vertical-align: top; }
th { background: #eee; }
.calibration { font-size: .92em; color: #333; }
.meta { font-size: .85em; color: #555; margin: .2em 0 .6em; }

/* A follow-up label has to be findable mid-sentence while you're talking. */
.fq { font-family: Helvetica, Arial, sans-serif; font-size: .92em; margin: 1.1em 0 .2em; }
.fq em { font-style: normal; color: #777; font-size: .9em; }

/* Reference blocks that must never split — you read them as one unit or not at all. */
.card { background: #f7f7f5; border-left: 3px solid #666; padding: .5em .9em; margin: .8em 0; }

code { font-family: Consolas, monospace; font-size: .88em; background: #eee; padding: .1em .3em; }
hr { border: 0; border-top: 1px solid #ccc; margin: 2em 0; }
a { color: #14507d; }

@media print {
  @page { size: letter; margin: 8mm 7mm; }
  body { background: #fff; font-size: 9.8pt; line-height: 1.33; padding: 0; }
  main {
    max-width: none; box-shadow: none; padding: 0;
    column-count: 2; column-gap: 6mm; column-fill: auto; hyphens: none;
  }
  h1 {
    font-size: 14pt; column-span: all; margin: 0 0 4pt;
    padding-bottom: 3pt; border-bottom: 2pt solid #000;
  }
  h1.pagebreak { break-before: page; }
  .parthead { column-span: all; break-inside: avoid; }
  .parthead.pagebreak { break-before: page; }
  .parthead h1, .parthead h2, .parthead .qhead { column-span: none; }
  .parthead .qhead { margin-top: 5pt; }
  /* Parts span both columns so you can find them while talking. */
  .qhead {
    column-span: all; break-inside: avoid; break-after: avoid;
    margin: 7pt 0 3pt;
  }
  .qhead h2 { column-span: none; margin: 0; }
  .qhead .meta { margin: 2.5pt 0 2pt; }
  .qhead blockquote.note { margin: 0; }
  h2 {
    font-size: 11pt; column-span: all; margin: 7pt 0 3pt;
    padding: 3pt 5pt; background: #e4e4e4; border-left: 3pt solid #000;
    break-after: avoid; break-inside: avoid;
  }
  h3 {
    font-size: 9.6pt; margin: 5pt 0 1.5pt; padding-bottom: 1pt;
    border-bottom: .6pt solid #999; break-after: avoid; break-inside: avoid;
  }
  h4 {
    font-size: 9.2pt; margin: 5.5pt 0 1.5pt; color: #000;
    text-transform: uppercase; letter-spacing: .03em;
    break-after: avoid; break-inside: avoid;
  }
  p { margin: 0 0 3.5pt; }
  ul, ol { margin: 0 0 4pt; padding-left: 11pt; }
  li { margin: 0 0 2pt; break-inside: avoid; }
  p, li, blockquote { orphans: 2; widows: 2; }
  blockquote { margin: 2pt 0 4pt; padding: 0 0 0 6pt; border-left: 2pt solid #555; }
  blockquote p { margin: 0 0 2.5pt; }
  blockquote.say { background: #f0f0ee; border-left: 2.5pt solid #111; padding: 4pt 6pt; break-inside: avoid; }
  blockquote.warn {
    background: #fbf6e8; border: .7pt dashed #7a6118; border-left-width: 2.5pt;
    padding: 4pt 6pt; font-size: 9.2pt; break-inside: avoid;
  }
  blockquote.note { background: #eef2f6; border-left: 2.5pt solid #35637f; padding: 4pt 6pt; font-size: 9.3pt; break-inside: avoid; break-after: avoid; }
  .answer {
    background: #fafaf9; border-left: 3pt solid #111;
    padding: 2pt 6pt; margin: 2.5pt 0 5pt;
    counter-reset: beat;
  }
  .answer p { margin: 0; padding: 2.4pt 0; counter-increment: beat; break-inside: avoid; }
  .answer p.flow { break-inside: auto; orphans: 3; widows: 3; }
  .answer p + p { border-top: .4pt solid #e0e0da; }
  .answer p > strong:first-child {
    display: block; font-family: Helvetica, Arial, sans-serif;
    font-size: 7.3pt; text-transform: uppercase; letter-spacing: .08em;
    color: #666; margin-bottom: .8pt; break-after: avoid;
  }
  .answer p > strong:first-child::before {
    content: counter(beat); display: inline-block; width: 1.4em; color: #aaa;
  }
  .meta { font-size: 8.4pt; color: #555; margin: 0 0 3pt; break-after: avoid; break-inside: avoid; }
  .calibration { font-size: 8.2pt; line-height: 1.24; color: #3a3a3a; }
  .calibration ul { margin: 0 0 2pt; padding-left: 9pt; }
  .calibration li { margin: 0; }
  /* The screen-side .fq metrics would reflow the long guide, so print resets to plain
     paragraph spacing and only the compact doc opts back in. */
  .fq { font-family: inherit; font-size: inherit; margin: 0 0 3.5pt; }
  .card {
    background: #f4f4f1; border-left: 2.5pt solid #666;
    padding: 3.5pt 6pt; margin: 0 0 4pt; break-inside: avoid;
  }
  table { column-span: all; font-size: 8.3pt; margin: 4pt 0 6pt; }
  thead { display: table-header-group; }
  tr { break-inside: avoid; }
  th, td { padding: 2.5pt 4pt; }
  code { background: none; font-size: .92em; }
  hr { display: none; }
  a { color: inherit; text-decoration: none; }

  /* Every column spanner closes both columns early, which is why the compact doc once
     dropped them all. At the 14-page budget consistency wins: every grey-bar heading and
     every Part divider spans, so no question header renders at half width. */
  /* The clock is the only table here and fits a column, so it need not close both. */
  body.compact table { column-span: none; font-size: 8.1pt; break-inside: avoid; }
  body.compact .calibration { break-inside: avoid; }
  /* Stops an "F1 — ... (~55 words)" label being left alone at a page bottom. */
  body.compact blockquote.say { break-before: avoid; }
  body.compact blockquote.flow { break-inside: auto; }
  body.compact .fq {
    font-family: Helvetica, Arial, sans-serif; font-size: 8.9pt; margin: 4pt 0 1.5pt;
    break-after: avoid; break-inside: avoid;
  }
}
"""

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>{css}</style>
</head>
<body class="{body_class}">
<main>
{body}
</main>
</body>
</html>
"""


# A beat longer than this can't fit a part-used column, so forcing it whole leaves a white gap.
FLOW_CHARS = 480


def _mark_long_beats(answer_block: str, flow_chars: int = FLOW_CHARS) -> str:
    def tag(match: re.Match[str]) -> str:
        para = match.group(0)
        if len(re.sub(r"<[^>]+>", "", match.group(1))) > flow_chars:
            return para.replace("<p>", '<p class="flow">', 1)
        return para

    return re.sub(r"<p>(.*?)</p>", tag, answer_block, flags=re.DOTALL)


def wrap_part_heads(body: str) -> str:
    """Keep a Part heading with whatever follows it, for the same spanner reason."""
    pattern = re.compile(
        r"(<h1(?: class=\"pagebreak\")?>Part [^<]*</h1>\s*)"
        r"((?:<hr />\s*)?)"
        r"(<div class=\"qhead\">.*?</div>\s*|<h2>.*?</h2>\s*|<p>.*?</p>\s*|<blockquote[^>]*>.*?</blockquote>\s*)?",
        flags=re.DOTALL,
    )

    def wrap(match: re.Match[str]) -> str:
        parts = "".join(p for p in match.groups() if p)
        cls = "parthead pagebreak" if 'class="pagebreak"' in match.group(1) else "parthead"
        return f'<div class="{cls}">\n{parts}</div>\n'

    return pattern.sub(wrap, body)


def wrap_question_heads(body: str) -> str:
    """Chrome ignores break-after on column spanners, so bind each heading to its question."""
    pattern = re.compile(
        r"(<h2>(?:EQ|MQ|RQ|SQ)\d+[^<]*</h2>\s*)"
        r"(<p class=\"meta\">.*?</p>\s*)?"
        r"(<blockquote class=\"note\">.*?</blockquote>\s*)?",
        flags=re.DOTALL,
    )

    def wrap(match: re.Match[str]) -> str:
        parts = "".join(p for p in match.groups() if p)
        return f'<div class="qhead">\n{parts}</div>\n'

    return pattern.sub(wrap, body)


def wrap_model_answers(
    body: str, break_before_part1: bool = True, flow_chars: int = FLOW_CHARS
) -> str:
    """Group the paragraphs under a 'Model answer' heading so the spoken block reads as one unit."""
    pattern = re.compile(
        r"(<h3>Model answer[^<]*</h3>\s*)((?:<p>(?:(?!</?h[1-4]|<blockquote|<hr).)*?</p>\s*)+)",
        flags=re.DOTALL,
    )
    body = pattern.sub(
        lambda m: f'{m.group(1)}<div class="answer">\n{_mark_long_beats(m.group(2), flow_chars)}</div>\n',
        body,
    )

    # The calibration list is reference, not rehearsal, so it reads smaller.
    calib = re.compile(
        r"(<h3>(?:Senior \u2192 Staff-signal|The Staff-signal)</h3>\s*)(<ul>.*?</ul>)", flags=re.DOTALL
    )
    body = calib.sub(lambda m: f'{m.group(1)}<div class="calibration">{m.group(2)}</div>', body)

    meta = re.compile(r"<p>(<strong>Asked by:</strong>.*?)</p>", flags=re.DOTALL)
    body = meta.sub(lambda m: f'<p class="meta">{m.group(1)}</p>', body)

    # The rehearsal section starts a fresh page so EQ01 isn't stranded under the front matter.
    if break_before_part1:
        body = body.replace("<h1>Part 1 ", '<h1 class="pagebreak">Part 1 ', 1)
    return body


def classify_blockquotes(body: str) -> str:
    """Warnings, coaching asides and spoken lines all render as plain blockquotes; separate them."""

    def tag(match: re.Match[str]) -> str:
        opening = match.group(1)
        if opening.startswith("\u26a0"):
            kind = "warn"
        elif opening.startswith("<strong>"):
            kind = "note"
        else:
            kind = "say"
        return f'<blockquote class="{kind}">\n<p>{opening}'

    return re.sub(r"<blockquote>\s*<p>(.{0,12})", tag, body, flags=re.DOTALL)


def style_labels(body: str, compact: bool = False, flow_chars: int = FLOW_CHARS) -> str:
    """Give follow-up labels and `[[card]]`-marked paragraphs their own classes."""
    if compact:
        body = re.sub(
            r"<p>(<strong>F\d+ \u2014.*?)</p>",
            lambda m: f'<p class="fq">{m.group(1)}</p>',
            body,
            flags=re.DOTALL,
        )
        body = _flow_long_quotes(body, flow_chars)
    return re.sub(r"<p>\[\[card\]\]\s*", '<p class="card">', body)


def _flow_long_quotes(body: str, flow_chars: int = FLOW_CHARS) -> str:
    """A quote taller than a part-used column strands the rest of it, so let big ones break."""

    def tag(match: re.Match[str]) -> str:
        if len(re.sub(r"<[^>]+>", "", match.group(2))) > FLOW_CHARS:
            return match.group(0).replace(
                f'class="{match.group(1)}"', f'class="{match.group(1)} flow"', 1
            )
        return match.group(0)

    return re.sub(
        r'<blockquote class="(warn|say)">(.*?)</blockquote>', tag, body, flags=re.DOTALL
    )


def main() -> None:
    keys = sys.argv[1:] or ["all"]
    if keys == ["all"]:
        keys = list(DOCS)

    md = MarkdownIt("commonmark", {"html": True}).enable("table")
    OUT.mkdir(parents=True, exist_ok=True)

    for key in keys:
        doc = DOCS[key]
        body = wrap_part_heads(
            style_labels(
                wrap_question_heads(
                    wrap_model_answers(
                        classify_blockquotes(md.render(doc["src"].read_text(encoding="utf-8"))),
                        break_before_part1=doc["break_before_part1"],
                        flow_chars=doc.get("flow_chars", FLOW_CHARS),
                    )
                ),
                compact=doc["body_class"] == "compact",
                flow_chars=doc.get("flow_chars", FLOW_CHARS),
            )
        )
        doc["out"].write_text(
            PAGE.format(
                title=html.escape(doc["title"]),
                css=CSS,
                body=body,
                body_class=doc["body_class"],
            ),
            encoding="utf-8",
        )
        print(f"  {doc['src'].name} -> {doc['out'].relative_to(ROOT)}")


if __name__ == "__main__":
    main()
