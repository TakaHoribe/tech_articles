#!/usr/bin/env python3
"""
Extract article body from a URL as structured data.

Usage:
  python tools/extract_article.py <URL>
  python tools/extract_article.py <URL> --text-only   # plain text output

Output (JSON):
  {
    "title": "...",
    "body_text": "plain text of article body",
    "body_html": "simplified HTML (p/h2/blockquote/strong only)",
    "images": [{"src": "https://...", "alt": "..."}],
    "videos": [{"type": "youtube", "id": "...", "url": "..."}]
  }

Note: JS-rendered pages (Waymo blog etc.) require Playwright and cannot be
      processed by this script. Use Playwright directly for those.
"""
import json, sys, re, hashlib
from urllib.request import urlopen, Request
from urllib.parse import urlparse, urljoin
from html.parser import HTMLParser

try:
    from bs4 import BeautifulSoup, Tag
except ImportError:
    print("ERROR: pip install beautifulsoup4", file=sys.stderr)
    sys.exit(1)

HEADERS = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120"}

# Site-specific article container selectors (tried in order)
SELECTORS = {
    "electrek.co":       ["article", ".article-content", ".post-content"],
    "aurora.tech":       ["article", "main .content", "main"],
    "ir.aurora.tech":    [".press-release", ".ir-content", "article", "main"],
    "wayve.ai":          ["article", "main", ".prose"],
}

JUNK_TAGS = ["script", "style", "nav", "header", "footer", "aside",
             "form", "button", "noscript", "figure.advertisement"]
JUNK_CLASSES = ["sidebar", "related", "comments", "share", "newsletter",
                "ad", "advertisement", "cookie", "subscribe", "popup"]

YT_PATTERN = re.compile(r'(?:youtube\.com/embed/|youtu\.be/)([A-Za-z0-9_-]{11})')


def fetch_html(url):
    req = Request(url, headers=HEADERS)
    with urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", errors="replace")


def find_body(soup, url):
    host = urlparse(url).hostname or ""
    for domain, selectors in SELECTORS.items():
        if domain in host:
            for sel in selectors:
                el = soup.select_one(sel)
                if el:
                    return el
    # Generic fallback: article > main > body
    for sel in ["article", "main", '[role="main"]']:
        el = soup.select_one(sel)
        if el and len(el.get_text(strip=True)) > 200:
            return el
    return soup.find("body")


def clean(soup_el):
    for tag in soup_el(JUNK_TAGS):
        tag.decompose()
    for cls in JUNK_CLASSES:
        for el in soup_el.find_all(class_=re.compile(cls, re.I)):
            el.decompose()
    return soup_el


def extract_videos(soup):
    videos = []
    for iframe in soup.find_all("iframe"):
        src = iframe.get("src", "")
        m = YT_PATTERN.search(src)
        if m:
            vid_id = m.group(1)
            videos.append({
                "type": "youtube",
                "id": vid_id,
                "url": f"https://www.youtube.com/watch?v={vid_id}",
                "thumb": f"https://img.youtube.com/vi/{vid_id}/maxresdefault.jpg",
            })
    return videos


def simplify_html(el):
    KEEP = {"h1", "h2", "h3", "h4", "p", "ul", "ol", "li",
            "blockquote", "strong", "em", "a", "figure", "img", "figcaption"}
    for tag in el.find_all(True):
        if tag.name not in KEEP:
            tag.unwrap()
    return str(el)


def extract(url):
    html = fetch_html(url)
    soup = BeautifulSoup(html, "html.parser")

    title_el = soup.find("h1") or soup.find("title")
    title = title_el.get_text(strip=True) if title_el else ""

    videos = extract_videos(soup)  # before cleaning removes iframes

    body = find_body(soup, url)
    body = clean(body)

    images = []
    base = f"{urlparse(url).scheme}://{urlparse(url).hostname}"
    for img in body.find_all("img"):
        src = img.get("src") or img.get("data-src") or img.get("data-lazy-src") or ""
        if not src or src.endswith(".svg") or "icon" in src.lower() or "logo" in src.lower():
            continue
        if src.startswith("//"):
            src = "https:" + src
        elif src.startswith("/"):
            src = base + src
        images.append({"src": src, "alt": img.get("alt", "")})

    return {
        "title": title,
        "url": url,
        "body_text": body.get_text(separator="\n", strip=True),
        "body_html": simplify_html(body),
        "images": images,
        "videos": videos,
    }


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("url")
    p.add_argument("--text-only", action="store_true", help="Output plain text instead of JSON")
    args = p.parse_args()

    result = extract(args.url)
    if args.text_only:
        print(result["body_text"])
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2))
