"""data.json ni template.html ichiga joylab, site/index.html yaratadi.
Savollarni o'zgartirsangiz:  python tools/build_site.py"""
import json, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
data = json.loads((root / "data.json").read_text(encoding="utf-8"))
html = (root / "tools" / "template.html").read_text(encoding="utf-8")
(root / "site" / "index.html").write_text(html.replace("__DATA__", json.dumps(data, ensure_ascii=False)), encoding="utf-8")
print("site/index.html tayyor")
