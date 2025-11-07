#!/usr/bin/env python3
# filepath: download_images.py

import re
import os
import json
import base64
import requests
from urllib.parse import urlparse, urljoin
import time

def extract_from_markdown_text(text):
    """Return (http_urls, data_urls) found in markdown/html text."""
    urls = []
    # Pattern for markdown images: ![alt](url)
    md_pattern = r'!\[.*?\]\((.*?)\)'
    md_urls = re.findall(md_pattern, text)
    urls.extend(md_urls)

    # Pattern for HTML img tags: <img src="url">
    html_pattern = r'<img[^>]+src=["\']([^"\']+)["\']'
    html_urls = re.findall(html_pattern, text)
    urls.extend(html_urls)

    http_urls = [u for u in urls if u.startswith('http')]
    data_urls = [u for u in urls if u.startswith('data:')]

    return http_urls, data_urls

def decode_data_url(data_url):
    """Decode data URL like data:image/png;base64,.... -> (bytes, ext)"""
    m = re.match(r'data:(image/[^;]+);base64,(.+)', data_url, re.S)
    if not m:
        return None, None
    mime, b64 = m.group(1), m.group(2)
    try:
        raw = base64.b64decode(b64.encode('utf-8'))
    except Exception:
        # try to sanitize whitespace/newlines
        raw = base64.b64decode(re.sub(r'\s+', '', b64).encode('utf-8'))
    # derive extension
    ext = {
        'image/png': '.png',
        'image/jpeg': '.jpg',
        'image/jpg': '.jpg',
        'image/gif': '.gif',
        'image/svg+xml': '.svg'
    }.get(mime, '')
    return raw, ext

def extract_from_ipynb(nb_file):
    """
    Extract external http URLs and embedded images (attachments/outputs/data: URIs)
    from a notebook. Returns (set(http_urls), list(embedded_images))
    embedded_images: list of dict { 'data': bytes, 'filename': suggested_filename }
    """
    http_urls = set()
    embedded = []
    base_name = os.path.splitext(os.path.basename(nb_file))[0]

    try:
        with open(nb_file, 'r', encoding='utf-8') as f:
            nb = json.load(f)
    except Exception as e:
        print(f"✗ Failed to read notebook {nb_file}: {e}")
        return http_urls, embedded

    cells = nb.get('cells', [])
    for ci, cell in enumerate(cells):
        cell_type = cell.get('cell_type', '')
        # Source text may be a list or a single string
        source = cell.get('source', '')
        if isinstance(source, list):
            source = ''.join(source)
        if cell_type == 'markdown':
            h_urls, d_urls = extract_from_markdown_text(source)
            http_urls.update(h_urls)
            for d in d_urls:
                raw, ext = decode_data_url(d)
                if raw is not None:
                    fname = f"{base_name}_cell{ci}_embedded{len(embedded)}{ext or '.png'}"
                    embedded.append({'data': raw, 'filename': fname})
        # Attachments (jupyter markdown attachments)
        attachments = cell.get('attachments', {}) or {}
        for attach_name, attach_val in attachments.items():
            # attach_val may be dict of mime->b64 or a single b64 string
            if isinstance(attach_val, dict):
                for mime, b64 in attach_val.items():
                    try:
                        raw = base64.b64decode(b64.encode('utf-8'))
                    except Exception:
                        raw = base64.b64decode(re.sub(r'\s+', '', b64).encode('utf-8'))
                    ext = {
                        'image/png': '.png',
                        'image/jpeg': '.jpg',
                        'image/jpg': '.jpg',
                        'image/gif': '.gif',
                        'image/svg+xml': '.svg'
                    }.get(mime, os.path.splitext(attach_name)[1] or '.png')
                    fname = f"{base_name}_cell{ci}_{attach_name}"
                    if not os.path.splitext(fname)[1]:
                        fname += ext
                    embedded.append({'data': raw, 'filename': fname})
            else:
                # if it's a string, assume base64 of a png
                try:
                    raw = base64.b64decode(attach_val.encode('utf-8'))
                    fname = f"{base_name}_cell{ci}_{attach_name}"
                    if not os.path.splitext(fname)[1]:
                        fname += '.png'
                    embedded.append({'data': raw, 'filename': fname})
                except Exception:
                    continue

        # Outputs for code cells: check data.image/png or image/jpeg
        outputs = cell.get('outputs', []) or []
        for oi, out in enumerate(outputs):
            data = out.get('data', {}) or {}
            for mime_key in ('image/png', 'image/jpeg', 'image/jpg', 'image/gif', 'image/svg+xml'):
                if mime_key in data:
                    val = data[mime_key]
                    if isinstance(val, list):
                        val = ''.join(val)
                    b64 = val
                    try:
                        raw = base64.b64decode(b64.encode('utf-8'))
                    except Exception:
                        raw = base64.b64decode(re.sub(r'\s+', '', b64).encode('utf-8'))
                    ext = {
                        'image/png': '.png',
                        'image/jpeg': '.jpg',
                        'image/jpg': '.jpg',
                        'image/gif': '.gif',
                        'image/svg+xml': '.svg'
                    }.get(mime_key, '.png')
                    fname = f"{base_name}_cell{ci}_out{oi}{ext}"
                    embedded.append({'data': raw, 'filename': fname})
            # Sometimes text outputs may contain HTML with <img src="...">
            if 'text/html' in data:
                html = data['text/html']
                if isinstance(html, list):
                    html = ''.join(html)
                h_urls, d_urls = extract_from_markdown_text(html)
                http_urls.update(h_urls)
                for d in d_urls:
                    raw, ext = decode_data_url(d)
                    if raw is not None:
                        fname = f"{base_name}_cell{ci}_embedded{len(embedded)}{ext or '.png'}"
                        embedded.append({'data': raw, 'filename': fname})

    return http_urls, embedded

