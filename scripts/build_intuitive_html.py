"""Render the Intuitive interview guide into a print-ready HTML file.

Run: python scripts/build_intuitive_html.py
Output: intuitive/print/intuitive-interview-guide.html — open in a browser and Ctrl+P.

Print layout is two-column at ~9.4pt.
"""

from __future__ import annotations

import html
import re
from pathlib import Path

from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "intuitive" / "intuitive-interview-guide.md"
OUT = ROOT / "intuitive" / "print"
TITLE = "Intuitive Surgical — Senior Human Factors Analyst"

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

table { border-collapse: collapse; width: 100%; font-size: .87rem; margin: 1em 0; }
th, td { border: 1px solid #999; padding: 5px 8px; text-align: left; vertical-align: top; }
th { background: #eee; }
code { font-family: Consolas, monospace; font-size: .88em; background: #eee; padding: .1em .3em; }
hr { border: 0; border-top: 1px solid #ccc; margin: 2em 0; }
a { color: #14507d; }

@media print {
  @page { size: letter; margin: 8mm 7mm; }
  body { background: #fff; font-size: 9.4pt; line-height: 1.29; padding: 0; }
  main {
    max-width: none; box-shadow: none; padding: 0;
    column-count: 2; column-gap: 6mm; column-fill: auto; hyphens: none;
  }
  h1 {
    font-size: 14pt; column-span: all; margin: 0 0 4pt;
    padding-bottom: 3pt; border-bottom: 2pt solid #000;
  }
  /* Parts span both columns so you can find them while talking. */
  h2 {
    font-size: 11pt; column-span: all; margin: 9pt 0 4pt;
    padding: 3pt 5pt; background: #e4e4e4; border-left: 3pt solid #000;
    break-after: avoid; break-inside: avoid;
  }
  h3 {
    font-size: 9.9pt; margin: 7pt 0 2pt; padding-bottom: 1.5pt;
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
  blockquote { margin: 2.5pt 0 5pt; padding: 0 0 0 6pt; border-left: 2pt solid #555; }
  blockquote p { margin: 0 0 3pt; }
  blockquote.say { background: #f0f0ee; border-left: 2.5pt solid #111; padding: 4pt 6pt; }
  blockquote.warn {
    background: #fbf6e8; border: .7pt dashed #7a6118; border-left-width: 2.5pt;
    padding: 4pt 6pt; font-size: 9.2pt; break-inside: avoid;
  }
  blockquote.note { background: #eef2f6; border-left: 2.5pt solid #35637f; padding: 4pt 6pt; font-size: 9.3pt; }
  table { column-span: all; font-size: 8.3pt; margin: 4pt 0 6pt; }
  thead { display: table-header-group; }
  tr { break-inside: avoid; }
  th, td { padding: 2.5pt 4pt; }
  code { background: none; font-size: .92em; }
  hr { display: none; }
  a { color: inherit; text-decoration: none; }
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
<body>
<main>
{body}
</main>
</body>
</html>
"""


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


def main() -> None:
    md = MarkdownIt("commonmark", {"html": True}).enable("table")
    OUT.mkdir(parents=True, exist_ok=True)

    body = classify_blockquotes(md.render(SRC.read_text(encoding="utf-8")))
    target = OUT / "intuitive-interview-guide.html"
    target.write_text(
        PAGE.format(title=html.escape(TITLE), css=CSS, body=body),
        encoding="utf-8",
    )
    print(f"  {SRC.name} -> {target.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
