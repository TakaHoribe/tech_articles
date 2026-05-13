#!/usr/bin/env python3
"""
Fetch arXiv paper content (HTML version) and extract structured data + figures.

Usage:
  python tools/fetch_arxiv.py 2503.20523
  python tools/fetch_arxiv.py 2503.20523 --download-figs
  python tools/fetch_arxiv.py 2503.20523 --download-figs --text-only

Output (JSON):
  {
    "arxiv_id": "...",
    "title": "...",
    "authors": ["..."],
    "abstract": "...",
    "sections": [{"heading": "...", "text": "..."}],
    "figures": [{"url": "...", "caption": "...", "local": "filename.png"}]
  }

Note: Uses arxiv.org/html/{ID} which is static — no Playwright needed.
      Figure images are downloaded to articles/images/ when --download-figs is set.
"""
import json, sys, re, hashlib
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.parse import urljoin

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("ERROR: pip install beautifulsoup4", file=sys.stderr)
    sys.exit(1)

HEADERS = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120"}
IMAGES_DIR = Path(__file__).parent.parent / "articles" / "images"


def fetch(url):
    req = Request(url, headers=HEADERS)
    with urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", errors="replace")


def download_image(url, img_dir=IMAGES_DIR):
    img_dir.mkdir(parents=True, exist_ok=True)
    h = hashlib.md5(url.encode()).hexdigest()[:12]
    ext = Path(url.split("?")[0]).suffix or ".png"
    local = img_dir / f"{h}_img{ext}"
    if local.exists():
        return local.name
    try:
        req = Request(url, headers=HEADERS)
        data = urlopen(req, timeout=30).read()
        if len(data) < 500:
            return None
        local.write_bytes(data)
        print(f"  DL {local.name}  {url[:70]}", file=sys.stderr)
        return local.name
    except Exception as e:
        print(f"  ERR {url[:70]}: {e}", file=sys.stderr)
        return None


def fetch_arxiv(arxiv_id, download_figs=False, img_dir=IMAGES_DIR):
    html_url = f"https://arxiv.org/html/{arxiv_id}"
    html = fetch(html_url)
    soup = BeautifulSoup(html, "html.parser")
    base_url = html_url + "/"

    # Title
    title_el = (soup.find("h1", class_="ltx_title") or
                soup.find("title") or
                soup.find("h1"))
    title = title_el.get_text(strip=True) if title_el else ""
    # arXiv HTML titles often have "HTML" appended
    title = title.replace(" [HTML]", "").replace(" HTML", "").strip()

    # Authors
    authors = [a.get_text(strip=True) for a in soup.find_all("span", class_="ltx_personname")]
    if not authors:
        authors = [a.get_text(strip=True) for a in soup.find_all(class_=["author", "ltx_creator"])]

    # Abstract
    abstract_el = (soup.find("div", class_="ltx_abstract") or
                   soup.find("blockquote", class_="abstract") or
                   soup.find(id="abstract"))
    abstract = abstract_el.get_text(strip=True) if abstract_el else ""

    # Sections — collect heading + first few paragraphs
    sections = []
    for heading in soup.find_all(["h2", "h3"]):
        h_text = heading.get_text(strip=True)
        if not h_text or len(h_text) < 2:
            continue
        paras = []
        for sib in heading.find_next_siblings():
            if sib.name in ("h2", "h3"):
                break
            if sib.name == "p":
                t = sib.get_text(strip=True)
                if t:
                    paras.append(t)
            # arXiv HTML wraps paragraphs in <div class="ltx_para"><p>…</p></div>
            elif sib.name == "div" and "ltx_para" in sib.get("class", []):
                for p in sib.find_all("p", recursive=True):
                    t = p.get_text(strip=True)
                    if t:
                        paras.append(t)
            if len(paras) >= 6:
                break
        sections.append({"heading": h_text, "text": "\n".join(paras)})

    # Figures
    figures = []
    for fig in soup.find_all("figure"):
        img = fig.find("img")
        cap = fig.find("figcaption")
        if not img:
            continue
        src = img.get("src", "")
        if not src:
            continue
        if not src.startswith("http"):
            src = urljoin(base_url, src)
        fig_data = {
            "url": src,
            "caption": cap.get_text(strip=True) if cap else "",
            "local": None,
        }
        if download_figs:
            fig_data["local"] = download_image(src, img_dir)
        figures.append(fig_data)

    return {
        "arxiv_id": arxiv_id,
        "url": f"https://arxiv.org/abs/{arxiv_id}",
        "html_url": html_url,
        "title": title,
        "authors": authors,
        "abstract": abstract,
        "sections": sections,
        "figures": figures,
    }


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("arxiv_id")
    p.add_argument("--download-figs", action="store_true", help="Download figures to articles/images/")
    p.add_argument("--dir", default=str(IMAGES_DIR), help="Image output directory")
    p.add_argument("--text-only", action="store_true", help="Output abstract + sections as plain text")
    args = p.parse_args()

    result = fetch_arxiv(args.arxiv_id, args.download_figs, Path(args.dir))

    if args.text_only:
        print(f"# {result['title']}")
        print(f"Authors: {', '.join(result['authors'])}\n")
        print(f"## Abstract\n{result['abstract']}\n")
        for sec in result["sections"]:
            print(f"## {sec['heading']}\n{sec['text']}\n")
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2))
