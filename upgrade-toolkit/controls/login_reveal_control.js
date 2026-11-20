'use strict';
// login_reveal_control.js: a login page that folds the local username/password form under a link (field run SITS: an
// SSO starter app, login.html shows "Sign in with SSO" and keeps the form behind "Show alternative login").
//
//   node login_reveal_control.js <patched engine dir> <unpatched engine dir>
//
// A local HTTP server plays the app. /login.html has #usernameInput/#passwordInput/#loginButton in a container that is
// display:none until the .alt-login link is clicked; /login-open.html shows the same form unfolded; / is the app shell
// once signed in. One line per case, "ok <case>" or "FAIL <case>", exit 0 when every case holds:
//   bin/loginreveal.js on the folded page          clicks the link, the password input becomes visible (returns true)
//   bin/loginreveal.js on the unfolded page        returns false and clicks nothing
//   bin/loginreveal.js on a page without a form    returns false
//   bin/loginreveal.js with only a "Hide ..." link returns false (never clicks a hide link)
//   unpatched engine on the folded page            login refused (the defect: no visible form, the old app looks broken)
//   patched engine on the folded page              signs in and reaches the app shell
//   patched engine on the unfolded page            still signs in (no regression)
const http = require('http');
const fs = require('fs');
const path = require('path');
const { revealLocalLogin } = require('../bin/loginreveal.js');

const [patchedDir, plainDir] = process.argv.slice(2).map((d) => path.resolve(d));
const USER = 'smoke_user', PASS = 'Smoke-only-1!';
const FORM = `<input id="usernameInput" type="text"><input id="passwordInput" type="password">
  <button id="loginButton" type="button" onclick="go()">Sign in</button><div id="loginMessage"></div>`;
const SCRIPT = `<script>
  function go() {
    fetch('/xas/', { method: 'POST', body: JSON.stringify({ action: 'login', params: {
      username: document.getElementById('usernameInput').value, password: document.getElementById('passwordInput').value } }) })
      .then((r) => { if (r.status === 200) location.href = '/'; });
  }
  </script>`;
const FOLDED = `<!doctype html><html><body><a id="sso" href="/oauth/v2/login">Sign in with SSO</a>
  <div class="sso-label"><a class="alt-login" href="javascript:void(0)" onclick="document.getElementById('f').style.display='block'">
      Show alternative login
    </a></div>
  <div id="f" style="display:none">${FORM}
  <a class="alt-login" href="javascript:void(0)" onclick="document.getElementById('f').style.display='none'">
      Hide alternative login
    </a></div>${SCRIPT}</body></html>`;
const OPEN = `<!doctype html><html><body><div id="f">${FORM}</div>${SCRIPT}</body></html>`;
const NOFORM = `<!doctype html><html><body><a href="/oauth/v2/login">Sign in with SSO</a></body></html>`;
const HIDEONLY = `<!doctype html><html><body><div id="f" style="display:none">${FORM}</div>
  <a id="hide" class="alt-login" href="javascript:void(0)" onclick="window.__clicked=1">Hide alternative login</a></body></html>`;
const SHELL = `<!doctype html><html><body><div class="mx-page"><div class="mx-navigationtree"><a title="Home" href="#">Home</a></div>
  <div class="mx-name-homeGrid">Home</div></div></body></html>`;

const server = http.createServer((req, res) => {
  const signedIn = /(^|;\s*)sess=ok/.test(req.headers.cookie || '');
  if (req.method === 'POST' && req.url === '/xas/') {
    let body = '';
    req.on('data', (c) => { body += c; });
    req.on('end', () => {
      const p = (JSON.parse(body || '{}').params) || {};
      if (p.username === USER && p.password === PASS) { res.writeHead(200, { 'Set-Cookie': 'sess=ok; Path=/', 'Content-Type': 'application/json' }); res.end('{}'); }
      else { res.writeHead(401); res.end('{}'); }
    });
    return;
  }
  res.writeHead(200, { 'Content-Type': 'text/html' });
  if (req.url.startsWith('/login-open.html')) return res.end(OPEN);
  if (req.url.startsWith('/login-noform.html')) return res.end(NOFORM);
  if (req.url.startsWith('/login-hideonly.html')) return res.end(HIDEONLY);
  if (req.url.startsWith('/login.html')) return res.end(FOLDED);
  return res.end(signedIn ? SHELL : NOFORM);
});

function engine(dir, port) {
  fs.writeFileSync(path.join(dir, 'project.config.js'), `'use strict';
module.exports = { root: ${JSON.stringify(dir)}, mpr: null, mxcli: 'mxcli', dsCss: null, defaultPort: '${port}',
  readySelectors: ['.mx-name-homeGrid'], NAV: {}, TARGETS: { 'full-app': [] },
  credentials: () => ({ user: '${USER}', pass: '${PASS}', fallbackUser: '', fallbackPass: '' }) };\n`);
  return require(path.join(dir, 'helpers.js'));
}
async function attempt(H) {
  const { browser, page } = await H.launchBrowser();
  try {
    const li = await H.login(page);
    const shell = await page.locator('.mx-name-homeGrid').first().isVisible().catch(() => false);
    return { ok: !!li.ok, shell, reason: li.reason || '' };
  } finally { await browser.close().catch(() => {}); }
}

(async () => {
  await new Promise((r) => server.listen(0, '127.0.0.1', r));
  const port = server.address().port, base = `http://127.0.0.1:${port}`;
  process.env.APP_PORT = String(port); process.env.APP_URL = base;
  let bad = 0;
  const line = (good, name, extra) => { if (!good) bad++; console.log(`${good ? 'ok  ' : 'FAIL'} ${name}${extra ? ': ' + extra : ''}`); };
  const { chromium } = require(require.resolve('playwright', { paths: [process.env.NODE_PATH || '', path.join(process.env.HOME || '', 'mendix-playwright/node_modules')].filter(Boolean) }));
  const b = await chromium.launch(); const page = await b.newPage();
  await page.goto(base + '/login.html'); 
  const before = await page.locator('#passwordInput').isVisible();
  const r1 = await revealLocalLogin(page);
  line(!before && r1 === true && await page.locator('#passwordInput').isVisible(), 'loginreveal on the folded page shows the form', `before visible ${before}, returned ${r1}`);
  await page.goto(base + '/login-open.html');
  line((await revealLocalLogin(page)) === false && await page.locator('#passwordInput').isVisible(), 'loginreveal on the unfolded page returns false');
  await page.goto(base + '/login-noform.html');
  line((await revealLocalLogin(page)) === false, 'loginreveal on a page with no form returns false');
  await page.goto(base + '/login-hideonly.html');
  const r4 = await revealLocalLogin(page);
  line(r4 === false && !(await page.evaluate(() => window.__clicked)), 'loginreveal never clicks a "Hide ..." link');
  await b.close();
  process.env.LOGIN_PATH = '/login.html';
  const a = await attempt(engine(plainDir, port));
  line(!a.ok && !a.shell, 'unpatched engine on the folded page: login refused (the defect reproduced)', a.reason);
  const c = await attempt(engine(patchedDir, port));
  line(c.ok && c.shell, 'patched engine on the folded page signs in and reaches the app shell', c.reason);
  process.env.LOGIN_PATH = '/login-open.html';
  const d = await attempt(engine(patchedDir, port));
  line(d.ok && d.shell, 'patched engine on the unfolded page still signs in', d.reason);
  server.close();
  process.exit(bad ? 1 : 0);
})().catch((e) => { console.error('control error:', e && e.stack || e); server.close(); process.exit(3); });
