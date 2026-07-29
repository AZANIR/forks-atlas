"""SVG для README: робочий стіл macOS, плитки тек, шапки вікон Finder.

GitHub показує SVG через <img>, тож усередині не працюють ні посилання, ні
скрипти. Тому робочий стіл — одна оглядова картинка, а переходи робить Markdown,
який обгортає окремі плитки тек посиланнями. Навігація лишається текстовою і
працює навіть тоді, коли зображення не завантажились.

Уся геометрія детермінована: жодних зовнішніх шрифтів, растру чи анімації —
тільки те, що GitHub гарантовано не вирізає.

Масштаб. Картинку шириною 1200 GitHub показує приблизно в 900 пікселях, тобто
коефіцієнт 0.75. Тому значущий текст тут не менший за 20 одиниць, підписи — за 18.
"""

from __future__ import annotations

# Системний стек: власних шрифтів GitHub не вантажить, а системний уже має
# і оптичні розміри, і кернінг, і кирилицю.
FONT = (
    "-apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Segoe UI', "
    "Roboto, 'Helvetica Neue', Arial, sans-serif"
)

INK = "#f5f5f7"
MUTED = "#a1a1a6"
PANEL = "#1c1c1e"
CHROME = "#2c2c2e"
HAIRLINE = "#ffffff"

GLYPH_BOX = 44  # усі глифи намальовані в квадраті 44×44 і масштабуються звідси


