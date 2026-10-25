#!/usr/bin/env python3
"""Build the trilingual static site for longtengautomation.com (v2, premium layout).

Run from the repo root:  python3 _src/build.py
Writes 7 pages × 3 languages (English at root = x-default, /vi/, /zh/) and single-file previews in preview/.
"""
import base64, html, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from content import *

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOMAIN = "https://longtengautomation.com"
DRAFT = True  # keep noindex until the company approves the content
PAGES = ["index", "solutions", "equipment", "projects", "innovation", "about", "contact"]
E = html.escape


def L(d, lang):
    return d[lang] if isinstance(d, dict) else d


def pre(lang):
    return "" if lang == "en" else "../"


def url_for(page, lang):
    base = "" if lang == "en" else f"{lang}/"
    return f"{DOMAIN}/{base}" + ("" if page == "index" else f"{page}.html")


def link(page, lang, from_lang, single=False):
    if single:
        return f"#{page}"
    p = pre(from_lang) + ("" if lang == "en" else f"{lang}/")
    return p + ("index.html" if page == "index" else f"{page}.html")


def img(path, lang, alt="", cls=""):
    c = f' class="{cls}"' if cls else ""
    return f'<img src="{pre(lang)}assets/img/{path}" alt="{E(alt)}" loading="lazy"{c}>'


# ── inline icons (24×24 line style) ──
def ico(name):
    P = {
        "assembly": '<circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.6 1.6 0 0 0 .3 1.8l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1a1.6 1.6 0 0 0-1.8-.3 1.6 1.6 0 0 0-1 1.5V21a2 2 0 0 1-4 0v-.1a1.6 1.6 0 0 0-1-1.5 1.6 1.6 0 0 0-1.8.3l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1a1.6 1.6 0 0 0 .3-1.8 1.6 1.6 0 0 0-1.5-1H3a2 2 0 0 1 0-4h.1a1.6 1.6 0 0 0 1.5-1 1.6 1.6 0 0 0-.3-1.8l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1a1.6 1.6 0 0 0 1.8.3H9a1.6 1.6 0 0 0 1-1.5V3a2 2 0 0 1 4 0v.1a1.6 1.6 0 0 0 1 1.5 1.6 1.6 0 0 0 1.8-.3l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1a1.6 1.6 0 0 0-.3 1.8V9a1.6 1.6 0 0 0 1.5 1H21a2 2 0 0 1 0 4h-.1a1.6 1.6 0 0 0-1.5 1z"/>',
        "vision": '<path d="M2 12s3.6-7 10-7 10 7 10 7-3.6 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/><path d="M12 2v2M12 20v2"/>',
        "laser": '<path d="M12 2v8"/><path d="M8 6l4 4 4-4"/><path d="M4 14h16"/><path d="M12 14l-3 8M12 14l3 8M12 14v8"/>',
        "test": '<path d="M12 21a9 9 0 1 1 9-9"/><path d="M12 12l4-4"/><path d="M16 21h5M18.5 18.5v5"/>',
        "badge": '<circle cx="12" cy="9" r="6"/><path d="M8.5 13.5L7 22l5-3 5 3-1.5-8.5"/>',
        "patent": '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M9 13h6M9 17h6"/>',
        "globe": '<circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15 15 0 0 1 0 20M12 2a15 15 0 0 0 0 20"/>',
        "plane": '<path d="M17.8 19.2L16 11l3.5-3.5C21 6 21.5 4 21 3c-1-.5-3 0-4.5 1.5L13 8 4.8 6.2c-.5-.1-.9.1-1.1.5l-.3.5c-.2.5-.1 1 .3 1.3L9 12l-2 3H4l-1 1 3 2 2 3 1-1v-3l3-2 3.5 5.3c.3.4.8.5 1.3.3l.5-.2c.4-.3.6-.7.5-1.2z"/>',
        "video": '<rect x="2" y="6" width="14" height="12" rx="2"/><path d="M22 8l-6 4 6 4z"/>',
        "chat": '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
        "wrench": '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.8-3.8a6 6 0 0 1-7.9 7.9l-6.9 6.9a2.1 2.1 0 0 1-3-3l6.9-6.9a6 6 0 0 1 7.9-7.9z"/>',
        "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
        "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/>',
        "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="M22 6l-10 7L2 6"/>',
    }
    return f'<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{P[name]}</svg>'


GRID_SVG = ('<svg class="grid" viewBox="0 0 800 600" preserveAspectRatio="none" aria-hidden="true"><defs><pattern id="g" width="40" height="40" patternUnits="userSpaceOnUse">'
            '<path d="M40 0H0V40" fill="none" stroke="rgba(120,170,255,.10)" stroke-width="1"/></pattern></defs><rect width="800" height="600" fill="url(#g)"/>'
            '<path d="M0 470 C 200 420 330 520 520 430 S 760 380 800 400" stroke="rgba(40,140,255,.35)" stroke-width="1.5" fill="none"/>'
            '<path d="M0 500 C 220 460 360 560 560 470 S 760 420 800 440" stroke="rgba(240,122,30,.30)" stroke-width="1.2" fill="none"/></svg>')

