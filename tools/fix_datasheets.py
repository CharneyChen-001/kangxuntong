#!/usr/bin/env python3
"""One-off fixes to the Rev A datasheet PDFs after the 2026-11-11 code review.

Values are reverted to what the factory source sheet says; inferred numbers
are removed. Requires PyMuPDF (pip install pymupdf). Run from repo root:
    python tools/fix_datasheets.py
Idempotent only in the sense that a second run finds nothing to replace.
"""
import pathlib, sys
import pymupdf

DS = pathlib.Path(__file__).resolve().parent.parent / "website" / "datasheets"
FONT = "notosc"
FONTFILE = __import__("os").environ.get("KXT_CJK_FONT", "/workspace/kxt-noto-sc.otf")  # Noto Sans CJK SC (OTF extracted from the TTC)


def _subset_font():
    """Subset Noto Sans CJK SC to the characters this script inserts (keeps PDFs small)."""
    import re, tempfile
    from fontTools import subset
    src = open(__file__, encoding="utf-8").read()
    chars = set("".join(re.findall(r'"([^"\n]*)"', src))) | set("0123456789.*—·")
    out = tempfile.NamedTemporaryFile(suffix=".otf", delete=False).name
    opts = subset.Options(); opts.name_IDs = ["*"]; opts.notdef_outline = True; opts.layout_features = ["*"]
    f = subset.load_font(FONTFILE, opts)
    sub = subset.Subsetter(opts); sub.populate(text="".join(chars)); sub.subset(f)
    subset.save_font(f, out, opts)
    return out


FONTFILE = _subset_font() if __name__ == "__main__" else FONTFILE


def lines(page):
    for b in page.get_text("dict")["blocks"]:
        for l in b.get("lines", []):
            yield b, l, "".join(s["text"] for s in l["spans"])


def rgb(c):
    return ((c >> 16) & 255) / 255, ((c >> 8) & 255) / 255, (c & 255) / 255


def put(page, rect, text, size, color, width=None):
    r = pymupdf.Rect(rect)
    if width:
        r.x1 = r.x0 + width
    r.y1 = r.y0 + size * 1.5 * 4
    page.insert_textbox(r, text, fontname=FONT, fontfile=FONTFILE, fontsize=size, color=rgb(color))


def cell_right_of(page, label_line, old):
    """Find span `old` on the same row (same y) right of label_line."""
    y = (label_line["bbox"][1] + label_line["bbox"][3]) / 2
    for _, l, t in lines(page):
        ly = (l["bbox"][1] + l["bbox"][3]) / 2
        if abs(ly - y) < 2 and l["bbox"][0] > label_line["bbox"][2] and t.strip() == old:
            return l
    return None


def replace_cells(page, row_key, old, new, nth=None):
    """Replace value `old` in every row whose label contains row_key."""
    hits, edits = 0, []
    for _, l, t in list(lines(page)):
        if row_key in t:
            hits += 1
            if nth is not None and hits != nth:
                continue
            c = cell_right_of(page, l, old)
            if c:
                edits.append(c)
    for c in edits:
        page.add_redact_annot(c["bbox"], fill=False)
    page.apply_redactions(images=0, graphics=0)
    for c in edits:
        s = c["spans"][0]
        page.insert_text((c["bbox"][0], s["origin"][1]), new, fontname=FONT, fontfile=FONTFILE, fontsize=s["size"], color=rgb(s["color"]))
    return len(edits)


def replace_note(page, start, new):
    """Replace a note paragraph that starts with `start` (may wrap)."""
    target = None
    for b, l, t in lines(page):
        if t.startswith(start):
            target = (b, l)
            break
    if not target:
        return 0
    b, l = target
    ls = b["lines"]
    i = ls.index(l)
    group = [ls[i]]
    for nxt in ls[i + 1:]:
        txt = "".join(s["text"] for s in nxt["spans"])
        if txt.startswith("·"):
            break
        group.append(nxt)
    rect = pymupdf.Rect(group[0]["bbox"])
    for g in group[1:]:
        rect |= pymupdf.Rect(g["bbox"])
    for g in group:
        page.add_redact_annot(g["bbox"], fill=False)
    page.apply_redactions(images=0, graphics=0)
    s = group[0]["spans"][0]
    n = len(group)
    lh = (group[1]["bbox"][1] - group[0]["bbox"][1]) if n > 1 else s["size"] * 1.33
    width = 555 - rect.x0
    font = pymupdf.Font(fontfile=FONTFILE)
    size = s["size"]
    # keep the note inside the lines it used to occupy: shrink rather than overflow
    while font.text_length(new, size) > width * n * 0.93 and size > 5:
        size -= 0.25
    # manual wrap into at most n lines at the original baselines
    out, cur = [], ""
    for ch in new:
        if font.text_length(cur + ch, size) > width:
            out.append(cur); cur = ch
        else:
            cur += ch
    out.append(cur)
    if len(out) > n:
        print("  warning: note wraps to", len(out), "lines (had", n, "):", start, file=sys.stderr)
    base = s["origin"][1]
    for i, txt in enumerate(out):
        page.insert_text((rect.x0, base + i * lh), txt, fontname=FONT, fontfile=FONTFILE,
                         fontsize=size, color=rgb(s["color"]))
    return 1


def nth_line(doc, key):
    out = []
    for pi, p in enumerate(doc):
        for _, l, t in lines(p):
            if t.strip().startswith(key):
                out.append((pi, l))
    return out


