#!/usr/bin/env python3
"""Shared head/footer/form/SEO pass over the static site in website/.

Idempotent: run it after editing any page.
    python3 tools/generate_locales.py
    python3 tools/build_site.py
What it does (and nothing else):
  * <head>: canonical, hreflang en/zh/ru/es/pt/ar/x-default, Open Graph, JSON-LD
    (Organization + WebSite on the home pages, Product on product pages),
    written between <!-- seo:start --> and <!-- seo:end -->.
  * footer: sales@cavityfilter.com, clickable WhatsApp, Privacy and Terms.
  * the RFQ form (contact + custom pages in every locale) posting to FormSubmit.
  * generated pages: contact/thanks.html, products/vhf-uhf-duplexers.html,
    shelf models, application sub-pages (all locales).
  * sitemap.xml (absolute URLs + hreflang) and robots.txt.
  * the six-language switcher on every page.
Specification numbers are never generated here; they live in the pages.
English and Chinese typo-corrected product bodies are not rewritten.
"""
import html, json, pathlib, re, datetime, sys
from bs4 import BeautifulSoup

SITE = "https://cavityfilter.com"
EMAIL = "sales@cavityfilter.com"
WA = "8618688718926"
ROOT = pathlib.Path(__file__).resolve().parent.parent / "website"
FORM_ACTION = f"https://formsubmit.co/{EMAIL}"

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from i18n.meta import (  # noqa: E402
    ALL_LOCALES, NEW_LOCALES, LOCALES, locale_of, en_rel, loc_rel, page_href, og_alternates,
)
from i18n.forms import form_strings  # noqa: E402
from i18n.translate import tr, translate_tree  # noqa: E402
from i18n.switcher import switcher_html  # noqa: E402

NOINDEX = {"404.html"} | {loc_rel("contact/thanks.html", loc) for loc in ALL_LOCALES}


def rd(p): return p.read_text(encoding="utf-8")
def wr(p, s):
    if not p.exists() or rd(p) != s:
        p.write_text(s, encoding="utf-8")


def rel(p): return p.relative_to(ROOT).as_posix()
def is_zh(r): return locale_of(r) == "zh"
def en_of(r): return en_rel(r)
def zh_of(r): return loc_rel(r, "zh")
def up(r): return "../" * r.count("/")          # path from page to website root
def lang_of(r): return locale_of(r)


def lang_root(r):
    """Relative path from this page to the root of its locale."""
    e = en_of(r)
    parent = pathlib.PurePosixPath(e).parent.as_posix()
    if parent in (".", ""):
        return ""
    return "../" * (parent.count("/") + 1)


def translate_fragment(lang, html_frag):
    """Translate an English HTML fragment into lang (no-op for en)."""
    if lang == "en":
        return html_frag
    soup = BeautifulSoup("<html><body>" + html_frag + "</body></html>", "html.parser")
    translate_tree(soup, lang)
    return "".join(str(c) for c in soup.body.contents)


def url(r):
    if r == "index.html": return SITE + "/"
    if r.endswith("/index.html"): return f"{SITE}/{r[:-len('index.html')]}"
    return f"{SITE}/{r}"


def esc(s): return html.escape(s, quote=True)
def is_product(stem): return re.match(r"kxt(-|\d)", stem) is not None


# ---------------------------------------------------------------- form
MODELS_RE = re.compile(r'<datalist id="model-list">.*?</datalist>', re.S)


def form_html(lang, r, models, source):
    L = form_strings(lang)
    base = lang_root(r)
    thanks = url(loc_rel("contact/thanks.html", lang))
    custom = source == "custom"
    prefill = f' value="{html.escape(L["custom_value"], quote=True)}"' if custom else ""
    enctype = ' enctype="multipart/form-data"' if custom else ""
    qty_req = " required" if custom else ""
    upload = (f'<label>{L["file"]}</label><input name="attachment" type="file" accept=".pdf,.dwg,.dxf,.step,.stp,.jpg,.jpeg,.png,application/pdf,image/jpeg,image/png">'
              f'<p class="note">{L["filenote"]}</p>\n') if custom else ""
    ltr = ' dir="ltr"' if lang == "ar" else ""
    return f"""<!-- rfq:start -->
<form id="rfq" action="{FORM_ACTION}" method="POST"{enctype} data-ajax="https://formsubmit.co/ajax/{EMAIL}" data-wa="{WA}" data-error="{esc(L['err'])}" data-sending="{esc(L['sending'])}" data-fail="{esc(L['fail'])}">
<input type="hidden" name="_subject" value="{esc(L['subj'])}">
<input type="hidden" name="_next" value="{thanks}">
<input type="hidden" name="_template" value="table">
<input type="hidden" name="_captcha" value="false">
<input type="hidden" name="page" value="{url(r)}">
<div class="row"><div><label>{L['name']}</label><input name="name" required></div><div><label>{L['company']}</label><input name="company" required></div></div>
<div class="row"><div><label>{L['email']}</label><input name="email" type="email" required{ltr}></div><div><label>{L['country']}</label><input name="country" required></div></div>
<div class="row"><div><label>{L['phone']}</label><input name="phone"{ltr}></div><div><label>{L['product']}</label><input name="product" required{prefill}></div></div>
<div class="row"><div><label>{L['model']}</label><input name="model" list="model-list"{ltr}>{models}</div><div><label>{L['qty']}</label><input name="qty"{qty_req}></div></div>
<div class="row"><div><label>{L['band']}</label><input name="band"></div><div><label>{L['power']}</label><input name="power"></div></div>
<div class="row"><div><label>{L['connector']}</label><input name="connector"></div><div><label>{L['pim']}</label><select name="pim"><option value="no">{L['pno']}</option><option value="yes">{L['pyes']}</option></select></div></div>
<label>{L['msg']}</label><textarea name="message" required></textarea>
{upload}<input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">
<p id="form-error" class="error" role="alert"></p>
<p><button class="btn" type="submit">{L['send']}</button></p>
<p class="note">{L['alt']} <a class="btn ghost" id="wa-link" href="https://wa.me/{WA}" target="_blank" rel="noopener">{L['wa']}</a> <a class="btn ghost" id="mail-link" href="mailto:{EMAIL}">{L['mail']}</a></p>
<p class="note">{L['note']} <a href="{base}privacy/index.html">{L['privacy']}</a>{L['period']}</p>
</form>
<!-- rfq:end -->"""