STR = {
    "trusted": {"en": "Recognised by", "vi": "Được công nhận", "zh": "资质认定"},
    "ind_h": {"en": "Industries we serve", "vi": "Ngành phục vụ", "zh": "服务行业"},
    "ind_sub": {"en": "From personal-care appliances to EV components — production lines designed around your product.", "vi": "Từ thiết bị chăm sóc cá nhân đến linh kiện xe điện — dây chuyền thiết kế theo sản phẩm của bạn.", "zh": "从个护小家电到新能源汽车零部件，围绕您的产品设计产线。"},
    "more": {"en": "Learn more", "vi": "Xem thêm", "zh": "了解更多"},
    "all_eq": {"en": "All equipment", "vi": "Tất cả thiết bị", "zh": "全部设备"},
    "all_prj": {"en": "All projects", "vi": "Tất cả dự án", "zh": "全部案例"},
    "see_innov": {"en": "Patents & certificates", "vi": "Sáng chế & chứng nhận", "zh": "专利与证书"},
    "faq_h": {"en": "Frequently asked questions", "vi": "Câu hỏi thường gặp", "zh": "常见问题"},
    "eq_sub": {"en": "35 machine types already designed and built, grouped by application. Every machine is customised to your product.", "vi": "35 loại máy đã thiết kế và chế tạo, phân theo ứng dụng. Mỗi máy đều được tùy biến theo sản phẩm của bạn.", "zh": "已设计制造的 35 类设备，按应用分组；每台设备都按您的产品定制。"},
    "all": {"en": "All", "vi": "Tất cả", "zh": "全部"},
    "prj_sub": {"en": "Selected projects. Customer names are withheld; details are shared on request.", "vi": "Một số dự án tiêu biểu. Tên khách hàng được giữ kín; thông tin chi tiết cung cấp khi có yêu cầu.", "zh": "部分项目示例。客户名称不公开，详情可应询提供。"},
    "noph": {"en": "Photo available on request", "vi": "Có ảnh khi yêu cầu", "zh": "实机照片可索取"},
    "k_sea": {"en": "Regional service network", "vi": "Mạng lưới dịch vụ khu vực", "zh": "区域服务网络"},
    "k_feat": {"en": "Case studies", "vi": "Dự án thực tế", "zh": "项目案例"},
    "k_creds": {"en": "Certified & recognised", "vi": "Chứng nhận & công nhận", "zh": "资质认定"},
    "k_pat": {"en": "Intellectual property", "vi": "Sở hữu trí tuệ", "zh": "知识产权"},
    "k_tl": {"en": "Our journey", "vi": "Hành trình phát triển", "zh": "发展历程"},
    "k_why": {"en": "Why Longteng", "vi": "Vì sao chọn Longteng", "zh": "选择龙腾"},
    "k_plant": {"en": "Facilities", "vi": "Cơ sở vật chất", "zh": "生产基地"},
    "why_h": {"en": "Why manufacturers choose Longteng", "vi": "Vì sao nhà sản xuất chọn Longteng", "zh": "制造企业为什么选择龙腾"},
    "plant_h": {"en": "Our plant", "vi": "Nhà xưởng", "zh": "工厂环境"},
    "vision_title": {"en": "CCD vision inspection modules", "vi": "Mô-đun kiểm tra bằng camera CCD", "zh": "CCD 视觉检测模块"},
    "contact_cards": {"en": ["Sales & engineering", "Phone / WeChat", "Factory"], "vi": ["Kinh doanh & kỹ thuật", "Điện thoại / WeChat", "Nhà máy"], "zh": ["销售与技术", "电话 / 微信", "工厂"]},
    "call": {"en": "Call", "vi": "Gọi", "zh": "电话"},
}

