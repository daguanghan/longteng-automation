#!/usr/bin/env python3
"""Build the trilingual static site for longtengautomation.com.

Run from the repo root:  python3 _src/build.py
Writes: index.html, solutions.html, equipment.html, projects.html, about.html, contact.html (English, x-default)
        vi/*.html and zh/*.html; preview/longteng_preview_<lang>.html (single file, images inlined, for WeChat)
"""
import base64, html, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from content import *

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOMAIN = "https://longtengautomation.com"
DRAFT = True  # keep noindex until the company approves the content
PAGES = ["index", "solutions", "equipment", "projects", "about", "contact"]
E = html.escape


def L(d, lang):
    return d[lang] if isinstance(d, dict) else d


def prefix(lang):
    return "" if lang == "en" else "../"


def url_for(page, lang):
    base = "" if lang == "en" else f"{lang}/"
    return f"{DOMAIN}/{base}" + ("" if page == "index" else f"{page}.html")


def link(page, lang, from_lang):
    p = prefix(from_lang) + ("" if lang == "en" else f"{lang}/")
    return p + ("index.html" if page == "index" else f"{page}.html")


FAQ = {
    "en": [("How long does a machine or line take?", "Single machines typically take several weeks from design approval; complete lines take longer. We confirm the schedule in the quotation."),
           ("Can you install and commission in Vietnam?", "Yes. Our technicians travel from Guangzhou (about 2 hours' flight to Hanoi) to install, commission and train operators at your factory."),
           ("Can we see the machine before shipment?", "Yes. Every machine passes a factory acceptance test (FAT) in Guangzhou, which you can attend on site or by video."),
           ("What about import duties?", "Most assembly, test and inspection machines are imported into Vietnam at 0% MFN duty; conveyors can benefit from the ASEAN–China certificate of origin (Form E). We prepare the export documents; please confirm duties with your customs broker."),
           ("How do you support us after installation?", "Remote diagnosis, a recommended spare-parts kit with each machine, and a named contact for any question.")],
    "vi": [("Thời gian chế tạo một máy hoặc một dây chuyền là bao lâu?", "Máy đơn thường mất vài tuần kể từ khi duyệt thiết kế; dây chuyền hoàn chỉnh lâu hơn. Tiến độ cụ thể được xác nhận trong báo giá."),
           ("Công ty có lắp đặt và chạy thử tại Việt Nam không?", "Có. Kỹ thuật viên của chúng tôi từ Quảng Châu (khoảng 2 giờ bay đến Hà Nội) sẽ lắp đặt, chạy thử và đào tạo công nhân vận hành tại nhà máy của bạn."),
           ("Có thể xem máy trước khi giao không?", "Có. Mỗi máy đều được nghiệm thu tại xưởng (FAT) ở Quảng Châu; bạn có thể tham dự trực tiếp hoặc qua video."),
           ("Thuế nhập khẩu như thế nào?", "Phần lớn máy lắp ráp, kiểm tra và kiểm tra ngoại quan nhập khẩu vào Việt Nam với thuế suất MFN 0%; băng tải có thể hưởng ưu đãi với C/O mẫu E (ASEAN – Trung Quốc). Chúng tôi chuẩn bị chứng từ xuất khẩu; vui lòng xác nhận thuế với đại lý hải quan của bạn."),
           ("Hỗ trợ sau lắp đặt ra sao?", "Chẩn đoán từ xa, bộ phụ tùng khuyến nghị đi kèm mỗi máy và người phụ trách giải đáp mọi thắc mắc.")],
    "zh": [("一台设备或一条线需要多长时间？", "单机通常在设计确认后数周完成，整线时间更长，具体以报价中的交期为准。"),
           ("能否在越南安装调试？", "可以。技术人员从广州出发（至河内航程约 2 小时），到您的工厂安装调试并培训操作人员。"),
           ("发货前能否看设备？", "可以。每台设备都在广州完成出厂验收（FAT），您可以到场或通过视频见证。"),
           ("进口关税怎么算？", "多数装配、检测与外观检测设备进口越南适用 0% 最惠国税率；输送线凭中国—东盟原产地证（Form E）可享优惠。我们负责出口单证，关税请以您的报关行确认为准。"),
           ("安装后如何服务？", "远程诊断、每台设备配推荐备件包，并有专人对接您的问题。")],
}
FAQ_H = {"en": "Frequently asked questions", "vi": "Câu hỏi thường gặp", "zh": "常见问题"}
MORE = {"en": "View all", "vi": "Xem tất cả", "zh": "查看全部"}
EQ_SUB = {"en": "35 machine types already designed and built, grouped by application. Photos shown where available; every machine is customised to your product.",
          "vi": "35 loại máy đã thiết kế và chế tạo, phân theo ứng dụng. Ảnh được hiển thị khi có; mỗi máy đều được tùy biến theo sản phẩm của bạn.",
          "zh": "已设计制造的 35 类设备，按应用分组；有照片的配图展示。每台设备都按您的产品定制。"}
