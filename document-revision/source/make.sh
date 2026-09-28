#!/bin/bash
# Build the revised docx with a TOC whose cached page numbers come from a LibreOffice render.
set -e
cd "$(dirname "$0")"
OUT=${1:-/tmp/lotest/final.docx}
node build.js /tmp/lotest/p1.docx
python3 postprocess.py /tmp/lotest/p1.docx /tmp/lotest/p1p.docx /tmp/lotest/p1.docx.headings.json
python3 pagemap.py /tmp/lotest/p1p.docx /tmp/lotest/p1.docx.headings.json /tmp/lotest/toc.json
python3 postprocess.py /tmp/lotest/p1.docx "$OUT" /tmp/lotest/p1.docx.headings.json /tmp/lotest/toc.json
python3 pagemap.py "$OUT" /tmp/lotest/p1.docx.headings.json /tmp/lotest/toc_check.json
python3 -c "import json;a=json.load(open('/tmp/lotest/toc.json'));b=json.load(open('/tmp/lotest/toc_check.json'));print('TOC stable' if a==b else 'TOC MISMATCH', {k:(a[k],b.get(k)) for k in a if a[k]!=b.get(k)})"
