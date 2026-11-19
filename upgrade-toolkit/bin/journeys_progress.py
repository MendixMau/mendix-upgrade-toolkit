#!/usr/bin/env python3
"""journeys_progress.py: a progress line for the journeys step ("212 of 435 user paths done, about 40 min left"), so a slow run is not
mistaken for a hung one (issue 26, SNOW: 435 user paths on the old app ran past 90 min with no output and a worker killed it).

Producer: bin/run_journeys.py (the journeys and basewalk steps of the pipeline both call it). It walks a role's journeys in one runner
process whose stdout names each journey it starts ("=== JOURNEY <id>"); `walk()` runs that process, counts those lines while it runs,
and says the progress: to stderr (the step's .out file), to the step log ($UPG_PROGRESS_LOG, the pipeline sets it), and to a state file
($UPG_PROGRESS_FILE, state/journeys-progress.json) which the cockpit page and the terminal brief read.
No verdict depends on any of this: a progress line is only said, never judged.

Pace: seconds per user path, kept in $UPG_PACE_FILE (state/journeys-pace.tsv: label, paths, seconds; one row per finished run, so the
second run of an app knows how long the first took). With no row the expected duration is "unknown": it is never guessed.

  journeys_progress.py read STATE_FILE        print the line the brief shows ("Testing now: 212 of 435 user paths done, about 40 min left")
Exit: 0, 2 usage.
"""
import json, os, subprocess, sys, time

EVERY_PATHS = 25      # a line after this many more paths ...
EVERY_SECONDS = 60    # ... or after this many seconds, whichever comes first
MARK = "=== JOURNEY "


def say_line(done, total, left_min):
    """The words, one place: the step log, the terminal and the page all quote this."""
    t = f"{done} of {total} user paths done"
    if left_min is None:
        return t + ", time left unknown"
    if left_min < 1:
        return t + ", less than a minute left"
    return t + f", about {left_min} min left"


def pace_of(path):
    """Seconds per user path over the earlier finished runs in this work folder; None when there is none."""
    n = s = 0
    try:
        for ln in open(path):
            p = ln.rstrip("\n").split("\t")
            if len(p) >= 3 and p[1].isdigit() and p[2].replace(".", "", 1).isdigit() and int(p[1]) >= 3:
                n += int(p[1]); s += float(p[2])
    except OSError:
        return None
    return (s / n) if n else None