FAQ = {
    "en": [("How long does a machine or line take?", "Single machines typically take several weeks from design approval; complete lines take longer. We confirm the schedule in the quotation."),
           ("Can you install and commission in Vietnam?", "Yes. Our technicians travel from Guangzhou (about 2 hours' flight to Hanoi) to install, commission and train operators at your factory."),
           ("Can we see the machine before shipment?", "Yes. Every machine passes a factory acceptance test (FAT) in Guangzhou, which you can attend on site or by live video."),
           ("What about import duties into Vietnam?", "Most assembly, test and inspection machines are imported into Vietnam at 0% MFN duty; conveyors can benefit from the ASEAN–China certificate of origin (Form E). We prepare the export documents; please confirm duties with your customs broker."),
           ("How do you support us after installation?", "Remote diagnosis, a recommended spare-parts kit with each machine, and a named contact for any question.")],
    "vi": [("Thời gian chế tạo một máy hoặc một dây chuyền là bao lâu?", "Máy đơn thường mất vài tuần kể từ khi duyệt thiết kế; dây chuyền hoàn chỉnh lâu hơn. Tiến độ cụ thể được xác nhận trong báo giá."),
           ("Công ty có lắp đặt và chạy thử tại Việt Nam không?", "Có. Kỹ thuật viên của chúng tôi từ Quảng Châu (khoảng 2 giờ bay đến Hà Nội) sẽ lắp đặt, chạy thử và đào tạo công nhân vận hành tại nhà máy của bạn."),
           ("Có thể xem máy trước khi giao không?", "Có. Mỗi máy đều được nghiệm thu tại xưởng (FAT) ở Quảng Châu; bạn có thể tham dự trực tiếp hoặc qua video trực tuyến."),
           ("Thuế nhập khẩu vào Việt Nam như thế nào?", "Phần lớn máy lắp ráp, kiểm tra và kiểm tra ngoại quan nhập khẩu vào Việt Nam với thuế suất MFN 0%; băng tải có thể hưởng ưu đãi với C/O mẫu E (ASEAN – Trung Quốc). Chúng tôi chuẩn bị chứng từ xuất khẩu; vui lòng xác nhận thuế với đại lý hải quan của bạn."),
           ("Hỗ trợ sau lắp đặt ra sao?", "Chẩn đoán từ xa, bộ phụ tùng khuyến nghị đi kèm mỗi máy và người phụ trách giải đáp mọi thắc mắc.")],
    "zh": [("一台设备或一条线需要多长时间？", "单机通常在设计确认后数周完成，整线时间更长，具体以报价中的交期为准。"),
           ("能否在越南安装调试？", "可以。技术人员从广州出发（至河内航程约 2 小时），到您的工厂安装调试并培训操作人员。"),
           ("发货前能否看设备？", "可以。每台设备都在广州完成出厂验收（FAT），您可以到场或通过实时视频见证。"),
           ("进口越南的关税怎么算？", "多数装配、检测与外观检测设备进口越南适用 0% 最惠国税率；输送线凭中国—东盟原产地证（Form E）可享优惠。我们负责出口单证，关税请以您的报关行确认为准。"),
           ("安装后如何服务？", "远程诊断、每台设备配推荐备件包，并有专人对接您的问题。")],
}


def head(page, lang, inline=False):
    title = f"{L(PAGE_TITLES[page], lang)} | Longteng Automation"
    alts = "".join(f'<link rel="alternate" hreflang="{HTML_LANG[l]}" href="{url_for(page, l)}">' for l in LANGS)
    alts += f'<link rel="alternate" hreflang="x-default" href="{url_for(page, "en")}">'
    robots = '<meta name="robots" content="noindex,nofollow">' if DRAFT else ""
    if inline:
        fonts = (ROOT / "assets/fonts/inter-local.css").read_text()
        for fn in ["inter-latin.woff2", "inter-latin-ext.woff2", "inter-vietnamese.woff2"]:
            b64 = base64.b64encode((ROOT / "assets/fonts" / fn).read_bytes()).decode()
            fonts = fonts.replace(f"../fonts/{fn}", f"data:font/woff2;base64,{b64}")
        css = f"<style>{fonts}{(ROOT/'assets/css/site.css').read_text()}</style>"
    else:
        css = (f'<link rel="preload" href="{pre(lang)}assets/fonts/inter-latin.woff2" as="font" type="font/woff2" crossorigin>'
               f'<link rel="stylesheet" href="{pre(lang)}assets/fonts/inter-local.css"><link rel="stylesheet" href="{pre(lang)}assets/css/site.css">')
    org = ('<script type="application/ld+json">{"@context":"https://schema.org","@type":"Organization",'
           '"name":"Longteng Automation","legalName":"Guangzhou Longteng Automation Equipment Co., Ltd.",'
           f'"url":"{DOMAIN}/","logo":"{DOMAIN}/assets/img/site/logo-mark.jpg","telephone":"{PHONE}",'
           '"address":{"@type":"PostalAddress","addressLocality":"Guangzhou","addressRegion":"Guangdong","addressCountry":"CN"}}</script>')
    return (f'<!doctype html><html lang="{HTML_LANG[lang]}"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width,initial-scale=1">{robots}<meta name="theme-color" content="#06142b">'
            f'<title>{E(title)}</title><meta name="description" content="{E(DESC[lang])}">'
            f'<meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(DESC[lang])}">'
            f'<meta property="og:image" content="{DOMAIN}/assets/img/site/hero-line.jpg">'
            f'<link rel="canonical" href="{url_for(page, lang)}">{alts}'
            f'<link rel="icon" href="{pre(lang)}assets/img/site/logo-mark.jpg">{css}{org}</head>')


