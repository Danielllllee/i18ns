"""Add heading bookmarks and a real Word TOC field (with cached entries) to the built docx.

Usage: python3 postprocess.py in.docx out.docx headings.json [toc_pages.json]
"""
import json
import re
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape

src, dst, headings_json = sys.argv[1], sys.argv[2], sys.argv[3]
pages = json.loads(Path(sys.argv[4]).read_text()) if len(sys.argv) > 4 and Path(sys.argv[4]).exists() else {}
headings = json.loads(Path(headings_json).read_text(encoding='utf-8'))

tmp = Path(tempfile.mkdtemp())
with zipfile.ZipFile(src) as z:
    z.extractall(tmp)
doc_path = tmp / 'word' / 'document.xml'
xml = doc_path.read_text(encoding='utf-8')

# 1) bookmarks on headings, in document order
counter = {'n': 0}
BM_BASE = 100


def add_bookmark(m):
    k = counter['n']
    counter['n'] += 1
    name = f'_Toc{BM_BASE + k:06d}'
    ppr_end = m.group(1)
    rest = m.group(2)
    return f'{ppr_end}<w:bookmarkStart w:id="{BM_BASE + k}" w:name="{name}"/>{rest}<w:bookmarkEnd w:id="{BM_BASE + k}"/></w:p>'


heading_para = re.compile(
    r'(<w:p>(?:(?!</w:p>).)*?<w:pStyle w:val="Heading[12]"/>(?:(?!</w:p>).)*?</w:pPr>)((?:(?!</w:p>).)*?)</w:p>',
    re.S)
xml = heading_para.sub(add_bookmark, xml)
assert counter['n'] == len(headings), (counter['n'], len(headings))

# 2) TOC entries
TEXT_W = 8306


def entry_xml(k, h, first, last):
    style = 'TOC1' if h['level'] == 1 else 'TOC2'
    name = f'_Toc{BM_BASE + k:06d}'
    page = str(pages.get(str(k), '0'))
    lead = ''
    if first:
        lead = ('<w:r><w:fldChar w:fldCharType="begin"/></w:r>'
                '<w:r><w:instrText xml:space="preserve"> TOC \\o "1-2" \\h \\z \\u </w:instrText></w:r>'
                '<w:r><w:fldChar w:fldCharType="separate"/></w:r>')
    tail = '<w:r><w:fldChar w:fldCharType="end"/></w:r>' if last else ''
    return (f'<w:p><w:pPr><w:pStyle w:val="{style}"/>'
            f'<w:tabs><w:tab w:val="right" w:leader="dot" w:pos="{TEXT_W}"/></w:tabs></w:pPr>'
            f'{lead}'
            f'<w:hyperlink w:anchor="{name}" w:history="1">'
            f'<w:r><w:t xml:space="preserve">{escape(h["text"])}</w:t></w:r>'
            f'<w:r><w:tab/></w:r>'
            f'<w:r><w:fldChar w:fldCharType="begin"/></w:r>'
            f'<w:r><w:instrText xml:space="preserve"> PAGEREF {name} \\h </w:instrText></w:r>'
            f'<w:r><w:fldChar w:fldCharType="separate"/></w:r>'
            f'<w:r><w:t>{page}</w:t></w:r>'
            f'<w:r><w:fldChar w:fldCharType="end"/></w:r>'
            f'</w:hyperlink>{tail}</w:p>')


n = len(headings)
for k, h in enumerate(headings):
    pat = re.compile(r'<w:p>(?:(?!</w:p>).)*?\{\{TOCENTRY:' + str(k) + r'\}\}(?:(?!</w:p>).)*?</w:p>', re.S)
    xml, cnt = pat.subn(lambda _m: entry_xml(k, h, k == 0, k == n - 1), xml, count=1)
    assert cnt == 1, f'placeholder {k} not found'

assert '{{TOCENTRY' not in xml
doc_path.write_text(xml, encoding='utf-8')

# 3) settings: keep Word from auto-updating fields on open (cached TOC is shown as-is)
settings = tmp / 'word' / 'settings.xml'
s = settings.read_text(encoding='utf-8')
s = s.replace('<w:updateFields w:val="true"/>', '')
settings.write_text(s, encoding='utf-8')

# 4) core properties: language
core = tmp / 'docProps' / 'core.xml'
c = core.read_text(encoding='utf-8')
if '<dc:language>' not in c:
    c = c.replace('</cp:coreProperties>', '<dc:language>zh-CN</dc:language></cp:coreProperties>')
core.write_text(c, encoding='utf-8')

# rezip with [Content_Types].xml first
out = Path(dst)
if out.exists():
    out.unlink()
with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as z:
    z.write(tmp / '[Content_Types].xml', '[Content_Types].xml')
    for p in sorted(tmp.rglob('*')):
        if p.is_file() and p.name != '[Content_Types].xml':
            z.write(p, p.relative_to(tmp).as_posix())
shutil.rmtree(tmp)
print('postprocessed ->', dst, 'headings:', n)
