"""Control for cockpitmatrix.found_detail: what a finding MEANS, per item, built from the run's own files.
Usage: found_means_control.py <scratch dir>. Prints "means <topic>: ..." and "item <topic>: what | tag | tone | meaning" lines."""
import json, os, sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "bin"))
import cockpitmatrix as cm

w = sys.argv[1]
os.makedirs(w, exist_ok=True)
json.dump({"endpoints": [
    {"doc": "Shop.GetRates", "kind": "rest", "status": "MOCKED", "why": "every location is an overridden constant"},
    {"doc": "Mail.GetToken", "kind": "rest", "status": "UNKNOWN", "why": "location from data Mail.Provider.TokenUrl: set it to the printed URL"},
    {"doc": "Sso.Refresh", "kind": "rest", "status": "UNKNOWN", "why": "$Uri is computed by Java action Sso.GetUri at runtime"}]},
    open(os.path.join(w, "apimock-inventory.json"), "w"))
json.dump([{"name": "Theme", "ui": [{"change": "CHANGED", "kind": "layout", "name": "Theme.Default", "detail": "content differs from the package"}]},
           {"name": "Plain", "ui": []}, {"name": "Odd", "domain_error": ["not found"]},
           {"name": "Admin", "domain": [{"change": "ADDED", "kind": "entity", "name": "Admin.Extra", "data": True, "detail": ""}],
            "logic": [{"change": "ADDED", "kind": "microflow", "name": "Admin.Save", "detail": "local document, removed by the update"}]}],
          open(os.path.join(w, "localedits.json"), "w"))
recs = [{"topic": "standins", "found": {}},
        {"topic": "modules", "found": {"evidence": ["module update Theme 1.0.0 -> 2.0.0 (after the convert)", "module update Plain 1.0.0 -> 1.1.0 (after the convert)",
                                                    "module update Odd 3.0.0 -> 3.1.0 (after the convert)"]}},
        {"topic": "module:Admin", "found": {}},
        {"topic": "react", "found": {"evidence": ["Dojo to React on the 11.12.7 rung: 4 x Drop-down (core) -> Combo box"]}},
        {"topic": "nothing:known", "found": {}}]
for r in recs:
    d = cm.found_detail(r, w)
    if not d:
        print(f"empty {r['topic']}")
    for m in d.get("means", []):
        print(f"means {r['topic']}: {m}")
    for i in d.get("items", []):
        print(f"item {r['topic']}: " + " | ".join(i))

# a case file per decision: loaded by id, screenshots embedded, a broken file ignored
if len(sys.argv) > 2 and sys.argv[2] == "cases":
    import base64
    os.makedirs(os.path.join(w, "cases"), exist_ok=True)
    open(os.path.join(w, "old.png"), "wb").write(base64.b64decode("iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg=="))
    json.dump({"headline": "Seven break", "tiles": [[7, "fail on the new", "bad"]], "shots": [{"old": "old.png", "new": "gone.png", "cap": "look"}],
               "why": ["one", "two"], "options": {"fix": {"does": "We fix it.", "catch": "One rerun."}}},
              open(os.path.join(w, "cases", cm.case_id("regression:module-X")), "w"))
    open(os.path.join(w, "cases", "broken.json"), "w").write("{not json")
    cs = cm.cases(w)
    print("case files:", sorted(cs))
    c = cs[cm.case_id("regression:module-X")]
    print("old shot:", c["shots"][0]["old"][:22], "| new shot:", repr(c["shots"][0]["new"]))
    h = cm.h_case(c)
    print("html:", "tiles" if 'class="ct bad"' in h else "-", "why=" + str(h.count("<li>")), "no-shot" if "no screenshot" in h else "-")
