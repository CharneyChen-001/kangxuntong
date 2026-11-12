#!/usr/bin/env python3
"""Rebuild website/datasheets/KXT-FF-11.pdf from the factory Word sheet.

Source: 5频合路器技术规格书1.doc (user-supplied Word file).
Port 5 insertion loss is 1.0 dB as displayed in Word (the cell XML stored
11.0dB because the leading 1 overflowed a narrow column). Ripple is 1.5 dB
merged across ports 1–4 and 0.7 dB on port 5. The mechanical drawing is
page 2 of the same Word file.

Requires PyMuPDF + fontTools and Noto Sans CJK SC at KXT_CJK_FONT.
"""
import os, pathlib, subprocess, tempfile
import pymupdf
from fontTools import subset

ROOT = pathlib.Path(__file__).resolve().parent.parent
PDF = ROOT / "website" / "datasheets" / "KXT-FF-11.pdf"
DRAW = ROOT / "website" / "assets" / "drawings" / "KXT-FF-11.png"
FONTFILE = os.environ.get("KXT_CJK_FONT", "/workspace/kxt-noto-sc.otf")
SRC_COMMIT = "6893ba6"

# Port columns as displayed in the Word file (not the overflowing XML text).
PORTS = ["1", "2", "3", "4", "5"]
FREQ = ["703-748MHZ", "758-803MHZ", "2500-2570MHZ", "2620-2690MHZ", "3300-3800MHZ"]
BW = ["45MHZ", "45MHZ", "70 MHZ", "70MHZ", "500MHZ"]
IL = ["1.7dB", "1.7dB", "1.7dB", "1.7dB", "1.0dB"]
REJ = [
    "≥80@758-803<br>≥80@2500-2570<br>≥80@2620-2690<br>≥80@3300-3800",
    "≥80@703-748<br>≥80@2500-2570<br>≥80@2620-2690<br>≥80@3300-3800",
    "≥80@703-748<br>≥80@758-803<br>≥80@2620-2690<br>≥80@3300-3800",
    "≥80@703-748<br>≥80@758-803<br>≥80@2500-2570<br>≥80@3300-3800",
    "≥80@703-748<br>≥80@758-803<br>≥80@2500-2570<br>≥80@2620-2690",
]

ZH = dict(
    title="5频合路器技术规格书1",
    sub="KXT-FF-11 · 誊清自工厂 Word 原稿",
    intro="下表按工厂 Word 原稿排版。合并单元格与原稿一致。数字按 Word 中显示的指标誊清。",
    heads=("项目", "1", "2", "3", "4", "5"),
    rows=[
        ("频率范围(MHz)", FREQ),
        ("带宽(MHz)", BW),
        ("插入损耗(dB)", IL),
        ("驻波比", "≤1.3"),
        ("带内波动（dB）", (["1.5dB"] * 4, "0.7dB")),
        ("带外抑制（dB）", REJ),
        ("工作温度(℃)", "-30～+60"),
        ("平均功率容量(W)", "80W"),
        ("工作湿度（%）", "5～95"),
        ("接口形式", "N-F/SMA-F"),
        ("外观", "黑色油漆"),
        ("外形尺寸", "215*184*44"),
    ],
    notes_title="说明",
    notes=[
        "来源文件：5频合路器技术规格书1.doc",
        "特性阻抗：原稿写了 50 Ω 的，以原稿为准；原稿没写的，N 与 SMA 口按 50 Ω。",
        "室内型铝合金腔体。测试条件 25 °C、50 Ω、矢量网络分析仪。出货附该件测试报告。",
        "原稿没有互调指标。若订单选择低互调档，按 PIM3 ≤ −150 dBc @ 2×43 dBm 测试并写入报告。",
        "外形图按同一份 Word 规格书第 2 页机械图。",
        "询价：sales@cavityfilter.com",
    ],
    fig="外形图（原稿第 2 页）",
)
EN = dict(
    title="5-band Cavity Combiner, 703–3800 MHz",
    sub="KXT-FF-11 · Transcribed from the factory Word file",
    intro="The table follows the factory Word sheet, including merged cells. Figures are those displayed in Word.",
    heads=("Item", "1", "2", "3", "4", "5"),
    rows=[
        ("Frequency (MHz)", FREQ),
        ("Bandwidth (MHz)", BW),
        ("Insertion loss (dB)", IL),
        ("VSWR", "≤1.3"),
        ("Ripple (dB)", (["1.5dB"] * 4, "0.7dB")),
        ("Rejection (dB)", REJ),
        ("Operating temperature (°C)", "-30～+60"),
        ("Average power (W)", "80W"),
        ("Humidity (%)", "5～95"),
        ("Connector", "N-F/SMA-F"),
        ("Finish", "黑色油漆"),
        ("Outline", "215*184*44"),
    ],
    notes_title="Notes",
    notes=[
        "Source file: 5频合路器技术规格书1.doc",
        "Impedance: where the source states 50 Ω, that stands. Where it is silent, N and SMA ports are 50 Ω.",
        "Indoor aluminum cavity. Tested at 25 °C in a 50 Ω system on a vector network analyzer. A test report ships with the unit.",
        "The source sheet has no PIM limit. If the order selects the low-PIM option, PIM3 is tested to ≤ −150 dBc @ 2×43 dBm and reported.",
        "The outline drawing is page 2 of the same Word file.",
        "Enquiries: sales@cavityfilter.com",
    ],
    fig="Outline (source sheet, page 2)",
)


