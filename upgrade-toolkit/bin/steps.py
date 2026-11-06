#!/usr/bin/env python3
"""steps.py: the step records of an upgrade run, <work>/steps.jsonl (append only, the last event per id and field wins).

  steps.py open    --work W --topic T --title TEXT --say TEXT [--stage S] [--evidence E ...] [--alias P-n] [--by NAME]
  steps.py propose --work W --id S-n [--say TEXT] [--why TEXT] [--option TEXT ...] [--recommend N] [--closes-by RUNG ...] [--decision D ...]
  steps.py propose --work W --new --topic T --title TEXT --found TEXT --say TEXT [--why TEXT] [--option TEXT ...] [--decision D ...]
                   (a mid-run decision: opens the step AND records it as assumed by the agent, so it needs a person; prints the new S-n)
  steps.py approve --work W --id S-n --state approved|assumed|rejected --by NAME [--source SRC]
  steps.py done    --work W --id S-n --commit SHA --say TEXT
  steps.py tested  --work W --id S-n --rung RUNG --verdict V --say TEXT [--proof P ...]
  steps.py tested  --work W --gate GATE_DIR         (the gate's own link: every step's closes_by rungs from gate-summary.md; see below)
  steps.py gap     --work W --id S-n --field F --say TEXT
  steps.py show    --work W [S-n] [--json]
  steps.py find    --work W --id S-n|P-n | --topic T      (prints the S-n, exit 1 when there is none)
  steps.py trailer [--work W] --kind KIND           (prints "Upgrade-Step: S-n" for a commit of that kind, nothing when no step fits; never fails)
  steps.py check   --work W [--decisions AGENT-DECISIONS.md]
  steps.py trail   --work W [--decisions AGENT-DECISIONS.md]   (the gate rung: the same completeness, in plain words; exit 1 on a gap)
  steps.py import-legacy --work W [--app REPO] [--decisions AGENT-DECISIONS.md]   (steps.jsonl for a run made before step records)

Event: {id, field, value, by, at}. One line per event, never rewritten; steps.py is the only writer. Fields: topic, title, alias
(the old P-n id of a plan item), found_say, stage, evidence, proposed_say, why, options, recommend, closes_by, decisions, approval ({state, source}),
commit:<sha> ({sha, say}), test:<rung> ({rung, verdict, say, proof}), gap:<field> (say).
Folded record: see STEP-RECORDS-PLAN.md section 2. status is derived, never written: done when approved and every
closes_by rung is PASS or PASS*; blocked on a FAIL or a rejection; otherwise open.

tested --gate reads GATE_DIR/gate-summary.md (and heal.json in the work folder) and writes, for each step and each rung in its
closes_by, one result: PASS or PASS* when the rung row says so, FAIL when it says FAIL, and a gap in plain words for every other
case (INVALID, NOT RUN, EXCEPT, no such row). A step with no closes_by gets the gap "no check is linked". A gap is a NOT RUN
result plus a gap:tested:<rung> event, so an earlier PASS is replaced and the step is never done on a test nobody ran. The gate's
verdict is never changed by this command. A rerun with the same gate adds no event.

A say holds plain words for a person: no backticks, no file path, no file name. Such text is refused (exit 2).

check also reads AGENT-DECISIONS.md (--decisions, else the work folder, else its parent): every D row must name an S-n that exists
(slice 4: a decision the agent made on its own is a step that needs the owner's OK, never only a row in a file).

trail asks, for every step: a proposal, an approval (assumed counts but is flagged), a done change or a written gap, a tested
result or a written gap, and every D row of AGENT-DECISIONS.md names a step. bin/gate.sh runs it as the rung trail (optional;
TRAIL_REQUIRED=1 makes it required, steps/gate.md).

import-legacy reads cockpit-items.json, cockpit-trail.json, PROPOSAL.md ([P-n] items and the routine updates), DECISIONS.md,
AGENT-DECISIONS.md (every D row not named by another step becomes a step assumed by the agent) and, with --app, the commits of the
app repo (linked only when a commit names the step's D row or its short hash appears in the step's own text). Every event carries
source "legacy" and by "legacy". What cannot be linked becomes a gap, "not linked in this run"; nothing is guessed. A second run
with the same inputs adds no event, and a field or approval that a person or the toolkit wrote is never overwritten.

Exit: 0 ok (check: complete), 1 check found something missing, 2 usage or refused input.
"""
import argparse, datetime, json, os, re, sys

FILE = "steps.jsonl"
EVENT_SOURCE = None   # import-legacy sets "legacy": every event it writes carries it
STATES = ("approved", "assumed", "rejected")
VERDICTS = ("PASS", "PASS*", "FAIL", "INVALID", "NOT RUN")
GAP_FIELDS = ("found", "proposed", "approval", "done", "tested")
FILENAME = re.compile(r"\b[\w-]+\.(py|md|json|jsonl|sh|js|ts|tsx|html|css|txt|csv|tsv|yml|yaml|xml|java|mpr|mpk|log)\b", re.I)
SLASHPATH = re.compile(r"(^|\s)(~|\.{1,2})?/\S|[\w.-]+/[\w.-]+/[\w.-]")   # a rooted path or two segments; "and/or" is plain


def die(msg, code=2):
    """Print one error line and exit."""
    print(f"steps: {msg}", file=sys.stderr)
    sys.exit(code)


def now():
    """UTC time stamp for an event."""
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def clean(s):
    """Collapse whitespace."""
    return " ".join(str(s).split())


def plain(s):
    """True when the text holds no backticks, file path or file name."""
    return not ("`" in s or FILENAME.search(s) or SLASHPATH.search(s))


BARE_ID = re.compile(r"[A-Za-z0-9_.:-]+")   # one token with no space: a module name, a decision id, a file name
DECISION_ID = re.compile(r"\bdecisions?\s+D\d+\b|^D\d+[a-z]?\b", re.I)
# a D row about one of these subjects gets the title of the subject, never the row's own wording
TITLE_TOPICS = (
    (re.compile(r"log ?in|sign[- ]?in|\bSSO\b|password", re.I), "How the test walks sign in"),
    (re.compile(r"\bseed|test data", re.I), "Seed data for the journeys"),
    (re.compile(r"\bheal", re.I), "How test-side problems are healed"),
    (re.compile(r"feedback", re.I), "What to do with the feedback widget"),
    (re.compile(r"\bcharts?\b", re.I), "What to do with the old Charts widgets"),
)


def capital(t):
    """The text with a capital first letter."""
    t = clean(t)
    first = t.split(" ")[0]
    return t if not (first.isalpha() and first.islower()) else t[:1].upper() + t[1:]   # jQuery stays jQuery


def title_problem(t):
    """Why a step title is not plain (a bare name or id, a decision id, a lowercase start), or None. The rule: a title says WHAT is chosen."""
    t = clean(t)
    if not t:
        return "the title is empty"
    if BARE_ID.fullmatch(t):
        return f"the title \"{t}\" is one bare name or id; say what is chosen, for example \"Keep or update module {t}\" or \"A choice about {t}\""
    if DECISION_ID.search(t):
        return f"the title \"{t}\" names a decision id; say what is chosen, or \"A choice about <topic>\""
    if t.split(" ")[0].isalpha() and t.split(" ")[0].islower():
        return f"the title \"{t}\" starts with a small letter; start with a capital"
    return None


