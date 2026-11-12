#!/usr/bin/env python3
"""Correct three factory typo/mismatch items on published datasheets.

1. KXT-FF-22: public title 9频 / 9-band → 8频 / 8-band (table has 8 ports;
   port 4 is dual-band). Factory filename is kept in the source note.
2. KXT-FF-26: footnote that the Word heading wrongly said 中频段8频合路器规格书;
   published title stays 低频段6频合路器规格书.
3. KXT-CM4-B1N78 / KXT-CM4-WIDE: fill omitted isolation values to match the
   rest of each sheet (≥80 dB / ≥70 dB) and drop the “原稿未写，询价确认” wording.

Run from the repo root with the venv that has PyMuPDF:
    KXT_CJK_FONT=/workspace/kxt-noto-sc.otf /tmp/kxt-venv/bin/python tools/apply_typo_corrections.py

Re-running on an already-patched PDF is safe: title and cell replacements
skip when the old string is gone; notes blocks are rewritten in full.
Do not modify files under 2026.11.7.
"""
import sys
from pathlib import Path

import pymupdf

sys.path.insert(0, str(Path(__file__).resolve().parent))
import apply_source_corrections as C

DS = C.DS
FONT = C.FONT
CELL_COLOR = C.CELL_COLOR

FF22_ZH_TITLE_OLD = "9频合路器技术规格书 -"
FF22_ZH_TITLE_NEW = "8频合路器技术规格书"
FF22_EN_SUB_OLD = "KXT-FF-22 · 9频合路器技术规格书 -"
FF22_EN_SUB_NEW = "KXT-FF-22 · 8-band Cavity Combiner, 1717.5–3600 MHz"

FF22_ZH_NOTES = [
    "· 来源文件：9频合路器技术规格书 -.doc",
    "· 工厂文件名为「9频合路器技术规格书」，表内只有 8 个端口（第 4 端口含两个通带 1887.5-1915 / 2010-2025），公开标题按 8 频合路器发布。",
    "· 特性阻抗：原稿写了 50 Ω 的，以原稿为准；原稿没写的，N 与 SMA 口按 50 Ω。",
    "· 室内型铝合金腔体。测试条件 25 °C、50 Ω、矢量网络分析仪。出货附该件测试报告。",
    "· 原稿没有互调指标。若订单选择低互调档，按 PIM3 ≤ −150 dBc @ 2×43 dBm 测试并写入报告。",
    "· 多端口表：插损、抑制、隔离只印该端口原稿里有的格子。标 † 的是合并单元格，字只出现在部分端口，已抄到空白端口，数字未改。",
    "· 相同内容还出现在：9频合路器技术规格书 -(1).doc",
]
FF22_EN_NOTES = [
    "· Source file: 9频合路器技术规格书 -.doc",
    "· The factory file was named 9频合路器技术规格书, but the table has 8 ports (port 4 carries two passbands 1887.5-1915 / 2010-2025), so the published title is 8-band.",
    "· Impedance: where the source states 50 Ω, that stands. Where it is silent, N and SMA ports are 50 Ω.",
    "· Indoor aluminum cavity. Tested at 25 °C in a 50 Ω system on a vector network analyzer. A test report ships with the unit.",
    "· The source sheet has no PIM limit. If the order selects the low-PIM option, test PIM3 to ≤ −150 dBc @ 2×43 dBm and put it on the report.",
    "· Multi-port sheet: insertion loss, rejection and isolation are printed only where that port’s source cell has text. A cell marked † repeats a merged source cell onto a blank port. The number is unchanged.",
    "· The same table also appears in: 9频合路器技术规格书 -(1).doc",
]

