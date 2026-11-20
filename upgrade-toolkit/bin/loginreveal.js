'use strict';
// loginreveal.js: reveal a username/password form that the login page hides behind a link (field run SITS: a starter app
// whose login.html shows an SSO button and keeps the local form folded under "Show alternative login"; the form is in
// the DOM, not visible, so every walk timed out on page.fill and the OLD app looked broken).
//
//   const { revealLocalLogin } = require('./loginreveal.js');
//   await page.goto(loginUrl); await revealLocalLogin(page); await page.fill('#usernameInput', user); ...
//
// Returns true when it clicked a reveal link and the password field became visible, false otherwise (form already
// visible, no password field in the page at all, or no link whose text names a local/alternative login). Never throws.
// The same text test is inlined in run_journeys.py's engine patch (the scratch engine copy cannot require this file).
const ALT = /^(?!.*\bhide\b).*((alternative|alternate|other|local)\s+(login|log\s?in|sign.?in|method)|(sign|log)\s?in\s+with\s+(a\s+)?(username|password|local|email)|(username|password)\s+(login|log\s?in|sign.?in))/i;

async function revealLocalLogin(page, timeout = 4000) {
  try {
    const pw = page.locator('#passwordInput, input[type=password]').first();
    if (await pw.isVisible().catch(() => false)) return false;
    if (!(await pw.count().catch(() => 0))) return false;
    const links = page.locator('.alt-login, a, button, [role=button]').filter({ hasText: ALT });
    const n = Math.min(await links.count().catch(() => 0), 6);
    for (let i = 0; i < n; i++) {
      const l = links.nth(i);
      if (!(await l.isVisible().catch(() => false))) continue;
      await l.click({ timeout: 2000 }).catch(() => {});
      if (await pw.waitFor({ state: 'visible', timeout }).then(() => true).catch(() => false)) return true;
    }
  } catch (e) { /* a reveal that cannot be done leaves the page as it was: the caller's own fill reports it */ }
  return false;
}

module.exports = { revealLocalLogin, ALT };
