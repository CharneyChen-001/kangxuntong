#!/usr/bin/env python3
"""Shared head/footer/form/SEO pass over the static site in website/.

Idempotent: run it after editing any page.
    python3 tools/build_site.py
What it does (and nothing else):
  * <head>: canonical, hreflang en/zh/x-default, Open Graph, JSON-LD
    (Organization + WebSite on the home pages, Product on product pages),
    written between <!-- seo:start --> and <!-- seo:end -->.
  * footer: sales@cavityfilter.com, clickable WhatsApp, Privacy and Terms.
  * the RFQ form (contact + custom pages, EN and ZH) posting to FormSubmit.
  * generated pages: contact/thanks.html, products/vhf-uhf-duplexers.html
    (EN and ZH).
  * sitemap.xml (absolute URLs + hreflang) and robots.txt.
Specification numbers are never generated here; they live in the pages.
"""
import html, json, pathlib, re, datetime

SITE = "https://cavityfilter.com"
EMAIL = "sales@cavityfilter.com"
WA = "8618688718926"
ROOT = pathlib.Path(__file__).resolve().parent.parent / "website"
FORM_ACTION = f"https://formsubmit.co/{EMAIL}"
NOINDEX = {"contact/thanks.html", "zh/contact/thanks.html"}


def rd(p): return p.read_text(encoding="utf-8")
def wr(p, s):
    if not p.exists() or rd(p) != s:
        p.write_text(s, encoding="utf-8")


def rel(p): return p.relative_to(ROOT).as_posix()
def is_zh(r): return r.startswith("zh/")
def en_of(r): return r[3:] if is_zh(r) else r
def zh_of(r): return r if is_zh(r) else "zh/" + r
def up(r): return "../" * r.count("/")          # path from page to website root


def url(r):
    if r == "index.html": return SITE + "/"
    if r.endswith("/index.html"): return f"{SITE}/{r[:-len('index.html')]}"
    return f"{SITE}/{r}"


def esc(s): return html.escape(s, quote=True)


# ---------------------------------------------------------------- form
MODELS_RE = re.compile(r'<datalist id="model-list">.*?</datalist>', re.S)


def form_html(lang, r, models, source):
    zh = lang == "zh"
    base = "../" * (r.count("/") - 1) if zh else up(r)  # path to the root of this language
    thanks = url("zh/contact/thanks.html" if zh else "contact/thanks.html")
    L = (dict(err="请填写姓名、公司、有效邮箱、国家、产品和需求。", name="姓名", company="公司", email="邮箱", country="国家或地区",
              phone="电话 / WhatsApp", product="产品或型号", model="型号", qty="数量", band="频段", power="功率", connector="接头",
              pim="是否要低互调档", pno="不需要", pyes="需要，≤ −150 dBc", msg="需求说明", send="发送询价",
              alt="也可以：", wa="用 WhatsApp 发送", mail="发邮件到 " + EMAIL,
              note="提交后询价直接发到 " + EMAIL + "，我们用邮件回复。表单经 FormSubmit（formsubmit.co）转发，见", privacy="隐私说明",
              sending="正在发送…", fail="发送失败。请改用邮件或 WhatsApp，内容已保留在表单里。", subj="新询价 · cavityfilter.com（中文站）")
         if zh else
         dict(err="Enter your name, company, a valid email, country, product and message.", name="Name", company="Company",
              email="Work email", country="Country", phone="Phone / WhatsApp", product="Product or model", model="Model",
              qty="Quantity", band="Frequency plan", power="Power", connector="Connector", pim="Low-PIM option",
              pno="Not required", pyes="Required, ≤ −150 dBc", msg="Message", send="Send enquiry",
              alt="Or:", wa="Send on WhatsApp", mail="Email " + EMAIL,
              note="The enquiry goes straight to " + EMAIL + " and we reply by email. The form is relayed by FormSubmit (formsubmit.co); see the",
              privacy="privacy note", sending="Sending…",
              fail="Sending failed. Please use email or WhatsApp instead; your text is still in the form.",
              subj="New RFQ · cavityfilter.com"))
    prefill = (' value="定制"' if zh else ' value="Custom design"') if source == "custom" else ""
    return f"""<!-- rfq:start -->
<form id="rfq" action="{FORM_ACTION}" method="POST" data-ajax="https://formsubmit.co/ajax/{EMAIL}" data-wa="{WA}" data-error="{esc(L['err'])}" data-sending="{esc(L['sending'])}" data-fail="{esc(L['fail'])}">
<input type="hidden" name="_subject" value="{esc(L['subj'])}">
<input type="hidden" name="_next" value="{thanks}">
<input type="hidden" name="_template" value="table">
<input type="hidden" name="_captcha" value="false">
<input type="hidden" name="page" value="{url(r)}">
<div class="row"><div><label>{L['name']}</label><input name="name" required></div><div><label>{L['company']}</label><input name="company" required></div></div>
<div class="row"><div><label>{L['email']}</label><input name="email" type="email" required></div><div><label>{L['country']}</label><input name="country" required></div></div>
<div class="row"><div><label>{L['phone']}</label><input name="phone"></div><div><label>{L['product']}</label><input name="product" required{prefill}></div></div>
<div class="row"><div><label>{L['model']}</label><input name="model" list="model-list">{models}</div><div><label>{L['qty']}</label><input name="qty"></div></div>
<div class="row"><div><label>{L['band']}</label><input name="band"></div><div><label>{L['power']}</label><input name="power"></div></div>
<div class="row"><div><label>{L['connector']}</label><input name="connector"></div><div><label>{L['pim']}</label><select name="pim"><option value="no">{L['pno']}</option><option value="yes">{L['pyes']}</option></select></div></div>
<label>{L['msg']}</label><textarea name="message" required></textarea>
<input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">
<p id="form-error" class="error" role="alert"></p>
<p><button class="btn" type="submit">{L['send']}</button></p>
<p class="note">{L['alt']} <a class="btn ghost" id="wa-link" href="https://wa.me/{WA}" target="_blank" rel="noopener">{L['wa']}</a> <a class="btn ghost" id="mail-link" href="mailto:{EMAIL}">{L['mail']}</a></p>
<p class="note">{L['note']} <a href="{base}privacy/index.html">{L['privacy']}</a>{'。' if zh else '.'}</p>
</form>
<!-- rfq:end -->"""


