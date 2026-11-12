#!/usr/bin/env python3
"""Patch Rev A datasheet PDFs after the 2026.11.7 originals audit.

Run from repo root:
    /tmp/kxt-venv/bin/python tools/patch_datasheets_audit.py

Re-running: cell replacements are exact-string; already-patched cells are skipped.
Notes blocks are rewritten in full.
"""
import sys
from pathlib import Path

import pymupdf

# allow importing sibling tool
sys.path.insert(0, str(Path(__file__).resolve().parent))
import apply_source_corrections as C

DS = C.DS
FONT = C.FONT
FONTFILE = C.FONTFILE
CELL_COLOR = C.CELL_COLOR
NOTE_COLOR = C.NOTE_COLOR


def save(doc, path):
    tmp = str(path) + ".tmp"
    doc.save(tmp, garbage=4, deflate=True)
    doc.close()
    Path(tmp).replace(path)


def lines(page):
    return C.page_lines(page)


def replace_exact(page, fontfile, old, new, pred=None):
    """Replace line text equal to `old` (stripped), optional pred(line_dict, text)."""
    hits = []
    for l, t in lines(page):
        if t.strip() == old and (pred is None or pred(l, t)):
            hits.append(l)
    if not hits:
        return 0
    for l in hits:
        page.add_redact_annot(l["bbox"], fill=False)
    page.apply_redactions(images=0, graphics=0)
    font = pymupdf.Font(fontfile=fontfile)
    n = 0
    for l in hits:
        s = l["spans"][0]
        size = s["size"]
        while font.text_length(new, size) > (l["bbox"][2] - l["bbox"][0]) + 40 and size > 6:
            size -= 0.25
        page.insert_text((l["bbox"][0], s["origin"][1]), new, fontname=FONT,
                         fontfile=fontfile, fontsize=size, color=CELL_COLOR)
        n += 1
    return n


def replace_span(page, fontfile, needle, new, pred=None):
    """Redact the search_for(needle) rects and write `new` at the same origin."""
    rects = page.search_for(needle)
    if pred:
        rects = [r for r in rects if pred(r)]
    if not rects:
        return 0
    # find matching span origin
    hits = []
    for r in rects:
        for l, t in lines(page):
            if needle in t:
                # pick span
                for sp in l["spans"]:
                    if needle in sp["text"] or pymupdf.Rect(sp["bbox"]).intersects(r):
                        hits.append((r, sp, l))
                        break
    if not hits:
        # just use search rects
        for r in rects:
            page.add_redact_annot(r, fill=(1, 1, 1))
        page.apply_redactions(images=0, graphics=0)
        font = pymupdf.Font(fontfile=fontfile)
        for r in rects:
            page.insert_text((r.x0, r.y1 - 1), new, fontname=FONT, fontfile=fontfile,
                             fontsize=8.5, color=CELL_COLOR)
        return len(rects)
    # unique by rect
    seen = set()
    uniq = []
    for r, sp, l in hits:
        key = (round(r.x0,1), round(r.y0,1))
        if key in seen:
            continue
        seen.add(key)
        uniq.append((r, sp, l))
    for r, sp, l in uniq:
        # expand rect a bit to cover remaining "-2690" if needle was only 22620
        page.add_redact_annot(r, fill=(1, 1, 1))
    page.apply_redactions(images=0, graphics=0)
    font = pymupdf.Font(fontfile=fontfile)
    for r, sp, l in uniq:
        size = sp["size"]
        page.insert_text((r.x0, sp["origin"][1]), new, fontname=FONT, fontfile=fontfile,
                         fontsize=size, color=CELL_COLOR)
    return len(uniq)


