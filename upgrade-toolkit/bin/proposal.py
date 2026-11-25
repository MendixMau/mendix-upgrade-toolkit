#!/usr/bin/env python3
"""proposal.py: the upgrade proposal a person signs before anything in the app changes (trust spec section 2).

  proposal.py --work W [--source V --target V [--target2 V]] [--original W/original.mpr] [--app APPDIR] [--unattended]
  proposal.py --status --work W          prints: signed | paused | unsigned | none (no PROPOSAL.md); exit 0

Reads the triage outputs in W (each by the name triage writes it; an input that is absent or unreadable is listed under
"not measured" in section 5, never skipped silently):
  versions.txt, plan-pre.txt, plan.txt, module-jumps.txt            versions, module updates (steps/triage.md items 1-3, 10)
  kept.txt (W, else APP/.stepupdate/kept.txt)                       modules kept at their version (stepupdate output; a rerun)
  stranded.md                                                       one bullet or table row per stranded module (item 3)
  localedits.json                                                   RED / logic / Java and theme file edits (item 5)
  release-impact.md                                                 rows whose "handled" cell is empty need a person (item 10)
  replacements.md                                                   replacement_check.py rows, HIT and UNKNOWN open (item 10)
  absentmods.json                                                   absentmods.py --json: modules a planned update calls that the app lacks (GM-12; optional, an older run has none)
  owngone.out                                                       crosscalls.py --own: own documents that use targets a planned package drops (GF-39; optional, an older run has none)
  keptvendor.json                                                   keptvendor.py --json: kept themesource uses a planned package removes (GM-15; optional; rows for the app's own styling exist at triage, GF-56, rows for a kept module once kept.txt exists)
  keptstyle.json                                                    keptstyle.py --json: platform widget selectors in a kept themesource (MC-11; optional, written once kept.txt exists)
  dojo-react.md                                                     dojo_report.py: can't move / not researched widgets (item 10)
  actions.json                                                      action_inventory.py summary (action count)
  journey-scope.json                                                journey_scope.py: reachable / out of scope split of the actions
  apimock-inventory.json                                            apimock.py inventory --json: external systems
  original.mpr (or --original)                                      modules / pages / microflows, through mprmodel.py
  DECISIONS.md                                                      P-n lines answer the section-3 items
Four inputs of the trust spec have NO output before the convert and are always listed as not measured, with the tool and
why: widgetcover.py (judges rendered pages: the gate's widgets rung), theme_clash.py (needs the NEW Atlas), rolecheck.py
(needs the NEW model), usercode.py (per module, after the update step: .stepupdate/step<n>-<module>.usercode). Java and
theme edits that exist before the update come from localedits.json FILES-EDITED rows, which are read.

Writes W/PROPOSAL.md: six sections in order (summary; done by the toolkit; needs your decision; needs a person anyway;
human effort; sign-off). A comment line stores the hash of the plan inputs. Section 6 is written by a person:
  Signed-off: <name> <yyyy-mm-dd>        or        Status: PAUSED <reason>
Exit: 0 signed (the section-3 items nobody answered take their recommendation, recorded P-n CONFIRMED in DECISIONS.md),
      or unattended (nothing signed; ASSUMED (unattended) lines in DECISIONS.md), 14 unsigned, 15 PAUSED, 2 usage.
W/AGENT-NOTES.md (agent notes, free text) is shown in an "Agent notes" section; this script only reads it, so a rerun keeps the notes.
GM-21: a rerun whose plan only SHRANK against the signed one (every current item was in the signed item set, which the file stores in an
"items" comment; none added or changed) clears the sign-off the same way (same action, same exit, unattended handling unchanged) but writes a "Held back since signed" block
that lists exactly the removed items, so the reading is lighter (the person signs section 6 again; nothing is carried over, no Signed-off
line is written here; the cockpit page does not show the block). A file with no stored item set (written before GM-21) takes the full path below.
A rerun after sign-off whose plan inputs hash differently rewrites the file with a "Changed since signed" block, clears the
sign-off and exits 14 (asked again). kept.txt, DECISIONS.md and the count of open release rows are not in the hash: the
update step writes kept.txt and people close release rows after the sign-off.
Producer of the inputs: the pipeline steps fetch..basewalk (steps/triage.md) and step_propose, which runs
action_inventory.py and apimock.py inventory on original.mpr.
"""
import argparse, base64, datetime, hashlib, json, os, re, sys

# cold test WM1 (2026-11-16): an edited Marketplace module is updated, not kept. Editing a module does not stop its update; an old
# module misses fixes and may not run on the next Mendix version. editroute.py carries the edits over (bin/editroute.py routes).
UPDATE_CARRY = "update to the latest version and carry the edits over (diagram-only dropped, UI and constants replayed, vendor drops checked)"

HERE = os.path.dirname(os.path.abspath(__file__))
TK = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import steps  # noqa: E402  step records (STEP-RECORDS-PLAN.md): the proposal opens one step per item

SIGNED = re.compile(r"^Signed-off:[ \t]+(\S.*?)[ \t]+(\d{4}-\d{2}-\d{2})[ \t]*$")
PAUSED = re.compile(r"^Status:[ \t]+PAUSED[ \t]+(\S.*?)[ \t]*$")
HASH = re.compile(r"^<!-- proposal inputs-hash: ([0-9a-f]{64}) -->$")
# GM-21: the item set the hash was taken over, so a later plan can be compared with what was signed (base64 of a JSON list)
ITEMS = re.compile(r"^<!-- proposal items: ([A-Za-z0-9+/=]*) -->$")
# the toolkit's own assumption for the effort range, hours per touchpoint size; shown as an assumption, not a measurement
HOURS = {"S": (0.5, 2), "M": (2, 8), "L": (8, 40)}
NOT_BEFORE_CONVERT = [
    ("widgetcover.py", "it judges which widget packages the walks render; the walks of the new app exist only at the gate (widgets rung)"),
    ("theme_clash.py", "it compares the app's styling with the NEW Atlas, which exists only after the update"),
    ("rolecheck.py", "it compares the OLD and the NEW model; module roles are checked after each module update"),
    ("usercode.py", "it compares a module's Java user code per module, after the update step (.stepupdate/step<n>-<module>.usercode); "
                    "Java edits that exist now are the localedits.json FILES-EDITED rows"),
]


def load_ra(path=None):
    """Re-architecture catalogue (playbooks/rearchitecture.md): entries '### RA-n title' with '- field: value' lines.
    Tolerant: a missing file, an entry with no usable match regex or a bad regex is skipped, never an error."""
    t = read(path or os.path.join(TK, "playbooks", "rearchitecture.md"))
    out = []
    for blk in re.split(r"(?m)^### (?=RA-\d+\b)", t or "")[1:]:
        m = re.match(r"(RA-\d+)", blk)
        f = {k.lower(): v.strip() for k, v in re.findall(r"(?m)^- ([a-z]+): (.*)$", blk)}
        try:
            rx = re.compile(f.get("match", ""), re.I) if f.get("match") else None
        except re.error:
            rx = None
        if m and rx and f.get("options") and f.get("recommendation"):
            eff = f.get("effort", "M")[:1].upper()
            out.append({"id": m.group(1), "rx": rx, "options": f["options"], "rec": f["recommendation"],
                        "effort": eff if eff in "SML" else "M", "status": f.get("status", "idea")})
    return out


def read(path):
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            return f.read()
    except OSError:
        return None


def lines_of(path):
    t = read(path)
    return None if t is None else [x.rstrip("\n") for x in t.splitlines()]


def tables(text):
    """Markdown tables: [(lower-cased header cells, [row cells])]."""
    out, head, rows = [], None, []
    for line in text.splitlines():
        s = line.strip()
        if not (s.startswith("|") and s.endswith("|")):
            if head:
                out.append((head, rows))
            head, rows = None, []
            continue
        c = [x.strip().replace("\\|", "|") for x in re.split(r"(?<!\\)\|", s[1:-1])]
        if head is None:
            head = [x.lower() for x in c]
        elif all(re.match(r"^:?-{2,}:?$", x) for x in c if x):
            continue
        else:
            rows.append(c)
    if head:
        out.append((head, rows))
    return out


def col(head, row, name):
    return row[head.index(name)] if name in head and head.index(name) < len(row) else ""


