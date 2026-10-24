"""Builds app/src/main/assets/index.html from web/cili.html (the same page as on claude.ai).
Run: python3 web/build_index.py"""
from pathlib import Path

root = Path(__file__).resolve().parent.parent
page = (root / "web" / "cili.html").read_text(encoding="utf-8")
head = (
    '<!doctype html><html lang="uk"><head><meta charset="utf-8">'
    '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
    '<style>:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}'
    'body{margin:0;font:14px system-ui,sans-serif}img{max-width:100%}[hidden]{display:none!important}</style>'
    # In the app the goals and posts are kept on the phone (localStorage).
    '<script>window.__APP__=true</script>'
    '</head><body>'
)
out = root / "app" / "src" / "main" / "assets" / "index.html"
out.write_text(head + page + "</body></html>", encoding="utf-8")
print("built", out, out.stat().st_size, "bytes")