def put_form(r, source):
    p = ROOT / r
    if not p.exists():
        return
    s = rd(p)
    m = MODELS_RE.search(rd(ROOT / "contact/index.html"))
    models = m.group(0)
    f = form_html(lang_of(r), r, models, source)
    if "<!-- rfq:start -->" in s:
        s = re.sub(r"<!-- rfq:start -->.*?<!-- rfq:end -->", lambda _: f, s, flags=re.S)
    elif '<form id="rfq"' in s:
        s = re.sub(r'<form id="rfq".*?</form>', lambda _: f, s, flags=re.S)
    else:
        lang = lang_of(r)
        if lang == "zh":
            h = "<h2>发来频段方案，直接询价</h2>"
        elif lang == "en":
            h = "<h2>Send the band plan</h2>"
        else:
            h = f"<h2>{tr(lang, 'Send the band plan')}</h2>"
        s = s.replace("</div></section>\n<footer", f"\n{h}\n{f}</div></section>\n<footer", 1)
    wr(p, s)


# ---------------------------------------------------------------- footer
def fix_footer(r, s):
    lang = lang_of(r)
    m = re.search(r'<footer class="site-footer">.*?</footer>', s, re.S)
    if not m: return s
    f = m.group(0)
    if f"mailto:{EMAIL}" not in f:
        # location line may already be translated; match by structure as a fallback
        f = f.replace("<li>Shenzhen, Guangdong, China</li>",
                      f'<li>Shenzhen, Guangdong, China</li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li>', 1)
        f = f.replace("<li>WhatsApp · 张体进</li>", f'<li><a href="https://wa.me/{WA}" target="_blank" rel="noopener">WhatsApp · 张体进</a></li>', 1)
    if "privacy/index.html" not in f:
        pm = re.search(r'(<div><h3>(?:Pages|页面|Страницы|Páginas|الصفحات)</h3><ul><li><a href="([^"]*)index.html">.*?)</ul>', f, re.S)
        if pm:
            b = pm.group(2)
            if lang == "zh":
                extra = f'<li><a href="{b}privacy/index.html">隐私</a></li><li><a href="{b}terms/index.html">条款</a></li>'
            elif lang == "en":
                extra = f'<li><a href="{b}privacy/index.html">Privacy</a></li><li><a href="{b}terms/index.html">Terms</a></li>'
            else:
                extra = (f'<li><a href="{b}privacy/index.html">{tr(lang, "Privacy")}</a></li>'
                         f'<li><a href="{b}terms/index.html">{tr(lang, "Terms")}</a></li>')
            f = f.replace(pm.group(0), pm.group(1) + extra + "</ul>", 1)
    return s.replace(m.group(0), f, 1)


# ---------------------------------------------------------------- head
def text_of(rx, s, default=""):
    m = re.search(rx, s, re.S)
    return html.unescape(re.sub(r"<[^>]+>", "", m.group(1))).strip() if m else default


ORG = {"@type": "Organization", "@id": SITE + "/#org", "name": "Kangxuntong", "alternateName": "康讯通",
       "url": SITE + "/", "logo": SITE + "/assets/logo-lockup.png", "email": EMAIL, "telephone": "+86 186 8871 8926",
       "address": {"@type": "PostalAddress", "addressLocality": "Shenzhen", "addressRegion": "Guangdong", "addressCountry": "CN"},
       "contactPoint": {"@type": "ContactPoint", "contactType": "sales", "email": EMAIL, "telephone": "+86 186 8871 8926",
                        "availableLanguage": ["en", "zh", "ru", "es", "pt", "ar"]}}


def product_ld(r, s, title, desc):
    stem = pathlib.Path(r).stem
    if not is_product(stem): return None
    model = stem.upper()
    name = text_of(r"<h1>(.*?)</h1>", s, model)
    d = {"@context": "https://schema.org", "@type": "Product", "name": f"{model} {name}", "sku": model, "mpn": model,
         "brand": {"@type": "Brand", "name": "Kangxuntong"}, "manufacturer": {"@id": SITE + "/#org", "@type": "Organization", "name": "Kangxuntong"},
         "description": desc, "url": url(r)}
    img = ROOT / "assets" / "drawings" / f"{model}.png"
    if img.exists(): d["image"] = f"{SITE}/assets/drawings/{model}.png"
    pdf = ROOT / "datasheets" / f"{model}.pdf"
    if pdf.exists(): d["subjectOf"] = {"@type": "DigitalDocument", "name": f"{model} datasheet", "url": f"{SITE}/datasheets/{model}.pdf"}
    return d


def seo_block(r, s):
    lang = lang_of(r)
    title = text_of(r"<title>(.*?)</title>", s)
    desc = text_of(r'<meta name="description" content="([^"]*)"', s)
    e = en_of(r)
    if r == "404.html":
        return '<!-- seo:start -->\n<meta name="robots" content="noindex">\n<!-- seo:end -->'
    lines = [f'<link rel="canonical" href="{url(r)}">']
    if r in NOINDEX:
        lines.append('<meta name="robots" content="noindex">')
    alts = []
    for loc in ALL_LOCALES:
        t = loc_rel(e, loc)
        if (ROOT / t).exists():
            alts.append((loc, t))
    if alts:
        for loc, t in alts:
            lines.append(f'<link rel="alternate" hreflang="{loc}" href="{url(t)}">')
        lines.append(f'<link rel="alternate" hreflang="x-default" href="{url(e)}">')
    stem = pathlib.Path(r).stem.upper()
    img = f"{SITE}/assets/drawings/{stem}.png" if (ROOT / "assets/drawings" / f"{stem}.png").exists() else f"{SITE}/assets/hero.jpg"
    is_prod = is_product(pathlib.Path(r).stem)
    lines += [f'<meta property="og:type" content="{"product" if is_prod else "website"}">',
              '<meta property="og:site_name" content="Kangxuntong">',
              f'<meta property="og:title" content="{esc(title)}">',
              f'<meta property="og:description" content="{esc(desc)}">',
              f'<meta property="og:url" content="{url(r)}">',
              f'<meta property="og:image" content="{img}">',
              f'<meta property="og:locale" content="{LOCALES[lang]["og"]}">']
    for alt_og in og_alternates(lang):
        lines.append(f'<meta property="og:locale:alternate" content="{alt_og}">')
    lines.append('<meta name="twitter:card" content="summary_large_image">')
    ld = []
    if e == "index.html":
        ld.append({"@context": "https://schema.org", "@graph": [ORG, {"@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/",
                   "name": "Kangxuntong Cavity Filters", "inLanguage": lang, "publisher": {"@id": SITE + "/#org"}}]})
    elif e.startswith("products/") and is_product(pathlib.Path(e).stem):
        p = product_ld(r, s, title, desc)
        if p: ld.append(p)
    for d in ld:
        lines.append('<script type="application/ld+json">' + json.dumps(d, ensure_ascii=False).replace("</", "<\\/") + "</script>")
    return "<!-- seo:start -->\n" + "\n".join(lines) + "\n<!-- seo:end -->"


