"""Translate English HTML text nodes and attributes into ru/es/pt/ar."""
from __future__ import annotations

import re
from collections import Counter

from .meta import LEGAL_CN, LEGAL_EN, BRAND_EN, BRAND_CN, EMAIL
from .phrases import PHRASES, PREFIXES, GLOSSARY

# typographic / whitespace normalization for dictionary lookup
_APOS = dict.fromkeys(map(ord, "‘’‚‛"), "'")
_QUOT = dict.fromkeys(map(ord, "“”„‟"), '"')
_DASH = {ord("–"): "-", ord("—"): "-", ord("−"): "-"}

_LEFTOVERS: Counter[str] = Counter()

# Skip translation when the node has no real English prose.
_TECH_ONLY = re.compile(
    r"^[\d\s./\-–—−×xX+±≤≥<>μΩ°℃,:%*()~～＋－†*]+$"
)
_MODEL = re.compile(r"^KXT[A-Z0-9\-]*$")
_HAS_CJK = re.compile(r"[\u4e00-\u9fff]")
_HAS_EN_WORD = re.compile(r"[A-Za-z]{3,}")
# factory bilingual header: 中文 / English
_BI = re.compile(r"^(.*?)(\s*/\s*)([A-Za-z].*)$")

# Tokens that must never be rewritten as words
_PROTECT = [
    (LEGAL_EN, "\u0000LEGALEN\u0000"),
    (LEGAL_CN, "\u0000LEGALCN\u0000"),
    (EMAIL, "\u0000EMAIL\u0000"),
]


def reset_leftovers() -> None:
    _LEFTOVERS.clear()


def leftover_report() -> list[tuple[int, str]]:
    return _LEFTOVERS.most_common()


def norm(s: str) -> str:
    s = s.translate(_APOS).translate(_QUOT)
    s = s.replace("\xa0", " ")
    s = re.sub(r"[ \t]+", " ", s)
    return s.strip()


def _lookup(text: str, lang: str) -> str | None:
    key = norm(text)
    rec = PHRASES.get(key) or PHRASES.get(text.strip())
    if rec and lang in rec:
        return rec[lang]
    # curly vs straight apostrophe already normalized in keys
    return None


def _protect(s: str) -> str:
    for src, tok in _PROTECT:
        s = s.replace(src, tok)
    return s


def _unprotect(s: str) -> str:
    for src, tok in _PROTECT:
        s = s.replace(tok, src)
    return s


_EXTRA_GLOSSARY = None

def _all_glossary():
    global _EXTRA_GLOSSARY
    if _EXTRA_GLOSSARY is None:
        extra = []
        seen = {en for en, _ in GLOSSARY}
        for en, rec in PHRASES.items():
            if en in seen:
                continue
            if len(en) < 12:
                continue
            extra.append((en, rec))
        extra.sort(key=lambda kv: len(kv[0]), reverse=True)
        _EXTRA_GLOSSARY = extra
    return list(GLOSSARY) + _EXTRA_GLOSSARY


def _glossary_apply(text: str, lang: str) -> str:
    """Longest-first phrase replacement for leftover mixed strings (titles, labels)."""
    s = text
    for en, rec in _all_glossary():
        val = rec.get(lang)
        if not val:
            continue
        if en in s:
            s = s.replace(en, val)
    return s