class Facts:
    def __init__(self, a):
        self.a = a
        self.W = a.work
        self.measured, self.not_measured = [], []
        self.plan = []          # (module, from, to, when)
        self.kv_seen = False    # keptvendor.json read (GM-15)
        self.ks_seen = False    # keptstyle.json read (MC-11)
        self.kept = {}          # module -> reason
        self.stranded = {}      # module -> text
        self.items3 = []        # decision items
        self.items2 = []        # toolkit items
        self.advisory = []      # advice that is not work of this run (GF-25)
        self.jumps = {}         # module -> (installed, target) from module-jumps.txt
        self.current = {}       # module -> installed version, already the newest that fits (GF-23, "# CURRENT" lines of module-jumps.txt)
        self.items4 = []        # person items
        self.repair_rows = {}
        self.sizes = {}
        self.systems = None
        self.nendpoints = None; self.api_mocked = 0; self.api_unknown = []; self.api_excluded = 0
        self.release_open = None
        self.release_total = None
        self.release_unread = {}  # module -> why; planned modules whose release impact is UNKNOWN (GM-18)
        self.actions = None
        self.scope = None       # journey_scope.py output: line, testability_line, counts
        self.effort = {}        # S/M/L -> count (section 3 items)
        self.filedocs = None    # FileDocument specializations in original.mpr (None: the model was not read)

    def p(self, name):
        return os.path.join(self.W, name)

    def need(self, name, why=""):
        t = read(self.p(name))
        if t is None:
            self.not_measured.append((name, why or "file not found in the work folder"))
            return None
        self.measured.append(name)
        return t

    def add3(self, kind, name, evidence, options, rec, effort, risk):
        self.items3.append({"kind": kind, "name": name, "evidence": evidence, "options": options, "rec": rec,
                            "effort": effort, "risk": risk})

    # ---- inputs ----
    def versions(self):
        t = self.need("versions.txt")
        a = self.a
        self.src, self.tgt, self.tgt2 = a.source or "unknown", a.target or "unknown", a.target2
        if t is not None and not a.source:
            m = re.search(r"^app:\s*(\S+)", t, re.M)
            self.src = m.group(1) if m else "unknown"

    def plans(self):
        jumps = {}
        j = lines_of(self.p("module-jumps.txt"))
        if j is not None:
            self.measured.append("module-jumps.txt")
            for ln in j:
                m = re.match(r"^\s*(\S+)\s+(\S+)\s*->\s*(\S+)", ln)
                if m and not ln.lstrip().startswith("#"):
                    jumps[m.group(1)] = (m.group(2), m.group(3))
        else:
            self.not_measured.append(("module-jumps.txt", "the installed version of each module is unknown; the plan lists the target only"))
        self.jumps = jumps
        # GF-23: modplan.py writes "# CURRENT <Module> <installed> <cid>" for a module whose installed version is already the newest that fits
        self.current = {m.group(1): m.group(2) for m in (re.match(r"^\s*#\s*CURRENT\s+(\S+)\s+(\S+)", ln) for ln in (j or [])) if m}
        # BT-11: the second pass starts from what the first pass left, not from the installed version (Atlas_Core 3.19.0 -> 3.21.1
        # before the convert, then 3.21.1 -> 4.5.1 after it, never 3.19.0 -> 4.5.1 beside the first line)
        left = {}
        for name, when in (("plan-pre.txt", "before the convert"), ("plan.txt", "after the convert")):
            ls = lines_of(self.p(name))
            if ls is None:
                self.not_measured.append((name, "no module updates are known for that pass" + (
                    "" if name == "plan.txt" else " (a 10.x source goes through plan-pre.txt, an 11.x or 9.x source has none)")))
                continue
            self.measured.append(name)
            for ln in ls:
                s = ln.strip()
                if not s or s.startswith("#"):
                    continue
                f = s.split()
                if len(f) < 3:
                    continue
                mod = f[2]
                fr = left.get(mod) or jumps.get(mod, ("?", f[1]))[0]
                left[mod] = f[1]
                self.plan.append((mod, fr, f[1], when))

    def keptmods(self):
        for path in (self.p("kept.txt"), os.path.join(self.a.app or "", ".stepupdate", "kept.txt") if self.a.app else None):
            ls = lines_of(path) if path else None
            if ls is None:
                continue
            self.measured.append("kept.txt")
            for ln in ls:
                f = ln.strip().split(None, 1)
                if f and not f[0].startswith("#"):
                    self.kept[f[0]] = f[1] if len(f) > 1 else "kept"
            return
        self.not_measured.append(("kept.txt", "written by the update step; before it runs, kept modules are only predicted by localedits RED rows and stranded.md"))

    def strandedmods(self):
        t = self.need("stranded.md", "steps/triage.md item 3 lists stranded modules and add-on modules built before 10.21 there")
        if t is None:
            return
        for ln in t.splitlines():
            s = ln.strip()
            m = (re.match(r"^[-*]\s+`?([A-Za-z][A-Za-z0-9_]*)`?\b[:\s-]*(.*)$", s)
                 or re.match(r"^#{2,}\s+`?([A-Za-z][A-Za-z0-9_]*)`?\b[:\s-]*(.*)$", s)
                 or re.match(r"^\|\s*`?([A-Za-z][A-Za-z0-9_]*)`?\s*\|(.*)$", s))
            if m and m.group(1).lower() not in ("module", "modules", "stranded", "name"):
                self.stranded.setdefault(m.group(1), m.group(2).strip(" |"))

    def localedits(self):
        t = self.need("localedits.json", "steps/triage.md item 5: localedits.py --json")
        self.red, self.logic, self.files, self.renamed = {}, {}, {}, {}
        if t is None:
            return
        try:
            rep = json.loads(t)
        except ValueError:
            self.measured.remove("localedits.json")
            self.not_measured.append(("localedits.json", "not valid JSON"))
            return
        # BT-6: a module the Marketplace renamed or republished (playbooks/module-renames.tsv, matched by content id)
        try:
            import renamed_modules
            for h in renamed_modules.find([e for e in rep if isinstance(e, dict)] if isinstance(rep, list) else []):
                self.renamed[h["module"]] = h
        except (OSError, ImportError):
            self.not_measured.append(("module-renames.tsv", "playbooks/module-renames.tsv could not be read; renamed Marketplace modules are not detected"))
        for e in rep if isinstance(rep, list) else []:
            n = e.get("name", "?")
            red = [x for x in (e.get("domain") or []) if x.get("data")]
            if red:
                self.red[n] = "; ".join(f"{x.get('change')} {x.get('kind')} {x.get('name')}" for x in red[:3]) + (f" (+{len(red) - 3})" if len(red) > 3 else "")
            lg = e.get("logic") or []
            if lg:
                self.logic[n] = f"{len(lg)} logic document(s) added or deleted locally"
            fl = e.get("files") or []
            if fl:
                self.files[n] = fl
            if (e.get("domain") is None) and not e.get("files_error"):
                self.logic.setdefault(n, "package not readable: edits UNKNOWN (never read as none)")

    def release(self):
        t = self.need("release-impact.md", "steps/triage.md item 10")
        if t is None:
            # cold test WM1: the release-note check could not run (no brain version tables) and the plan still went to sign-off,
            # so nobody had read what Mendix 10 and 11 change. A check that did not run is a question, never a silent pass.
            why = (read(self.p("release-impact.out")) or "release-impact.md was not written").strip().splitlines()[0]
            self.add3("check", "Release notes", f"the release-note check did not run: {why}",
                      "run the check first: give the run the company brain (its version tables), then rerun triage | "
                      "go on without it: a named person reads the Mendix release notes for every version on the route before go-live | "
                      "pause the upgrade",
                      "run the check first: give the run the company brain (its version tables), then rerun triage", "S", "a change in the new Mendix versions is only found at the build or the test, or after go-live")
            return
        tot = opn = 0
        for head, rows in tables(t):
            if "handled" not in head:
                continue
            for r in rows:
                tot += 1
                if not col(head, r, "handled").strip():
                    opn += 1
        self.release_total, self.release_open = tot, opn
        # GM-18: "Not covered" rows are modules release_impact had no brain file for (UNKNOWN): their release notes were not read
        for head, rows in tables(t):
            if "module or source" not in head:
                continue
            for r in rows:
                mod = col(head, r, "module or source")
                # a non-empty handled cell (a person's entry, or release_impact's own "not relevant (auto)") closes the item
                if mod and mod != "Studio Pro" and not col(head, r, "handled").strip():
                    # the row is [#, module, UNKNOWN, why, handled] under a header whose 3rd cell reads "why" for the older rows
                    self.release_unread.setdefault(mod, (r[3] if len(r) > 4 else col(head, r, "why")).strip())

    def absent(self):
        """GM-12: a planned update whose package calls a module that is neither in the app nor in the plan is a decision
        ("needs module X") before the update, not 31 CE1613 at the build. absentmods.json is optional (a run from before the
        check has none); an update whose package could not be read is listed as not measured, never as clean."""
        t = read(self.p("absentmods.json"))
        if t is None:
            return
        try:
            d = json.loads(t)
            needs, unchecked = d.get("needs") or {}, d.get("unchecked") or []
        except (ValueError, AttributeError):
            self.not_measured.append(("absentmods.json", "not valid JSON; calls into modules the app lacks were not checked"))
            return
        self.measured.append("absentmods.json")
        for x, by in sorted(needs.items()):
            who = "; ".join(f"{p} {v.get('installed') or '?'} -> {v.get('plan')} calls it ({v.get('refs')} refs, e.g. "
                            + ", ".join(f"{doc} -> {tgt}" for doc, tgt in (v.get("examples") or [])[:2]) + ")" for p, v in sorted(by.items()))
            callers = ", ".join(sorted(by))
            self.add3("module", f"needs module {x}",
                      f"the target package of {callers} refers to {x}, which is not in the app and not on the plan: {who}",
                      f"install {x} from the Marketplace before the update (mxcli marketplace search {x}), add it to the plan | "
                      f"hold {callers} at its installed version | hand to a named person",
                      f"install {x} from the Marketplace before the update and add it to the plan",
                      "S", f"every reference to {x} is CE1613 at the build, and the update step cannot add a module")
        for u in unchecked:
            self.not_measured.append((f"absentmods.py {u.get('module')} {u.get('version')}", u.get("reason") or "package not read"))

    def owngone(self):
        """GF-39: crosscalls.py --own output (owngone.out). An own document that uses a page, microflow or Java action the plan version of a
        module no longer has is CE1613 after the update; one section-3 item per planned module, naming each target and the own document.
        Optional (an older run has none); a NOTE line (package not cached) is listed as not measured, never as clean."""
        t = read(self.p("owngone.out"))
        if t is None:
            return
        self.measured.append("owngone.out")
        cur, by, cnt = None, {}, {}
        for ln in t.splitlines():
            m = re.match(r"OWN (\S+) (\S*) -> (\S+): (\d+) target", ln)
            g = re.match(r"\s+GONE (.+?) (\S+) \(used by own (.+)\)", ln)
            n = re.match(r"NOTE (\S+) (\S*) -> (\S+): .*NOT checked", ln)
            if m:
                cur = (m.group(1), m.group(2), m.group(3)); by[cur] = []; cnt[cur] = int(m.group(4))
            elif g and cur:
                by[cur].append((g.group(1), g.group(2), g.group(3)))
            elif n:
                self.not_measured.append((f"crosscalls.py --own {n.group(1)} {n.group(3)}", "the plan version's package is not in the cache: own use of dropped targets not checked"))
        for (pm, inst, pv), gone in sorted(by.items()):
            total = max(cnt.get((pm, inst, pv), 0), len(gone))   # the OWN header line states the count; rows are only the examples
            ex = "; ".join(f"{k} {tgt} used by own {src}" for k, tgt, src in gone[:4]) + (f"; and {total - min(len(gone), 4)} more" if total > min(len(gone), 4) else "")
            self.add3("module", f"own documents use targets {pm} {pv} drops",
                      f"{pm} {inst or '?'} -> {pv}: {total} target(s) the app's own modules use are gone from the {pv} package: {ex}",
                      f"change the own documents to the replacement the {pm} release notes name before the update | hold {pm} at {inst or 'its installed version'} | hand to a named person",
                      f"change the own documents to the replacement the {pm} release notes name before the update, or hold {pm}",
                      "S", f"each is CE1613 at the build ({total} target(s)); mx check on the old model does not see it")

    def keptvend(self, only=None):
        """GM-15: a kept module's themesource uses a mixin, variable or file that a planned package no longer has (the theme compile
        fails after the update). keptvendor.json is optional (the pipeline writes it at triage for the app's own styling, GF-56, and again after the update step for kept modules once .stepupdate/kept.txt exists; an older run has none). One
        section-3 item per planned package with MISSING uses; a package whose target could not be read is listed as not measured,
        never as clean. GF-56: a MISSING use in the app's OWN styling (theme/, own themesource; `own` in the json) is measured at triage, before
        the sign-off, so it is its own item and IS in the plan hash (main takes it through only="own"); a kept module's use is not: the file
        gets those after the update step, like kept.txt."""
        t = read(self.p("keptvendor.json"))
        if t is None:
            return
        try:
            d = json.loads(t)
            missing, unchecked = d.get("missing") or [], d.get("not_checked") or {}
            by = {}
            for x in missing:
                by.setdefault((bool(x.get("own")), x["pkg"], x.get("version") or "?"), []).append(x)
            unchecked = {str(m): (v.get("why") or "package not read", v.get("uses") or []) for m, v in unchecked.items()}
        except (ValueError, AttributeError, KeyError, TypeError):
            self.not_measured.append(("keptvendor.json", "not valid JSON; kept themesource uses of planned packages were not checked"))
            return
        self.measured.append("keptvendor.json")
        self.kv_seen = True
        for (isown, pkg, ver), xs in sorted(by.items()):
            if only == "own" and not isown:
                continue
            who = "the app's own styling" if isown else "a kept themesource"
            what = "; ".join(f"{x.get('kind')} {x.get('name')} used in {x.get('where')} (module {x.get('module')})" for x in xs[:6]) \
                + (f" (+{len(xs) - 6} more)" if len(xs) > 6 else "")
            self.add3("theme", f"{'own' if isown else 'kept'} styling uses what {pkg} {ver} removes",
                      f"keptvendor.json: {len(xs)} use(s) in {who} that {pkg} {ver} no longer has: {what}",
                      f"fix the {'own' if isown else 'kept'} SCSS (use what {pkg} {ver} offers instead) | hold {pkg}: the package stays at its installed version | hand to a named person",
                      f"fix the {'own' if isown else 'kept'} SCSS (the build fails at the theme compile otherwise)",
                      "M", f"the theme compile fails at the build for every use listed ({len(xs)}), and the update step does not edit {'the app' + chr(39) + 's own styling' if isown else 'a kept module'}")
            self.items3[-1]["fixed"] = True
            if not isown:
                self.items3[-1]["own"] = True   # late (written after the sign-off); its options are fixed (see "fixed")
        for m, (why, uses) in sorted(unchecked.items()):
            self.not_measured.append((f"keptvendor.py {m}", f"{why}; {len(uses)} kept use(s) it defines are unverified"))

    def keptstyle(self):
        """MC-11: a kept module's themesource targets a platform widget selector (.widget-datagrid ...); after a widget major the
        markup changes and the kept SCSS can break the layout, which only a screenshot shows. keptstyle.json is optional (written once
        .stepupdate/kept.txt exists; an older run has none): a list of {module, file, line, selector, cls} rows, [] when clean. One
        section-3 item per kept module with hits. A visual risk, not a stop. Not in the plan hash (see main); keptvendor.json is only half in it: its own-styling rows are."""
        t = read(self.p("keptstyle.json"))
        if t is None:
            return
        try:
            rows = json.loads(t)
            by = {}
            for x in rows:
                by.setdefault(str(x["module"]), []).append(x)
            for xs in by.values():
                for x in xs:
                    x["file"], x["line"], x["selector"]
        except (ValueError, AttributeError, KeyError, TypeError):
            self.not_measured.append(("keptstyle.json", "not valid JSON; kept themesource platform widget selectors were not checked"))
            return
        self.measured.append("keptstyle.json")
        self.ks_seen = True
        for m, xs in sorted(by.items()):
            what = "; ".join(f"{str(x['selector']).rstrip(' ,{')} at {x['file']}:{x['line']}" for x in xs[:6]) + (f" (+{len(xs) - 6} more)" if len(xs) > 6 else "")
            self.add3("theme", f"kept module {m} styles platform widgets",
                      f"keptstyle.json: {len(xs)} platform widget selector(s) in the kept themesource of {m}: {what}",
                      "look at a page with each of these widgets after the update and restyle the kept SCSS if it broke | accept the risk | hand to a named person",
                      "look at a page with each widget after the update (the screens rung names this cause)",
                      "S", f"a widget major can change the markup these selectors target; the layout may break with no build error ({len(xs)} selector(s) in {m})")
            self.items3[-1]["own"] = True   # late (after the sign-off); fixed options: the evidence names themesource paths, which RA-6 (vendor theme edits) would claim
            self.items3[-1]["fixed"] = True

    def repairmap(self):
        t = read(os.path.join(TK, "steps", "repair.md")) or ""
        for m in re.finditer(r"^\| (\d+) \|([^\n]*)$", t, re.M):
            code = re.search(r"\bCE\d{4}\b", m.group(2))
            for rid in set(re.findall(r"\bR\d{1,2}\b", m.group(0))):
                self.repair_rows[rid] = (m.group(1), code.group(0) if code else "")

    def replacements(self):
        t = self.need("replacements.md", "steps/triage.md item 10: replacement_check.py --out")
        if t is None:
            return
        for head, rows in tables(t):
            if "id" not in head or "status" not in head:
                continue
            for r in rows:
                rid, st = col(head, r, "id"), col(head, r, "status")
                short = lambda x: (x if len(x) <= 70 else x[:67].rsplit(" ", 1)[0] + "...")
                if st not in ("HIT", "UNKNOWN"):
                    continue
                ev, pat, rep = col(head, r, "evidence"), col(head, r, "pattern"), col(head, r, "replacement")
                eff = (col(head, r, "effort") or "M")[:1].upper()
                eff = eff if eff in "SML" else "M"
                if rid in self.repair_rows and st == "HIT":
                    n, code = self.repair_rows[rid]
                    self.items2.append({"key": f"repair:{rid}", "text": f"predicted repair {rid} ({short(pat)}) -> repair row {n}"
                                        + (f" ({code})" if code else "")})
                    continue
                low = (pat + " " + ev + " " + rep).lower()
                kind = ("widget" if "widget" in low or ".mpk" in low else "Java" if re.search(r"\bjava\b|\bjar\b", low)
                        else "theme" if re.search(r"theme|scss", low) else "page" if re.search(r"\bpage|layout|template", low)
                        else "re-architecture" if eff == "L" else "module")
                self.add3(kind, f"{rid} {short(pat)}", f"replacements.md row {rid} {st}: {ev or 'no detector decided'}",
                          f"{rep} (replacements.tsv row {rid})" if rep and rep != "-" else "see replacements.tsv row " + rid,
                          f"follow replacements.tsv row {rid}: {rep}" if rep and rep != "-" else "hand to a named person",
                          eff, (col(head, r, "risk") or "see the row")[:80])
                # GM-20: the packages this hit names (widgets/<file>.mpk in its evidence), for the per-package merge
                self.items3[-1]["rpkgs"] = sorted(set(re.findall(r"widgets/([^\s;/]+\.mpk)\b", ev))) if st == "HIT" and kind == "widget" else []

    def dojo(self):
        t = self.need("dojo-react.md", "steps/triage.md item 10: dojo_report.py --out")
        if t is None:
            return
        # the move to React is part of every upgrade (where a path exists): plan work, not advice. Only a widget without
        # a React path is a decision (below)
        last = getattr(self.a, "target2", None) or self.a.target or "the target"
        # GF-25: below Mendix 12 the React client is optional (dojo_report.py says ADVISORY) and nothing in the pipeline swaps the widgets:
        # those lines are advice, listed apart, never work of this run
        mj = major(last)
        into = self.advisory if (mj is not None and mj < 12) else self.items2
        for head, rows in tables(t):
            if head[:2] == ["widget", "count"]:
                for r in rows:
                    if len(r) > 3 and r[1].isdigit():
                        into.append({"key": f"react:{r[0]}", "text": f"Dojo to React on the {last} rung: {r[1]} x {r[0]} -> {r[3].split(';')[0]}"})
        for head, rows in tables(t):
            if head[:3] != ["status", "package", "version"]:
                continue
            for r in rows:
                st, pkg = r[0], r[1]
                ver = r[2] if len(r) > 2 else ""
                if st in ("can't move", "not researched", "unreadable"):
                    self.add3("widget", (pkg if ver in ("", "?") else f"{pkg} {ver}"), f"dojo-react.md: {st}: {r[3] if len(r) > 3 else ''}",
                              "keep old package, accept the risk | swap to a successor (dojo-successors.tsv) | rebuild as pluggable / native | hand to a named person",
                              "rebuild as pluggable / native (no React path found; keep the old package only for this rung, Mendix 12 blocks it)", "L" if st == "can't move" else "M",
                              "does not run on the React client; Mendix 12 removes the Dojo client")
                    self.items3[-1]["dojopkg"] = pkg
                elif st in ("can move", "delete"):
                    into.append({"key": f"react:{pkg}", "text": f"Dojo to React on the {last} rung: widget package {pkg} ({st}: {r[4] if len(r) > 4 else ''})"})
                    if st == "can move" and re.search(r"htmlsnippet|snippetjs", pkg + " " + (r[3] if len(r) > 3 else ""), re.I):
                        # the successor depends on what each snippet holds (HTML only, a little script, DOM work): a decision per snippet
                        self.add3("widget", (pkg if ver in ("", "?") else f"{pkg} {ver}"),
                                  f"dojo-react.md: can move: {r[3] if len(r) > 3 else ''}; the successor depends on the content of each snippet",
                                  "keep on the Dojo client for now | HTML Element widget | JavaScript action + nanoflow + Events | pluggable widget | hand to a named person",
                                  "HTML Element widget for every snippet that holds HTML only; classify the rest (script, DOM work) per snippet", "M",
                                  "script in a snippet runs on the Dojo page DOM; Mendix 12 removes the Dojo client")

    def merge_packages(self):
        """GM-20: one item per widget package. A replacement HIT (crash or replace finding) and the dojo-report item name the
        same package by its file name (`widgets/<file>.mpk` in the evidence, `package` column of dojo-react.md). The stronger
        finding leads: the replacement advice comes first, "keep, accept the risk" (or the catalogue's "stay on 11") last, and the dojo line stays in the
        evidence as the supporting one. An identity that is not exact (a hit naming several packages, a package listed twice
        in the dojo report) is not merged; the dojo item says so."""
        dojo = {}
        for it in self.items3:
            if it.get("dojopkg"):
                dojo.setdefault(it["dojopkg"], []).append(it)
        merged, gone = {}, set()
        for rep in self.items3:
            pk = rep.get("rpkgs") or []
            hit = [x for x in pk if x in dojo]
            if not hit:
                continue
            if len(pk) != 1 or len(dojo[pk[0]]) != 1:
                for x in hit:
                    for d in dojo[x]:
                        d["evidence"] += (f"; not merged with replacements.md row {rep['name'].split()[0]}: its evidence names "
                                          f"{len(pk)} package(s) ({', '.join(pk)}), so the package identity is ambiguous")
                continue
            merged.setdefault(id(dojo[pk[0]][0]), (dojo[pk[0]][0], []))[1].append(rep)
            gone.add(id(rep))
        for d, reps in merged.values():
            # the dojo item's catalogue link (its RA tag and recommendation) survives as a supporting line; the replacement
            # findings lead. Every keep / "stay on" option, whichever side it came from, goes after the last other option.
            tag = re.search(r"\[(RA-\d+)[^\]]*\]", d["rec"])
            also = (f"; also {tag.group(1)}: {re.sub(chr(32) + r'*\[RA-\d+[^]]*\]', '', d['rec'])} [playbooks/rearchitecture.md]") if tag else ""
            allopts = [o for r in reps for o in r["options"].split(" | ")] + d["options"].split(" | ")
            opts = []
            for o in allopts:
                if o not in opts:
                    opts.append(o)
            isk = lambda o: o.startswith(("keep", "stay on"))
            d["options"] = " | ".join([o for o in opts if not isk(o)] + [o for o in opts if isk(o)])
            d["evidence"] = ("; ".join(dict.fromkeys(r["evidence"] for r in reps)) + "; supporting, weaker: " + d["evidence"] + also)
            d["rec"] = "; and ".join(r["rec"] for r in reps)
            d["effort"] = max([d["effort"]] + [r["effort"] for r in reps], key="SML".index)
            d["risk"] = "; ".join(dict.fromkeys(r["risk"] for r in reps)) + "; " + d["risk"]
            d["merged_keys"] = [f"{d['kind']}:{d['name']}"] + [f"{r['kind']}:{r['name']}" for r in reps]
        self.items3 = [i for i in self.items3 if id(i) not in gone]

    def sizes_and_actions(self):
        t = read(self.p("actions.json"))
        if t is None:
            self.not_measured.append(("actions.json", "action_inventory.py; the action count of the app is unknown"))
        else:
            try:
                self.actions = json.loads(t)["summary"]["actions"]
                self.measured.append("actions.json")
                sc = read(self.p("journey-scope.json"))
                if sc is not None:
                    try:
                        d = json.loads(sc)
                        self.scope = {k: d[k] for k in ("line", "testability_line", "counts")}
                        self.measured.append("journey-scope.json")
                    except (ValueError, KeyError, TypeError):
                        self.not_measured.append(("journey-scope.json", "not a journey_scope.py file"))
            except (ValueError, KeyError, TypeError):
                self.not_measured.append(("actions.json", "not an action_inventory.py file"))
        orig = self.a.original or self.p("original.mpr")
        if not os.path.exists(orig):
            self.not_measured.append(("original.mpr", "modules, pages and microflows cannot be counted"))
            return
        try:
            import mprmodel
            m = mprmodel.Model.load(orig)
            docs = list(m.docs.items())
            self.sizes = {"modules": len({qn.split(".")[0] for qn, _ in docs}),
                          "pages": sum(1 for _, d in docs if d.type == "Forms$Page"),
                          "microflows": sum(1 for _, d in docs if d.type == "Microflows$Microflow")}
            self.filedocs = mprmodel.file_document_entities(m)
            self.measured.append("original.mpr")
        except Exception as ex:  # noqa: BLE001  an unreadable model is not an empty app
            self.not_measured.append(("original.mpr", f"cannot be read ({ex}); modules, pages and microflows are not counted"))

    def apimock(self):
        t = read(self.p("apimock-inventory.json"))
        if t is None:
            self.not_measured.append(("apimock-inventory.json", "apimock.py inventory; the external systems the app consumes are unknown"))
            return
        try:
            eps = json.loads(t)["endpoints"]
            self.systems = sorted({(e.get("system") or "unclassified") for e in eps})
            self.nendpoints = len(eps)
            self.api_mocked = sum(1 for e in eps if e.get("status") == "MOCKED")
            self.api_unknown = [e for e in eps if e.get("status") == "UNKNOWN"]
            self.api_excluded = sum(1 for e in eps if e.get("status") == "EXCLUDED")
            self.measured.append("apimock-inventory.json")
        except (ValueError, KeyError, TypeError):
            self.not_measured.append(("apimock-inventory.json", "not an apimock.py inventory file"))

    def filedoc_item(self):
        """GM-42: Mendix 11.0 refuses to start while a pre-5.12 file document is still present in the data (Mendix 10.24
        logs a warning). The model shows whether FileDocument entities exist; only the environment's database shows whether old files
        are in it, so the proposal asks which databases the app runs on and raises a BLOCKER until each was checked."""
        if not self.filedocs:
            return
        tm = [x for x in (major(self.tgt), major(self.tgt2)) if x]
        if (major(self.src) or 0) >= 11 or (tm and max(tm) < 11):   # an unknown version still asks: a missing version is no "no"
            return
        ents = ", ".join(self.filedocs[:5]) + (f" and {len(self.filedocs) - 5} more" if len(self.filedocs) > 5 else "")
        self.add3("data", "BLOCKER: pre-5.12 file documents in each environment's database",
                  f"the model has {len(self.filedocs)} entities that hold files (FileDocument specializations: {ents}). Mendix 11.0 refuses to "
                  "start when a file document from before Mendix 5.12 is still present in the data; Mendix 10.24 logs a warning "
                  "(release notes 10.24.0 and 11.0.0). QUESTION: which databases do the app's environments (test, acceptance, "
                  "production) run on, and who can read them? WHAT TO LOOK FOR: file document rows of those entities whose file is "
                  "still stored the pre-5.12 way; on 10.24 or later the runtime writes a warning at start when any exist, so a copy "
                  "of each environment's database started on 10.24 shows it in the log. A read-only count in Postgres syntax that "
                  "a GF field run checked on a copy of a real database (GF-49): select count(*) from \"system$filedocument\" where "
                  "__uuid__ is null; it counts the file document rows with no uuid (it does not filter hascontents), the rows 11 refuses, and a copy with a uuid set on those rows got "
                  "past the check. Run it on each environment's database; a count above 0 is a go-live item for that environment",
                  "the app's data was first created on Mendix 5.12 or later: no such file can exist; the convert goes ahead | "
                  "I checked each environment's database: none holds pre-5.12 file documents; the convert goes ahead | "
                  "some do: start on 10.x until the app team has moved the old file documents as the 11.0 release note describes, then convert | "
                  "I cannot read an environment's database: hand to a named person; the convert waits for their answer | pause the upgrade",
                  "I cannot read an environment's database: hand to a named person; the convert waits for their answer",
                  "M", "the app does not start on Mendix 11 in an environment whose database still holds an old file document")

    def build(self):
        self.versions(); self.repairmap(); self.plans(); self.keptmods(); self.strandedmods(); self.localedits()
        self.release(); self.absent(); self.owngone(); self.keptvend(); self.keptstyle(); self.replacements(); self.dojo(); self.sizes_and_actions(); self.apimock()
        for tool, why in NOT_BEFORE_CONVERT:
            self.not_measured.append((tool, why))
        # modules that are decisions, never "done by the toolkit"
        held = {}
        for m, h in self.renamed.items():
            held[m] = (f"{h['kind']} on the Marketplace: content {h['cid']} is now '{h['new']}' (installed {m} {h['version']}); "
                       f"no version update of {m} is planned. {h['route']}")
        for m, why in self.kept.items():
            held[m] = f"the update step did not update it: {why}"
        for m, why in self.red.items():
            held.setdefault(m, f"RED local edit (data-bearing): {why}")
        for m, why in self.logic.items():
            held.setdefault(m, f"local logic edits: {why}")
        for m, why in self.stranded.items():
            held.setdefault(m, f"stranded (no version fits the target): {why or 'see stranded.md'}")
        for m, rows in self.files.items():
            kinds = sorted({x.get("kind", "?") for x in rows})
            if "java" in kinds:
                held.setdefault(m, f"Java user code edited locally ({len(rows)} FILES-EDITED rows)")
        for m, why in sorted(held.items()):
            kind = "module"
            if m in self.files and any(x.get("kind") == "java" for x in self.files[m]) and m not in self.kept and m not in self.red:
                kind = "Java"
            stranded = m in self.stranded
            if m in self.renamed:
                self.add3("renamed module", m, held[m] + f" ({self.renamed[m]['row']}, playbooks/module-renames.tsv)",
                          "install the new module and move the references | keep the installed module as is and test it at the gate | hand to a named person",
                          "install the new module" if self.renamed[m]["kind"] == "RENAMED" else "keep the installed module, test it at the gate; the owner decides on the new listing",
                          "M", "references and data of the old module are moved by hand" if self.renamed[m]["kind"] == "RENAMED" else "the installed version may not run on the target")
                continue
            rec = ("hand to a named person (no version fits; port, replace or remove)" if stranded else
                   f"{UPDATE_CARRY}; a real logic edit is held until it is moved to {m}_Ext" if kind == "module" else "keep old jar, pin")
            if kind == "module" and not stranded:
                jm = getattr(self, "jumps", {}).get(m)
                on_plan = any(x[0] == m for x in self.plan)
                newest = False
                if m in self.current or (jm and jm[0] == jm[1]) or any(x[0] == m and x[1] == x[2] for x in self.plan):
                    # GF-23: the installed version is the newest one; "update to the latest version" has nothing to update to
                    newest = True
                    rec = ("keep old version for now (the installed version is already the newest, so there is nothing to update to; "
                           "it may be deprecated: check its Marketplace listing) or replace with the Marketplace equivalent")
                if not on_plan and not newest and any(n in self.measured for n in ("plan-pre.txt", "plan.txt")):
                    # GF-24: a module on neither plan file is left out of the update on purpose or by mistake; the recommendation cannot run
                    rec += "; not on the plan: the recommendation needs a plan line"
            # GF-30: a Java file of the package deleted locally holds the update (the update step refuses to carry edits over it);
            # the signed answer would otherwise turn into "kept" with no new question. Show the deletion and offer the way out.
            gone = [x.get("path", "?") for x in self.files.get(m, []) if x.get("kind") == "java" and x.get("change") == "REMOVED"]
            back = (f"accept the package's Java back ({len(gone)} deleted file(s) return on the update, then update and carry the other edits over)"
                    if gone else "")
            evid = why + " (" + ("stranded.md" if stranded else "localedits.json / kept.txt") + ")"
            if gone:
                evid += ("; Java deleted locally: " + ", ".join(os.path.basename(g) for g in gone[:4]) + (f" (+{len(gone) - 4})" if len(gone) > 4 else "")
                         + "; an update that carries edits over cannot keep a deleted Java file, so the module is held unless the package's Java comes back")
            self.add3(kind, m, evid,
                      (f"{UPDATE_CARRY} | " + (back + " | " if back else "") + f"update, move the edits to {m}_Ext by hand | keep old version for now (a reason and an end date) | "
                       "replace with the Marketplace equivalent (replacements.tsv row) | hand to a named person")
                      if kind == "module" else ("keep old jar, pin | " + (back + " | " if back else "") + "port to the new API | replace with a Marketplace module or a microflow | hand to a named person"),
                      rec,
                      "L" if stranded else "M", "data loss if a RED edit is replaced" if m in self.red else "behaviour of local edits is lost on update")
        for m, rows in sorted(self.files.items()):
            if any(x.get("kind") == "theme" for x in rows):
                self.add3("theme", f"{m} themesource edits", f"localedits.json FILES-EDITED rows of {m} in themesource/",
                          "keep module styling and replay | adopt the package styling | hand to a named person",
                          "replay the edits after the update (UI-only edits are replayed by the pipeline)", "S", "look only")
        for mod, fr, to, when in self.plan:
            if mod in held:
                continue
            self.items2.append({"key": f"module:{mod}", "text": f"module update {mod} {fr} -> {to} ({when})"})
        for mod, why in self.release_unread.items():
            if mod in held:
                continue
            rng = [(fr, to) for m, fr, to, _w in self.plan if m == mod]
            vr = f"{rng[0][0]} -> {rng[-1][1]}" if rng else "version range not known"
            self.add3("check", f"{mod}: release notes not read",
                      f"release-impact.md lists {mod} ({vr}) under Not covered: UNKNOWN, {why or 'no reason given'}; no release-note row was checked",
                      "read the release notes of every version in the range, record what you found in the handled cell of its Not covered row | "
                      "add a brain file for the module, then rerun triage | hand to a named person",
                      f"read the release notes of {mod} for {vr}, or add a brain file for it", "S",
                      "a breaking change in the module is only found at the build or the test")
        self.items2.sort(key=lambda x: x["key"])
        self.advisory.sort(key=lambda x: x["key"])
        self.items3.sort(key=lambda x: (x["kind"], x["name"]))
        # re-architecture catalogue: the first RA entry whose match fits kind + name + evidence prefills options, recommendation, effort
        ra = load_ra(getattr(self.a, "ra_file", None))
        for it in self.items3:
            for e in [] if it.get("fixed") else ra:
                if e["rx"].search(f"{it['kind']} {it['name']} {it['evidence']}"):
                    it["options"], it["effort"] = e["options"], e["effort"]
                    it["rec"] = f"{e['rec']} [{e['id']}, {e['status']}, playbooks/rearchitecture.md]"
                    break
            else:
                # a none-found widget that no catalogue entry claimed keeps its own options; they cite RA-22 (custom-widget route) only when the catalogue was read
                if ra and it.get("dojopkg") and not it.get("fixed"):
                    it["options"] = it["options"].replace("rebuild as pluggable / native |", "rebuild as pluggable / native [RA-22] |")
        self.merge_packages()   # after the catalogue prefill: the merged item takes each finding's own options and recommendation
        self.filedoc_item()
        # section 4: a person anyway
        if self.release_open:
            self.items4.append({"key": "release-rows", "text": "release-impact rows a person must judge",
                                "detail": f"{self.release_open} of {self.release_total} rows have no 'handled' entry yet (release-impact.md)"})
        self.items4.append({"key": "key-user", "text": "key-user confirmation of the user processes (status: confirmed is set only by a person)",
                            "detail": "templates/process-interview.md; the number of processes is unknown at this point"})
        self.items4.append({"key": "visual", "text": "visual sign-off of the changed screens (shotdiff REVIEW pairs)",
                            "detail": "the number of changed screens is known only after the gate"})
        if self.systems:
            self.items4.append({"key": "apis:" + ",".join(self.systems), "text": "real test systems for external APIs: " + ", ".join(self.systems),
                                "detail": f"{self.nendpoints} endpoints in apimock-inventory.json; the stand-in gives at best PASS (on stand-in APIs)"})
        elif self.systems is not None:
            self.items4.append({"key": "apis:none", "text": "external systems: none found by apimock.py inventory", "detail": ""})
        self.items4.append({"key": "go-live", "text": "go-live actions (deployment, data migration window, rollback decision)",
                            "detail": "outside the toolkit"})