PRJ_SUB = {"en": "Selected projects. Customer names are withheld; details are shared on request.",
           "vi": "Một số dự án tiêu biểu. Tên khách hàng được giữ kín; thông tin chi tiết cung cấp khi có yêu cầu.",
           "zh": "部分项目示例。客户名称不公开，详情可应询提供。"}
GALLERY_H = {"en": "Our plant", "vi": "Nhà xưởng", "zh": "工厂环境"}
WHY_H = {"en": "Why work with Longteng", "vi": "Vì sao chọn Longteng", "zh": "为什么选择龙腾"}
ZALO = {"en": "Zalo", "vi": "Zalo", "zh": "Zalo"}
CALL = {"en": "Call", "vi": "Gọi điện", "zh": "电话"}


def head(page, lang, inline=False):
    title = f"{L(PAGE_TITLES[page], lang)} | Longteng Automation"
    alts = "".join(f'<link rel="alternate" hreflang="{HTML_LANG[l]}" href="{url_for(page, l)}">' for l in LANGS)
    alts += f'<link rel="alternate" hreflang="x-default" href="{url_for(page, "en")}">'
    robots = '<meta name="robots" content="noindex,nofollow">' if DRAFT else ""
    css = (f"<style>{(ROOT/'assets/css/site.css').read_text()}</style>" if inline
           else f'<link rel="stylesheet" href="{prefix(lang)}assets/css/site.css">')
    org = ('<script type="application/ld+json">{"@context":"https://schema.org","@type":"Organization",'
           '"name":"Longteng Automation","legalName":"Guangzhou Longteng Automation Equipment Co., Ltd.",'
           f'"url":"{DOMAIN}/","telephone":"{PHONE}","address":{{"@type":"PostalAddress","addressLocality":"Guangzhou","addressRegion":"Guangdong","addressCountry":"CN"}}}}</script>')
    return (f'<!doctype html><html lang="{HTML_LANG[lang]}"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width,initial-scale=1">{robots}'
            f'<title>{E(title)}</title><meta name="description" content="{E(DESC[lang])}">'
            f'<link rel="canonical" href="{url_for(page, lang)}">{alts}'
            f'<link rel="icon" href="{prefix(lang)}assets/img/site/logo-mark.jpg">{css}{org}</head><body>')


def img(path, lang, alt="", cls=""):
    return f'<img src="{prefix(lang)}assets/img/{path}" alt="{E(alt)}" loading="lazy"{" class=" + chr(34) + cls + chr(34) if cls else ""}>'


def header(page, lang, single=False):
    nav = []
    for p, label in zip(PAGES, T["nav"][lang]):
        href = f"#{p}" if single else link(p, lang, lang)
        cur = ' class="cur"' if p == page and not single else ""
        nav.append(f'<a href="{href}"{cur}>{E(label)}</a>')
    sw = []
    for l in LANGS:
        href = f"longteng_preview_{l}.html" if single else link(page, l, lang)
        sw.append(f'<a href="{href}"{" class=on" if l == lang else ""}>{LANG_LABEL[l]}</a>')
    home = "#index" if single else link("index", lang, lang)
    quote = "#contact" if single else link("contact", lang, lang)
    draft = f'<div class="draft">{E(T["draft"][lang])}</div>' if DRAFT else ""
    return (f'{draft}<div class="top"><span>{E(T["topbar"][lang])}</span><span><a href="tel:{PHONE_TEL}">{PHONE}</a> · <a href="mailto:{EMAIL}">{EMAIL}</a></span></div>'
            f'<header><a class="logo" href="{home}">{img("site/logo-mark.jpg", lang, "Longteng logo")}<span class="brand">LONGTENG AUTOMATION<small>{E(T["brand_sub"][lang])}</small></span></a>'
            f'<input type="checkbox" id="navt" hidden><label for="navt" class="burger" aria-label="Menu">☰</label>'
            f'<nav>{"".join(nav)}</nav><div class="hr"><span class="lang">{" · ".join(sw)}</span>'
            f'<a class="btn" href="{quote}">{E(T["cta"][lang])}</a></div></header>')


