# 技術記事ローカル翻訳サイト — ノウハウまとめ

## プロジェクト概要

英語技術記事（主に自動運転系）を取得・日本語翻訳し、ローカルHTMLとして保存するワークフロー。
画像・動画なども含めて完全にローカルで閲覧できる静的サイトを構築する。

---

## 1. ページスクレイピング

### 基本方針
- **JS描画が必要なページ**（SPAや遅延ロード）→ Playwright（ヘッドレスChromium）を使う
- **静的HTMLページ**（arXiv論文など）→ urllib で十分

### Playwright 基本パターン（Python）

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(url, wait_until="networkidle")
    html = page.content()
    browser.close()
```

### 注意点
- `wait_until="networkidle"` で動的コンテンツのロードを待つ
- arXiv等のJSなし静的ページにはurllibで十分。Playwrightは重いので使い分ける

---

## 2. 画像ダウンロード

### 基本（urllib）

```python
import urllib.request
urllib.request.urlretrieve(url, local_path)
```

ヘッダーが必要な場合：

```python
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 ..."})
with urllib.request.urlopen(req) as r:
    with open(local_path, "wb") as f:
        f.write(r.read())
```

### 落とし穴①：プロトコル相対URL

`//lh3.googleusercontent.com/...` のように `//` で始まるURLは、`file://` プロトコル下では壊れる。
→ **必ずローカルにダウンロード**して `./images/xxx.jpg` に差し替える。

```python
# HTML内のプロトコル相対URLを修正
src = src.replace("//", "https://", 1) if src.startswith("//") else src
```

### 落とし穴②：署名付きURL（lh3.googleusercontent.com）

`https://lh3.googleusercontent.com/...=e365-s420` のような署名付きURLは期限切れでHTTP 400を返す。
urllib・curlどちらでも取得不可。

**解決策：PlaywrightでDOM要素をスクリーンショット**

```python
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(article_url, wait_until="networkidle")
    img_el = page.query_selector(f'img[alt="{alt_text}"]')
    if img_el:
        img_el.screenshot(path=local_path)
    browser.close()
```

ブラウザのレンダリングコンテキスト内ではアクセス可能なため、要素単位でスクショを撮れる。

### 落とし穴③：レスポンス傍受

Playwrightで `page.on("response", ...)` を使ってネットワーク応答を傍受する方法もあるが、
画像URLが動的に変わる場合は要素スクショの方が確実。

---

## 3. 動画コンテンツの処理

### 方針
動画ファイル本体を埋め込む必要はない。**「ここに動画があった」ことが視覚的にわかること**が重要。

### webm / mp4 の最初のフレーム抽出（ffmpeg）

```bash
ffmpeg -i input.mp4 -vframes 1 -q:v 2 output.jpg
ffmpeg -i input.webm -vframes 1 -q:v 2 output.jpg
```

### YouTube サムネイル取得

```
https://img.youtube.com/vi/{VIDEO_ID}/maxresdefault.jpg
```

最高解像度。存在しない場合は `hqdefault.jpg` にフォールバック。

```python
yt_id = "dtMMW0kTXIE"
thumb_url = f"https://img.youtube.com/vi/{yt_id}/maxresdefault.jpg"
urllib.request.urlretrieve(thumb_url, local_path)
```

### 動画プレースホルダー HTML + CSS パターン

サムネイル画像の上に再生ボタンオーバーレイを重ねるパターン。クリックで元動画を開く。