def ids_for(items, work):
    """Stable P-n ids: first appearance order, remembered in state/proposal-ids.json."""
    path = os.path.join(work, "state", "proposal-ids.json")
    try:
        ids = json.load(open(path))
    except (OSError, ValueError):
        ids = {}
    for it in items:
        k = f"{it['kind']}:{it['name']}"
        if k not in ids:
            ids[k] = max(ids.values(), default=0) + 1
        it["id"] = f"P-{ids[k]}"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    json.dump(ids, open(path, "w"), indent=1, sort_keys=True)


def plainify(text, fallback):
    """The text when it is plain words for a person (steps.plain), else without its parentheses, else the fallback."""
    s = " ".join(str(text).split())
    for c in (s, re.sub(r"\s*\([^)]*\)", "", s).strip(" ;,"), re.sub(r"\s*\[[^\]]*\]", "", s).strip(" ;,")):
        if c and steps.plain(c):
            return c
    return fallback


def major(v):
    """The major version number of a Mendix version string, None when it has none."""
    m = re.match(r"\s*(\d+)\.", str(v or ""))
    return int(m.group(1)) if m else None


def edited_modules(work):
    """Modules whose comparison with their Marketplace package found the app's own edits, or could not be made (localedits.json)."""
    try:
        with open(os.path.join(work, "localedits.json"), encoding="utf-8") as f:
            le = json.load(f)
    except (OSError, ValueError):
        return set()
    return {m["name"] for m in le if isinstance(m, dict) and m.get("name") and
            (m.get("domain_error") or any(m.get(k) for k in ("domain", "ui", "logic", "files")))}


