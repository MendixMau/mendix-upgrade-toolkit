#!/usr/bin/env python3
"""orphan_javasource.py: list javasource action files whose Java action is no longer in the model (GM-29), PROPOSE deleting them.

Why: Studio Pro regenerates javasource/<module>/actions/<Name>.java from the Java action document <Module>.<Name>. When
the document is gone (deleted, or lost when a module was updated) the .java file stays, still extending the
CustomJavaAction base class that Mendix 11 removed, and javac fails the whole build on a file nothing in the model uses.
Nothing else lists such files.

  orphan_javasource.py <app dir | app.mpr>

Per file javasource/<module>/actions/*.java (the module folder is the lower-case module name):
  ORPHAN   the file extends CustomJavaAction / UserAction (an action class), the model was read, and it has no
           JavaActions$JavaAction document <Module>.<file name>. Excluded documents count as present (they are in the model).
  UNKNOWN  the model could not be read (no .mpr, unreadable, no bson module, no modules in it): nothing is judged an orphan.
  (nothing) a file that is not an action class (a helper class the user wrote next to the actions), or an action that exists.
Each ORPHAN is followed by a PROPOSE line with the git rm command. This tool never deletes: a person approves, then
deletes (git is the undo). Add-on module Java is not under javasource/ and is never looked at.
Exit: 0 = no orphan and nothing unknown, 1 = orphan files listed (propose deleting), 2 = UNKNOWN (model unreadable) or input error.
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))

ACTION_BASE = re.compile(r"\bextends\s+(?:[\w$]+\.)*(?:CustomJavaAction|UserAction)\b")


def strip_comments(t):
    t = re.sub(r'"(?:\\.|[^"\\\n])*"', '""', t)   # string literals first: "//" or "extends ..." inside one is text
    t = re.sub(r"/\*.*?\*/", " ", t, flags=re.S)
    return re.sub(r"//[^\n]*", " ", t)


def is_action_class(path):
    try:
        t = open(path, encoding="utf-8", errors="replace").read()
    except OSError:
        return False
    return bool(ACTION_BASE.search(strip_comments(t)))


def model_actions(target):
    """({module: {action names}}, None) or (None, reason). Never raises."""
    try:
        import mprmodel
    except Exception as e:
        return None, f"cannot load mprmodel ({e.__class__.__name__}: {e})"
    try:
        m = mprmodel.Model.load(target)
    except SystemExit as e:
        return None, str(e.code or "model refused")
    except Exception as e:
        return None, f"{e.__class__.__name__}: {e}"
    if not m.modules:
        return None, "the model holds no modules"
    acts = {n: set() for n in m.modules}
    for d in m.of_type("JavaActions$JavaAction"):
        acts.setdefault(d.module, set()).add(d.qn.split(".", 1)[1])
    return acts, None


def main(argv):
    if len(argv) != 2 or argv[1].startswith("-"):
        print("usage: orphan_javasource.py <app dir | app.mpr>", file=sys.stderr); return 2
    path = os.path.abspath(argv[1])
    proj = os.path.dirname(path) if os.path.isfile(path) else path
    js = os.path.join(proj, "javasource")
    if not os.path.isdir(js):
        print(f"orphan_javasource: no javasource/ in {proj}: nothing to check"); return 0
    cands = []   # (module folder, file name, relative path)
    for mod in sorted(os.listdir(js)):
        ad = os.path.join(js, mod, "actions")
        if not os.path.isdir(ad):
            continue
        for f in sorted(os.listdir(ad)):
            if f.endswith(".java") and is_action_class(os.path.join(ad, f)):
                cands.append((mod, f[:-5], f"javasource/{mod}/actions/{f}"))
    if not cands:
        print("orphan_javasource: 0 action files under javasource/*/actions: nothing to check"); return 0
    acts, why = model_actions(path if os.path.isfile(path) else proj)
    if acts is None:
        for _, _, rel in cands:
            print(f"UNKNOWN  {rel}  model not readable ({why}): not judged")
        print(f"orphan_javasource: UNKNOWN, {len(cands)} action file(s) not judged because the model could not be read")
        return 2
    low = {n.lower(): n for n in acts}
    orph = []
    for mod, name, rel in cands:
        real = low.get(mod.lower())
        if real is None:
            orph.append((rel, f"module {mod} is not in the model"))
        elif name not in acts[real]:
            orph.append((rel, f"module {real} has no Java action {name}"))
    for rel, r in orph:
        print(f"ORPHAN   {rel}  {r}; extends the removed CustomJavaAction base class and breaks the Mendix 11 build")
    if orph:
        print("PROPOSE  delete these files after a person has looked (nothing was deleted):")
        print("         git rm -- " + " ".join(rel for rel, _ in orph))
    print(f"orphan_javasource: {len(cands)} action file(s) checked, {len(orph)} orphan, {len(cands) - len(orph)} with a model Java action")
    return 1 if orph else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