def header(page, lang, single=False):
    over = " over" if page == "index" and not single else ""
    nav = "".join(f'<a href="{link(p, lang, lang, single)}"{" class=cur" if p == page and not single else ""}>{E(lab)}</a>'
                  for p, lab in zip(PAGES, T["nav"][lang]))
    sw = "".join(f'<a href="{("longteng_preview_" + l + ".html") if single else link(page, l, lang)}"{" class=on" if l == lang else ""}>{LANG_LABEL[l]}</a>' for l in LANGS)
    draft = f'<div class="draft">{E(T["draft"][lang])}</div>' if DRAFT else ""
    return (f'<body class="p-{page}">{draft}<header class="hd{over}"><div class="wrap hdin">'
            f'<a class="logo" href="{link("index", lang, lang, single)}">{img("site/logo-mark.jpg", lang, "Longteng")}<span><b>LONGTENG</b><i>AUTOMATION</i></span></a>'
            f'<nav id="nav">{nav}</nav><div class="hr"><div class="lang">{sw}</div>'
            f'<a class="btn sm" href="{link("contact", lang, lang, single)}">{E(T["quote"][lang])}</a>'
            f'<button class="burger" aria-label="Menu" onclick="document.body.classList.toggle(\'navopen\')"><span></span><span></span><span></span></button></div></div></header>')


def footer(lang, single=False):
    cols = "".join(f'<a href="{link(p, lang, lang, single)}">{E(lab)}</a>' for p, lab in zip(PAGES, T["nav"][lang]))
    creds = "".join(f"<li>{E(L(t, lang))}</li>" for t, _ in CREDS[:3])
    return (f'<section class="ctaband"><div class="wrap ctain"><div><span class="kick light">{E(T["hero_kicker"][lang].split(" · ")[0])}</span>'
            f'<h2>{E(T["cta_band_h"][lang])}</h2><p>{E(T["cta_band_p"][lang])}</p></div>'
            f'<div class="ctabtns"><a class="btn lg" href="{link("contact", lang, lang, single)}">{E(T["cta"][lang])}{ico("arrow")}</a>'
            f'<a class="ghost" href="tel:{PHONE_TEL}">{ico("phone")}{PHONE}</a></div></div></section>'
            f'<footer class="ft"><div class="wrap ftin"><div class="fbrand">{img("site/logo-mark.jpg", lang, "Longteng")}<div><b>LONGTENG AUTOMATION</b>'
            f'<p>{E(T["brand_sub"][lang])}</p><p>{E(CONTACT["addr"][lang])}</p></div></div>'
            f'<div><h4>{E(T["nav"][lang][0])}</h4><nav class="fnav">{cols}</nav></div>'
            f'<div><h4>{E(CREDS_H[lang])}</h4><ul class="fcred">{creds}</ul></div>'
            f'<div><h4>{E(T["nav"][lang][-1])}</h4><p><a href="tel:{PHONE_TEL}">{ico("phone")}{PHONE}</a></p><p><a href="mailto:{EMAIL}">{ico("mail")}{EMAIL}</a></p>'
            f'<p class="langs">{E(CONTACT["langs"][lang])}</p></div></div>'
            f'<div class="wrap fbot">© 2026 Guangzhou Longteng Automation Equipment Co., Ltd. · {E(T["footer_rights"][lang])}</div></footer>'
            f'<div class="dock"><a href="tel:{PHONE_TEL}">{ico("phone")}{E(STR["call"][lang])}</a><a href="mailto:{EMAIL}">{ico("mail")}Email</a>'
            f'<a class="q" href="{link("contact", lang, lang, single)}">{E(T["quote"][lang])}</a></div>')


def pagehead(title, sub, lang, bg="site/workshop-1.jpg"):
    return (f'<section class="ph" style="--bg:url(../img/{bg})">{GRID_SVG}<div class="wrap phin">'
            f'<h1>{E(title)}</h1>{"<p>" + E(sub) + "</p>" if sub else ""}</div></section>')


