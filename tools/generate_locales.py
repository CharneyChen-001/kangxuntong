#!/usr/bin/env python3
"""Build website/{ru,es,pt,ar}/ from the English tree.

Idempotent. Does not modify English or Chinese pages, assets, or datasheets.
Run this, then python3 tools/build_site.py, so SEO, forms and the sitemap
are rewritten for every locale.
"""
from __future__ import annotations

import posixpath
import re
import sys
from pathlib import Path

from bs4 import BeautifulSoup, Comment, NavigableString

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

from i18n.meta import NEW_LOCALES, LOCALES, loc_rel  # noqa: E402
from i18n.translate import (  # noqa: E402
    translate_tree, reset_leftovers, leftover_report, tr,
)
from i18n.switcher import switcher_html  # noqa: E402

SITE_ROOT = ROOT / "website"
SHARED_PREFIXES = ("assets/", "css/", "js/", "datasheets/")
LTR_RE = re.compile(
    r"(sales@cavityfilter\.com|\+86[\d\s]+|KXT[A-Z0-9\-]+|"
    r"https?://[^\s<]+|"
    r"\d+(?:[.,]\d+)?\s*[–\-]\s*\d+(?:[.,]\d+)?(?:\s*(?:MHz|GHz|kHz|dB|dBc|dBm|W|mm|Ω))?)",
    re.I,
)


def en_pages():
    pages = []
    for p in SITE_ROOT.rglob("*.html"):
        rel = p.relative_to(SITE_ROOT).as_posix()
        if rel.split("/")[0] in {"zh", "ru", "es", "pt", "ar"}:
            continue
        if rel == "404.html":
            continue
        pages.append(rel)
    return sorted(pages)


def split_href(href: str) -> tuple[str, str]:
    cuts = [i for i in (href.find("?"), href.find("#")) if i >= 0]
    i = min(cuts) if cuts else len(href)
    return href[:i], href[i:]


def resolve(from_rel: str, href_path: str) -> str:
    base = posixpath.dirname(from_rel)
    return posixpath.normpath(posixpath.join(base, href_path) if base else href_path)


def rel_to(from_rel: str, target: str) -> str:
    start = posixpath.dirname(from_rel) or "."
    return posixpath.relpath(target, start)


def is_shared(target: str) -> bool:
    t = target.lstrip("./")
    return any(t == d[:-1] or t.startswith(d) for d in SHARED_PREFIXES)


def rewrite_url(src_rel: str, dest_rel: str, href: str) -> str:
    if not href:
        return href
    path, suffix = split_href(href)
    if not path or path.startswith(("http://", "https://", "mailto:", "tel:", "#", "/")):
        return href
    target = resolve(src_rel, path)
    if target.startswith("zh/") or "/zh/" in ("/" + target):
        return href
    if is_shared(target):
        return rel_to(dest_rel, target) + suffix
    return href


def rewrite_tree_urls(soup, src_rel: str, dest_rel: str) -> None:
    for el in soup.find_all(True):
        for attr in ("href", "src"):
            if el.has_attr(attr):
                el[attr] = rewrite_url(src_rel, dest_rel, el[attr])
        # CSS background thumbnails
        style = el.get("style") or ""
        if "url(" in style:
            def repl(m):
                u = m.group(1)
                return "url(" + rewrite_url(src_rel, dest_rel, u) + ")"
            el["style"] = re.sub(r"url\(([^)]+)\)", repl, style)


def set_switcher(soup, dest_rel: str) -> None:
    nav = BeautifulSoup(switcher_html(dest_rel), "html.parser").find("nav")
    existing = soup.find("span", class_="lang") or soup.find("nav", class_="lang")
    if existing and nav:
        existing.replace_with(nav)


def set_lang_dir(soup, lang: str) -> None:
    html = soup.find("html")
    if not html:
        return
    meta = LOCALES[lang]
    html["lang"] = meta["html_lang"]
    if meta["dir"] == "rtl":
        html["dir"] = "rtl"
    elif "dir" in html.attrs:
        del html.attrs["dir"]


def wrap_ltr_nodes(soup) -> None:
    if not soup.body:
        return
    for node in list(soup.body.descendants):
        if not isinstance(node, NavigableString) or isinstance(node, Comment):
            continue
        parent = node.parent
        if parent is None or parent.name in {"script", "style"}:
            continue
        if parent.name == "span" and parent.get("dir") == "ltr":
            continue
        text = str(node)
        if not LTR_RE.search(text):
            continue
        parts = []
        pos = 0
        for m in LTR_RE.finditer(text):
            if m.start() > pos:
                parts.append(text[pos:m.start()])
            parts.append(('ltr', m.group(0)))
            pos = m.end()
        if pos < len(text):
            parts.append(text[pos:])
        from bs4 import BeautifulSoup as BS
        frag = BS("", "html.parser")
        new_nodes = []
        for part in parts:
            if isinstance(part, tuple):
                span = soup.new_tag("span", **{"dir": "ltr", "class": "ltr"})
                span.string = part[1]
                new_nodes.append(span)
            else:
                new_nodes.append(NavigableString(part))
        node.replace_with(*new_nodes)


def serialize(soup, original: str) -> str:
    html = soup.find("html")
    body = "<!DOCTYPE html>\n" + (html.decode(formatter="html5") if html else soup.decode(formatter="html5"))
    if not body.endswith("\n"):
        body += "\n"
    return body


def build_locale(lang: str, pages: list[str]) -> int:
    count = 0
    for rel in pages:
        src = SITE_ROOT / rel
        dest_rel = loc_rel(rel, lang)
        dest = SITE_ROOT / dest_rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        raw = src.read_text(encoding="utf-8")
        soup = BeautifulSoup(raw, "html.parser")
        set_lang_dir(soup, lang)
        rewrite_tree_urls(soup, rel, dest_rel)
        translate_tree(soup, lang)
        set_switcher(soup, dest_rel)
        if lang == "ar":
            wrap_ltr_nodes(soup)
        dest.write_text(serialize(soup, raw), encoding="utf-8")
        count += 1
    return count


def main() -> None:
    pages = en_pages()
    reset_leftovers()
    total = 0
    for lang in NEW_LOCALES:
        n = build_locale(lang, pages)
        total += n
        print(f"{lang}: {n} pages")
    leftovers = leftover_report()
    report = ROOT / "tools" / "i18n" / "_leftovers.txt"
    if leftovers:
        report.write_text("\n".join(f"{c}\t{s}" for c, s in leftovers) + "\n", encoding="utf-8")
        print(f"{len(leftovers)} distinct untranslated strings → {report}")
    elif report.exists():
        report.unlink()
        print("no untranslated leftovers")
    print(f"{total} locale pages written from {len(pages)} English sources")


if __name__ == "__main__":
    main()
