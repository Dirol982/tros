"""Технические чертежи для сайта: трос КПП и кулиса.

Все цвета берутся из CSS-токенов через классы svg-*, поэтому чертежи
одинаково читаются в светлой и тёмной теме.
"""

# Точки, к которым привязаны выноски на тросе (viewBox 640×360)
CABLE_POINTS = {
    "core": (560, 110),      # сердечник (виден на штоке)
    "sheath": (318, 178),    # наружная оплётка
    "drive": (36, 250),      # деталь привода / наконечник
    "boot": (118, 250),      # гофрированный пыльник
    "guide": (474, 110),     # направляющая / крепление к кронштейну
}


def _boot(x0, x1, y, h=12, n=6):
    step = (x1 - x0) / (n * 2)
    top = " ".join(f"{x0 + i * step:.1f},{y - (h if i % 2 == 0 else h - 5):.1f}" for i in range(n * 2 + 1))
    bot = " ".join(f"{x0 + i * step:.1f},{y + (h if i % 2 == 0 else h - 5):.1f}" for i in range(n * 2 + 1))
    return (f'<polyline points="{top}" class="svg-ink" fill="none" stroke-width="2" stroke-linejoin="round"/>'
            f'<polyline points="{bot}" class="svg-ink" fill="none" stroke-width="2" stroke-linejoin="round"/>'
            f'<line x1="{x0}" y1="{y - h}" x2="{x0}" y2="{y + h}" class="svg-ink" stroke-width="2"/>'
            f'<line x1="{x1}" y1="{y - h}" x2="{x1}" y2="{y + h}" class="svg-ink" stroke-width="2"/>')


def cable_body():
    s = []
    # сетка-подложка чертежа
    s.append('<defs><pattern id="g" width="20" height="20" patternUnits="userSpaceOnUse">'
             '<path d="M20 0H0V20" fill="none" class="svg-muted" stroke-width=".4" opacity=".35"/></pattern></defs>')
    s.append('<rect x="0" y="0" width="640" height="360" fill="url(#g)"/>')
    # оплётка: широкая линия + внутренняя светлая, создаёт объём
    d = "M170 250 C 300 250, 330 110, 460 110"
    s.append(f'<path d="{d}" class="svg-accent draw-in" stroke-width="16" fill="none" stroke-linecap="butt"/>')
    s.append(f'<path d="{d}" class="svg-surface-fill" stroke="currentColor" style="stroke:var(--surface)" stroke-width="3" fill="none" stroke-dasharray="2 9" opacity=".7"/>')
    # левый конец: проушина, шток, пыльник, втулка
    s.append('<circle cx="36" cy="250" r="14" class="svg-ink svg-surface-fill" stroke-width="3"/>')
    s.append('<circle cx="36" cy="250" r="5" class="svg-ink-fill"/>')
    s.append('<rect x="50" y="246" width="48" height="8" rx="2" class="svg-ink-fill"/>')
    s.append(_boot(96, 140, 250))
    s.append('<rect x="140" y="240" width="32" height="20" rx="3" class="svg-ink-fill"/>')
    # правый конец: втулка с кронштейном, пыльник, шток, шаровой наконечник
    s.append('<rect x="458" y="100" width="34" height="20" rx="3" class="svg-ink-fill"/>')
    s.append('<rect x="468" y="82" width="12" height="56" rx="2" class="svg-ink svg-surface2-fill" stroke-width="2.5"/>')
    s.append(_boot(492, 536, 110))
    s.append('<rect x="536" y="106" width="44" height="8" rx="2" class="svg-ink-fill"/>')
    s.append('<rect x="578" y="98" width="26" height="24" rx="5" class="svg-ink svg-surface-fill" stroke-width="3"/>')
    s.append('<circle cx="591" cy="110" r="5" class="svg-ink-fill"/>')
    # размерная линия
    s.append('<g class="svg-muted" stroke-width="1">'
             '<line x1="22" y1="318" x2="604" y2="318"/><line x1="22" y1="306" x2="22" y2="330"/>'
             '<line x1="604" y1="306" x2="604" y2="330"/></g>')
    s.append('<path d="M22 318l10 -4v8z M604 318l-10 -4v8z" class="svg-muted-fill"/>')
    s.append('<rect x="214" y="308" width="200" height="20" class="svg-surface-fill"/>')
    s.append('<text x="314" y="322" text-anchor="middle" class="svg-text-muted">L = длина вашего троса</text>')
    return "".join(s)


