"""Check the generated site's routes, content, assets, and contact exposure."""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlsplit, unquote
import re

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path, self.ids, self.links, self.images = path, [], [], []
        self.h1 = self.active = self.courses = self.entries = 0
        self.canonical = None
    def handle_starttag(self, tag, attributes):
        a = dict(attributes)
        if 'id' in a: self.ids.append(a['id'])
        if tag == 'h1': self.h1 += 1
        if a.get('aria-current') == 'page': self.active += 1
        if 'course' in a.get('class', '').split(): self.courses += 1
        if 'journey-entry' in a.get('class', '').split(): self.entries += 1
        for key in ['href', 'src']:
            if a.get(key): self.links.append(a[key])
        if tag == 'link' and a.get('rel') == 'canonical': self.canonical = a.get('href')
        if tag == 'img':
            assert a.get('alt'), f'Missing alt text in {self.path}'
            assert a.get('width') and a.get('height'), f'Missing image dimensions in {self.path}'
            self.images.append(a['src'])

root = Path('_site').resolve()
pages = {}
for path in root.rglob('*.html'):
    key = '/' + path.relative_to(root).as_posix()
    source = path.read_text()
    page = Page(key)
    page.feed(source)
    pages[key] = page
    assert page.h1 == 1, f'Expected one h1: {key}'
    assert len(page.ids) == len(set(page.ids)), f'Duplicate IDs: {key}'
    expected = key.removesuffix('index.html')
    assert page.canonical == 'https://ahmadamine998.github.io' + expected, f'Canonical: {key}'
    assert page.active == (0 if key == '/404.html' else 1), f'Current navigation: {key}'
    assert not re.search(r'[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}', source), f'Raw email: {key}'
    assert 'mailto:' not in source, f'Initial mail link: {key}'
    assert '{{' not in source and '{%' not in source, f'Unprocessed template: {key}'
    assert 'noindex' not in source.lower(), f'Indexing disabled: {key}'

assert set(pages) == {'/index.html', '/research/index.html', '/teaching/index.html',
                      '/community/index.html', '/journey/index.html', '/404.html'}
for key, page in pages.items():
    for link in page.links:
        parts = urlsplit(link)
        if parts.scheme or parts.netloc: continue
        target = urlsplit(urljoin(key, link))
        path = root / unquote(target.path).lstrip('/')
        if path.is_dir(): path /= 'index.html'
        assert path.is_relative_to(root) and path.exists(), f'Broken link {key}: {link}'
        if target.fragment:
            dest = '/' + path.relative_to(root).as_posix()
            if dest in pages: assert target.fragment in pages[dest].ids, f'Broken anchor {key}: {link}'

papers = ['fail','ad-mpcc','stl-svpio','nonplanar','sit-lmpc','ensemble-gp','vahr','friction-estimation','poseinn']
assert all(p in pages['/research/index.html'].ids for p in papers), 'Missing publication'
assert pages['/teaching/index.html'].courses == 6
assert pages['/journey/index.html'].entries == 13
teaching = (root/'teaching/index.html').read_text()
assert 'co-instructor' not in teaching.lower()
assert not re.search(r'<a[^>]+href="[^"]*(?:syllabus|slides|lecture|materials)', teaching, re.I)
css_path = root/'assets/css/portfolio.css'
for asset in re.findall(r'url\([\'"]?([^\)\'\"]+)', css_path.read_text()):
    if not urlsplit(asset).scheme: assert (css_path.parent/asset).exists(), f'Missing font: {asset}'
print(f'Passed: {len(pages)} pages, {sum(len(p.links) for p in pages.values())} links/assets, '
      'nine papers, six courses, 13 journey entries, no exposed email in HTML.')