def item_title(kind, name):
    """The title of a proposal item (kind and name as proposal.py writes them): a template from the kind plus the subject."""
    kind, name = clean(kind).lower(), clean(name)
    m = re.fullmatch(r"(\S+) themesource edits", name)
    if kind == "theme" and m:
        return f"How to keep the {m.group(1)} style edits"
    if BARE_ID.fullmatch(name) or re.fullmatch(r"[\w.-]+ [\d.x]+", name):
        pre = {"module": "Keep or update module ", "renamed module": "Switch to the renamed module ", "java": "Keep or replace the Java library ",
               "widget": "Keep or replace the widget ", "theme": "How to keep the theme "}.get(kind)
        return (pre + name) if pre else f"A choice about {name}"
    return capital(name)


def check_plain(label, text):
    """Refuse a say that holds a path or code."""
    if not text:
        die(f"{label} is empty")
    if not plain(text):
        die(f"{label} must be plain words: no backticks, file path or file name (put them in --evidence or --proof): {text}")


def path_of(work):
    """Location of the event file."""
    return os.path.join(work, FILE)


class Damaged(ValueError):
    """steps.jsonl holds a line that is not an event."""


def read_events(work):
    """All events in file order. A line that is not an event raises Damaged; a missing file gives []."""
    out = []
    try:
        f = open(path_of(work), encoding="utf-8")
    except FileNotFoundError:
        return out
    with f:
        for n, line in enumerate(f, 1):
            if not line.strip():
                continue
            try:
                e = json.loads(line)
                assert isinstance(e, dict) and e["id"] and e["field"]
            except (ValueError, AssertionError, KeyError, TypeError):
                raise Damaged(f"line {n} is not an event")
            out.append(e)
    return out


def events(work):
    """All events in file order; a line that is not an event is a usage error."""
    try:
        return read_events(work)
    except Damaged as e:
        die(f"{path_of(work)} {e}")


def load(work):
    """(records, error) for readers that must not stop, such as the cockpit: records is None when steps.jsonl is missing (error None)
    or damaged (error says which line), so the reader can fall back to its older inputs."""
    if not os.path.isfile(path_of(work)):
        return None, None
    try:
        recs = fold(read_events(work))
        for r in recs:
            ok = (all({"sha", "say"} <= set(c) for c in r["done"]["commits"] if isinstance(c, dict))
                  and all(isinstance(c, dict) for c in r["done"]["commits"])
                  and all(isinstance(t, dict) and {"rung", "verdict", "say"} <= set(t) for t in r["tested"]["results"])
                  and (r.get("approval") is None or "state" in r["approval"]))
            if not ok:
                raise Damaged(f"step {r['id']} is incomplete")
        return recs, None
    except (Damaged, OSError, UnicodeDecodeError, KeyError, TypeError, ValueError) as e:
        return None, str(e) or "unreadable"


def append(work, sid, field, value, by):
    """Append one event."""
    e = {"id": sid, "field": field, "value": value, "by": by, "at": now()}
    if EVENT_SOURCE:
        e["source"] = EVENT_SOURCE
    with open(path_of(work), "a", encoding="utf-8") as f:
        f.write(json.dumps(e, ensure_ascii=False) + "\n")


def idnum(sid):
    """Number of an S-n id, 0 when it is not one."""
    m = re.fullmatch(r"S-(\d+)", sid)
    return int(m.group(1)) if m else 0


def lastmap(evs):
    """{id: {field: event}} with the last event per id and field."""
    out = {}
    for e in evs:
        out.setdefault(e["id"], {})[e["field"]] = e
    return out


def derive_status(rec):
    """open, done or blocked, from approval and tests only."""
    ap = (rec.get("approval") or {}).get("state")
    res = rec["tested"]["results"]
    if ap == "rejected" or any(r["verdict"] == "FAIL" for r in res):
        return "blocked"
    got = {r["rung"]: r["verdict"] for r in res}
    if not rec["proposed"].get("closes_by") and "tested" in rec["gaps"]:
        return "open"   # the gate wrote "no check is linked": that is a gap, never a pass
    if ap == "approved" and all(got.get(r) in ("PASS", "PASS*") for r in rec["proposed"].get("closes_by", [])):
        return "done"
    return "open"


def fold(evs):
    """Fold events into records, ordered by id number."""
    recs = []
    for sid, fs in lastmap(evs).items():
        v = lambda k, d=None: fs[k]["value"] if k in fs else d
        proposed = {k: v(n) for k, n in (("say", "proposed_say"), ("why", "why"), ("options", "options"), ("recommend", "recommend"),
                                         ("closes_by", "closes_by"), ("decisions", "decisions")) if n in fs}
        rec = {"id": sid, "topic": v("topic", ""), "title": v("title", ""),
               "found": {k: v(n) for k, n in (("say", "found_say"), ("stage", "stage"), ("evidence", "evidence")) if n in fs},
               "proposed": proposed}
        if "alias" in fs:
            rec["alias"] = v("alias")
        if "approval" in fs:
            rec["approval"] = dict(fs["approval"]["value"], by=fs["approval"]["by"], at=fs["approval"]["at"])
        rec["done"] = {"commits": [fs[k]["value"] for k in sorted(fs, key=lambda k: fs[k]["at"]) if k.startswith("commit:")]}
        rec["tested"] = {"results": [fs[k]["value"] for k in sorted(fs, key=lambda k: fs[k]["at"]) if k.startswith("test:")]}
        rec["gaps"] = {k[4:]: fs[k]["value"] for k in fs if k.startswith("gap:")}
        rec["status"] = derive_status(rec)
        recs.append(rec)
    return sorted(recs, key=lambda r: idnum(r["id"]))


def known(work, sid):
    """Refuse an id that was never opened."""
    if not any(e["id"] == sid and e["field"] == "topic" for e in events(work)):
        die(f"unknown step '{sid}' (steps.py show lists the ids)")


# ---- library use by proposal.py and decisions.py (they import these, they never shell out) ----
def resolve(work, ref):
    """The S-n id for an S-n id or a P-n alias, None when no step has it."""
    for r in fold(events(work)):
        if ref in (r["id"], r.get("alias")):
            return r["id"]
    return None


def ensure(work, topic, title, fields, by="toolkit"):
    """Open the step with this topic and title, or find it, then write each field whose value differs from the folded one.
    fields: {event field: value}. A rerun with the same input adds no event. Returns the S-n id."""
    evs = events(work)
    sid = next((r["id"] for r in fold(evs) if r["topic"] == topic and r["title"] == title), None)
    if sid is None:
        sid = f"S-{max([idnum(e['id']) for e in evs] + [0]) + 1}"
        append(work, sid, "topic", topic, by)
        append(work, sid, "title", title, by)
    cur = lastmap(events(work)).get(sid, {})
    for f, v in fields.items():
        if v is None or v == [] or (f in cur and cur[f]["value"] == v):
            continue
        append(work, sid, f, v, by)
    return sid