def write_steps(F, work):
    """Open (or find) one step per triage item and set found and proposed (STEP-RECORDS-PLAN.md section 3). A rerun with the
    same input adds no event; the same topic and title is the same step. Returns {step id: key} in item order.
    Routine module updates (section 2) are ONE step per topic row, approved with the plan sign-off. Section 3 items keep
    their P-n as the alias field of the step; PROPOSAL.md itself keeps showing [P-n]. Plain-language texts are fixed
    template sentences (the item's own words only when they are plain)."""
    out = {}
    groups = [("modules", "Routine module updates", "module", ("module update in the plan that the toolkit does on its own", "module updates in the plan that the toolkit does on its own"),
               "Update these modules to the versions that fit the new Mendix version."),
              ("repairs", "Predicted repairs", "repair", ("repair that the toolkit expects to make", "repairs that the toolkit expects to make"),
               "Make these repairs during the upgrade, as the repair table describes."),
              ("react", "Dojo to React client", "react", ("move to the React client that the toolkit makes", "moves to the React client that the toolkit makes"),
               "Move the app to the React client on the last rung: every legacy widget to its React successor, then test (playbooks/dojo-to-react.md).")]
    carry = edited_modules(work)
    for topic, title, key, what, prop in groups:
        its = [x for x in F.items2 if x["key"].startswith(key + ":")]
        if topic == "modules":
            # a module with the app's own edits is no routine swap (the owner, 2026-11-17): it goes ahead and the edits are carried
            # over, but the screens that use them are checked on both apps after the build; only a difference asks a person
            ed = [x for x in its if x["key"].split(":", 1)[1] in carry]
            its = [x for x in its if x not in ed]
            if ed:
                names = [x["key"].split(":", 1)[1] for x in ed]
                sid = steps.ensure(work, "module-edits", "Module updates that carry the app's edits", {
                    "found_say": f"{len(ed)} module {'update holds' if len(ed) == 1 else 'updates hold'} the app's own edits ({', '.join(names)}).",
                    "stage": "triage", "evidence": [x["text"] for x in ed],
                    "proposed_say": "Update these modules and carry every edit over to the new version. After the build, compare the screens "
                                    "that use them on the old and the new app. A difference becomes a decision with its case.",
                    "why": "Not routine: the update replaces the whole module, so each edit has to come back. It goes ahead with the plan "
                           "(in auto mode at once) and asks a person only when a screen differs.", "closes_by": ["build", "journeys"]})
                out[sid] = "2:module-edits"
        if not its:
            continue
        sid = steps.ensure(work, topic, title, {
            "found_say": f"The plan holds {len(its)} {what[len(its) != 1]}.", "stage": "triage", "evidence": [x["text"] for x in its],
            "proposed_say": prop, "why": "Routine work with a known result. It is approved with the sign-off of the plan."})
        out[sid] = f"2:{topic}"
    if major(F.src) and major(F.tgt) and major(F.src) != major(F.tgt):
        # the plan converts the app: the convert commit and the "after the convert" updates belong to this step (steps.py trailer --kind convert)
        sid = steps.ensure(work, "convert", "Convert the app to the new Mendix version", {
            "found_say": f"The app is on Mendix {major(F.src)} and the plan moves it to Mendix {major(F.tgt)}, which needs the Mendix conversion.",
            "stage": "triage", "evidence": [f"{F.src} -> {F.tgt}"],
            "proposed_say": "Run the Mendix conversion once, then fix what it leaves open.",
            "why": "Routine work with a known result. It is approved with the sign-off of the plan.", "closes_by": ["build"]})
        out[sid] = "2:convert"
    for it in F.items3:
        opts = [o.strip() for o in it["options"].split(" | ") if o.strip()]
        opts = [plainify(o, "see the proposal for this option") for o in opts]
        rec = re.sub(r"\s*\[RA-\d+[^\]]*\]", "", it["rec"])
        pick = next((i for i, o in enumerate(opts) if o.split(" (")[0].lower() in rec.lower()), None)
        name = plainify(it["name"], "")
        sid = steps.ensure(work, f"{it['kind']}:{it['name']}", steps.item_title(it["kind"], it["name"]), {
            "alias": it["id"],
            "found_say": f"A {it['kind']}{(' (' + name + ')') if name else ''} needs a decision before the upgrade starts.",
            "stage": "triage", "evidence": [it["evidence"]],
            "proposed_say": "The toolkit recommends: " + plainify(rec, "the first option in the proposal") + ".",
            "why": f"Effort {it['effort']}. Risk: " + plainify(it["risk"], "see the proposal") + ".",
            "options": opts, "recommend": pick})
        out[sid] = f"3:{it['id']}"
    for it in F.items4:
        sid = steps.ensure(work, f"person:{it['key']}", it["text"], {
            "found_say": plainify(it["text"], "A person has to do something that the toolkit cannot do.") .rstrip(".") + ".",
            "stage": "triage", "evidence": [it["detail"]] if it["detail"] else None,
            "proposed_say": "A person does this. The toolkit lists it so it is not forgotten.",
            "why": "The toolkit has no way to do this on its own."})
        out[sid] = f"4:{it['key']}"
    steps.withdraw(work, set(out), "No longer in the plan: a rerun of the proposal dropped this item.")
    return out