def fix_head(r, s):
    s = re.sub(r"\n?<!-- seo:start -->.*?<!-- seo:end -->", "", s, flags=re.S)
    return s.replace("</head>", seo_block(r, s) + "\n</head>", 1)


def fix_misc(r, s):
    lang = lang_of(r)
    def aria(model):
        if lang == "zh":
            return "外形图 " + model
        if lang == "en":
            return "Outline drawing of " + model
        return tr(lang, "Outline drawing of") + " " + model
    def thumb(m):
        prefix = m.group(1) or ""
        model = m.group(2)
        return f'<div class="thumb" role="img" aria-label="{aria(model)}" style="background-image:url({prefix}{model}.png)"></div>'
    s = re.sub(r'<div class="thumb" style="background-image:url\(([^)]*/)?([A-Z0-9-]+)\.png\)"></div>', thumb, s)
    s = re.sub(r'<div class="thumb" role="img" aria-label="[^"]*" style="background-image:url\(([^)]*/)?([A-Z0-9-]+)\.png\)"></div>', thumb, s)
    if is_zh(r) and is_product(pathlib.Path(r).stem) and r.startswith("zh/products/"):
        model = pathlib.Path(r).stem.upper()
        h1 = text_of(r"<h1>(.*?)</h1>", s, model)
        s = re.sub(r"<title>.*?</title>", f"<title>{esc(h1)} {model} | 康讯通</title>", s, count=1)
    return s


# ---------------------------------------------------------------- generated pages
def page_from(template_rel, new_rel, title, desc, body):
    if not (ROOT / template_rel).exists():
        return
    t = rd(ROOT / template_rel)
    head_end = t.index("</header>") + len("</header>")
    foot = t.index('<footer class="site-footer">')
    s = t[:head_end] + "\n" + body + "\n" + t[foot:]
    s = re.sub(r"<title>.*?</title>", f"<title>{esc(title)}</title>", s, count=1)
    s = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{esc(desc)}">', s, count=1)
    nav = switcher_html(new_rel)
    s = re.sub(r'<span class="lang">.*?</span>|<nav class="lang"[^>]*>.*?</nav>', nav, s, count=1, flags=re.S)
    wr(ROOT / new_rel, s)


def generated_pages():
    page_from("contact/index.html", "contact/thanks.html", "Thank you | Kangxuntong", "Your enquiry has been sent to sales@cavityfilter.com.",
              f'<div class="wrap page-hero"><h1>Thank you</h1><p>Your enquiry has been sent to {EMAIL}. We will reply by email.</p></div>'
              f'<section style="padding-top:10px"><div class="wrap prose"><p>If it is urgent, you can also reach us on '
              f'<a href="https://wa.me/{WA}" target="_blank" rel="noopener">WhatsApp +86 186 8871 8926</a> or write to <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>'
              f'<p><a class="btn" href="../products/index.html">Back to the catalog</a></p></div></section>')
    page_from("zh/contact/index.html", "zh/contact/thanks.html", "询价已发送 | 康讯通", "你的询价已发送到 sales@cavityfilter.com。",
              f'<div class="wrap page-hero"><h1>询价已发送</h1><p>询价已发到 {EMAIL}，我们会用邮件回复。</p></div>'
              f'<section style="padding-top:10px"><div class="wrap prose"><p>着急的话，也可以直接 '
              f'<a href="https://wa.me/{WA}" target="_blank" rel="noopener">WhatsApp +86 186 8871 8926</a>，或写信到 <a href="mailto:{EMAIL}">{EMAIL}</a>。</p>'
              f'<p><a class="btn" href="../products/index.html">返回产品目录</a></p></div></section>')

    # VHF/UHF category. Numbers come only from KXT-FF-09 (factory Word sheet) and the 29 May 2026 roster.
    en_body = """<div class="wrap page-hero"><p class="crumbs"><a href="index.html">Products</a> / VHF/UHF duplexers</p><h1>VHF/UHF Duplexers for Two-way Radio / LMR</h1>
<p>Cavity duplexers in the VHF and UHF bands from the factory catalog. Figures below are exactly what the factory sheets state; anything else is confirmed on the quotation and the unit’s test report.</p></div>
<section style="padding-top:10px"><div class="wrap">
<table class="spec"><tbody><tr><th>Model</th><th>Type</th><th>Passbands</th><th>Stated on the factory sheet</th><th></th></tr>
<tr><td><a href="kxt26065.html">KXT26065</a></td><td>Duplexer</td><td>135–210 / 400–500 MHz</td><td>Passbands only (quotation roster, 29 May 2026). Electrical limits are on the unit’s test report.</td><td><a href="kxt26065.html">Model page</a> · <a href="../datasheets/KXT-ROSTER-20260529.pdf">Roster PDF</a> · <a href="../contact/index.html?model=KXT26065">Quote</a></td></tr>
<tr><td><a href="kxt-ff-09.html">KXT-FF-09</a></td><td>UHF cavity duplexer</td><td>452.5–457.5 / 462.5–467.5 MHz</td><td>Insertion loss ≤2.2 dB, VSWR ≤1.3, ripple ≤1.9 dB, rejection ≥80 dB at the other band, isolation ≥80 dB, 50 W average, N-F / SMA-F, 177×134×73.5 mm.</td><td><a href="kxt-ff-09.html">Specification</a> · <a href="../datasheets/KXT-FF-09.pdf">PDF</a> · <a href="../contact/index.html?model=KXT-FF-09">Quote</a></td></tr>
</tbody></table>
<p class="note">Need another VHF or UHF Tx/Rx pair, spacing, power or connector? Send the band plan on the <a href="../custom/index.html">custom design</a> page or write to <a href="mailto:sales@cavityfilter.com">sales@cavityfilter.com</a>.</p>
<p><a class="btn" href="../contact/index.html">Request a quote</a> <a class="btn ghost" href="index.html">Full catalog</a></p>
</div></section>"""
    page_from("products/more.html", "products/vhf-uhf-duplexers.html", "VHF/UHF Duplexers for Two-way Radio / LMR | Kangxuntong",
              "VHF/UHF cavity duplexers for two-way radio (LMR) from a Shenzhen factory: KXT26065 135–210 / 400–500 MHz and KXT-FF-09 452.5–457.5 / 462.5–467.5 MHz. Factory-sheet specifications; test report with each unit.",
              en_body)
    zh_body = """<div class="wrap page-hero"><p class="crumbs"><a href="index.html">产品</a> / VHF/UHF 双工器</p><h1>VHF/UHF 对讲机（专网 LMR）双工器</h1>
<p>工厂目录里 VHF、UHF 频段的腔体双工器。下表只列工厂规格书上写明的数字，其余以报价单和随货测试报告为准。</p></div>
<section style="padding-top:10px"><div class="wrap">
<table class="spec"><tbody><tr><th>型号</th><th>类别</th><th>通带</th><th>工厂规格书写明的指标</th><th></th></tr>
<tr><td><a href="kxt26065.html">KXT26065</a></td><td>双工器</td><td>135–210 / 400–500 MHz</td><td>只有通带（2026 年 5 月 29 日报价货架）。电气指标见该件测试报告。</td><td><a href="kxt26065.html">型号页</a> · <a href="../../datasheets/KXT-ROSTER-20260529.pdf">通带表 PDF</a> · <a href="../contact/index.html?model=KXT26065">询价</a></td></tr>
<tr><td><a href="kxt-ff-09.html">KXT-FF-09</a></td><td>UHF 腔体双工器</td><td>452.5–457.5 / 462.5–467.5 MHz</td><td>插损 ≤2.2 dB，驻波 ≤1.3，波动 ≤1.9 dB，对另一频段抑制 ≥80 dB，隔离 ≥80 dB，平均功率 50 W，N-F / SMA-F，177×134×73.5 mm。</td><td><a href="kxt-ff-09.html">规格</a> · <a href="../../datasheets/KXT-FF-09.pdf">PDF</a> · <a href="../contact/index.html?model=KXT-FF-09">询价</a></td></tr>
</tbody></table>
<p class="note">需要其他 VHF/UHF 收发频点、间隔、功率或接头？到<a href="../custom/index.html">定制</a>页发来频段方案，或写信到 <a href="mailto:sales@cavityfilter.com">sales@cavityfilter.com</a>。</p>
<p><a class="btn" href="../contact/index.html">提交询价</a> <a class="btn ghost" href="index.html">完整目录</a></p>
</div></section>"""
    page_from("zh/products/more.html", "zh/products/vhf-uhf-duplexers.html", "VHF/UHF 对讲机（专网 LMR）双工器 | 康讯通",
              "康讯通深圳工厂的 VHF/UHF 腔体双工器：KXT26065 135–210 / 400–500 MHz，KXT-FF-09 452.5–457.5 / 462.5–467.5 MHz。指标以工厂规格书为准，随货附测试报告。",
              zh_body)
    thanks_en = (
        f'<div class="wrap page-hero"><h1>Thank you</h1><p>Your enquiry has been sent to {EMAIL}. We will reply by email.</p></div>'
        f'<section style="padding-top:10px"><div class="wrap prose"><p>If it is urgent, you can also reach us on '
        f'<a href="https://wa.me/{WA}" target="_blank" rel="noopener">WhatsApp +86 186 8871 8926</a> or write to <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>'
        f'<p><a class="btn" href="../products/index.html">Back to the catalog</a></p></div></section>'
    )
    vhf_title_en = "VHF/UHF Duplexers for Two-way Radio / LMR | Kangxuntong"
    vhf_desc_en = ("VHF/UHF cavity duplexers for two-way radio (LMR) from a Shenzhen factory: "
                   "KXT26065 135–210 / 400–500 MHz and KXT-FF-09 452.5–457.5 / 462.5–467.5 MHz. "
                   "Factory-sheet specifications; test report with each unit.")
    for lang in NEW_LOCALES:
        if not (ROOT / loc_rel("contact/index.html", lang)).exists():
            continue
        page_from(loc_rel("contact/index.html", lang), loc_rel("contact/thanks.html", lang),
                  tr(lang, "Thank you | Kangxuntong"),
                  tr(lang, "Your enquiry has been sent to sales@cavityfilter.com."),
                  translate_fragment(lang, thanks_en))
        tmpl = loc_rel("products/more.html", lang)
        if (ROOT / tmpl).exists():
            page_from(tmpl, loc_rel("products/vhf-uhf-duplexers.html", lang),
                      tr(lang, vhf_title_en), tr(lang, vhf_desc_en),
                      translate_fragment(lang, en_body))


