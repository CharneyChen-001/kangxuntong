#!/usr/bin/env python3
"""Rebuild website/datasheets/KXT-FF-23.pdf after the code review.

The first transcription split the two-column source table into four
"ports" and printed a model number that may belong to a customer. This
keeps the Rev A header/footer of the old file, clears the body and lays the
same numbers out as one table. No number is changed.
Requires PyMuPDF + fontTools and Noto Sans CJK SC (OTF) at KXT_CJK_FONT.
"""
import os, pathlib, tempfile
import pymupdf
from fontTools import subset

ROOT = pathlib.Path(__file__).resolve().parent.parent
PDF = ROOT / "website" / "datasheets" / "KXT-FF-23.pdf"
FONTFILE = os.environ.get("KXT_CJK_FONT", "/workspace/kxt-noto-sc.otf")

ROWS = [  # (zh label, en label, channel 1, channel 2 or None = one value for both)
    ("工作频段", "Passband", "1710-1785MHz", "1805-1880MHz"),
    ("带内插入损耗", "Insertion loss", "≤1.5dB", "≤1.7dB"),
    ("带内波动", "Ripple", "≤0.5dB", "≤0.8dB"),
    ("输入输出驻波比", "VSWR", "≤1.3", "≤1.3"),
    ("隔离度", "Isolation", "≥80dB", "≥80dB"),
    ("模块尺寸", "Outline", "192*88*46.5带螺杆高度", None),
    ("螺丝固定尺寸", "Mounting pitch", "182mm", None),
    ("螺丝固定孔孔径", "Mounting hole", "4~4.5（mm）", None),
    ("RF信号输入输出接头", "RF connector", "SMA-Female", None),
    ("外观", "Finish", "无明显划伤，丝印正确", None),
]

ZH = dict(
    title="B3 FDD 1.8G 75M 双工器", sub="KXT-FF-23 · 誊清自工厂 Word 原稿",
    intro="原稿是一张两通道表。本页按原稿重排为一张表，数字没有改写。",
    head=("项目", "通道 1（原稿指标）", "通道 2（原稿指标）"),
    notes=[
        "原稿「规格型号」一栏的编号尚未确认可以公开，已隐去。",
        "特性阻抗：原稿没写，N 与 SMA 口按 50 Ω。",
        "室内型铝合金腔体。测试条件 25 °C、50 Ω、矢量网络分析仪。出货附该件测试报告。",
        "原稿没有互调指标。若订单选择低互调档，按 PIM3 ≤ −150 dBc @ 2×43 dBm 测试并写入报告。",
        "机械指标在原稿是两通道共用的合并单元格。",
        "询价：sales@cavityfilter.com",
    ],
)
EN = dict(
    title="B3 FDD 1.8 GHz Cavity Duplexer, 1710–1785 / 1805–1880 MHz", sub="KXT-FF-23 · Transcribed from the factory Word file",
    intro="The source is one two-channel table. It is laid out here as a single table. No number is changed.",
    head=("Item", "Channel 1 (as written)", "Channel 2 (as written)"),
    notes=[
        "The source “model” cell is withheld until its publication is approved.",
        "Impedance: not stated on the source; N and SMA ports are 50 Ω.",
        "Indoor aluminum cavity. Tested at 25 °C in a 50 Ω system on a vector network analyzer. A test report ships with the unit.",
        "The source sheet has no PIM limit. If the order selects the low-PIM option, PIM3 is tested to ≤ −150 dBc @ 2×43 dBm and reported.",
        "Mechanical rows are merged cells shared by both channels on the source sheet.",
        "Enquiries: sales@cavityfilter.com",
    ],
)


def html(t, en):
    rows = []
    for zh, enl, a, b in ROWS:
        label = f"{enl} / {zh}" if en else zh
        if b is None:
            rows.append(f"<tr><th>{label}</th><td colspan='2'>{a}</td></tr>")
        else:
            rows.append(f"<tr><th>{label}</th><td>{a}</td><td>{b}</td></tr>")
    notes = "".join(f"<li>{n}</li>" for n in t["notes"])
    h = t["head"]
    return f"""<h1>{t['title']}</h1><p class='sub'>{t['sub']}</p><p>{t['intro']}</p>
<table><tr class='hd'><th>{h[0]}</th><th>{h[1]}</th><th>{h[2]}</th></tr>{''.join(rows)}</table>
<h2>{'Notes' if en else '说明'}</h2><ul>{notes}</ul>"""


CSS = """
@font-face { font-family: kxt; src: url(kxt.otf); }
* { font-family: kxt; }
body { font-size: 8pt; color: #1c1915; }
h1 { font-size: 14pt; color: #141c24; margin: 0 0 4pt 0; }
h2 { font-size: 9pt; color: #8d5e32; margin: 12pt 0 3pt 0; }
p.sub { font-size: 8.5pt; color: #5e584f; margin: 0 0 6pt 0; }
table { border-collapse: collapse; width: 100%; margin-top: 8pt; }
th, td { border: 0.5pt solid #d8d2c6; padding: 3pt 5pt; text-align: left; }
tr th { background-color: #f3efe8; width: 34%; }
tr.hd th { background-color: #141c24; color: #ffffff; }
ul { margin: 0; padding-left: 10pt; color: #5e584f; font-size: 7.5pt; }
"""


def main():
    text = "".join(html(ZH, False) + html(EN, True)) + "Page 12"
    tmp = tempfile.mkdtemp()
    opts = subset.Options(); opts.name_IDs = ["*"]; opts.notdef_outline = True; opts.layout_features = ["*"]
    f = subset.load_font(FONTFILE, opts)
    s = subset.Subsetter(opts); s.populate(text=text + "0123456789"); s.subset(f)
    subset.save_font(f, os.path.join(tmp, "kxt.otf"), opts)
    arch = pymupdf.Archive(tmp)

    doc = pymupdf.open(PDF)
    keep = [0, 2]  # first page of the Chinese and of the English section
    doc.select(keep)
    for i, (page, t, en) in enumerate(zip(doc, (ZH, EN), (False, True))):
        page.add_redact_annot(pymupdf.Rect(0, 52, page.rect.width, 812), fill=(1, 1, 1))
        page.apply_redactions(images=pymupdf.PDF_REDACT_IMAGE_REMOVE,
                              graphics=pymupdf.PDF_REDACT_LINE_ART_REMOVE_IF_COVERED)
        for b in page.get_text("dict")["blocks"]:
            for l in b.get("lines", []):
                txt = "".join(sp["text"] for sp in l["spans"]).strip()
                if txt.startswith("Page "):
                    sp = l["spans"][0]
                    page.add_redact_annot(l["bbox"], fill=False)
                    page.apply_redactions(images=0, graphics=0)
                    page.insert_text((l["bbox"][0], sp["origin"][1]), f"Page {i + 1}", fontname="helv",
                                     fontsize=sp["size"], color=(1, 1, 1))
        page.insert_htmlbox(pymupdf.Rect(40, 66, 555, 805), html(t, en), css=CSS, archive=arch)
    doc.set_metadata({**doc.metadata, "title": "KXT-FF-23", "subject": "B3 FDD 1.8 GHz cavity duplexer"})
    doc.save(str(PDF) + ".tmp", garbage=4, deflate=True)
    doc.close()
    pathlib.Path(str(PDF) + ".tmp").replace(PDF)
    print("rebuilt", PDF)


if __name__ == "__main__":
    main()
