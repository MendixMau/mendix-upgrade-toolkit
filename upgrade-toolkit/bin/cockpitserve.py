#!/usr/bin/env python3
"""cockpitserve.py: serve the live cockpit page on localhost, so the browser tab reloads itself when the run changes it.

  cockpitserve.py --dir D [--port N] [--idle-exit SECONDS]

A file opened from disk cannot see that it changed; this tiny server can. It binds 127.0.0.1 on a free port (--port N: that one, so an open tab keeps working after a restart) and serves:
  /          D/COCKPIT-view.html (cockpitpage.py --standalone --live writes it)
  /status    the step running now (cockpitpage.running on the rung named in D/.cockpit-work): step, minutes, the script it
             is in and its last line; the page fills its "Running now" bar from it every few seconds, without a reload.
             Never null: with nothing to report it says why, {"state": "idle", "reason": "no-work-dir"} (D/.cockpit-work
             is missing or empty: the pipeline has named no rung) or {"state": "idle", "reason": "no-step-running"}
             (the rung has no live step). A running step has no "state" key; the page hides its bar on state idle.
  /stamp     the page's change stamp (mtime in ns); the page polls it every few seconds and reloads when it moves.
             Every /stamp request also touches D/.cockpit-seen: the pipeline reads that heartbeat to know a tab is open,
             and opens the page again at the next step when no tab has asked for a while (cockpit_live in upgrade-pipeline.sh).
  POST /decide  one answer from a question dialog: {"item", "choice", "by"?, "reason"?}, or {"item": "signoff"}. Without "by"
             the answer carries the machine's Git name (git config user.name): the dev work is tracked in Git anyway.
             It goes through decisions.py import (source page; a sign-off carries the current plan hash) and apply, into the
             same decisions.json the pipeline reads, then the page is written again and D/.cockpit-decided is touched, so
             the session that drives the run sees the answer within seconds. JSON only (a cross-site form cannot send it).
Writes D/.cockpit-port and D/.cockpit-pid at start. Exits on its own after --idle-exit seconds without a request (default 6 h).
Exit: 0 idle exit, 2 usage.
"""
import argparse, http.server, json, os, subprocess, sys, tempfile, threading, time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cockpitpage  # noqa: E402

VIEW = "COCKPIT-view.html"
BIN = os.path.dirname(os.path.abspath(__file__))


def git_name():
    r = subprocess.run(["git", "config", "user.name"], capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else ""


def decide(d, work, body):
    """One answer from the page into the run's decision ledger; returns (http status, message)."""
    item, by = str(body.get("item") or ""), " ".join(str(body.get("by") or git_name()).split())[:80]
    if not item or not by:
        return 400, "an answer needs the item and a name (no git config user.name on this machine)"
    if item == "signoff":
        data = {"signoffs": [{"by": by, "plan": cockpitpage.build_model(work)["planHash"], "source": "page"}]}
    else:
        row = {"item": item, "choice": str(body.get("choice") or ""), "by": by}
        if body.get("reason"):
            row["reason"] = str(body["reason"])[:200]
        data = {"decisions": [row]}
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump(data, f)
    try:
        imp = subprocess.run([sys.executable, os.path.join(BIN, "decisions.py"), "import", "--work", work, "--json", f.name],
                             capture_output=True, text=True)
    finally:
        os.unlink(f.name)
    said = (imp.stdout + imp.stderr).strip()
    if imp.returncode != 0 or "imported 0 row" in said:
        return 422, said or "not saved"
    subprocess.run([sys.executable, os.path.join(BIN, "decisions.py"), "apply", "--work", work], capture_output=True)
    new = os.path.join(d, ".COCKPIT-view.new")
    if subprocess.run([sys.executable, os.path.join(BIN, "cockpitpage.py"), "--work", work, "--out", new, "--standalone", "--live"],
                      capture_output=True).returncode == 0 and os.path.exists(new):
        os.replace(new, os.path.join(d, VIEW))
    with open(os.path.join(d, ".cockpit-decided"), "a") as f:
        f.write(json.dumps({"item": item, "choice": body.get("choice") or "sign", "by": by, "at": time.time()}) + "\n")
    return 200, f"Saved: {item} by {by}"


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--dir", required=True)
    ap.add_argument("--port", type=int, default=0)
    ap.add_argument("--idle-exit", type=int, default=6 * 3600)
    a = ap.parse_args()
    if not os.path.isdir(a.dir):
        print(f"cockpitserve: no folder {a.dir}", file=sys.stderr)
        return 2
    d = os.path.abspath(a.dir)
    last = [time.time()]

    class H(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            last[0] = time.time()
            path = self.path.split("?")[0]
            view = os.path.join(d, VIEW)
            if path == "/stamp":
                with open(os.path.join(d, ".cockpit-seen"), "a"):
                    os.utime(os.path.join(d, ".cockpit-seen"))
                body = str(os.stat(view).st_mtime_ns if os.path.exists(view) else 0).encode()
                ctype = "text/plain"
            elif path == "/status":   # the step running now in the rung the pipeline named (.cockpit-work), else an idle object that says why (DV-14)
                work = (cockpitpage.rd(os.path.join(d, ".cockpit-work")) or "").strip()
                run = cockpitpage.running(work) if work else None
                body = json.dumps(run or {"state": "idle", "reason": "no-step-running" if work else "no-work-dir"}).encode()
                ctype = "application/json"
            elif path in ("/", "/" + VIEW) and os.path.exists(view):
                with open(view, "rb") as f:
                    body = f.read()
                ctype = "text/html; charset=utf-8"
            else:
                self.send_error(404)
                return
            self.send_response(200)
            self.send_header("Content-Type", ctype)
            self.send_header("Cache-Control", "no-store")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def do_POST(self):
            last[0] = time.time()
            if self.path.split("?")[0] != "/decide" or "application/json" not in (self.headers.get("Content-Type") or ""):
                self.send_error(404)
                return
            try:
                body = json.loads(self.rfile.read(min(int(self.headers.get("Content-Length") or 0), 65536)) or b"{}")
            except ValueError:
                body = None
            work = (cockpitpage.rd(os.path.join(d, ".cockpit-work")) or "").strip() or d
            code, msg = (400, "not JSON") if not isinstance(body, dict) else decide(d, work, body)
            out = json.dumps({"ok": code == 200, "said": msg}).encode()
            self.send_response(code)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(out)))
            self.end_headers()
            self.wfile.write(out)

        def log_message(self, *args):
            pass

    srv = http.server.ThreadingHTTPServer(("127.0.0.1", a.port), H)
    for name, val in ((".cockpit-port", srv.server_address[1]), (".cockpit-pid", os.getpid())):
        with open(os.path.join(d, name + ".tmp"), "w") as f:
            f.write(f"{val}\n")
        os.replace(os.path.join(d, name + ".tmp"), os.path.join(d, name))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    while time.time() - last[0] < a.idle_exit:
        time.sleep(min(30, a.idle_exit))
    srv.shutdown()
    return 0


if __name__ == "__main__":
    sys.exit(main())
