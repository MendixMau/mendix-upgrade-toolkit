#!/usr/bin/env python3
"""cockpitserve.py: serve the live cockpit page on localhost, so the browser tab reloads itself when the run changes it.

  cockpitserve.py --dir D [--idle-exit SECONDS]

A file opened from disk cannot see that it changed; this tiny server can. It binds 127.0.0.1 on a free port and serves:
  /          D/COCKPIT-view.html (cockpitpage.py --standalone --live writes it)
  /stamp     the page's change stamp (mtime in ns); the page polls it every few seconds and reloads when it moves.
             Every /stamp request also touches D/.cockpit-seen: the pipeline reads that heartbeat to know a tab is open,
             and opens the page again at the next step when no tab has asked for a while (cockpit_live in upgrade-pipeline.sh).
Writes D/.cockpit-port and D/.cockpit-pid at start. Exits on its own after --idle-exit seconds without a request (default 6 h).
Exit: 0 idle exit, 2 usage.
"""
import argparse, http.server, os, sys, threading, time

VIEW = "COCKPIT-view.html"


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--dir", required=True)
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

        def log_message(self, *args):
            pass

    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), H)
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
