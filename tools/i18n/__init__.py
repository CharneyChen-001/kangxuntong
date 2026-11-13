"""Locale metadata and translation helpers for the Kangxuntong static site."""
from .meta import (
    ALL_LOCALES,
    NEW_LOCALES,
    LOCALES,
    EMAIL,
    WA,
    SITE,
    LEGAL_CN,
    LEGAL_EN,
    locale_of,
    en_rel,
    loc_rel,
    page_href,
    og_alternates,
)
from .translate import tr, translate_tree, leftover_report, reset_leftovers
from .forms import form_strings
