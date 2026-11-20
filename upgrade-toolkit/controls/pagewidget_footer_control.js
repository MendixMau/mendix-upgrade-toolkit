'use strict';
// pagewidget_footer_control.js: which element a widget name picks when the page body and the layout footer share it
// (field run SITS, an SSO starter app on 10.24 to 11.12).
//
//   node pagewidget_footer_control.js          (NODE_PATH must reach playwright with a browser)
//
// The generated click "actionButton5" (create-save) and the sign-out button landed on a layout footer link
// ("Terms of Use") that carries the same mx-name: the footer sits in nested placeholders, the deepest placeholder won, and
// create-save FAILed on the new app only (a false regression). Cases, one line each ("ok <case>" or "FAIL <case>"):
//   old pick, body + footer share the name          the footer link (the defect: a CATCH of the old rule)
//   topmost: body + footer share the name            the page body button
//   topmost: body + [role=contentinfo] share it      the page body button
//   topmost: only a footer match                     the footer match (a sole match is kept)
//   topmost: body match is hidden, footer shown      the footer match (only shown matches count)
//   topmost: two body matches, deeper placeholder    the deeper one (the old rule still holds outside footers)
// Exit 0 when every case holds, 1 otherwise.
const { chromium } = require('playwright');
const V = require('../bin/journey-verbs.js');

const LAYOUT = (body, foot) => `<div class="mx-page"><div class="mx-placeholder"><div class="mx-placeholder">${body}</div></div>
  <div class="mx-placeholder"><div class="mx-placeholder"><div class="mx-placeholder">${foot}</div></div></div></div>`;
const BODY = `<button class="mx-name-actionButton5">New Account</button>`;
const FOOT = `<footer><a class="mx-name-actionButton5" href="#">Terms of Use</a></footer>`;
const INFO = `<div role="contentinfo"><a class="mx-name-actionButton5" href="#">Terms of Use</a></div>`;
const HIDDEN_BODY = `<button class="mx-name-actionButton5" style="display:none">New Account</button>`;
const TWO = `<div class="mx-placeholder"><button class="mx-name-actionButton5">Deep</button></div><button class="mx-name-actionButton5">Shallow</button>`;

// the rule before the fix: the shown element nested in the most placeholders
function oldPick(els) {
  let best = 0, depth = -1;
  els.forEach((e, i) => {
    if (!e.getClientRects().length) return;
    let d = 0;
    for (let a = e.parentElement; a; a = a.parentElement) if (a.classList.contains('mx-placeholder')) d++;
    if (d > depth) { best = i; depth = d; }
  });
  return best;
}

let bad = 0;
const say = (ok, c) => { console.log(`${ok ? 'ok' : 'FAIL'} ${c}`); if (!ok) bad++; };

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  const text = async (html, fn) => {
    await page.setContent(`<!doctype html><html><body>${html}</body></html>`);
    if (fn) { const i = await page.locator('.mx-name-actionButton5').evaluateAll(fn); return (await page.locator('.mx-name-actionButton5').nth(i).innerText()).trim(); }
    const el = await V.topmost(page, 'actionButton5');
    return (await el.innerText()).trim();
  };
  say(await text(LAYOUT(BODY, FOOT), oldPick) === 'Terms of Use', 'old pick, body + footer share the name: the footer link');
  say(await text(LAYOUT(BODY, FOOT)) === 'New Account', 'topmost: body + footer share the name: the page body button');
  say(await text(LAYOUT(BODY, INFO)) === 'New Account', 'topmost: body + [role=contentinfo] share it: the page body button');
  say(await text(LAYOUT('', FOOT)) === 'Terms of Use', 'topmost: only a footer match: the footer match is kept');
  say(await text(LAYOUT(HIDDEN_BODY, FOOT)) === 'Terms of Use', 'topmost: body match hidden, footer shown: the footer match');
  say(await text(LAYOUT(TWO, '')) === 'Deep', 'topmost: two body matches, deeper placeholder: the deeper one');
  await browser.close();
  process.exit(bad ? 1 : 0);
})().catch((e) => { console.error(e); process.exit(1); });
