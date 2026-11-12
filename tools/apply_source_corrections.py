#!/usr/bin/env python3
"""Patch datasheet PDFs to follow the factory source more faithfully.

Run from the repo root:
    python tools/apply_source_corrections.py

Re-running is safe only on the *unpatched* review PDFs (the files as they
stood after tools/fix_datasheets.py). If a run is interrupted, restore from
git or a backup and start again.

Do not re-run tools/fix_datasheets.py afterwards: that script still
restores the raw “43dBC” typo on KXT-FF-01.

Requires PyMuPDF + fontTools and Noto Sans CJK SC at KXT_CJK_FONT.
"""
import os, pathlib, tempfile
import pymupdf
from fontTools import subset

ROOT = pathlib.Path(__file__).resolve().parent.parent
DS = ROOT / "website" / "datasheets"
FONTFILE = os.environ.get("KXT_CJK_FONT", "/workspace/kxt-noto-sc.otf")
NOTE_COLOR = (94 / 255, 88 / 255, 79 / 255)
CELL_COLOR = (28 / 255, 25 / 255, 21 / 255)
FONT = "notosc"

# --- page note lists (full block, including the updated * footnote) ---

FF01_ZH_NOTES = [
    "· 来源文件：1.8G+3.5G技术规格书 -.doc",
    "· 特性阻抗：原稿写了 50 Ω 的，以原稿为准；原稿没写的，N 与 SMA 口按 50 Ω。",
    "· 室内型铝合金腔体。测试条件 25 °C、50 Ω、矢量网络分析仪。出货附该件测试报告。",
    "· 互调以原稿这一栏为准。",
    "· * 互调电平按原稿为 ≤−145 dBc。测试条件原稿写作「43dBC」，按行业常规三阶互调（PIM3）双音测试理解为 2×43 dBm，标 *，以工厂书面确认为准。",
    "· 多端口表：插损、抑制、隔离只印该端口原稿里有的格子。标 † 的是合并单元格，字只出现在部分端口，已抄到空白端口，数字未改。",
]
FF01_EN_NOTES = [
    "· Source file: 1.8G+3.5G技术规格书 -.doc",
    "· Impedance: where the source states 50 Ω, that stands. Where it is silent, N and SMA ports are 50 Ω.",
    "· Indoor aluminum cavity. Tested at 25 °C in a 50 Ω system on a vector network analyzer. A test report ships with the unit.",
    "· PIM follows the figure written in the source sheet.",
    "· * The source PIM level is ≤−145 dBc. The test condition was written “43dBC”; this page reads it as the industry-standard two-tone PIM3 test at 2×43 dBm. Marked * and pending written factory confirmation.",
    "· Multi-port sheet: insertion loss, rejection and isolation are printed only where that port’s source cell has text. A cell marked † repeats a merged source cell onto a blank port. The number is unchanged.",
]
FF0708_ZH_NOTES = [
    "SOURCE_PLACEHOLDER",
    "· 特性阻抗：原稿写了 50 Ω 的，以原稿为准；原稿没写的，N 与 SMA 口按 50 Ω。",
    "· 室内型铝合金腔体。测试条件 25 °C、50 Ω、矢量网络分析仪。出货附该件测试报告。",
    "· 原稿没有互调指标。若订单选择低互调档，按 PIM3 ≤ −150 dBc @ 2×43 dBm 测试并写入报告。",
    "· * 原稿有一栏驻波写作 ≤0.9（驻波比不能小于 1，可能是 1.9 的笔误，或把回波损耗写成了驻波）。誊清无法确定是哪一个端口，故未改写成 1.9 或其他值。表内印出的 ≤1.3 是同表其余端口的原稿值；所有驻波栏标 *，以工厂书面确认为准。",
    "· 接头原稿写作 ISMA-F，已改为 SMA-F。",
    "· 多端口表：插损、抑制、隔离只印该端口原稿里有的格子。标 † 的是合并单元格，字只出现在部分端口，已抄到空白端口，数字未改。",
]
FF0708_EN_NOTES = [
    "SOURCE_PLACEHOLDER",
    "· Impedance: where the source states 50 Ω, that stands. Where it is silent, N and SMA ports are 50 Ω.",
    "· Indoor aluminum cavity. Tested at 25 °C in a 50 Ω system on a vector network analyzer. A test report ships with the unit.",
    "· The source sheet has no PIM limit. If the order selects the low-PIM option, test PIM3 to ≤ −150 dBc @ 2×43 dBm and put it on the report.",
    "· * One VSWR cell on the source sheet was written ≤0.9 (VSWR cannot be below 1; it may be a typo for 1.9, or a return-loss figure written as VSWR). The port cannot be identified, so that cell is not rewritten as 1.9 or any other invented value. The ≤1.3 figures shown are those written on the other ports; all VSWR rows are marked * and pending written factory confirmation.",
    "· The connector was written ISMA-F and is corrected to SMA-F.",
    "· Multi-port sheet: insertion loss, rejection and isolation are printed only where that port’s source cell has text. A cell marked † repeats a merged source cell onto a blank port. The number is unchanged.",
]
# source-file lines differ between FF-07 and FF-08
FF07_ZH_SRC = "· 来源文件：3频合路器规格书.doc"
FF07_EN_SRC = "· Source file: 3频合路器规格书.doc"
# FF-08 source filename – confirm from the backup after restore
FF08_ZH_SRC = None  # filled at runtime if needed
FF08_EN_SRC = None