class Progress:
    def __init__(self, label, total, state_file=None, step_log=None, pace_file=None, clock=time.time, err=sys.stderr):
        self.label, self.total, self.state_file, self.step_log, self.pace_file = label, total, state_file, step_log, pace_file
        self.clock, self.err = clock, err
        self.done = 0
        self.base = self.started = 0   # paths finished in earlier batches; paths the running batch has started (the last of them is still running)
        self.t0 = self.last_t = self.clock()
        self.last_done = 0
        self.earlier = pace_of(pace_file) if pace_file else None

    def _left(self):
        """Minutes left: the pace of this run once it has walked 5 paths, before that the earlier runs' pace, else None."""
        el = self.clock() - self.t0
        pace = (el / self.done) if self.done >= 5 else self.earlier
        return None if pace is None else int(round((self.total - self.done) * pace / 60))

    def _say(self, text):
        print("progress: " + text, file=self.err, flush=True)
        if self.step_log:
            try:
                with open(self.step_log, "a") as f:
                    f.write("progress: " + text + "\n")
            except OSError:
                pass

    def _write(self, left, started=False):
        if not self.state_file:
            return
        d = {"label": self.label, "done": self.done, "total": self.total, "left_min": left, "started": int(self.t0),
             "updated": int(self.clock()), "finished": False}
        try:
            os.makedirs(os.path.dirname(self.state_file) or ".", exist_ok=True)
            tmp = self.state_file + ".tmp"
            json.dump(d, open(tmp, "w")); os.replace(tmp, self.state_file)
        except OSError:
            pass

    def start(self):
        """The expected duration, before the first path: from the count and the earlier runs' pace, else "unknown"."""
        if self.earlier is None:
            self._say(f"{self.total} user paths to walk. Expected duration: unknown (no earlier run here to measure it from).")
        else:
            m = int(round(self.total * self.earlier / 60))
            self._say(f"{self.total} user paths to walk. Expected duration: about {m} min (earlier runs here: {self.earlier:.0f} s per path).")
        self._write(self._left())

    def begin_batch(self):
        self.started = 0

    def end_batch(self):
        self.base += self.started
        self.started = 0
        self.done = min(self.total, self.base)

    def seen(self, n_more):
        self.started += n_more
        self.done = min(self.total, self.base + max(0, self.started - 1))   # the newest one has begun, not ended
        now = self.clock()
        if self.done - self.last_done >= EVERY_PATHS or now - self.last_t >= EVERY_SECONDS:
            self.tick()

    def tick(self):
        left = self._left()
        self._say(say_line(self.done, self.total, left))
        self._write(left)
        self.last_t, self.last_done = self.clock(), self.done

    def finish(self, walked):
        """The run ended: its pace joins the earlier ones, and the state file says it is over."""
        el = self.clock() - self.t0
        if self.pace_file and walked >= 3:
            try:
                os.makedirs(os.path.dirname(self.pace_file) or ".", exist_ok=True)
                with open(self.pace_file, "a") as f:
                    f.write(f"{self.label}\t{walked}\t{el:.0f}\n")
            except OSError:
                pass
        if self.state_file:
            try:
                d = {"label": self.label, "done": self.done, "total": self.total, "left_min": 0, "started": int(self.t0),
                     "updated": int(self.clock()), "finished": True}
                json.dump(d, open(self.state_file + ".tmp", "w")); os.replace(self.state_file + ".tmp", self.state_file)
            except OSError:
                pass


def walk(cmd, env, cwd, prog, live_dir, poll=5):
    """Run the runner process, stdout and stderr to files so the journeys it has started can be counted while it runs.
    Returns (returncode, stdout, stderr), the same as subprocess.run(capture_output=True, text=True)."""
    os.makedirs(live_dir, exist_ok=True)
    po, pe = os.path.join(live_dir, ".live.out"), os.path.join(live_dir, ".live.err")
    if prog:
        prog.begin_batch()
    with open(po, "wb") as fo, open(pe, "wb") as fe:
        p = subprocess.Popen(cmd, env=env, cwd=cwd, stdout=fo, stderr=fe)
        off, buf = 0, b""
        while True:
            try:
                p.wait(timeout=poll)
                break
            except subprocess.TimeoutExpired:
                pass
            if prog:
                off, buf = _count(po, off, buf, prog)
        if prog:
            _count(po, off, buf, prog)
            prog.end_batch()
    out, err = open(po, encoding="utf-8", errors="replace").read(), open(pe, encoding="utf-8", errors="replace").read()
    for f in (po, pe):
        try:
            os.unlink(f)
        except OSError:
            pass
    return p.returncode, out, err


def _count(path, off, buf, prog):
    """Journeys started since the last look: complete lines only, so a line cut in two is counted once."""
    try:
        with open(path, "rb") as f:
            f.seek(off)
            new = f.read()
    except OSError:
        return off, buf
    data = buf + new
    cut = data.rfind(b"\n") + 1
    n = sum(1 for ln in data[:cut].splitlines() if ln.startswith(MARK.encode()))
    if n:
        prog.seen(n)
    return off + len(new), data[cut:]


def main(argv):
    if len(argv) == 3 and argv[1] == "read":
        try:
            d = json.load(open(argv[2]))
        except (OSError, ValueError):
            return 0
        if not d.get("finished"):
            print("Testing now: " + say_line(d["done"], d["total"], d.get("left_min")))
        return 0
    print("usage: journeys_progress.py read STATE_FILE", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