def cable_hero():
    """Чертёж с подписями для первого экрана."""
    labels = [
        # (точка, текст, позиция подписи, якорь)
        ("core", "сердечник", (560, 52), "middle"),
        ("guide", "направляющая", (452, 52), "end"),
        ("sheath", "оплётка", (300, 140), "end"),
        ("boot", "пыльник", (118, 296), "middle"),
        ("drive", "наконечник", (36, 200), "start"),
    ]
    s = [cable_body()]
    for key, text, (tx, ty), anchor in labels:
        px, py = CABLE_POINTS[key]
        ly = ty + 6 if ty < py else ty - 16
        s.append(f'<line x1="{px}" y1="{py}" x2="{tx}" y2="{ly}" class="svg-ink" stroke-width="1"/>')
        s.append(f'<circle cx="{px}" cy="{py}" r="3.5" class="svg-accent-fill"/>')
        s.append(f'<text x="{tx}" y="{ty}" text-anchor="{anchor}" class="svg-text">{text}</text>')
    return ('<svg viewBox="0 0 640 360" role="img" aria-labelledby="hero-svg-t">'
            '<title id="hero-svg-t">Схема троса КПП: наконечник, пыльник, оплётка, направляющая, сердечник</title>'
            + "".join(s) + "</svg>")


def cable_interactive(order):
    """Чертёж с номерами-кнопками; order — список ключей деталей по номерам."""
    offsets = {"core": (0, -48), "sheath": (0, -46), "drive": (0, -50), "boot": (0, 44), "guide": (-44, -40)}
    s = [cable_body()]
    for i, key in enumerate(order, 1):
        px, py = CABLE_POINTS[key]
        dx, dy = offsets[key]
        cx, cy = px + dx, py + dy
        s.append(f'<line x1="{px}" y1="{py}" x2="{cx}" y2="{cy}" class="svg-ink" stroke-width="1"/>')
        s.append(f'<circle cx="{px}" cy="{py}" r="3.5" class="svg-accent-fill"/>')
        s.append(f'<g class="hotspot" data-part="{key}" tabindex="0" role="button" aria-label="Деталь {i}">'
                 f'<circle class="ring svg-ink svg-surface-fill" cx="{cx}" cy="{cy}" r="15" stroke-width="2"/>'
                 f'<text x="{cx}" y="{cy + 4.5}" text-anchor="middle" class="svg-text" style="font-weight:600">{i}</text></g>')
    return ('<svg viewBox="0 0 640 360" role="img" aria-label="Интерактивная схема троса КПП">'
            + "".join(s) + "</svg>")


KULISA_POINTS = {
    "friction": (150, 262),
    "bushing": (320, 236),
    "body": (470, 286),
    "grease": (348, 250),
    "reverse": (320, 150),
}


