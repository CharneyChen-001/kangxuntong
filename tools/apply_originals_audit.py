#!/usr/bin/env python3
"""Apply the 2026.11.7 original-datasheet audit fixes to product HTML.

Idempotent enough to re-run: replacements are exact old→new strings.
Does not modify 2026.11.7 originals. Run from repo root, then:

    python3 tools/build_site.py

PDF updates are in tools/patch_datasheets_audit.py.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "website"

NOTE_ZH_OLD = (
    "* 原稿有一栏驻波写作 ≤0.9（驻波比不能小于 1，可能是 1.9 的笔误，或把回波损耗写成了驻波）。"
    "誊清无法确定是哪一个端口，故未改写成 1.9 或其他值。表内印出的 ≤1.3 是同表其余端口的原稿值；"
    "所有驻波栏标 *，以工厂书面确认为准。"
)
NOTE_ZH_NEW = (
    "* 原稿第 3 端口驻波写作 ≤0.9（驻波比不能小于 1；格子够宽，Word 显示与 XML 一致，不是溢出。"
    "可能是 1.9 的笔误，或把回波损耗写成了驻波）。本页按原稿印出 ≤0.9，未改写成其他值，标 *。"
    "第 1、2 端口原稿为 ≤1.3。以工厂书面确认为准。"
)
NOTE_EN_OLD = (
    "* One VSWR cell on the source sheet was written ≤0.9 (VSWR cannot be below 1; "
    "it may be a typo for 1.9, or a return-loss figure written as VSWR). The port cannot be identified, "
    "so that cell is not rewritten as 1.9 or any other invented value. The ≤1.3 figures shown are those "
    "written on the other ports; all VSWR rows are marked * and pending written factory confirmation."
)
NOTE_EN_NEW = (
    "* Port 3 VSWR is written ≤0.9 on the source sheet (VSWR cannot be below 1; the cell is wide, "
    "and the Word display matches the XML, so this is not an overflow. It may be a typo for 1.9, "
    "or a return-loss figure written as VSWR). This page prints ≤0.9 as written, marked *, and does not "
    "rewrite it. Ports 1 and 2 are ≤1.3 as written. Pending written factory confirmation."
)

BF_NOTE_ZH_OLD = (
    "* 原稿表格内频率写作 1802–1833 MHz；来源文件名「1802-1883滤波器技术规格书.docx」与本型号编号均为 1802–1883。"
    "两处不一致。本页暂按文件名和型号印 1802–1883 MHz（带宽 81 MHz），标 *，以工厂书面确认为准。"
)
BF_NOTE_ZH_NEW = (
    "* 原稿表格写作 1802–1833 MHz（Word 显示与 XML 一致，格子够宽，不是溢出）；"
    "来源文件名「1802-1883滤波器技术规格书.docx」与型号 KXT-BF-18021883 均为 1802–1883。"
    "本页按表格印 1802–1833 MHz（带宽 31 MHz），标 *。型号编号不变。"
)
BF_NOTE_EN_OLD = (
    "* The source table wrote 1802–1833 MHz; the source file name (1802-1883滤波器技术规格书.docx) "
    "and the model number are 1802–1883. The two disagree. This page keeps 1802–1883 MHz "
    "(bandwidth 81 MHz) after the file name and model, marked *, pending written factory confirmation."
)
BF_NOTE_EN_NEW = (
    "* The source table writes 1802–1833 MHz (the Word display matches the XML; the cell is wide, "
    "so this is not overflow). The file name (1802-1883滤波器技术规格书.docx) and the model number "
    "KXT-BF-18021883 are 1802–1883. This page prints the table value 1802–1833 MHz (bandwidth 31 MHz), "
    "marked *. The catalog model number is unchanged."
)

FF18_NOTE_ZH = "†† 原稿第 2 端口抑制有一处写作 90@22620-2690，同表其余端口均为 2620-2690，按笔误改为 2620-2690，标 *。"
FF18_NOTE_EN = "†† Port 2 rejection was written 90@22620-2690 on the source sheet; every other port uses 2620-2690. Printed as 2620-2690, marked *."

FF06_NOTE_ZH = "原稿第 2 端口抑制末尾有一个未写完的「≥」，未当作指标。第 2 端口驻波是合并单元格，按第 1 端口抄为 ≤1.3，标 †。"
FF06_NOTE_EN = "A dangling “≥” at the end of the port 2 rejection list is not treated as a limit. Port 2 VSWR is a merged cell, copied from port 1 as ≤1.3, marked †."

FREQ_NOTE_ZH = "原稿「频率范围」格是空的，通带只写在表头，本页抄到频率范围这一行。"
FREQ_NOTE_EN = "The source frequency cell is blank; the passband is only in the table header. This page copies it into the frequency row."

HUM_ZH_ROW = "<tr><th>工作湿度</th><td>0～95%</td></tr>"
HUM_EN_ROW = "<tr><th>Humidity</th><td>0～95%</td></tr>"
STOR_ZH_ROW = "<tr><th>存储温度</th><td>−40 °C ~ +70 °C</td></tr>"
STOR_EN_ROW = "<tr><th>Storage temperature</th><td>−40 °C ~ +70 °C</td></tr>"

changes = []

def patch(rel, pairs):
    p = ROOT / rel
    s = p.read_text(encoding="utf-8")
    orig = s
    n = 0
    for a, b in pairs:
        c = s.count(a)
        if c == 0:
            if b in s:
                continue  # already applied
            changes.append(f"MISSING in {rel}: {a[:80]!r}")
            continue
        s = s.replace(a, b)
        n += c
    if s != orig:
        p.write_text(s, encoding="utf-8")
        changes.append(f"patched {rel}: {n} replacements")
    else:
        changes.append(f"unchanged {rel}")

# ---- FF-07 / FF-08 VSWR ----
# Port 1 and 2: drop star on 1.3; port 3 (last VSWR in file) becomes 0.9 *
# Each file has three '≤1.3 *' in VSWR rows. Replace carefully per-port by unique surrounding context.

def patch_ff0708(rel, port3_freq, note_old, note_new):
    p = ROOT / rel
    s = p.read_text(encoding="utf-8")
    orig = s
    # replace VSWR in the table whose frequency is port3
    old3 = f"<th>频率范围(MHz) / Frequency</th><td>{port3_freq}</td></tr><tr><th>带宽(MHz) / Bandwidth</th><td>"
    if old3 not in s:
        changes.append(f"MISSING port3 freq context in {rel}")
        return
    # after finding port3 table, its VSWR should change
    # simpler: replace all ≤1.3 * first with ≤1.3, then set port3 back to 0.9 *
    # But ≤1.3 * only appears on VSWR rows in these files.
    count = s.count("<th>驻波比 / VSWR</th><td>≤1.3 *</td>")
    s = s.replace("<th>驻波比 / VSWR</th><td>≤1.3 *</td>", "<th>驻波比 / VSWR</th><td>≤1.3</td>")
    # now set port 3
    key = f"<th>频率范围(MHz) / Frequency</th><td>{port3_freq}</td></tr>"
    idx = s.find(key)
    if idx < 0:
        changes.append(f"MISSING port3 after strip in {rel}")
        return
    # VSWR in this table
    vswr = "<th>驻波比 / VSWR</th><td>≤1.3</td>"
    pos = s.find(vswr, idx)
    if pos < 0:
        # maybe already 0.9
        if "<th>驻波比 / VSWR</th><td>≤0.9 *</td>" in s[idx:idx+800]:
            pass
        else:
            changes.append(f"MISSING VSWR after port3 in {rel}")
            return
    else:
        s = s[:pos] + "<th>驻波比 / VSWR</th><td>≤0.9 *</td>" + s[pos+len(vswr):]
    if note_old in s:
        s = s.replace(note_old, note_new)
    elif note_new not in s:
        changes.append(f"MISSING note in {rel}")
    if s != orig:
        p.write_text(s, encoding="utf-8")
        changes.append(f"patched {rel}: FF-07/08 VSWR (found {count} starred 1.3 rows)")
    else:
        changes.append(f"unchanged {rel}")

patch_ff0708("zh/products/kxt-ff-07.html", "3300-3800", NOTE_ZH_OLD, NOTE_ZH_NEW)
patch_ff0708("zh/products/kxt-ff-08.html", "3600-3800", NOTE_ZH_OLD, NOTE_ZH_NEW)
patch_ff0708("products/kxt-ff-07.html", "3300-3800", NOTE_EN_OLD, NOTE_EN_NEW)
patch_ff0708("products/kxt-ff-08.html", "3600-3800", NOTE_EN_OLD, NOTE_EN_NEW)

# ---- BF-18021883 ----
bf_pairs_common = [
    ("1802–1883 MHz *", "1802–1833 MHz *"),
    ("1802–1883 MHz", "1802–1833 MHz"),  # titles, cards, meta (after starred already replaced)
    (">81 MHz", ">31 MHz"),  # won't match
    (">81 MHz", ">31 MHz"),
]
# Do carefully
for rel, note_old, note_new in [
    ("zh/products/kxt-bf-18021883.html", BF_NOTE_ZH_OLD, BF_NOTE_ZH_NEW),
    ("products/kxt-bf-18021883.html", BF_NOTE_EN_OLD, BF_NOTE_EN_NEW),
    ("zh/products/index.html", None, None),
    ("products/index.html", None, None),
]:
    p = ROOT / rel
    s = p.read_text(encoding="utf-8")
    orig = s
    n = 0
    if "1802–1883 MHz *" in s:
        s = s.replace("1802–1883 MHz *", "1802–1833 MHz *"); n += orig.count("1802–1883 MHz *")
    # remaining un-starred (titles, cards) — do not touch model number KXT-BF-18021883
    c = s.count("1802–1883 MHz")
    s = s.replace("1802–1883 MHz", "1802–1833 MHz"); n += c
    c = s.count("<th>带宽</th><td>81 MHz</td>")
    s = s.replace("<th>带宽</th><td>81 MHz</td>", "<th>带宽</th><td>31 MHz</td>"); n += c
    c = s.count("<th>Bandwidth</th><td>81 MHz</td>")
    s = s.replace("<th>Bandwidth</th><td>81 MHz</td>", "<th>Bandwidth</th><td>31 MHz</td>"); n += c
    if note_old and note_old in s:
        s = s.replace(note_old, note_new); n += 1
    elif note_old and note_new not in s:
        changes.append(f"MISSING BF note in {rel}")
    if s != orig:
        p.write_text(s, encoding="utf-8")
        changes.append(f"patched {rel}: BF-18021883 ({n})")
    else:
        changes.append(f"unchanged {rel}")

# ---- FF-18 typo 22620 ----
for rel, note, lang in [
    ("zh/products/kxt-ff-18.html", FF18_NOTE_ZH, "zh"),
    ("products/kxt-ff-18.html", FF18_NOTE_EN, "en"),
]:
    p = ROOT / rel
    s = p.read_text(encoding="utf-8")
    orig = s
    if "90@22620-2690" in s:
        s = s.replace("90@22620-2690", "90@2620-2690 *")
    if note not in s and "22620" not in s:
        # insert note before the generic transcription note or after last table
        marker_zh = "<p class=\"note\">按工厂 Word 原稿誊清。"
        marker_en = "<p class=\"note\">Transcribed from the factory Word file."
        marker = marker_zh if lang == "zh" else marker_en
        if marker in s:
            s = s.replace(marker, f"<p class=\"note\">{note}</p>{marker}", 1)
        else:
            changes.append(f"MISSING insert point for FF-18 note in {rel}")
    if s != orig:
        p.write_text(s, encoding="utf-8")
        changes.append(f"patched {rel}: FF-18 22620 typo")
    else:
        changes.append(f"unchanged {rel}")

# ---- FF-06 port 2 VSWR + dangling ≥ ----
for rel, note, lang in [
    ("zh/products/kxt-ff-06.html", FF06_NOTE_ZH, "zh"),
    ("products/kxt-ff-06.html", FF06_NOTE_EN, "en"),
]:
    p = ROOT / rel
    s = p.read_text(encoding="utf-8")
    orig = s
    # port 2: after IL 0.8dB, insert VSWR if missing
    needle = "<th>插入损耗(dB) / Insertion loss</th><td>0.8dB</td></tr><tr><th>带内波动（dB） / Ripple</th><td>0.5dB</td></tr>"
    repl = ("<th>插入损耗(dB) / Insertion loss</th><td>0.8dB</td></tr>"
            "<tr><th>驻波比 / VSWR</th><td>≤1.3 †</td></tr>"
            "<tr><th>带内波动（dB） / Ripple</th><td>0.5dB</td></tr>")
    if needle in s:
        s = s.replace(needle, repl)
    # trailing ≥ after 3400-3600 (end of port 2 rejection)
    s = s.replace("≥90@3400-3600 ≥</td>", "≥90@3400-3600</td>")
    s = s.replace("≥90@3400-3600 / ≥</td>", "≥90@3400-3600</td>")
    if note not in s:
        marker_zh = "<p class=\"note\">按工厂 Word 原稿誊清。"
        marker_en = "<p class=\"note\">Transcribed from the factory Word file."
        marker = marker_zh if lang == "zh" else marker_en
        if marker in s:
            s = s.replace(marker, f"<p class=\"note\">{note}</p>{marker}", 1)
    if s != orig:
        p.write_text(s, encoding="utf-8")
        changes.append(f"patched {rel}: FF-06")
    else:
        changes.append(f"unchanged {rel}")

# ---- empty frequency rows: fill from header ----
DASH_PAGES = [
    "kxt-ff-03","kxt-ff-05","kxt-ff-13","kxt-ff-14",
    "kxt-ff-17","kxt-ff-20","kxt-ff-46","kxt-ff-47",
]
for stem in DASH_PAGES:
    for lang, rel, note in [
        ("zh", f"zh/products/{stem}.html", FREQ_NOTE_ZH),
        ("en", f"products/{stem}.html", FREQ_NOTE_EN),
    ]:
        p = ROOT / rel
        s = p.read_text(encoding="utf-8")
        orig = s
        # first data row of the first spec table: header value
        # pattern: <table class="spec"><tbody><tr><th></th><td>VALUE</td></tr><tr><th>频率范围(MHz) / Frequency</th><td>—</td></tr>
        import re
        m = re.search(
            r'(<table class="spec"><tbody><tr><th></th><td>([^<]+)</td></tr><tr><th>频率范围\(MHz\) / Frequency</th><td>)—(</td></tr>)',
            s,
        )
        if m:
            s = s[:m.start()] + m.group(1) + m.group(2) + m.group(3) + s[m.end():]
        elif "频率范围(MHz) / Frequency</th><td>—</td>" in s:
            changes.append(f"FREQ DASH unexpected format in {rel}")
        if note not in s and "频率范围(MHz) / Frequency</th><td>—</td>" not in s:
            marker_zh = "<p class=\"note\">按工厂 Word 原稿誊清。"
            marker_en = "<p class=\"note\">Transcribed from the factory Word file."
            marker = marker_zh if lang == "zh" else marker_en
            if marker in s:
                s = s.replace(marker, f"<p class=\"note\">{note}</p>{marker}", 1)
        if s != orig:
            p.write_text(s, encoding="utf-8")
            changes.append(f"patched {rel}: fill frequency from header")
        else:
            changes.append(f"unchanged {rel}")

# ---- BF-33003800 humidity + storage ----
for rel, temp_row, hum, stor in [
    ("zh/products/kxt-bf-33003800.html",
     "<tr><th>温度</th><td>−40 °C ~ +70 °C</td></tr>",
     HUM_ZH_ROW, STOR_ZH_ROW),
    ("products/kxt-bf-33003800.html",
     "<tr><th>Temperature</th><td>−40 °C ~ +70 °C</td></tr>",
     HUM_EN_ROW, STOR_EN_ROW),
]:
    p = ROOT / rel
    s = p.read_text(encoding="utf-8")
    orig = s
    if "工作湿度" in s or "Humidity" in s and "0～95%" in s:
        pass
    elif temp_row in s:
        s = s.replace(temp_row, temp_row + hum + stor, 1)
    else:
        changes.append(f"MISSING temp row in {rel}")
    if s != orig:
        p.write_text(s, encoding="utf-8")
        changes.append(f"patched {rel}: humidity/storage")
    else:
        changes.append(f"unchanged {rel}")

print("\n".join(changes))
