// Control for the anonymous visitor of the journey engine (vendor/e2e/journey-runner.js anonymousVisit): an app with Guest
// access on has no sign-in form on its anonymous home, so "no password input" must not mean "did not render".
// Fake Playwright page (plain node); the function text is cut out of the engine file, so the control runs the real code.
// The error / not-found cases run the engine's own in-page probe against a tiny fake DOM (no jsdom): `dom` is a list of
// {sel, text, cls} elements and `body` the page text.
// Usage: node anonymous_visit_control.js <journey-runner.js>. Exit 0 = pass.
const fs = require('fs');
const src = fs.readFileSync(process.argv[2], 'utf8');
const m = src.match(/async function anonymousVisit\(page, baseUrl\) \{[\s\S]*?\n\}\n/);
let fail = 0;
const check = (name, ok, detail) => { if (!ok) fail++; console.log(`${ok ? 'ok  ' : 'FAIL'} ${name}: ${detail}`); };
if (!m) { check('engine has anonymousVisit', false, 'function not found in ' + process.argv[2]); process.exit(1); }
const anonymousVisit = new Function(`${m[0]}; return anonymousVisit;`)();
const fakeDom = ({ els = [], body = '', main, guest = true, pages = 1 }) => fn => {
  const mk = e => ({ offsetParent: {}, className: e.cls || '', textContent: e.text || '', getClientRects: () => [{}] });
  const q = sel => els.filter(e => sel.split(',').map(x => x.trim()).includes(e.sel)).map(mk);
  const saved = [global.document, global.window];
  global.document = { querySelectorAll: sel => sel === '.mx-page' ? new Array(pages).fill({ innerText: main === undefined ? body : main }) : q(sel), body: { innerText: body } };
  global.window = { mx: { session: { isGuest: () => guest } } }; global.mx = global.window.mx;
  try { return fn(); } finally { [global.document, global.window] = saved; delete global.mx; }
};
const fake = ({ form, ev, dom }) => ({
  context: () => ({ clearCookies: async () => {} }),
  goto: async () => {},
  locator: () => ({ first: () => ({ waitFor: async () => { if (!form) throw new Error('timeout'); } }) }),
  evaluate: async fn => { if (dom) return dom(fn); if (ev instanceof Error) throw ev; return ev; },
});
(async () => {
  let r = await anonymousVisit(fake({ form: true, ev: { guest: false, pages: 0 } }), 'http://x');
  check('sign-in form is the anonymous home -> ok', r.ok === true && r.user === 'anonymous', JSON.stringify(r));
  r = await anonymousVisit(fake({ form: false, ev: { guest: true, pages: 1 } }), 'http://x');
  check('guest home, no sign-in form, mx session is guest -> ok', r.ok === true && /guest home/.test(r.user), JSON.stringify(r));
  r = await anonymousVisit(fake({ form: false, ev: { guest: false, pages: 1 } }), 'http://x');
  check('page renders but the session is not a guest -> not ok', r.ok === false && /did not render/.test(r.reason), JSON.stringify(r));
  r = await anonymousVisit(fake({ form: false, ev: { guest: true, pages: 0 } }), 'http://x');
  check('guest session but no page -> not ok, says so', r.ok === false && /no page rendered/.test(r.reason), JSON.stringify(r));
  r = await anonymousVisit(fake({ form: false, ev: new Error('boom') }), 'http://x');
  check('client probe throws -> not ok', r.ok === false && /did not render/.test(r.reason), JSON.stringify(r));
  r = await anonymousVisit(fake({ form: false, dom: fakeDom({ body: 'Welcome' }) }), 'http://x');
  check('real probe, guest home page renders -> ok, distinct detail', r.ok === true && r.user === 'anonymous (guest home, no sign-in form)', JSON.stringify(r));
  r = await anonymousVisit(fake({ form: false, dom: fakeDom({ body: 'The page you requested could not be found.' }) }), 'http://x');
  check('guest session on a not-found page -> not ok', r.ok === false && /error or not-found page/.test(r.reason), JSON.stringify(r));
  r = await anonymousVisit(fake({ form: false, dom: fakeDom({ body: 'Home\nPages\nSettings\nCustomer not found', main: 'Customers\nCustomer not found' }) }), 'http://x');
  check('nav item "Pages" and an empty state "Customer not found" -> ok', r.ok === true, JSON.stringify(r));
  r = await anonymousVisit(fake({ form: false, dom: fakeDom({ body: 'Pages\nCustomer not found' }) }), 'http://x');
  check('"Pages" and "not found" on separate lines in one page -> ok', r.ok === true, JSON.stringify(r));
  r = await anonymousVisit(fake({ form: false, dom: fakeDom({ body: 'Open cases\n404\nClosed 12' }) }), 'http://x');
  check('a stat tile reading 404 is not an error page -> ok', r.ok === true, JSON.stringify(r));
  r = await anonymousVisit(fake({ form: false, dom: fakeDom({ body: 'Orders\n404 open orders' }) }), 'http://x');
  check('a table cell starting 404 on a later line is not an error page -> ok', r.ok === true, JSON.stringify(r));
  r = await anonymousVisit(fake({ form: false, dom: fakeDom({ body: '404 open cases\nClosed 12\nOverdue 3' }) }), 'http://x');
  check('a first tile reading "404 open cases" is not an error page -> ok', r.ok === true, JSON.stringify(r));
  r = await anonymousVisit(fake({ form: false, dom: fakeDom({ body: '404\nOpen cases\nClosed 12' }) }), 'http://x');
  check('a KPI tile 404 / Open cases / Closed 12 -> ok', r.ok === true, JSON.stringify(r));
  r = await anonymousVisit(fake({ form: false, dom: fakeDom({ body: '404 Orders overdue' }) }), 'http://x');
  check('page text that merely starts with 404 -> ok', r.ok === true, JSON.stringify(r));
  for (const [t, why] of [['404 Not Found', '404 page'], ['404', 'bare 404 heading'], ['404 Not Found\n'+'Lorem ipsum dolor sit amet. '.repeat(20), '404 Not Found with long body'], ['404 | Not Found', '404 pipe Not Found'], ['404 Not Found.', '404 Not Found full stop'], ['404 \u2014 Not Found', '404 em dash Not Found'], ["404. That's an error.", '404 that is an error'], ['Error 404', 'Error 404'], ['404 - Page not found', '404 dash page not found'], ['Error\n\n404', 'error then 404'], ['Oops\nThe page does not exist', 'page does not exist']]) {
    r = await anonymousVisit(fake({ form: false, dom: fakeDom({ body: t }) }), 'http://x');
    check('not-found text still fails: ' + why + ' -> not ok', r.ok === false && /not-found text/.test(r.reason), JSON.stringify(r));
  }
  r = await anonymousVisit(fake({ form: false, dom: fakeDom({ els: [{ sel: '.mx-dialog-error', text: 'An error occurred. Contact your administrator' }] }) }), 'http://x');
  check('guest session with an error dialog -> not ok', r.ok === false && /error or not-found page \(error dialog\)/.test(r.reason), JSON.stringify(r));
  r = await anonymousVisit(fake({ form: false, dom: fakeDom({ els: [{ sel: '.alert-danger', text: 'x', cls: 'alert alert-danger' }] }) }), 'http://x');
  check('guest session with a red error box -> not ok', r.ok === false && /error box/.test(r.reason), JSON.stringify(r));
  r = await anonymousVisit(fake({ form: false, dom: fakeDom({ els: [{ sel: '.alert-danger', text: 'x', cls: 'alert-danger mx-validation-message' }] }) }), 'http://x');
  check('a validation message is not an error page -> ok', r.ok === true, JSON.stringify(r));
  process.exit(fail ? 1 : 0);
})();