def sea_map(lang):
    W, H = 560, 440
    def xy(lon, lat):
        return 30 + (lon - 98) / 25 * (W - 60), 30 + (25 - lat) / 33 * (H - 60)
    dots = "".join(f'<circle cx="{x}" cy="{y}" r="1.2" fill="rgba(140,180,255,.22)"/>' for x in range(14, W, 16) for y in range(14, H, 16))
    gx, gy = xy(113.26, 23.13)
    arcs, nodes = [], []
    for name_en, name_vi, name_zh, lon, lat, t in CITIES:
        x, y = xy(lon, lat)
        nm = {"en": name_en, "vi": name_vi, "zh": name_zh}[lang]
        if t:
            cx, cy = (gx + x) / 2 + (y - gy) * .18, (gy + y) / 2 - (x - gx) * .18
            arcs.append(f'<path d="M{gx:.0f},{gy:.0f} Q{cx:.0f},{cy:.0f} {x:.0f},{y:.0f}" class="arc"/>')
            nodes.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="5" class="node"/><text x="{x+9:.0f}" y="{y+4:.0f}" class="lbl">{E(nm)}</text>'
                         f'<text x="{x+9:.0f}" y="{y+19:.0f}" class="tm">{t}</text>')
        else:
            nodes.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="16" class="pulse"/><circle cx="{x:.0f}" cy="{y:.0f}" r="7" class="hub"/>'
                         f'<text x="{x+14:.0f}" y="{y-10:.0f}" class="lbl hubl">{E(nm)} · HQ</text>')
    return f'<svg class="seamap" viewBox="0 0 {W} {H}" role="img" aria-label="{E(SEA_H[lang])}">{dots}{"".join(arcs)}{"".join(nodes)}</svg>'


# ── bodies ──
def body_index(lang, single=False):
    S = single
    stats = "".join(f'<div><b>{E(a)}</b><span>{E(b)}</span></div>' for a, b in T["stats"][lang])
    badges = "".join(f'<div class="bdg">{ico("badge")}<span>{E(L(t, lang))}</span></div>' for t, _ in CREDS)
    caps = "".join(f'<div class="cap rv"><div class="capi">{ico(k)}</div><span class="num">0{n+1}</span><h3>{E(L(t, lang))}</h3><p>{E(L(d, lang))}</p></div>'
                   for n, (k, t, d) in enumerate(CAPS))
    tiles = "".join(f'<a class="tile t{n} rv" href="{link("solutions", lang, lang, S)}{"" if S else "#" + i["id"]}" style="--img:url(../img/{i["img"]})">'
                    f'<div class="tc"><h3>{E(L(i["t"], lang))}</h3><p>{E(L(i["d"], lang))}</p><span class="go">{E(STR["more"][lang])}{ico("arrow")}</span></div></a>'
                    for n, i in enumerate(INDUSTRIES))
    pts = "".join(f'<li>{ico(ic)}{E(p)}</li>' for ic, p in zip(["plane", "video", "chat", "wrench"], SEA_POINTS[lang]))
    feats = "".join(f'<a class="pc rv" href="{link("projects", lang, lang, S)}"><div class="pci">{img(p["imgs"][0], lang, L(p["t"], lang))}</div>'
                    f'<div class="pct"><span class="kick">{E(L(p["ind"], lang))}</span><h3>{E(L(p["t"], lang))}</h3><p>{E(L(p["d"], lang)[0])}</p></div></a>' for p in PROJECTS[:3])
    steps = "".join(f'<div class="st rv"><b>{k+1:02d}</b><h4>{E(a)}</h4><p>{E(b)}</p></div>' for k, (a, b) in enumerate(T["steps"][lang]))
    return (f'<section class="hero" style="--bg:url(../img/site/hero-line.jpg)">{GRID_SVG}<div class="wrap heroin">'
            f'<div class="htxt"><span class="kick light">{E(T["hero_kicker"][lang])}</span><h1>{E(T["hero_h1"][lang])}</h1><p>{E(T["hero_p"][lang])}</p>'
            f'<div class="hbtns"><a class="btn lg" href="{link("contact", lang, lang, S)}">{E(T["cta"][lang])}{ico("arrow")}</a>'
            f'<a class="ghost lg" href="{link("equipment", lang, lang, S)}">{E(T["hero_btn2"][lang])}</a></div></div>'
            f'<div class="hcards"><div class="hc a">{img("eq/ptc-line-b.jpg", lang, "")}</div><div class="hc b">{img("eq/vision-laser-marking.jpg", lang, "")}</div>'
            f'<div class="hc c">{img("eq/laser-weld-cell.jpg", lang, "")}</div></div></div>'
            f'<div class="wrap"><div class="kpis">{stats}</div></div></section>'
            f'<section class="trust"><div class="wrap trin"><span class="tlab">{E(STR["trusted"][lang])}</span><div class="bdgs">{badges}</div></div></section>'
            f'<section class="sec"><div class="wrap"><div class="shead rv"><span class="kick">{E(CAPS_H[lang])}</span><h2>{E(CAPS_SUB[lang])}</h2></div><div class="caps">{caps}</div></div></section>'
            f'<section class="sec alt"><div class="wrap"><div class="shead rv"><span class="kick">{E(STR["ind_h"][lang])}</span><h2>{E(STR["ind_sub"][lang])}</h2></div><div class="bento">{tiles}</div></div></section>'
            f'<section class="sea"><div class="wrap seain"><div class="seat rv"><span class="kick light">{E(STR["k_sea"][lang])}</span><h2>{E(SEA_H[lang])}</h2><p>{E(SEA_P[lang])}</p><ul class="pts">{pts}</ul>'
            f'<p class="note">{E(SEA_NOTE[lang])}</p></div><div class="seam rv">{sea_map(lang)}</div></div></section>'
            f'<section class="sec"><div class="wrap"><div class="shead row rv"><div><span class="kick">{E(STR["k_feat"][lang])}</span><h2>{E(T["feat_h"][lang])}</h2></div>'
            f'<a class="more" href="{link("projects", lang, lang, S)}">{E(STR["all_prj"][lang])}{ico("arrow")}</a></div><div class="pcs">{feats}</div></div></section>'
            f'<section class="sec alt"><div class="wrap"><div class="shead rv"><span class="kick">{E(T["how_h"][lang])}</span><h2>{E(T["how_sub"][lang])}</h2></div><div class="steps">{steps}</div></div></section>')


