// settle.js: wait until a Mendix page has finished loading before a screenshot is taken (E6-17).
// Run E6: the old app's MonitoringDashboard smoke shot was the Home page with the Mendix progress bar, taken 1.5 s
// after the page opened. shotdiff then compared a loading screen with a finished one and the pair could not be judged.
//
// A page counts as SETTLED when, for `stableMs` in a row:
//   - no visible loading indicator (Mendix progress bar, data view / list view / grid loading state, spinner,
//     aria-busy), see BUSY below
//   - the DOM size (document.body.innerHTML length) did not change
// plus one attempt at Playwright's 'networkidle' (bounded, a page with polling never idles, that is not fatal).
// settle(page) never throws. It returns { ok, ms, reason, stuck }: ok false means the page was still loading when the
// time ran out; the caller saves the screenshot as <name>-LOADING.png and shotdiff marks the pair INVALID (never
// acceptable: take it again).
// STUCK (T7-22): when the time runs out with a loading indicator still shown but the DOM size unchanged for the last
// `stuckMs` (SETTLE_STUCK_MS, default 5000), the page is not loading, it is stuck (a 10.6 Data grid 2 with 0 rows keeps
// its mx-progress bar, an error page keeps one too). settle returns { ok: false, stuck: true } and the caller saves
// <name>-STUCK.png: shotdiff keeps the pair INVALID, but a person may close it with an accept line after a look.
// The full timeout is always waited first, so a slow page that is still fetching is never called STUCK early.
// TOP BAR (B4N1-14, Opcenter EF on 10.24/11): a thin progress bar pinned to the top edge of the window (the UMC session
// renew nanoflow keeps one running) never goes away on pages that rendered fully, so StarterKit.HowTo, Contents and
// three more were named -STUCK and only PASSed through shotdiff's "equal below the top 10 px" rule. A shown indicator
// whose box lies within the top TOPBAR_PX (10, the same band shotdiff uses) and is at most TOPBAR_PX high is reported
// apart (topbar) and ignored, bounded: only when it is the ONLY indicator, the DOM stood still for `topbarMs`
// (SETTLE_TOPBAR_MS, default 3000) and the page content has visible text (the .mx-placeholder elements, or the body when
// there are none). Then settle returns { ok: true, topbar: true, reason: 'top bar ignored: ...' }. A blank page under
// the same bar (the Opcenter home pages, no text) and any page with another indicator stay STUCK / LOADING as before.
// LAZY PLACEHOLDERS (GM-33): a lazy-loading widget (Marketplace "LazyloadingDataPlaceholder", In View Content Renderer,
// Skeleton) draws a placeholder first and its content later, so the baseline shot showed a page with holes. A shown
// placeholder (LAZY below) counts as busy like any loading indicator, bounded by the same timeout. On timeout the reason
// says "lazy-load placeholder(s) still present: <class>" and the page is never passed silently (ok false, never
// stuck-ignored as a top bar). ASSUMED: no captured page in this repo shows the placeholder's DOM, so the selectors are
// class-name patterns taken from the widget names, not read from a captured page; replace them with the real class
// once a page capture exists (FEEDBACK GM-33).
// FALSE MATCH: a class that matches but never goes away (a permanent "skeleton" theme class) would fail every page. When
// the timeout ends on the lazy path with the DOM unchanged for stuckMs the reason says so and names SETTLE_LAZY_OFF=1,
// which turns lazy detection off entirely (the pre-GM-33 behaviour).
// pageSettled() runs in the browser (page.evaluate) and in node with a fake document (controls/smokewalk_predicates.js).

const BUSY = [
  '.mx-progress', '.mx-progress-indicator', '.mx-progress-line',
  '.mx-dataview-loading', '.mx-listview-loading', '.mx-templategrid-loading', '.mx-datagrid-loading',
  '.widget-datagrid-loading', '.widget-gallery-loading', '.mx-loading',
  '.spinner', '.spinner-border', '.loading-spinner', '[aria-busy="true"]',
];

// ASSUMED (GM-33): class-name substrings, matched case-insensitively; no captured page shows the real markup.
// ONE copy: settle() passes LAZY (and BUSY) into pageSettled as an argument, because pageSettled is serialised into the
// browser and cannot see this const. SETTLE_LAZY_OFF=1 passes an empty list (lazy detection off, the pre-GM-33 behaviour).
const LAZY = [
  '[class*="lazyload" i]', '[class*="lazy-load" i]', '[class*="skeleton" i]', '[class*="dataview-loader" i]',
];

const TOPBAR_PX = 10;