def patch_ff0708(name, fontfile):
    path = DS / name
    doc = pymupdf.open(path)
    n = 0
    # ZH page 0, EN page 2: three "≤1.3 *" ; last one (highest y) is port 3
    for pi in (0, 2):
        page = doc[pi]
        cells = []
        for l, t in lines(page):
            if t.strip() == "≤1.3 *":
                cells.append(l)
        cells.sort(key=lambda l: l["bbox"][1])
        if len(cells) != 3:
            print(f"  WARN {name} p{pi+1}: found {len(cells)} starred VSWR cells")
        # redact all
        for l in cells:
            page.add_redact_annot(l["bbox"], fill=False)
        page.apply_redactions(images=0, graphics=0)
        for i, l in enumerate(cells):
            new = "≤0.9 *" if i == len(cells) - 1 else "≤1.3"
            s = l["spans"][0]
            page.insert_text((l["bbox"][0], s["origin"][1]), new, fontname=FONT,
                             fontfile=fontfile, fontsize=s["size"], color=CELL_COLOR)
            n += 1
    zh = list(C.FF0708_ZH_NOTES)
    en = list(C.FF0708_EN_NOTES)
    # keep existing source-file first line
    zh_src, en_src = None, None
    for _, t in lines(doc[1]):
        if t.strip().startswith("· 来源文件："):
            zh[0] = t.strip()
            break
    for _, t in lines(doc[3]):
        if t.strip().startswith("· Source file:"):
            en[0] = t.strip()
            break
    n += C.write_notes(doc[1], fontfile, zh)
    n += C.write_notes(doc[3], fontfile, en)
    save(doc, path)
    print(f"{name}: {n} edits")


def patch_bf(fontfile):
    path = DS / "KXT-BF-18021883.pdf"
    doc = pymupdf.open(path)
    n = 0
    for p in doc:
        n += replace_exact(p, fontfile, "1802–1883 MHz *", "1802–1833 MHz *")
        n += replace_exact(p, fontfile, "81 MHz", "31 MHz")
    n += C.write_notes(doc[0], fontfile, C.BF_ZH_NOTES, C.BF_ZH_TRAIL)
    n += C.write_notes(doc[1], fontfile, C.BF_EN_NOTES, C.BF_EN_TRAIL)
    save(doc, path)
    print(f"KXT-BF-18021883.pdf: {n} edits")


def patch_22620(name, fontfile, zh_note, en_note):
    path = DS / name
    doc = pymupdf.open(path)
    n = 0
    for i, p in enumerate(doc):
        # redact "22620-2690" (search 22620 and widen)
        rects = p.search_for("22620")
        if not rects:
            continue
        expanded = []
        for r in rects:
            # cover through -2690
            rr = pymupdf.Rect(r.x0 - 1, r.y0 - 0.5, r.x1 + 28, r.y1 + 0.5)
            expanded.append(rr)
            p.add_redact_annot(rr, fill=(1, 1, 1))
        p.apply_redactions(images=0, graphics=0)
        for r in expanded:
            # baseline approx
            p.insert_text((r.x0, r.y1 - 1.2), "2620-2690 *", fontname=FONT,
                          fontfile=fontfile, fontsize=8.5, color=CELL_COLOR)
            n += 1
    # append a short note on last ZH notes page (p3? typically notes on p3 of first language?)
    # FF-18/28 are 6 pages: zh tables p1-2, maybe notes; en tables p4-5.
    # Add note at bottom of page 2 (ZH after tables) and page 5 or 6 if notes exist.
    # Safer: add as a line under existing notes if a 说明/Notes page exists, else footer of table pages 1 and 4.
    for i, p in enumerate(doc):
        texts = "\n".join(t for _, t in lines(p))
        if "按工厂 Word 原稿誊清" in texts or "Transcribed from the factory Word file" in texts:
            note = zh_note if "按工厂" in texts or "来源文件" in texts else en_note
            # insert near bottom if space
            # find last · line
            last_y = 0
            x = 40
            size = 8
            for l, t in lines(p):
                if t.strip().startswith("·"):
                    last_y = l["bbox"][3]
                    x = l["bbox"][0]
                    size = l["spans"][0]["size"]
            if last_y and last_y < 790:
                font = pymupdf.Font(fontfile=fontfile)
                y = last_y + 11
                for line in C.wrap(font, "· " + note, size, 500):
                    p.insert_text((x, y), line, fontname=FONT, fontfile=fontfile,
                                  fontsize=size, color=NOTE_COLOR)
                    y += 11
                n += 1
    save(doc, path)
    print(f"{name}: {n} edits")


