#!/usr/bin/env python3
"""brief.py: the cockpit's top, in the terminal. One answer to "what do I do next?", in plain words.

  brief.py --work W [--json]      (or: upgrade-pipeline.sh --work W --brief)

Built from the SAME model and the SAME wording as the top of COCKPIT.html (cockpitpage.build_model, then the brief() of
cockpitmatrix.py): this file only lays the lines out for an 80-column terminal, it words nothing itself. Five lines, then the
open questions (decisions.py pending, same list the page shows). No colours. Printed by upgrade-pipeline.sh at every stop and at
the end of a run. The producer of the work folder is the pipeline (every step regenerates the page); nothing here writes a file.
Exit: 0, 2 usage.
"""
import argparse, json, os, re, sys, textwrap

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cockpitpage  # noqa: E402
import cockpitmatrix  # noqa: E402
import decisions  # noqa: E402

WIDTH = 78
LABELS = (("status", ""), ("broken", "Broken for your users: "), ("unmeasured", "Not measured yet: "),
          ("act", "Do this now: "), ("who", "Who changed what: "))


def fields(work):
    """The brief as plain strings, taken from the page model: {status, broken, unmeasured, act, who, questions: [...]}."""
    model = cockpitpage.build_model(work)
    b = cockpitmatrix.build(work, model)["brief"]
    a = b["act"]
    act = " ".join(x for x in (a["text"], a.get("rec"), a.get("time")) if x)
    return {"act_parts": [x for x in (a["text"], a.get("rec")) if x], "status": b["status"], "broken": b["broken"]["text"], "unmeasured": b["unmeasured"] or "nothing; every check has run.", "act": act,
            "who": b["who"], "n": b["n"], "kind": a["kind"]}


def sentences(t):
    return re.findall(r".+?(?:[.!?](?=\s|$)|$)", t or "")


def fit(label, text, room, tail=False):
    """Whole sentences of the page's own text that fit in `room` lines: from the start, or from the end (tail) so the newest
    fact stays. Never other words. A single sentence longer than the room is cut at a word with an ellipsis."""
    ss = [x.strip() for x in sentences(text) if x.strip()]
    pick = []
    for x in (reversed(ss) if tail else ss):
        cand = ([x] + pick) if tail else (pick + [x])
        if len(textwrap.wrap(label + " ".join(cand), WIDTH, subsequent_indent="  ", break_long_words=False)) > room:
            break
        pick = cand
    if not pick:
        w = textwrap.wrap(label + (ss[-1] if tail else ss[0]) if ss else label, WIDTH, subsequent_indent="  ", break_long_words=False)
        return w[:room - 1] + [w[room - 1].rstrip(" .,;:") + " ..."] if len(w) > room else w
    return textwrap.wrap(label + " ".join(pick), WIDTH, subsequent_indent="  ", break_long_words=False)


MAX_LINES = 8


def lines(f):
    """Each field in its own labelled line(s); about 8 lines in all: the status and the action keep their room, the rest shrinks first."""
    texts = {"status": f["status"], "broken": f["broken"], "unmeasured": f["unmeasured"], "act": " ".join(x if x[-1] in ".!?" else x + "." for x in f["act_parts"]), "who": f["who"]}
    room = {"status": 2, "broken": 2, "unmeasured": 2, "act": 3 if f.get("kind") == "handoff" else 2, "who": 2}   # a hand-off says why and what it needs: no room for one without the other
    for shrink in (None, "unmeasured", "who", "broken"):
        if shrink:
            room[shrink] = 1
        out = [l for key, label in LABELS for l in fit(label, texts[key], room[key], tail=(key == "who"))]
        if len(out) <= MAX_LINES:
            break
    return out


def pending(work):
    """decisions.py pending, in the same words (its own output, so the chat and the terminal never differ)."""
    import io, contextlib
    class A:  # the namespace cmd_pending reads
        pass
    a = A(); a.work = work; a.json = False
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        decisions.cmd_pending(a)
    return buf.getvalue().rstrip()


def render(work):
    f = fields(work)
    n = len(decisions.open_items(work))   # the question count of `decisions.py pending`, the list the page and the chat share
    out = lines(f) + [""]
    if not n:
        out.append("Open questions: 0. Nothing waits for you.")
    elif not f["n"]:   # the run does not wait for them: the AI took its recommended choice, a person may review or change it
        out.append(f"Open questions: {n}. None holds the run up: the AI took its recommended choice. Review or change them on the "
                   f"cockpit page, or list them with: decisions.py pending --work {work}")
        out = out[:-1] + textwrap.wrap(out[-1], WIDTH, subsequent_indent="  ", break_long_words=False)
    else:
        own = sum(1 for i in decisions.open_items(work) if i.get("unattended"))
        # the same number as the status sentence above (the questions that wait for a person); the AI's own choices are counted apart
        out.append(f"Open questions: {f['n']}. Answer them here or on the cockpit page."
                   + (f" {n - f['n']} more are the AI's own choices, or confirmations; review is optional." if n > f["n"] else ""))
        out.append("\n".join(pending(work).splitlines()[1:]).strip())   # the first line is its own count
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--work", required=True)
    ap.add_argument("--json", action="store_true", help="the five fields, for the controls")
    a = ap.parse_args()
    w = os.path.abspath(a.work)
    if not os.path.isdir(w):
        print(f"brief: no work folder {w}", file=sys.stderr)
        return 2
    if a.json:
        print(json.dumps(fields(w), indent=1))
    else:
        print(render(w))
    return 0


if __name__ == "__main__":
    sys.exit(main())
