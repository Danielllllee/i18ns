// Step 4: rasterize the SVG with headless Chromium (Playwright).
// usage: node render.js drawing.svg drawing.png
// Playwright must be resolvable, e.g. NODE_PATH="$(npm root -g)" when it is installed globally.
const { chromium } = require('playwright');
const fs = require('fs');

(async () => {
  const [inp, out] = process.argv.slice(2);
  const svg = fs.readFileSync(inp, 'utf8');
  const m = svg.match(/<svg[^>]*\swidth="(\d+)"[^>]*\sheight="(\d+)"/);
  const W = parseInt(m[1], 10), H = parseInt(m[2], 10);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 1 });
  await page.setContent(
    `<!doctype html><html><head><style>html,body{margin:0;padding:0;background:#fff}svg{display:block}</style></head><body>${svg}</body></html>`,
    { waitUntil: 'load' });
  await page.waitForTimeout(300);
  await page.screenshot({ path: out, clip: { x: 0, y: 0, width: W, height: H }, timeout: 180000 });
  await browser.close();
  console.log(`rendered ${out} (${W}x${H})`);
})().catch((e) => { console.error(e); process.exit(1); });
