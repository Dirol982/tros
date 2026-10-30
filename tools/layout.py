"""Общий каркас страниц: <head> с SEO-разметкой, шапка, подвал, форма заявки."""
import json

from svg import FAVICON, LOGO

SITE = "https://www.tros-kpp.by"
COMPANY = "ТехноЛекарь"
LEGAL = "ЧПУП «ТехноЛекарь»"
UNP = "192610719"
ADDRESS = "г. Минск, ул. Щербакова, 5"
ADDRESS_FULL = "г. Минск, ул. Щербакова, 5, кв. 24"
HOURS = "Без выходных, 8:00–20:00"
MAP_URL = "https://yandex.by/maps/?text=%D0%9C%D0%B8%D0%BD%D1%81%D0%BA%2C%20%D1%83%D0%BB.%20%D0%A9%D0%B5%D1%80%D0%B1%D0%B0%D0%BA%D0%BE%D0%B2%D0%B0%2C%205"

# Номера взяты с текущего сайта; оператор velcom с 2019 года называется A1.
PHONES = [
    {"op": "МТС", "text": "+375 29 508-78-33", "tel": "+375295087833", "note": "основной"},
    {"op": "life", "text": "+375 25 976-91-92", "tel": "+375259769192", "note": "Viber"},
    {"op": "A1", "text": "+375 44 456-62-99", "tel": "+375444566299", "note": ""},
    {"op": "A1", "text": "+375 44 588-66-13", "tel": "+375445886613", "note": ""},
]
MAIN = PHONES[0]
VIBER = "viber://chat?number=%2B375259769192"

NAV = [
    ("index.html", "Главная"),
    ("remont-trosov.html", "Ремонт тросов"),
    ("remont-kulis.html", "Ремонт кулис"),
    ("izgotovlenie-trosov.html", "Изготовление"),
    ("diagnostika.html", "Диагностика"),
    ("po-belarusi.html", "По Беларуси"),
    ("kontakty.html", "Контакты"),
]

ICON_PHONE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/></svg>'
ICON_CHAT = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/></svg>'
ICON_CALC = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="5" y="3" width="14" height="18" rx="2"/><path d="M8 7h8M8 12h2m4 0h2M8 16h2m4 0h2"/></svg>'

FONTS = "https://fonts.googleapis.com/css2?family=Golos+Text:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&family=Unbounded:wght@500;600;700&display=swap"

ORG = {
    "@type": "AutoRepair",
    "@id": SITE + "/#org",
    "name": f"{COMPANY} — ремонт тросов и кулис",
    "legalName": "Частное производственное унитарное предприятие «ТехноЛекарь»",
    "taxID": UNP,
    "url": SITE + "/",
    "telephone": [p["tel"] for p in PHONES],
    "foundingDate": "2010",
    "priceRange": "$$",
    "address": {"@type": "PostalAddress", "streetAddress": "ул. Щербакова, 5", "addressLocality": "Минск", "addressCountry": "BY"},
    "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
                                   "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
                                   "opens": "08:00", "closes": "20:00"}],
    "areaServed": {"@type": "Country", "name": "Беларусь"},
    "knowsAbout": ["ремонт тросов КПП", "ремонт кулисы КПП", "ремонт троса ручника", "ремонт троса электронного стояночного тормоза", "изготовление тросов по размерам"],
}


def head(page, *, artifact=False):
    """page: dict(slug, title, description, h1, crumbs, schema=[...])."""
    url = SITE + "/" + ("" if page["slug"] == "index.html" else page["slug"])
    graph = [ORG] + page.get("schema", [])
    if page.get("crumbs"):
        items = [{"@type": "ListItem", "position": 1, "name": "Главная", "item": SITE + "/"}]
        items.append({"@type": "ListItem", "position": 2, "name": page["crumbs"], "item": url})
        graph.append({"@type": "BreadcrumbList", "itemListElement": items})
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1)
    meta = f"""<title>{page['title']}</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="{page['description']}">
<link rel="canonical" href="{url}">
<meta name="robots" content="{page.get('robots', 'index, follow')}">
<meta name="theme-color" content="#141b22">
<meta property="og:type" content="website">
<meta property="og:locale" content="ru_BY">
<meta property="og:site_name" content="{COMPANY}">
<meta property="og:title" content="{page['title']}">
<meta property="og:description" content="{page['description']}">
<meta property="og:url" content="{url}">
<link rel="icon" href="{FAVICON}" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="assets/styles.css">
<script type="application/ld+json">
{ld}
</script>"""
    if artifact:
        return meta
    return f"""<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
{meta}
</head>
<body>"""