```css
.vid-wrap{position:relative;margin:20px auto;border-radius:12px;overflow:hidden;
  border:1px solid var(--bd);display:block;max-width:100%;cursor:pointer;text-decoration:none}
.vid-wrap img{width:100%;height:auto;display:block;filter:brightness(.85)}
.vid-overlay{position:absolute;inset:0;display:flex;flex-direction:column;
  align-items:center;justify-content:center;gap:10px;background:rgba(0,0,0,.35)}
.vid-play{width:64px;height:64px;background:rgba(255,255,255,.92);border-radius:50%;
  display:flex;align-items:center;justify-content:center;transition:transform .15s}
.vid-wrap:hover .vid-play{transform:scale(1.1)}
.vid-play svg{width:28px;height:28px;margin-left:4px}
.vid-badge{font-size:.72rem;font-weight:600;letter-spacing:.06em;
  color:rgba(255,255,255,.9);background:rgba(0,0,0,.55);padding:3px 10px;border-radius:20px}
.vid-title{font-size:.82rem;color:rgba(255,255,255,.85);text-align:center;
  max-width:80%;line-height:1.4;padding:0 16px}
.vid-caption{font-size:.82rem;color:var(--m);text-align:center;margin-top:8px}
```

```html
<!-- 動画プレースホルダー（webm / mp4） -->
<a class="vid-wrap" href="VIDEO_URL" target="_blank" rel="noopener">
  <img src="./images/frame.jpg" alt="動画タイトル">
  <div class="vid-overlay">
    <div class="vid-play">
      <svg viewBox="0 0 24 24" fill="#222"><polygon points="5,3 19,12 5,21"/></svg>
    </div>
    <div class="vid-badge">動画</div>
    <div class="vid-title">動画タイトル</div>
  </div>
</a>
<div class="vid-caption">動画の説明（クリックで元動画を開く）</div>

<!-- YouTubeプレースホルダー -->
<a class="vid-wrap" href="https://www.youtube.com/watch?v=VIDEO_ID" target="_blank" rel="noopener">
  <img src="./images/thumbnail.jpg" alt="YouTube タイトル">
  <div class="vid-overlay">
    <div class="vid-play">
      <svg viewBox="0 0 24 24" fill="#ff0000">
        <path d="M21.8 8s-.2-1.4-.8-2c-.8-.8-1.6-.8-2-.9C16.8 5 12 5 12 5s-4.8 0-7 .1c-.4.1-1.2.1-2 .9-.6.6-.8 2-.8 2S2 9.6 2 11.2v1.5c0 1.6.2 3.2.2 3.2s.2 1.4.8 2c.8.8 1.8.8 2.2.8C6.8 19 12 19 12 19s4.8 0 7-.1c.4-.1 1.2-.1 2-.9.6-.6.8-2 .8-2s.2-1.6.2-3.2v-1.5C22 9.6 21.8 8 21.8 8z"/>
        <polygon points="10,15 10,9 15,12" fill="white"/>
      </svg>
    </div>
    <div class="vid-badge">YouTube</div>
    <div class="vid-title">動画タイトル</div>
  </div>
</a>
<div class="vid-caption">説明（クリックでYouTubeを開く）</div>
```

---

## 4. GIF アニメーション

GIFはそのままダウンロードして `<img>` で埋め込めば動作する。
`<video>` タグや特別な処理は不要。

```html
<figure>
  <img src="./images/animation.gif" alt="説明">
  <figcaption>キャプション</figcaption>
</figure>
```

**注意：** テキストリンクや `.note` divにするのはNG。`<figure><img>` で表示すること。

---

## 5. 画像の表示サイズとセンタリング

画像は記事幅いっぱいに表示する（`width: 100%`）。`max-width: 100%` だと元画像が小さい場合に縮んだまま表示されるため使わない。

```css
.body img {
  width: 100%;          /* 記事幅いっぱいに広げる */
  height: auto;
  border-radius: 8px;
  margin: 16px auto;    /* auto で左右センタリング */
  display: block;       /* block にしないと margin:auto が効かない */
}
```

**インライン style は書かない。** `articles/style.css` の共通スタイルが適用されるので、`<img>` タグに `style="..."` を追加するのは冗長で、後でまとめて変更できなくなる。

### ユーザーの嗜好
- 画像は記事テキスト幅と同じ幅で表示する（横に目一杯使う）
- 視認性・ひと目でわかる構造を最優先にする

---

## 6. HTMLファイル命名・ディレクトリ構成