FF26_ZH_NOTES = [
    "· 来源文件：低频段6频合路器规格书20240614.doc",
    "· 工厂 Word 文内标题误写「中频段8频合路器规格书」，已按文件名和 6 端口表格更正为「低频段6频合路器规格书」。",
    "· 特性阻抗：原稿写了 50 Ω 的，以原稿为准；原稿没写的，N 与 SMA 口按 50 Ω。",
    "· 室内型铝合金腔体。测试条件 25 °C、50 Ω、矢量网络分析仪。出货附该件测试报告。",
    "· 原稿没有互调指标。若订单选择低互调档，按 PIM3 ≤ −150 dBc @ 2×43 dBm 测试并写入报告。",
    "· 多端口表：插损、抑制、隔离只印该端口原稿里有的格子。标 † 的是合并单元格，字只出现在部分端口，已抄到空白端口，数字未改。",
]
FF26_EN_NOTES = [
    "· Source file: 低频段6频合路器规格书20240614.doc",
    "· The factory Word heading said 中频段8频合路器规格书; it is corrected to 低频段6频合路器规格书 to match the filename and the 6-port table.",
    "· Impedance: where the source states 50 Ω, that stands. Where it is silent, N and SMA ports are 50 Ω.",
    "· Indoor aluminum cavity. Tested at 25 °C in a 50 Ω system on a vector network analyzer. A test report ships with the unit.",
    "· The source sheet has no PIM limit. If the order selects the low-PIM option, test PIM3 to ≤ −150 dBc @ 2×43 dBm and put it on the report.",
    "· Multi-port sheet: insertion loss, rejection and isolation are printed only where that port’s source cell has text. A cell marked † repeats a merged source cell onto a blank port. The number is unchanged.",
]

B1_ZH_NOTES = [
    "· 回波损耗由端口驻波比 ≤ 1.3 换算：RL = −20 log10((VSWR−1)/(VSWR+1)) ≈ 17.7 dB。",
    "· 低互调档是订货选项。原稿没有给出实测互调，未选该档时不作为本页保证值。需要时按 2×43 dBm 测试并附报告。",
    "· CH3、CH4 原稿把 1920–1980 MHz 写了两遍，漏了 2110–2170 MHz；隔离按同表其余端口补为 ≥80 dB。",
    "· 规格来源：四端口合路器规格7.15.docx",
]
B1_ZH_TRAIL = "订货写法：KXT-CM4-B1N78 + 接头公母 + 颜色（本色/黑色）+ 是否低互调档 + 数量。"
B1_EN_NOTES = [
    "· Return loss is calculated from VSWR ≤ 1.3: RL = −20 log10((VSWR−1)/(VSWR+1)) ≈ 17.7 dB.",
    "· Low PIM is an order option. The source sheet has no measured PIM, so it is not a guaranteed value unless that option is ordered and reported.",
    "· On CH3 and CH4 the source repeated 1920–1980 MHz and omitted 2110–2170 MHz; isolation is filled as ≥80 dB to match the rest of the sheet.",
    "· Source specification: 四端口合路器规格7.15.docx",
]
B1_EN_TRAIL = "Order as: KXT-CM4-B1N78 + connector gender + finish (natural/black) + low-PIM option + quantity."

WIDE_ZH_NOTES = [
    "· 回波损耗由端口驻波比 ≤ 1.3 换算：RL = −20 log10((VSWR−1)/(VSWR+1)) ≈ 17.7 dB。",
    "· 低互调档是订货选项。原稿没有给出实测互调，未选该档时不作为本页保证值。需要时按 2×43 dBm 测试并附报告。",
    "· CH2–CH4 原稿未写对 758–960 MHz 的隔离，按同表其余端口补为 ≥70 dB。CH4 原稿「1805-1920MH」少一个字母，按 1805–1920 MHz 读。",
    "· 规格来源：四端口合路器规格(1).docx",
]
WIDE_ZH_TRAIL = "订货写法：KXT-CM4-WIDE + 接头公母 + 颜色（本色/黑色）+ 是否低互调档 + 数量。"
WIDE_EN_NOTES = [
    "· Return loss is calculated from VSWR ≤ 1.3: RL = −20 log10((VSWR−1)/(VSWR+1)) ≈ 17.7 dB.",
    "· Low PIM is an order option. The source sheet has no measured PIM, so it is not a guaranteed value unless that option is ordered and reported.",
    "· CH2–CH4 source omitted isolation to 758–960 MHz; filled as ≥70 dB to match the rest of the sheet. A truncated «1805-1920MH» on CH4 is read as 1805–1920 MHz.",
    "· Source specification: 四端口合路器规格(1).docx",
]
WIDE_EN_TRAIL = "Order as: KXT-CM4-WIDE + connector gender + finish (natural/black) + low-PIM option + quantity."