def catalog_link():
    items = [
        ("products/index.html", "VHF/UHF Duplexers for Two-way Radio / LMR"),
        ("zh/products/index.html", "VHF/UHF 对讲机（专网 LMR）双工器"),
    ]
    for lang in NEW_LOCALES:
        items.append((loc_rel("products/index.html", lang),
                      tr(lang, "VHF/UHF Duplexers for Two-way Radio / LMR")))
    for r, txt in items:
        path = ROOT / r
        if not path.exists():
            continue
        s = rd(path)
        if "vhf-uhf-duplexers.html" not in s:
            s = s.replace('<div class="filters">', f'<p><a class="btn ghost" href="vhf-uhf-duplexers.html">{txt} →</a></p>\n<div class="filters">', 1)
        wr(path, s)


# ---------------------------------------------------------------- shelf model pages
# The 12 models on the 29 May 2026 quotation (KXT-ROSTER-20260529.pdf). The
# roster gives model, type and passband only, plus the series interface
# (50 Ω, indoor, aluminum cavity). Nothing else is stated, so nothing else is
# printed: every other row says "on the test report" or "state on the enquiry".
SHELF = [  # (model, type, passbands)
    ("KXT26050", "bpf", "758–788 MHz"),
    ("KXT26051", "bpf", "869–880 / 935–960 MHz"),
    ("KXT26052", "bpf", "2010–2025 / 2110–2170 MHz"),
    ("KXT26053", "bpf", "2300–2370 MHz"),
    ("KXT26054", "bpf", "2515–2675 MHz"),
    ("KXT26055", "bpf", "3300–3600 MHz"),
    ("KXT26056", "bpf", "4800–4960 MHz"),
    ("KXT26048", "bpf", "1805–1880 / 1885–1915 MHz"),
    ("KXT26057", "dup", "791–821 / 925–940 MHz"),
    ("KXT26058", "dup", "758–788 / 940–960 MHz"),
    ("KXT26059", "dup", "1559–1610 / 1164–1301 MHz"),
    ("KXT26065", "dup", "135–210 / 400–500 MHz"),
]
TYPE_EN = {"bpf": "Cavity Bandpass Filter", "dup": "Cavity Duplexer"}
TYPE_ZH = {"bpf": "腔体带通滤波器", "dup": "腔体双工器"}
TYPE_ROSTER_EN = {"bpf": "Bandpass filter", "dup": "Duplexer"}
TYPE_ROSTER_ZH = {"bpf": "滤波器", "dup": "双工器"}