def extract_image_urls_from_md(md_file):
    """Extract http URLs and data: URLs from markdown file"""
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"✗ Failed to read markdown {md_file}: {e}")
        return set(), []

    http_urls, data_urls = extract_from_markdown_text(content)
    embedded = []
    for d in data_urls:
        raw, ext = decode_data_url(d)
        if raw is not None:
            base = os.path.splitext(os.path.basename(md_file))[0]
            fname = f"{base}_embedded{len(embedded)}{ext or '.png'}"
            embedded.append({'data': raw, 'filename': fname})

    return set(http_urls), embedded

def save_embedded_image(data_bytes, output_dir, filename):
    """Save raw bytes to output_dir/filename, skip if exists"""
    output_path = os.path.join(output_dir, filename)
    # make unique if name collision
    base, ext = os.path.splitext(output_path)
    i = 1
    while os.path.exists(output_path):
        output_path = f"{base}_{i}{ext}"
        i += 1
    try:
        with open(output_path, 'wb') as f:
            f.write(data_bytes)
        print(f"✓ Saved embedded: {os.path.basename(output_path)}")
        return True
    except Exception as e:
        print(f"✗ Failed to save embedded {filename}: {e}")
        return False

def download_image(url, output_dir):
    """Download an image from URL"""
    try:
        # Parse URL to get filename
        parsed = urlparse(url)
        filename = os.path.basename(parsed.path)
        # If no filename, create one from URL
        if not filename or '.' not in filename:
            filename = f"image_{abs(hash(url)) % 100000}.jpg"

        # Create output path
        output_path = os.path.join(output_dir, filename)

        # Skip if file already exists
        if os.path.exists(output_path):
            print(f"✓ Already exists: {filename}")
            return True

        # Download the image
        print(f"Downloading: {filename}")
        response = requests.get(url, stream=True, timeout=30)
        response.raise_for_status()

        # Save the image
        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        print(f"✓ Downloaded: {filename}")
        return True

    except Exception as e:
        print(f"✗ Failed to download {url}: {e}")
        return False

def main():
    # Configuration
    book_dir = "book"
    output_dir = "downloaded_images"

    # Create output directory
    os.makedirs(output_dir, exist_ok=True)

    # Find all markdown and ipynb files
    md_files = []
    nb_files = []
    for file in os.listdir(book_dir):
        if file.endswith('.md'):
            md_files.append(os.path.join(book_dir, file))
        elif file.endswith('.ipynb'):
            nb_files.append(os.path.join(book_dir, file))

    if not md_files and not nb_files:
        print("No markdown or notebook files found in book/ directory")
        return

    print(f"Found {len(md_files)} markdown files and {len(nb_files)} notebooks")

    all_http_urls = set()
    embedded_images = []

    # Process markdown files
    for md in md_files:
        print(f"\nProcessing markdown: {md}")
        h_urls, embeds = extract_image_urls_from_md(md)
        if h_urls:
            print(f"  Found {len(h_urls)} external image URLs")
            for u in h_urls:
                print(f"    {u}")
            all_http_urls.update(h_urls)
        if embeds:
            print(f"  Found {len(embeds)} embedded images in markdown")
            for e in embeds:
                print(f"    (embedded) {e['filename']}")
            embedded_images.extend(embeds)

    # Process notebooks
    for nb in nb_files:
        print(f"\nProcessing notebook: {nb}")
        h_urls, embeds = extract_from_ipynb(nb)
        if h_urls:
            print(f"  Found {len(h_urls)} external image URLs")
            for u in h_urls:
                print(f"    {u}")
            all_http_urls.update(h_urls)
        if embeds:
            print(f"  Found {len(embeds)} embedded images in notebook")
            for e in embeds:
                print(f"    (embedded) {e['filename']}")
            embedded_images.extend(embeds)

    if not all_http_urls and not embedded_images:
        print("\nNo image URLs or embedded images found")
        return

    print(f"\n{'='*50}")
    print(f"Total unique external image URLs: {len(all_http_urls)}")
    print(f"Total embedded images to save: {len(embedded_images)}")
    print(f"Downloading to: {output_dir}")
    print(f"{'='*50}")

    # Download external images
    success_count = 0
    for i, url in enumerate(sorted(all_http_urls), 1):
        print(f"\n[{i}/{len(all_http_urls)}]", end=" ")
        if download_image(url, output_dir):
            success_count += 1
        time.sleep(1)

    # Save embedded images
    saved_count = 0
    for e in embedded_images:
        if save_embedded_image(e['data'], output_dir, e['filename']):
            saved_count += 1

    print(f"\n{'='*50}")
    print(f"Download complete!")
    print(f"Successfully downloaded external: {success_count}/{len(all_http_urls)}")
    print(f"Saved embedded images: {saved_count}/{len(embedded_images)}")
    print(f"Images saved to: {output_dir}/")

if __name__ == "__main__":
    main()