// Build the revised essay as .docx from the plain-text sources in src/.
// Usage: node build.js <out.docx> [--allow-placeholders] [--toc toc.json]
const fs = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, TextRun, AlignmentType, HeadingLevel, Table, TableRow, TableCell,
  WidthType, BorderStyle, ShadingType, Header, Footer, PageNumber, NumberFormat, TabStopType,
  TabStopPosition, LineRuleType, VerticalAlign, PageBreak, SectionType, TableLayoutType,
} = require('docx');

const args = process.argv.slice(2);
const OUT = args[0];
const ALLOW_PH = args.includes('--allow-placeholders');
const tocIdx = args.indexOf('--toc');
const TOC_JSON = tocIdx >= 0 ? args[tocIdx + 1] : null;

const SRC_DIR = path.join(__dirname, 'src');
const files = fs.readdirSync(SRC_DIR).filter(f => f.endsWith('.txt')).sort();
const raw = files.map(f => fs.readFileSync(path.join(SRC_DIR, f), 'utf8')).join('\n\n');
if (!ALLOW_PH && /⟦[^⟧]*⟧/.test(raw)) {
  const left = raw.match(/⟦[^⟧]*⟧/g);
  console.error('Unresolved placeholders:', left.join(' '));
  process.exit(1);
}

// ---------- typography constants ----------
const BODY_PT = 12;                 // 小四
const BODY_SZ = BODY_PT * 2;        // half-points
const LINE_BODY = 440;              // exact 22pt (twips)
const INDENT_2CH = BODY_PT * 2 * 20; // two CJK characters, in twips
const FONT_SONG = '宋体';
const FONT_HEI = '黑体';
const FONT_KAI = '楷体';
const LATIN_SERIF = 'Times New Roman';
const LATIN_SANS = 'Arial';
const PAGE_W = 11906, PAGE_H = 16838, MARGIN_LR = 1800, MARGIN_TB = 1440;
const TEXT_W = PAGE_W - 2 * MARGIN_LR; // 8306
const SHORT_TITLE = '积累、无心与无我';

const fonts = (east, latin) => ({ ascii: latin, hAnsi: latin, eastAsia: east, cs: latin });

// ---------- inline markup: **bold**, *italic* (italic may nest inside bold) ----------
function runs(text, base = {}) {
  const out = [];
  const re = /\*\*(.+?)\*\*/g;
  let last = 0, m;
  while ((m = re.exec(text)) !== null) {
    if (m.index > last) out.push(...splitItalic(text.slice(last, m.index), base));
    out.push(...splitItalic(m[1], { ...base, bold: true }));
    last = m.index + m[0].length;
  }
  if (last < text.length) out.push(...splitItalic(text.slice(last), base));
  return out;
}
function splitItalic(text, base) {
  const out = []; const re = /\*([^*]+?)\*/g; let last = 0, m;
  while ((m = re.exec(text)) !== null) {
    if (m.index > last) out.push(seg(text.slice(last, m.index), base));
    out.push(seg(m[1], { ...base, italics: true }));
    last = m.index + m[0].length;
  }
  if (last < text.length) out.push(seg(text.slice(last), base));
  return out;
}
function seg(t, o) {
  const ph = /⟦[^⟧]*⟧/.test(t);
  return new TextRun({ text: t, ...o, ...(ph ? { highlight: 'yellow' } : {}) });
}