def collect_text():
    bag = []
    for seq in (
        FF22_ZH_NOTES, FF22_EN_NOTES, FF26_ZH_NOTES, FF26_EN_NOTES,
        B1_ZH_NOTES, B1_EN_NOTES, WIDE_ZH_NOTES, WIDE_EN_NOTES,
    ):
        bag.extend(seq)
    bag += [
        B1_ZH_TRAIL, B1_EN_TRAIL, WIDE_ZH_TRAIL, WIDE_EN_TRAIL,
        FF22_ZH_TITLE_NEW, FF22_EN_SUB_NEW, "≥ 80 dB", "≥ 70 dB",
        "2110–2170 MHz", "758–960 MHz",
    ]
    return " ".join(bag)



def save(doc, path):
    tmp = str(path) + ".tmp"
    doc.save(tmp, garbage=4, deflate=True)
    doc.close()
    Path(tmp).replace(path)


def replace_exact(page, fontfile, old, new, fontname):
    hits = []
    for l, t in C.page_lines(page):
        if t.strip() == old:
            hits.append(l)
    if not hits:
        return 0
    for l in hits:
        page.add_redact_annot(l["bbox"], fill=(1, 1, 1))
    page.apply_redactions(images=0, graphics=0)
    for l in hits:
        s = l["spans"][0]
        color = CELL_COLOR
        if s.get("color") is not None:
            c = s["color"]
            color = (((c >> 16) & 255) / 255, ((c >> 8) & 255) / 255, (c & 255) / 255)
        page.insert_text(
            (l["bbox"][0], s["origin"][1]),
            new,
            fontname=fontname,
            fontfile=fontfile,
            fontsize=s["size"],
            color=color,
        )
    return len(hits)


def fill_isolation(page, fontfile, band_old, value_new, fontname):
    """Remove † from the band label and replace the same-row em-dash with value_new."""
    labels, dashes = [], []
    for l, t in C.page_lines(page):
        ts = t.strip()
        if ts == band_old:
            labels.append(l)
        elif ts == "—":
            dashes.append(l)
    if not labels:
        return 0
    paired = []
    for lab in labels:
        ly = (lab["bbox"][1] + lab["bbox"][3]) / 2
        cands = [d for d in dashes if abs((d["bbox"][1] + d["bbox"][3]) / 2 - ly) < 3 and d["bbox"][0] > lab["bbox"][2]]
        if not cands:
            raise SystemExit(f"no em-dash to the right of {band_old!r} at y={ly:.1f}")
        cands.sort(key=lambda d: d["bbox"][0])
        paired.append((lab, cands[0]))
    for lab, dash in paired:
        page.add_redact_annot(lab["bbox"], fill=(1, 1, 1))
        page.add_redact_annot(dash["bbox"], fill=(1, 1, 1))
    page.apply_redactions(images=0, graphics=0)
    band_new = band_old.replace(" †", "").replace("†", "").strip()
    for lab, dash in paired:
        ls, ds = lab["spans"][0], dash["spans"][0]
        page.insert_text((lab["bbox"][0], ls["origin"][1]), band_new,
                         fontname=fontname, fontfile=fontfile, fontsize=ls["size"], color=CELL_COLOR)
        page.insert_text((dash["bbox"][0], ds["origin"][1]), value_new,
                         fontname=fontname, fontfile=fontfile, fontsize=ds["size"], color=CELL_COLOR)
    return len(paired)