def shelf_page(model, typ, band, zh):
    low = model.lower()
    if zh:
        rows = [("型号", model), ("类别（报价单原文）", TYPE_ROSTER_ZH[typ]), ("工作频段", band),
                ("阻抗", "50 Ω（系列接口规范）"), ("结构", "室内型，铝合金腔体（系列接口规范）"),
                ("插入损耗 / 波动 / 抑制", "报价单未写，以该件出厂测试报告为准"),
                ("功率", "—，请询价时说明"), ("接头", "—，请询价时说明"), ("尺寸", "—，请联系我们"),
                ("低互调档", "订货选项，报价时确认")]
        extra = ""
        if model == "KXT26065":
            extra = ('<p>VHF/UHF 专网（LMR）用途的双工器，另见 <a href="vhf-uhf-duplexers.html">VHF/UHF 双工器</a>'
                     ' 和 <a href="../applications/private-networks.html">TETRA / P25 / DMR 专网</a>。</p>')
        body = f"""<div class="wrap page-hero"><p class="crumbs"><a href="index.html">产品</a> / {model}</p>
<h1>{TYPE_ZH[typ]} {band}</h1><p class="kicker">{model} · 2026 年 5 月 29 日报价货架</p></div>
<section style="padding-top:10px"><div class="wrap layout">
<div>
<h2>报价单写明的内容</h2>
<table class="spec"><tbody>{''.join(f'<tr><th>{a}</th><td>{b}</td></tr>' for a, b in rows)}</tbody></table>
<p class="note">这个型号来自公司报价单上的在售货架。报价单只给出通带，没有给出插损和抑制；本页不借用其他型号的电气数值。标“—”的项目以报价单和随货测试报告为准。</p>
{extra}</div>
<aside class="side">
<div class="card"><h3>{model}</h3>
<p><a class="btn" href="../contact/index.html?model={model}">询价</a></p>
<p><a class="btn ghost" href="../../datasheets/KXT-ROSTER-20260529.pdf">货架型号清单 PDF</a></p>
</div>
<div class="card"><h3>订货</h3><p>{model} + 接头 + 功率 + 是否低互调档 + 数量</p><p>需要不同通带？到<a href="../custom/index.html">定制</a>页发来频段方案。</p></div>
</aside>
</div></section>"""
        title = f"{TYPE_ZH[typ]} {band} {model} | 康讯通"
        desc = f"{model} {TYPE_ZH[typ]}，通带 {band}。2026 年 5 月 29 日报价货架型号，50 Ω 室内铝合金腔体，电气指标以随货测试报告为准。"
        page_from("zh/products/kxt-bf-703748.html", f"zh/products/{low}.html", title, desc, body)
    else:
        rows = [("Model", model), ("Type (as on the quotation)", TYPE_ROSTER_EN[typ]), ("Passband", band),
                ("Impedance", "50 Ω (series interface)"), ("Construction", "Indoor, aluminum cavity (series interface)"),
                ("Insertion loss / ripple / rejection", "Not stated on the quotation; on the unit’s factory test report"),
                ("Power", "—, state it on the enquiry"), ("Connector", "—, state it on the enquiry"), ("Outline", "—, contact us"),
                ("Low-PIM option", "Order option, confirmed on the quotation")]
        extra = ""
        if model == "KXT26065":
            extra = ('<p>A duplexer for VHF/UHF private radio (LMR). See also <a href="vhf-uhf-duplexers.html">VHF/UHF duplexers</a>'
                     ' and <a href="../applications/private-networks.html">TETRA / P25 / DMR networks</a>.</p>')
        body = f"""<div class="wrap page-hero"><p class="crumbs"><a href="index.html">Products</a> / {model}</p>
<h1>{TYPE_EN[typ]} {band}</h1><p class="kicker">{model} · Quotation shelf, 29 May 2026</p></div>
<section style="padding-top:10px"><div class="wrap layout">
<div>
<h2>What the quotation states</h2>
<table class="spec"><tbody>{''.join(f'<tr><th>{a}</th><td>{b}</td></tr>' for a, b in rows)}</tbody></table>
<p class="note">This model is on the commercial shelf of the company quotation. The quotation gives the passband only, not insertion loss or rejection, and this page does not borrow electrical limits from other models. Rows marked “—” are settled on the quotation and the unit’s test report.</p>
{extra}</div>
<aside class="side">
<div class="card"><h3>{model}</h3>
<p><a class="btn" href="../contact/index.html?model={model}">Request a quote</a></p>
<p><a class="btn ghost" href="../datasheets/KXT-ROSTER-20260529.pdf">Shelf model list PDF</a></p>
</div>
<div class="card"><h3>Ordering</h3><p>{model} + connector + power + low-PIM option + quantity</p><p>Need a different passband? Send the band plan on the <a href="../custom/index.html">custom design</a> page.</p></div>
</aside>
</div></section>"""
        title = f"{model} {TYPE_EN[typ]} {band} | Kangxuntong"
        desc = f"{model} {TYPE_EN[typ].lower()}, passband {band}. Shelf model from the 29 May 2026 quotation; 50 Ω indoor aluminum cavity. Electrical limits are on the unit’s test report."
        page_from("products/kxt-bf-703748.html", f"products/{low}.html", title, desc, body)


def shelf_pages():
    for model, typ, band in SHELF:
        shelf_page(model, typ, band, False)
        shelf_page(model, typ, band, True)
        for lang in NEW_LOCALES:
            if (ROOT / loc_rel("products/kxt-bf-703748.html", lang)).exists():
                shelf_page_locale(model, typ, band, lang)
    # link the shelf rows on the catalog (the VHF/UHF page links KXT26065 in its own body)
    for loc in ALL_LOCALES:
        r = loc_rel("products/index.html", loc)
        path = ROOT / r
        if not path.exists():
            continue
        s = rd(path)
        for model, _, _ in SHELF:
            s = s.replace(f"<td>{model}</td>", f'<td><a href="{model.lower()}.html">{model}</a></td>')
        wr(path, s)