def footer(lang, single=False):
    quote = "#contact" if single else link("contact", lang, lang)
    return (f'<section class="band"><div><h2>{E(T["cta_band_h"][lang])}</h2><p>{E(T["cta_band_p"][lang])}</p></div>'
            f'<a class="btn big" href="{quote}">{E(T["cta"][lang])}</a></section>'
            f'<footer><div><b>LONGTENG AUTOMATION</b><br>{E(T["brand_sub"][lang])}<br>{E(CONTACT["addr"][lang])}</div>'
            f'<div><a href="tel:{PHONE_TEL}">{PHONE}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a><br>© 2026 · {E(T["footer_rights"][lang])}</div></footer>'
            f'<div class="dock"><a href="tel:{PHONE_TEL}">{E(CALL[lang])}</a><a href="mailto:{EMAIL}">Email</a>'
            f'<a class="q" href="{quote}">{E(T["cta"][lang])}</a></div>')


# ── page bodies ──
def body_index(lang, single=False):
    eqlink = "#equipment" if single else link("equipment", lang, lang)
    quote = "#contact" if single else link("contact", lang, lang)
    stats = "".join(f'<div><b>{E(a)}</b><span>{E(b)}</span></div>' for a, b in T["stats"][lang])
    inds = "".join(f'<a class="card" href="{"#solutions" if single else link("solutions", lang, lang) + "#" + i["id"]}">'
                   f'<div class="ph">{img(i["img"], lang, L(i["t"], lang))}</div><div class="tx"><h3>{E(L(i["t"], lang))}</h3><p>{E(L(i["d"], lang))}</p></div></a>'
                   for i in INDUSTRIES)
    feats = "".join(f'<div class="feat"><div class="ph">{img(p["imgs"][0], lang, L(p["t"], lang))}</div><div class="tx"><span class="kick">{E(L(p["ind"], lang))}</span>'
                    f'<h3>{E(L(p["t"], lang))}</h3><p>{E(L(p["d"], lang)[0])}</p></div></div>' for p in PROJECTS[:3])
    steps = "".join(f'<div class="step"><b>{k+1:02d}</b><span>{E(a)}</span><p>{E(b)}</p></div>' for k, (a, b) in enumerate(T["steps"][lang]))
    return (f'<section class="hero" style="background-image:url({prefix(lang)}assets/img/site/hero-line.jpg)"><div class="in">'
            f'<span class="tag">{E(T["hero_tag"][lang])}</span><h1>{E(T["hero_h1"][lang])}</h1><p>{E(T["hero_p"][lang])}</p>'
            f'<div class="cta"><a class="btn" href="{quote}">{E(T["cta"][lang])}</a><a class="ghost" href="{eqlink}">{E(T["hero_btn2"][lang])}</a></div></div></section>'
            f'<div class="stats">{stats}</div>'
            f'<section><h2>{E(T["sol_h"][lang])}</h2><p class="sub">{E(T["sol_sub"][lang])}</p><div class="grid3">{inds}</div></section>'
            f'<section class="alt"><h2>{E(T["feat_h"][lang])}</h2><div class="grid3">{feats}</div></section>'
            f'<section><h2>{E(T["how_h"][lang])}</h2><p class="sub">{E(T["how_sub"][lang])}</p><div class="steps">{steps}</div></section>')