def write_notes(page, fontfile, notes, trailing=None, fontname="kxtnotes"):
    """Rewrite the 说明/Notes block. Uses a unique fontname so a prior
    isolation-cell subset of Noto is not reused (missing glyphs → tofu)."""
    origin_y, x, size = C.first_note_origin(page)
    y_top = origin_y - size - 1
    C.redact_below(page, y_top)
    font = pymupdf.Font(fontfile=fontfile)
    width = 500
    lh = 11.0
    y = origin_y
    for para in notes:
        for line in C.wrap(font, para, size, width):
            if y > 800:
                raise SystemExit(f"notes overflow at y={y}: {line!r}")
            page.insert_text((x, y), line, fontname=fontname, fontfile=fontfile,
                             fontsize=size, color=C.NOTE_COLOR)
            y += lh
    if trailing:
        y += 4
        for line in C.wrap(font, trailing, size, width):
            page.insert_text((x, y), line, fontname=fontname, fontfile=fontfile,
                             fontsize=size, color=C.NOTE_COLOR)
            y += lh
    return 1


def patch_ff22(fontfile):
    path = DS / "KXT-FF-22.pdf"
    doc = pymupdf.open(path)
    n = 0
    n += replace_exact(doc[0], fontfile, FF22_ZH_TITLE_OLD, FF22_ZH_TITLE_NEW, "kxttitle")
    n += replace_exact(doc[3], fontfile, FF22_EN_SUB_OLD, FF22_EN_SUB_NEW, "kxttitle")
    n += write_notes(doc[2], fontfile, FF22_ZH_NOTES)
    n += write_notes(doc[5], fontfile, FF22_EN_NOTES)
    meta = dict(doc.metadata or {})
    meta["title"] = "KXT-FF-22"
    meta["subject"] = "8-band cavity combiner 1717.5–3600 MHz"
    doc.set_metadata(meta)
    save(doc, path)
    print(f"KXT-FF-22.pdf: {n} edits")


def patch_ff26(fontfile):
    path = DS / "KXT-FF-26.pdf"
    doc = pymupdf.open(path)
    n = 0
    n += write_notes(doc[1], fontfile, FF26_ZH_NOTES)
    n += write_notes(doc[3], fontfile, FF26_EN_NOTES)
    save(doc, path)
    print(f"KXT-FF-26.pdf: {n} edits")


def patch_cm4(name, fontfile, band_old, value_new, zh_notes, zh_trail, en_notes, en_trail, zh_page=1, en_page=3):
    path = DS / name
    doc = pymupdf.open(path)
    n = 0
    for page in doc:
        n += fill_isolation(page, fontfile, band_old, value_new, "kxtiso")
    n += write_notes(doc[zh_page], fontfile, zh_notes, zh_trail, fontname="kxtnotes")
    n += write_notes(doc[en_page], fontfile, en_notes, en_trail, fontname="kxtnotes")
    save(doc, path)
    print(f"{name}: {n} edits")


def main():
    fontfile = C.subset_font(collect_text())
    patch_ff22(fontfile)
    patch_ff26(fontfile)
    patch_cm4(
        "KXT-CM4-B1N78.pdf", fontfile,
        "2110–2170 MHz †", "≥ 80 dB",
        B1_ZH_NOTES, B1_ZH_TRAIL, B1_EN_NOTES, B1_EN_TRAIL,
    )
    patch_cm4(
        "KXT-CM4-WIDE.pdf", fontfile,
        "758–960 MHz †", "≥ 70 dB",
        WIDE_ZH_NOTES, WIDE_ZH_TRAIL, WIDE_EN_NOTES, WIDE_EN_TRAIL,
    )
    print("done")


if __name__ == "__main__":
    main()
