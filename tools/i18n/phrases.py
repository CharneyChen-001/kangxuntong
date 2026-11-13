"""Merged translation dictionaries and longest-first glossary for mixed titles."""
from __future__ import annotations

from . import phrases_chrome, phrases_terms, phrases_pages, phrases_apps, phrases_more, phrases_notes

def _merge() -> dict:
    P: dict = {}
    for mod in (phrases_chrome, phrases_terms, phrases_pages, phrases_apps, phrases_more, phrases_notes):
        part = mod.entries()
        overlap = set(P) & set(part)
        # later modules may refine; last write wins, but warn on conflict of values
        for k in overlap:
            if P[k] != part[k]:
                # keep the first unless the later is clearly intended; first wins for safety
                continue
        for k, v in part.items():
            if k not in P:
                P[k] = v
    return P


PHRASES = _merge()

# Prefix translations: keep the remainder (filenames, model codes) unchanged.
PREFIXES = [
    ("Source file: ", {
        "ru": "Исходный файл: ",
        "es": "Archivo de origen: ",
        "pt": "Ficheiro de origem: ",
        "ar": "ملف المصدر: ",
    }),
    ("Outline drawing of ", {
        "ru": "Габаритный чертёж ",
        "es": "Dibujo de contorno de ",
        "pt": "Desenho de contorno de ",
        "ar": "رسم الأبعاد الخارجية لـ ",
    }),
    ("Products / ", {
        "ru": "Продукция / ",
        "es": "Productos / ",
        "pt": "Produtos / ",
        "ar": "المنتجات / ",
    }),
    ("Specifications / ", {
        "ru": "Спецификации / ",
        "es": "Especificaciones / ",
        "pt": "Especificações / ",
        "ar": "المواصفات / ",
    }),
    ("Applications / ", {
        "ru": "Применения / ",
        "es": "Aplicaciones / ",
        "pt": "Aplicações / ",
        "ar": "التطبيقات / ",
    }),
]

# Longest-first glossary for composite titles and leftover mixed strings.
# Only include phrases long enough to avoid accidental inner replacements.
_GLOSSARY_KEYS = [
    "Specification transcribed from the factory Word file; the test report ships with the unit.",
    "Shelf model from the 29 May 2026 quotation; 50 Ω indoor aluminum cavity. Electrical limits are on the unit’s test report.",
    "Cavity Quadplexer with Coupled Port",
    "B5 + B3 + B40 Cavity Pentaplexer",
    "7-band Cavity Combiner (B1, B3, B40, B41, n78)",
    "6-band Cavity Combiner (B5, B8, B28)",
    "8-band Cavity Combiner, mid band",
    "6-band Cavity Combiner, low band",
    "2-band Cavity Combiner, high band",
    "Dual-band Cavity Diplexer",
    "UHF Cavity Duplexer",
    "B3 FDD Cavity Duplexer",
    "Cavity Bandpass Filter",
    "4-port Cavity Combiner",
    "2-port Cavity Combiner",
    "Cavity Quadplexer",
    "Cavity Duplexer",
    "10-band Cavity Combiner",
    "9-band Cavity Combiner",
    "8-band Cavity Combiner",
    "7-band Cavity Combiner",
    "6-band Cavity Combiner",
    "5-band Cavity Combiner",
    "4-band Cavity Combiner",
    "3-band Cavity Combiner",
    "2-band Cavity Combiner",
    "UHF cavity duplexer",
    "cavity bandpass filter",
    "cavity quadplexer with coupled port",
    "cavity quadplexer",
    "cavity duplexer",
    "4-port cavity combiner",
    "2-port cavity combiner",
    "10-band cavity combiner",
    "9-band cavity combiner",
    "8-band cavity combiner",
    "7-band cavity combiner",
    "6-band cavity combiner",
    "5-band cavity combiner",
    "4-band cavity combiner",
    "3-band cavity combiner",
    "2-band cavity combiner",
    "Bandpass filters",
    "Bandpass filter",
    "bandpass filter",
    "Download datasheet PDF",
    "Request a quote",
    "Custom design",
    "custom design",
    "Electrical specification",
    "Insertion loss",
    "Return loss",
    "Low-PIM option",
    "Operating temperature",
    "Average power",
]

def _build_glossary():
    items = []
    seen = set()
    keys = list(_GLOSSARY_KEYS)
    for key in list(keys):
        low = key.lower()
        if low != key:
            keys.append(low)
    for key in keys:
        rec = PHRASES.get(key)
        if rec and key not in seen:
            items.append((key, rec))
            seen.add(key)
    items.sort(key=lambda kv: len(kv[0]), reverse=True)
    return items


GLOSSARY = _build_glossary()