def put_form(r, source):
    p = ROOT / r
    s = rd(p)
    m = MODELS_RE.search(rd(ROOT / "contact/index.html"))
    models = m.group(0)
    f = form_html("zh" if is_zh(r) else "en", r, models, source)
    if "<!-- rfq:start -->" in s:
        s = re.sub(r"<!-- rfq:start -->.*?<!-- rfq:end -->", lambda _: f, s, flags=re.S)
    elif '<form id="rfq"' in s:
        s = re.sub(r'<form id="rfq".*?</form>', lambda _: f, s, flags=re.S)
    else:  # custom pages: add a heading + the form at the end of the prose block
        h = "<h2>发来频段方案，直接询价</h2>" if is_zh(r) else "<h2>Send the band plan</h2>"
        s = s.replace("</div></section>\n<footer", f"\n{h}\n{f}</div></section>\n<footer", 1)
    wr(p, s)


# ---------------------------------------------------------------- footer
def fix_footer(r, s):
    zh = is_zh(r)
    m = re.search(r'<footer class="site-footer">.*?</footer>', s, re.S)
    if not m: return s
    f = m.group(0)
    if f"mailto:{EMAIL}" not in f:
        f = f.replace("<li>Shenzhen, Guangdong, China</li>",
                      f'<li>Shenzhen, Guangdong, China</li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li>', 1)
        f = f.replace("<li>WhatsApp · 张体进</li>", f'<li><a href="https://wa.me/{WA}" target="_blank" rel="noopener">WhatsApp · 张体进</a></li>', 1)
    if "privacy/index.html" not in f:
        pm = re.search(r'(<div><h3>(?:Pages|页面)</h3><ul><li><a href="([^"]*)index.html">.*?)</ul>', f, re.S)
        if pm:
            b = pm.group(2)  # path to this language's root, taken from the Home link
            extra = (f'<li><a href="{b}privacy/index.html">隐私</a></li><li><a href="{b}terms/index.html">条款</a></li>' if zh else
                     f'<li><a href="{b}privacy/index.html">Privacy</a></li><li><a href="{b}terms/index.html">Terms</a></li>')
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
                        "availableLanguage": ["en", "zh"]}}


