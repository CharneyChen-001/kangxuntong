"""Locale metadata and path helpers. Legal names are never invented in other languages."""
from __future__ import annotations

SITE = "https://cavityfilter.com"
EMAIL = "sales@cavityfilter.com"
WA = "8618688718926"
PHONE_DISPLAY = "+86 186 8871 8926"
LEGAL_CN = "深圳市康讯通技术有限公司"
LEGAL_EN = "Shenzhen Kangxuntong Technology Co., Ltd."
BRAND_EN = "Kangxuntong"
BRAND_CN = "康讯通"

# Path-prefix locales. English stays at the site root; Chinese stays at /zh/.
LOCALES = {
    "en": {"code": "en", "prefix": "", "html_lang": "en", "dir": "ltr", "og": "en_US", "label": "EN", "hreflang": "en"},
    "zh": {"code": "zh", "prefix": "zh/", "html_lang": "zh", "dir": "ltr", "og": "zh_CN", "label": "中文", "hreflang": "zh"},
    "ru": {"code": "ru", "prefix": "ru/", "html_lang": "ru", "dir": "ltr", "og": "ru_RU", "label": "RU", "hreflang": "ru"},
    "es": {"code": "es", "prefix": "es/", "html_lang": "es", "dir": "ltr", "og": "es", "label": "ES", "hreflang": "es"},
    "pt": {"code": "pt", "prefix": "pt/", "html_lang": "pt", "dir": "ltr", "og": "pt", "label": "PT", "hreflang": "pt"},
    "ar": {"code": "ar", "prefix": "ar/", "html_lang": "ar", "dir": "rtl", "og": "ar", "label": "AR", "hreflang": "ar"},
}

ALL_LOCALES = ("en", "zh", "ru", "es", "pt", "ar")
NEW_LOCALES = ("ru", "es", "pt", "ar")


def locale_of(rel: str) -> str:
    for loc in ("zh", "ru", "es", "pt", "ar"):
        if rel == loc or rel.startswith(loc + "/"):
            return loc
    return "en"


def en_rel(rel: str) -> str:
    loc = locale_of(rel)
    if loc == "en":
        return rel
    return rel[len(loc) + 1 :]


def loc_rel(rel: str, loc: str) -> str:
    e = en_rel(rel)
    if loc == "en":
        return e
    return f"{loc}/{e}"


def page_href(rel: str) -> str:
    """Root-absolute href for a page under website/ (index.html → / or /zh/)."""
    if rel == "index.html":
        return "/"
    if rel.endswith("/index.html"):
        return "/" + rel[: -len("index.html")]
    return "/" + rel


def og_alternates(current: str) -> list[str]:
    return [LOCALES[loc]["og"] for loc in ALL_LOCALES if loc != current]