```
tech_articles/
├── index.html          # 記事一覧トップページ
├── requirements.md     # プロジェクト要件
├── know-how.md         # このファイル
└── articles/
    ├── article_001.html
    ├── article_002.html
    ├── ...
    └── images/
        ├── xxxxx_img.jpg    # 記事画像（ハッシュ_img.拡張子）
        ├── xxxxx_img.gif    # アニメーションGIF
        ├── xxxxx_frame.jpg  # 動画の最初のフレーム
        └── xxxxx_img.mp4    # 動画本体（必要な場合のみ）
```

画像ファイル名はURLからハッシュを取り、`{hash}_{type}.{ext}` の形式で統一。

---

## 7. index.html のローカル記事リンク管理

```javascript
const LOCAL_ARTICLES = {
  1: './articles/article_001.html',
  2: './articles/article_002.html',
  // ...
};

// renderCard() 内
const localUrl = LOCAL_ARTICLES[a.num];
// タイトルリンクをローカルに向け、↗原文リンクを別途追加
```

「↗原文」リンクは `.orig-link` クラスで別スタイルを当てる。

---

## 8. 記事HTMLテンプレート

```html
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>記事タイトル</title>
<style>
:root{--bg:#0f1117;--s:#1a1d27;--bd:#2e3250;--a:#4f8ef7;--a2:#7c6af7;--t:#e8eaf6;--m:#8891b0}
/* ... 共通スタイル ... */
</style>
</head>
<body>
<div class="wrap">
<nav><a href="../index.html">← 記事一覧に戻る</a></nav>
<div class="ah">
  <h1>記事タイトル（日本語）</h1>
  <div class="meta">日付 · カテゴリ · ⭐評価</div>
  <div class="orig">原文: <a href="元URL" target="_blank" rel="noopener">元URL</a></div>
</div>
<div class="body">
  <!-- 翻訳本文 -->
</div>
<footer><p>日本語翻訳版 | 原文: <a href="元URL" target="_blank" rel="noopener">こちら</a></p></footer>
</div>
</body>
</html>
```

---

## 9. トラブルシューティング集

| 症状 | 原因 | 対処 |
|------|------|------|
| 画像が表示されない（壊れたアイコン） | URLがプロトコル相対（`//...`） | ローカルにダウンロード |
| 画像が HTTP 400 で取得できない | 署名付きURL期限切れ（lh3等） | Playwright要素スクショ |
| 画像が左寄りになる | `display:block` がない | `margin:auto;display:block` を追加 |
| GIFが表示されない（テキストになっている） | `<img>` ではなく `.note` divになっている | `<figure><img>` に修正 |
| `<figure>` にキャプションはあるが画像なし | `<img>` タグが挿入されていない | `<figure>` 内に `<img>` を追加 |
| `file://` で動画・音声が再生できない | ブラウザのセキュリティ制限 | 動画はプレースホルダー方式にする |

---

## 10. arXiv論文の図画像取得

### 基本方針

arXivには論文のHTMLバージョン（`https://arxiv.org/html/{ARXIV_ID}`）があり、そこから図画像を直接取得できる。
PDFからの抽出は不要。HTMLバージョンの `<figure>` タグを解析すればURLが得られる。

### 図URLの構造

arXivのHTMLバージョンの画像は `https://arxiv.org/html/{ARXIV_ID}/` 以下に配置されている。
例：`https://arxiv.org/html/2410.23262/figs/fig1.png`

### 取得手順

1. `https://arxiv.org/html/{ARXIV_ID}` を urllib で fetch（JS不要、静的HTML）
2. BeautifulSoup 等で `<figure>` → `<img src>` を列挙
3. 相対URLは `https://arxiv.org/html/{ARXIV_ID}/` を prefix して絶対URL化
4. urllib で `articles/images/` にダウンロード（ファイル名は `{論文名}_fig{N}.png` 等）
5. 翻訳HTMLの対応セクションに `<figure><img><figcaption>` で挿入

### ファイル命名規則