def product_ld(r, s, title, desc):
    stem = pathlib.Path(r).stem
    if not stem.startswith("kxt-"): return None
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
    zh = is_zh(r)
    title = text_of(r"<title>(.*?)</title>", s)
    desc = text_of(r'<meta name="description" content="([^"]*)"', s)
    e, z = en_of(r), zh_of(r)
    lines = [f'<link rel="canonical" href="{url(r)}">']
    if r in NOINDEX:
        lines.append('<meta name="robots" content="noindex">')
    if (ROOT / e).exists() and (ROOT / z).exists():
        lines += [f'<link rel="alternate" hreflang="en" href="{url(e)}">',
                  f'<link rel="alternate" hreflang="zh" href="{url(z)}">',
                  f'<link rel="alternate" hreflang="x-default" href="{url(e)}">']
    stem = pathlib.Path(r).stem.upper()
    img = f"{SITE}/assets/drawings/{stem}.png" if (ROOT / "assets/drawings" / f"{stem}.png").exists() else f"{SITE}/assets/hero.jpg"
    is_prod = pathlib.Path(r).stem.startswith("kxt-")
    lines += [f'<meta property="og:type" content="{"product" if is_prod else "website"}">',
              '<meta property="og:site_name" content="Kangxuntong">',
              f'<meta property="og:title" content="{esc(title)}">',
              f'<meta property="og:description" content="{esc(desc)}">',
              f'<meta property="og:url" content="{url(r)}">',
              f'<meta property="og:image" content="{img}">',
              f'<meta property="og:locale" content="{"zh_CN" if zh else "en_US"}">',
              f'<meta property="og:locale:alternate" content="{"en_US" if zh else "zh_CN"}">',
              '<meta name="twitter:card" content="summary_large_image">']
    ld = []
    if e == "index.html":
        ld.append({"@context": "https://schema.org", "@graph": [ORG, {"@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/",
                   "name": "Kangxuntong Cavity Filters", "inLanguage": "zh" if zh else "en", "publisher": {"@id": SITE + "/#org"}}]})
    elif e.startswith("products/kxt-"):
        p = product_ld(r, s, title, desc)
        if p: ld.append(p)
    for d in ld:
        lines.append('<script type="application/ld+json">' + json.dumps(d, ensure_ascii=False).replace("</", "<\\/") + "</script>")
    return "<!-- seo:start -->\n" + "\n".join(lines) + "\n<!-- seo:end -->"


def fix_head(r, s):
    s = re.sub(r"\n?<!-- seo:start -->.*?<!-- seo:end -->", "", s, flags=re.S)
    return s.replace("</head>", seo_block(r, s) + "\n</head>", 1)


def fix_misc(r, s):
    # catalog thumbnails are CSS backgrounds: give them an accessible name
    s = re.sub(r'<div class="thumb" style="background-image:url\(([^)]*/)?([A-Z0-9-]+)\.png\)"></div>',
               lambda m: f'<div class="thumb" role="img" aria-label="{"外形图" if is_zh(r) else "Outline drawing of"} {m.group(2)}" style="background-image:url({m.group(1) or ""}{m.group(2)}.png)"></div>', s)
    # zh product titles: Chinese product name + model
    if is_zh(r) and pathlib.Path(r).stem.startswith("kxt-") and r.startswith("zh/products/"):
        model = pathlib.Path(r).stem.upper()
        h1 = text_of(r"<h1>(.*?)</h1>", s, model)
        s = re.sub(r"<title>.*?</title>", f"<title>{esc(h1)} {model} | 康讯通</title>", s, count=1)
    return s


