#!/usr/bin/env python3
"""Controls for bin/journeys_progress.py (issue 26). The runner is a stand-in that prints the engine's real marker lines
("=== JOURNEY <id>", the shape journey-runner.js prints) slowly enough for the poll to see them; the clock is a fake one so no test waits.
  journeys_progress_control.py CASE
"""
import io, json, os, sys, tempfile
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "bin"))
import journeys_progress as jp


class Clock:
    def __init__(self): self.t = 1000.0
    def __call__(self): return self.t


def mk(total, pace_rows=None, clock=None):
    d = tempfile.mkdtemp()
    pace = os.path.join(d, "pace.tsv")
    if pace_rows:
        open(pace, "w").write("".join(f"{a}\t{b}\t{c}\n" for a, b, c in pace_rows))
    err = io.StringIO()
    return jp.Progress("new", total, os.path.join(d, "p.json"), os.path.join(d, "step.log"), pace, clock or Clock(), err), d, err


def case(name):
    if name == "start-unknown":        # no earlier run: "unknown", never a guess
        p, d, e = mk(435); p.start(); print(e.getvalue().strip())
    elif name == "start-known":        # an earlier run: 40 paths in 2400 s = 60 s each; 435 paths -> 435 min
        p, d, e = mk(435, [("old", 40, 2400)]); p.start(); print(e.getvalue().strip())
    elif name == "pace-ignores-tiny":  # a run of 1 or 2 paths says nothing about pace
        p, d, e = mk(435, [("old", 2, 900)]); p.start(); print(e.getvalue().strip())
    elif name == "ticks":              # 212 of 435 at 4 s each so far: a line every 25 paths, the last says about 15 min left
        c = Clock(); p, d, e = mk(435, clock=c); p.start(); p.begin_batch()
        for i in range(213):
            c.t += 4; p.seen(1)
        print("\n".join(e.getvalue().strip().splitlines()[-2:]))
        print("lines: %d" % len(e.getvalue().strip().splitlines()))
        print("log: " + open(os.path.join(d, "step.log")).read().strip().splitlines()[-1])
        print("state: " + json.dumps({k: json.load(open(os.path.join(d, "p.json")))[k] for k in ("done", "total", "left_min", "finished")}))
    elif name == "by-minute":          # slow paths: one line a minute even when 25 paths are far away
        c = Clock(); p, d, e = mk(435, clock=c); p.start(); p.begin_batch()
        for i in range(8):
            c.t += 20; p.seen(1)
        print("lines after 160 s: %d" % (len(e.getvalue().strip().splitlines()) - 1))
    elif name == "finish-keeps-pace":  # the run ends: its pace is kept for the next run's start line
        c = Clock(); p, d, e = mk(10, clock=c); p.start(); p.begin_batch()
        for i in range(10):
            c.t += 6; p.seen(1)
        p.end_batch(); p.finish(10)
        print("pace row: " + open(os.path.join(d, "pace.tsv")).read().strip())
        print("finished: %s" % json.load(open(os.path.join(d, "p.json")))["finished"])
        q = jp.Progress("new", 100, None, None, os.path.join(d, "pace.tsv"), c, io.StringIO()); print("next start: about %d min" % round(100 * q.earlier / 60))
    elif name == "walk-counts":        # a real child process, real files: 6 journeys in two batches of 3, counted while it runs
        d = tempfile.mkdtemp()
        script = "import sys,time\nfor i in range(3):\n  print('=== JOURNEY J%d' % i, flush=True); print('ok'); time.sleep(0.6)\n"
        c = Clock(); p, _, e = mk(6, clock=c); p.start()
        for b in range(2):
            rc, out, err = jp.walk([sys.executable, "-c", script], os.environ.copy(), d, p, d, poll=0.2)
            print("batch %d rc=%d journeys in output=%d" % (b, rc, out.count("=== JOURNEY")))
        print("done=%d" % p.done)
        print("live files left: %d" % len([f for f in os.listdir(d) if f.startswith(".live")]))
    elif name == "read-line":
        p, d, e = mk(435); p.done = 212; p._write(40)
        os.system("python3 %s read %s" % (os.path.join(os.path.dirname(jp.__file__), "journeys_progress.py"), p.state_file))
    elif name == "read-over":
        p, d, e = mk(435); p.done = 435; p.finish(435); print("[%s]" % os.popen("python3 %s read %s" % (jp.__file__, p.state_file)).read().strip())
    else:
        print("no case " + name); return 2


sys.exit(case(sys.argv[1]) or 0)
