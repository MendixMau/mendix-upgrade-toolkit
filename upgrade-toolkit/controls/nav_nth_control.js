// Control for CHK/PMNT: navTo picks one of several anchors with the same title by position (icon-only menu, blank captions).
// Fake page: evaluate runs the browser function against a fake document. Exit 0 = pass.
process.env.APP_PORT = process.env.APP_PORT || '1'; process.env.ALLOW_UNVERIFIED_APP = '1';
const fs = require('fs'), os = require('os'), path = require('path');
const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'navnth-'));
for (const f of fs.readdirSync(path.join(__dirname, '../vendor/e2e'))) fs.copyFileSync(path.join(__dirname, '../vendor/e2e', f), path.join(dir, f));
fs.writeFileSync(path.join(dir, 'project.config.js'), `'use strict';
module.exports = { root: ${JSON.stringify(dir)}, mpr: null, mxcli: 'mxcli', dsCss: null, defaultPort: '1', readySelectors: [], NAV: {}, TARGETS: { 'full-app': [] },
  credentials: () => ({ user: 'u', pass: 'p', fallbackUser: '', fallbackPass: '' }) };\n`);
const H = require(path.join(dir, 'helpers.js'));
let fail = 0;
const check = (n, ok, d) => { if (!ok) fail++; console.log(`${ok ? 'ok  ' : 'FAIL'} ${n}: ${d}`); };
const mk = titles => titles.map((t, i) => ({ i, getAttribute: () => t, scrollIntoView() {}, click() { clicked.push(i); } }));
let clicked = [];
const page = { evaluate: async (f, arg) => f(arg), waitForTimeout: async () => {}, locator: () => ({ first: () => ({ isVisible: async () => false }) }) };
(async () => {
  global.document = { querySelectorAll: () => mk([' ', ' ', 'Home', ' ', ' ']) };
  clicked = []; await H.navTo(page, null, ' ', 3);
  check('nav nth picks the 4th blank item', clicked.join() === '4', `clicked ${clicked}`);
  clicked = []; await H.navTo(page, null, ' ');
  check('nav without nth keeps the first match', clicked.join() === '0', `clicked ${clicked}`);
  clicked = []; await H.navTo(page, null, 'Home', 0);
  check('nav by caption unchanged', clicked.join() === '2', `clicked ${clicked}`);
  clicked = []; await H.navTo(page, null, ' ', 9);
  check('nav nth past the last item clicks nothing', clicked.length === 0, `clicked ${clicked}`);
  process.exit(fail ? 1 : 0);
})();
