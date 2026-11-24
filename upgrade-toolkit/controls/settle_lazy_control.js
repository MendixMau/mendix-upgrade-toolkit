// Control for GM-33: settle() must not report a page as settled while a lazy-load placeholder is shown, must say on
// timeout that placeholders were still present, and must leave a page without placeholders unchanged.
// Fake Playwright page (plain node), plus a real Chromium when there is one. Exit 0 = pass.
// The placeholder class names are ASSUMED (no captured page shows them); the control uses the same assumed names.
const fs = require('fs');
const { settle, pageSettled, LAZY } = require('../bin/settle.js');
const fake = states => {
  let i = 0;
  return { waitForLoadState: async () => {}, waitForTimeout: async () => {},
           evaluate: async () => states[Math.min(i++, states.length - 1)] };
};
let fail = 0;
const check = (name, ok, detail) => { if (!ok) fail++; console.log(`${ok ? 'ok  ' : 'FAIL'} ${name}: ${detail}`); };
(async () => {
  // catch: the page-level busy list is empty, the DOM stands still, but a lazy placeholder is shown
  let r = await settle(fake([{ busy: ['lazy-placeholder:widget-lazyloading'], lazy: ['widget-lazyloading'], size: 10 }]), { timeout: 300, stableMs: 0, stuckMs: 100 });
  check('lazy placeholder never goes away -> not settled, says placeholders present', !r.ok && r.lazy === true && /lazy-load placeholder\(s\) still present: widget-lazyloading/.test(r.reason), JSON.stringify(r));
  r = await settle(fake([{ busy: ['lazy-placeholder:skeleton'], lazy: ['skeleton'], size: 10 }, { busy: [], size: 50 }, { busy: [], size: 50 }, { busy: [], size: 50 }]), { timeout: 2000, stableMs: 0 });
  check('placeholder goes away, then stable -> settled', r.ok, JSON.stringify(r));
  // pass: no placeholder, same as before
  r = await settle(fake([{ busy: [], size: 50 }]), { timeout: 2000, stableMs: 0 });
  check('no placeholder -> settled, unchanged', r.ok && !r.lazy && !r.reason, JSON.stringify(r));
  // GM-33 review fix 1: false-match diagnostic and the SETTLE_LAZY_OFF escape hatch. These run the REAL pageSettled
  // against a fake document, so what settle() passes as the argument decides the result.
  const el = cls => ({ className: cls, getClientRects: () => [1], style: { display: 'block' } });
  const realPage = cls => ({ waitForLoadState: async () => {}, waitForTimeout: async () => {},
    evaluate: async (fn, arg) => fn(arg) });
  const withDoc = (cls, body) => { global.document = { body: { innerHTML: 'x'.repeat(50) },
    querySelectorAll: sel => [el(cls)].filter(e => sel.includes('skeleton') && /skeleton/i.test(e.className)) }; return body(); };
  const DOC = 'theme-skeleton';
  r = await withDoc(DOC, () => settle(realPage(), { timeout: 400, stableMs: 0, stuckMs: 100 }));
  check('permanent placeholder, DOM unchanged -> diagnostic names the false match and SETTLE_LAZY_OFF=1',
    !r.ok && r.lazy === true && /placeholder present and DOM unchanged for \d+ms; if this class is permanent it is a false match \u2014 set SETTLE_LAZY_OFF=1/.test(r.reason), JSON.stringify(r));
  r = await withDoc(DOC, () => settle(realPage(), { timeout: 400, stableMs: 0, stuckMs: 100, lazyOff: true }));
  check('SETTLE_LAZY_OFF (opts.lazyOff): permanent placeholder no longer gives lazy:true', r.ok === true && !r.lazy, JSON.stringify(r));
  process.env.SETTLE_LAZY_OFF = '1';
  r = await withDoc(DOC, () => settle(realPage(), { timeout: 400, stableMs: 0, stuckMs: 100 }));
  delete process.env.SETTLE_LAZY_OFF;
  check('SETTLE_LAZY_OFF=1 env: permanent placeholder no longer gives lazy:true', r.ok === true && !r.lazy, JSON.stringify(r));
  // review fix 2: one selector list. drift guard: the list is pinned, pageSettled uses exactly the one it is handed, and
  // no second copy of a class-substring selector exists in the source.
  const PIN = ['[class*="lazyload" i]', '[class*="lazy-load" i]', '[class*="skeleton" i]', '[class*="dataview-loader" i]'];
  check('drift guard: LAZY is the pinned list', JSON.stringify(LAZY) === JSON.stringify(PIN), JSON.stringify(LAZY));
  let asked = null;
  global.document = { body: { innerHTML: '' }, querySelectorAll: sel => { if (/class\*=/.test(sel)) asked = sel; return []; } };
  pageSettled({ lazy: ['[class*="zzz" i]'] });
  check('drift guard: pageSettled queries the list it is handed, not its own copy', asked === '[class*="zzz" i]', String(asked));
  asked = null; pageSettled(); 
  check('drift guard: with no argument pageSettled falls back to LAZY', asked === PIN.join(', '), String(asked));
  delete global.document;
  const src = fs.readFileSync(require.resolve('../bin/settle.js'), 'utf8').split('\n').filter(l => !/^\s*\/\//.test(l)).join('\n');
  const copies = (src.match(/\[class\*=/g) || []).length;
  check('drift guard: class-substring selectors appear once (' + PIN.length + ' entries in LAZY, no second copy)', copies === PIN.length, 'found ' + copies);
  let pw = null;
  for (const d of [process.env.PLAYWRIGHT_DIR, '/opt/node-tools/node_modules/playwright', 'playwright'].filter(Boolean)) { try { pw = require(d); break; } catch (e) { /* next */ } }
  let browser = null;
  try { if (pw) browser = await pw.chromium.launch({ args: ['--use-mock-keychain', '--password-store=basic'] }); } catch (e) { browser = null; }
  if (browser) {
    const page = await browser.newPage();
    const CASES = [
      ['page with a shown lazy placeholder', '<div class="mx-placeholder"><h1>Profile</h1><div class="widget-lazyloading-placeholder" style="height:40px">.</div></div>', x => !x.ok && x.lazy && /lazy-load placeholder/.test(x.reason)],
      ['page with a hidden lazy placeholder', '<div class="mx-placeholder"><h1>Profile</h1><div class="widget-lazyloading-placeholder" style="display:none">.</div></div>', x => x.ok && !x.lazy],
      ['page with a shown skeleton', '<div class="mx-placeholder"><h1>Profile</h1><div class="Skeleton-row" style="height:40px">.</div></div>', x => !x.ok && x.lazy && /skeleton/i.test(x.reason)],
      ['page without placeholders', '<div class="mx-placeholder"><h1>Profile</h1></div>', x => x.ok && !x.lazy],
    ];
    for (const [n, html, want] of CASES) {
      await page.setContent('<!doctype html><body>' + html + '</body>');
      const x = await settle(page, { timeout: 2000, stableMs: 0, stuckMs: 500 });
      check(n + ' (chromium)', !!want(x), JSON.stringify(x));
    }
    await browser.close();
  } else console.log('note  settle lazy: no Playwright/Chromium here, fake page only');
  process.exit(fail ? 1 : 0);
})();
