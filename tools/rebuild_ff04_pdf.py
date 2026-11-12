#!/usr/bin/env python3
"""Rebuild website/datasheets/KXT-FF-04.pdf to match the corrected web table.

The first transcription laid the source columns out as four “ports”
(row numbers in one column, labels in another, values in the last two).
The web pages were already rewritten as two ports plus shared mechanical
rows. This rebuild keeps the Rev A header/footer of the first-commit file
and lays the same numbers out that way. No number is changed.
The font subset carries no OpenType layout features so the text copies
cleanly. Requires PyMuPDF + fontTools and Noto Sans CJK SC at KXT_CJK_FONT.
"""
import os, pathlib, subprocess, tempfile
import pymupdf
from fontTools import subset

ROOT = pathlib.Path(__file__).resolve().parent.parent
PDF = ROOT / "website" / "datasheets" / "KXT-FF-04.pdf"
FONTFILE = os.environ.get("KXT_CJK_FONT", "/workspace/kxt-noto-sc.otf")
SRC_COMMIT = "6893ba6"

# Electrical rows: (zh, en, port1, port2)
ELEC = [
    ("工作频段", "Passband", "2496~2690MHz", "2300-2400MHz"),
    ("带内插入损耗", "Insertion loss", "≤1.2dB", "≤1.2dB"),
    ("带内波动", "Ripple", "≤0.8dB", "≤0.8dB"),
    ("输入输出驻波比", "VSWR", "≤1.3", "≤1.3"),
    ("隔离度", "Isolation", "≥90dB", "≥90dB"),
]
MECH = [
    ("外形尺寸", "Outline", "150*105*40mm含调杆"),
    ("螺丝固定尺寸", "Mounting pitch", "142*97mm"),
    ("螺丝固定孔径", "Mounting hole", "4~3.4（mm）"),
    ("接头类型", "Connector", "N-F/SMA"),
]

ZH = dict(
    title="5G 合路器（N41 / N78）",
    sub="KXT-FF-04 · 誊清自工厂 Word 原稿",
    intro="原稿表格是按列排的项目。本页按行重排为两个端口加共用机械指标，数字没有改写。",
    name_row=("名称", "5G合路器"),
    port_heads=("项目", "端口 1（原稿指标）", "端口 2（原稿指标）"),
    mech_title="机械指标（两端口共用）",
    notes_title="说明",
    notes=[
        "来源文件：1_N41N78合路器指标(4)(1).2026.9.11doc(2).doc。相同内容还出现在：2频合路器指标(2026.9.29.doc。",
        "特性阻抗：原稿写了 50 Ω 的，以原稿为准；原稿没写的，N 与 SMA 口按 50 Ω。",
        "室内型铝合金腔体。测试条件 25 °C、50 Ω、矢量网络分析仪。出货附该件测试报告。",
        "原稿没有互调指标。若订单选择低互调档，按 PIM3 ≤ −150 dBc @ 2×43 dBm 测试并写入报告。",
        "询价：sales@cavityfilter.com",
    ],
)
EN = dict(
    title="2-band Cavity Combiner, 2300–2400 / 2496–2690 MHz",
    sub="KXT-FF-04 · Transcribed from the factory Word file",
    intro="The source table is laid out with items in columns. It is shown here as two ports plus shared mechanical rows. No number is changed.",
    name_row=("Name", "5G合路器"),
    port_heads=("Item", "Port 1 (as written)", "Port 2 (as written)"),
    mech_title="Mechanical (shared by both ports)",
    notes_title="Notes",
    notes=[
        "Source file: 1_N41N78合路器指标(4)(1).2026.9.11doc(2).doc. The same table also appears in: 2频合路器指标(2026.9.29.doc.",
        "Impedance: where the source states 50 Ω, that stands. Where it is silent, N and SMA ports are 50 Ω.",
        "Indoor aluminum cavity. Tested at 25 °C in a 50 Ω system on a vector network analyzer. A test report ships with the unit.",
        "The source sheet has no PIM limit. If the order selects the low-PIM option, PIM3 is tested to ≤ −150 dBc @ 2×43 dBm and reported.",
        "Enquiries: sales@cavityfilter.com",
    ],
)


def html(t, en):
    rows = [f"<tr><th>{t['name_row'][0]}</th><td colspan='2'>{t['name_row'][1]}</td></tr>"]
    for zh, enl, a, b in ELEC:
        label = f"{enl} / {zh}" if en else zh
        rows.append(f"<tr><th>{label}</th><td>{a}</td><td>{b}</td></tr>")
    rows.append(f"<tr class='sec'><th colspan='3'>{t['mech_title']}</th></tr>")
    for zh, enl, v in MECH:
        label = f"{enl} / {zh}" if en else zh
        rows.append(f"<tr><th>{label}</th><td colspan='2'>{v}</td></tr>")
    notes = "".join(f"<li>{n}</li>" for n in t["notes"])
    h = t["port_heads"]
    return f"""<h1>{t['title']}</h1><p class='sub'>{t['sub']}</p><p>{t['intro']}</p>
<table><tr class='hd'><th>{h[0]}</th><th>{h[1]}</th><th>{h[2]}</th></tr>{''.join(rows)}</table>
<h2>{t['notes_title']}</h2><ul>{notes}</ul>"""


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
tr.sec th { background-color: #f3efe8; color: #8d5e32; font-weight: bold; }
ul { margin: 0; padding-left: 10pt; color: #5e584f; font-size: 7.5pt; }
"""


def main():
    text = "".join(html(ZH, False) + html(EN, True)) + "Page 12"
    tmp = tempfile.mkdtemp()
    opts = subset.Options(); opts.name_IDs = ["*"]; opts.notdef_outline = True; opts.layout_features = []
    f = subset.load_font(FONTFILE, opts)
    s = subset.Subsetter(opts); s.populate(text=text + "0123456789"); s.subset(f)
    subset.save_font(f, os.path.join(tmp, "kxt.otf"), opts)
    arch = pymupdf.Archive(tmp)

    src = subprocess.run(["git", "-C", str(ROOT), "show", f"{SRC_COMMIT}:website/datasheets/KXT-FF-04.pdf"],
                         check=True, capture_output=True).stdout
    doc = pymupdf.open(stream=src, filetype="pdf")
    assert doc.page_count == 2
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
    doc.set_metadata({**doc.metadata, "title": "KXT-FF-04", "subject": "2-band cavity combiner 2300–2400 / 2496–2690 MHz"})
    doc.save(str(PDF) + ".tmp", garbage=4, deflate=True)
    doc.close()
    pathlib.Path(str(PDF) + ".tmp").replace(PDF)
    print("rebuilt", PDF)


if __name__ == "__main__":
    main()
