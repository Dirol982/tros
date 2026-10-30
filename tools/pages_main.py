"""Главная страница."""
from layout import (ICON_CALC, ICON_CHAT, ICON_PHONE, MAIN, VIBER, cta_band, faq_html, faq_schema,
                    order_form)
from svg import cable_hero, cable_interactive

FAQ = [
    ("Зачем ремонтировать трос, если можно купить новый?",
     "Восстановленный трос — это ваша же деталь, поэтому он гарантированно подходит по длине, креплениям и ходу. "
     "Новый трос часто приходится заказывать по предоплате и ждать 2–3 недели, а б/у может отказать через короткое время. "
     "После ремонта у троса около 90% ресурса нового, а гарантия — 12 месяцев."),
    ("Сколько времени занимает ремонт?",
     "Любой заказ выполняем не дольше 24 часов с момента, как трос или кулиса попали к нам."),
    ("Действует ли гарантия, если трос ставлю не у вас?",
     "Да. Гарантия 12 месяцев не зависит от того, где установлена деталь: на сертифицированной СТО или в гараже. "
     "Важно лишь, чтобы трос не повредили при установке."),
    ("Я живу не в Минске. Как отдать трос в ремонт?",
     "Передайте трос или кулису поездом, маршруткой или почтой. Мы восстановим деталь и отправим обратно тем же способом."),
    ("С какими машинами вы работаете?",
     "С легковыми автомобилями любых марок, автобусами и спецтехникой. Ремонтируем также тросы катеров и лодок."),
    ("Можно приехать без записи?",
     "Лучше позвоните заранее: менеджер согласует время приёма, и мастер будет на месте."),
]

ANATOMY = [
    ("core", "Порван сердечник", "Ставим новый сердечник и выдерживаем точную длину троса."),
    ("sheath", "Изношена оплётка", "Меняем наружную оплётку на новую той же длины, ход троса возвращается."),
    ("drive", "Разбиты детали привода", "Детали с демпфированием делаем из износостойкого материала под фактические размеры."),
    ("boot", "Порван пыльник", "Ставим гофрированный пыльник из масло-бензостойкой резины."),
    ("guide", "Сломана направляющая", "Пластиковые направляющие меняем на металлические, чтобы трос не оборвали при следующем снятии."),
]


def anatomy_block(title="Что ломается в тросе и как мы это чиним", eyebrow="Устройство троса"):
    cards = "".join(
        f'<button type="button" class="fault" data-part="{k}" aria-pressed="false"><span class="num">{i}</span>'
        f'<h3>{t}</h3><p>{d}</p></button>' for i, (k, t, d) in enumerate(ANATOMY, 1))
    return f"""<section class="section" aria-labelledby="anat-t"><div class="wrap">
  <div class="section-head"><p class="eyebrow"><b>●</b> {eyebrow}</p><h2 id="anat-t">{title}</h2>
  <p class="lead">Нажмите на номер на схеме или на карточку. Мы меняем только изношенный узел, остальное остаётся родным.</p></div>
  <div class="anatomy">
    <figure class="drawing" style="margin:0">{cable_interactive([k for k, _, _ in ANATOMY])}
      <figcaption><span>Трос КПП · схема</span><span>5 типовых неисправностей</span></figcaption></figure>
    <div class="faults">{cards}</div>
  </div>
</div></section>"""


def specs_strip():
    items = [
        ("Срок", "24", "ч", "максимум на любой заказ"),
        ("Гарантия", "12", "мес", "где бы ни ставили трос"),
        ("Ресурс", "90", "%", "от нового изделия"),
        ("Посадка", "100", "%", "это ваша же деталь"),
        ("Опыт", "2010", "", "работаем с этого года"),
    ]
    return '<div class="specs">' + "".join(
        f'<div class="spec"><span class="key">{k}</span><span class="val">{v}<sub>{u}</sub></span><p>{d}</p></div>'
        for k, v, u, d in items) + "</div>"