def body_solutions(lang, single=False):
    eqbycat = {"appliances": ["dryer", "shaver", "brush", "test"], "vision": ["elec"], "locks": ["line"], "ev": ["line", "stamp"], "packaging": ["stamp", "brush"], "garment": []}
    out = [pagehead(T["sol_h"][lang], T["sol_sub"][lang], lang, "site/workshop-2.jpg")]
    for n, i in enumerate(INDUSTRIES):
        names = [e for e in EQ if e[0] in eqbycat[i["id"]]][:6]
        lis = "".join(f"<li>{E(e[3] if lang == 'en' else e[4] if lang == 'vi' else e[2])}</li>" for e in names)
        out.append(f'<section class="ind{" rev" if n % 2 else ""}" id="{i["id"]}"><div class="wrap indin"><div class="indi rv">{img(i["img"], lang, L(i["t"], lang))}</div>'
                   f'<div class="indt rv"><span class="kick">{n+1:02d}</span><h2>{E(L(i["t"], lang))}</h2><p>{E(L(i["d"], lang))}</p>{"<ul class=chk>" + lis + "</ul>" if lis else ""}'
                   f'<a class="more" href="{link("contact", lang, lang, single)}">{E(T["quote"][lang])}{ico("arrow")}</a></div></div></section>')
    return "".join(out)


CAT_ICO = {"dryer": "assembly", "shaver": "assembly", "brush": "assembly", "test": "test",
           "elec": "wrench", "stamp": "laser", "line": "assembly"}


def body_equipment(lang, single=False):
    filt = f'<button class="on" data-f="*">{E(STR["all"][lang])}</button>' + "".join(f'<button data-f="{c}">{E(L(n, lang))}</button>' for c, n in CATS) + \
           f'<button data-f="vis">{E(STR["vision_title"][lang])}</button>'
    cards, bare = [], []
    for e in EQ:
        name = e[3] if lang == "en" else e[4] if lang == "vi" else e[2]
        cat = dict(CATS)[e[0]]
        ph = img("eq/" + e[1], lang, name) if e[1] else f'<div class="noph">{ico(CAT_ICO[e[0]])}<span>{E(STR["noph"][lang])}</span></div>'
        (cards if e[1] else bare).append(f'<div class="eq" data-c="{e[0]}"><div class="eqi">{ph}</div><div class="eqt"><span class="kick sm">{E(L(cat, lang))}</span><h3>{E(name)}</h3></div></div>')
    vis = [("vision-hot-stamp-defect.jpg", {"en": "Hot-stamping defect detection", "vi": "Phát hiện lỗi ép nhũ", "zh": "烫金瑕疵检测"}),
           ("vision-laser-marking.jpg", {"en": "Vision-guided laser marking", "vi": "Khắc laser định vị bằng camera", "zh": "视觉定位激光打标"}),
           ("vision-assembly.jpg", {"en": "Vision-guided assembly", "vi": "Lắp ráp định vị bằng camera", "zh": "视觉定位组装"}),
           ("vision-screwdriving.jpg", {"en": "Vision-guided screw-driving", "vi": "Bắt vít định vị bằng camera", "zh": "视觉定位打螺丝"}),
           ("vision-glue-inspection.jpg", {"en": "Glue bead inspection", "vi": "Kiểm tra đường keo", "zh": "喷胶外观检测"}),
           ("vision-sorting.jpg", {"en": "Multi-material sorting", "vi": "Phân loại nhiều loại vật liệu", "zh": "多物料分选"})]
    for f, t in vis:
        cards.append(f'<div class="eq" data-c="vis"><div class="eqi">{img("eq/" + f, lang, L(t, lang))}</div><div class="eqt"><span class="kick sm">{E(STR["vision_title"][lang])}</span><h3>{E(L(t, lang))}</h3></div></div>')
    cards += bare  # machines with photos first, so the grid opens strong
    return (pagehead(L(PAGE_TITLES["equipment"], lang), STR["eq_sub"][lang], lang, "eq/toothbrush-assembly-test-line.jpg") +
            f'<section class="sec"><div class="wrap"><div class="filters">{filt}</div><div class="eqgrid">{"".join(cards)}</div></div></section>')