# ---------------------------------------------------------------- generated pages
def page_from(template_rel, new_rel, title, desc, body):
    t = rd(ROOT / template_rel)
    head_end = t.index("</header>") + len("</header>")
    foot = t.index('<footer class="site-footer">')
    s = t[:head_end] + "\n" + body + "\n" + t[foot:]
    s = re.sub(r"<title>.*?</title>", f"<title>{esc(title)}</title>", s, count=1)
    s = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{esc(desc)}">', s, count=1)
    name = pathlib.Path(new_rel).name
    if is_zh(new_rel):
        lang = f'<span class="lang"><a href="../../{en_of(new_rel)}" class="">EN</a><a href="{name}" class="on">中文</a></span>'
    else:
        lang = f'<span class="lang"><a href="{name}" class="on">EN</a><a href="../zh/{new_rel}" class="">中文</a></span>'
    s = re.sub(r'<span class="lang">.*?</span></span>|<span class="lang">.*?</span>', lang, s, count=1, flags=re.S)
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
<tr><td>KXT26065</td><td>Duplexer</td><td>135–210 / 400–500 MHz</td><td>Passbands only (quotation roster, 29 May 2026). Electrical limits are on the unit’s test report.</td><td><a href="../datasheets/KXT-ROSTER-20260529.pdf">Roster PDF</a> · <a href="../contact/index.html?model=KXT26065">Quote</a></td></tr>
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
<tr><td>KXT26065</td><td>双工器</td><td>135–210 / 400–500 MHz</td><td>只有通带（2026 年 5 月 29 日报价货架）。电气指标见该件测试报告。</td><td><a href="../../datasheets/KXT-ROSTER-20260529.pdf">通带表 PDF</a> · <a href="../contact/index.html?model=KXT26065">询价</a></td></tr>
<tr><td><a href="kxt-ff-09.html">KXT-FF-09</a></td><td>UHF 腔体双工器</td><td>452.5–457.5 / 462.5–467.5 MHz</td><td>插损 ≤2.2 dB，驻波 ≤1.3，波动 ≤1.9 dB，对另一频段抑制 ≥80 dB，隔离 ≥80 dB，平均功率 50 W，N-F / SMA-F，177×134×73.5 mm。</td><td><a href="kxt-ff-09.html">规格</a> · <a href="../../datasheets/KXT-FF-09.pdf">PDF</a> · <a href="../contact/index.html?model=KXT-FF-09">询价</a></td></tr>
</tbody></table>
<p class="note">需要其他 VHF/UHF 收发频点、间隔、功率或接头？到<a href="../custom/index.html">定制</a>页发来频段方案，或写信到 <a href="mailto:sales@cavityfilter.com">sales@cavityfilter.com</a>。</p>
<p><a class="btn" href="../contact/index.html">提交询价</a> <a class="btn ghost" href="index.html">完整目录</a></p>
</div></section>"""
    page_from("zh/products/more.html", "zh/products/vhf-uhf-duplexers.html", "VHF/UHF 对讲机（专网 LMR）双工器 | 康讯通",
              "康讯通深圳工厂的 VHF/UHF 腔体双工器：KXT26065 135–210 / 400–500 MHz，KXT-FF-09 452.5–457.5 / 462.5–467.5 MHz。指标以工厂规格书为准，随货附测试报告。",
              zh_body)


def catalog_link():
    for r, label, txt in (("products/index.html", "VHF/UHF (LMR)", "VHF/UHF Duplexers for Two-way Radio / LMR"),
                          ("zh/products/index.html", "VHF/UHF（专网）", "VHF/UHF 对讲机（专网 LMR）双工器")):
        p = ROOT / r; s = rd(p)
        if "vhf-uhf-duplexers.html" not in s:
            s = s.replace('<div class="filters">', f'<p><a class="btn ghost" href="vhf-uhf-duplexers.html">{txt} →</a></p>\n<div class="filters">', 1)
        wr(p, s)


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
        e, z = en_of(r), zh_of(r)
        if (ROOT / e).exists() and (ROOT / z).exists():
            for hl, t in (("en", e), ("zh", z), ("x-default", e)):
                out.append(f'    <xhtml:link rel="alternate" hreflang="{hl}" href="{html.escape(url(t))}"/>')
        out.append("  </url>")
    out.append("</urlset>")
    wr(ROOT / "sitemap.xml", "\n".join(out) + "\n")
    wr(ROOT / "robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    old = ROOT / "sitemap.txt"
    if old.exists(): old.unlink()


def main():
    generated_pages()
    catalog_link()
    for r in ("contact/index.html", "zh/contact/index.html"): put_form(r, "contact")
    for r in ("custom/index.html", "zh/custom/index.html"): put_form(r, "custom")
    pages = sorted(rel(p) for p in ROOT.rglob("*.html"))
    for r in pages:
        p = ROOT / r
        s = rd(p)
        s = fix_misc(r, s)
        s = fix_footer(r, s)
        s = fix_head(r, s)
        wr(p, s)
    sitemap(pages)
    print(f"{len(pages)} pages processed")


if __name__ == "__main__":
    main()