def tr(lang: str, text: str, *, record: bool = True) -> str:
    """Translate an English string. Leave non-English / technical values unchanged."""
    if not text or lang in ("en", "zh"):
        return text
    leading = re.match(r"^\s*", text).group(0)
    trailing = re.search(r"\s*$", text).group(0)
    raw = text[len(leading): len(text) - len(trailing) if trailing else len(text)]
    if not raw:
        return text

    if raw in (LEGAL_EN, LEGAL_CN, BRAND_EN, BRAND_CN, EMAIL, "康讯通", "Kangxuntong"):
        return text
    if _TECH_ONLY.match(raw) or _MODEL.match(raw):
        return text
    # Chinese-only factory cells, or Chinese plus a short Latin token (N-K, Item already handled)
    if _HAS_CJK.search(raw) and not _HAS_EN_WORD.search(raw):
        return text

    hit = _lookup(raw, lang)
    if hit is not None:
        return leading + hit + trailing

    # "Page title | Kangxuntong"
    if raw.endswith(" | Kangxuntong"):
        left = raw[: -len(" | Kangxuntong")]
        left_tr = tr(lang, left, record=record)
        return leading + left_tr + " | Kangxuntong" + trailing

    # "Source file: 中文文件名"
    for prefix, rec in PREFIXES:
        if raw.startswith(prefix):
            rest = raw[len(prefix):]
            return leading + rec[lang] + rest + trailing

    # bilingual factory header "工作频率(MHz) / Passband"
    m = _BI.match(raw)
    if m and _HAS_CJK.search(m.group(1)):
        right = m.group(3)
        right_tr = _lookup(right, lang)
        if right_tr is None:
            right_tr = _glossary_apply(right, lang)
            if right_tr == right and record and _HAS_EN_WORD.search(right):
                _LEFTOVERS[right] += 1
        return leading + m.group(1) + m.group(2) + right_tr + trailing

    protected = _protect(raw)
    applied = _glossary_apply(protected, lang)
    applied = _unprotect(applied)
    if applied != raw:
        # still record leftover English words of length >= 4, except units/codes
        if record:
            leftover_en = _leftover_english(applied)
            if leftover_en:
                _LEFTOVERS[raw] += 1
        return leading + applied + trailing

    if record and _HAS_EN_WORD.search(raw):
        _LEFTOVERS[raw] += 1
    return text


_IGNORE_WORDS = {
    "mhz", "ghz", "khz", "db", "dbc", "dbm", "vswr", "pim", "pim3", "vna", "sma",
    "din", "lte", "pdf", "fob", "exw", "lmr", "pmr", "das", "erces", "poi", "bda",
    "nfpa", "ahj", "ifc", "tetra", "dmr", "apco", "etsi", "tia", "fdd", "tdd",
    "wifi", "wi-fi", "n-f", "n-k", "the", "and", "or", "of", "a", "an", "to",
    "in", "on", "at", "for", "with", "from", "by", "as", "is", "are", "be",
    "mhz", "ch1", "ch2", "ch3", "ch4", "tx", "rx", "ant", "item", "wcdma",
    "html", "css", "http", "https", "www", "com", "co", "ltd",
}


def _leftover_english(s: str) -> bool:
    words = re.findall(r"[A-Za-z][A-Za-z\-']+", s)
    for w in words:
        if w.lower() in _IGNORE_WORDS:
            continue
        if w.startswith("KXT") or re.fullmatch(r"B\d+|n\d+|CH\d+", w):
            continue
        if len(w) >= 4:
            return True
    return False


# Attributes that carry visible prose
_ATTRS = ("alt", "aria-label", "placeholder", "title")
_DATA_ATTRS = ("data-error", "data-sending", "data-fail")
_SKIP_TAGS = {"script", "style", "svg", "code"}


def translate_tree(soup, lang: str) -> None:
    """In-place translation of a BeautifulSoup document."""
    # <title> and meta description / og title+description (seo block is rewritten later)
    if soup.title and soup.title.string:
        soup.title.string = tr(lang, soup.title.string)
    for meta in soup.find_all("meta"):
        name = (meta.get("name") or "") + (meta.get("property") or "")
        if name in {"description", "og:title", "og:description"} and meta.get("content"):
            meta["content"] = tr(lang, meta["content"])
    # html lang/dir is set by the generator, not here
    if not soup.body:
        return
    for el in soup.find_all(True):
        if el.name in _SKIP_TAGS:
            continue
        # skip SEO json-ld and comments handled separately
        for attr in _ATTRS:
            if el.has_attr(attr) and el[attr]:
                el[attr] = tr(lang, el[attr])
        for attr in _DATA_ATTRS:
            if el.has_attr(attr) and el[attr]:
                el[attr] = tr(lang, el[attr])
        # hidden subject line
        if el.name == "input" and el.get("name") == "_subject" and el.get("value"):
            el["value"] = tr(lang, el["value"])
        if el.name == "option" and el.get("value") in {"no", "yes"} and el.string:
            el.string = tr(lang, el.string)
        if el.name == "input" and el.get("name") == "product" and el.get("value"):
            el["value"] = tr(lang, el["value"])
    for node in list(soup.body.descendants):
        if getattr(node, "name", None) is not None:
            continue
        parent = node.parent
        if parent is None or parent.name in _SKIP_TAGS:
            continue
        # do not touch comments
        from bs4 import Comment, NavigableString
        if isinstance(node, Comment):
            continue
        if not isinstance(node, NavigableString):
            continue
        original = str(node)
        if not original or not original.strip():
            continue
        node.replace_with(tr(lang, original))
