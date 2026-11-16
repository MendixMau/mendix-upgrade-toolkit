#!/usr/bin/env node
// widgetrender.js: is a pluggable widget drawn, not only present in the DOM? (E2E-R1)
// Why: FSM 9.24 -> 11.12.7. The Scheduler page opened, the smoke walk and the journeys PASSed, and the scheduler itself
// was blank: Ultimate Scheduler 1.4.0 under the React client drew its toolbar and time header, the resource rows area
// was 0 px tall, no row and no appointment. The client threw "Cannot read properties of undefined (reading
// 'setTimeSpan')" from the widget's own script and React #520. The journey guards skip anything inside a pluggable
// widget (steps/journeys.md, T1-25) and the page guard only asks that the page is there, so nothing looked inside.
// The fix (Ultimate Scheduler 3.8.0) was found by a person looking at a screenshot.
//
// Generic rules, every widget (FAIL names the first that broke):
//   found    a shown .mx-name-<widget> (the one in the topmost open dialog first); "Could not render widget '...<widget>'"
//            in its place is said as such (the scheduler that threw long enough was replaced by it)
//   size     its box is wider and taller than 0
//   drawn    it has a drawn descendant (box above 2 x 2 px, not hidden) with text, an image, a canvas or an svg
//   no error no "Could not render widget" / .alert-danger text inside it
//   no client error from a widget script: a pageerror or console error since the last check whose text or stack names
//            /widgets/ (resource 404s and errors from other scripts are listed as notes, not FAILs; "strict": true
//            FAILs on every client error)
// Per widget, playbooks/widget-render.tsv rows whose root class (one of a comma list) the widget has: "h>0" (every match drawn with a height)
// and "min=N" (at least N drawn matches); rows marked data apply only with "data": true (the step's DB check showed
// the records exist: an empty scheduler on an empty table is not a defect). Inline "expect": [{"sel", "min"|"h"}] too.
// It polls up to timeoutMs (default 15000) until every rule holds on a still widget (nothing loading, two looks one
// second apart alike), so a widget still fetching gets its time; the verdict is the last state seen.
//
//   journey step: {"do": "rendered", "widget": "bizzomateUltimateScheduler1", "data": true}
//   module:      const R = require('./widgetrender.js'); R.watch(page) once after newPage; await R.check(page, a)
//   CLI:         node widgetrender.js --url http://localhost:8080 --user Role=name:pass --open Scheduler \
//                     --widget bizzomateUltimateScheduler1 [--data] [--strict] [--shot f.png] [--out r.json]
//                exit 0 PASS, 1 FAIL, 2 could not judge (login failed, menu item not found).
const fs = require('fs');
const path = require('path');
const os = require('os');

// the toolkit's playbook; run_journeys.py copies it next to this file in the engine copy
const PLAYBOOK = [path.join(__dirname, 'widget-render.tsv'), path.join(__dirname, '..', 'playbooks', 'widget-render.tsv')].find(f => fs.existsSync(f)) || '';
const IGNORE = [/favicon/i, /Failed to load resource/i];
const LOGS = new WeakMap();

function rules(file = PLAYBOOK) {
  if (!file || !fs.existsSync(file)) return [];
  const rows = fs.readFileSync(file, 'utf8').split('\n').filter(l => l.trim() && !l.startsWith('#'));
  const head = rows.shift().split('\t');
  return rows.map(l => Object.fromEntries(l.split('\t').map((v, i) => [head[i], v])));
}

// Record client errors from the moment the page exists; check() reads the ones since its previous call.
function watch(page) {
  if (LOGS.has(page)) return;
  const log = { errs: [], seen: 0 }; LOGS.set(page, log);
  page.on('pageerror', e => log.errs.push('pageerror: ' + String(e.stack || e.message).slice(0, 600)));
  page.on('console', m => {
    if (m.type() !== 'error') return;
    const loc = m.location && m.location();
    log.errs.push('console: ' + m.text().slice(0, 600) + (loc && loc.url ? ' @ ' + loc.url : ''));
  });
}

