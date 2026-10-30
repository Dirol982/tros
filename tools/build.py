"""Сборка сайта: python3 tools/build.py → HTML-страницы в корне репозитория."""
import datetime
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from layout import SITE, footer, head, header  # noqa: E402
from pages_inner import diagnostika, izgotovlenie, kontakty, po_belarusi, remont_kulis, remont_trosov  # noqa: E402
from pages_main import index  # noqa: E402
from pages_report import izmeneniya  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGES = [index, remont_trosov, remont_kulis, izgotovlenie, diagnostika, po_belarusi, kontakty, izmeneniya]


def render(page, body, artifact=False):
    html = head(page, artifact=artifact) + "\n" + header(page["slug"]) + body + footer()
    return html if artifact else html + "\n</body>\n</html>\n"


def main(artifact_dir=None):
    today = datetime.date.today().isoformat()
    urls = []
    for fn in PAGES:
        page, body = fn()
        (ROOT / page["slug"]).write_text(render(page, body), encoding="utf-8")
        if not page.get("robots", "").startswith("noindex"):
            loc = SITE + "/" + ("" if page["slug"] == "index.html" else page["slug"])
            prio = "1.0" if page["slug"] == "index.html" else "0.8"
            urls.append(f"  <url><loc>{loc}</loc><lastmod>{today}</lastmod><priority>{prio}</priority></url>")
        if artifact_dir and page["slug"] == "index.html":
            pathlib.Path(artifact_dir, "index.html").write_text(render(page, body, artifact=True), encoding="utf-8")
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(urls) + "\n</urlset>\n", encoding="utf-8")
    (ROOT / "robots.txt").write_text(
        f"User-agent: *\nDisallow: /izmeneniya.html\nDisallow: /tools/\nDisallow: /deploy/\n\nSitemap: {SITE}/sitemap.xml\n",
        encoding="utf-8")
    print("built", len(PAGES), "pages")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