def body_solutions(lang, single=False):
    eqbycat = {"appliances": ["dryer", "shaver", "brush", "test"], "vision": ["elec"], "locks": ["line"], "ev": ["line", "stamp"], "packaging": ["stamp", "brush"], "garment": []}
    out = [f'<section class="pagehead"><h1>{E(T["sol_h"][lang])}</h1><p class="sub">{E(T["sol_sub"][lang])}</p></section>']
    for i in INDUSTRIES:
        names = [e for e in EQ if e[0] in eqbycat[i["id"]]][:6]
        lis = "".join(f"<li>{E(e[3] if lang == 'en' else e[4] if lang == 'vi' else e[2])}</li>" for e in names)
        out.append(f'<section class="ind" id="{i["id"]}"><div class="ph">{img(i["img"], lang, L(i["t"], lang))}</div><div><h2>{E(L(i["t"], lang))}</h2>'
                   f'<p>{E(L(i["d"], lang))}</p>{"<ul>" + lis + "</ul>" if lis else ""}</div></section>')
    return "".join(out)


def body_equipment(lang, single=False):
    out = [f'<section class="pagehead"><h1>{E(L(PAGE_TITLES["equipment"], lang))}</h1><p class="sub">{E(EQ_SUB[lang])}</p></section>']
    for cid, cname in CATS:
        items = [e for e in EQ if e[0] == cid]
        cards = []
        for e in items:
            name = e[3] if lang == "en" else e[4] if lang == "vi" else e[2]
            ph = img("eq/" + e[1], lang, name) if e[1] else f'<div class="noph">{E(L(cname, lang))}</div>'
            cards.append(f'<div class="eq"><div class="ph">{ph}</div><p>{E(name)}</p></div>')
        out.append(f'<section class="eqcat"><h2>{E(L(cname, lang))} <small>{len(items)}</small></h2><div class="grid4">{"".join(cards)}</div></section>')
    vis = [("vision-hot-stamp-defect.jpg", {"en": "Hot-stamping defect detection", "vi": "Phát hiện lỗi ép nhũ", "zh": "烫金瑕疵检测"}),
           ("vision-laser-marking.jpg", {"en": "Vision-guided laser marking", "vi": "Khắc laser định vị bằng camera", "zh": "视觉定位激光打标"}),
           ("vision-assembly.jpg", {"en": "Vision-guided assembly", "vi": "Lắp ráp định vị bằng camera", "zh": "视觉定位组装"}),
           ("vision-screwdriving.jpg", {"en": "Vision-guided screw-driving", "vi": "Bắt vít định vị bằng camera", "zh": "视觉定位打螺丝"}),
           ("vision-glue-inspection.jpg", {"en": "Glue bead inspection", "vi": "Kiểm tra đường keo", "zh": "喷胶外观检测"}),
           ("vision-sorting.jpg", {"en": "Multi-material sorting", "vi": "Phân loại nhiều loại vật liệu", "zh": "多物料分选"})]
    vh = {"en": "CCD vision inspection modules", "vi": "Mô-đun kiểm tra bằng camera CCD", "zh": "CCD 视觉检测模块"}
    cards = "".join(f'<div class="eq"><div class="ph">{img("eq/" + f, lang, L(t, lang))}</div><p>{E(L(t, lang))}</p></div>' for f, t in vis)
    out.append(f'<section class="eqcat"><h2>{E(L(vh, lang))} <small>6</small></h2><div class="grid4">{cards}</div></section>')
    return "".join(out)


def body_projects(lang, single=False):
    out = [f'<section class="pagehead"><h1>{E(L(PAGE_TITLES["projects"], lang))}</h1><p class="sub">{E(PRJ_SUB[lang])}</p></section>']
    for p in PROJECTS:
        pics = "".join(img(i, lang, L(p["t"], lang)) for i in p["imgs"])
        lis = "".join(f"<li>{E(x)}</li>" for x in L(p["d"], lang))
        out.append(f'<section class="prj"><div class="pics n{len(p["imgs"])}">{pics}</div><div><span class="kick">{E(L(p["ind"], lang))}</span>'
                   f'<h2>{E(L(p["t"], lang))}</h2><ul>{lis}</ul></div></section>')
    return "".join(out)