// One look at the widget: geometry and the playbook/inline parts, measured in the page.
function measure(page, name, parts) {
  return page.evaluate(([name, parts]) => {
    const shown = e => { const r = e.getBoundingClientRect(); const cs = getComputedStyle(e);
      return r.width > 2 && r.height > 2 && cs.visibility !== 'hidden' && cs.display !== 'none' && cs.opacity !== '0'; };
    const all = [...document.querySelectorAll('.mx-name-' + CSS.escape(name))];
    const dlg = [...document.querySelectorAll('.modal-dialog, .mx-dialog, .mx-window')].filter(shown).pop();
    const el = (dlg && all.find(e => dlg.contains(e) && shown(e))) || all.find(shown) || all[0];
    // a widget that threw while mounting is replaced by the client's own message, without the mx-name class
    const crash = (document.body.innerText.match(new RegExp("Could not render widget '[^']*\\." + name + "'")) || [])[0];
    if (!el) return { found: false, crash };
    const r = el.getBoundingClientRect();
    const kids = [...el.querySelectorAll('*')].filter(shown);
    const drawn = kids.filter(k => k.matches('img, canvas, svg') || [...k.childNodes].some(n => n.nodeType === 3 && n.textContent.trim())).length;
    const errText = [...el.querySelectorAll('.alert-danger, .mx-widget-error')].filter(shown).map(e => e.textContent.trim().slice(0, 160));
    if (/Could not render widget/i.test(el.textContent)) errText.push('Could not render widget');
    const got = parts.map(p => {
      const m = [...el.querySelectorAll(p.sel)];
      return { ...p, n: m.length, drawn: m.filter(shown).length,
               flat: m.filter(e => { const b = e.getBoundingClientRect(); return b.width > 0 && b.height < 1; }).length };
    });
    return { found: true, cls: el.className, box: [r.x, r.y, r.width, r.height].map(Math.round), kids: kids.length, drawn,
             errText, busy: !!el.querySelector('[class*="is-fetching"], [class*="is-loading"], .mx-progress'), parts: got };
  }, [name, parts]);
}

function verdict(m, name) {
  if (!m.found) return m.crash ? 'not rendered: the client shows "' + m.crash + '"' : 'not found: no .mx-name-' + name + ' on the screen';
  if (!(m.box[2] > 0 && m.box[3] > 0)) return `zero size: drawn ${m.box[2]} x ${m.box[3]} px`;
  if (!m.drawn) return `nothing drawn: ${m.kids} shown descendants, none with text, an image, a canvas or an svg`;
  if (m.errText.length) return 'error text in the widget: ' + m.errText[0];
  for (const p of m.parts) {
    if (p.h && (!p.n || p.flat)) return `${p.sel}: ${p.flat} of ${p.n} drawn 0 px tall (${p.why})`;
    if (p.min && p.drawn < p.min) return `${p.sel}: ${p.drawn} drawn, at least ${p.min} expected (${p.why})`;
  }
  return null;
}