def kulisa_interactive(order):
    s = ['<defs><pattern id="g2" width="20" height="20" patternUnits="userSpaceOnUse">'
         '<path d="M20 0H0V20" fill="none" class="svg-muted" stroke-width=".4" opacity=".35"/></pattern></defs>'
         '<rect x="0" y="0" width="640" height="360" fill="url(#g2)"/>']
    # корпус
    s.append('<path d="M120 300 L150 250 H490 L520 300 Z" class="svg-ink svg-surface2-fill" stroke-width="3" stroke-linejoin="round"/>')
    s.append('<rect x="108" y="300" width="424" height="14" rx="3" class="svg-ink-fill"/>')
    # элементы трения (накладки)
    s.append('<rect x="140" y="256" width="22" height="14" rx="3" class="svg-accent-fill"/>')
    s.append('<rect x="478" y="256" width="22" height="14" rx="3" class="svg-accent-fill"/>')
    # трещина в корпусе
    s.append('<path d="M462 270 l8 8 -6 6 9 10" class="svg-accent" fill="none" stroke-width="2"/>')
    # шар и опорная втулка
    s.append('<path d="M290 246 A32 32 0 0 1 350 246" class="svg-ink" fill="none" stroke-width="7" stroke-linecap="round"/>')
    s.append('<circle cx="320" cy="236" r="20" class="svg-ink svg-surface-fill" stroke-width="3"/>')
    # рычаг
    s.append('<rect x="313" y="76" width="14" height="150" rx="5" class="svg-ink-fill"/>')
    # блок задней передачи (кольцо на рычаге)
    s.append('<rect x="300" y="140" width="40" height="22" rx="5" class="svg-ink svg-surface-fill" stroke-width="3"/>')
    # рукоятка
    s.append('<rect x="282" y="34" width="76" height="52" rx="22" class="svg-ink svg-surface-fill" stroke-width="3"/>')
    s.append('<text x="320" y="66" text-anchor="middle" class="svg-text-muted">R 1 3 5</text>')
    # выходы тросов
    s.append('<path d="M500 280 C 560 280, 570 220, 630 220" class="svg-accent" stroke-width="9" fill="none"/>')
    s.append('<path d="M506 292 C 570 292, 580 250, 630 250" class="svg-accent" stroke-width="9" fill="none"/>')
    s.append('<text x="626" y="206" text-anchor="end" class="svg-text-muted">тросы к КПП</text>')
    offsets = {"friction": (-40, -46), "bushing": (-70, -24), "body": (24, 44), "grease": (60, -20), "reverse": (-70, 0)}
    for i, key in enumerate(order, 1):
        px, py = KULISA_POINTS[key]
        dx, dy = offsets[key]
        cx, cy = px + dx, py + dy
        s.append(f'<line x1="{px}" y1="{py}" x2="{cx}" y2="{cy}" class="svg-ink" stroke-width="1"/>')
        s.append(f'<circle cx="{px}" cy="{py}" r="3.5" class="svg-accent-fill"/>')
        s.append(f'<g class="hotspot" data-part="{key}" tabindex="0" role="button" aria-label="Узел {i}">'
                 f'<circle class="ring svg-ink svg-surface-fill" cx="{cx}" cy="{cy}" r="15" stroke-width="2"/>'
                 f'<text x="{cx}" y="{cy + 4.5}" text-anchor="middle" class="svg-text" style="font-weight:600">{i}</text></g>')
    return ('<svg viewBox="0 0 640 360" role="img" aria-label="Интерактивная схема кулисы КПП">'
            + "".join(s) + "</svg>")


LOGO = ('<svg viewBox="0 0 40 40" aria-hidden="true"><rect width="40" height="40" rx="10" class="svg-ink-fill"/>'
        '<path d="M9 27 C 17 27, 19 13, 31 13" fill="none" class="svg-accent" stroke-width="4" stroke-linecap="round"/>'
        '<circle cx="9" cy="27" r="3.4" fill="none" stroke="var(--bg)" stroke-width="2"/>'
        '<circle cx="31" cy="13" r="3.4" fill="none" stroke="var(--bg)" stroke-width="2"/></svg>')

FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 40 40'%3E"
           "%3Crect width='40' height='40' rx='10' fill='%23141b22'/%3E"
           "%3Cpath d='M9 27 C 17 27, 19 13, 31 13' fill='none' stroke='%23d63f1c' stroke-width='4' stroke-linecap='round'/%3E"
           "%3C/svg%3E")
