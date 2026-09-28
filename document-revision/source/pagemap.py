"""Render a docx with LibreOffice and map each heading to its printed page number.

Usage: python3 pagemap.py doc.docx headings.json out_pages.json
The body section restarts numbering at 1; front-matter pages carry roman numerals.
"""
import json
import re
import subprocess
import sys
import shutil
from pathlib import Path

docx, headings_json, out_json = sys.argv[1:4]
work = Path('/tmp/lotest/pm')
if work.exists():
    shutil.rmtree(work)
work.mkdir(parents=True)
shutil.copy(docx, work / 'd.docx')
subprocess.run(['soffice', '-env:UserInstallation=file:///tmp/lotest/profile', '--headless',
                '--convert-to', 'pdf', '--outdir', str(work), str(work / 'd.docx')],
               check=True, capture_output=True, timeout=300)
pdf = work / 'd.pdf'
info = subprocess.run(['pdfinfo', str(pdf)], capture_output=True, text=True).stdout
npages = int(re.search(r'Pages:\s+(\d+)', info).group(1))
headings = json.loads(Path(headings_json).read_text(encoding='utf-8'))


def norm(s):
    return re.sub(r'\s+', '', s)


page_text = []
for i in range(1, npages + 1):
    t = subprocess.run(['pdftotext', '-layout', '-f', str(i), '-l', str(i), str(pdf), '-'],
                       capture_output=True, text=True).stdout
    page_text.append(t)

# printed page number: last non-empty line of the page (footer)
printed = []
for t in page_text:
    lines = [l.strip() for l in t.splitlines() if l.strip()]
    printed.append(lines[-1] if lines else '')

result = {}
start = 0
# skip front matter pages (roman numerals / title page) when searching
first_body = next(i for i, p in enumerate(printed) if p == '1')
cur = first_body
for k, h in enumerate(headings):
    target = norm(h['text'])
    found = None
    for i in range(cur, npages):
        if target in norm(page_text[i]):
            found = i
            break
    if found is None:
        print('NOT FOUND:', h['text'])
        continue
    result[str(k)] = printed[found]
    cur = found
Path(out_json).write_text(json.dumps(result, ensure_ascii=False, indent=1))
print('pages:', npages, 'first body page index:', first_body, 'mapped:', len(result), '/', len(headings))
