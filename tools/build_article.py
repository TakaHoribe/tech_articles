#!/usr/bin/env python3
"""
Build a complete article HTML file from body content + metadata.
Handles all boilerplate so agents only need to produce the inner body HTML.

Usage:
  # Body from stdin:
  echo "<p>本文</p>" | python tools/build_article.py --num 021 --title "タイトル" --meta "2025 · Source · ⭐⭐⭐" --url "https://..."

  # Body from file:
  python tools/build_article.py --num 021 --title "タイトル" --meta "2025 · Source · ⭐⭐⭐" --url "https://..." --body /tmp/body.html

Output:
  Writes articles/article_NNN.html and prints the path.
  Also prints the LOCAL_ARTICLES entry to add to index.html.

Agent usage pattern:
  - Agent receives: article text (from extract_article.py output)
  - Agent produces: only the <div class="body"> inner HTML (no DOCTYPE/head/nav/footer needed)
  - This script wraps it into the full article file
"""
import sys
from pathlib import Path

ARTICLES_DIR = Path(__file__).parent.parent / "articles"

TEMPLATE = """\
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<link rel="stylesheet" href="./style.css">
</head>
<body>
<div class="wrap">
<nav><a href="../index.html">← 記事一覧に戻る</a></nav>
<div class="ah">
<h1>{title}</h1>
<div class="meta">{meta}</div>
<div class="orig">原文: <a href="{url}" target="_blank" rel="noopener">{url}</a></div>
</div>
<div class="body">

{body}

</div>
<footer><p>日本語翻訳版 | 原文: <a href="{url}" target="_blank" rel="noopener">こちら</a></p></footer>
</div>
</body>
</html>
"""


def build(num: int, title: str, meta: str, url: str, body: str) -> Path:
    out = ARTICLES_DIR / f"article_{num:03d}.html"
    html = TEMPLATE.format(title=title, meta=meta, url=url, body=body.strip())
    out.write_text(html, encoding="utf-8")
    return out


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--num",   required=True, type=int, help="Article number, e.g. 21")
    p.add_argument("--title", required=True, help="Japanese article title")
    p.add_argument("--meta",  required=True, help='e.g. "2025 · Aurora · ⭐⭐⭐⭐"')
    p.add_argument("--url",   required=True, help="Original article URL")
    p.add_argument("--body",  help="Path to body HTML file (default: read from stdin)")
    args = p.parse_args()

    if args.body:
        body = Path(args.body).read_text(encoding="utf-8")
    else:
        body = sys.stdin.read()

    if not body.strip():
        print("ERROR: body content is empty", file=sys.stderr)
        sys.exit(1)

    out = build(args.num, args.title, args.meta, args.url, body)
    print(f"Written: {out}")
    print(f"Add to LOCAL_ARTICLES: {args.num}:'./articles/article_{args.num:03d}.html'")