def approve_steps(work, ids, state, signer, source, answers=None):
    """Write the approval of every step that has none yet (state assumed: unattended run) or is not answered on its own
    (state approved: the sign-off). A step a person approved or rejected on its own keeps that answer. A section-3 item
    with a hand-written, non-ASSUMED P-n line in DECISIONS.md is approved by the name on that line."""
    n = 0
    for sid, key in ids.items():
        cur = steps.approval_of(work, sid)
        have = cur["state"] if cur else None
        if state == "assumed" and have:
            continue
        if state == "approved" and have in ("approved", "rejected"):
            continue
        by, src = signer, source
        d = (answers or {}).get(key[2:]) if key.startswith("3:") else None
        if state == "approved" and by_hand(d):
            by, src = d[4], "decisions"
        extra = {"needs": "a person signs the proposal or answers this item"} if state == "assumed" else {}
        steps.set_approval(work, sid, state, by, src, **extra)
        n += 1
    return n


def by_hand(d):
    """A DECISIONS.md line a real person answered: a status of CONFIRMED or APPROVED (any case; REJECTED, ASSUMED, `CONFIRMED?` or empty
    never approve) and a signer that is a name, not empty, `-`, `agent` or `toolkit` (the toolkit's own lines and an unattended run's
    ASSUMED line never approve in a name)."""
    return bool(d) and len(d) > 5 and d[5].strip().upper() in ("CONFIRMED", "APPROVED") \
        and d[4].strip().lower() not in ("", "-", "agent", "toolkit")