def body_projects(lang, single=False):
    out = [pagehead(L(PAGE_TITLES["projects"], lang), STR["prj_sub"][lang], lang, "eq/ptc-line-a.jpg")]
    for n, p in enumerate(PROJECTS):
        pics = "".join(img(i, lang, L(p["t"], lang)) for i in p["imgs"])
        lis = "".join(f"<li>{E(x)}</li>" for x in L(p["d"], lang))
        out.append(f'<section class="prj{" rev" if n % 2 else ""}"><div class="wrap prjin"><div class="pics n{len(p["imgs"])} rv">{pics}</div>'
                   f'<div class="prjt rv"><span class="kick">{E(L(p["ind"], lang))}</span><h2>{E(L(p["t"], lang))}</h2><ul class="chk">{lis}</ul></div></div></section>')
    return "".join(out)


def body_innovation(lang, single=False):
    creds = "".join(f'<div class="cred rv"><div class="credi">{ico("badge" if k != 3 else "patent")}</div><h3>{E(L(t, lang))}</h3><p>{E(L(d, lang))}</p></div>'
                    for k, (t, d) in enumerate(CREDS))
    caps = "".join(f'<div class="cap rv"><div class="capi">{ico(k)}</div><span class="num">0{n+1}</span><h3>{E(L(t, lang))}</h3><p>{E(L(d, lang))}</p></div>' for n, (k, t, d) in enumerate(CAPS))
    c = PAT_COLS[lang]
    rows = "".join(f'<tr><td class="mono">{no}</td><td>{E(L(t, lang))}</td><td>{E(L(PAT_TYPE[ty], lang))}</td>'
                   f'<td><span class="st-{stt}">{E(L(PAT_STATUS[stt], lang))}</span></td></tr>' for no, ty, stt, t in PATENTS)
    return (pagehead(L(PAGE_TITLES["innovation"], lang), INNOV_SUB[lang], lang, "eq/vision-laser-marking.jpg") +
            f'<section class="sec"><div class="wrap"><div class="shead rv"><span class="kick">{E(STR["k_creds"][lang])}</span><h2>{E(CREDS_H[lang])}</h2></div><div class="creds">{creds}</div></div></section>'
            f'<section class="sec alt"><div class="wrap"><div class="shead rv"><span class="kick">{E(CAPS_H[lang])}</span><h2>{E(CAPS_SUB[lang])}</h2></div><div class="caps">{caps}</div></div></section>'
            f'<section class="sec"><div class="wrap"><div class="shead rv"><span class="kick">{E(STR["k_pat"][lang])}</span><h2>{E(PATENTS_H[lang])}</h2></div>'
            f'<div class="tbl rv"><table><tr><th>{c[0]}</th><th>{c[1]}</th><th>{c[2]}</th><th>{c[3]}</th></tr>{rows}</table></div></div></section>')


def body_about(lang, single=False):
    paras = "".join(f"<p>{E(x)}</p>" for x in ABOUT["p"][lang])
    vals = "".join(f'<div class="val rv"><b>{k+1:02d}</b><h3>{E(a)}</h3><p>{E(b)}</p></div>' for k, (a, b) in enumerate(ABOUT["values"][lang]))
    tl = "".join(f'<div class="tl rv"><b>{y}</b><p>{E(L(t, lang))}</p></div>' for y, t in TIMELINE)
    gal = "".join(img(f"site/{g}.jpg", lang, "") for g in ["factory-entrance", "workshop-1", "workshop-2", "design-office", "office", "honour-wall"])
    stats = "".join(f'<div><b>{E(a)}</b><span>{E(b)}</span></div>' for a, b in T["stats"][lang])
    return (pagehead(L(ABOUT["h"], lang), "", lang, "site/factory-entrance.jpg") +
            f'<section class="sec"><div class="wrap about"><div class="rv">{paras}</div><div class="abimg rv">{img("site/honour-wall.jpg", lang, "")}</div></div>'
            f'<div class="wrap"><div class="kpis dark">{stats}</div></div></section>'
            f'<section class="sec alt"><div class="wrap"><div class="shead rv"><span class="kick">{E(STR["k_tl"][lang])}</span><h2>{E(TIMELINE_H[lang])}</h2></div><div class="tline">{tl}</div></div></section>'
            f'<section class="sec"><div class="wrap"><div class="shead rv"><span class="kick">{E(STR["k_why"][lang])}</span><h2>{E(STR["why_h"][lang])}</h2></div><div class="vals">{vals}</div></div></section>'
            f'<section class="sec alt"><div class="wrap"><div class="shead rv"><span class="kick">{E(STR["k_plant"][lang])}</span><h2>{E(STR["plant_h"][lang])}</h2></div><div class="gallery">{gal}</div></div></section>')


