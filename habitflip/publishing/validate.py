#!/usr/bin/env python3
"""Validate the HabitFlip publication bundle without third-party dependencies."""
import csv
import json
import re
import struct
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

APP = Path(__file__).resolve().parents[1]
WEB = APP / 'public'
PACK = APP / 'publishing'
errors = []
checks = []


def check(ok, message):
    (checks if ok else errors).append(message)


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path = path
        self.links = []
        self.ids = set()
        self.tags = []
        self.meta = {}
        self.title = False
        self.h1 = 0
        self.lang = None
        self.feed(path.read_text(encoding='utf-8'))

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append(tag)
        if tag == 'html':
            self.lang = attrs.get('lang')
        if tag == 'title':
            self.title = True
        if tag == 'h1':
            self.h1 += 1
        if tag == 'meta':
            self.meta[attrs.get('name') or attrs.get('property')] = attrs.get('content')
        if 'id' in attrs:
            check(attrs['id'] not in self.ids, f'{self.path.name}: unique ID {attrs["id"]}')
            self.ids.add(attrs['id'])
        if tag == 'img':
            check('alt' in attrs, f'{self.path.name}: image has alt attribute')
        for key in ['href', 'src']:
            if key in attrs:
                self.links.append(attrs[key])


pages = {path.resolve(): Page(path) for path in WEB.glob('*.html')}
check(len(pages) == 5, 'Five public HTML pages exist')
for path, page in pages.items():
    check(page.lang == 'en', f'{path.name}: English document language')
    check(page.title and page.h1 == 1, f'{path.name}: title and single h1')
    check(bool(page.meta.get('description')) and bool(page.meta.get('viewport')), f'{path.name}: description and viewport')
    check('script' not in page.tags and 'iframe' not in page.tags, f'{path.name}: no scripts or embedded trackers')
    for href in page.links:
        parts = urlsplit(href)
        if parts.scheme or parts.netloc:
            check(parts.scheme in ['https', 'mailto'], f'{path.name}: allowed external link scheme')
            continue
        dest = (path.parent / unquote(parts.path)).resolve() if parts.path else path
        if dest.is_dir():
            dest = dest / 'index.html'
        check(dest.exists(), f'{path.name}: local target exists: {href}')
        if parts.fragment and dest in pages:
            check(unquote(parts.fragment) in pages[dest].ids, f'{path.name}: fragment exists: {href}')
    text = path.read_text()
    check(not re.search(r'TODO|TBD|PLACEHOLDER|id123456|lorem ipsum', text, re.I), f'{path.name}: no placeholder content')

metadata = json.loads((PACK / 'app-store/metadata.json').read_text())
for field, limit in {'name': 30, 'subtitle': 30, 'promotional_text': 170, 'description': 4000}.items():
    value = metadata[field]
    check(len(value) <= limit, f'{field}: {len(value)}/{limit} characters')
keywords = metadata['keywords'].encode('utf-8')
check(len(keywords) <= 100, f'keywords: {len(keywords)}/100 bytes')
for field in ['name', 'subtitle', 'promotional_text', 'keywords', 'description', 'release_notes']:
    check((PACK / f'app-store/en-US/{field}.txt').read_text().strip() == metadata[field], f'{field}: paste-ready copy matches JSON')
for field, file in {'marketing_url': 'index.html', 'support_url': 'support.html', 'privacy_url': 'privacy.html'}.items():
    expected = 'https://ammarisme.github.io/app-docs/habitflip/' + ('' if file == 'index.html' else file)
    check(metadata[field] == expected, f'{field}: planned Pages URL matches')
for name, size in [('app-icon-1024.png', 1024), ('app-icon-256.png', 256), ('apple-touch-icon.png', 180)]:
    data = (WEB / 'assets' / name).read_bytes()
    check(data[:8] == b'\x89PNG\r\n\x1a\n' and struct.unpack('>II', data[16:24]) == (size, size), f'{name}: {size}px square PNG')
rows = list(csv.DictReader((PACK / 'screenshots.csv').open()))
check(len(rows) == 6 and [r['order'] for r in rows] == [str(i) for i in range(1, 7)], 'Six ordered screenshot scenes')
check(all(row['capture'] and row['shipping_requirement'] for row in rows), 'Screenshot capture and release requirements provided')
check(metadata['app_store_id'] is None and metadata['price'] is None, 'No invented store ID or pricing')
for message in checks:
    if any(key in message for key in ['characters', 'bytes', 'PNG', 'Five public', 'Six ordered']):
        print('PASS', message)
if errors:
    for message in errors:
        print('FAIL', message)
    raise SystemExit(1)
print(f'PASS {len(checks)} static checks. External URLs, visual layout, app tests, and live deployment are separate checks.')