// a: {widget, data, strict, expect, timeoutMs, rules}. Returns {ok, reason, m, errors, notes}; never throws on a FAIL.
async function check(page, a) {
  watch(page);
  const all = a.rules || rules();
  const ms = a.timeoutMs || 15000, until = Date.now() + ms;
  let m, bad, parts = [], last = '';
  for (;;) {
    // the root's classes pick the playbook rows; read each round, the widget may mount after the page opened
    const cls = String(await page.evaluate(n => { const e = document.querySelector('.mx-name-' + CSS.escape(n)); return e ? e.className : ''; }, a.widget).catch(() => '')).split(/\s+/);
    parts = all.filter(r => r.root.split(',').some(c => cls.includes(c)) && (r.when !== 'data' || a.data))
      .map(r => ({ sel: r.selector, h: r.rule === 'h>0', min: (r.rule.match(/^min=(\d+)$/) || [])[1] | 0, why: r.reason }))
      .concat((a.expect || []).map(x => ({ sel: x.sel, h: !!x.h, min: x.min | 0, why: 'step expect' })));
    m = await measure(page, a.widget, parts).catch(e => ({ found: false, err: String(e.message) }));
    bad = verdict(m, a.widget);
    // a PASS needs a still widget: nothing loading and the same box, descendants and parts as one second before
    // (the fixed scheduler PASSed half-mounted, 18 descendants and none of its playbook classes yet)
    const sig = JSON.stringify([m.cls, m.box, m.kids, m.parts]);
    if ((!bad && !m.busy && sig === last) || Date.now() > until) break;
    last = sig;
    await page.waitForTimeout(bad ? 500 : 1000);
  }
  const log = LOGS.get(page); const errs = log.errs.slice(log.seen); log.seen = log.errs.length;
  const mine = errs.filter(e => !IGNORE.some(re => re.test(e)) && (a.strict || /\/widgets\//.test(e)));
  const notes = errs.filter(e => !mine.includes(e));
  if (mine.length) bad = (bad ? bad + '; ' : '') + 'client error from a widget script: ' + mine[0].split('\n')[0].slice(0, 200);
  if (bad && m.busy) bad += ` (still loading after ${ms} ms)`;
  return { ok: !bad, reason: bad || '', m, errors: mine, notes };
}

module.exports = { watch, check, rules, measure };

if (require.main === module) (async () => {
  const o = { users: [] };
  const av = process.argv.slice(2);
  for (let i = 0; i < av.length; i++) {
    const k = av[i];
    if (k === '--data' || k === '--strict') o[k.slice(2)] = true;
    else if (k === '--user') o.users.push(av[++i]);
    else o[k.slice(2)] = av[++i];
  }
  if (!o.url || !o.widget || !o.users.length) { console.error('usage: widgetrender.js --url U --user Role=name:pass --widget W [--open MenuCaption] [--data] [--strict] [--shot f.png] [--out r.json]'); process.exit(2); }
  const dirs = [process.env.PLAYWRIGHT_DIR, path.join(os.homedir(), 'mendix-playwright/node_modules/playwright'), 'playwright'].filter(Boolean);
  let pw; for (const d of dirs) { try { pw = require(d); break; } catch (e) { /* next */ } }
  if (!pw) { console.error('widgetrender: playwright not found (set PLAYWRIGHT_DIR)'); process.exit(2); }
  // no keychain prompt on macOS: Playwright's own profile, a mock keychain and a plain password store
  const browser = await pw.chromium.launch({ args: ['--use-mock-keychain', '--password-store=basic'] });
  let code = 0; const out = [];
  for (const u of o.users) {
    const role = u.slice(0, u.indexOf('=')), cred = u.slice(u.indexOf('=') + 1);
    const user = cred.slice(0, cred.indexOf(':')), pass = cred.slice(cred.indexOf(':') + 1);
    const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 } }); const page = await ctx.newPage();
    watch(page);
    const r = { role, widget: o.widget };
    try {
      await page.goto(o.url.replace(/\/$/, '') + '/login.html', { waitUntil: 'domcontentloaded' });
      await page.fill('#usernameInput', user); await page.fill('#passwordInput', pass); await page.click('#loginButton');
      await page.waitForSelector('.mx-page', { timeout: 30000 });
      if (o.open) {
        const exact = new RegExp('^\\s*' + o.open.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '\\s*$');
        const item = page.locator('.mx-navigationtree a, .mx-navbar a, .mx-menubar a').filter({ hasText: exact }).first();
        await item.waitFor({ timeout: 15000 }).catch(() => {});
        if (!await item.count()) throw new Error('menu item "' + o.open + '" not found');
        await item.click();
      }
      Object.assign(r, await check(page, { widget: o.widget, data: o.data, strict: o.strict }));
      r.verdict = r.ok ? 'PASS' : 'FAIL';
    } catch (e) { r.verdict = 'INVALID'; r.reason = String(e.message).split('\n')[0]; }
    if (o.shot) await page.screenshot({ path: o.users.length > 1 ? o.shot.replace(/\.png$/, '-' + role + '.png') : o.shot }).catch(() => {});
    await ctx.close();
    code = Math.max(code, r.verdict === 'PASS' ? 0 : r.verdict === 'FAIL' ? 1 : 2);
    out.push(r);
    const m = r.m || {};
    console.log(`${r.verdict.padEnd(7)} ${role} .mx-name-${o.widget}${r.reason ? ': ' + r.reason : ''}`);
    if (m.found) console.log(`        box ${m.box.join(',')}, ${m.drawn} drawn of ${m.kids} shown descendants; ` + m.parts.map(p => `${p.sel} ${p.drawn}/${p.n} drawn${p.flat ? ', ' + p.flat + ' at 0 px' : ''}`).join('; '));
    for (const e of r.errors || []) console.log('        error: ' + e.split('\n')[0].slice(0, 160));
    for (const e of r.notes || []) console.log('        note:  ' + e.split('\n')[0].slice(0, 160));
  }
  await browser.close();
  if (o.out) fs.writeFileSync(o.out, JSON.stringify(out, null, 1));
  process.exit(code);
})().catch(e => { console.error('widgetrender: ' + e.stack); process.exit(2); });