def header(slug):
    cur = ' aria-current="page"'
    links = "".join(f'<a href="{href}"{cur if href == slug else ""}>{name}</a>' for href, name in NAV[1:])
    return f"""<a class="skip" href="#main">Перейти к содержимому</a>
<div class="topbar"><div class="wrap">
  <span><i class="dot" aria-hidden="true"></i>{HOURS} · приём по записи</span>
  <span>Ремонт за 24 часа · гарантия 12 месяцев · вся Беларусь</span>
</div></div>
<header class="site-header"><div class="wrap">
  <a class="logo" href="index.html" aria-label="{COMPANY} — на главную">{LOGO}<span><strong>{COMPANY}</strong><small>тросы · кулисы · с 2010</small></span></a>
  <nav class="nav" id="nav" aria-label="Основное меню">{links}</nav>
  <a class="header-phone" href="tel:{MAIN['tel']}">{MAIN['text']}<small>{MAIN['op']} · звоните 8–20</small></a>
  <a class="btn btn-primary btn-sm header-cta" href="#order">Рассчитать ремонт</a>
  <button class="menu-btn" type="button" aria-controls="nav" aria-expanded="false" aria-label="Открыть меню">
    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
  </button>
</div></header>
<main id="main">"""


def phone_lines(copy=True):
    rows = []
    for p in PHONES:
        note = f'<span class="tagline">{p["note"]}</span>' if p["note"] else '<span class="tagline"></span>'
        btn = f'<button class="copy" type="button" data-copy="{p["text"]}">Копировать</button>' if copy else ""
        rows.append(f'<div class="contact-line"><span class="op">{p["op"]}</span>'
                    f'<span><a href="tel:{p["tel"]}">{p["text"]}</a> {note}</span>{btn}</div>')
    return '<div class="contact-lines">' + "".join(rows) + "</div>"


PARTS = [
    ("tros-kpp", "Трос КПП"),
    ("kulisa", "Кулиса"),
    ("ruchnik", "Ручник / ЭСТ"),
    ("kapot", "Капот, двери, багажник"),
    ("trapeciya", "Трапеция дворников"),
    ("drugoe", "Другое"),
]


def order_form(title="Узнайте стоимость ремонта", lead=None, uid="o"):
    lead = lead or ("Опишите поломку и модель авто. Мастер перезвонит, уточнит детали и назовёт цену. "
                    "Фото троса или кулисы помогает оценить работу точнее.")
    chips = "".join(
        f'<input type="radio" name="part" id="{uid}-{k}" value="{v}"{" checked" if i == 0 else ""}><label for="{uid}-{k}">{v}</label>'
        for i, (k, v) in enumerate(PARTS))
    return f"""<section class="section band-ink" id="order" aria-labelledby="{uid}-title"><div class="wrap order">
  <div class="prose">
    <p class="eyebrow"><b>●</b> Расчёт стоимости</p>
    <h2 id="{uid}-title">{title}</h2>
    <p class="lead">{lead}</p>
    {phone_lines(copy=False)}
    <p class="muted">{HOURS}. Перед визитом позвоните, чтобы согласовать время приёма.</p>
  </div>
  <form class="form" data-order novalidate>
    <div class="field full"><span class="label" id="{uid}-part-l">Что ремонтируем</span>
      <div class="chips" role="radiogroup" aria-labelledby="{uid}-part-l">{chips}</div></div>
    <div class="field"><label for="{uid}-car">Марка и модель</label>
      <input id="{uid}-car" name="car" autocomplete="off" placeholder="Например, Renault Megane II, 2006"></div>
    <div class="field"><label for="{uid}-phone">Телефон *</label>
      <input id="{uid}-phone" name="phone" type="tel" inputmode="tel" autocomplete="tel" required placeholder="+375 29 123-45-67"></div>
    <div class="field full"><label for="{uid}-msg">Что случилось</label>
      <textarea id="{uid}-msg" name="msg" placeholder="Передача включается с трудом, рычаг не возвращается в нейтраль…"></textarea></div>
    <div class="field full"><label class="file-drop" for="{uid}-photo">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M4 7h3l2-3h6l2 3h3v13H4z"/><circle cx="12" cy="13" r="4"/></svg>
      <span>Прикрепите 1–3 фото троса или кулисы</span>
      <input id="{uid}-photo" name="photo" type="file" accept="image/*" multiple></label></div>
    <div class="form-foot">
      <small>Нажимая кнопку, вы соглашаетесь на обработку телефона для обратного звонка.</small>
      <button class="btn btn-primary" type="submit">{ICON_CALC} Получить расчёт</button>
    </div>
    <p class="form-done" role="status" hidden></p>
  </form>
</div></section>"""