BF_ZH_NOTES = [
    "· 原稿插损、波动未写不等号，本版按最大允许值规范为 ≤。",
    "· 回波损耗由端口驻波比 ≤ 1.3 换算：RL = −20 log10((VSWR−1)/(VSWR+1)) ≈ 17.7 dB。",
    "· 低互调档是订货选项。原稿没有给出实测互调，未选该档时不作为本页保证值。需要时按 2×43 dBm 测试并附报告。",
    "· * 原稿表格内频率写作 1802–1833 MHz；来源文件名「1802-1883滤波器技术规格书.docx」与本型号编号均为 1802–1883。两处不一致。本页暂按文件名和型号印 1802–1883 MHz（带宽 81 MHz），标 *，以工厂书面确认为准。",
    "· 规格来源：1802-1883滤波器技术规格书.docx",
]
BF_ZH_TRAIL = "订货写法：KXT-BF-18021883 + 接头公母 + 颜色（本色/黑色）+ 是否低互调档 + 数量。"
BF_EN_NOTES = [
    "· The source sheet gave insertion loss and ripple without a symbol. This revision states them as maximum values (≤).",
    "· Return loss is calculated from VSWR ≤ 1.3: RL = −20 log10((VSWR−1)/(VSWR+1)) ≈ 17.7 dB.",
    "· Low PIM is an order option. The source sheet has no measured PIM, so it is not a guaranteed value unless that option is ordered and reported.",
    "· * The source table wrote 1802–1833 MHz; the source file name (1802-1883滤波器技术规格书.docx) and the model number are 1802–1883. The two disagree. This page keeps 1802–1883 MHz (bandwidth 81 MHz) after the file name and model, marked *, pending written factory confirmation.",
    "· Source specification: 1802-1883滤波器技术规格书.docx",
]
BF_EN_TRAIL = "Order as: KXT-BF-18021883 + connector gender + finish (natural/black) + low-PIM option + quantity."

CELL_OLD = "≤−145 dBc @ 43dBC *"
CELL_NEW = "≤−145 dBc @ 2×43 dBm *"


def subset_font(text):
    tmp = tempfile.NamedTemporaryFile(suffix=".otf", delete=False).name
    opts = subset.Options()
    opts.name_IDs = ["*"]
    opts.notdef_outline = True
    opts.layout_features = []
    f = subset.load_font(FONTFILE, opts)
    s = subset.Subsetter(opts)
    s.populate(text=text + "0123456789.*—·@×≤≥−°")
    s.subset(f)
    subset.save_font(f, tmp, opts)
    return tmp


def page_lines(page):
    out = []
    for b in page.get_text("dict")["blocks"]:
        for l in b.get("lines", []):
            t = "".join(sp["text"] for sp in l["spans"])
            out.append((l, t))
    return out


def header_y(page, titles=("说明", "Notes")):
    for l, t in page_lines(page):
        if t.strip() in titles:
            return l["bbox"][3]
    raise SystemExit("notes header not found")


def first_note_origin(page):
    """Baseline y of the first · note under the 说明/Notes header."""
    seen_header = False
    for l, t in page_lines(page):
        ts = t.strip()
        if ts in ("说明", "Notes"):
            seen_header = True
            continue
        if seen_header and ts.startswith("·"):
            return l["spans"][0]["origin"][1], l["bbox"][0], l["spans"][0]["size"]
    raise SystemExit("first note not found")


def redact_below(page, y_top, y_bottom=812):
    """Clear the notes area, leaving the header and the footer bar."""
    page.add_redact_annot(pymupdf.Rect(20, y_top, page.rect.width - 20, y_bottom), fill=(1, 1, 1))
    page.apply_redactions(images=0, graphics=0)


def wrap(font, text, size, width):
    """Wrap preferring the last space (English); fall back to a character break (CJK)."""
    out, cur = [], ""
    for ch in text:
        trial = cur + ch
        if cur and font.text_length(trial, size) > width:
            sp = cur.rfind(" ")
            if sp > 0:
                out.append(cur[:sp])
                cur = cur[sp + 1:] + ch
            else:
                out.append(cur)
                cur = ch
        else:
            cur = trial
    if cur:
        out.append(cur)
    return out or [""]