def shelf_page_locale(model, typ, band, lang):
    """Build a translated shelf page from the English template."""
    low = model.lower()
    # Reuse the English body by temporarily rendering it, then translating.
    # Datasheet path must climb to the site root (one extra ../ under /ru/ etc.).
    rows = [("Model", model), ("Type (as on the quotation)", TYPE_ROSTER_EN[typ]), ("Passband", band),
            ("Impedance", "50 Ω (series interface)"), ("Construction", "Indoor, aluminum cavity (series interface)"),
            ("Insertion loss / ripple / rejection", "Not stated on the quotation; on the unit’s factory test report"),
            ("Power", "—, state it on the enquiry"), ("Connector", "—, state it on the enquiry"), ("Outline", "—, contact us"),
            ("Low-PIM option", "Order option, confirmed on the quotation")]
    extra = ""
    if model == "KXT26065":
        extra = ('<p>A duplexer for VHF/UHF private radio (LMR). See also <a href="vhf-uhf-duplexers.html">VHF/UHF duplexers</a>'
                 ' and <a href="../applications/private-networks.html">TETRA / P25 / DMR networks</a>.</p>')
    body = f"""<div class="wrap page-hero"><p class="crumbs"><a href="index.html">Products</a> / {model}</p>
<h1>{TYPE_EN[typ]} {band}</h1><p class="kicker">{model} · Quotation shelf, 29 May 2026</p></div>
<section style="padding-top:10px"><div class="wrap layout">
<div>
<h2>What the quotation states</h2>
<table class="spec"><tbody>{''.join(f'<tr><th>{a}</th><td>{b}</td></tr>' for a, b in rows)}</tbody></table>
<p class="note">This model is on the commercial shelf of the company quotation. The quotation gives the passband only, not insertion loss or rejection, and this page does not borrow electrical limits from other models. Rows marked “—” are settled on the quotation and the unit’s test report.</p>
{extra}</div>
<aside class="side">
<div class="card"><h3>{model}</h3>
<p><a class="btn" href="../contact/index.html?model={model}">Request a quote</a></p>
<p><a class="btn ghost" href="../../datasheets/KXT-ROSTER-20260529.pdf">Shelf model list PDF</a></p>
</div>
<div class="card"><h3>Ordering</h3><p>{model} + connector + power + low-PIM option + quantity</p><p>Need a different passband? Send the band plan on the <a href="../custom/index.html">custom design</a> page.</p></div>
</aside>
</div></section>"""
    title = f"{model} {TYPE_EN[typ]} {band} | Kangxuntong"
    desc = (f"{model} {TYPE_EN[typ].lower()}, passband {band}. "
            "Shelf model from the 29 May 2026 quotation; 50 Ω indoor aluminum cavity. Electrical limits are on the unit’s test report.")
    page_from(loc_rel("products/kxt-bf-703748.html", lang), loc_rel(f"products/{low}.html", lang),
              tr(lang, title), tr(lang, desc), translate_fragment(lang, body))