def approval_of(work, sid):
    """The folded approval of a step ({state, by, at, ...}) or None."""
    r = next((r for r in fold(events(work)) if r["id"] == sid), None)
    return r.get("approval") if r else None


def set_approval(work, sid, state, by, source="", **extra):
    """Write one approval event (the last one wins); extra keys are kept in the value."""
    append(work, sid, "approval", dict({"state": state, "source": source}, **extra), clean(by))


def add_commit(work, sid, sha, say, by="toolkit"):
    """Add a commit to a step unless it is there already. True when an event was written."""
    if any(c["sha"] == sha for r in fold(events(work)) if r["id"] == sid for c in r["done"]["commits"]):
        return False
    append(work, sid, f"commit:{sha}", {"sha": sha, "say": clean(say)}, clean(by))
    return True


def find_topic(work, topic):
    """The S-n id of the step with this topic, None when there is none."""
    return next((r["id"] for r in fold(events(work)) if r["topic"] == topic), None)


def cmd_find(a):
    """Print the S-n of an id, a P-n alias or a topic."""
    sid = resolve(a.work, a.id) if a.id else find_topic(a.work, a.topic) if a.topic else die("find needs --id or --topic")
    if not sid:
        return 1
    print(sid)
    return 0


KIND_TOPIC = {"module-update": "modules", "replay": "modules", "repair": "repairs", "convert": "convert"}


def cmd_trailer(a):
    """The commit trailer for a toolkit commit: UPG_STEP when set (an S-n or P-n), else the step whose topic fits the commit kind.
    Prints nothing and exits 0 when no step fits, so a commit without a step still happens and the change list shows it as such."""
    work = a.work or os.environ.get("UPG_STEPS_WORK", "")
    if not work or not os.path.isfile(path_of(work)):
        return 0
    ref = os.environ.get("UPG_STEP", "")
    sid = resolve(work, ref) if ref else find_topic(work, KIND_TOPIC.get(a.kind, "-"))
    if sid:
        print(f"Upgrade-Step: {sid}")
    return 0


def cmd_open(a):
    """Create the next S-n and print it."""
    check_plain("--say", a.say)
    a.title = capital(a.title)
    if title_problem(a.title):
        die(title_problem(a.title))
    n = max([idnum(e["id"]) for e in events(a.work)] + [0]) + 1
    sid = f"S-{n}"
    by = clean(a.by)
    for f, v in (("topic", clean(a.topic)), ("title", clean(a.title)), ("alias", a.alias), ("found_say", clean(a.say)),
                 ("stage", a.stage), ("evidence", a.evidence)):
        if v:
            append(a.work, sid, f, v, by)
    print(sid)
    return 0


def cmd_propose_new(a):
    """A decision made mid-run: open the step, set found and proposed, write the approval as assumed by the agent."""
    for lab, t in (("--topic", a.topic), ("--title", a.title), ("--found", a.found), ("--say", a.say)):
        if not t:
            die(f"--new needs {lab}")
    if a.id:
        die("--new opens a step, it takes no --id")
    a.title = capital(a.title)
    if title_problem(a.title):
        die(title_problem(a.title))
    for lab, t in [("--found", a.found), ("--say", a.say), ("--why", a.why)] + [("--option", o) for o in a.option or []]:
        if t is not None:
            check_plain(lab, t)
    by = clean(a.by)
    sid = f"S-{max([idnum(e['id']) for e in events(a.work)] + [0]) + 1}"
    for f, v in (("topic", clean(a.topic)), ("title", clean(a.title)), ("found_say", clean(a.found)), ("stage", a.stage or "run"),
                 ("proposed_say", clean(a.say)), ("why", clean(a.why) if a.why else None), ("options", a.option),
                 ("recommend", a.recommend), ("closes_by", a.closes_by), ("decisions", a.decision)):
        if v is not None and v != []:
            append(a.work, sid, f, v, by)
    set_approval(a.work, sid, "assumed", "agent", "mid-run", needs="the owner's OK")
    print(sid)
    print(f"steps: {sid} proposed, assumed by the agent, needs the owner's OK. Write {sid} in the D row.")
    return 0


def cmd_propose(a):
    """Set the proposal fields given on the command line."""
    if a.new:
        return cmd_propose_new(a)
    if not a.id:
        die("propose needs --id S-n (or --new to open a step)")
    known(a.work, a.id)
    for lab, t in [("--say", a.say), ("--why", a.why)] + [("--option", o) for o in a.option or []]:
        if t is not None:
            check_plain(lab, t)
    by = clean(a.by)
    for f, v in (("proposed_say", a.say), ("why", a.why), ("options", a.option), ("recommend", a.recommend),
                 ("closes_by", a.closes_by), ("decisions", a.decision)):
        if v is not None and v != []:
            append(a.work, a.id, f, clean(v) if isinstance(v, str) else v, by)
    print(f"steps: {a.id} proposed")
    return 0


def cmd_approve(a):
    """Set the approval; the first one stays in the file."""
    known(a.work, a.id)
    if a.state not in STATES:
        die(f"bad state '{a.state}': {', '.join(STATES)}")
    append(a.work, a.id, "approval", {"state": a.state, "source": a.source or ""}, clean(a.by))
    print(f"steps: {a.id} {a.state} by {clean(a.by)}")
    return 0


def cmd_done(a):
    """Add a commit that did the step."""
    known(a.work, a.id)
    check_plain("--say", a.say)
    sha = a.commit.strip()
    if not re.fullmatch(r"[0-9a-f]{7,40}", sha):
        die(f"'{a.commit}' is not a commit sha")
    append(a.work, a.id, f"commit:{sha}", {"sha": sha, "say": clean(a.say)}, clean(a.by))
    print(f"steps: {a.id} done by {sha}")
    return 0


RUNG_PLAIN = {"build": "build", "idcheck": "data identity check", "const": "settings check", "data": "data comparison",
              "rest": "outside call comparison", "logdiff": "log comparison", "smoke": "page walk-through",
              "journeys": "click paths", "screens": "screen comparison", "release": "release notes check",
              "apis": "outside systems check", "widgets": "widgets check"}
SUMMARY_ROW = re.compile(r"^\| (\d+) \| (\w+) \| (PASS\*?|FAIL|INVALID|NOT RUN|EXCEPT) \| ([\d-]+) \| (.*) \|$")


def gate_rows(summary):
    """{rung: (verdict, one line)} from the table of a gate-summary.md; {} when the file is missing."""
    out = {}
    try:
        text = open(summary, encoding="utf-8").read()
    except OSError:
        return out
    for ln in text.splitlines():
        m = SUMMARY_ROW.match(ln)
        if m:
            out[m.group(2)] = (m.group(3), m.group(5).replace("\\|", "|").strip())
    return out


def heal_regressions(work):
    """Number of click paths the heal step found to pass on the old app and fail on the new one, None without a heal.json."""
    try:
        rows = json.load(open(os.path.join(work, "heal.json"), encoding="utf-8")).get("rows", [])
    except (OSError, ValueError, AttributeError):
        return None
    return sum(1 for r in rows if isinstance(r, dict) and r.get("class") == "real-regression" and str(r.get("id", "")).startswith("journey:"))