def esc(text: str) -> str:
    return (
        str(text)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def shade(color: str, factor: float) -> str:
    """Освітлює (factor > 1) або притемнює (< 1) колір, лишаючись у межах 0..255."""
    r, g, b = (int(color[i:i + 2], 16) for i in (1, 3, 5))
    clamp = lambda c: max(0, min(255, round(c * factor)))
    return f"#{clamp(r):02x}{clamp(g):02x}{clamp(b):02x}"


def plural(n: int, one: str, few: str, many: str) -> str:
    if n % 10 == 1 and n % 100 != 11:
        return one
    if 2 <= n % 10 <= 4 and not 12 <= n % 100 <= 14:
        return few
    return many


def projects(n: int) -> str:
    return f"{n} {plural(n, 'проєкт', 'проєкти', 'проєктів')}"


def thousands(value: int) -> str:
    return f"{value:,}".replace(",", " ")


# --------------------------------------------------------------------------- #
# Глифи
#
# Кожна категорія має власний знак, а не однакову теку: на робочому столі
# теки шукають периферійним зором, за формою й кольором, а не читанням підписів.
# Малюємо обведенням, а не заливкою — тонкий контур однаково читається і на
# кольоровій підкладці, і в маленькому розмірі.
# --------------------------------------------------------------------------- #

GLYPHS = {
    "archive": """
      <path d="M8 13 h28 v8 H8 Z"/>
      <path d="M11.5 21 v11.5 a3 3 0 0 0 3 3 h15 a3 3 0 0 0 3 -3 V21"/>
      <path d="M18 27 h8"/>""",
    "security": """
      <path d="M22 7 L36.5 12 v11 c0 9 -7 14.5 -14.5 17.5 C14 37.5 7.5 32 7.5 23 V12 Z"/>
      <path d="M16.5 22.5 l4.5 4.5 L29 19"/>""",
    "qa": """
      <circle cx="22" cy="22" r="14"/>
      <path d="M15.5 22.5 l5 5 L30 18"/>""",
    "skills": """
      <path d="M22 11 L38.5 18 L22 25 L5.5 18 Z"/>
      <path d="M12 21.2 v7.8 c0 3 4.5 5 10 5 s10 -2 10 -5 v-7.8"/>
      <path d="M35.5 19.5 V30"/>""",
    "llm-infra": """
      <path d="M22 8 L35.5 15.5 V30 L22 37.5 L8.5 30 V15.5 Z"/>
      <path d="M8.5 15.5 L22 23 L35.5 15.5"/>
      <path d="M22 23 V37.5"/>""",
    "memory": """
      <circle cx="22" cy="11.5" r="4.2"/>
      <circle cx="10.5" cy="31" r="4.2"/>
      <circle cx="33.5" cy="31" r="4.2"/>
      <path d="M19.2 14.8 L13.3 27.7"/>
      <path d="M24.8 14.8 L30.7 27.7"/>
      <path d="M14.7 31 h14.6"/>""",
    "media": """
      <rect x="7" y="11" width="30" height="22" rx="5.5"/>
      <path d="M19 17.5 L28.5 22 L19 26.5 Z" fill="#ffffff" stroke="none"/>""",
    "agents": """
      <rect x="9.5" y="15" width="25" height="20" rx="6"/>
      <circle cx="17.5" cy="24" r="2.3" fill="#ffffff" stroke="none"/>
      <circle cx="26.5" cy="24" r="2.3" fill="#ffffff" stroke="none"/>
      <path d="M22 15 V9.5"/>
      <circle cx="22" cy="7.5" r="2.4" fill="#ffffff" stroke="none"/>
      <path d="M9.5 26 H5.5"/>
      <path d="M34.5 26 H38.5"/>""",
    "devops": """
      <circle cx="15.5" cy="22" r="7.6"/>
      <circle cx="28.5" cy="22" r="7.6"/>""",
    "resources": """
      <path d="M22 14 c-4 -3 -9.5 -4.2 -14.5 -3.2 V30.5 c5 -1 10.5 0.2 14.5 3.3 Z"/>
      <path d="M22 14 c4 -3 9.5 -4.2 14.5 -3.2 V30.5 c-5 -1 -10.5 0.2 -14.5 3.3 Z"/>""",
    "web": """
      <circle cx="22" cy="22" r="14"/>
      <path d="M8 22 H36"/>
      <ellipse cx="22" cy="22" rx="6.2" ry="14"/>""",
    "other": """
      <circle cx="13" cy="22" r="2.7" fill="#ffffff" stroke="none"/>
      <circle cx="22" cy="22" r="2.7" fill="#ffffff" stroke="none"/>
      <circle cx="31" cy="22" r="2.7" fill="#ffffff" stroke="none"/>""",
}

# Глифи для Dock. Це не декор: кожна іконка — реальна частина проєкту.
DOCK = [
    ("terminal", "#3a3a3c", """
      <path d="M13 15 l7 7 l-7 7"/>
      <path d="M24 29 h8"/>"""),
    ("git", "#f05033", """
      <circle cx="14" cy="12.5" r="4"/>
      <circle cx="14" cy="32" r="4"/>
      <circle cx="30" cy="18.5" r="4"/>
      <path d="M14 16.5 V28"/>
      <path d="M14 22.5 h10 a6 6 0 0 0 6 -6"/>"""),
    ("clock", "#0a84ff", """
      <circle cx="22" cy="22" r="13"/>
      <path d="M22 13.5 V22 l6.5 4"/>"""),
    ("doc", "#8e8e93", """
      <path d="M13.5 9 h12 l6.5 6.5 V35 a2 2 0 0 1 -2 2 H15.5 a2 2 0 0 1 -2 -2 Z"/>
      <path d="M18.5 23 h10"/>
      <path d="M18.5 29 h10"/>"""),
    ("sliders", "#5e5ce6", """
      <path d="M11 15 h22"/><path d="M11 22 h22"/><path d="M11 29 h22"/>
      <circle cx="19" cy="15" r="3" fill="#ffffff" stroke="none"/>
      <circle cx="27" cy="22" r="3" fill="#ffffff" stroke="none"/>
      <circle cx="17" cy="29" r="3" fill="#ffffff" stroke="none"/>"""),
    ("trash", "#48484a", """
      <path d="M11 15 h22"/>
      <path d="M15 15 v18 a2 2 0 0 0 2 2 h10 a2 2 0 0 0 2 -2 V15"/>
      <path d="M18.5 11.5 h7"/>"""),
]

DOCK_TITLES = {
    "terminal": "update.py",
    "git": "GitHub",
    "clock": "щотижневий запуск",
    "doc": "довідка",
    "sliders": "винятки",
    "trash": "видалені форки",
}


def glyph(body: str, x: float, y: float, size: float, weight: float = 3.1) -> str:
    """Ставить глиф так, щоб його квадрат 44×44 вписався в size і центр був у (x, y)."""
    scale = size / GLYPH_BOX
    left = x - size / 2
    top = y - size / 2
    return (
        f'<g transform="translate({left:.1f} {top:.1f}) scale({scale:.4f})" '
        f'fill="none" stroke="#ffffff" stroke-width="{weight / scale:.2f}" '
        f'stroke-linecap="round" stroke-linejoin="round">{body}</g>'
    )


def app_icon(key: str, color: str, cx: float, cy: float, size: float,
             body: str | None = None, label: str | None = None) -> str:
    """Іконка застосунку macOS: скруглений квадрат із градієнтом і глифом.

    Id градієнта походить від ключа й позиції, а не від hash(): хешування
    рядків у Python рандомізоване між процесами, тож id змінювались би щозапуску
    і той самий каталог давав би побайтово різні файли.
    """
    ident = f"ic-{key}-{round(cx)}-{round(cy)}"
    radius = size * 0.26
    caption = f"<title>{esc(label)}</title>" if label else ""
    return (
        f'<g>{caption}<defs><linearGradient id="{ident}" x1="0" y1="0" x2="0" y2="1">'
        f'<stop offset="0" stop-color="{shade(color, 1.22)}"/>'
        f'<stop offset="1" stop-color="{shade(color, 0.86)}"/></linearGradient></defs>'
        f'<rect x="{cx - size / 2:.1f}" y="{cy - size / 2:.1f}" width="{size}" '
        f'height="{size}" rx="{radius:.1f}" fill="url(#{ident})"/>'
        f'<rect x="{cx - size / 2:.1f}" y="{cy - size / 2:.1f}" width="{size}" '
        f'height="{size}" rx="{radius:.1f}" fill="none" stroke="#ffffff" '
        f'stroke-opacity="0.22"/>'
        f'{glyph(body if body is not None else GLYPHS.get(key, GLYPHS["other"]), cx, cy, size * 0.60, size * 0.058)}'
        f'</g>'
    )


# --------------------------------------------------------------------------- #
# Тека — клікабельна плитка під робочим столом
# --------------------------------------------------------------------------- #

def folder(label: str, color: str, key: str, width: int = 164) -> str:
    """Плитка з текою macOS: вкладка, корпус, світліша передня стінка, глиф.

    Лічильника тут немає навмисно: плитка — це кнопка переходу, а числа вже
    показані на обкладинці й у текстовому переліку під сіткою. Одне значення
    в одному візуальному місці.
    """
    height = round(width * 252 / 320)
    alt = f"Тека «{label}»"

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 252" \
width="{width}" height="{height}" role="img" aria-label="{esc(alt)}">
  <title>{esc(alt)}</title>
  <defs>
    <linearGradient id="tile" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#2a2a2f"/>
      <stop offset="1" stop-color="#1a1a1d"/>
    </linearGradient>
    <linearGradient id="front" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{shade(color, 1.18)}"/>
      <stop offset="1" stop-color="{shade(color, 0.92)}"/>
    </linearGradient>
    <filter id="shadow" x="-25%" y="-25%" width="150%" height="150%">
      <feDropShadow dx="0" dy="8" stdDeviation="10" flood-color="#000000"
                    flood-opacity="0.30"/>
    </filter>
  </defs>

  <rect width="320" height="252" rx="28" fill="url(#tile)"/>
  <!-- Верхня грань ловить світло: так поверхня читається як матеріал, а не заливка. -->
  <rect x="1" y="1" width="318" height="250" rx="27" fill="none"
        stroke="{HAIRLINE}" stroke-opacity="0.09"/>
  <path d="M29 1 H291" fill="none" stroke="{HAIRLINE}" stroke-opacity="0.16"
        stroke-width="1.5"/>

  <g filter="url(#shadow)">
    <rect x="80" y="44" width="68" height="34" rx="11" fill="{shade(color, 0.72)}"/>
    <rect x="80" y="60" width="160" height="104" rx="16" fill="{shade(color, 0.78)}"/>
    <rect x="80" y="78" width="160" height="86" rx="16" fill="url(#front)"/>
    <path d="M96 79 H224" fill="none" stroke="#ffffff" stroke-opacity="0.34"
          stroke-width="1.5"/>
  </g>
  {glyph(GLYPHS.get(key, GLYPHS["other"]), 160, 121, 52, 3.4)}

  <text x="160" y="212" text-anchor="middle" fill="{INK}" font-family="{FONT}"
        font-size="30" font-weight="600" letter-spacing="-0.4">{esc(label)}</text>
</svg>
"""


# --------------------------------------------------------------------------- #
# Робочий стіл — обкладинка README
# --------------------------------------------------------------------------- #

# Вікно зсунуте вліво навмисно: праворуч лишається смуга під іконки на столі.
# Але не надто — 100 ліворуч проти 200 праворуч читалося як помилка верстки.
WIN_X, WIN_Y, WIN_W = 64, 62, 950
CARD_W, CARD_H, CARD_GAP = 124, 152, 14


def _menubar(updated: str) -> str:
    menus = ["Файл", "Правка", "Вигляд", "Перейти", "Вікно", "Довідка"]
    x = 208
    items = []
    for name in menus:
        items.append(
            f'<text x="{x}" y="23" fill="{INK}" fill-opacity="0.70" '
            f'font-family="{FONT}" font-size="19">{esc(name)}</text>'
        )
        x += round(len(name) * 10.4) + 26

    return f"""
    <rect width="1200" height="34" fill="#ffffff" fill-opacity="0.13"/>
    <path d="M0 34 H1200" stroke="{HAIRLINE}" stroke-opacity="0.14"/>
    <!-- Знак замість логотипа платформи: роза вітрів під назву «Атлас». -->
    <path d="M22 7 L24.6 14.4 L32 17 L24.6 19.6 L22 27 L19.4 19.6 L12 17 L19.4 14.4 Z"
          fill="{INK}" fill-opacity="0.92"/>
    <text x="42" y="23" fill="{INK}" font-family="{FONT}" font-size="19"
          font-weight="680">Атлас проєктів</text>
    {"".join(items)}

    <!-- Дата стоїть праворуч і займає близько 100 одиниць, тож іконки статусу
         мусять закінчитись до 1050 — інакше вони наїжджають на текст. -->
    <g fill="none" stroke="{INK}" stroke-opacity="0.85" stroke-width="1.9"
       stroke-linecap="round">
      <g transform="translate(962 17)">
        <path d="M-10 -2.5 a14 14 0 0 1 20 0"/>
        <path d="M-5.8 2.2 a8.6 8.6 0 0 1 11.6 0"/>
        <circle cx="0" cy="6.8" r="1.5" fill="{INK}" stroke="none"/>
      </g>
      <g transform="translate(1000 17)">
        <circle cx="-1" cy="-1" r="6"/>
        <path d="M3.4 3.4 L7.6 7.6"/>
      </g>
      <g transform="translate(1038 17)">
        <rect x="-8.5" y="-7" width="7.5" height="14" rx="3.7"/>
        <rect x="1" y="-7" width="7.5" height="14" rx="3.7"/>
        <circle cx="-4.7" cy="-3" r="1.5" fill="{INK}" stroke="none"/>
        <circle cx="4.7" cy="3" r="1.5" fill="{INK}" stroke="none"/>
      </g>
    </g>
    <text x="1178" y="23" text-anchor="end" fill="{INK}" fill-opacity="0.88"
          font-family="{FONT}" font-size="19">{esc(updated)}</text>"""


# Глифи чипів залиті, а не обведені: на 17 пікселях контур замулюється,
# а суцільна форма лишається впізнаваною.
CHIP_GLYPHS = {
    "folder": '<path d="M8 15 h10 l3.5 4.5 H36 v13 a3 3 0 0 1 -3 3 H11 '
              'a3 3 0 0 1 -3 -3 Z" fill="#ffffff" stroke="none"/>',
    "star": '<path d="M22 8 L26.6 18.2 L37.5 19.6 L29.6 27.2 L31.6 38 L22 32.8 '
            'L12.4 38 L14.4 27.2 L6.5 19.6 L17.4 18.2 Z" fill="#ffffff" '
            'stroke="none"/>',
    "tag": '<path d="M11 13 h12.5 L35 24.5 L23.5 36 L11 23.5 Z" fill="#ffffff" '
           'stroke="none"/>'
           '<circle cx="18" cy="20" r="2.6" fill="#3a3a3c" stroke="none"/>',
}

CHIP_TOP, CHIP_H = 186, 50
CARDS_TOP = 278

# Рядок з пошуком, відрахований від правого краю вікна.
BTN2_X = WIN_W - 36 - 38
BTN1_X = BTN2_X - 48
SEARCH_W = 222
SEARCH_X = BTN1_X - 14 - SEARCH_W


def _chips(total: int, stars: int, categories: int) -> str:
    """Три показники одним рядком: іконка + значення, без дублювання одиниці."""
    data = [
        ("folder", projects(total), "#0a84ff", "проєктів у каталозі"),
        ("star", f"{thousands(stars)} ★", "#ff9f0a", "зірок у оригіналів разом"),
        ("tag", f"{categories} {plural(categories, 'тека', 'теки', 'тек')}", "#bf5af2",
         "категорій"),
    ]
    out, x = [], 36
    for key, value, tint, hint in data:
        # Власного вимірювання тексту в SVG немає, тож 11.2 одиниці на символ —
        # емпіричний крок для цього кегля. Запас праворуч свідомий.
        w = round(len(value) * 11.2) + 74
        out.append(
            f'<g transform="translate({x} {CHIP_TOP})">'
            f'<title>{esc(hint)}</title>'
            f'<rect width="{w}" height="{CHIP_H}" rx="15" fill="#ffffff" '
            f'fill-opacity="0.07"/>'
            f'<rect width="{w}" height="{CHIP_H}" rx="15" fill="none" stroke="#ffffff" '
            f'stroke-opacity="0.13"/>'
            f'{app_icon("chip-" + key, tint, 30, CHIP_H / 2, 28, CHIP_GLYPHS[key])}'
            f'<text x="52" y="{CHIP_H / 2 + 8:.0f}" fill="{INK}" font-family="{FONT}" '
            f'font-size="22" font-weight="600">{esc(value)}</text>'
            f'</g>'
        )
        x += w + 14
    return "".join(out)


def _cards(cards: list[tuple[str, str, str, int]]) -> tuple[str, int]:
    """Сітка карток категорій: шість у рядку, останній рядок центрується.

    Повертає розмітку і потрібну висоту вікна — від кількості категорій
    залежить, скільки рядків, тому вікно не може мати фіксовану висоту.
    """
    biggest = max((c[3] for c in cards), default=1) or 1
    rows = [cards[i:i + 6] for i in range(0, len(cards), 6)]
    out = []
    for r, row in enumerate(rows):
        span = len(row) * CARD_W + (len(row) - 1) * CARD_GAP
        x0 = (WIN_W - span) / 2
        y0 = CARDS_TOP + r * (CARD_H + CARD_GAP)
        for i, (key, label, color, count) in enumerate(row):
            x = x0 + i * (CARD_W + CARD_GAP)
            bar = max(round(80 * count / biggest), 6)
            out.append(
                f'<g transform="translate({x:.1f} {y0})">'
                f'<rect width="{CARD_W}" height="{CARD_H}" rx="18" fill="#ffffff" '
                f'fill-opacity="0.055"/>'
                f'<rect width="{CARD_W}" height="{CARD_H}" rx="18" fill="none" '
                f'stroke="#ffffff" stroke-opacity="0.085"/>'
                f'{app_icon(key, color, CARD_W / 2, 48, 56)}'
                f'<text x="{CARD_W / 2}" y="99" text-anchor="middle" fill="{INK}" '
                f'font-family="{FONT}" font-size="21" font-weight="620" '
                f'letter-spacing="-0.2">{esc(label)}</text>'
                f'<text x="{CARD_W / 2}" y="122" text-anchor="middle" fill="{MUTED}" '
                f'font-family="{FONT}" font-size="18">{esc(projects(count))}</text>'
                f'<rect x="22" y="134" width="80" height="4" rx="2" fill="#ffffff" '
                f'fill-opacity="0.12"/>'
                f'<rect x="22" y="134" width="{bar}" height="4" rx="2" fill="{color}"/>'
                f'</g>'
            )
    height = CARDS_TOP + len(rows) * (CARD_H + CARD_GAP) + 20
    return "".join(out), height


def _dock(y: int) -> str:
    size, gap, pad = 56, 16, 18
    count = len(DOCK)
    inner = count * size + (count - 1) * gap + 22  # 22 — розділювач перед кошиком
    total = inner + pad * 2
    x0 = (1200 - total) / 2
    height = size + pad * 2

    icons = []
    cx = x0 + pad + size / 2
    for key, color, body in DOCK:
        if key == "trash":
            # Кошик у macOS відділений від застосунків — не декор, а межа сенсу.
            cx += 22
            icons.append(
                f'<path d="M{cx - size / 2 - 11:.1f} {y + 16} V{y + height - 16}" '
                f'fill="none" stroke="#ffffff" stroke-opacity="0.20"/>'
            )
        icons.append(
            app_icon(key, color, cx, y + height / 2, size, body, DOCK_TITLES[key])
        )
        cx += size + gap

    return f"""
    <g>
      <rect x="{x0:.1f}" y="{y}" width="{total}" height="{height}" rx="26"
            fill="#ffffff" fill-opacity="0.14"/>
      <rect x="{x0:.1f}" y="{y}" width="{total}" height="{height}" rx="26" fill="none"
            stroke="#ffffff" stroke-opacity="0.20"/>
      <path d="M{x0 + 26:.1f} {y + 1} H{x0 + total - 26:.1f}" stroke="{HAIRLINE}"
            stroke-opacity="0.28" stroke-width="1.5"/>
      {"".join(icons)}
    </g>"""


def _desk_icons() -> str:
    """Іконки на самому столі: те, що поруч із каталогом, але не є текою."""
    bodies = {key: body for key, _, body in DOCK}
    items = [
        ("desk-doc", "Довідка", "#8e8e93", bodies["doc"]),
        ("desk-data", "Дані", "#30d158", GLYPHS["llm-infra"]),
    ]
    out = []
    for index, (ident, label, color, body) in enumerate(items):
        cy = 108 + index * 134
        out.append(
            f'{app_icon(ident, color, 1104, cy, 68, body, label)}'
            f'<text x="1104" y="{cy + 60}" text-anchor="middle" fill="{INK}" '
            f'font-family="{FONT}" font-size="19" font-weight="520">{esc(label)}</text>'
        )
    return "".join(out)


def desktop(total: int, stars: int, updated: str,
            cards: list[tuple[str, str, str, int]]) -> str:
    """Робочий стіл: меню-бар, вікно з картками категорій, іконки на столі, Dock."""
    grid, grid_height = _cards(cards)
    win_h = grid_height
    dock_y = WIN_Y + win_h + 26
    page_h = dock_y + 92 + 22
    alt = f"Атлас проєктів: {projects(total)} у {len(cards)} теках"

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 {page_h}" \
width="1200" height="{page_h}" role="img" aria-label="{esc(alt)}">
  <title>Атлас проєктів — робочий стіл</title>
  <defs>
    <linearGradient id="wall" x1="0.05" y1="0" x2="0.95" y2="1">
      <stop offset="0" stop-color="#3b2a63"/>
      <stop offset="0.42" stop-color="#241f4d"/>
      <stop offset="1" stop-color="#141230"/>
    </linearGradient>
    <radialGradient id="aurora" cx="0.16" cy="0.08" r="0.75">
      <stop offset="0" stop-color="#8b6cff" stop-opacity="0.40"/>
      <stop offset="1" stop-color="#8b6cff" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="streak" cx="0.9" cy="0.95" r="0.6">
      <stop offset="0" stop-color="#c77dff" stop-opacity="0.34"/>
      <stop offset="1" stop-color="#c77dff" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="glass" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#2e2e33"/>
      <stop offset="1" stop-color="#1a1a1d"/>
    </linearGradient>
    <filter id="winShadow" x="-10%" y="-10%" width="120%" height="130%">
      <feDropShadow dx="0" dy="18" stdDeviation="22" flood-color="#0a0618"
                    flood-opacity="0.55"/>
    </filter>
    <clipPath id="screen"><rect width="1200" height="{page_h}" rx="22"/></clipPath>
    <clipPath id="win">
      <rect x="{WIN_X}" y="{WIN_Y}" width="{WIN_W}" height="{win_h}" rx="15"/>
    </clipPath>
  </defs>

  <g clip-path="url(#screen)">
    <rect width="1200" height="{page_h}" fill="url(#wall)"/>
    <rect width="1200" height="{page_h}" fill="url(#aurora)"/>
    <rect width="1200" height="{page_h}" fill="url(#streak)"/>
    {_menubar(updated)}
    {_desk_icons()}

    <g filter="url(#winShadow)">
      <rect x="{WIN_X}" y="{WIN_Y}" width="{WIN_W}" height="{win_h}" rx="15"
            fill="url(#glass)"/>
    </g>
    <g clip-path="url(#win)">
      <rect x="{WIN_X}" y="{WIN_Y}" width="{WIN_W}" height="{win_h}" fill="{PANEL}"/>
      <rect x="{WIN_X}" y="{WIN_Y}" width="{WIN_W}" height="42" fill="{CHROME}"/>
      <path d="M{WIN_X} {WIN_Y + 42} H{WIN_X + WIN_W}" stroke="{HAIRLINE}"
            stroke-opacity="0.10"/>

      <g transform="translate({WIN_X} {WIN_Y})">
        <!-- Керування вікном завжди ліворуч зверху — ламати це немає підстав. -->
        <circle cx="24" cy="21" r="6.5" fill="#ff5f57"/>
        <circle cx="45" cy="21" r="6.5" fill="#febc2e"/>
        <circle cx="66" cy="21" r="6.5" fill="#28c840"/>
        <text x="{WIN_W / 2}" y="28" text-anchor="middle" fill="{INK}"
              fill-opacity="0.86" font-family="{FONT}" font-size="20"
              font-weight="600">Атлас проєктів</text>

        <!-- Великий кегль просить від'ємного трекінгу: інакше літери розповзаються. -->
        <text x="36" y="104" fill="{INK}" font-family="{FONT}" font-size="46"
              font-weight="700" letter-spacing="-1.1">Атлас проєктів</text>
        <text x="36" y="138" fill="{INK}" fill-opacity="0.66" font-family="{FONT}"
              font-size="20">Що варте уваги в AI-агентах, безпеці та автоматизації —</text>
        <text x="36" y="162" fill="{INK}" fill-opacity="0.66" font-family="{FONT}"
              font-size="20">розкладене по теках, оновлюється щотижня.</text>

        <!-- Пошук і кнопки прив'язані до правого краю вікна виразом, а не
             числами: інакше кожна зміна WIN_W тихо зсуває їх у нікуди. -->
        <g>
          <rect x="{SEARCH_X}" y="66" width="{SEARCH_W}" height="38" rx="19"
                fill="#ffffff" fill-opacity="0.08"/>
          <rect x="{SEARCH_X}" y="66" width="{SEARCH_W}" height="38" rx="19" fill="none"
                stroke="#ffffff" stroke-opacity="0.14"/>
          <g transform="translate({SEARCH_X + 24} 85)" fill="none" stroke="{MUTED}"
             stroke-width="1.9" stroke-linecap="round">
            <circle cx="-1" cy="-1" r="5.4"/><path d="M3 3 L6.8 6.8"/>
          </g>
          <text x="{SEARCH_X + 40}" y="91" fill="{MUTED}" font-family="{FONT}" font-size="18">Пошук по теках…</text>

          <rect x="{BTN1_X}" y="66" width="38" height="38" rx="13" fill="#ffffff"
                fill-opacity="0.08"/>
          <path d="M{BTN1_X + 22} 76 a10 10 0 1 0 6.5 17.5 A11.5 11.5 0 0 1 {BTN1_X + 22} 76 Z"
                fill="{INK}" fill-opacity="0.72"/>
          <rect x="{BTN2_X}" y="66" width="38" height="38" rx="13" fill="#ffffff"
                fill-opacity="0.08"/>
          <g fill="{INK}" fill-opacity="0.72">
            <circle cx="{BTN2_X + 13}" cy="80" r="2.1"/>
            <circle cx="{BTN2_X + 25}" cy="80" r="2.1"/>
            <circle cx="{BTN2_X + 13}" cy="90" r="2.1"/>
            <circle cx="{BTN2_X + 25}" cy="90" r="2.1"/>
          </g>
        </g>

        {_chips(total, stars, len(cards))}
        <path d="M36 {CHIP_TOP + CHIP_H + 24} H{WIN_W - 36}" stroke="{HAIRLINE}"
              stroke-opacity="0.09"/>
        {grid}
      </g>
    </g>

    {_dock(dock_y)}
  </g>
</svg>
"""


# --------------------------------------------------------------------------- #
# Вікно Finder — шапка сторінки категорії
# --------------------------------------------------------------------------- #

def window(title: str, color: str, count: int, key: str) -> str:
    """Вікно Finder: світлофор ліворуч, назва по центру, шлях і глиф теки під ним."""
    alt = f"Вікно Finder: {title}, {projects(count)}"
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 112" \
width="1200" height="112" role="img" aria-label="{esc(alt)}">
  <title>{esc(alt)}</title>
  <defs>
    <clipPath id="win"><rect width="1200" height="112" rx="16"/></clipPath>
  </defs>
  <g clip-path="url(#win)">
    <rect width="1200" height="112" fill="{PANEL}"/>
    <rect width="1200" height="56" fill="{CHROME}"/>
    <path d="M0 56 H1200" stroke="{HAIRLINE}" stroke-opacity="0.10"/>
    <path d="M0 0.5 H1200" stroke="{HAIRLINE}" stroke-opacity="0.14"/>

    <circle cx="28" cy="28" r="7.5" fill="#ff5f57"/>
    <circle cx="52" cy="28" r="7.5" fill="#febc2e"/>
    <circle cx="76" cy="28" r="7.5" fill="#28c840"/>

    <text x="600" y="36" text-anchor="middle" fill="{INK}" font-family="{FONT}"
          font-size="26" font-weight="640" letter-spacing="-0.4">{esc(title)}</text>

    {app_icon(key, color, 42, 84, 34)}
    <text x="70" y="91" fill="{INK}" fill-opacity="0.60" font-family="{FONT}"
          font-size="21">Атлас</text>
    <text x="127" y="91" fill="{INK}" fill-opacity="0.34" font-family="{FONT}"
          font-size="21">›</text>
    <text x="145" y="91" fill="{INK}" font-family="{FONT}" font-size="21"
          font-weight="560">{esc(title)}</text>
    <text x="1172" y="91" text-anchor="end" fill="{MUTED}" font-family="{FONT}"
          font-size="21">{esc(projects(count))}</text>
  </g>
</svg>
"""