def body_about(lang, single=False):
    paras = "".join(f"<p>{E(x)}</p>" for x in ABOUT["p"][lang])
    vals = "".join(f'<div class="val"><b>{k+1:02d}</b><h3>{E(a)}</h3><p>{E(b)}</p></div>' for k, (a, b) in enumerate(ABOUT["values"][lang]))
    gal = "".join(img(f"site/{g}.jpg", lang, "") for g in ["factory-entrance", "workshop-1", "workshop-2", "design-office", "office", "honour-wall"])
    return (f'<section class="pagehead"><h1>{E(L(ABOUT["h"], lang))}</h1></section>'
            f'<section class="about"><div>{paras}</div><div class="ph">{img("site/factory-entrance.jpg", lang, "")}</div></section>'
            f'<section class="alt"><h2>{E(WHY_H[lang])}</h2><div class="vals">{vals}</div></section>'
            f'<section><h2>{E(GALLERY_H[lang])}</h2><div class="gallery">{gal}</div></section>')


def body_contact(lang, single=False):
    f = CONTACT["fields"][lang]; lab = CONTACT["labels"][lang]
    faq = "".join(f"<details><summary>{E(q)}</summary><p>{E(a)}</p></details>" for q, a in FAQ[lang])
    form = (f'<form class="rfq" onsubmit="var d=new FormData(this),b=[];d.forEach(function(v,k){{b.push(k+\': \'+v)}});'
            f'location.href=\'mailto:{EMAIL}?subject=\'+encodeURIComponent(\'RFQ – \'+(d.get(\'{E(f[0])}\')||\'\'))+\'&body=\'+encodeURIComponent(b.join(\'\\n\'));return false;">'
            f'<input name="{E(f[0])}" placeholder="{E(f[0])}" required><input name="{E(f[1])}" placeholder="{E(f[1])}">'
            f'<input name="{E(f[2])}" placeholder="{E(f[2])}" required><input name="{E(f[3])}" placeholder="{E(f[3])}" required>'
            f'<textarea name="{E(f[4])}" placeholder="{E(f[4])}" rows="5"></textarea><button class="btn" type="submit">{E(f[5])}</button></form>')
    return (f'<section class="pagehead"><h1>{E(L(CONTACT["h"], lang))}</h1><p class="sub">{E(L(CONTACT["sub"], lang))}</p></section>'
            f'<section class="contact"><div>{form}</div><div class="ci"><dl>'
            f'<dt>{E(lab[0])}</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd><dt>{E(lab[1])}</dt><dd><a href="tel:{PHONE_TEL}">{PHONE}</a></dd>'
            f'<dt>{E(lab[2])}</dt><dd>{E(CONTACT["addr"][lang])}</dd><dt>{E(lab[3])}</dt><dd>{E(CONTACT["langs"][lang])}</dd></dl></div></section>'
            f'<section class="alt"><h2>{E(FAQ_H[lang])}</h2><div class="faq">{faq}</div></section>')


BODY = {"index": body_index, "solutions": body_solutions, "equipment": body_equipment, "projects": body_projects, "about": body_about, "contact": body_contact}


def build_site():
    for lang in LANGS:
        d = ROOT if lang == "en" else ROOT / lang
        d.mkdir(exist_ok=True)
        for page in PAGES:
            html_out = head(page, lang) + header(page, lang) + "<main>" + BODY[page](lang) + "</main>" + footer(lang) + "</body></html>"
            (d / f"{page}.html").write_text(html_out, encoding="utf-8")
    print("site pages:", len(LANGS) * len(PAGES))


def build_previews():
    out = ROOT / "preview"; out.mkdir(exist_ok=True)
    cache = {}
    def inline(m):
        rel = m.group(2)
        p = (ROOT / "assets" / "img" / rel)
        if rel not in cache:
            cache[rel] = "data:image/jpeg;base64," + base64.b64encode(p.read_bytes()).decode()
        return m.group(1) + cache[rel]
    for lang in LANGS:
        parts = [head("index", lang, inline=True), header("index", lang, single=True), "<main>"]
        for page in PAGES:
            parts.append(f'<div id="{page}" class="anchor"></div>' + BODY[page](lang, single=True))
        parts.append("</main>" + footer(lang, single=True) + "</body></html>")
        s = "".join(parts)
        s = re.sub(r'((?:src="|url\())(?:\.\./)?assets/img/([^")]+)', inline, s)
        (out / f"longteng_preview_{lang}.html").write_text(s, encoding="utf-8")
    print("previews written")


if __name__ == "__main__":
    build_site()
    build_previews()
