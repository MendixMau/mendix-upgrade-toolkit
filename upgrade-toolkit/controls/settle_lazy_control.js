// Control for GM-33: settle() must not report a page as settled while a lazy-load placeholder is shown, must say on
// timeout that placeholders were still present, and must leave a page without placeholders unchanged.
// Fake Playwright page (plain node), plus a real Chromium when there is one. Exit 0 = pass.
// The placeholder class names are ASSUMED (no captured page shows them); the control uses the same assumed names.
const { settle } = require('../bin/settle.js');
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
  let pw = null;
  for (const d of [process.env.PLAYWRIGHT_DIR, '/opt/node-tools/node_modules/playwright', 'playwright'].filter(Boolean)) { try { pw = require(d); break; } catch (e) { /* next */ } }
  let browser = null;
  try { if (pw) browser = await pw.chromium.launch({ args: ['--use-mock-keychain', '--password-store=basic'] }); } catch (e) { browser = null; }
  if (browser) {
    const page = await browser.newPage();
    const CASES = [
      ['page with a shown lazy placeholder', '<div class="mx-placeholder"><h1>Profile</h1><div class="widget-lazyloading-placeholder" style="height:40px">.</div></div>', x => !x.ok && x.lazy && /lazy-load placeholder/.test(x.reason)],
      ['page with a hidden lazy placeholder', '<div class="mx-placeholder"><h1>Profile</h1><div class="widget-lazyloading-placeholder" style="display:none">.</div></div>', x => x.ok && !x.lazy],
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