def footer():
    nav = "".join(f'<li><a href="{h}">{n}</a></li>' for h, n in NAV[1:])
    phones = "".join(f'<li><a href="tel:{p["tel"]}">{p["text"]}</a> <span class="muted">{p["op"]}</span></li>' for p in PHONES)
    return f"""</main>
<footer class="site-footer"><div class="wrap">
  <div class="cols">
    <div style="display:grid;gap:14px;align-content:start">
      <a class="logo" href="index.html">{LOGO}<span><strong>{COMPANY}</strong><small>тросы · кулисы · с 2010</small></span></a>
      <p style="opacity:.75">Ремонт и изготовление тросов управления и кулис КПП для легковых авто, автобусов, спецтехники, катеров и лодок.</p>
    </div>
    <div><h3>Услуги</h3><ul>{nav}<li><a href="izmeneniya.html">Что изменилось на сайте</a></li></ul></div>
    <div><h3>Телефоны</h3><ul>{phones}<li><a href="{VIBER}">Написать в Viber</a></li></ul></div>
    <div><h3>Приём</h3><ul><li>{ADDRESS_FULL}</li><li>{HOURS}</li><li>Приём по предварительной записи</li><li><a href="{MAP_URL}" rel="noopener" target="_blank">Открыть на Яндекс Картах</a></li></ul></div>
  </div>
  <div class="legal">
    <span>© 2010–<span id="year">2026</span> {LEGAL}, УНП {UNP}</span>
    <span>Ремонт тросов и кулис в Минске и по всей Беларуси</span>
  </div>
</div></footer>
<nav class="actionbar" aria-label="Быстрая связь">
  <a href="tel:{MAIN['tel']}">{ICON_PHONE} Звонок</a>
  <a href="{VIBER}">{ICON_CHAT} Viber</a>
  <a class="primary" href="#order">{ICON_CALC} Расчёт</a>
</nav>
<script src="assets/app.js" defer></script>"""


def page_head_block(crumb, eyebrow, h1, lead, facts=()):
    tags = "".join(f'<span class="tag">{f}</span>' for f in facts)
    return f"""<section class="page-head blueprint"><div class="wrap">
  <ol class="crumbs" aria-label="Хлебные крошки"><li><a href="index.html">Главная</a></li><li aria-current="page">{crumb}</li></ol>
  <p class="eyebrow">{eyebrow}</p>
  <h1>{h1}</h1>
  <p class="lead">{lead}</p>
  {'<div class="facts">' + tags + '</div>' if tags else ''}
</div></section>"""


def cta_band(title, text):
    return f"""<section class="band cta-band"><div class="wrap">
  <div class="prose"><h2>{title}</h2><p class="muted">{text}</p></div>
  <div class="hero-actions"><a class="btn btn-primary" href="#order">{ICON_CALC} Рассчитать ремонт</a>
  <a class="btn btn-ghost" href="tel:{MAIN['tel']}">{ICON_PHONE} {MAIN['text']}</a></div>
</div></section>"""


def faq_schema(qa):
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qa]}


def faq_html(qa):
    return '<div class="faq">' + "".join(
        f"<details><summary>{q}</summary><div><p>{a}</p></div></details>" for q, a in qa) + "</div>"


def service_schema(name, desc):
    return {"@type": "Service", "name": name, "description": desc, "provider": {"@id": SITE + "/#org"},
            "areaServed": {"@type": "Country", "name": "Беларусь"}}