def deciding_line(lines):
    """The line that decides a late item (one with an `appeared after sign-off` line): the last by-hand line after the last late line,
    or None. A later junk line (agent, ASSUMED, short) neither answers it nor takes the answer away. Items with no late line: the
    last line, as decisions() has it (None when there is none)."""
    late = [n for n, d in enumerate(lines) if len(d) > 3 and d[3].startswith("appeared after sign-off")]
    if not late:
        return lines[-1] if lines else None
    hand = [d for d in lines[late[-1] + 1:] if by_hand(d)]
    return hand[-1] if hand else None


def decisions_all(work):
    """P-n -> every line's fields in file order (decisions() keeps only the last)."""
    out = {}
    for ln in lines_of(os.path.join(work, "DECISIONS.md")) or []:
        m = re.match(r"^(P-\d+)\s*\|(.*)$", ln)
        if m:
            out.setdefault(m.group(1), []).append([x.strip() for x in m.group(2).split("|")])
    return out


def decisions(work):
    """P-n -> fields of DECISIONS.md. A line whose id carries the `~stale-merged` marker (reanswer()) does not match."""
    out = {}
    for ln in lines_of(os.path.join(work, "DECISIONS.md")) or []:
        m = re.match(r"^(P-\d+)\s*\|(.*)$", ln)
        if m:
            f = [x.strip() for x in m.group(2).split("|")]
            out[m.group(1)] = f
    return out


def reanswer(items, work):
    """GM-20: a merged item has a new recommendation order, so an answer given to the dojo item or to one of the absorbed
    replacement items before the merge is not carried over. Each such answer line in DECISIONS.md is rewritten in place to
    `P-n~stale-merged | <rest>` (every reader's `^(P-\\d+)\\s*\\|` then skips it; nothing is deleted) and the item's evidence names
    all of them. The file is the only state: an id that already has a stale-merged line is never marked again, so an answer
    written after the merge (a plain P-n line) counts, and a rerun finds the same note."""
    try:
        ids = json.load(open(os.path.join(work, "state", "proposal-ids.json")))
    except (OSError, ValueError):
        ids = {}
    dpath = os.path.join(work, "DECISIONS.md")
    for it in items:
        keys = it.get("merged_keys")
        if not keys:
            continue
        frm = [f"P-{ids[k]}" for k in keys if k in ids]
        stale = lambda: {m.group(1): [x.strip() for x in m.group(2).split("|")]
                         for m in (re.match(r"^(P-\d+)~stale-merged\s*\|(.*)$", ln) for ln in lines_of(dpath) or []) if m}
        have = stale()
        live = decisions(work)
        for pid in frm:
            if pid in live and pid not in have:
                mark_stale(dpath, pid)
        have = stale()
        olds = [(pid, have[pid]) for pid in frm if pid in have]
        if olds:
            txt = "; ".join(f"{pid}: '{f[2] if len(f) > 2 else '?'}'" for pid, f in olds)
            it["evidence"] += f"; re-answer: merged from {'/'.join(frm)}; earlier answer {txt} was given to the unmerged item (kept in DECISIONS.md as ~stale-merged)"


def mark_stale(path, pid):
    """Rewrite every `pid | ...` line of DECISIONS.md to `pid~stale-merged | ...` (decisions() is last-wins, so marking only the
    last one would revive an earlier line). Every other byte stays: line endings are kept (newline=""). The read-then-replace
    window can lose a line that write_decisions appends meanwhile; the pipeline runs one proposal.py at a time."""
    with open(path, encoding="utf-8", newline="") as f:
        text = f.read()
    lines = text.split("\n")
    for n, ln in enumerate(lines):
        lines[n] = re.sub(rf"^{re.escape(pid)}(\s*\|)", rf"{pid}~stale-merged\1", ln, count=1)
    with open(path + ".tmp", "w", encoding="utf-8", newline="") as f:
        f.write("\n".join(lines))
    os.replace(path + ".tmp", path)


def journeys_estimate(F):
    """GF-50: the run time of the journeys, said before anyone starts them: count x seconds per journey. The seconds are the
    measured pace of an earlier run in this work folder (state/journeys-pace.tsv) when there is one, else 80 (the field run's)."""
    n, what = None, ""
    import glob
    gen = glob.glob(os.path.join(F.W, "journeys", "journeys", "*", "*.journey.json"))   # run_journeys.py's set (gen_dir = <work>/journeys)
    if gen:
        n, what = len(gen), "generated journeys"
    elif F.scope and isinstance(F.scope.get("counts"), dict):
        n = sum(v for k, v in F.scope["counts"].items() if k in ("reachable-with-path", "reachable-no-path-yet"))
        what = "reachable actions (journeys are not generated yet; one journey per action is the plan)"
    elif F.actions is not None:
        n, what = F.actions, "actions (journeys are not generated yet, scope not measured; one journey per action is the plan)"
    if n is None:
        return "estimate: not measured (no actions.json): the journey count and so the run time are unknown"
    sec, how = 80, "default 80 s each, no earlier run measured"
    try:
        import journeys_progress
        m = journeys_progress.pace_of(os.path.join(F.W, "state", "journeys-pace.tsv"))
        if m:
            sec, how = m, "measured on an earlier run"
    except Exception:
        pass
    mins = n * sec / 60
    t = f"{mins / 60:.1f} h" if mins >= 120 else f"{mins:.0f} min"
    return (f"estimate: {n} {what} x {sec:.0f} s each ({how}) = about {t} per app; "
            f"cap it with run_journeys.py --max N or --budget-min M (impact-picked first, then always-on, then the rest; the rest is listed deferred)")