NO_CHECK = "No check is linked to this step, so nothing tested it."


def gate_outcome(rung, rows, nreg):
    """(verdict or None for a gap, plain sentence) of one rung. Template sentences only."""
    name = RUNG_PLAIN.get(rung, rung)
    v = rows.get(rung, (None, ""))[0]
    if v in ("PASS", "PASS*"):
        return v, f"The {name} passed on the new app." if v == "PASS" else f"The {name} passed on the new app, with differences that a person accepted."
    if v == "FAIL":
        extra = f" {nreg} click paths work on the old app and fail on the new one." if rung == "journeys" and nreg else ""
        return "FAIL", f"The {name} found a problem on the new app.{extra}"
    why = {"INVALID": "could not judge", "NOT RUN": "did not run", "EXCEPT": "only passed except on a system that was left out"}.get(v)
    if why is None:
        return None, f"No result for the {name} was found, so nothing tested this."
    return None, f"The {name} {why}, so nothing has shown that this works."


def cmd_tested_gate(a):
    """Link the gate's rungs to the steps: one result or one gap per step and rung. Never touches the gate's verdict."""
    summary = a.summary or os.path.join(a.gate, "gate-summary.md")
    if not os.path.isfile(summary):
        die(f"no gate-summary.md in {a.gate}")
    rows, nreg, by = gate_rows(summary), heal_regressions(a.work), clean(a.by)
    proof = [os.path.join(os.path.basename(os.path.normpath(a.gate)), "gate-summary.md")]
    wrote = 0
    for rec in fold(events(a.work)):
        cur = lastmap(events(a.work)).get(rec["id"], {})

        def put(field, value):
            nonlocal wrote
            if field in cur and cur[field]["value"] == value:
                return
            append(a.work, rec["id"], field, value, by)
            wrote += 1
        rungs = rec["proposed"].get("closes_by") or []
        if not rungs:
            put("gap:tested", NO_CHECK)
            continue
        for rung in rungs:
            verdict, say = gate_outcome(rung, rows, nreg)
            pf = proof + ([f"row: {rows[rung][1]}"] if rung in rows else [])
            put(f"test:{rung}", {"rung": rung, "verdict": verdict or "NOT RUN", "say": say, "proof": pf})
            if verdict is None:
                put(f"gap:tested:{rung}", say)
    print(f"steps: tested --gate: {wrote} event(s) written from {summary}")
    return 0


def cmd_tested(a):
    """Add (or replace, same rung) a test result."""
    if a.gate:
        return cmd_tested_gate(a)
    if not (a.id and a.rung and a.verdict and a.say):
        die("tested needs --id, --rung, --verdict and --say (or --gate GATE_DIR)")
    known(a.work, a.id)
    if a.verdict not in VERDICTS:
        die(f"bad verdict '{a.verdict}': {', '.join(VERDICTS)}")
    check_plain("--say", a.say)
    append(a.work, a.id, f"test:{a.rung}", {"rung": a.rung, "verdict": a.verdict, "say": clean(a.say), "proof": a.proof or []},
           clean(a.by))
    print(f"steps: {a.id} {a.rung} {a.verdict}")
    return 0


def cmd_gap(a):
    """Write the reason a part is missing."""
    known(a.work, a.id)
    if a.field.split(":")[0] not in GAP_FIELDS:
        die(f"bad gap field '{a.field}': {', '.join(GAP_FIELDS)} (tested:<rung> for one rung)")
    check_plain("--say", a.say)
    append(a.work, a.id, f"gap:{a.field}", clean(a.say), clean(a.by))
    print(f"steps: {a.id} gap {a.field}")
    return 0


def cmd_show(a):
    """Print the folded records."""
    recs = fold(events(a.work))
    if a.sid:
        recs = [r for r in recs if r["id"] == a.sid]
        if not recs:
            die(f"unknown step '{a.sid}'")
    if a.json:
        print(json.dumps(recs, indent=1, ensure_ascii=False))
        return 0
    for r in recs:
        print(f"{r['id']}  [{r['status']}]  {r['topic']}  {r['title']}")
        print(f"    approval: {(r.get('approval') or {}).get('state', 'none')}  commits: {len(r['done']['commits'])}  tests: {len(r['tested']['results'])}")
    return 0


def problems(rec):
    """(problems, notes) of one record: what is missing, and what only needs plain words or an owner."""
    p, n, g = [], [], rec["gaps"]
    sid = rec["id"]
    if not rec["found"].get("say") and "found" not in g:
        p.append(f"{sid}: no found")
    if not rec["proposed"].get("say") and "proposed" not in g:
        p.append(f"{sid}: no proposed")
    ap = rec.get("approval")
    if not ap and "approval" not in g:
        p.append(f"{sid}: no approval")
    if ap and ap["state"] == "approved" and not rec["done"]["commits"] and "done" not in g:
        p.append(f"{sid}: approved but no done commit and no gap")
    got = {r["rung"] for r in rec["tested"]["results"]}
    for rung in rec["proposed"].get("closes_by", []):
        if rung not in got and "tested" not in g and f"tested:{rung}" not in g:
            p.append(f"{sid}: no tested result for {rung}")
    if ap and ap["state"] == "assumed":
        n.append(f"{sid}: assumed by {ap['by']}, an open topic for the owner")
    texts = [("found", rec["found"].get("say")), ("proposed", rec["proposed"].get("say"))]
    texts += [(f"done {c['sha']}", c["say"]) for c in rec["done"]["commits"]] + [(f"tested {t['rung']}", t["say"]) for t in rec["tested"]["results"]]
    for lab, t in texts:
        if t and not plain(t):
            n.append(f"{sid}: needs plain words in {lab}")
    return p, n


def decision_rows(text):
    """{base D id: (title, [S-n named in its rows])} from the AGENT-DECISIONS.md table; D71b belongs to D71."""
    out = {}
    for ln in (text or "").splitlines():
        if not ln.startswith("|"):
            continue
        c = [x.strip() for x in ln.strip().strip("|").split("|")]
        m = re.match(r"^(D\d+)[a-z]?\b", c[0]) if c else None
        if not m or len(c) < 2:
            continue
        title, ids = out.setdefault(m.group(1), [None, []])
        if title is None:
            out[m.group(1)][0] = re.sub(r"\s*\((agent|OPEN)[^)]*\)\s*", " ", c[1]).strip() or c[1]
        ids += re.findall(r"\bS-\d+\b", ln)
    return out


def find_decisions(a):
    """AGENT-DECISIONS.md given, in the work folder or in its parent; None when there is none."""
    for p in ([a.decisions] if a.decisions else [os.path.join(a.work, "AGENT-DECISIONS.md"), os.path.join(os.path.dirname(a.work), "AGENT-DECISIONS.md")]):
        if os.path.isfile(p):
            return open(p, encoding="utf-8").read()
    if a.decisions:
        die(f"no decisions file {a.decisions}")
    return None


