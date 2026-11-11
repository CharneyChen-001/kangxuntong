# Kangxuntong / cavityfilter.com

Static bilingual (EN / 中文) catalog site. The web root is `website/` (served at https://cavityfilter.com/).

## Editing
- Pages are plain HTML in `website/` (Chinese mirror in `website/zh/`). Specification numbers must match the factory source sheet; do not fill in missing values.
- After editing any page run `python3 tools/build_site.py`. It rewrites, idempotently, the SEO head block (canonical, hreflang, Open Graph, JSON-LD), the footer links, the RFQ form on the contact and custom pages, the generated pages (`contact/thanks.html`, `products/vhf-uhf-duplexers.html`), `sitemap.xml` and `robots.txt`.
- `tools/fix_datasheets.py` and `tools/rebuild_ff23_pdf.py` record the one-off PDF corrections made after the 2026-11-11 review (need PyMuPDF, fontTools and a Noto Sans CJK SC font).

## Enquiry form
The RFQ form posts to FormSubmit (`https://formsubmit.co/sales@cavityfilter.com`, AJAX endpoint with a normal POST fallback), with a `_honey` honeypot and a thank-you page. FormSubmit sends a one-time activation email to sales@cavityfilter.com on first use; it must be confirmed before enquiries are delivered. WhatsApp and `mailto:` are offered as alternatives.

## Deploy
Copy the contents of `website/` to the web root. Do not deploy `tools/` or `.git`.
