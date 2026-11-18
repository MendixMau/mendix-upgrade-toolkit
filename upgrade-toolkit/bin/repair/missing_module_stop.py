#!/usr/bin/env python3
"""missing_module_stop.py: a module update that needs a module the app does not have, said as a person's decision before the build.

Why (run SNOW, issue 24): Atlas_Core 4.3 -> 4.7.0 ships a snippet whose Feedback widget calls a nanoflow in FeedbackModule. The app had
no FeedbackModule, so after the update the build stopped on CE1613 "FeedbackModule.ACT_Open_Feedback_Modal no longer exists". stepupdate
only updates: a plan line for an absent module is refused ("module FeedbackModule not found"). A person had to find the module and
install it by hand. The toolkit does NOT install it on its own: it adds a module to the owner's app. It names the module, the version
and the two ways out, and stops.

Producer: step_build in bin/cloud/upgrade-pipeline.sh runs repair/missing_deps.py first (its "MISSING module X" lines and the catalog
line under each are the detection and the version) and then this script on that output, with the app's git history (the "step: <Module>
<version>" commits stepupdate makes). A missing module counts only when a "step:" commit INTRODUCED a reference to it (git log -S):
a reference that was already dangling before the update is not an update's doing and stays a note.

  missing_module_stop.py MISSING_DEPS.txt PLAN.txt [--app APP_DIR] [--ack missing-module-ack.txt]
Prints, for the pipeline to turn into the stop (nj_meta person ...):
  Q<TAB>question      R<TAB>recommended key      O<TAB>key|label|what it does      B<TAB>one line of the stop's body
Exit: 0 = nothing to decide (nothing missing, or nothing an update introduced), 1 = a decision is needed, 2 = input error.

Design note (data the toolkit does not have): the package's own list of required modules. A Marketplace package declares none that the
toolkit can read (the .mpk holds the module, not its needs), so the need is read from the model after the update: references to a
module that does not exist, plus the step commit that introduced them. The version named is the catalog's latest; when that needs a
newer Mendix than the target the script says so and names no version ("choose one from `mxcli marketplace versions <id>`"). If a
package ever declares its needs, read them before the update and name the module before the first step instead.
"""
import argparse, re, subprocess, sys

MISSING = re.compile(r"^MISSING module (\S+?): (\d+) references?")
CAT = re.compile(r"^\s+Marketplace: content (\d+) '([^']*)' latest (\S+) \(min Mendix ([^,)]*)(?:, [^)]*)?\)( \[min Mendix above target [^\]]*\])?")


def missing(path):
    """[(module, content id or None, version or None, above target)] from missing_deps.py's own output."""
    out, cur = [], None
    for ln in open(path, encoding="utf-8", errors="replace"):
        m = MISSING.match(ln)
        if m:
            cur = [m.group(1), None, None, False]
            out.append(cur)
            continue
        c = CAT.match(ln)
        if c and cur is not None and cur[1] is None:
            cur[1], cur[2], cur[3] = c.group(1), c.group(3), bool(c.group(5))
        elif ln.strip() and not ln.startswith(" "):
            cur = None
    return [tuple(x) for x in out]


def plan_modules(path):
    mods = set()
    try:
        for ln in open(path):
            p = ln.split("#")[0].split()
            if len(p) >= 3:
                mods.add(p[2])
    except OSError:
        pass
    return mods


def introduced_by(app, module):
    """[(short sha, module, version)] of the 'step: <Module> <version>' commits whose change added or removed '<module>.' in the model."""
    if not app:
        return []
    try:
        r = subprocess.run(["git", "-C", app, "log", "--grep=^step: ", "-S" + module + ".", "--format=%h %s"],
                           capture_output=True, text=True, timeout=300)
    except (OSError, subprocess.TimeoutExpired):
        return []
    out = []
    for ln in r.stdout.splitlines():
        m = re.match(r"(\w+) step: (\S+) (\S+)", ln)
        if m:
            out.append((m.group(1), m.group(2), m.group(3)))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("deps"); ap.add_argument("plan"); ap.add_argument("--app"); ap.add_argument("--target")
    ap.add_argument("--ack", help="missing-module-ack.txt: '<Module> <reason>' per line, a module the person decided to go without")
    a = ap.parse_args()
    try:
        mods = missing(a.deps)
    except OSError as e:
        print(f"missing_module_stop: {e}", file=sys.stderr); return 2
    acked = set()
    if a.ack:
        try:
            acked = {ln.split()[0] for ln in open(a.ack) if ln.split("#")[0].split() and len(ln.split()) >= 2 and not ln.lstrip().startswith("#")}
        except OSError:
            pass
    need = []   # (module, cid, version, above, [step commits])
    for m, cid, ver, above in mods:
        by = introduced_by(a.app, m) if m not in acked else []
        if by:
            need.append((m, cid, ver, above, by))
    if not need:
        return 0
    names = ", ".join(n[0] for n in need)
    updaters = sorted({s[1] for n in need for s in n[4]})
    upd = " and ".join(updaters)
    plural = len(need) > 1
    print(f"Q\tThe update of {upd} needs {'modules' if plural else 'a module'} this app does not have: {names}. "
          f"The update only updates, it never adds a module, so the app would not build. What should we do?")
    inst = []
    for m, cid, ver, above, _ in need:
        if cid and ver and not above:
            inst.append(f"{m} {ver}")
        elif cid:
            inst.append(f"{m} (an older version: its latest needs a newer Mendix than the target)")
        else:
            inst.append(f"{m} (no Marketplace match: search it by name)")
    cmds = []
    for m, cid, ver, above, _ in need:
        cmds.append(f"mxcli marketplace install {cid} --version {ver}" if cid and ver and not above
                    else (f"mxcli marketplace versions {cid}, then mxcli marketplace install {cid} --version <one>" if cid else f"find {m} on the Marketplace"))
    print("R\t" + ("install" if all(n[1] and n[2] and not n[3] for n in need) else "keep"))   # no usable version to name: keeping is the safe default
    print(f"O\tinstall|Install {'; '.join(inst)} from the Marketplace|"
          f"Adds {'these modules' if plural else 'this module'} to your app ({'; '.join(cmds)}), commit, rerun from the build step. "
          f"Nothing is installed until you say so.")
    shas = ", ".join(f"git revert {s[0]}" for n in need for s in n[4])
    print(f"O\tkeep|Keep the old version of {upd}|Revert its update ({shas}) or remove its line from the plan, and rerun from the update step. "
          f"The app stays on the old version and gets no new module.")
    print("B\tWhat was found (missing_deps.py, then the app's step commits):")
    for m, cid, ver, above, by in need:
        print(f"B\t  {m}: Marketplace content {cid or 'unknown'}, " + (f"version {ver}" if ver else "version unknown")
              + (", NOT usable on the target (needs a newer Mendix)" if above else "")
              + "; introduced by " + ", ".join(f"{s[1]} {s[2]} ({s[0]})" for s in by))
    inplan = [u for u in updaters if u in plan_modules(a.plan)]
    print("B\tPlan lines of the updating module(s): " + (", ".join(inplan) if inplan else "none found in the plan file"))
    print("B\tCarry on without it (the module comes from elsewhere): write the module name and a reason in missing-module-ack.txt, then rerun from build.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