# ---- choice or log: which D row of AGENT-DECISIONS.md is a step the owner must see (steps/decide.md) --------------------------
CHOICE_VERB = re.compile(r"\s*(KEEP|UPDATE|REMOVE|DROP|REPLACE|SWITCH|REBUILD|BRIDGE|SKIP|ACCEPT)\b")
CHOICE_OPTIONS = re.compile(r"\bOptions?:|\(1\)|\(a\)")
CHOICE_USERS = re.compile(r"VISIBLE UI CHANGE|what users see|\b(SSO|login page|sign-in page)\b|\bGallery\b|\bbutton is gone\b", re.I)
CHOICE_WORDS = re.compile(r"instead of|\bchose\b|\bchosen\b|rather than|\bpolicy\b", re.I)
CHOICE_CHANGE = re.compile(r"rebuilt|replaced|removed|\bswitch", re.I)
LOG_TESTSIDE = re.compile(r"test[- ]side|stand-in|\brung\b|journey|journeys|\bgate\b|evidence|\bheal\b|mishap|incident", re.I)


def is_choice(title, choice="", rows=()):
    """True when a D row is a choice: the agent picked between real alternatives that change what the app does, what users see
    or what it costs. Everything else (a finding, a tool error, a mishap, a routine bump, a retry, an observation) is a log."""
    first = clean(title)
    text = first + " " + clean(choice)
    more = " ".join(rows)
    flagged = bool(re.match(r"(OPEN|PROPOSAL)\b", first)) or any(re.search(r"\bOPEN\b", " ".join((x.split(" | ") + ["", ""])[:2])) for x in rows)
    if re.match(r"PROPOSAL\b", first) or CHOICE_VERB.match(choice or "") or re.search(r"VISIBLE UI CHANGE|\bpolicy\b", text + " " + more):
        return True
    if re.match(r"\s*Options?:", choice or "") and not LOG_TESTSIDE.search(first):   # the row itself opens with its alternatives
        return True
    if LOG_TESTSIDE.search(first):
        return False
    if CHOICE_USERS.search(text):
        return True
    return (flagged and bool(CHOICE_OPTIONS.search(text + " " + more) or CHOICE_CHANGE.search(text))) or bool(CHOICE_WORDS.search(text))


def cmd_kind(a):
    """Prints choice or log for one D row (the agent asks this before it opens a step for a decision)."""
    print("choice" if is_choice(a.title, a.choice or "", ()) else "log")
    return 0



def cmd_check(a):
    """Step-content completeness (plan section 4) and the D rows of AGENT-DECISIONS.md; exit 1 when something is missing."""
    allp = []
    recs0 = fold(events(a.work))
    have = {r["id"] for r in recs0}
    held = {d for r in recs0 for d in (r["proposed"].get("decisions") or [])}   # a step that lists the D id holds the row (import-legacy)
    for d, (title, ids) in sorted(decision_rows(find_decisions(a)).items(), key=lambda kv: int(kv[0][1:])):
        if not ids and d in held:
            continue
        if not ids:
            allp.append(f"{d}: the agent decided \"{clean(title)}\" but no step holds it, so the owner never sees it as a topic. "
                        f"Open one with steps.py propose --new and write its S-n in the row.")
        elif not any(i in have for i in ids):
            allp.append(f"{d}: the row names {ids[0]}, but there is no such step in this run")
    for rec in fold(events(a.work)):
        p, n = problems(rec)
        allp += p
        for x in n:
            print(f"note: {x}")
    for x in allp:
        print(f"MISSING {x}")
    if not allp:
        print("steps: complete")
    return 1 if allp else 0


def trail_report(work, decisions_text):
    """(gaps, notes, nsteps) of the rung trail, each line in plain words for a person. A test counts when the step holds a passing or
    failing result for the rung, or a gap that somebody other than the gate wrote on purpose (the gate's own "did not run" and "no
    check is linked" gaps are what the rung exists to show)."""
    evs = events(work)
    recs, lm = fold(evs), lastmap(evs)
    gaps, notes = [], []
    held = {d for r in recs for d in (r["proposed"].get("decisions") or [])}
    have = {r["id"] for r in recs}
    for d, (title, ids) in sorted(decision_rows(decisions_text).items(), key=lambda kv: int(kv[0][1:])):
        if not ids and d not in held:
            gaps.append(f"Decision {d} (\"{clean(title)[:70]}\") belongs to no step.")
        elif ids and not any(i in have for i in ids):
            gaps.append(f"Decision {d} names {ids[0]}, which is not a step of this run.")
    for r in recs:
        sid, g = r["id"], r["gaps"]
        ap = r.get("approval")
        tag = f"{sid} ({clean(r['title'])[:50]})"

        def written(field):   # a gap on this field that the gate did not write by itself
            return any(k == f"gap:{field}" and lm[sid][k]["by"] != "gate" for k in lm[sid])
        if not r["proposed"].get("say") and "proposed" not in g:
            gaps.append(f"{tag} has no proposal.")
        if not ap and "approval" not in g:
            gaps.append(f"{tag} has no approval.")
        if ap and ap["state"] == "assumed":
            notes.append(f"{tag} is assumed by {ap['by']} and waits for the owner's OK.")
        if ap and ap["state"] in ("approved", "assumed") and not r["done"]["commits"] and "done" not in g:
            gaps.append(f"{tag} has no change recorded and no note that none was needed.")
        got = {t["rung"] for t in r["tested"]["results"] if t["verdict"] in ("PASS", "PASS*", "FAIL")}
        rungs = r["proposed"].get("closes_by") or []
        for rung in rungs:
            if rung not in got and not written("tested") and not written(f"tested:{rung}"):
                gaps.append(f"{tag} has no test result for the {RUNG_PLAIN.get(rung, rung)} (it did not run, or could not judge).")
        if not rungs and not got and not written("tested"):
            gaps.append(f"{tag} has no check linked to it and no note why.")
    return gaps, notes, len(recs)


def cmd_trail(a):
    """Plain-words completeness of the step records. The last line is the one-line summary for the gate summary."""
    if not os.path.isfile(path_of(a.work)):
        print("trail: no step records in this run")
        return 1
    gaps, notes, n = trail_report(a.work, find_decisions(a))
    for x in notes:
        print(f"note: {x}")
    for x in gaps:
        print(f"GAP {x}")
    if not gaps:
        print(f"trail: complete, {n} steps" + (f"; {len(notes)} assumed by the agent, waiting for the owner's OK" if notes else ""))
        return 0
    print(f"trail: {len(gaps)} gap(s) in {n} steps. First: {gaps[0]}" + (f" {len(notes)} step(s) wait for the owner's OK." if notes else ""))
    return 1


# ---- import-legacy ---------------------------------------------------------------------------------------------------------
NOT_LINKED = "This is not linked in this run."
LEGACY = "legacy"


def plainify(text, fallback):
    """The text when it is plain words, else without its parentheses, else the fallback."""
    s = clean(text or "")
    for c in (s, re.sub(r"\s*\([^)]*\)", "", s).strip(" ;,"), re.sub(r"\s*\[[^\]]*\]", "", s).strip(" ;,")):
        if c and plain(c) and not TECH.search(c) and len(c) < 400:
            return c.rstrip(".") + "."
    return fallback


def read_text(*paths):
    """The first file that exists, as text; None when none does."""
    for p in paths:
        if p and os.path.isfile(p):
            return open(p, encoding="utf-8").read()
    return None


