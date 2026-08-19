"""Render practice/*.md into standalone print-ready HTML.

Run: python scripts/build_practice_html.py
Output: practice/print/*.html — open in a browser and Ctrl+P.
"""

from __future__ import annotations

import html
import re
from pathlib import Path

from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "practice"
OUT = SRC / "print"

STYLE_BLOCK = re.compile(r"^\s*<style>.*?</style>\s*", re.DOTALL)

CSS = """
:root { color-scheme: light; }
* { box-sizing: border-box; }
body {
  font-family: Georgia, "Times New Roman", serif;
  font-size: 12pt;
  line-height: 1.55;
  color: #111;
  background: #f4f4f2;
  margin: 0;
  padding: 2rem 1rem 4rem;
}
main {
  max-width: 46em;
  margin: 0 auto;
  background: #fff;
  padding: 3rem 3.25rem;
  box-shadow: 0 1px 4px rgba(0,0,0,.12);
}
h1, h2, h3, h4 { font-family: Helvetica, Arial, sans-serif; line-height: 1.25; }
h1 { font-size: 1.75rem; margin: 0 0 .4em; }
h2 {
  font-size: 1.3rem;
  margin: 2.4em 0 .5em;
  padding-top: .5em;
  border-top: 2px solid #111;
}
h3 { font-size: 1.05rem; margin: 1.6em 0 .4em; }
h4 { font-size: .98rem; margin: 1.3em 0 .3em; }
p, li { orphans: 3; widows: 3; }
blockquote {
  border-left: 3px solid #666;
  margin: .9em 0 .9em 0;
  padding: .15em 0 .15em 1em;
  color: #1a1a1a;
}
blockquote p { margin: .4em 0; }
code {
  font-family: Consolas, "Courier New", monospace;
  font-size: .88em;
  background: #eee;
  padding: .1em .3em;
  border-radius: 2px;
}
table { border-collapse: collapse; width: 100%; font-size: .88rem; margin: 1em 0; }
th, td { border: 1px solid #999; padding: 5px 8px; text-align: left; vertical-align: top; }
th { background: #eee; }
hr { border: 0; border-top: 1px solid #ccc; margin: 2em 0; }
a { color: #14507d; }
strong { font-weight: 700; }

/* The interviewer's prompt — must not look like your answer. */
blockquote.prompt {
  font-family: Helvetica, Arial, sans-serif;
  border: 1px solid #444;
  border-left-width: 5px;
  background: #f2f2f0;
  padding: .55em .8em;
  margin: .8em 0 1em;
}
blockquote.warn {
  border: 1px dashed #8a6d1f;
  border-left-width: 4px;
  background: #fdf8ea;
  padding: .5em .8em;
}
p.probe {
  font-family: Helvetica, Arial, sans-serif;
  margin-top: 1.1em;
}
p.probe em { color: #666; font-style: normal; }

@media print {
  @page { size: letter; margin: 8mm 7mm; }
  body { background: #fff; font-size: 9.6pt; line-height: 1.28; padding: 0; }
  /* Two columns keeps a readable line length; a single column at this size runs ~100 characters. */
  main {
    max-width: none; box-shadow: none; padding: 0;
    column-count: 2; column-gap: 5mm; column-fill: auto;
    column-rule: 0.5pt solid #ddd;
    hyphens: none;
  }
  h1 {
    font-size: 14pt; column-span: all; margin: 0 0 6pt;
    padding-bottom: 3pt; border-bottom: 2pt solid #000;
  }
  h1:first-of-type { margin-top: 0; }
  /* Each pillar is a memorization chunk, so give it a hard visual boundary. */
  h2 {
    font-size: 11pt; margin: 10pt 0 3pt; padding-top: 3pt;
    border-top: 1.5pt solid #000; break-after: avoid; break-inside: avoid;
  }
  h2 + p { font-size: 8.2pt; color: #444; margin: 0 0 4pt; }
  h3 {
    font-size: 9.6pt; margin: 7pt 0 2pt; break-after: avoid;
    text-transform: uppercase; letter-spacing: .03em;
  }
  h4 { font-size: 9.4pt; margin: 5pt 0 1.5pt; break-after: avoid; }
  p { margin: 0 0 4pt; }
  ul, ol { margin: 0 0 4pt; padding-left: 11pt; }
  li { margin: 0 0 1.5pt; }
  p, li, blockquote { orphans: 2; widows: 2; }
  /* Default blockquote = the words you actually say. */
  blockquote {
    margin: 3pt 0 5pt; padding: 0 0 0 6pt;
    border-left: 2pt solid #555; background: none;
  }
  blockquote p { margin: 0 0 2.5pt; }
  blockquote.prompt {
    border: 0.7pt solid #333; border-left-width: 3pt;
    background: #f0f0ee; padding: 4pt 5pt; margin: 4pt 0 6pt;
    break-inside: avoid;
  }
  blockquote.warn {
    border: 0.7pt dashed #7a6118; border-left-width: 2.5pt;
    background: #fbf6e8; padding: 4pt 5pt;
  }
  p.probe { margin: 8pt 0 2pt; font-size: 9.6pt; break-after: avoid; }
  p.probe em { color: #555; font-style: normal; }
  table { column-span: all; font-size: 8.2pt; margin: 5pt 0; }
  th, td { padding: 2.5pt 4pt; }
  code { background: none; font-size: .9em; }
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


def render(md: MarkdownIt, path: Path) -> str:
    text = STYLE_BLOCK.sub("", path.read_text(encoding="utf-8"), count=1)
    body = md.render(text)
    # Markdown renders prompts, warnings and model answers as identical blockquotes; tag them so print CSS can separate them.
    body = body.replace(
        "<blockquote>\n<p><strong>Base:</strong>", '<blockquote class="prompt">\n<p><strong>Base:</strong>'
    )
    body = body.replace("<blockquote>\n<p>\u26a0\ufe0f", '<blockquote class="warn">\n<p>\u26a0\ufe0f')
    body = re.sub(r"<p><strong>(F\d) \u2014", lambda m: f'<p class="probe"><strong>{m.group(1)} \u2014', body)
    return body


def main() -> None:
    md = MarkdownIt("commonmark", {"html": True}).enable("table")
    OUT.mkdir(exist_ok=True)

    sources = sorted(SRC.glob("*.md"))
    if not sources:
        raise SystemExit(f"No markdown files found in {SRC}")

    combined: list[str] = []
    for path in sources:
        body = render(md, path)
        title = path.stem.replace("-", " ")
        (OUT / f"{path.stem}.html").write_text(
            PAGE.format(title=html.escape(title), css=CSS, body=body), encoding="utf-8"
        )
        combined.append(body)
        print(f"  {path.name} -> print/{path.stem}.html")

    (OUT / "ALL-tracks.html").write_text(
        PAGE.format(
            title="Anduril Interview Practice — All Tracks",
            css=CSS,
            body="\n<hr>\n".join(combined),
        ),
        encoding="utf-8",
    )
    print(f"  all {len(sources)} files -> print/ALL-tracks.html")


if __name__ == "__main__":
    main()