// cfg = { busy, lazy, top } (arrays of selectors, band in px); a bare array is taken as the busy list (old call shape).
function pageSettled(cfg) {
  try {
    const c = Array.isArray(cfg) ? { busy: cfg } : (cfg || {});
    const sel = (c.busy || BUSY).join(', ');
    const lazyList = c.lazy || LAZY;
    const band = c.top || 10;
    const shown = e => {
      try {
        if (e.getClientRects && !e.getClientRects().length) return false;
        const s = typeof getComputedStyle === 'function' ? getComputedStyle(e) : (e.style || {});
        return s.display !== 'none' && s.visibility !== 'hidden' && s.opacity !== '0';
      } catch (x) { return false; }
    };
    const name = e => (e.className && String(e.className).split(/\s+/)[0]) || e.tagName || '?';
    // B4N1-14: a thin bar at the very top of the window is reported apart; anything else shown is busy
    const thinTop = e => {
      try {
        if (!e.getBoundingClientRect) return false;
        const r = e.getBoundingClientRect();
        return r.top >= -1 && r.top <= band && r.height <= band && r.top + r.height <= band + 1;
      } catch (x) { return false; }
    };
    const lazy = lazyList.length ? [...document.querySelectorAll(lazyList.join(', '))].filter(shown).map(name) : [];
    const shownAll = [...document.querySelectorAll(sel)].filter(shown);
    const busy = shownAll.filter(e => !thinTop(e)).map(name);
    const topbar = shownAll.filter(thinTop).map(name);
    const size = document.body ? document.body.innerHTML.length : 0;
    let text = 0;
    try {
      const ph = document.querySelectorAll('.mx-placeholder');
      const roots = ph && ph.length ? [...ph] : (document.body ? [document.body] : []);
      text = roots.reduce((n, e) => n + String(e.innerText || '').replace(/\s+/g, '').length, 0);
    } catch (x) { text = 0; }
    return { busy: busy.concat(lazy.map(n => 'lazy-placeholder:' + n)), size, topbar, text, lazy };
  } catch (e) {
    return { busy: ['error: ' + String(e && e.message || e).slice(0, 80)], size: -1 };
  }
}

async function settle(page, opts = {}) {
  const timeout = opts.timeout ?? Number(process.env.SETTLE_MS || 15000);
  const stableMs = opts.stableMs ?? 750;
  const stuckMs = opts.stuckMs ?? Number(process.env.SETTLE_STUCK_MS || 5000);
  const topbarMs = opts.topbarMs ?? Number(process.env.SETTLE_TOPBAR_MS || 3000);
  const lazyOff = opts.lazyOff ?? process.env.SETTLE_LAZY_OFF === '1';   // escape hatch for a permanent false match
  const arg = { busy: BUSY, lazy: lazyOff ? [] : LAZY, top: TOPBAR_PX };
  const poll = 250;
  const t0 = Date.now();
  let last = null, stableSince = 0, sizeSince = 0, lastBusy = [], topSince = 0;
  await page.waitForLoadState('networkidle', { timeout: Math.min(5000, timeout) }).catch(() => {});
  while (Date.now() - t0 < timeout) {
    const s = await page.evaluate(pageSettled, arg).catch(e => ({ busy: ['evaluate: ' + String(e.message).split('\n')[0]], size: -1 }));
    const top = s.topbar || [];
    lastBusy = s.busy.concat(top);
    if (s.size !== last || s.size < 0) sizeSince = Date.now();   // DOM size changed (or unreadable): not standing still
    // B4N1-14: only a thin top bar left, on a page with text, DOM still for topbarMs: the bar is not page loading
    if (!s.busy.length && top.length && s.size === last && s.size >= 0 && (s.text || 0) > 0) {
      if (!topSince) topSince = Date.now();
      if (Date.now() - topSince >= topbarMs && Date.now() - sizeSince >= topbarMs)
        return { ok: true, topbar: true, ms: Date.now() - t0,
                 reason: `top bar ignored: ${[...new Set(top)].slice(0, 2).join(', ')} within the top ${TOPBAR_PX}px, ` +
                         `DOM unchanged for ${Date.now() - sizeSince}ms, ${s.text} chars of page text` };
    } else {
      topSince = 0;
    }
    if (!lastBusy.length && s.size === last) {
      if (!stableSince) stableSince = Date.now();
      if (Date.now() - stableSince >= stableMs) return { ok: true, ms: Date.now() - t0 };
    } else {
      stableSince = 0;
    }
    last = s.size;
    await page.waitForTimeout(poll);
  }
  const ms = Date.now() - t0, still = Date.now() - sizeSince;
  const busy = [...new Set(lastBusy)].slice(0, 4).join(', ');
  const lazyLeft = lastBusy.filter(b => /^lazy-placeholder:/.test(b));
  if (lazyLeft.length) {
    const names = [...new Set(lazyLeft)].slice(0, 4).map(b => b.slice(17)).join(', ');
    const other = [...new Set(lastBusy.filter(b => !/^lazy-placeholder:/.test(b)))].slice(0, 3).join(', ');
    const unchanged = sizeSince && still >= stuckMs
      ? `; placeholder present and DOM unchanged for ${still}ms; if this class is permanent it is a false match — set SETTLE_LAZY_OFF=1` : '';
    return { ok: false, ms, lazy: true,
             reason: `still loading: lazy-load placeholder(s) still present: ${names}${other ? '; also ' + other : ''}${unchanged}` };
  }
  const real = lastBusy.length && !lastBusy.some(b => /^(error|evaluate):/.test(b));
  if (real && sizeSince && still >= stuckMs)
    return { ok: false, stuck: true, ms, reason: `stuck: ${busy} shown, DOM unchanged for ${still}ms` };
  return { ok: false, ms, reason: lastBusy.length ? 'still loading: ' + busy : 'DOM still changing' };
}

module.exports = { BUSY, LAZY, TOPBAR_PX, pageSettled, settle };