def legacy_ensure(work, topic, title, fields):
    """Like ensure(), but a field that another writer set (no source legacy) is kept. Returns the S-n id."""
    evs = events(work)
    sid = next((r["id"] for r in fold(evs) if r["topic"] == topic and r["title"] == title), None)
    if sid is None:
        sid = f"S-{max([idnum(e['id']) for e in evs] + [0]) + 1}"
        append(work, sid, "topic", topic, LEGACY)
        append(work, sid, "title", title, LEGACY)
    cur = lastmap(events(work)).get(sid, {})
    for f, v in fields.items():
        if v is None or v == [] or v == "":
            continue
        if f in cur and (cur[f]["value"] == v or cur[f].get("source") != LEGACY):
            continue
        append(work, sid, f, v, LEGACY)
    return sid


def legacy_approval(work, sid, state, by, **extra):
    """Write an approval unless one stands: a person's or the toolkit's answer is never overwritten, a legacy one only when it differs."""
    cur = lastmap(events(work)).get(sid, {}).get("approval")
    if cur and cur["value"].get("source") != LEGACY:
        return
    if cur and cur["value"].get("state") == state and cur["by"] == by:
        return
    append(work, sid, "approval", dict({"state": state, "source": LEGACY}, **extra), by)


def legacy_gap(work, sid, field, say):
    """Write a gap once; a rerun adds nothing."""
    if f"gap:{field}" not in lastmap(events(work)).get(sid, {}):
        append(work, sid, f"gap:{field}", say, LEGACY)


def pipe_rows(text):
    """The cells of every pipe-separated row of a text (table separator rows left out)."""
    out = []
    for ln in (text or "").splitlines():
        if "|" in ln and not re.match(r"^\s*\|?[\s:|-]+\|?\s*$", ln):
            out.append([c.strip() for c in ln.strip().strip("|").split("|")])
    return out


def agent_decisions(text):
    """{base D id: {title, choice, why, rows}}; D71a and D71b belong to D71."""
    out = {}
    for c in pipe_rows(text):
        m = re.match(r"^(D\d+)[a-z]?\b", c[0]) if c else None
        if not m or len(c) < 2:
            continue
        d = out.setdefault(m.group(1), {"title": "", "choice": "", "why": "", "rows": []})
        title = re.sub(r"\s*\((agent|OPEN)[^)]*\)\s*", " ", c[1]).strip() or c[1]
        d["title"] = d["title"] or re.sub(r"^OPEN:\s*", "", title)
        d["choice"] = d["choice"] or (c[2] if len(c) > 2 else "")
        d["why"] = d["why"] or (c[3] if len(c) > 3 else "")
        d["rows"].append(" | ".join(c))
    return out


def proposal_items(text):
    """([routine module lines], [repair lines], [{id, kind, name, evidence, options, rec, answer}], signer) from PROPOSAL.md."""
    mods, reps, items, signer = [], [], [], None
    sec, cur = 0, None
    for ln in (text or "").splitlines():
        m = re.match(r"^## (\d)\.", ln)
        if m:
            sec, cur = int(m.group(1)), None
            continue
        m = re.match(r"^Signed-off:\s*(.+?)\s+(\d{4}-\d\d-\d\d)", ln)
        if m:
            signer = m.group(1)
        if sec == 2 and ln.startswith("- "):
            (reps if ln.startswith("- predicted repair") else mods).append(ln[2:].strip())
        if sec == 3:
            m = re.match(r"^- \[(P-\d+)\] (\w+): (.+?)\s*$", ln)
            if m:
                cur = {"id": m.group(1), "kind": m.group(2), "name": m.group(3), "evidence": "", "options": "", "rec": "", "answer": ""}
                items.append(cur)
                continue
            m = re.match(r"^\s+- (evidence|options|recommendation|answer): (.*)$", ln)
            if m and cur:
                cur[{"recommendation": "rec"}.get(m.group(1), m.group(1))] = m.group(2).strip()
    return mods, reps, items, signer


def git_commits(repo):
    """[(short sha, subject, body)] of the whole history of an app repo; [] when git cannot read it."""
    import subprocess
    try:
        r = subprocess.run(["git", "-C", repo, "log", "--format=%x01%h%x02%s%x02%b"], capture_output=True, text=True, check=True)
    except (OSError, subprocess.CalledProcessError):
        return []
    return [tuple((c.split("\x02") + ["", ""])[:3]) for c in r.stdout.split("\x01")[1:]]


def topic_title(work, sid):
    """(topic, title) of a step."""
    r = next(r for r in fold(events(work)) if r["id"] == sid)
    return r["topic"], r["title"]


ROUTINE = "routine"
GENERIC = {"build", "builds", "widget", "widgets", "module", "modules", "error", "errors", "later", "after", "before", "which", "their", "there",
           "check", "checks", "rows", "journeys", "journey", "pages", "page", "client", "app", "apps", "script", "scripts",
           "update", "updates", "files", "agent", "notes", "edits", "using", "other", "kept", "cannot", "without", "should"}


def word_set(text):
    """The lower-case plain words of a text that can name a subject (5 letters or more, not a generic word)."""
    return {w for w in re.findall(r"[A-Za-z]{5,}", clean(text).lower()) if w not in GENERIC and w.rstrip("s") not in GENERIC}


TECH = re.compile(r"[A-Za-z]\.[A-Za-z]|_|\bexit\b|\bmx\b|mxbuild|javac|basewalk|\bCE\d+")


def plain_title(text, d):
    """A title a person can read, saying WHAT is chosen: a template for a known subject, the row's own words when they are short and plain,
    else "A choice about <topic>". Never a bare decision id."""
    t = re.sub(r"\s*\([^)]*\)", "", clean(text)).replace("->", "to").strip(" :;,.?")
    t = re.sub(r"^(OPEN|PROPOSAL):\s*", "", t)
    for rx, title in TITLE_TOPICS:
        if rx.search(t):
            return title
    m = re.match(r"([A-Za-z][\w]*) v?(\d[\d.x]*)(?: to (\d[\d.x]*))?$", t)
    if m:
        return f"Keep or update module {m.group(1)} ({m.group(2)}" + (f" to {m.group(3)})" if m.group(3) else ")")
    if plain(t) and len(t) <= 80 and not TECH.search(t) and not title_problem(capital(t)):
        return capital(t)
    allw = t.split()
    words = [w for w in allw if not (re.search(r"[._/\\`#]", w) or TECH.search(w) or w in ("exit", "mx"))]
    if len(words) == len(allw) and 3 <= len(words) <= 12 and plain(" ".join(words)):
        return "A choice about " + " ".join(words[:8]).rstrip(",:;").lower()
    dotted = next((w.split(".")[0] for w in t.split() if re.search(r"[._]", w) and len(w.split(".")[0]) >= 4 and re.fullmatch(r"[A-Za-z][A-Za-z_]*", w.split(".")[0])), "")
    return f"A choice about {dotted}" if dotted else "A choice made during the run"


def merge_list(work, sid, field_get, new):
    """The current list of a step field with the new items appended once each."""
    return list(dict.fromkeys(list(field_get) + [x for x in new if x]))