def write_notes(page, fontfile, notes, trailing=None):
    origin_y, x, size = first_note_origin(page)
    # redact from just above the first note to above the footer
    # use the first note's top bbox
    first_top = None
    for l, t in page_lines(page):
        if t.strip().startswith("·"):
            # only notes after the header
            pass
    # Compute top from origin and size
    y_top = origin_y - size - 1
    redact_below(page, y_top)
    font = pymupdf.Font(fontfile=fontfile)
    width = 500  # conservative vs the 515 pt measure
    lh = 11.0
    y = origin_y
    for para in notes:
        for line in wrap(font, para, size, width):
            if y > 800:
                raise SystemExit(f"notes overflow at y={y}: {line!r}")
            page.insert_text((x, y), line, fontname=FONT, fontfile=fontfile,
                             fontsize=size, color=NOTE_COLOR)
            y += lh
    if trailing:
        y += 4
        for line in wrap(font, trailing, size, width):
            page.insert_text((x, y), line, fontname=FONT, fontfile=fontfile,
                             fontsize=size, color=NOTE_COLOR)
            y += lh
    return 1


def replace_cell(page, fontfile, old, new):
    hits = []
    for l, t in page_lines(page):
        if t.strip() == old:
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
        # allow the * to extend a little past the old box
        while font.text_length(new, size) > (l["bbox"][2] - l["bbox"][0]) + 30 and size > 6:
            size -= 0.25
        page.insert_text((l["bbox"][0], s["origin"][1]), new, fontname=FONT,
                         fontfile=fontfile, fontsize=size, color=CELL_COLOR)
        n += 1
    return n


def source_line(page, prefix):
    for _, t in page_lines(page):
        if t.strip().startswith(prefix):
            # may be wrapped; take this first line only if it looks complete
            return t.strip() if t.strip().startswith("·") else None
    return None


def collect_text():
    bag = []
    for seq in (FF01_ZH_NOTES, FF01_EN_NOTES, FF0708_ZH_NOTES, FF0708_EN_NOTES,
                BF_ZH_NOTES, BF_EN_NOTES):
        bag.extend(seq)
    bag += [BF_ZH_TRAIL, BF_EN_TRAIL, CELL_NEW, "1802–1883 MHz *",
            "· 来源文件：3频合路器规格书.doc", "· 来源文件：3频合路器规格书 - 1.doc",
            "· Source file: 3频合路器规格书.doc", "· Source file: 3频合路器规格书 - 1.doc"]
    return " ".join(bag)


def ff0708_sources(path):
    """Read source-file lines from the unpatched PDF."""
    doc = pymupdf.open(path)
    zh = en = None
    for _, t in page_lines(doc[1]):
        if t.strip().startswith("· 来源文件："):
            zh = t.strip(); break
    for _, t in page_lines(doc[3]):
        if t.strip().startswith("· Source file:"):
            en = t.strip(); break
    doc.close()
    return zh, en


def patch_ff01(fontfile):
    path = DS / "KXT-FF-01.pdf"
    doc = pymupdf.open(path)
    n = 0
    for p in doc:
        n += replace_cell(p, fontfile, CELL_OLD, CELL_NEW)
    n += write_notes(doc[1], fontfile, FF01_ZH_NOTES)
    n += write_notes(doc[3], fontfile, FF01_EN_NOTES)
    tmp = str(path) + ".tmp"
    doc.save(tmp, garbage=4, deflate=True)
    doc.close()
    pathlib.Path(tmp).replace(path)
    print(f"KXT-FF-01.pdf: {n} edits")


def patch_ff0708(name, fontfile):
    path = DS / name
    zh_src, en_src = ff0708_sources(path)
    if not zh_src or not en_src:
        raise SystemExit(f"source-file line not found in {name}: {zh_src!r} {en_src!r}")
    zh = [zh_src if i == 0 else x for i, x in enumerate(FF0708_ZH_NOTES)]
    en = [en_src if i == 0 else x for i, x in enumerate(FF0708_EN_NOTES)]
    doc = pymupdf.open(path)
    n = 0
    n += write_notes(doc[1], fontfile, zh)
    n += write_notes(doc[3], fontfile, en)
    tmp = str(path) + ".tmp"
    doc.save(tmp, garbage=4, deflate=True)
    doc.close()
    pathlib.Path(tmp).replace(path)
    print(f"{name}: {n} edits (src zh={zh_src})")


def patch_bf(fontfile):
    path = DS / "KXT-BF-18021883.pdf"
    doc = pymupdf.open(path)
    n = 0
    for p in doc:
        n += replace_cell(p, fontfile, "1802–1883 MHz", "1802–1883 MHz *")
    n += write_notes(doc[0], fontfile, BF_ZH_NOTES, BF_ZH_TRAIL)
    n += write_notes(doc[1], fontfile, BF_EN_NOTES, BF_EN_TRAIL)
    tmp = str(path) + ".tmp"
    doc.save(tmp, garbage=4, deflate=True)
    doc.close()
    pathlib.Path(tmp).replace(path)
    print(f"KXT-BF-18021883.pdf: {n} edits")


def main():
    fontfile = subset_font(collect_text())
    patch_ff01(fontfile)
    patch_ff0708("KXT-FF-07.pdf", fontfile)
    patch_ff0708("KXT-FF-08.pdf", fontfile)
    patch_bf(fontfile)
    print("done")


if __name__ == "__main__":
    main()