def patch_ff06(fontfile):
    path = DS / "KXT-FF-06.pdf"
    doc = pymupdf.open(path)
    n = 0
    for p in doc:
        # trailing "≥" at end of port 2 rejection
        for l, t in lines(p):
            if t.strip().endswith("≥90@3400-3600 ≥") or t.strip().endswith("≥90@3400-3600 ≥"):
                # redact only the last ≥
                rects = p.search_for("≥")
                # the rightmost ≥ on this line
                line_y = (l["bbox"][1] + l["bbox"][3]) / 2
                cands = [r for r in rects if abs((r.y0+r.y1)/2 - line_y) < 3 and r.x0 > 300]
                if not cands:
                    continue
                r = max(cands, key=lambda x: x.x0)
                p.add_redact_annot(r, fill=(1, 1, 1))
                p.apply_redactions(images=0, graphics=0)
                n += 1
                break
        # also try search for the exact end token on the line
    # notes
    zh = "原稿第 2 端口抑制末尾有一个未写完的「≥」，未当作指标。第 2 端口驻波是合并单元格，网页已按第 1 端口抄为 ≤1.3，标 †。"
    en = "A dangling “≥” at the end of the port 2 rejection list is not treated as a limit. Port 2 VSWR is a merged cell; the web page copies ≤1.3 from port 1, marked †."
    for i, p in enumerate(doc):
        texts = "\n".join(t for _, t in lines(p))
        if "按工厂 Word 原稿誊清" in texts or "Transcribed from the factory Word file" in texts:
            note = zh if "按工厂" in texts or "来源文件" in texts else en
            last_y, x, size = 0, 40, 8
            for l, t in lines(p):
                if t.strip().startswith("·"):
                    last_y = l["bbox"][3]
                    x = l["bbox"][0]
                    size = l["spans"][0]["size"]
            if last_y and last_y < 790:
                font = pymupdf.Font(fontfile=fontfile)
                y = last_y + 11
                for line in C.wrap(font, "· " + note, size, 500):
                    p.insert_text((x, y), line, fontname=FONT, fontfile=fontfile,
                                  fontsize=size, color=NOTE_COLOR)
                    y += 11
                n += 1
    save(doc, path)
    print(f"KXT-FF-06.pdf: {n} edits")


def patch_dash_freq(name, fontfile):
    path = DS / name
    doc = pymupdf.open(path)
    n = 0
    for p in doc:
        # find header value (right of first row) and freq-row em dash in value column (x~229)
        freq_header = None
        dash_lines = []
        for l, t in lines(p):
            ts = t.strip()
            # value-column dash only
            if ts == "—" and l["bbox"][0] > 200:
                dash_lines.append(l)
            # header passband like 1452-1492 or 758-803MHZ sitting in value col near top
        # The first value-col dash is often the left? we filtered x>200
        # There may be 1 per language page. The header frequency is in the value col one row above.
        for l in dash_lines:
            # find text in value column (~x 229) with y slightly less
            header = None
            for l2, t2 in lines(p):
                if l2["bbox"][0] > 200 and l2["bbox"][3] <= l["bbox"][1] + 0.5:
                    # closest above
                    if header is None or l2["bbox"][1] > header[0]["bbox"][1]:
                        if t2.strip() and t2.strip() != "—":
                            header = (l2, t2.strip())
            if not header:
                continue
            new = header[1]
            p.add_redact_annot(l["bbox"], fill=False)
            p.apply_redactions(images=0, graphics=0)
            s = l["spans"][0]
            p.insert_text((l["bbox"][0], s["origin"][1]), new, fontname=FONT,
                          fontfile=fontfile, fontsize=s["size"], color=CELL_COLOR)
            n += 1
    # short note
    zh = "原稿「频率范围」格是空的，通带只写在表头，本页抄到频率范围这一行。"
    en = "The source frequency cell is blank; the passband is only in the table header. This page copies it into the frequency row."
    for p in doc:
        texts = "\n".join(t for _, t in lines(p))
        if "按工厂 Word 原稿誊清" in texts or "Transcribed from the factory Word file" in texts:
            note = zh if "按工厂" in texts or "来源文件" in texts else en
            last_y, x, size = 0, 40, 8
            for l, t in lines(p):
                if t.strip().startswith("·"):
                    last_y = l["bbox"][3]
                    x = l["bbox"][0]
                    size = l["spans"][0]["size"]
            if last_y and last_y < 790:
                font = pymupdf.Font(fontfile=fontfile)
                y = last_y + 11
                for line in C.wrap(font, "· " + note, size, 500):
                    p.insert_text((x, y), line, fontname=FONT, fontfile=fontfile,
                                  fontsize=size, color=NOTE_COLOR)
                    y += 11
                n += 1
    save(doc, path)
    print(f"{name}: {n} edits")


