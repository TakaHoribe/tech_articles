#!/usr/bin/env python3
"""Download external images from article HTML files and rewrite src to local paths."""
import os, re, hashlib, urllib.request, urllib.parse, mimetypes

ARTICLES_DIR = os.path.dirname(os.path.abspath(__file__)) + '/articles'
IMAGES_DIR   = ARTICLES_DIR + '/images'
os.makedirs(IMAGES_DIR, exist_ok=True)

# Match src="..." or src='...' including protocol-relative //
IMG_RE = re.compile(r'''src=["']((?:https?:)?//[^"']+)["']''')

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36',
    'Referer': 'https://waymo.com/',
    'Accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
}

def ext_from_url(url, content_type=None):
    path = urllib.parse.urlparse(url).path
    _, e = os.path.splitext(path)
    if e.lower() in ('.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg'):
        return e.lower()
    if content_type:
        g = mimetypes.guess_extension(content_type.split(';')[0].strip())
        if g:
            return g
    return '.jpg'

def download(url):
    if url.startswith('//'):
        url = 'https:' + url
    h = hashlib.md5(url.encode()).hexdigest()[:12]
    # check if already downloaded
    for f in os.listdir(IMAGES_DIR):
        if f.startswith(h + '_'):
            return './images/' + f
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=20) as resp:
            ct = resp.headers.get('Content-Type', '')
            e = ext_from_url(url, ct)
            fname = h + '_img' + e
            data = resp.read()
        with open(IMAGES_DIR + '/' + fname, 'wb') as f:
            f.write(data)
        print(f'  OK  {fname}  ({len(data)//1024}KB)  {url[:80]}')
        return './images/' + fname
    except Exception as ex:
        print(f'  ERR {url[:80]}: {ex}')
        return None

html_files = sorted(f for f in os.listdir(ARTICLES_DIR) if re.match(r'article_0\d+\.html', f))

for hf in html_files:
    path = ARTICLES_DIR + '/' + hf
    with open(path, encoding='utf-8') as f:
        html = f.read()

    urls = IMG_RE.findall(html)
    if not urls:
        print(f'{hf}: no images')
        continue

    print(f'\n{hf}: {len(urls)} image(s)')
    changed = False
    for url in urls:
        local = download(url)
        if local:
            orig = url  # may be //... or https://...
            # replace both quoted forms
            html = html.replace(f'src="{orig}"', f'src="{local}"')
            html = html.replace(f"src='{orig}'", f"src='{local}'")
            changed = True

    if changed:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'  -> {hf} updated')

print('\nDone.')