def fix(name, fn):
    path = DS / name
    doc = pymupdf.open(path)
    n = fn(doc)
    doc.save(str(path) + ".tmp", garbage=3, deflate=True)
    doc.close()
    pathlib.Path(str(path) + ".tmp").replace(path)
    print(f"{name}: {n} edits")


def cm4_wide(d):
    n = 0
    for p in d:
        n += replace_cells(p, "758–960 MHz †", "≥ 70 dB", "—")
    n += replace_note(d[1], "· 带 † 的 758–960", "· 带 † 的 758–960 MHz 隔离：原稿该端口未写，本表不补数，标“—”，请询价确认。CH4 原稿「1805-1920MH」少一个字母，按 1805–1920 MHz 读。")
    n += replace_note(d[3], "· Rows marked †", "· Rows marked †: the source sheet gives no isolation value on that port, so none is printed (—). Contact us for the factory figure. A truncated «1805-1920MH» on CH4 is read as 1805–1920 MHz.")
    return n


def cm4_b1n78(d):
    n = 0
    for p in d:
        n += replace_cells(p, "2110–2170 MHz †", "≥ 80 dB", "—")
    n += replace_note(d[1], "· CH3、CH4 原稿", "· CH3、CH4 原稿把 1920–1980 MHz 写了两遍，漏了 2110–2170 MHz。带 † 的一行原稿没有隔离数值，本表不补数，标“—”，请询价确认。")
    n += replace_note(d[3], "· On CH3 and CH4", "· On CH3 and CH4 the source repeated 1920–1980 MHz and omitted 2110–2170 MHz. Rows marked † have no isolation value on the source sheet, so none is printed (—). Contact us for the factory figure.")
    return n


def ff11(d):
    n = 0
    zh = [x for x in nth_line(d, "插入损耗(dB)") if "Insertion" not in "".join(s["text"] for s in x[1]["spans"])]
    en = nth_line(d, "插入损耗(dB) / Insertion loss")
    for pi, l in (zh[4], en[4]):
        c = cell_right_of(d[pi], l, "1.7dB")
        if c:
            d[pi].add_redact_annot(c["bbox"], fill=False); d[pi].apply_redactions(images=0, graphics=0)
            s = c["spans"][0]
            d[pi].insert_text((c["bbox"][0], s["origin"][1]), "11.0dB *", fontname=FONT, fontfile=FONTFILE, fontsize=s["size"], color=rgb(s["color"]))
            n += 1
    n += replace_note(d[1], "· 3300–3800 MHz 端口插入损耗", "· * 3300–3800 MHz 端口插入损耗按原稿印 11.0 dB。同表其余端口为 1.7 dB，此格可能是笔误，以工厂书面确认为准，请询价确认。")
    n += replace_note(d[3], "· Insertion loss on the 3300", "· * Insertion loss on the 3300–3800 MHz port is printed as written on the source sheet: 11.0 dB. The other ports are 1.7 dB; this cell may be a typo and is pending factory confirmation.")
    return n


def ff0708(d):
    n = 0
    for p in d:
        n += replace_cells(p, "驻波比", "≤1.3", "≤1.3 *")
    n += replace_note(d[1], "· 有一栏驻波原稿写作", "· * 原稿有一栏驻波写作 ≤0.9（驻波比不能小于 1，属原稿笔误），誊清无法确定是哪一个端口。标 * 的驻波值以工厂书面确认为准。")
    n += replace_note(d[3], "· One VSWR cell", "· * One VSWR cell on the source sheet was written ≤0.9, which is not physically possible; the port cannot be identified. VSWR values marked * are pending factory confirmation.")
    return n


def ff01(d):
    n = 0
    for p in d:
        for _, l, t in list(lines(p)):
            if t.strip() == "≤−145 dBc @ 2×43 dBm":
                p.add_redact_annot(l["bbox"], fill=False); p.apply_redactions(images=0, graphics=0)
                s = l["spans"][0]
                p.insert_text((l["bbox"][0], s["origin"][1]), "≤−145 dBc @ 43dBC *", fontname=FONT, fontfile=FONTFILE, fontsize=s["size"], color=rgb(s["color"]))
                n += 1
    n += replace_note(d[1], "· 互调原稿写作", "· * 互调按原稿印 ≤−145 dBc @ 43dBC，测试功率单位以工厂书面确认为准。")
    n += replace_note(d[3], "· PIM was written", "· * PIM is printed as written on the source sheet: ≤−145 dBc @ 43dBC. The test-power unit is pending factory confirmation.")
    return n


def catalog(d):
    p = d[0]
    for _, l, t in list(lines(p)):
        if "深耕三十年" in t:
            p.add_redact_annot(l["bbox"], fill=False); p.apply_redactions(images=0, graphics=0)
            s = l["spans"][0]
            p.insert_text((l["bbox"][0], s["origin"][1]), t.replace(" · 深耕三十年", ""), fontname=FONT, fontfile=FONTFILE, fontsize=s["size"], color=rgb(s["color"]))
            return 1
    return 0


if __name__ == "__main__":
    fix("KXT-CM4-WIDE.pdf", cm4_wide)
    fix("KXT-CM4-B1N78.pdf", cm4_b1n78)
    fix("KXT-FF-11.pdf", ff11)
    fix("KXT-FF-07.pdf", ff0708)
    fix("KXT-FF-08.pdf", ff0708)
    fix("KXT-FF-01.pdf", ff01)
    fix("KXT-CATALOG-INDEX.pdf", catalog)