def body_contact(lang, single=False):
    f = CONTACT["fields"][lang]; cc = STR["contact_cards"][lang]
    faq = "".join(f"<details><summary>{E(q)}</summary><p>{E(a)}</p></details>" for q, a in FAQ[lang])
    form = (f'<form class="rfq" onsubmit="var d=new FormData(this),b=[];d.forEach(function(v,k){{b.push(k+\': \'+v)}});'
            f'location.href=\'mailto:{EMAIL}?subject=\'+encodeURIComponent(\'RFQ – \'+(d.get(\'{E(f[0])}\')||\'\'))+\'&body=\'+encodeURIComponent(b.join(\'\\n\'));return false;">'
            f'<label>{E(f[0])}<input name="{E(f[0])}" required></label><label>{E(f[1])}<input name="{E(f[1])}"></label>'
            f'<label>{E(f[2])}<input name="{E(f[2])}" required></label><label>{E(f[3])}<input name="{E(f[3])}" required></label>'
            f'<label class="full">{E(f[4])}<textarea name="{E(f[4])}" rows="5"></textarea></label><button class="btn lg full" type="submit">{E(f[5])}{ico("arrow")}</button></form>')
    cards = (f'<div class="cc">{ico("mail")}<h4>{E(cc[0])}</h4><a href="mailto:{EMAIL}">{EMAIL}</a></div>'
             f'<div class="cc">{ico("phone")}<h4>{E(cc[1])}</h4><a href="tel:{PHONE_TEL}">{PHONE}</a></div>'
             f'<div class="cc">{ico("globe")}<h4>{E(cc[2])}</h4><p>{E(CONTACT["addr"][lang])}</p></div>')
    return (pagehead(L(CONTACT["h"], lang), L(CONTACT["sub"], lang), lang, "site/design-office.jpg") +
            f'<section class="sec"><div class="wrap contact"><div class="formbox rv">{form}</div><div class="ccs rv">{cards}</div></div></section>'
            f'<section class="sec alt"><div class="wrap narrow"><div class="shead rv"><span class="kick">FAQ</span><h2>{E(STR["faq_h"][lang])}</h2></div><div class="faq">{faq}</div></div></section>')


BODY = {"index": body_index, "solutions": body_solutions, "equipment": body_equipment, "projects": body_projects,
        "innovation": body_innovation, "about": body_about, "contact": body_contact}


def js(lang, inline=False):
    code = (ROOT / "assets/js/site.js").read_text()
    return f"<script>{code}</script>" if inline else f'<script src="{pre(lang)}assets/js/site.js" defer></script>'


def build_site():
    for lang in LANGS:
        d = ROOT if lang == "en" else ROOT / lang
        d.mkdir(exist_ok=True)
        for page in PAGES:
            out = head(page, lang) + header(page, lang) + "<main>" + BODY[page](lang) + "</main>" + footer(lang) + js(lang) + "</body></html>"
            (d / f"{page}.html").write_text(out, encoding="utf-8")
    print("site pages:", len(LANGS) * len(PAGES))


def build_previews():
    out = ROOT / "preview"; out.mkdir(exist_ok=True)
    cache = {}
    def inline(m):
        rel = m.group(2)
        if rel not in cache:
            cache[rel] = "data:image/jpeg;base64," + base64.b64encode((ROOT / "assets" / "img" / rel).read_bytes()).decode()
        return m.group(1) + cache[rel]
    for lang in LANGS:
        parts = [head("index", lang, inline=True), header("index", lang, single=True), "<main>"]
        for page in PAGES:
            parts.append(f'<div id="{page}" class="anchor"></div>' + BODY[page](lang, single=True))
        parts.append("</main>" + footer(lang, single=True) + js(lang, inline=True) + "</body></html>")
        s = "".join(parts)
        s = re.sub(r'((?:src="|href="|url\())(?:\.\./)?(?:assets/)?img/([^")]+)', inline, s)
        (out / f"longteng_preview_{lang}.html").write_text(s, encoding="utf-8")
    print("previews written")


if __name__ == "__main__":
    build_site()
    build_previews()
