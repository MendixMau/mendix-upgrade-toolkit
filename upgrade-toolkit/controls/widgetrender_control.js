'use strict';
// widgetrender_control.js: bin/widgetrender.js measure/verdict/check in a real browser (E2E-R1 review fixes).
//
//   node widgetrender_control.js          (NODE_PATH must reach playwright with a browser)
//
// Pages: fixtures/widgetrender/*.html, a minimal reconstruction of the Bryntum grid classes the playbook selects,
// not a captured page. Cases, one line each ("ok <case>: <detail>" or "FAIL <case>: <detail>"):
//   broken: subgrid 0 px tall, no rows, no events      FAIL naming .b-grid-subgrid
//   broken, part visibility:hidden, 200 px tall         FAIL naming .b-grid-subgrid (the old flat count missed it)
//   fixed: rows and events drawn                       PASS
//   fixed, no data flag: only the h>0 row applies       PASS
//   broken, no data flag: the h>0 row still fails       FAIL
//   error logged before the step                        PASS (an earlier page's /widgets/ error is not this step's)
//   error logged during the step                        FAIL naming the widget script error
// Exit 0 when every case holds, 1 otherwise.
const path = require('path');
const { chromium } = require('playwright');
const R = require('../bin/widgetrender.js');
const dir = path.join(__dirname, 'fixtures', 'widgetrender');
const url = f => 'file://' + path.join(dir, f);
const A = { widget: 'scheduler1', data: true, timeoutMs: 2500 };

(async () => {
  let fail = 0;
  const check = (name, ok, detail) => { if (!ok) fail++; console.log(`${ok ? 'ok  ' : 'FAIL'} ${name}: ${detail}`); };
  const browser = await chromium.launch({ args: ['--use-mock-keychain', '--password-store=basic'] });
  const open = async f => { const ctx = await browser.newContext(); const page = await ctx.newPage(); R.watch(page); await page.goto(url(f)); return page; };
  let p, r;
  p = await open('scheduler-broken.html'); r = await R.check(p, A);
  check('broken: 0 px subgrid', !r.ok && /\.b-grid-subgrid/.test(r.reason), r.reason);
  p = await open('scheduler-broken-hidden.html'); r = await R.check(p, A);
  const part = r.m.parts.find(x => x.sel === '.b-grid-subgrid');
  check('broken: part hidden', !r.ok && /\.b-grid-subgrid: 1 of 1/.test(r.reason) && part.flat === 1, r.reason);
  p = await open('scheduler-fixed.html'); r = await R.check(p, A);
  check('fixed: rows and events drawn', r.ok, r.ok ? 'PASS' : r.reason);
  r = await R.check(p, { ...A, data: false });
  check('fixed, no data flag', r.ok, r.ok ? 'PASS' : r.reason);
  p = await open('scheduler-broken.html'); r = await R.check(p, { ...A, data: false });
  check('broken, no data flag', !r.ok && /\.b-grid-subgrid/.test(r.reason), r.reason);
  p = await open('scheduler-fixed.html');
  await p.evaluate(() => console.error('Error from /widgets/ciphix/scheduler.js: earlier page'));
  await p.waitForTimeout(200);
  r = await R.check(p, A);
  check('error logged before the step', r.ok && !r.errors.length, r.ok ? 'PASS' : r.reason);
  setTimeout(() => p.evaluate(() => console.error('Error from /widgets/ciphix/scheduler.js: during step')).catch(() => {}), 300);
  r = await R.check(p, A);
  check('error logged during the step', !r.ok && /client error from a widget script/.test(r.reason), r.reason);
  await browser.close();
  console.log(fail ? `${fail} FAILED` : 'all ok');
  process.exit(fail ? 1 : 0);
})().catch(e => { console.log(`FAIL control crashed: ${e.stack}`); process.exit(1); });