// ---------- block parser ----------
const blocks = [];
{
  const lines = raw.split(/\r?\n/);
  let i = 0;
  while (i < lines.length) {
    const line = lines[i];
    if (!line.trim()) { i++; continue; }
    if (line.startsWith('|')) {
      const rows = [];
      while (i < lines.length && lines[i].startsWith('|')) {
        rows.push(lines[i].replace(/^\|\s*/, '').split(/\s+\|\s+/).map(s => s.trim()));
        i++;
      }
      blocks.push({ type: 'table', rows });
      continue;
    }
    let m;
    if ((m = line.match(/^@(\w+)\s*(.*)$/))) blocks.push({ type: m[1], text: m[2] });
    else if ((m = line.match(/^## (.*)$/))) blocks.push({ type: 'h2', text: m[1] });
    else if ((m = line.match(/^# (.*)$/))) blocks.push({ type: 'h1', text: m[1] });
    else if ((m = line.match(/^> (.*)$/))) blocks.push({ type: 'quote', text: m[1] });
    else blocks.push({ type: 'p', text: line.trim() });
    i++;
  }
}

// ---------- TOC entries ----------
const headings = blocks.filter(b => b.type === 'h1' || b.type === 'h2');
let tocPages = {};
if (TOC_JSON && fs.existsSync(TOC_JSON)) tocPages = JSON.parse(fs.readFileSync(TOC_JSON, 'utf8'));

// ---------- element builders ----------
const border = { style: BorderStyle.SINGLE, size: 4, color: '808080' };
const cellBorders = { top: border, bottom: border, left: border, right: border };

function bodyPara(text, opts = {}) {
  return new Paragraph({
    style: 'BodyTextCN',
    children: runs(text),
    ...opts,
  });
}

function makeTable(rows, opts = {}) {
  const ncol = rows[0].length;
  let widths;
  if (opts.widths) {
    const tot = opts.widths.reduce((a, b) => a + b, 0);
    widths = opts.widths.map(w => Math.floor(TEXT_W * w / tot));
    widths[ncol - 1] = TEXT_W - widths.slice(0, -1).reduce((a, b) => a + b, 0);
  } else {
    // default: first column narrower, the rest equal
    const first = Math.round(TEXT_W * 0.19);
    const rest = Math.floor((TEXT_W - first) / (ncol - 1));
    widths = [first, ...Array(ncol - 1).fill(rest)];
    widths[ncol - 1] = TEXT_W - first - rest * (ncol - 2);
  }
  const plainFirst = opts.firstcol === 'plain';
  const tr = rows.map((cells, ri) => new TableRow({
    tableHeader: ri === 0,
    cantSplit: true,
    children: cells.map((c, ci) => new TableCell({
      borders: cellBorders,
      width: { size: widths[ci], type: WidthType.DXA },
      shading: ri === 0 ? { fill: 'EDEDED', type: ShadingType.CLEAR, color: 'auto' } : undefined,
      margins: { top: 60, bottom: 60, left: 100, right: 100 },
      verticalAlign: VerticalAlign.CENTER,
      children: [new Paragraph({
        style: ri === 0 ? 'TableHeadCN' : (ci === 0 && !plainFirst ? 'TableFirstColCN' : 'TableTextCN'),
        children: runs(c),
      })],
    })),
  }));
  return new Table({
    width: { size: TEXT_W, type: WidthType.DXA },
    columnWidths: widths,
    layout: TableLayoutType.FIXED,
    rows: tr,
  });
}

// ---------- assemble sections ----------
const front = [];   // title page + TOC
const body = [];
let inBody = false;
let tocInserted = false;
let pendingTableOpts = {};

for (const b of blocks) {
  const target = inBody ? body : front;
  switch (b.type) {
    case 'title':
      front.push(new Paragraph({ style: 'TitleCN', children: runs(b.text) }));
      break;
    case 'subtitle':
      front.push(new Paragraph({ style: 'SubtitleCN', children: runs(b.text) }));
      break;
    case 'abstract':
      front.push(new Paragraph({ style: 'AbstractCN', children: [
        new TextRun({ text: '摘要：', font: fonts(FONT_HEI, LATIN_SANS), bold: true }), ...runs(b.text)] }));
      break;
    case 'keywords':
      front.push(new Paragraph({ style: 'AbstractCN', spacing: { before: 120 }, children: [
        new TextRun({ text: '关键词：', font: fonts(FONT_HEI, LATIN_SANS), bold: true }), ...runs(b.text)] }));
      break;
    case 'toc': {
      front.push(new Paragraph({ children: [new PageBreak()] }));
      front.push(new Paragraph({ style: 'TOCHeadingCN', children: [new TextRun('目　录')] }));
      // placeholder paragraphs, one per heading; replaced in post-processing
      headings.forEach((h, k) => {
        front.push(new Paragraph({ style: h.type === 'h1' ? 'TOC1' : 'TOC2', children: [new TextRun(`{{TOCENTRY:${k}}}`)] }));
      });
      tocInserted = true;
      inBody = true;
      break;
    }
    case 'h1':
      target.push(new Paragraph({ heading: HeadingLevel.HEADING_1, children: runs(b.text) }));
      break;
    case 'h2':
      target.push(new Paragraph({ heading: HeadingLevel.HEADING_2, children: runs(b.text) }));
      break;
    case 'quote':
      target.push(new Paragraph({ style: 'QuoteCN', children: runs(b.text) }));
      break;
    case 'tablecaption':
      target.push(new Paragraph({ style: 'CaptionCN', keepNext: true, children: runs(b.text) }));
      break;
    case 'tableopts': {
      const o = {};
      for (const kv of b.text.split(/\s+/)) {
        const [k, v] = kv.split('=');
        if (k === 'widths') o.widths = v.split(',').map(Number);
        else o[k] = v;
      }
      pendingTableOpts = o;
      break;
    }
    case 'table':
      target.push(makeTable(b.rows, pendingTableOpts));
      pendingTableOpts = {};
      target.push(new Paragraph({ style: 'AfterTableCN', children: [] }));
      break;
    case 'tablenote':
      target.push(new Paragraph({ style: 'TableNoteCN', children: runs(b.text) }));
      break;
    case 'refhead':
      target.push(new Paragraph({ style: 'RefHeadCN', children: runs(b.text) }));
      break;
    case 'refnote':
      target.push(new Paragraph({ style: 'RefNoteCN', children: runs(b.text) }));
      break;
    case 'ref': {
      const idx = b.text.indexOf('使用限度：');
      let kids;
      if (idx >= 0) {
        kids = [...runs(b.text.slice(0, idx)),
          new TextRun({ text: '使用限度：', font: fonts(FONT_HEI, LATIN_SANS), color: '404040' }),
          ...runs(b.text.slice(idx + 5), { color: '404040' })];
      } else kids = runs(b.text);
      target.push(new Paragraph({ style: 'RefCN', children: kids }));
      break;
    }
    case 'pagebreak':
      target.push(new Paragraph({ children: [new PageBreak()] }));
      break;
    case 'p':
      target.push(bodyPara(b.text));
      break;
    default:
      throw new Error('Unknown block type: ' + b.type);
  }
}
if (!tocInserted) throw new Error('No @toc directive');

// ---------- styles ----------
const styles = {
  default: {
    document: { run: { font: fonts(FONT_SONG, LATIN_SERIF), size: BODY_SZ }, paragraph: { spacing: { line: LINE_BODY, lineRule: LineRuleType.EXACT } } },
    heading1: {
      run: { font: fonts(FONT_HEI, LATIN_SANS), size: 32, bold: true, color: '000000' },
      paragraph: { spacing: { before: 480, after: 240, line: 480, lineRule: LineRuleType.EXACT }, keepNext: true, keepLines: true, outlineLevel: 0 },
    },
    heading2: {
      run: { font: fonts(FONT_HEI, LATIN_SANS), size: 26, bold: true, color: '000000' },
      paragraph: { spacing: { before: 300, after: 120, line: 400, lineRule: LineRuleType.EXACT }, keepNext: true, keepLines: true, outlineLevel: 1 },
    },
  },
  paragraphStyles: [
    { id: 'BodyTextCN', name: 'Body Text CN', basedOn: 'Normal', quickFormat: true,
      paragraph: { alignment: AlignmentType.JUSTIFIED, indent: { firstLine: INDENT_2CH }, spacing: { line: LINE_BODY, lineRule: LineRuleType.EXACT, before: 0, after: 0 } } },
    { id: 'TitleCN', name: 'Title CN', basedOn: 'Normal', next: 'SubtitleCN',
      run: { font: fonts(FONT_HEI, LATIN_SANS), size: 40, bold: true },
      paragraph: { alignment: AlignmentType.CENTER, spacing: { before: 1200, after: 240, line: 640, lineRule: LineRuleType.EXACT } } },
    { id: 'SubtitleCN', name: 'Subtitle CN', basedOn: 'Normal',
      run: { font: fonts(FONT_KAI, LATIN_SERIF), size: 28 },
      paragraph: { alignment: AlignmentType.CENTER, spacing: { before: 0, after: 720, line: 440, lineRule: LineRuleType.EXACT } } },
    { id: 'AbstractCN', name: 'Abstract CN', basedOn: 'Normal',
      run: { font: fonts(FONT_KAI, LATIN_SERIF), size: 22 },
      paragraph: { alignment: AlignmentType.JUSTIFIED, indent: { left: 420, right: 420 }, spacing: { line: 400, lineRule: LineRuleType.EXACT } } },
    { id: 'TOCHeadingCN', name: 'TOC Heading CN', basedOn: 'Normal',
      run: { font: fonts(FONT_HEI, LATIN_SANS), size: 32, bold: true },
      paragraph: { alignment: AlignmentType.CENTER, spacing: { before: 0, after: 360, line: 480, lineRule: LineRuleType.EXACT } } },
    { id: 'TOC1', name: 'toc 1', basedOn: 'Normal', next: 'Normal',
      run: { font: fonts(FONT_HEI, LATIN_SANS), size: 22 },
      paragraph: { spacing: { before: 100, after: 0, line: 340, lineRule: LineRuleType.EXACT }, tabStops: [{ type: TabStopType.RIGHT, position: TEXT_W, leader: 'dot' }] } },
    { id: 'TOC2', name: 'toc 2', basedOn: 'Normal', next: 'Normal',
      run: { font: fonts(FONT_SONG, LATIN_SERIF), size: 21 },
      paragraph: { indent: { left: 420 }, spacing: { before: 0, after: 0, line: 300, lineRule: LineRuleType.EXACT }, tabStops: [{ type: TabStopType.RIGHT, position: TEXT_W, leader: 'dot' }] } },
    { id: 'QuoteCN', name: 'Quote CN', basedOn: 'Normal',
      run: { font: fonts(FONT_KAI, LATIN_SERIF), size: BODY_SZ },
      paragraph: { alignment: AlignmentType.JUSTIFIED, indent: { left: INDENT_2CH, right: INDENT_2CH }, spacing: { before: 120, after: 120, line: LINE_BODY, lineRule: LineRuleType.EXACT } } },
    { id: 'CaptionCN', name: 'Caption CN', basedOn: 'Normal',
      run: { font: fonts(FONT_HEI, LATIN_SANS), size: 21, bold: true },
      paragraph: { alignment: AlignmentType.CENTER, keepNext: true, spacing: { before: 200, after: 100, line: 320, lineRule: LineRuleType.EXACT } } },
    { id: 'TableHeadCN', name: 'Table Head CN', basedOn: 'Normal',
      run: { font: fonts(FONT_HEI, LATIN_SANS), size: 20, bold: true },
      paragraph: { alignment: AlignmentType.CENTER, spacing: { line: 300, lineRule: LineRuleType.EXACT, before: 0, after: 0 } } },
    { id: 'TableFirstColCN', name: 'Table First Column CN', basedOn: 'Normal',
      run: { font: fonts(FONT_HEI, LATIN_SANS), size: 20 },
      paragraph: { alignment: AlignmentType.LEFT, spacing: { line: 300, lineRule: LineRuleType.EXACT, before: 0, after: 0 } } },
    { id: 'TableTextCN', name: 'Table Text CN', basedOn: 'Normal',
      run: { font: fonts(FONT_SONG, LATIN_SERIF), size: 20 },
      paragraph: { alignment: AlignmentType.LEFT, spacing: { line: 300, lineRule: LineRuleType.EXACT, before: 0, after: 0 } } },
    { id: 'AfterTableCN', name: 'After Table CN', basedOn: 'Normal',
      run: { size: 12 }, paragraph: { spacing: { line: 200, lineRule: LineRuleType.EXACT, before: 0, after: 0 } } },
    { id: 'TableNoteCN', name: 'Table Note CN', basedOn: 'Normal',
      run: { size: 18, color: '404040' }, paragraph: { spacing: { line: 280, lineRule: LineRuleType.EXACT, before: 60, after: 120 } } },
    { id: 'RefHeadCN', name: 'Reference Group CN', basedOn: 'Normal',
      run: { font: fonts(FONT_HEI, LATIN_SANS), size: 22, bold: true },
      paragraph: { keepNext: true, spacing: { before: 240, after: 120, line: 360, lineRule: LineRuleType.EXACT } } },
    { id: 'RefNoteCN', name: 'Reference Note CN', basedOn: 'Normal',
      run: { size: 21 },
      paragraph: { alignment: AlignmentType.JUSTIFIED, indent: { firstLine: 420 }, spacing: { line: 360, lineRule: LineRuleType.EXACT, before: 0, after: 120 } } },
    { id: 'RefCN', name: 'Reference CN', basedOn: 'Normal',
      run: { size: 20 },
      paragraph: { alignment: AlignmentType.LEFT, indent: { left: 400, hanging: 400 }, spacing: { line: 320, lineRule: LineRuleType.EXACT, before: 0, after: 100 } } },
    { id: 'HeaderCN', name: 'Header CN', basedOn: 'Normal',
      run: { font: fonts(FONT_KAI, LATIN_SERIF), size: 18, color: '595959' },
      paragraph: { alignment: AlignmentType.RIGHT, spacing: { line: 240, lineRule: LineRuleType.AUTO }, border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: 'A6A6A6', space: 4 } } } },
    { id: 'FooterCN', name: 'Footer CN', basedOn: 'Normal',
      run: { font: fonts(FONT_SONG, LATIN_SERIF), size: 18 },
      paragraph: { alignment: AlignmentType.CENTER, spacing: { line: 240, lineRule: LineRuleType.AUTO } } },
  ],
};

const pageProps = (numFmt, start) => ({
  page: {
    size: { width: PAGE_W, height: PAGE_H },
    margin: { top: MARGIN_TB, bottom: MARGIN_TB, left: MARGIN_LR, right: MARGIN_LR, header: 851, footer: 992 },
    pageNumbers: { start, formatType: numFmt },
  },
});

const doc = new Document({
  creator: '',
  title: '积累、无心与无我：能力、控制与自我关系的分析框架',
  subject: '能力、控制与自我关系的分析框架',
  description: '刻意练习、熟练执行与自我关系的联系、边界和待检验机制',
  styles,
  sections: [
    {
      properties: { ...pageProps(NumberFormat.UPPER_ROMAN, 1), titlePage: true },
      headers: { default: new Header({ children: [new Paragraph({ style: 'HeaderCN', children: [new TextRun(SHORT_TITLE)] })] }),
                 first: new Header({ children: [new Paragraph({ children: [] })] }) },
      footers: { default: new Footer({ children: [new Paragraph({ style: 'FooterCN', children: [new TextRun({ children: [PageNumber.CURRENT] })] })] }),
                 first: new Footer({ children: [new Paragraph({ children: [] })] }) },
      children: front,
    },
    {
      properties: { ...pageProps(NumberFormat.DECIMAL, 1), type: SectionType.NEXT_PAGE },
      headers: { default: new Header({ children: [new Paragraph({ style: 'HeaderCN', children: [new TextRun(SHORT_TITLE)] })] }) },
      footers: { default: new Footer({ children: [new Paragraph({ style: 'FooterCN', children: [new TextRun({ children: [PageNumber.CURRENT] })] })] }) },
      children: body,
    },
  ],
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync(OUT, buf);
  fs.writeFileSync(OUT + '.headings.json', JSON.stringify(headings.map(h => ({ level: h.type === 'h1' ? 1 : 2, text: h.text.replace(/\*/g, '') })), null, 1));
  console.log('wrote', OUT, 'headings:', headings.length, 'blocks:', blocks.length);
});
