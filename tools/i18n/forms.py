"""Language-aware RFQ form strings for build_site.form_html()."""
from __future__ import annotations

from .meta import EMAIL
from .translate import tr

# Canonical English / Chinese form copy (must stay identical to the existing site).
_EN = dict(
    err="Fill in every required field (name, company, a valid email, country, product, message; quantity on the custom page).",
    name="Name", company="Company", email="Work email", country="Country",
    phone="Phone / WhatsApp", product="Product or model", model="Model",
    qty="Quantity", band="Frequency plan", power="Power", connector="Connector",
    pim="Low-PIM option", pno="Not required", pyes="Required, ≤ −150 dBc",
    msg="Message", send="Send enquiry",
    file="Drawing or band plan (optional)",
    filenote="PDF, DWG, DXF, STEP, JPG or PNG, 10 MB in total. Email larger files.",
    alt="Or:", wa="Send on WhatsApp", mail="Email " + EMAIL,
    note="The enquiry goes straight to " + EMAIL + " and we reply by email. The form is relayed by FormSubmit (formsubmit.co); see the",
    privacy="privacy note", sending="Sending…",
    fail="Sending failed. Please use email or WhatsApp instead; your text is still in the form.",
    subj="New RFQ · cavityfilter.com",
    custom_value="Custom design",
    period=".",
)
_ZH = dict(
    err="请填写所有必填项（姓名、公司、有效邮箱、国家、产品、需求；定制页还要数量）。",
    name="姓名", company="公司", email="邮箱", country="国家或地区",
    phone="电话 / WhatsApp", product="产品或型号", model="型号", qty="数量",
    band="频段", power="功率", connector="接头", pim="是否要低互调档",
    pno="不需要", pyes="需要，≤ −150 dBc", msg="需求说明", send="发送询价",
    file="图纸或频段方案（可选）",
    filenote="PDF、DWG、DXF、STEP、JPG 或 PNG，合计不超过 10 MB。更大的文件请发邮件。",
    alt="也可以：", wa="用 WhatsApp 发送", mail="发邮件到 " + EMAIL,
    note="提交后询价直接发到 " + EMAIL + "，我们用邮件回复。表单经 FormSubmit（formsubmit.co）转发，见",
    privacy="隐私说明", sending="正在发送…",
    fail="发送失败。请改用邮件或 WhatsApp，内容已保留在表单里。",
    subj="新询价 · cavityfilter.com（中文站）",
    custom_value="定制",
    period="。",
)

_SUBJ = {
    "en": "New RFQ · cavityfilter.com",
    "zh": "新询价 · cavityfilter.com（中文站）",
    "ru": "Новый запрос · cavityfilter.com (русская версия)",
    "es": "Nueva RFQ · cavityfilter.com (español)",
    "pt": "Novo RFQ · cavityfilter.com (português)",
    "ar": "طلب تسعير جديد · cavityfilter.com (العربية)",
}


def form_strings(lang: str) -> dict:
    if lang == "zh":
        return dict(_ZH)
    if lang == "en":
        return dict(_EN)
    L = {k: tr(lang, v, record=False) if k not in {"period"} else v for k, v in _EN.items()}
    L["mail"] = tr(lang, "Email sales@cavityfilter.com", record=False)
    L["note"] = tr(lang, "The enquiry goes straight to sales@cavityfilter.com and we reply by email. The form is relayed by FormSubmit (formsubmit.co); see the", record=False)
    L["subj"] = _SUBJ[lang]
    L["custom_value"] = tr(lang, "Custom design", record=False)
    L["period"] = "."
    if lang == "ar":
        L["period"] = "."
    return L