def patch_catalog(fontfile):
    path = DS / "KXT-CATALOG-INDEX.pdf"
    doc = pymupdf.open(path)
    p = doc[0]
    n = 0
    # only the passband cell, not the model number (model is at x~41-114)
    hits = []
    for l, t in lines(p):
        if t.strip() == "1802–1883" and l["bbox"][0] > 150:
            hits.append(l)
    for l in hits:
        p.add_redact_annot(l["bbox"], fill=False)
    if hits:
        p.apply_redactions(images=0, graphics=0)
        for l in hits:
            s = l["spans"][0]
            p.insert_text((l["bbox"][0], s["origin"][1]), "1802–1833", fontname=FONT,
                          fontfile=fontfile, fontsize=s["size"], color=CELL_COLOR)
            n += 1
    save(doc, path)
    print(f"KXT-CATALOG-INDEX.pdf: {n} edits")


def main():
    # large charset for all new notes
    bag = C.collect_text()
    extra = (
        "2620-2690 * 22620 第2端口抑制笔误 dangling frequency header 频率范围格是空的通带只写在表头抄到这一行 "
        "A dangling at the end of the port 2 rejection list is not treated as a limit. "
        "The source frequency cell is blank; the passband is only in the table header. "
        "This page copies it into the frequency row. 未写完的合并单元格网页已按 "
        "Port 3 VSWR is written on the source sheet the cell is wide Word display matches XML overflow typo "
        "catalog model number is unchanged 型号编号不变 格子够宽不是溢出"
    )
    fontfile = C.subset_font(bag + " " + extra)
    patch_ff0708("KXT-FF-07.pdf", fontfile)
    patch_ff0708("KXT-FF-08.pdf", fontfile)
    patch_bf(fontfile)
    patch_22620(
        "KXT-FF-18.pdf", fontfile,
        "原稿第 2 端口抑制有一处写作 90@22620-2690，同表其余端口均为 2620-2690，按笔误改为 2620-2690，标 *。",
        "Port 2 rejection was written 90@22620-2690 on the source sheet; every other port uses 2620-2690. Printed as 2620-2690, marked *.",
    )
    patch_22620(
        "KXT-FF-28.pdf", fontfile,
        "原稿第 2 端口抑制有一处写作 90@22620-2690，同表其余端口均为 2620-2690，按笔误改为 2620-2690，标 *。",
        "Port 2 rejection was written 90@22620-2690 on the source sheet; every other port uses 2620-2690. Printed as 2620-2690, marked *.",
    )
    patch_ff06(fontfile)
    for name in [
        "KXT-FF-03.pdf","KXT-FF-05.pdf","KXT-FF-13.pdf","KXT-FF-14.pdf",
        "KXT-FF-17.pdf","KXT-FF-20.pdf","KXT-FF-46.pdf","KXT-FF-47.pdf",
    ]:
        patch_dash_freq(name, fontfile)
    patch_catalog(fontfile)
    print("done")


if __name__ == "__main__":
    main()