def row_html(label, val):
    # val: list of 5, or a shared string (colspan 5), or (list of 4, last)
    if isinstance(val, str):
        return f"<tr><th>{label}</th><td colspan='5'>{val}</td></tr>"
    if isinstance(val, tuple) and len(val) == 2 and isinstance(val[0], list):
        left = "".join(f"<td colspan='4'>{val[0][0]}</td>" if i == 0 else "" for i in range(1))
        # simpler:
        return f"<tr><th>{label}</th><td colspan='4'>{val[0][0]}</td><td>{val[1]}</td></tr>"
    return "<tr><th>" + label + "</th>" + "".join(f"<td>{c}</td>" for c in val) + "</tr>"


def html(t):
    h = t["heads"]
    head = "<tr class='hd'>" + "".join(f"<th>{c}</th>" for c in h) + "</tr>"
    rows = [row_html(lbl, val) for lbl, val in t["rows"]]
    notes = "".join(f"<li>{n}</li>" for n in t["notes"])
    return (
        f"<h1>{t['title']}</h1><p class='sub'>{t['sub']}</p><p>{t['intro']}</p>"
        f"<table>{head}{''.join(rows)}</table>"
        f"<h2>{t['notes_title']}</h2><ul>{notes}</ul>"
        f"<p class='fig'>{t['fig']}</p>"
        f"<img src='KXT-FF-11.png' alt='outline'>"
    )


CSS = """
@font-face { font-family: kxt; src: url(kxt.otf); }
* { font-family: kxt; }
body { font-size: 7.5pt; color: #1c1915; }
h1 { font-size: 13pt; color: #141c24; margin: 0 0 3pt 0; }
h2 { font-size: 9pt; color: #8d5e32; margin: 8pt 0 2pt 0; }
p { margin: 0 0 6pt 0; }
p.sub { font-size: 8pt; color: #5e584f; margin: 0 0 4pt 0; }
p.fig { font-size: 8pt; color: #8d5e32; margin: 8pt 0 3pt 0; }
table { border-collapse: collapse; width: 100%; margin-top: 4pt; }
th, td { border: 0.5pt solid #d8d2c6; padding: 2.5pt 3pt; text-align: left; vertical-align: top; }
tr.hd th { background-color: #141c24; color: #ffffff; text-align: center; }
th { background-color: #f3efe8; width: 16%; }
td { width: 16.8%; }
ul { margin: 0; padding-left: 10pt; color: #5e584f; font-size: 7pt; }
img { width: 100%; max-height: 230pt; object-fit: contain; }
"""


def main():
    text = html(ZH) + html(EN) + "Page 12"
    tmp = tempfile.mkdtemp()
    # copy drawing into archive
    import shutil
    shutil.copy(DRAW, os.path.join(tmp, "KXT-FF-11.png"))
    opts = subset.Options(); opts.name_IDs = ["*"]; opts.notdef_outline = True; opts.layout_features = []
    f = subset.load_font(FONTFILE, opts)
    s = subset.Subsetter(opts)
    s.populate(text=text + "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    s.subset(f)
    subset.save_font(f, os.path.join(tmp, "kxt.otf"), opts)
    arch = pymupdf.Archive(tmp)

    src = subprocess.run(
        ["git", "-C", str(ROOT), "show", f"{SRC_COMMIT}:website/datasheets/KXT-FF-11.pdf"],
        check=True, capture_output=True,
    ).stdout
    srcdoc = pymupdf.open(stream=src, filetype="pdf")
    # Build a 2-page datasheet (ZH + EN) using the chrome of first-commit pages 0 and 2.
    doc = pymupdf.open()
    for src_i, t in ((0, ZH), (2, EN)):
        doc.insert_pdf(srcdoc, from_page=src_i, to_page=src_i)
        page = doc[-1]
        page.add_redact_annot(pymupdf.Rect(0, 52, page.rect.width, 812), fill=(1, 1, 1))
        page.apply_redactions(
            images=pymupdf.PDF_REDACT_IMAGE_REMOVE,
            graphics=pymupdf.PDF_REDACT_LINE_ART_REMOVE_IF_COVERED,
        )
        # rewrite footer page number
        for b in page.get_text("dict")["blocks"]:
            for l in b.get("lines", []):
                txt = "".join(sp["text"] for sp in l["spans"]).strip()
                if txt.startswith("Page "):
                    sp = l["spans"][0]
                    page.add_redact_annot(l["bbox"], fill=False)
                    page.apply_redactions(images=0, graphics=0)
                    page.insert_text(
                        (l["bbox"][0], sp["origin"][1]),
                        f"Page {page.number + 1}",
                        fontname="helv",
                        fontsize=sp["size"],
                        color=(1, 1, 1),
                    )
        page.insert_htmlbox(pymupdf.Rect(36, 62, 559, 805), html(t), css=CSS, archive=arch)
    srcdoc.close()
    doc.set_metadata({
        **doc.metadata,
        "title": "KXT-FF-11",
        "subject": "5-band cavity combiner 703–3800 MHz",
    })
    doc.save(str(PDF) + ".tmp", garbage=4, deflate=True)
    doc.close()
    pathlib.Path(str(PDF) + ".tmp").replace(PDF)
    print("rebuilt", PDF, "bytes", PDF.stat().st_size)


if __name__ == "__main__":
    main()
