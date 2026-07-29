"""SVG для README: робочий стіл, теки та вікна Finder.

GitHub показує SVG через <img>, тож усередині не працюють ні посилання, ні
скрипти. Тому кожна тека — окремий файл, а клікабельною її робить Markdown,
який обгортає картинку посиланням. Навігація лишається текстовою і працює
навіть тоді, коли зображення не завантажились.

Уся геометрія детермінована: жодних зовнішніх шрифтів, растру чи анімації —
тільки те, що GitHub гарантовано не вирізає.
"""

from __future__ import annotations

# Системний стек: власних шрифтів GitHub не вантажить, а системний уже має
# і оптичні розміри, і кернінг, і кирилицю.
FONT = (
    "-apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Segoe UI', "
    "Roboto, 'Helvetica Neue', Arial, sans-serif"
)

INK = "#f5f5f7"
MUTED = "#98989d"
PANEL = "#1c1c1f"
CHROME = "#2a2a2e"
HAIRLINE = "#ffffff"


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
# Тека — плитка робочого столу
# --------------------------------------------------------------------------- #

def folder(label: str, color: str, count: int, width: int = 240) -> str:
    """Плитка з текою macOS: вкладка, корпус, світліша передня стінка."""
    height = round(width * 288 / 320)
    tab = shade(color, 0.74)
    back = shade(color, 0.80)
    front_top = shade(color, 1.16)
    front_bottom = shade(color, 0.94)
    alt = f"Тека «{label}», {projects(count)}"

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 288" \
width="{width}" height="{height}" role="img" aria-label="{esc(alt)}">
  <title>{esc(alt)}</title>
  <defs>
    <linearGradient id="tile" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#26262b"/>
      <stop offset="1" stop-color="#161619"/>
    </linearGradient>
    <linearGradient id="front" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{front_top}"/>
      <stop offset="1" stop-color="{front_bottom}"/>
    </linearGradient>
  </defs>

  <rect width="320" height="288" rx="28" fill="url(#tile)"/>
  <!-- Верхня грань ловить світло: так поверхня читається як матеріал, а не як заливка. -->
  <rect x="1" y="1" width="318" height="286" rx="27" fill="none"
        stroke="{HAIRLINE}" stroke-opacity="0.09"/>
  <path d="M29 1 H291" stroke="{HAIRLINE}" stroke-opacity="0.16" stroke-width="1.5"/>

  <g>
    <rect x="80" y="56" width="68" height="34" rx="11" fill="{tab}"/>
    <rect x="80" y="72" width="160" height="100" rx="16" fill="{back}"/>
    <rect x="80" y="90" width="160" height="82" rx="16" fill="url(#front)"/>
    <path d="M96 91 H224" stroke="#ffffff" stroke-opacity="0.34" stroke-width="1.5"/>
  </g>

  <text x="160" y="214" text-anchor="middle" fill="{INK}" font-family="{FONT}"
        font-size="27" font-weight="600" letter-spacing="-0.3">{esc(label)}</text>
  <text x="160" y="248" text-anchor="middle" fill="{MUTED}" font-family="{FONT}"
        font-size="21" letter-spacing="0.2">{esc(projects(count))}</text>