def host_step(work, d, text, choice=False):
    """The id of an existing step that this D row is about: its topic name or title shows in the row. A choice only joins a module,
    theme, widget or page step. None when no step fits."""
    best = (0, None)
    low = clean(text).lower()
    for r in fold(events(work)):
        if r["topic"].startswith(("decision:", "run-notes")) or (choice and not r["topic"].startswith(("module:", "theme:", "widget:", "page:"))):
            continue
        names = {r["title"], r["topic"].split(":", 1)[-1]}
        score = max([len(n) for n in names if len(n) >= 4 and re.search(r"(?<![a-z0-9_])" + re.escape(n.lower()) + r"(?![a-z0-9_])", low)] + [0])
        if not score:
            continue
        if score > best[0]:
            best = (score, r["id"])
    return best[1]


def cmd_import_legacy(a):
    """Build steps.jsonl for a run made before step records existed (see the module docstring)."""
    global EVENT_SOURCE
    EVENT_SOURCE = LEGACY
    W = a.work
    touched, claimed = [], set()

    def jd(n):
        p = os.path.join(W, n)
        return json.load(open(p, encoding="utf-8")) if os.path.isfile(p) else {}
    try:
        items, trail = jd("cockpit-items.json").get("items", {}), jd("cockpit-trail.json").get("rows", {})
    except ValueError as e:
        die(f"cannot read the cockpit files: {e}")
    mods, reps, p_items, signer = proposal_items(read_text(os.path.join(W, "PROPOSAL.md")))
    drows = pipe_rows(read_text(os.path.join(W, "DECISIONS.md")))
    ad = agent_decisions(find_decisions(a))
    commits = git_commits(a.app) if a.app else []

    def keep(sid):
        if sid not in touched:
            touched.append(sid)
        return sid

    def routine_ok(sid):
        """A routine step needs nobody's OK: approved by the agent, source routine."""
        cur = lastmap(events(W)).get(sid, {}).get("approval")
        if not cur:
            append(W, sid, "approval", {"state": "approved", "source": ROUTINE, "needs": "nobody: routine work"}, "agent")

    def link_commits(sid, text, ds):
        """A commit belongs to a step when it names one of the step's D rows or its short hash is in the step's own text."""
        for sha, subj, body in commits:
            if any(re.search(rf"\b{d}\b", subj + " " + body) for d in ds) or (sha and sha in text):
                add_commit(W, sid, sha, subj if plain(subj) else "A change was committed for this step.", LEGACY)

    # 1. PROPOSAL.md: the routine updates, then each [P-n] item (same topic and title as proposal.py, so a later run merges)
    for topic, title, lines, what, prop_say in (
            ("modules", "Routine module updates", mods, ("module update", "module updates"),
             "Update these modules to the versions that fit the new Mendix version."),
            ("repairs", "Predicted repairs", reps, ("repair", "repairs"), "Make these repairs during the upgrade, as the repair table describes.")):
        if lines:
            sid = keep(legacy_ensure(W, topic, title, {
                "found_say": f"The plan holds {len(lines)} {what[len(lines) != 1]} that the toolkit does on its own.", "stage": "triage",
                "evidence": lines, "proposed_say": prop_say,
                "why": "Routine work with a known result. It is approved with the sign-off of the plan."}))
            if signer:
                legacy_approval(W, sid, "approved", signer)
            else:
                routine_ok(sid)   # routine work with a known result is assumed to be fine; nobody has to press a button
    pid = {}
    for it in p_items:
        opts = [plainify(o, "see the proposal for this option").rstrip(".") for o in it["options"].split(" | ") if o.strip()]
        rec = re.sub(r"\s*\[RA-\d+[^\]]*\]", "", it["rec"])
        pick = next((i for i, o in enumerate(opts) if o.split(" (")[0].lower() in rec.lower()), None)
        name = plainify(it["name"], "").rstrip(".")
        sid = keep(legacy_ensure(W, f"{it['kind']}:{it['name']}", item_title(it["kind"], it["name"]), {
            "alias": it["id"], "found_say": f"A {it['kind']}{(' (' + name + ')') if name else ''} needed a decision before the upgrade started.",
            "stage": "triage", "evidence": [it["evidence"]] if it["evidence"] else None,
            "proposed_say": "The toolkit recommended: " + plainify(rec.split(";")[0], "the first option in the proposal"),
            "options": opts, "recommend": pick}))
        pid[it["id"]] = sid
        if "ASSUMED" in it["answer"]:
            legacy_approval(W, sid, "assumed", "agent", needs="the owner's OK")

    # 2. DECISIONS.md rows: a P-n row answers its item; an S-n row (a stuck item of the older kind) is a step of its own
    for c in drows:
        if len(c) < 7 or not re.match(r"^[PS]-\d+$", c[0]) or c[0] == "P-0":
            continue
        rid, item, kind, choice, why, who, status = c[:7]
        ds = sorted(set(re.findall(r"\bD\d+\b", why + " " + choice)))
        if rid.startswith("P-"):
            sid = pid.get(rid)
            if sid is None:
                continue
            if ds:
                legacy_ensure(W, *topic_title(W, sid), {"decisions": ds})
        else:
            short = clean(item.split(" (")[0])[:120]
            sid = keep(legacy_ensure(W, f"{kind}:{short}", short, {
                "found_say": plainify(item, "A stuck item was listed in this run."), "stage": "triage", "evidence": [item],
                "proposed_say": plainify(choice, "See the decision list of this run for what was chosen."),
                "why": plainify(why.split("(")[0], "") if why else None, "decisions": ds}))
        claimed.update(ds)
        if status.startswith("CONFIRMED") and who not in ("", "-"):
            legacy_approval(W, sid, "approved", who)
        elif status.startswith("ASSUMED"):
            legacy_approval(W, sid, "assumed", "agent", needs="the owner's OK")

    # 3. cockpit items and trail rows: a trail action is a step under its item key; an item without trail rows is a step itself
    for key, it in items.items():
        if not it.get("name"):
            continue
        cells = it.get("cells", {})
        ds = [d for d in it.get("decisions", []) if re.fullmatch(r"D\d+", d)]
        claimed.update(ds)
        plan_you = (cells.get("plan") or {}).get("status") == "you"
        result = plainify(it.get("result", ""), "")
        for act in trail.get(key) or [None]:
            st = (act or {}).get("stages", {})
            plan = st.get("plan") or {}
            tri = (cells.get("triage") or {}).get("steps") or [""]
            sid = keep(legacy_ensure(W, key, (act or {}).get("name") or it["name"], {
                "found_say": plainify((st.get("triage") or {}).get("say") or it.get("problem") or tri[0], "A problem was found here during triage."),
                "stage": "triage", "proposed_say": plainify(plan.get("say") or it.get("proposal"), ""),
                "why": plainify(plan.get("why"), "") if plan.get("why") else None,
                "options": [plainify(o, "see the run notes for this option").rstrip(".") for o in plan.get("options", [])] or None,
                "decisions": ds or None}))
            if plan_you or any(is_choice(ad[d]["title"], ad[d]["choice"], ad[d]["rows"]) for d in ds if d in ad):
                legacy_approval(W, sid, "assumed", "agent", needs="the owner's OK")
            else:
                routine_ok(sid)
            if commits:
                link_commits(sid, json.dumps(st.get("upgrade") or {}, ensure_ascii=False), ds)
            said = plainify((st.get("test") or {}).get("say"), "") or result
            legacy_gap(W, sid, "tested", NOT_LINKED + " No test result of this run is tied to a check of the gate."
                       + (f" The run's own note says: {said}" if said else ""))

    # 4. D rows no other step holds. A choice is a step the owner must see; a log is evidence on the step it is about, or on one
    #    rolled-up step for the whole run. Its approval is "approved" by the agent (source routine), so it never becomes an open topic.
    for d, row in sorted(ad.items(), key=lambda kv: int(kv[0][1:])):
        if d in claimed:
            continue
        text = row["title"][:120]   # the host and the subject come from the title only; the long text is evidence
        choice = is_choice(row["title"], row["choice"], row["rows"])
        host = host_step(W, d, text, choice)
        if host is None and choice:
            # the same subject is the same step: share a word with an earlier choice step of this import
            ws = word_set(row["title"][:120] + " " + row["choice"][:300])
            host = next((r["id"] for r in fold(events(W)) if (r.get("approval") or {}).get("state") == "assumed"
                         and not r["topic"].startswith(("module:", "theme:")) and ws & word_set(r["title"])), None)
        if host is None and not choice:
            sid = keep(legacy_ensure(W, "run-notes", "Notes the agent kept during the run", {
                "found_say": "The agent kept notes of findings, tool problems, retries and results while it worked. None of them is a choice.",
                "stage": "run", "proposed_say": "Nothing to decide. The notes stay as evidence.", "why": "A note changes nothing in the app by itself."}))
            routine_ok(sid)
            legacy_gap(W, sid, "done", "These are notes only, so no change in the app is tied to this step.")
            legacy_gap(W, sid, "tested", "These are notes only, so no check of the gate is tied to this step.")
            host = sid
        if host is None:
            host = keep(legacy_ensure(W, f"decision:{d}", plain_title(row["title"], d), {
                "found_say": plainify(row["title"], "During the run the agent met a point with more than one way to go."), "stage": "run",
                "proposed_say": plainify(row["choice"], "The agent picked one way on its own. The full row is in the evidence."),
                "why": plainify(row["why"], "") if row["why"] else None}))
        cur = next(r for r in fold(events(W)) if r["id"] == host)
        legacy_ensure(W, cur["topic"], cur["title"], {
            "decisions": merge_list(W, host, cur["proposed"].get("decisions") or [], [d]),
            "evidence": merge_list(W, host, cur["found"].get("evidence") or [], row["rows"])})
        keep(host)
        if choice and (not cur.get("approval") or cur["approval"].get("source") == ROUTINE):
            append(W, host, "approval", {"state": "assumed", "source": LEGACY, "needs": "the owner's OK"}, "agent")
        elif not choice and not cur.get("approval"):
            routine_ok(host)
        if commits:
            link_commits(host, "", [d])

    # 5. everything that could not be linked is a gap, in plain words
    for sid in touched:
        r = next(r for r in fold(events(W)) if r["id"] == sid)
        if not r["proposed"].get("say"):
            legacy_gap(W, sid, "proposed", NOT_LINKED + " No proposal was written down for this step.")
        if not r.get("approval"):
            legacy_gap(W, sid, "approval", NOT_LINKED + " Nobody's answer is written down for this step.")
        if not r["done"]["commits"]:
            legacy_gap(W, sid, "done", NOT_LINKED + " No change in the app is tied to this step.")
        if not r["tested"]["results"]:
            legacy_gap(W, sid, "tested", NOT_LINKED + " No test result is tied to this step.")
    recs = fold(events(W))
    n_as = sum(1 for r in recs if (r.get("approval") or {}).get("state") == "assumed")
    print(f"steps: import-legacy: {len(recs)} steps ({n_as} assumed by the agent, waiting for the owner's OK)")
    return 0