def testing_plan(F):
    """The testing plan: what is tested and how, what cannot be tested in the sandbox, how each gap is closed. From the
    apimock inventory, the action inventory and the app shape only; a missing input is said, never guessed."""
    sz = F.sizes
    L = ["", "## Testing plan", "",
         "What the gate tests, what it cannot test in a sandbox, and how each gap is closed. Numbers come from the inputs named in section 5.", "",
         "### What is tested and how", ""]
    L.append("- build: mx check and mxbuild of the converted app, errors listed per code" +
             (f" ({sz['modules']} modules, {sz['pages']} pages, {sz['microflows']} microflows)" if sz else " (app size not measured)"))
    L.append("- data: the old and the new app each start on a copy of the same database; every table is compared row by row (a row that differs is FAIL until accepted with a written reason)")
    L.append("- journeys: " + (f"one browser journey per action ({F.actions} actions in the inventory)" if F.actions is not None else "one browser journey per action (action count not measured)") +
             ", per role, run on the old app and the new app; a difference is a regression")
    if F.scope:   # journey_scope.py: only what is used and reachable counts; the rest is listed, never INVALID
        L.append("  - " + F.scope["line"])
        L.append("  - " + F.scope["testability_line"] + "; each of these stays INVALID in the gate until it has a path")
    L.append("  - " + journeys_estimate(F))
    if F.nendpoints is not None:
        unk = len(F.api_unknown)
        L.append(f"- external calls on a stand-in: {F.nendpoints} endpoints and constants found, {F.api_mocked} can be answered by the stand-in (apimock.py), {unk} are UNKNOWN"
                 + (f", {F.api_excluded} excluded" if F.api_excluded else "") + "; the apis rung checks that the stand-in was asked what the model says it should be asked")
    else:
        L.append("- external calls: not measured (no apimock-inventory.json)")
    L += ["", "### What cannot be tested in the sandbox", ""]
    if F.nendpoints is not None:
        L.append(f"- {len(F.api_unknown)} of {F.nendpoints} external endpoints are UNKNOWN: no stand-in route exists, so a journey that needs one is INVALID, not PASS" +
                 (" (examples: " + ", ".join(sorted({e.get('doc') or e.get('id') for e in F.api_unknown})[:5]) + ")" if F.api_unknown else ""))
    L.append("- the real behaviour of an external system (answers, limits, errors): a stand-in only returns shaped data, so a pass on it is reported as PASS (on stand-in APIs), never plain PASS")
    L.append("- single sign-on and any login through an identity provider: the sandbox uses local smoke users")
    L.append("- data the sandbox database does not hold (an action that needs rows of a kind that does not exist yet): the heal step seeds identical rows in both databases where it can, the rest stays INVALID")
    L += ["", "### How each gap is closed", ""]
    L.append("- classify every UNKNOWN endpoint (static, data-driven or add-on) in apimock-classify.txt; owner: the person who knows the integration")
    L.append("- seed the data that data-driven endpoints need, in the old and the new database alike; owner: the app owner")
    L.append("- run the apis rung against a real test system before go-live and compare with the stand-in run; owner: a named person on the customer side")
    L.append("- go-live decision on every INVALID journey that remains: accept in writing or test by hand; owner: a named person")
    return L


def render(F, hashval, changed_block, signoff_text):
    a = F.a
    ans = decisions(F.W)
    n2, n3, n4 = len(F.items2), len(F.items3), len(F.items4)
    sz = F.sizes
    size = (f"{sz['modules']} modules, {sz['pages']} pages, {sz['microflows']} microflows" if sz else "modules, pages, microflows not measured")
    size += f", {F.actions} actions" if F.actions is not None else ", actions not measured"
    rungs = f"rung 1 {F.src} -> {F.tgt}" + (f", rung 2 {F.tgt} -> {F.tgt2}" if F.tgt2 else "")
    L = [f"# Upgrade proposal: {F.src} -> {F.tgt}" + (f" -> {F.tgt2}" if F.tgt2 else ""), "",
         f"<!-- proposal inputs-hash: {hashval} -->",
         *([f"<!-- proposal items: {base64.b64encode(json.dumps(sorted(set(F.ident))).encode()).decode()} -->"] if getattr(F, "ident", None) else []), "",
         "Written by bin/proposal.py from the triage outputs. Nothing in the app model changes before section 6 is signed. "
         "Every line starting with `- ` is an item; sub-lines are evidence.", ""]
    if changed_block:
        L += changed_block + [""]
    L += ["## 1. Summary", "",
          f"- From {F.src} to {F.tgt}" + (f" and {F.tgt2}" if F.tgt2 else "") + f" ({rungs}). App size: {size}.",
          f"- {n2} items the toolkit expects to handle, {n3} need your decision, {n4} need a person anyway.", "",
          "## 2. Done by the toolkit", "",
          "Module updates and predicted repairs only. A kept module, a stranded module, a RED local edit and a widget with no "
          "successor are never here; they are in section 3.", ""]
    L += [f"- {it['text']}" for it in F.items2] or ["- none: no module update and no predicted repair in the inputs read"]
    if F.advisory:
        L += ["", "Advisory, not in this run (the target needs no React client; these are lines of advice and are not items to sign):", ""]
        L += [f"  - {it['text']}" for it in F.advisory]
    L += ["", "## 3. Needs your decision before we start", "",
          "Answer each item in chat (steps/decide.md options); the toolkit records it in DECISIONS.md as the P-n line. "
          "Signing section 6 without an answer accepts the recommendation of that item.", ""]
    for it in F.items3:
        L.append(f"- [{it['id']}] {it['kind']}: {it['name']}")
        L.append(f"  - evidence: {it['evidence']}")
        L.append(f"  - options: {it['options']}")
        L.append(f"  - recommendation: {it['rec']}; effort {it['effort']}; risk: {it['risk']}")
        d = ans.get(it["id"])
        L.append(f"  - answer: {d[2] if len(d) > 2 else '?'} ({d[5] if len(d) > 5 else '?'})" if d else "  - answer: not yet")
    if not F.items3:
        L.append("- none: no kept, stranded, RED, Java, theme, widget or replacement item in the inputs read")
    L += ["", "## 4. Needs a person anyway", ""]
    for it in F.items4:
        L.append(f"- {it['text']}")
        if it["detail"]:
            L.append(f"  - {it['detail']}")
    # section 5
    cnt = {}
    for it in F.items3:
        cnt[it["effort"]] = cnt.get(it["effort"], 0) + 1
    lo = sum(HOURS[e][0] * n for e, n in cnt.items())
    hi = sum(HOURS[e][1] * n for e, n in cnt.items())
    kinds = {}
    for it in F.items3:
        kinds[it["kind"]] = kinds.get(it["kind"], 0) + 1
    L += ["", "## 5. Human effort", "",
          "- decision touchpoints: " + (", ".join(f"{k} {n}" for k, n in sorted(kinds.items())) or "0"),
          f"- person-anyway touchpoints: {n4}" + (f", release rows to judge {F.release_open}" if F.release_open else ""),
          f"- range for the decisions alone: {lo:g} to {hi:g} hours (toolkit assumption per item: " + ", ".join(
              f"{e} {HOURS[e][0]:g}-{HOURS[e][1]:g} h" for e in "SML") + "; not measured). Key-user time, screen review and go-live are not in it.",
          "- unknown at this point:"]
    L += [f"  - not measured: {n}: {w}" for n, w in F.not_measured] or ["  - nothing: every input was read"]
    L += testing_plan(F)
    notes = agent_notes(F.W)
    if notes:
        L += ["", "## Agent notes", "",
              "From AGENT-NOTES.md in the work folder, written by the agent and kept on every rerun; this section is not part of the plan hash.", ""]
        L += ["> " + ln if ln.strip() else ">" for ln in notes.splitlines()]
    L += ["", "## 6. Sign-off", "", signoff_text, ""]
    return "\n".join(L)


def agent_notes(work):
    """The text of W/AGENT-NOTES.md (free text, written by the agent, never written by this script), or ''."""
    return (read(os.path.join(work, "AGENT-NOTES.md")) or "").strip()


def signoff_default():
    return ("A person writes exactly one of these two lines below (an agent never does). Copy the line, fill in the name and the date, "
            "and leave out the angle brackets; backticks and spaces around the line do no harm. "
            "The line `Status: open` may stay or go: the reader takes a real Signed-off line whether it is there or not.\n\n"
            "`Signed-off: <name> <yyyy-mm-dd>`   or   `Status: PAUSED <reason>`\n\n"
            "Status: open")


def _plain(ln):
    """A section-6 line as a person may have pasted it: backticks, quote marks, list marks and spaces around it dropped (GF-27)."""
    return re.sub(r"^[\s`>*-]+|[\s`]+$", "", ln)


def _section6(text):
    i = (text or "").find("\n## 6.")
    return (text[i:] if i >= 0 else "").splitlines()


def parse_signoff(text):
    if not text:
        return None
    sec = _section6(text)
    for ln in sec:
        m = PAUSED.match(_plain(ln))
        if m and "<" not in m.group(1):
            return ("paused", m.group(1), "")
    for ln in sec:
        m = SIGNED.match(_plain(ln))
        # the literal template (`Signed-off: <name> <yyyy-mm-dd>`) is never a signature (GF-27)
        if m and "<" not in m.group(1):
            return ("signed", m.group(1), m.group(2))
    return None


def signoff_problem(text):
    """Why a Signed-off or PAUSED line in section 6 is not a sign-off, or None when there is none to explain (GF-27: the rerun said
    only "awaits sign-off")."""
    for ln in _section6(text):
        t = _plain(ln)
        if not re.match(r"(?i)^(Signed-off|Status:\s*PAUSED)", t) or " or " in t:   # " or ": the default line offering both choices
            continue
        m = SIGNED.match(t) or PAUSED.match(t)
        if "<" in t:
            return f"found the template line '{t}': replace the angle-bracket text with your name and the date (or the reason)"
        if not m:
            return f"found a line that is not a sign-off: '{t}'. Write it as 'Signed-off: <your name> <yyyy-mm-dd>' (a real name, a date such as 2026-10-15)"
    return None


def signed_items(text):
    """The item set stored in a PROPOSAL.md (list of ident strings), or None for one written before GM-21 or unreadable."""
    for ln in (text or "").splitlines():
        m = ITEMS.match(ln)
        if m:
            try:
                v = json.loads(base64.b64decode(m.group(1)).decode())
                return v if isinstance(v, list) and all(isinstance(x, str) for x in v) else None
            except Exception:
                return None
    return None


def ident_label(x):
    """A person-readable line for one ident string of the hash (2|key|text, 3|kind|name|evidence, 4|key|text, v|...)."""
    p = x.split("|")
    if p[0] == "3" and len(p) >= 3:
        return f"{p[1]}: {p[2]}"
    if p[0] in ("2", "4") and len(p) >= 3:
        return "|".join(p[2:])
    return x


def item_lines(text):
    out = set()
    sec = ""
    for ln in (text or "").splitlines():
        if ln.startswith("## "):
            sec = ln
        elif ln.startswith("- ") and sec[:5] in ("## 2.", "## 3.", "## 4."):
            out.add(sec[3:4] + ": " + re.sub(r"^- \[P-\d+\] ", "- ", ln))
    return out


