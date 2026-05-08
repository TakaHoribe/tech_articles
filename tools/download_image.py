#!/usr/bin/env python3
"""
Download a single image (or list of images) to articles/images/ using the project naming convention.
Supplements the batch download_images.py in the project root.

Usage:
  # Single URL
  python tools/download_image.py https://example.com/photo.jpg

  # Multiple URLs
  python tools/download_image.py https://... https://... https://...

  # YouTube thumbnail by video ID
  python tools/download_image.py --yt VIDEO_ID

  # From extract_article.py JSON (download all images in result)
  python tools/extract_article.py https://... | python tools/download_image.py --stdin-json

Output:
  One line per image: "<local_filename>  <original_url>"
  Use the local_filename in <img src="./images/FILENAME"> tags.
"""
import hashlib, json, sys, mimetypes
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.parse import urlparse

IMAGES_DIR = Path(__file__).parent.parent / "articles" / "images"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120",
    "Accept": "image/avif,image/webp,image/apng,image/*,*/*;q=0.8",
}


def filename_for(url: str) -> str:
    h = hashlib.md5(url.encode()).hexdigest()[:12]
    path = urlparse(url).path.split("?")[0]
    ext = Path(path).suffix.lower()
    if ext not in (".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"):
        ext = ".jpg"
    return f"{h}_img{ext}"


def download(url: str, out_dir: Path = IMAGES_DIR) -> str | None:
    if url.startswith("//"):
        url = "https:" + url
    out_dir.mkdir(parents=True, exist_ok=True)
    fname = filename_for(url)
    out = out_dir / fname
    if out.exists():
        print(f"SKIP (exists)  {fname}  {url[:70]}", file=sys.stderr)
        return fname
    try:
        req = Request(url, headers=HEADERS)
        with urlopen(req, timeout=30) as r:
            ct = r.headers.get("Content-Type", "")
            data = r.read()
        if len(data) < 200:
            print(f"ERR (too small)  {url[:70]}", file=sys.stderr)
            return None
        # Fix extension from Content-Type if unclear
        if Path(fname).suffix == ".jpg" and "png" in ct:
            fname = fname[:-4] + ".png"
            out = out_dir / fname
        out.write_bytes(data)
        print(f"OK  {fname}  ({len(data)//1024}KB)  {url[:70]}", file=sys.stderr)
        return fname
    except Exception as e:
        print(f"ERR  {url[:70]}: {e}", file=sys.stderr)
        return None


def youtube_thumb(video_id: str, out_dir: Path = IMAGES_DIR) -> str | None:
    for res in ("maxresdefault", "hqdefault"):
        url = f"https://img.youtube.com/vi/{video_id}/{res}.jpg"
        fname = f"yt_{video_id}_{res}.jpg"
        out = out_dir / fname
        if out.exists():
            print(f"SKIP (exists)  {fname}", file=sys.stderr)
            return fname
        try:
            req = Request(url, headers=HEADERS)
            with urlopen(req, timeout=15) as r:
                data = r.read()
            if len(data) < 1000:
                continue
            out.write_bytes(data)
            print(f"OK  {fname}  ({len(data)//1024}KB)  YouTube:{video_id}", file=sys.stderr)
            return fname
        except Exception:
            continue
    return None


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("urls", nargs="*")
    p.add_argument("--yt", metavar="VIDEO_ID", help="Download YouTube thumbnail")
    p.add_argument("--stdin-json", action="store_true", help="Read extract_article.py JSON from stdin")
    p.add_argument("--dir", default=str(IMAGES_DIR))
    args = p.parse_args()

    out_dir = Path(args.dir)
    results = {}

    if args.yt:
        fname = youtube_thumb(args.yt, out_dir)
        if fname:
            print(f"{fname}  yt:{args.yt}")

    elif args.stdin_json:
        data = json.loads(sys.stdin.read())
        for img in data.get("images", []):
            fname = download(img["src"], out_dir)
            if fname:
                results[img["src"]] = fname
                print(f"{fname}  {img['src']}")
        for vid in data.get("videos", []):
            if vid.get("type") == "youtube":
                fname = youtube_thumb(vid["id"], out_dir)
                if fname:
                    results[vid["url"]] = fname
                    print(f"{fname}  yt:{vid['id']}")

    else:
        for url in args.urls:
            fname = download(url, out_dir)
            if fname:
                print(f"{fname}  {url}")