def main():
    """Parse the command line and run one command."""
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    for n in ("open", "propose", "approve", "done", "tested", "gap", "show", "check", "find", "trailer", "trail", "import-legacy", "kind"):
        s = sub.add_parser(n)
        s.add_argument("--work", required=(n not in ("trailer", "kind")))
        if n != "approve":
            s.add_argument("--by", default=os.environ.get("USER", "agent"))
        if n == "tested":
            s.add_argument("--id")
            s.add_argument("--gate")
            s.add_argument("--summary")   # a gate-summary.md to read instead of GATE_DIR's (the gate's own trail rung, before the summary exists)
        elif n not in ("open", "show", "check", "find", "propose", "trailer", "trail", "import-legacy", "kind"):
            s.add_argument("--id", required=True)
        if n == "kind":
            s.add_argument("--title", required=True)
            s.add_argument("--choice")
        if n == "trailer":
            s.add_argument("--kind", required=True)
        if n == "find":
            s.add_argument("--id")
            s.add_argument("--topic")
        if n in ("check", "trail", "import-legacy"):
            s.add_argument("--decisions")
        if n == "import-legacy":
            s.add_argument("--app")
        if n == "open":
            s.add_argument("--topic", required=True)
            s.add_argument("--title", required=True)
            s.add_argument("--say", required=True)
            s.add_argument("--stage")
            s.add_argument("--alias")
            s.add_argument("--evidence", action="append")
        if n == "propose":
            s.add_argument("--id")
            s.add_argument("--new", action="store_true")
            s.add_argument("--topic")
            s.add_argument("--title")
            s.add_argument("--found")
            s.add_argument("--stage")
            s.add_argument("--say")
            s.add_argument("--why")
            s.add_argument("--option", action="append")
            s.add_argument("--recommend", type=int)
            s.add_argument("--closes-by", dest="closes_by", action="append")
            s.add_argument("--decision", action="append")
        if n == "approve":
            s.add_argument("--state", required=True)
            s.add_argument("--by", required=True)
            s.add_argument("--source")
        if n == "done":
            s.add_argument("--commit", required=True)
            s.add_argument("--say", required=True)
        if n == "tested":
            s.add_argument("--rung")
            s.add_argument("--verdict")
            s.add_argument("--say")
            s.add_argument("--proof", action="append")
        if n == "gap":
            s.add_argument("--field", required=True)
            s.add_argument("--say", required=True)
        if n == "show":
            s.add_argument("sid", nargs="?")
            s.add_argument("--json", action="store_true")
    a = ap.parse_args()
    if a.cmd == "kind":
        return cmd_kind(a)
    if a.cmd == "trailer":
        a.work = os.path.abspath(a.work) if a.work else ""
        return cmd_trailer(a)
    a.work = os.path.abspath(a.work)
    if not os.path.isdir(a.work):
        die(f"no work folder {a.work}")
    return {"open": cmd_open, "propose": cmd_propose, "approve": cmd_approve, "done": cmd_done, "tested": cmd_tested,
            "gap": cmd_gap, "show": cmd_show, "check": cmd_check, "find": cmd_find, "trail": cmd_trail,
            "import-legacy": cmd_import_legacy}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
