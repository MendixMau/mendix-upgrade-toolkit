// Control for the anonymous visitor of the journey engine (vendor/e2e/journey-runner.js anonymousVisit): an app with Guest
// access on has no sign-in form on its anonymous home, so "no password input" must not mean "did not render".
// Fake Playwright page (plain node); the function text is cut out of the engine file, so the control runs the real code.
// Usage: node anonymous_visit_control.js <journey-runner.js>. Exit 0 = pass.
const fs = require('fs');
const src = fs.readFileSync(process.argv[2], 'utf8');
const m = src.match(/async function anonymousVisit\(page, baseUrl\) \{[\s\S]*?\n\}\n/);
let fail = 0;
const check = (name, ok, detail) => { if (!ok) fail++; console.log(`${ok ? 'ok  ' : 'FAIL'} ${name}: ${detail}`); };
if (!m) { check('engine has anonymousVisit', false, 'function not found in ' + process.argv[2]); process.exit(1); }
const anonymousVisit = new Function(`${m[0]}; return anonymousVisit;`)();
const fake = ({ form, ev }) => ({
  context: () => ({ clearCookies: async () => {} }),
  goto: async () => {},
  locator: () => ({ first: () => ({ waitFor: async () => { if (!form) throw new Error('timeout'); } }) }),
  evaluate: async () => { if (ev instanceof Error) throw ev; return ev; },
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
  process.exit(fail ? 1 : 0);
})();