# ---------------------------------------------------------------- application sub-pages
APPS_EN = {
"applications/private-networks.html": ("Private Radio Networks: TETRA, P25 and DMR | Kangxuntong",
"Cavity duplexers, bandpass filters and combiners for TETRA, P25 and DMR private radio (LMR) base stations and repeaters. Typical bands, where the filters go, and what to send for a quotation.",
"""<div class="wrap page-hero"><p class="crumbs"><a href="index.html">Applications</a> / Private radio networks</p><h1>Private Radio Networks: TETRA, P25 and DMR</h1>
<p>Public safety, utilities, transport and industrial sites run their own two-way radio (LMR / PMR) networks. Cavity filters sit at the base station and repeater sites of these networks.</p></div>
<section style="padding-top:10px"><div class="wrap prose">
<h2>Where the systems operate</h2>
<p>Frequencies are set by each country’s regulator and each licence. The usual ranges are:</p>
<table class="spec"><tbody><tr><th>System</th><th>Standard</th><th>Typical bands</th></tr>
<tr><td>TETRA</td><td>ETSI EN 300 392</td><td>380–400 MHz (public safety in many countries), 410–430 MHz, 450–470 MHz; 800 MHz in some regions</td></tr>
<tr><td>P25 (APCO-25)</td><td>TIA-102</td><td>VHF 136–174 MHz, UHF 380–512 MHz, 700 MHz and 800 MHz public-safety bands</td></tr>
<tr><td>DMR</td><td>ETSI TS 102 361</td><td>VHF 136–174 MHz, UHF 400–470 MHz</td></tr>
</tbody></table>
<h2>Where cavity filters go</h2>
<ul>
<li><strong>Repeater duplexer.</strong> Transmit and receive share one antenna. The duplexer passes each half of the pair and isolates the receiver from the transmitter at the duplex spacing.</li>
<li><strong>Receiver protection.</strong> A bandpass cavity in front of the receiver rejects nearby transmitters on shared towers.</li>
<li><strong>Transmitter combining.</strong> Multi-channel and trunked sites combine several transmitters onto one antenna.</li>
<li><strong>Coexistence with cellular.</strong> Band filters keep LTE and 5G energy out of the radio path, and the other way round.</li>
</ul>
<h2>Related products</h2>
<ul>
<li><a href="../products/kxt-ff-09.html">KXT-FF-09</a>: UHF cavity duplexer, 452.5–457.5 / 462.5–467.5 MHz (factory sheet).</li>
<li><a href="../products/kxt26065.html">KXT26065</a>: duplexer, 135–210 / 400–500 MHz (passbands only on the quotation).</li>
<li><a href="../products/vhf-uhf-duplexers.html">All VHF/UHF duplexers</a></li>
</ul>
<h2>What to send for a quotation</h2>
<p>Tx and Rx frequencies (or band and duplex spacing), channels and power per channel, the isolation or rejection you need, connector, and quantity. Use the <a href="../custom/index.html">custom design</a> form; a drawing or site plan can be attached.</p>
<p><a class="btn" href="../custom/index.html">Send a band plan</a> <a class="btn ghost" href="index.html">All applications</a></p>
</div></section>"""),
"applications/das-erces.html": ("In-building DAS and Emergency Responder Radio (ERCES) | Kangxuntong",
"Cavity bandpass filters, duplexers and combiners for in-building distributed antenna systems (DAS) and emergency responder radio coverage systems (ERCES): bands, filter positions and what to send.",
"""<div class="wrap page-hero"><p class="crumbs"><a href="index.html">Applications</a> / In-building DAS and ERCES</p><h1>In-building DAS and Emergency Responder Radio (ERCES)</h1>
<p>A distributed antenna system (DAS) carries cellular and public-safety radio signals inside a building. Cavity filters decide which bands enter it and keep them apart.</p></div>
<section style="padding-top:10px"><div class="wrap prose">
<h2>Emergency responder radio coverage</h2>
<p>In the United States many jurisdictions require in-building coverage for fire and police radio. The requirement comes from the International Fire Code (section 510) and NFPA 1225, as adopted locally. The authority having jurisdiction (AHJ) sets the frequencies, the coverage targets and the acceptance test. System listings and acceptance are handled by the system integrator with the AHJ.</p>
<h2>Bands commonly carried</h2>
<table class="spec"><tbody><tr><th>Service</th><th>Typical frequencies</th></tr>
<tr><td>VHF / UHF public safety</td><td>150–174 MHz, 450–470 MHz (470–512 MHz in some cities)</td></tr>
<tr><td>700 MHz public safety, incl. FirstNet Band 14</td><td>758–768 / 788–798 MHz (Band 14); 769–775 / 799–805 MHz (narrowband)</td></tr>
<tr><td>800 MHz public safety</td><td>806–824 / 851–869 MHz</td></tr>
<tr><td>Cellular DAS</td><td>LTE and 5G bands of the operators served, e.g. Band 28, 20, 8, 3, 1, 7 and n78</td></tr>
</tbody></table>
<h2>Where cavity filters go</h2>
<ul>
<li><strong>Signal booster / BDA band selection.</strong> Pass the licensed channels, reject adjacent services.</li>
<li><strong>Point of interface (POI).</strong> Band combiners and duplexers join several operators’ signal sources onto the DAS.</li>
<li><strong>Shared cabling.</strong> Combiners and diplexers separate public-safety and cellular systems on one riser.</li>
<li><strong>Low PIM.</strong> Passive intermodulation from strong downlink carriers can land in uplink bands, so low-PIM parts matter at the POI. Low PIM is an order option on our datasheets.</li>
</ul>
<h2>Related products</h2>
<ul>
<li><a href="../products/kxt-bf-758803.html">KXT-BF-758803</a>: bandpass, 758–803 MHz.</li>
<li><a href="../products/kxt-cm4-wide.html">KXT-CM4-WIDE</a>: 4-port combiner, 758–960 / 1805–1920 / 2010–2170 / 2310–2675 MHz.</li>
<li><a href="../products/vhf-uhf-duplexers.html">VHF/UHF duplexers</a> for the public-safety radio side.</li>
<li><a href="../products/index.html">Cellular bandpass filters and combiners</a></li>
</ul>
<h2>What to send for a quotation</h2>
<p>The band plan for each system, the rejection or isolation between them, power at the filter, connector, and quantity. A riser diagram or POI drawing can be attached on the <a href="../custom/index.html">custom design</a> form.</p>
<p><a class="btn" href="../custom/index.html">Send a band plan</a> <a class="btn ghost" href="index.html">All applications</a></p>
</div></section>"""),
}
APPS_ZH = {
"zh/applications/private-networks.html": ("TETRA、P25、DMR 专网对讲 | 康讯通",
"用于 TETRA、P25、DMR 专网对讲（LMR）基站和中继台的腔体双工器、带通滤波器和合路器：常见频段、滤波器装在哪里、询价要发什么。",
"""<div class="wrap page-hero"><p class="crumbs"><a href="index.html">应用</a> / 专网对讲</p><h1>TETRA、P25、DMR 专网对讲</h1>
<p>公安消防、电力、交通和工矿企业都有自己的对讲专网（LMR / PMR）。腔体滤波器装在这些网络的基站和中继台上。</p></div>
<section style="padding-top:10px"><div class="wrap prose">
<h2>系统工作在哪些频段</h2>
<p>具体频点由各国监管部门和执照决定。常见范围：</p>
<table class="spec"><tbody><tr><th>系统</th><th>标准</th><th>常见频段</th></tr>
<tr><td>TETRA</td><td>ETSI EN 300 392</td><td>380–400 MHz（许多国家的公共安全频段）、410–430 MHz、450–470 MHz；部分地区用 800 MHz</td></tr>
<tr><td>P25（APCO-25）</td><td>TIA-102</td><td>VHF 136–174 MHz、UHF 380–512 MHz，以及 700 MHz、800 MHz 公共安全频段</td></tr>
<tr><td>DMR</td><td>ETSI TS 102 361</td><td>VHF 136–174 MHz、UHF 400–470 MHz</td></tr>
</tbody></table>
<h2>腔体滤波器装在哪里</h2>
<ul>
<li><strong>中继台双工器。</strong>收发共用一副天线。双工器分别通过收、发频段，在双工间隔上把接收机和发射机隔开。</li>
<li><strong>接收保护。</strong>接收机前加带通腔体，压住同塔附近的发射机。</li>
<li><strong>发射合路。</strong>多信道和集群站把几台发射机合到一副天线上。</li>
<li><strong>与蜂窝网共存。</strong>频段滤波器把 LTE、5G 的能量挡在对讲通路外，反过来也一样。</li>
</ul>
<h2>相关产品</h2>
<ul>
<li><a href="../products/kxt-ff-09.html">KXT-FF-09</a>：UHF 腔体双工器，452.5–457.5 / 462.5–467.5 MHz（工厂规格书）。</li>
<li><a href="../products/kxt26065.html">KXT26065</a>：双工器，135–210 / 400–500 MHz（报价单只列了通带）。</li>
<li><a href="../products/vhf-uhf-duplexers.html">全部 VHF/UHF 双工器</a></li>
</ul>
<h2>询价要发什么</h2>
<p>收发频点（或频段与双工间隔）、信道数和单信道功率、需要的隔离或抑制、接头和数量。用<a href="../custom/index.html">定制</a>页的表单提交，可以附图纸或站点方案。</p>
<p><a class="btn" href="../custom/index.html">发频段方案</a> <a class="btn ghost" href="index.html">全部应用</a></p>
</div></section>"""),
"zh/applications/das-erces.html": ("室内分布 DAS 与应急通信覆盖（ERCES） | 康讯通",
"用于室内分布系统（DAS）和应急救援无线覆盖系统（ERCES）的腔体带通滤波器、双工器和合路器：常见频段、滤波器装在哪里、询价要发什么。",
"""<div class="wrap page-hero"><p class="crumbs"><a href="index.html">应用</a> / 室内分布与 ERCES</p><h1>室内分布 DAS 与应急通信覆盖（ERCES）</h1>
<p>室内分布系统（DAS）把蜂窝和公共安全对讲信号送进楼内。腔体滤波器决定哪些频段进入系统，并把它们彼此隔开。</p></div>
<section style="padding-top:10px"><div class="wrap prose">
<h2>应急救援无线覆盖</h2>
<p>在美国，许多地区要求楼内有消防、警务对讲覆盖。依据是《国际消防规范》（IFC）第 510 节和 NFPA 1225，按当地采纳的版本执行。频点、覆盖指标和验收测试由当地主管部门（AHJ）确定。系统认证与验收由系统集成商和主管部门对接。</p>
<h2>常见频段</h2>
<table class="spec"><tbody><tr><th>业务</th><th>常见频率</th></tr>
<tr><td>VHF / UHF 公共安全</td><td>150–174 MHz、450–470 MHz（部分城市 470–512 MHz）</td></tr>
<tr><td>700 MHz 公共安全，含 FirstNet Band 14</td><td>758–768 / 788–798 MHz（Band 14）；769–775 / 799–805 MHz（窄带）</td></tr>
<tr><td>800 MHz 公共安全</td><td>806–824 / 851–869 MHz</td></tr>
<tr><td>蜂窝室分</td><td>所服务运营商的 LTE、5G 频段，如 Band 28、20、8、3、1、7 和 n78</td></tr>
</tbody></table>
<h2>腔体滤波器装在哪里</h2>
<ul>
<li><strong>信号放大器 / BDA 选频。</strong>通过有执照的信道，抑制相邻业务。</li>
<li><strong>多系统接入平台（POI）。</strong>频段合路器和双工器把几家运营商的信源接入同一套室分。</li>
<li><strong>共用线缆。</strong>合路器、分频器在同一竖井里把公共安全系统和蜂窝系统分开。</li>
<li><strong>低互调。</strong>强下行载波产生的无源互调可能落进上行频段，所以 POI 处要用低互调器件。低互调是我们规格书上的订货档。</li>
</ul>
<h2>相关产品</h2>
<ul>
<li><a href="../products/kxt-bf-758803.html">KXT-BF-758803</a>：带通，758–803 MHz。</li>
<li><a href="../products/kxt-cm4-wide.html">KXT-CM4-WIDE</a>：四端口合路器，758–960 / 1805–1920 / 2010–2170 / 2310–2675 MHz。</li>
<li>对讲侧用的 <a href="../products/vhf-uhf-duplexers.html">VHF/UHF 双工器</a></li>
<li><a href="../products/index.html">蜂窝带通滤波器与合路器</a></li>
</ul>
<h2>询价要发什么</h2>
<p>每个系统的频段方案、系统之间需要的抑制或隔离、滤波器处的功率、接头和数量。可以在<a href="../custom/index.html">定制</a>页的表单里附上竖井图或 POI 图纸。</p>
<p><a class="btn" href="../custom/index.html">发频段方案</a> <a class="btn ghost" href="index.html">全部应用</a></p>
</div></section>"""),
}


