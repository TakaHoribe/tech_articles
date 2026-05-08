#!/usr/bin/env python3
"""Replace broken/unfetchable img tags with styled placeholders, and add onerror to all remaining external imgs."""
import os, re, urllib.request

ARTICLES_DIR = os.path.dirname(os.path.abspath(__file__)) + '/articles'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36',
    'Referer': 'https://waymo.com/',
}

PLACEHOLDER_CSS = """
<style>
.img-placeholder{display:flex;flex-direction:column;align-items:center;justify-content:center;
background:var(--s);border:1px solid var(--bd);border-radius:8px;padding:24px;margin:16px 0;
min-height:120px;text-align:center;gap:8px}
.img-placeholder .ip-icon{font-size:2rem;opacity:.5}
.img-placeholder .ip-label{font-size:.8rem;color:var(--m);font-style:italic}
</style>"""

def check_url(url):
    """Returns True if URL is reachable."""
    if url.startswith('//'):
        url = 'https:' + url
    try:
        req = urllib.request.Request(url, headers=HEADERS, method='HEAD')
        with urllib.request.urlopen(req, timeout=8) as r:
            return r.status == 200
    except:
        return False

def placeholder(alt):
    alt_text = alt if alt else '画像'
    return f'<div class="img-placeholder"><div class="ip-icon">🖼️</div><div class="ip-label">{alt_text}</div></div>'

def process_file(path):
    with open(path, encoding='utf-8') as f:
        html = f.read()

    # Already has placeholder CSS?
    has_placeholder_css = 'img-placeholder' in html
    changed = False

    # Find all img tags
    img_re = re.compile(r'<img([^>]*)>', re.DOTALL)

    def fix_img(m):
        nonlocal changed
        attrs = m.group(1)
        # Extract src
        src_m = re.search(r'''src=["']((?:https?:)?//[^"']+)["']''', attrs)
        if not src_m:
            return m.group(0)  # no external src, leave alone
        src = src_m.group(1)
        full_src = 'https:' + src if src.startswith('//') else src

        # Extract alt
        alt_m = re.search(r'''alt=["']([^"']*)["']''', attrs)
        alt = alt_m.group(1) if alt_m else ''

        # Skip local paths
        if src.startswith('./') or src.startswith('../') or src.startswith('/images/'):
            return m.group(0)

        # Check if reachable
        if check_url(full_src):
            # Add onerror if not present
            if 'onerror' not in attrs:
                changed = True
                return f'<img{attrs} onerror="this.style.display=\'none\'">'
            return m.group(0)
        else:
            # Replace with placeholder
            print(f'  BROKEN -> placeholder: {full_src[:80]}')
            changed = True
            return placeholder(alt)

    new_html = img_re.sub(fix_img, html)

    if changed and not has_placeholder_css and '<div class="img-placeholder">' in new_html:
        # Insert placeholder CSS before </style>
        new_html = new_html.replace('</style>', PLACEHOLDER_CSS + '</style>', 1)

    if changed:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_html)
        return True
    return False

html_files = sorted(f for f in os.listdir(ARTICLES_DIR) if re.match(r'article_0\d+\.html', f))
for hf in html_files:
    path = ARTICLES_DIR + '/' + hf
    print(f'\n{hf}:')
    changed = process_file(path)
    if not changed:
        print('  no changes needed')

print('\nDone.')