`emma_fig1.png`, `emma_fig2.png` ... のように `{論文略称}_fig{N}.{ext}` で統一。
可視化図が複数ある場合は `emma_vis_{ID}t.jpg`（t=trajectory, d=detection, r=road graph）のようにサフィックスで区別。

### 挿入位置の対応

論文の Figure N と翻訳HTMLのセクションを対照して適切な位置に挿入する。
通常は各セクションの冒頭（説明文の前）か、言及箇所の直後。

---

## 11. 元記事の構造確認には必ず Playwright を使う

**WebFetch は使わない。** WebFetch はJSを実行せず、以下を見落とす：
- YouTube / iframe 埋め込みの位置
- 遅延ロードされる画像・動画
- JS で動的に挿入されるコンテンツ

### 正しい確認手順

元記事の構造を確認するときは Playwright で実際にレンダリングし、DOM要素を上から順に走査する：

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(url, wait_until="domcontentloaded", timeout=60000)
    page.wait_for_timeout(3000)  # 動的コンテンツのロードを待つ

    result = page.evaluate('''() => {
        const out = [];
        const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_ELEMENT);
        let node;
        while (node = walker.nextNode()) {
            const tag = node.tagName;
            if (['H1','H2','H3','P','IFRAME','IMG','UL','OL'].includes(tag)) {
                let info = {tag};
                if (tag === 'IFRAME') info.src = node.src;
                else if (tag === 'IMG') info.alt = node.alt;
                else info.text = (node.innerText||'').substring(0,100);
                out.push(info);
                if (out.length > 80) break;
            }
        }
        return out;
    }''')
    browser.close()
```

これにより iframe（YouTube等）の正確な位置が取得できる。

---

## 12. 翻訳時の構造忠実度ルール

翻訳時に元記事の構造を変えてはいけない。特に以下は厳守。

- **箇条書き（ul/ol）は元記事に箇条書きがある箇所にのみ使う。** 元記事が段落＋インラインboldなら、勝手にリスト化しない
- **見出し（h2/h3/h4）は元記事の見出し構造に合わせる。** 元記事でbold段落ヘッダーのものをh3/h4に昇格させない
- **画像・動画は元記事の位置に置く。** セクション冒頭ではなく、説明段落の後に来る場合が多い
- **bold（太字）は元記事でboldな箇所と一致させる。** 追加も削除もしない
- **段落の区切りも元記事に合わせる。** 段落をまとめたり分割したりしない
- **本文の欠落は禁止。** 翻訳時に段落が抜け落ちていないか必ず確認する（特に記事の末尾段落が欠落しやすい）

## 12. ユーザーの嗜好・好み

記事・UIを作るときに守るべき方針。

- **画像は横幅いっぱいに表示する。** `max-width:100%` は元サイズ以上に広がらないので使わない。`width:100%` を使う
- **視認性・ひと目でわかる構造を最優先にする。** 動画や画像が抜けていると指摘される
- **動画は省略しない。** 動画本体がなくても「ここに動画があった」とわかるプレースホルダーを必ず入れる
- **GIFはテキストリンクにしない。** `<figure><img>` で実際に表示する
- **背景は白（ライトテーマ）。** ダークモードは好まない
- **インラインCSSは書かない。** `articles/style.css` で一元管理し、個別タグに `style="..."` を追加しない
- **翻訳は省略禁止・自然な日本語で。** 要約や意訳ではなくありのままを訳す

---

## 12. 今後の拡張方針

- 記事追加時は `article_NNN.html` を作成し、`index.html` の `LOCAL_ARTICLES` に追加
- 新記事の翻訳フロー：fetch → Playwright描画 → 画像ローカル保存 → HTML生成 → 動画プレースホルダー追加
- 翻訳後は必ず元URLと見比べて、画像・動画の抜けがないか確認する
- 動画フレーム抽出は `ffmpeg` が必要（要インストール確認）
- Playwright は `pip install playwright && playwright install chromium` で使用可能
