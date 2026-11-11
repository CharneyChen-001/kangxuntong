#!/usr/bin/env python3
"""KXT-FF-11.pdf: the operating-temperature row of port 1 was labelled
"项目" (the source table's header word) instead of "工作温度(℃)". Relabel it on
the Chinese and the English page. The value -30～+60 is unchanged.
Requires PyMuPDF and Noto Sans CJK SC (OTF) at KXT_CJK_FONT. Idempotent."""
import os, pathlib, tempfile
import pymupdf
from fontTools import subset

ROOT = pathlib.Path(__file__).resolve().parent.parent
PDF = ROOT / "website" / "datasheets" / "KXT-FF-11.pdf"
FONTFILE = os.environ.get("KXT_CJK_FONT", "/workspace/kxt-noto-sc.otf")


def small_font(text):
    """Subset of the CJK font with only the glyphs used and no layout features (clean copy-paste)."""
    opts = subset.Options(); opts.layout_features = []; opts.notdef_outline = True
    f = subset.load_font(FONTFILE, opts)
    s = subset.Subsetter(opts); s.populate(text=text); s.subset(f)
    out = os.path.join(tempfile.mkdtemp(), "kxtsc.otf")
    subset.save_font(f, out, opts)
    return out


def main():
    font = small_font("工作温度(℃) / Operating temperature")
    doc = pymupdf.open(PDF)
    n = 0
    for page in doc:
        lines = [l for b in page.get_text("dict")["blocks"] for l in b.get("lines", [])]
        temps = [l for l in lines if "".join(s["text"] for s in l["spans"]).strip() == "-30～+60"]
        en = "Item" in page.get_text()
        for t in temps:
            y = t["bbox"][1]
            for l in lines:
                if "".join(s["text"] for s in l["spans"]).strip() == "项目" and abs(l["bbox"][1] - y) < 1:
                    sp = l["spans"][0]
                    page.add_redact_annot(l["bbox"], fill=False)
                    page.apply_redactions(images=0, graphics=0)
                    label = "工作温度(℃) / Operating temperature" if en else "工作温度(℃)"
                    page.insert_text(sp["origin"], label, fontname="kxtsc", fontfile=font, fontsize=sp["size"],
                                     color=pymupdf.sRGB_to_pdf(sp["color"]))
                    n += 1
    if n:
        doc.save(str(PDF) + ".tmp", garbage=4, deflate=True)
        doc.close()
        pathlib.Path(str(PDF) + ".tmp").replace(PDF)
    print("relabelled", n, "rows")


if __name__ == "__main__":
    main()