def app_pages():
    for r, (t, d, b) in APPS_EN.items(): page_from("applications/index.html", r, t, d, b)
    for r, (t, d, b) in APPS_ZH.items(): page_from("zh/applications/index.html", r, t, d, b)
    for lang in NEW_LOCALES:
        tmpl = loc_rel("applications/index.html", lang)
        if not (ROOT / tmpl).exists():
            continue
        for r, (t, d, b) in APPS_EN.items():
            page_from(tmpl, loc_rel(r, lang), tr(lang, t), tr(lang, d), translate_fragment(lang, b))


# ---------------------------------------------------------------- 404
def page_404():
    """404.html is served for any missing path, so every link is root-absolute."""
    t = rd(ROOT / "index.html")
    head_end = t.index("</header>") + len("</header>")
    foot = t.index('<footer class="site-footer">')
    body = """<div class="wrap page-hero"><p class="kicker">404</p><h1>Page not found</h1>
<p>The page you asked for is not here. It may have moved when the catalog was reorganized.</p></div>
<section style="padding-top:10px"><div class="wrap prose">
<p><a class="btn" href="products/index.html">Product catalog</a> <a class="btn ghost" href="index.html">Home</a> <a class="btn ghost" href="contact/index.html">Contact</a></p>
<p>Looking for a model? Write to <a href="mailto:sales@cavityfilter.com">sales@cavityfilter.com</a> with the model number or the band plan.</p>
<p lang="zh">页面不存在。<a href="/zh/">返回中文首页</a> · <a href="/zh/products/index.html">产品目录</a></p>
<p lang="ru">Страница не найдена. <a href="/ru/">На главную (RU)</a> · <a href="/ru/products/index.html">Каталог</a></p>
<p lang="es">Página no encontrada. <a href="/es/">Inicio (ES)</a> · <a href="/es/products/index.html">Catálogo</a></p>
<p lang="pt">Página não encontrada. <a href="/pt/">Início (PT)</a> · <a href="/pt/products/index.html">Catálogo</a></p>
<p lang="ar" dir="rtl">الصفحة غير موجودة. <a href="/ar/">الرئيسية (AR)</a> · <a href="/ar/products/index.html">الكتالوج</a></p>
</div></section>"""
    s = t[:head_end] + "\n" + body + "\n" + t[foot:]
    s = re.sub(r"<title>.*?</title>", "<title>Page not found | Kangxuntong</title>", s, count=1)
    s = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="Page not found.">', s, count=1)
    s = re.sub(r'(href|src)="(?!https?:|mailto:|tel:|#|/)([^"]*)"', r'\1="/\2"', s)
    s = s.replace('href="/index.html"', 'href="/"')
    for loc in ALL_LOCALES:
        if loc == "en":
            continue
        s = s.replace(f'href="/{loc}/index.html"', f'href="/{loc}/"')
    s = re.sub(r'<span class="lang">.*?</span>|<nav class="lang"[^>]*>.*?</nav>', switcher_html("404.html"), s, count=1, flags=re.S)
    wr(ROOT / "404.html", s)


# ---------------------------------------------------------------- sitemap
def sitemap(pages):
    today = datetime.date.today().isoformat()
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for r in pages:
        if r in NOINDEX: continue
        out.append("  <url>")
        out.append(f"    <loc>{html.escape(url(r))}</loc>")
        out.append(f"    <lastmod>{today}</lastmod>")
        e = en_of(r)
        alts = []
        for loc in ALL_LOCALES:
            t = loc_rel(e, loc)
            if (ROOT / t).exists():
                alts.append((loc, t))
        if alts:
            for hl, t in alts:
                out.append(f'    <xhtml:link rel="alternate" hreflang="{hl}" href="{html.escape(url(t))}"/>')
            out.append(f'    <xhtml:link rel="alternate" hreflang="x-default" href="{html.escape(url(e))}"/>')
        out.append("  </url>")
    out.append("</urlset>")
    wr(ROOT / "sitemap.xml", "\n".join(out) + "\n")
    wr(ROOT / "robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    old = ROOT / "sitemap.txt"
    if old.exists(): old.unlink()


def fix_switcher(r, s):
    nav = switcher_html(r)
    return re.sub(r'<span class="lang">.*?</span>|<nav class="lang"[^>]*>.*?</nav>', nav, s, count=1, flags=re.S)


def main():
    generated_pages()
    shelf_pages()
    app_pages()
    page_404()
    catalog_link()
    for loc in ALL_LOCALES:
        put_form(loc_rel("contact/index.html", loc), "contact")
        put_form(loc_rel("custom/index.html", loc), "custom")
    pages = sorted(rel(p) for p in ROOT.rglob("*.html"))
    for r in pages:
        p = ROOT / r
        s = rd(p)
        s = fix_misc(r, s)
        s = fix_footer(r, s)
        s = fix_switcher(r, s)
        s = fix_head(r, s)
        wr(p, s)
    sitemap(pages)
    print(f"{len(pages)} pages processed")


if __name__ == "__main__":
    main()
