# tools/

トークン効率化のためのPythonユーティリティ。
プログラムで処理できる部分はClaudeに任せず、Claudeは翻訳・構造判断のみに集中する。

## ツール一覧

### `extract_article.py` — 記事本文抽出
静的HTMLページからarticle bodyを抽出し、翻訳Agentに渡すための本文テキストと画像URLを出力する。
WebFetchで丸ごとfetchする（〜20,000トークン）より、本文テキスト（〜2,000トークン）を渡すほうが大幅に効率的。

```bash
python3 tools/extract_article.py https://example.com/article > /tmp/content.json
python3 tools/extract_article.py https://example.com/article --text-only
```

**注意**: JS描画が必要なページ（Waymoブログ等）はPlaywrightが必要でこのツールでは処理できない。

---

### `fetch_arxiv.py` — arXiv論文抽出
arXivのHTML版から著者・Abstract・セクション・図を抽出する。`--download-figs` で画像も一括ダウンロード。

```bash
python3 tools/fetch_arxiv.py 2503.20523 --text-only
python3 tools/fetch_arxiv.py 2503.20523 --download-figs
```

---

### `download_image.py` — 画像ダウンロード
1枚〜複数URLを `articles/images/` に `{md5_12char}_img.{ext}` 命名でダウンロード。
YouTube サムネイルにも対応。

```bash
python3 tools/download_image.py https://example.com/photo.jpg
python3 tools/download_image.py --yt VIDEO_ID
cat /tmp/content.json | python3 tools/download_image.py --stdin-json
```

---

### `build_article.py` — 記事HTML生成
body HTMLを受け取り、完全な `article_NNN.html` を生成する。
Agentは `<div class="body">` の中身HTMLだけ出力すればよく、テンプレートを知る必要がない。

```bash
echo "<p>本文</p>" | python3 tools/build_article.py --num 21 --title "タイトル" --meta "2025 · Source · ⭐⭐⭐" --url "https://..."
python3 tools/build_article.py --num 21 --title "..." --meta "..." --url "..." --body /tmp/body.html
```

---

### `add_to_index.py` — index.html更新
`index.html` の `LOCAL_ARTICLES` に新規エントリを追加する。index.html全体を読み込む必要がない。

```bash
python3 tools/add_to_index.py 21
python3 tools/add_to_index.py 21 22 23
```

---

## 推奨ワークフロー（新記事作成）

```bash
# 1. 本文と画像URLを抽出
python3 tools/extract_article.py <URL> > /tmp/content.json

# 2. 画像を一括ダウンロード
cat /tmp/content.json | python3 tools/download_image.py --stdin-json

# 3. AgentにJSON内のbody_textを渡して翻訳・body HTML生成を依頼
#    Agentが /tmp/body.html を出力する

# 4. article HTMLを生成
python3 tools/build_article.py --num NNN --title "..." --meta "..." --url "..." --body /tmp/body.html

# 5. index.htmlに追記
python3 tools/add_to_index.py NNN
```