</svg>
"""


# --------------------------------------------------------------------------- #
# Робочий стіл — головна сторінка
# --------------------------------------------------------------------------- #

def hero(total: int, stars: int, categories: int, updated: str) -> str:
    """Робочий стіл: рядок меню зверху, назва, три показники."""
    chips = [
        (projects(total), "#0a84ff"),
        (f"{thousands(stars)} ★", "#ff9f0a"),
        (f"{categories} {plural(categories, 'категорія', 'категорії', 'категорій')}", "#bf5af2"),
    ]
    x = 56
    chip_svg = []
    for text, tint in chips:
        # Ширина рахується від довжини рядка: власного вимірювання тексту в SVG
        # немає, тож 12.2 одиниці на символ — емпіричний крок для цього кегля.
        w = round(len(text) * 12.2 + 52)
        chip_svg.append(
            f'<g><rect x="{x}" y="262" width="{w}" height="52" rx="26" '
            f'fill="{tint}" fill-opacity="0.16"/>'
            f'<rect x="{x}" y="262" width="{w}" height="52" rx="26" fill="none" '
            f'stroke="{tint}" stroke-opacity="0.42"/>'
            f'<circle cx="{x + 26}" cy="288" r="6" fill="{tint}"/>'
            f'<text x="{x + 44}" y="295" fill="{INK}" font-family="{FONT}" '
            f'font-size="23" font-weight="500">{esc(text)}</text></g>'
        )
        x += w + 16

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 360" \
width="1200" height="360" role="img" \
aria-label="Атлас проєктів: {esc(projects(total))} у {categories} категоріях">
  <title>Атлас проєктів — робочий стіл</title>
  <defs>
    <linearGradient id="wall" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#2b2350"/>
      <stop offset="0.45" stop-color="#1b1b3a"/>
      <stop offset="1" stop-color="#141428"/>
    </linearGradient>
    <radialGradient id="glow" cx="0.78" cy="0.12" r="0.7">
      <stop offset="0" stop-color="#6f5bff" stop-opacity="0.34"/>
      <stop offset="1" stop-color="#6f5bff" stop-opacity="0"/>
    </radialGradient>
    <clipPath id="card"><rect width="1200" height="360" rx="22"/></clipPath>
  </defs>

  <g clip-path="url(#card)">
    <rect width="1200" height="360" fill="url(#wall)"/>
    <rect width="1200" height="360" fill="url(#glow)"/>

    <!-- Рядок меню: напівпрозорий шар поверх шпалер, як у macOS. -->
    <rect width="1200" height="46" fill="#ffffff" fill-opacity="0.10"/>
    <path d="M0 46 H1200" stroke="{HAIRLINE}" stroke-opacity="0.14"/>
    <circle cx="34" cy="23" r="8" fill="{INK}" fill-opacity="0.9"/>
    <text x="58" y="31" fill="{INK}" font-family="{FONT}" font-size="20"
          font-weight="650">Атлас</text>
    <text x="130" y="31" fill="{INK}" fill-opacity="0.62" font-family="{FONT}"
          font-size="20">Категорії</text>
    <text x="228" y="31" fill="{INK}" fill-opacity="0.62" font-family="{FONT}"
          font-size="20">Джерела</text>
    <text x="320" y="31" fill="{INK}" fill-opacity="0.62" font-family="{FONT}"
          font-size="20">Оновлення</text>
    <text x="1168" y="31" text-anchor="end" fill="{INK}" fill-opacity="0.72"
          font-family="{FONT}" font-size="20">{esc(updated)}</text>

    <!-- Великий кегль просить від'ємного трекінгу: інакше літери розповзаються. -->
    <text x="56" y="176" fill="{INK}" font-family="{FONT}" font-size="66"
          font-weight="700" letter-spacing="-1.4">Атлас проєктів</text>
    <text x="56" y="222" fill="{INK}" fill-opacity="0.66" font-family="{FONT}"
          font-size="25" letter-spacing="-0.1">Що варте уваги в AI-агентах, безпеці та
      автоматизації — розкладене по теках</text>

    {"".join(chip_svg)}
  </g>
</svg>
"""


# --------------------------------------------------------------------------- #
# Вікно Finder — шапка сторінки категорії
# --------------------------------------------------------------------------- #

def window(title: str, color: str, count: int) -> str:
    """Вікно Finder: світлофор ліворуч, назва по центру, шлях під ним."""
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

    <!-- Керування вікном завжди ліворуч зверху — ламати це немає підстав. -->
    <circle cx="28" cy="28" r="7.5" fill="#ff5f57"/>
    <circle cx="52" cy="28" r="7.5" fill="#febc2e"/>
    <circle cx="76" cy="28" r="7.5" fill="#28c840"/>

    <text x="600" y="36" text-anchor="middle" fill="{INK}" font-family="{FONT}"
          font-size="26" font-weight="640" letter-spacing="-0.4">{esc(title)}</text>

    <g transform="translate(28 70)">
      <rect x="0" y="0" width="13" height="6" rx="2" fill="{shade(color, 0.78)}"/>
      <rect x="0" y="3" width="30" height="19" rx="4" fill="{shade(color, 0.82)}"/>
      <rect x="0" y="7" width="30" height="15" rx="4" fill="{shade(color, 1.10)}"/>
    </g>
    <text x="70" y="88" fill="{INK}" fill-opacity="0.60" font-family="{FONT}"
          font-size="21">Атлас</text>
    <text x="127" y="88" fill="{INK}" fill-opacity="0.34" font-family="{FONT}"
          font-size="21">›</text>
    <text x="145" y="88" fill="{INK}" font-family="{FONT}" font-size="21"
          font-weight="560">{esc(title)}</text>
    <text x="1172" y="88" text-anchor="end" fill="{MUTED}" font-family="{FONT}"
          font-size="21">{esc(projects(count))}</text>
  </g>
</svg>
"""
