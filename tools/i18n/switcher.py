"""Language switcher markup shared by the generators."""
from __future__ import annotations

from .meta import ALL_LOCALES, LOCALES, locale_of, en_rel, loc_rel, page_href
from .translate import tr


def switcher_html(rel: str) -> str:
    cur = locale_of(rel)
    e = en_rel(rel)
    if cur == "en":
        aria = "Language"
    elif cur == "zh":
        aria = "语言"
    else:
        aria = tr(cur, "Language", record=False)
    parts = []
    for loc in ALL_LOCALES:
        # 404 lives only at the site root; its switcher points at each locale home.
        target = "index.html" if e == "404.html" else e
        href = page_href(loc_rel(target, loc))
        cls = "on" if loc == cur else ""
        label = LOCALES[loc]["label"]
        parts.append(
            f'<a href="{href}" lang="{loc}" hreflang="{loc}" class="{cls}">{label}</a>'
        )
    return f'<nav class="lang" aria-label="{aria}">' + "".join(parts) + "</nav>"