def write_decisions(F, rows, signer, status, closes):
    path = os.path.join(F.W, "DECISIONS.md")
    have = decisions(F.W)
    add = []
    for rid, name, kind, option, reason in rows:
        if rid in have:
            continue
        add.append(f"{rid} | {name} | {kind} | {option} | {reason} | {signer} | {status} | closes by: {closes}")
    if add:
        with open(path, "a", encoding="utf-8") as f:
            if os.path.exists(path) and os.path.getsize(path) and not (read(path) or "").endswith("\n"):
                f.write("\n")
            f.write("\n".join(add) + "\n")
    return len(add)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--work", required=True)
    ap.add_argument("--source"); ap.add_argument("--target"); ap.add_argument("--target2")
    ap.add_argument("--original"); ap.add_argument("--app")
    ap.add_argument("--unattended", action="store_true")
    ap.add_argument("--ra-file", help="re-architecture catalogue to read (default playbooks/rearchitecture.md)")
    ap.add_argument("--status", action="store_true")
    a = ap.parse_args()
    a.work = os.path.abspath(a.work)
    out_path = os.path.join(a.work, "PROPOSAL.md")
    old = read(out_path)
    if a.status:
        s = parse_signoff(old)
        print("none" if old is None else s[0] if s else "unsigned")
        return 0
    if not os.path.isdir(a.work):
        print(f"proposal: no work folder {a.work}", file=sys.stderr)
        return 2
    F = Facts(a)
    F.build()
    ids_for(F.items3, a.work)
    reanswer(F.items3, a.work)
    sids = write_steps(F, a.work) if os.path.isdir(a.work) else {}
    # keptvendor.json: the items about the app's OWN styling (GF-56) exist at triage, before the sign-off, so they are in the hash; a
    # kept module's items (written after the update step) are not. keptstyle.json is not in it either.
    # the hash is taken without kept.txt: the update step writes it after the sign-off, and a module it kept moves from section 2 to
    # section 3 (cold test WM1: 7 kept modules cleared the sign-off at the end of rung 1 and asked the whole plan again). The
    # signed path below accepts a kept module the signed PROPOSAL.md rendered (section 2 or 3) at its recommendation, CONFIRMED in the signer's
    # name (they read that module; update, a real logic edit held for <Module>_Ext). A kept module or file the signed PROPOSAL.md never
    # showed is ASSUMED ("signer did not see it"; see unseen() below).
    H = F
    if F.kept or F.kv_seen or F.ks_seen:
        H = Facts(a)
        H.keptmods = lambda: None
        H.keptvend = lambda: Facts.keptvend(H, only="own")   # GM-15: a kept module's rows of keptvendor.json, like kept.txt, come after the sign-off; GF-56: own-styling rows do not
        H.keptstyle = lambda: None  # MC-11: keptstyle.json likewise
        H.build()
    ident = [f"2|{it['key']}|{it['text']}" for it in H.items2] + [f"3|{it['kind']}|{it['name']}|{it['evidence']}" for it in H.items3] \
        + [f"4|{it['key']}|{it['text']}" for it in H.items4] + [f"v|{H.src}|{H.tgt}|{H.tgt2}"]
    hashval = hashlib.sha256("\n".join(sorted(ident)).encode()).hexdigest()
    F.ident = ident
    prev_hash = next((m.group(1) for m in (HASH.match(x) for x in (old or "").splitlines()) if m), None)
    so = parse_signoff(old)
    today = os.environ.get("PROPOSAL_TODAY") or datetime.date.today().isoformat()

    signed_text = old or ""

    def unseen(it):
        """GF-32: an item the signature does not cover was never seen by the signer. keptvendor.json and keptstyle.json items are
        always new. A kept.txt module is seen when the signed PROPOSAL.md rendered it, as its section-3 item or as its section-2 update
        line (the update step moved it to section 3 after the sign-off; the signer still read that module). A kept module the signed
        file never showed appeared later."""
        if it.get("own"):
            return True
        if f"3|{it['kind']}|{it['name']}|{it['evidence']}" in set(ident):
            return False
        # a rerun re-renders PROPOSAL.md with the late item in it, so the regex below would read it as seen: the lines DECISIONS.md
        # holds for it are what stay true. Any line saying "appeared after sign-off" keeps it late until a LATER line is a hand answer.
        lines = decisions_all(a.work).get(it["id"], [])
        if any(len(d) > 3 and d[3].startswith("appeared after sign-off") for d in lines):
            return deciding_line(lines) is None
        n = re.escape(it["name"])
        return not re.search(rf"^- \[P-\d+\] {re.escape(it['kind'])}: {n}$|module update {n} ", signed_text, re.M)

    def accept_answers(signer):
        ans = decisions(a.work)
        todo = [it for it in F.items3 if it["id"] not in ans]
        rows = [(it["id"], it["name"], it["kind"], it["rec"], f"accepted with the sign-off of {signer} (no separate answer)")
                for it in todo if not unseen(it)]
        # an item the signed PROPOSAL.md never rendered was not seen by the signer: ASSUMED, never CONFIRMED in their name
        late = [(it["id"], it["name"], it["kind"], it["rec"], "appeared after sign-off; signer did not see it")
                for it in todo if unseen(it)]
        n = write_decisions(F, rows, signer, "CONFIRMED", "the rung that measures it passes (steps/decide.md)")
        return n, write_decisions(F, late, "-", "ASSUMED", "a person answers it with decisions.py add, or a hand-written line (steps/decide.md)")

    if so and so[0] == "paused":
        print(f"proposal: PAUSED by the owner: {so[1]}. Resume: remove the Status line and sign, then rerun the pipeline.")
        return 15
    if so and so[0] == "signed" and prev_hash == hashval:
        # same plan, newer wording (cold test WM1: the signed cards kept saying "keep old version" after the toolkit
        # recommended the update): re-render the items, the person's sign-off section is copied over as written
        i = old.find("\n## 6. Sign-off\n")
        cur = render(F, hashval, None, old[i + len("\n## 6. Sign-off\n"):].strip("\n")) if i >= 0 else old
        if cur != old and parse_signoff(cur) == so:
            with open(out_path + ".tmp", "w", encoding="utf-8") as f:
                f.write(cur)
            os.replace(out_path + ".tmp", out_path)
        n, nl = accept_answers(so[1])
        # an item that appeared after the sign-off (keptvendor.json, keptstyle.json) was not seen by the signer: its step is assumed, not approved in their name
        late_ids = {it["id"] for it in F.items3 if unseen(it)}
        late = {s: k for s, k in sids.items() if k.startswith("3:") and k[2:] in late_ids}
        approve_steps(a.work, {s: k for s, k in sids.items() if s not in late}, "approved", so[1], "signoff",
                      {i: deciding_line(l) for i, l in decisions_all(a.work).items()})
        approve_steps(a.work, late, "assumed", "agent", "after-signoff")
        print(f"proposal: signed by {so[1]} on {so[2]}" + (f"; {n} unanswered section-3 item(s) took their recommendation (DECISIONS.md)" if n else "")
              + (f"; {nl} item(s) appeared after sign-off (ASSUMED in DECISIONS.md, the signer did not see them)" if nl else ""))
        return 0
    changed = None
    shrink_msg = None
    signoff = signoff_default()
    if so and so[0] == "signed":
        cur = render(F, hashval, None, signoff)
        before, after = item_lines(old), item_lines(cur)
        was, now = signed_items(old), set(ident)
        held = sorted(set(was) - now) if was is not None and now < set(was) else []
        if held:
            # GM-21: the scope only shrank (items removed, none added or changed). The sign-off is cleared and a person signs as
            # before; only the reading is lighter: the held-back list is shown. Nothing is carried over: no Signed-off line is
            # written here. The shared write and the unattended handling below run as for any changed plan.
            changed = [f"## Held back since signed ({so[1]}, {so[2]})", "",
                       f"The scope is smaller than the one signed: {len(held)} item(s) were held back, none added, none changed. "
                       "The sign-off is cleared and section 6 is signed again as before; what differs from the plan signed is only the items below.", ""]
            changed += [f"- held back: {ident_label(x)}" for x in held]
            signoff = (f"Previously signed-off: {so[1]} {so[2]} (cleared: scope shrank, {len(held)} held-back item(s); sign again)\n\n" + signoff)
            shrink_msg = (f"proposal: scope shrank since the sign-off of {so[1]} ({so[2]}): {len(held)} item(s) held back, none added or changed; "
                          "sign section 6 again (the held-back list is in the file)")
        else:
            changed = [f"## Changed since signed ({so[1]}, {so[2]})", "",
                       "The plan inputs changed after the sign-off; the sign-off is cleared and the proposal is asked again. "
                       "Items that differ from the signed version:", ""]
            changed += [f"- removed: {x}" for x in sorted(before - after)] + [f"- added: {x}" for x in sorted(after - before)]
            if before == after:
                changed.append("- no item text differs; the versions or the evidence behind an item changed (compare the input files)")
            signoff = f"Previously signed-off: {so[1]} {so[2]} (cleared: the plan inputs changed)\n\n" + signoff
    doc = render(F, hashval, changed, signoff)
    tmp = out_path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(doc)
    os.replace(tmp, out_path)
    if a.unattended:
        rows = [("P-0", "proposal", "proposal", "continue without a sign-off", "Interview mode: unattended signs nothing; the run goes on at the recommendations")]
        rows += [(it["id"], it["name"], it["kind"], it["rec"], "unattended: recommendation taken, nobody asked") for it in F.items3]
        write_decisions(F, rows, "-", "ASSUMED (unattended)", "a person signs PROPOSAL.md section 6")
        # routine work with a known result (section 2) goes ahead in auto mode; only a real decision waits for a person (the owner, 2026-11-17)
        routine = {s: k for s, k in sids.items() if k.startswith("2:")}
        approve_steps(a.work, {s: k for s, k in routine.items() if k != "2:module-edits"}, "approved", "agent", steps.ROUTINE)
        approve_steps(a.work, {s: k for s, k in routine.items() if k == "2:module-edits"}, "approved", "agent", steps.CARRY)
        approve_steps(a.work, {s: k for s, k in sids.items() if s not in routine}, "assumed", "agent", "unattended")
        print("proposal: not signed (unattended): ASSUMED (unattended) lines in DECISIONS.md; every report says 'proposal not signed'")
        return 0
    if shrink_msg:
        print(f"{shrink_msg}: {out_path}")
        return 14
    prob = signoff_problem(old)
    if prob:
        print(f"proposal: {prob}")
    print(f"proposal awaits sign-off: {out_path} ({len(F.items2)} done by the toolkit, {len(F.items3)} to decide, {len(F.items4)} for a person)")
    return 14


if __name__ == "__main__":
    sys.exit(main())
