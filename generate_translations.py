"""記事リンク先を取得し、日本語訳付きのローカルHTMLを生成する。"""
from pathlib import Path
import re, json, time, html, urllib.parse, urllib.request

SOURCE = Path('index.html')
OUT_DIR = Path('translated')
MAX_ARTICLES = 20  # API制限回避のため初期値は20


def http_get(url: str, timeout: int = 30) -> str:
    with urllib.request.urlopen(url, timeout=timeout) as resp:
        return resp.read().decode('utf-8', 'ignore')


def translate_to_ja(text: str) -> str:
    if not text.strip():
        return ''
    out = []
    for i in range(0, len(text), 3500):
        chunk = text[i:i + 3500]
        params = urllib.parse.urlencode({
            'client': 'gtx', 'sl': 'en', 'tl': 'ja', 'dt': 't', 'q': chunk
        })
        url = 'https://translate.googleapis.com/translate_a/single?' + params
        try:
            data = json.loads(http_get(url, 20))
            out.append(''.join(x[0] for x in data[0] if x and x[0]))
        except Exception:
            out.append(chunk)
        time.sleep(0.2)
    return ''.join(out)


def parse_articles(index_html: str):
    return re.findall(r'\{\s*num:(\d+),\s*title:"([^"]+)",\s*url:"([^"]+)".*?desc:"([^"]+)"\s*\}', index_html, re.S)


def main() -> None:
    OUT_DIR.mkdir(exist_ok=True)
    articles = parse_articles(SOURCE.read_text(encoding='utf-8'))
    cards = []

    for num, title, url, _desc in articles[:MAX_ARTICLES]:
        mirror = 'https://r.jina.ai/http://' + url.replace('https://', '').replace('http://', '')
        try:
            english = http_get(mirror, 30)
        except Exception as e:
            english = f'Fetch failed: {e}\n\nOriginal URL: {url}'

        ja_title = translate_to_ja(title)
        japanese = translate_to_ja(english)
        slug = f'article-{int(num):03d}.html'

        page = f"""<!doctype html><html lang='ja'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><title>{html.escape(ja_title)}</title>
<style>body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;line-height:1.8;max-width:960px;margin:0 auto;padding:24px}}pre{{white-space:pre-wrap;word-break:break-word;background:#f7f7f8;padding:16px;border-radius:8px}}a{{color:#2563eb}}</style></head>
<body><p><a href='../index.html'>← 一覧へ戻る</a></p><h1>{html.escape(ja_title)}</h1><p>原文: <a href='{html.escape(url)}'>{html.escape(url)}</a></p>
<h2>日本語訳（省略なし・取得テキスト全文）</h2><pre>{html.escape(japanese)}</pre>
<h2>英語原文（取得テキスト全文）</h2><pre>{html.escape(english)}</pre></body></html>"""
        (OUT_DIR / slug).write_text(page, encoding='utf-8')
        cards.append((int(num), slug, ja_title, url))

    cards.sort(key=lambda x: x[0])
    items = '\n'.join(
        f"<li>#{n:03d} <a href='{slug}'>{html.escape(title)}</a> <small><a href='{url}'>原文リンク</a></small></li>"
        for n, slug, title, url in cards
    )
    (OUT_DIR / 'index.html').write_text(
        f"<!doctype html><html lang='ja'><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><title>翻訳記事一覧</title><body><h1>翻訳記事一覧</h1><p>生成数: {len(cards)} 件</p><p><a href='../index.html'>元一覧へ戻る</a></p><ol>{items}</ol></body></html>",
        encoding='utf-8'
    )


if __name__ == '__main__':
    main()
