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

@media print {
  @page { margin: 16mm 15mm; }
  body { background: #fff; font-size: 10.5pt; line-height: 1.5; padding: 0; }
  main { max-width: none; box-shadow: none; padding: 0; }
  h1 { font-size: 19pt; }
  /* Each pillar starts on a fresh sheet. */
  h2 { font-size: 15pt; page-break-before: always; border-top: none; padding-top: 0; margin-top: 0; }
  h2:first-of-type { page-break-before: avoid; }
  h3 { font-size: 12.5pt; }
  h4 { font-size: 11pt; }
  h1, h2, h3, h4 { page-break-after: avoid; page-break-inside: avoid; }
  blockquote, table { page-break-inside: avoid; }
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
    return md.render(text)


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
