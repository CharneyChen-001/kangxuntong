# Kangxuntong / cavityfilter.com

Static multilingual catalog site (English, 中文, русский, español, português, العربية). The web root is `website/` (served at https://cavityfilter.com/). English is at the site root; the other locales use path prefixes `/zh/`, `/ru/`, `/es/`, `/pt/` and `/ar/`.

## Editing
- Pages are plain HTML in `website/` (locale mirrors in `website/zh/`, `website/ru/`, `website/es/`, `website/pt/` and `website/ar/`). Specification numbers must match the factory source sheet; do not fill in missing values. Do not invent legal names in languages other than Chinese and English.
- After editing English (or Chinese) copy, run `python3 tools/generate_locales.py` and then `python3 tools/build_site.py`. The first rebuilds the Russian, Spanish, Portuguese and Arabic trees from English. The second rewrites, idempotently, the SEO head block (canonical, hreflang for all six locales plus x-default, Open Graph, JSON-LD), the six-language switcher, the footer links, the RFQ form on the contact and custom pages in every locale, the generated pages (`contact/thanks.html`, `products/vhf-uhf-duplexers.html`, the 12 shelf-model pages `products/kxt260xx.html` from the 29 May 2026 roster, `applications/private-networks.html`, `applications/das-erces.html`, and `404.html` with root-absolute links), `sitemap.xml` and `robots.txt`. Running `build_site.py` alone does not wipe typo-corrected English or Chinese product bodies.
- Self-hosted SIL OFL fonts live in `website/assets/fonts/` (Noto Sans for Latin and Cyrillic, Noto Sans Arabic). Do not depend on a font CDN at runtime.
- `tools/fix_datasheets.py`, `tools/rebuild_ff23_pdf.py` and `tools/fix_ff11_temp_row.py` record the one-off PDF corrections made after the 2026-11-11 review (need PyMuPDF, fontTools and a Noto Sans CJK SC font).

## Enquiry form
The RFQ form posts to FormSubmit (`https://formsubmit.co/sales@cavityfilter.com`, AJAX endpoint with a normal POST fallback), with a `_honey` honeypot and a thank-you page. FormSubmit sends a one-time activation email to sales@cavityfilter.com on first use; it must be confirmed before enquiries are delivered. WhatsApp and `mailto:` are offered as alternatives.

## Deploy
Copy the contents of `website/` to the web root. Do not deploy `tools/` or `.git`.
nginx: `error_page 404 /404.html;` in the cavityfilter.com server block; requests to the bare server IP are 301-redirected to https://cavityfilter.com.

## Custom-design form
The custom page form is `multipart/form-data` with an optional `attachment` file (PDF/DWG/DXF/STEP/JPG/PNG, FormSubmit limit 10 MB total) and a required quantity. With a file attached the form is sent by a normal POST (FormSubmit's AJAX endpoint does not take files) and FormSubmit redirects to the `_next` thank-you page.