def index():
    page = {
        "slug": "index.html",
        "title": "Ремонт тросов КПП и кулис в Минске за 24 часа — ТехноЛекарь",
        "description": "Восстанавливаем тросы КПП, кулисы, тросы ручника и электронного стояночного тормоза. Срок до 24 часов, гарантия 12 месяцев, приём со всей Беларуси. С 2010 года. ☎ +375 29 508-78-33",
        "schema": [faq_schema(FAQ)],
    }
    body = f"""
<section class="hero blueprint"><div class="wrap hero-grid">
  <div class="hero-copy">
    <p class="eyebrow"><b>●</b> Минск · вся Беларусь · с 2010 года</p>
    <h1>Ремонт тросов КПП и кулис <span class="accent">за 24 часа</span></h1>
    <p class="lead">Восстанавливаем ваш трос или кулису вместо покупки новых. Деталь гарантированно подойдёт, получит около 90% ресурса нового и гарантию 12 месяцев.</p>
    <div class="hero-actions">
      <a class="btn btn-primary" href="#order">{ICON_CALC} Рассчитать стоимость</a>
      <a class="btn btn-ghost" href="tel:{MAIN['tel']}">{ICON_PHONE} {MAIN['text']}</a>
    </div>
    <p class="hero-note"><i class="dot" aria-hidden="true"></i>Работаем без выходных, 8:00–20:00. Из регионов принимаем поездом, маршруткой и почтой.</p>
  </div>
  <figure class="drawing" style="margin:0">{cable_hero()}
    <figcaption><span>Изделие: трос КПП</span><span>Работа: восстановление · ≤ 24 ч</span></figcaption></figure>
</div>
<div class="wrap" style="margin-top:clamp(28px,4vw,48px)">{specs_strip()}</div>
</section>

<section class="section" aria-labelledby="why-t"><div class="wrap">
  <div class="section-head"><p class="eyebrow"><b>●</b> Почему ремонт</p>
  <h2 id="why-t">Трос порвался. Что выгоднее: новый, б/у или ремонт?</h2>
  <p class="lead">Клиенты часто приходят к нам после того, как заказанный трос не подошёл. Сравните три варианта до того, как платить.</p></div>
  <div class="table-scroll"><table class="compare">
    <thead><tr><th scope="col">Критерий</th><th scope="col">Новый под заказ</th><th scope="col">Б/у с разборки</th><th scope="col" class="us">Ремонт в ТехноЛекарь</th></tr></thead>
    <tbody>
      <tr><th scope="row">Подойдёт ли к машине</th><td><span class="mark bad">Бывает, что нет: ошибка в каталоге или модификации</span></td><td><span class="mark bad">Нужно угадать с модификацией</span></td><td class="us"><span class="mark good">Да, это ваша деталь</span></td></tr>
      <tr><th scope="row">Срок</th><td><span class="mark bad">Часто 2–3 недели по предоплате</span></td><td><span class="mark good">Быстро, если найдётся</span></td><td class="us"><span class="mark good">До 24 часов</span></td></tr>
      <tr><th scope="row">Ресурс</th><td><span class="mark good">100%</span></td><td><span class="mark bad">Неизвестен, может отказать быстро</span></td><td class="us"><span class="mark good">Около 90% от нового</span></td></tr>
      <tr><th scope="row">Гарантия</th><td><span class="mark good">По условиям продавца</span></td><td><span class="mark bad">Обычно нет</span></td><td class="us"><span class="mark good">12 месяцев</span></td></tr>
      <tr><th scope="row">Редкие и снятые с производства</th><td><span class="mark bad">Может не быть в продаже</span></td><td><span class="mark bad">Как повезёт</span></td><td class="us"><span class="mark good">Восстановим или изготовим по размерам</span></td></tr>
    </tbody>
  </table></div>
</div></section>

<section class="section band" aria-labelledby="svc-t"><div class="wrap">
  <div class="section-head"><p class="eyebrow"><b>●</b> Услуги</p><h2 id="svc-t">Ремонтируем любые тросы управления и кулисы</h2>
  <p class="lead">Любые марки легковых авто, автобусы, спецтехника, катера и лодки.</p></div>
  <div class="services">
    <a class="svc feature wide" href="remont-trosov.html"><span class="code">Основная услуга</span><h3>Ремонт тросов КПП</h3>
      <p>Замена сердечника и оплётки, новые пыльники, металлические направляющие. Длина и ход как у родного троса.</p><span class="more">Подробнее о ремонте тросов</span></a>
    <a class="svc wide" href="remont-kulis.html"><span class="code">МКПП</span><h3>Ремонт кулис</h3>
      <p>Убираем люфт рычага, восстанавливаем корпус и блок задней передачи, меняем элементы трения и смазку.</p><span class="more">Подробнее о кулисах</span></a>
    <a class="svc" href="remont-trosov.html#types"><span class="code">Тормоз</span><h3>Тросы ручника и ЭСТ</h3>
      <p>Тросы стояночного тормоза, в том числе электронного.</p><span class="more">Подробнее</span></a>
    <a class="svc" href="remont-trosov.html#types"><span class="code">Кузов</span><h3>Капот, двери, багажник</h3>
      <p>Тросы замков и приводов, трапеции стеклоочистителей.</p><span class="more">Подробнее</span></a>
    <a class="svc" href="izgotovlenie-trosov.html"><span class="code">Под заказ</span><h3>Новые тросы по размерам</h3>
      <p>Изготовим трос, если старого нет или его не восстановить.</p><span class="more">Как заказать</span></a>
  </div>
  <div class="tags" style="margin-top:20px"><span class="tag">Легковые авто</span><span class="tag">Автобусы</span><span class="tag">Спецтехника</span><span class="tag">Катера и лодки</span><span class="tag">МКПП и АКПП</span></div>
</div></section>

{anatomy_block()}

<section class="section band-ink" aria-labelledby="how-t"><div class="wrap">
  <div class="section-head"><p class="eyebrow"><b>●</b> Как мы работаем</p><h2 id="how-t">Четыре шага от звонка до исправной КПП</h2></div>
  <ol class="steps">
    <li><h3>Свяжитесь с нами</h3><p>Позвоните или оставьте заявку с фото. Назовём стоимость и согласуем время приёма.</p></li>
    <li><h3>Передайте деталь</h3><p>Привезите в Минск или отправьте поездом, маршруткой, почтой из любого города.</p></li>
    <li><h3>Ремонт до 24 часов</h3><p>Меняем изношенные узлы, проверяем ход и чёткость работы.</p></li>
    <li><h3>Получите обратно</h3><p>Забираете деталь лично или получаете тем же транспортом. Гарантия 12 месяцев.</p></li>
  </ol>
</div></section>

<section class="section" aria-labelledby="reg-t"><div class="wrap split">
  <div class="prose"><p class="eyebrow"><b>●</b> Вся Беларусь</p><h2 id="reg-t">Не в Минске? Отправьте трос, мы вернём его исправным</h2>
  <p class="lead">Снимать машину с ходу на недели не нужно. Трос едет к нам и обратно, а сам ремонт занимает не больше 24 часов.</p>
  <a class="btn btn-ghost" href="po-belarusi.html" style="justify-self:start">Как отправить из региона</a></div>
  <div class="regions">
    <div class="region"><b>Брест</b><span>поезд · маршрутка · почта</span></div>
    <div class="region"><b>Витебск</b><span>поезд · маршрутка · почта</span></div>
    <div class="region"><b>Гомель</b><span>поезд · маршрутка · почта</span></div>
    <div class="region"><b>Гродно</b><span>поезд · маршрутка · почта</span></div>
    <div class="region"><b>Могилёв</b><span>поезд · маршрутка · почта</span></div>
    <div class="region"><b>Минская обл.</b><span>лично или почтой</span></div>
  </div>
</div></section>

<section class="section band" aria-labelledby="faq-t"><div class="wrap split">
  <div class="prose"><p class="eyebrow"><b>●</b> Вопросы</p><h2 id="faq-t">Частые вопросы о ремонте тросов</h2>
  <p class="muted">Не нашли ответ? Спросите мастера в Viber, он ответит в рабочее время.</p>
  <a class="btn btn-ghost" href="{VIBER}" style="justify-self:start">{ICON_CHAT} Написать в Viber</a></div>
  {faq_html(FAQ)}
</div></section>

<section class="section" aria-labelledby="know-t"><div class="wrap">
  <div class="section-head"><p class="eyebrow"><b>●</b> Полезно знать</p><h2 id="know-t">Проверьте трос сами, прежде чем ехать на СТО</h2></div>
  <div class="services">
    <a class="svc wide" href="diagnostika.html"><span class="code">6 шагов</span><h3>Диагностика троса и кулисы</h3><p>Как по поведению рычага понять, что неисправно: трос, кулиса или механизм на коробке.</p><span class="more">Читать инструкцию</span></a>
    <a class="svc wide" href="remont-trosov.html#faults"><span class="code">5 поломок</span><h3>Неисправности тросов</h3><p>Обрыв сердечника, износ оплётки, разбитые наконечники и что с этим делать.</p><span class="more">Смотреть</span></a>
  </div>
</div></section>

{order_form()}"""
    return page, body
