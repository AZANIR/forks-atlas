#!/usr/bin/env python3
"""Каталог форкнутих репозиторіїв GitHub.

Тягне всі форки користувача через GraphQL, розкладає по категоріях
і перегенеровує README.md та data/forks.json.

Запуск:
    python scripts/update.py              # оновити каталог
    python scripts/update.py --self-test  # перевірити класифікатор (без мережі)

Токен береться з GITHUB_TOKEN / GH_TOKEN, а якщо їх немає — з `gh auth token`.
Залежностей немає: тільки стандартна бібліотека.
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

USER = "AZANIR"
ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
DATA = ROOT / "data" / "forks.json"
OVERRIDES = ROOT / "scripts" / "overrides.json"
EXTRA = ROOT / "scripts" / "extra.json"

PAGE_SIZE = 50          # 100 вузлів із вкладеним parent перевищують ліміт вартості GraphQL
STALE_DAYS = 365        # після цього оригінал вважається «сплячим»
DESC_LIMIT = 165        # обрізання опису в таблиці

# ---------------------------------------------------------------------------
# Категорії.
#
# Порядок має значення: перемагає перший збіг. Вузькі категорії стоять раніше
# за широкі, інакше «AI» проковтне і безпеку, і QA — майже кожен сучасний
# інструмент згадує агентів. Тому `strix` («AI penetration testing») лягає в
# безпеку, а `explorbot` («AI Agent for Exploratory Browser Testing») — у QA.
#
# `blurb` — це відповідь на питання «навіщо цей кластер існує», її пишемо руками.
# `keywords` — те, за чим класифікатор шукає збіг у назві, описі й темах.
# ---------------------------------------------------------------------------
CATEGORIES = [
    {
        "key": "archive",
        "title": "Навчальний архів і курсові проєкти",
        "blurb": (
            "Курсові приклади й чужі profile-README, збережені колись як зразок оформлення. "
            "Робочої цінності не мають, але видаляти їх — це стирати власну історію. "
            "Тримаються окремо, щоб не засмічувати активні категорії. "
            "Навчальних завдань GitHub Classroom тут немає: вони приватні, "
            "а каталог свідомо показує лише публічне."
        ),
        "keywords": ["classroom", "github classroom", "udemy", "course"],
    },
    {
        "key": "security",
        "title": "Кібербезпека, OSINT і red team",
        "blurb": (
            "Класичний інструментарій безпеки поруч з новою хвилею AI-пентестерів. "
            "Тут і фундамент, який працює десятиліттями (ghidra, mitmproxy, nuclei, SecLists), "
            "і автономні агенти, що намагаються цей фундамент замінити (strix, shannon, pentagi). "
            "Тримати їх разом корисно саме для порівняння: видно, що AI поки додає шар зверху, "
            "а не витісняє базові сканери."
        ),
        "keywords": [
            "security", "cybersecurity", "infosec", "appsec", "pentest", "pentesting",
            "penetration testing", "osint", "redteam", "red team", "offensive security",
            "blueteam", "bugbounty", "bug bounty", "vulnerability", "vulnerabilities",
            "exploit", "exploits", "malware", "reverse engineering", "disassembler",
            "threat", "threat intelligence", "forensics", "dfir", "incident response",
            "hacking", "ethical hacking", "hackerone", "recon", "reconnaissance",
            "nuclei", "seclists", "ctf", "privacy", "antidetect", "anti detect",
            "man in the middle", "sbom", "secrets", "active directory", "ldap",
            "captcha", "cve", "xss", "sql injection",
            # Ідентифікація й доступ. Свідомо без голого «authentication»:
            # це слово згадує половина веб-бойлерплейтів, і безпека, що стоїть
            # раніше за них у черзі, забрала б їх усі.
            "sso", "single sign on", "multi factor", "multifactor", "2fa", "mfa",
            "oauth2", "openid connect", "webauthn", "passkeys", "identity provider",
            "zero trust", "vpn", "firewall", "password manager", "encryption",
        ],
    },
    {
        "key": "qa",
        "title": "QA та автоматизація тестування",
        "blurb": (
            "Профільний блок: фреймворки, бойлерплейти й утиліти для e2e, API та "
            "мобільного тестування. Частина форків — робочі інструменти (Playwright, Appium, "
            "mokapi, k6), частина — навчальні репозиторії часів опанування Cypress. "
            "Другі позначені як сплячі, але лишаються як приклади еволюції підходів."
        ),
        "keywords": [
            "playwright", "cypress", "selenium", "webdriver", "webdriverio", "wdio",
            # «end to end» без слова testing забирає навчальні матеріали
            # («End-to-end tutorials for building agents»), тому лише повна форма.
            "appium", "e2e", "end to end testing", "test automation", "automated testing",
            "testing", "test", "tests", "qa", "qa automation", "test runner",
            "cucumber", "gherkin", "allure", "newman", "postman", "swagger", "openapi",
            "k6", "jmeter", "load testing", "performance testing", "unit testing",
            "mocking", "mock", "test architecture", "static analysis", "code quality",
            "sonarqube", "coverage", "flaky", "selenoid", "device farm",
        ],
    },
    {
        "key": "skills",
        "title": "Agent Skills, субагенти та плагіни",
        "blurb": (
            "Найшвидше зростаючий шар екосистеми: не самі агенти, а те, чим їх «озброюють». "
            "Skills, субагенти, плагіни й марketplace-каталоги для Claude Code, Codex, "
            "OpenClaw і Cursor. Цінність колекції тут не в кожному окремому репо, "
            "а в можливості порівняти, як різні команди описують одну й ту саму ідею — "
            "переносний набір інструкцій для агента."
        ),
        "keywords": [
            "agent skills", "agent skill", "claude skills", "claude skill", "agentskills",
            "skill", "skills", "subagent", "subagents", "codex skills", "openclaw skills",
            "claude code plugin", "plugin", "plugins", "marketplace", "slash command",
            "prompt engineering", "system prompts", "system prompt", "claude md",
        ],
    },
    {
        "key": "llm-infra",
        "title": "LLM-інфраструктура, гейтвеї та проксі",
        "blurb": (
            "Шар під агентами: сервери інференсу, маршрутизатори моделей, проксі для "
            "економії токенів і локальні голосові моделі. Це те, що визначає вартість "
            "і швидкість усього, що вище. Форки тут — переважно про незалежність від "
            "одного провайдера: гейтвеї на 200+ моделей, локальний STT/TTS, обхід rate limit."
        ),
        # Стоїть перед «пам'яттю» навмисно: в описах інфраструктурних проєктів
        # слово memory майже завжди означає RAM, а не пам'ять агента
        # («memory-efficient serving engine» у vllm).
        "keywords": [
            "inference", "inference server", "gateway", "ai gateway", "proxy",
            "llmops", "model serving", "llm serving", "vllm", "quantization",
            "abliteration", "transformer", "fine tuning", "finetuning", "ollama",
            "llama cpp", "gguf", "onnx", "tts", "stt", "text to speech",
            "speech to text", "asr", "whisper", "voice", "router", "openrouter",
            "token", "tokens", "api key", "rate limit", "self hosted llm",
        ],
    },
    {
        "key": "memory",
        "title": "Пам'ять, контекст і RAG",
        "blurb": (
            "Відповідь індустрії на головне обмеження LLM — вікно контексту. "
            "Тут бібліотеки довготривалої пам'яті агентів, графи знань, RAG-фреймворки "
            "й інтеграції з Obsidian та NotebookLM. Практичний сенс форків: більшість "
            "проєктів у цій категорії ще не стабілізували API, тому власна копія — "
            "це страховка від ламких оновлень."
        ),
        "keywords": [
            "memory", "agent memory", "rag", "retrieval augmented generation",
            "retrieval augmented", "knowledge graph", "graphrag", "context engineering",
            "context window", "embeddings", "vector search", "vector database",
            "second brain", "obsidian", "notebooklm", "notebook lm", "knowledge base",
            "knowledge management", "semantic", "note taking", "persistent memory",
            "spaced repetition", "compression",
        ],
    },
    {
        "key": "media",
        "title": "Медіа, контент і маркетинг",
        "blurb": (
            "Інструменти, що виробляють артефакт для людини, а не для рантайму: відео, "
            "презентації, діаграми, зображення, SEO-аналіз. Окрема категорія потрібна тому, "
            "що ці проєкти майже завжди агентні за реалізацією, але їхня цінність — у результаті, "
            "а не в архітектурі."
        ),
        # Стоїть перед «агентами» навмисно: сьогодні кожен конвертер описує себе як
        # AI-інструмент, тому ширше слово `ai` інакше забирає весь медійний блок
        # («An AI-boost concurrent downloader»).
        "keywords": [
            "video", "video editor", "video editing", "audio", "image generation",
            "downloader", "download manager", "screen recorder", "screen capture",
            "editor", "presentation", "presentations", "pptx", "powerpoint", "slides",
            "ffmpeg", "transcription", "dictation", "translation", "translator",
            "dubbing", "podcast", "design", "design systems", "figma", "drawio",
            "diagram", "diagrams", "seo", "marketing", "content", "animation",
            "pdf", "markdown", "document parsing", "ocr", "svg", "3d",
        ],
    },
    {
        "key": "agents",
        "title": "AI-агенти, harness'и та оркестрація",
        "blurb": (
            "Ядро колекції й причина, чому вона взагалі така велика. Агентні фреймворки, "
            "harness'и навколо Claude Code / Codex / OpenClaw, дашборди для керування "
            "роями агентів, MCP-сервери. Категорія навмисно широка: у 2025–2026 межа між "
            "«фреймворком», «оболонкою» і «продуктом» розмита, і розділяти їх штучно означало б "
            "щотижня перекладати репозиторії з полиці на полицю."
        ),
        "keywords": [
            "agent", "agents", "ai agent", "ai agents", "agentic", "multi agent",
            "claude", "claude code", "codex", "openclaw", "clawdbot", "anthropic",
            "openai", "chatgpt", "gpt", "gemini", "copilot", "cursor", "opencode",
            "llm", "llms", "ai", "artificial intelligence", "genai", "generative ai",
            "agi", "orchestration", "orchestrator", "swarm", "harness", "autonomous",
            "mcp", "model context protocol", "chatbot", "assistant", "ai assistant",
            "coding agent", "vibe coding", "spec driven development", "evals",
            "computer use", "browser automation", "workflow automation", "n8n",
        ],
    },
    {
        "key": "devops",
        "title": "DevOps, інфраструктура та мережі",
        "blurb": (
            "Контейнери, Kubernetes, Terraform, мережеві утиліти й самохостинг. "
            "Помітно менший блок, ніж AI, і це чесно відображає зміщення фокусу: "
            "інфраструктурні форки здебільшого 2021–2024 років, тоді як AI-шар — останнього року."
        ),
        "keywords": [
            "docker", "kubernetes", "k8s", "terraform", "devops", "ci cd", "cicd",
            "github actions", "self hosted", "selfhosted", "container", "containers",
            "ansible", "cloud", "aws", "azure", "gcp", "networking", "network",
            "monitoring", "observability", "linux", "shell", "bash", "sysadmin",
            "nginx", "deployment", "deployments", "infrastructure", "sre",
            "virtualization", "android", "proxmox", "homelab",
        ],
    },
    {
        "key": "resources",
        "title": "Ресурси, роадмапи та навчальні матеріали",
        "blurb": (
            "Курировані списки й дорожні карти, що не належать жодній технічній категорії "
            "напряму. Зверніть увагу: тематичні awesome-списки (наприклад, про безпеку чи "
            "агентів) лежать не тут, а у своїх категоріях із міткою 📋 — формат не є темою."
        ),
        "keywords": [
            "awesome", "awesome list", "curated", "curated list", "roadmap", "roadmaps",
            "tutorial", "tutorials", "course", "courses", "learning", "guide", "guides",
            "handbook", "cheatsheet", "cheat sheet", "best practices", "interview",
            "interview questions", "book", "study", "study plan", "resources",
            "writeups", "career", "documentation", "docs", "readme",
            # Загальне ML тримаємо тут, а не в LLM-інфраструктурі: у цій колекції
            # воно трапляється майже виключно у вигляді роадмапів і курсів.
            "machine learning", "neural networks", "deep learning",
        ],
    },
    {
        "key": "web",
        "title": "Веб, фронтенд і шаблони",
        "blurb": (
            "Стартові шаблони, генератори статичних сайтів і фронтенд-утиліти. "
            "Найстаріший шар колекції — здебільшого форки-заготовки, збережені «щоб було "
            "з чого почати», коли така потреба виникне."
        ),
        "keywords": [
            "react", "nextjs", "next js", "vue", "vuejs", "svelte", "astro",
            "11ty", "eleventy", "scss", "sass", "tailwind", "tailwindcss", "shadcn",
            "frontend", "landing", "landing page", "static site", "static site generator",
            "template", "templates", "boilerplate", "starter", "ui", "ux", "css",
            "html", "website", "web app", "electron", "theme", "portfolio",
        ],
    },
]

CATEGORY_BY_KEY = {c["key"]: c for c in CATEGORIES}
OTHER = {
    "key": "other",
    "title": "Нерозібране",
    "blurb": (
        "Форки, які правила не змогли віднести до жодної категорії — зазвичай через "
        "порожній опис і відсутність тем в оригіналі. Виправляється одним рядком "
        "у `scripts/overrides.json`; якщо цей блок росте — правила потребують уваги."
    ),
    "keywords": [],
}

BADGES = {
    "list": ("📋", "куративний список"),
    "linkonly": ("🔗", "у форках немає — стежимо за оригіналом"),
    "archived": ("⚠️", "оригінал заархівовано"),
    "stale": ("💤", "оригінал без комітів понад рік"),
    "orphan": ("🗑️", "оригінал видалено або недоступний"),
}

# `privacy: PUBLIC` тут обов'язкове, а не косметичне. Токен GitHub Actions бачить
# лише публічні репозиторії, а особистий PAT — ще й приватні. Без фільтра каталог
# отримував би різний склад залежно від того, хто його запустив, і щотижня
# перезаписував би сам себе. До того ж це публічна сторінка: назвам приватних
# репозиторіїв тут не місце.
GRAPHQL = """
query($login: String!, $cursor: String, $size: Int!) {
  user(login: $login) {
    repositories(first: $size, after: $cursor, ownerAffiliations: OWNER, isFork: true,
                 privacy: PUBLIC, orderBy: {field: PUSHED_AT, direction: DESC}) {
      pageInfo { hasNextPage endCursor }
      nodes {
        name
        url
        description
        isArchived
        stargazerCount
        pushedAt
        createdAt
        primaryLanguage { name }
        repositoryTopics(first: 10) { nodes { topic { name } } }
        parent {
          nameWithOwner
          url
          description
          homepageUrl
          stargazerCount
          forkCount
          isArchived
          pushedAt
          licenseInfo { spdxId }
          primaryLanguage { name }
          repositoryTopics(first: 10) { nodes { topic { name } } }
        }
      }
    }
  }
}
"""


# --------------------------------------------------------------------------- #
# Отримання даних
# --------------------------------------------------------------------------- #

def get_token() -> str:
    for var in ("GITHUB_TOKEN", "GH_TOKEN"):
        if os.environ.get(var):
            return os.environ[var].strip()
    try:
        out = subprocess.run(
            ["gh", "auth", "token"], capture_output=True, text=True, timeout=15
        )
        if out.returncode == 0 and out.stdout.strip():
            return out.stdout.strip()
    except (OSError, subprocess.SubprocessError):
        pass
    sys.exit("Немає токена: задайте GITHUB_TOKEN або виконайте `gh auth login`.")


def graphql(query: str, variables: dict, token: str) -> dict:
    """Один запит до GraphQL з ретраями: GitHub стабільно віддає 502 на пікових вартостях."""
    body = json.dumps({"query": query, "variables": variables}).encode()
    request = urllib.request.Request(
        "https://api.github.com/graphql",
        data=body,
        headers={
            "Authorization": f"bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "forks-atlas",
        },
    )
    last = ""
    for attempt in range(4):
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                payload = json.load(response)
            if payload.get("errors"):
                sys.exit(f"GraphQL повернув помилку: {payload['errors']}")
            return payload["data"]
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as exc:
            last = str(exc)
            time.sleep(2 ** attempt)
    sys.exit(f"GraphQL недоступний після 4 спроб: {last}")


# Запит для записів із scripts/extra.json — проєктів, за якими стежимо без форку.
# Псевдонімами (r0, r1, …) кількадесят репозиторіїв беруться одним запитом
# замість окремого виклику на кожен.
EXTRA_QUERY = """
fragment RepoFields on Repository {
  name
  nameWithOwner
  url
  description
  homepageUrl
  stargazerCount
  forkCount
  isArchived
  pushedAt
  licenseInfo { spdxId }
  primaryLanguage { name }
  repositoryTopics(first: 10) { nodes { topic { name } } }
}
query {
%s
}
"""

EXTRA_BATCH = 25


def fetch_extra(names: list[str], token: str) -> list[dict]:
    """Дані про репозиторії, вказані як 'owner/name'."""
    found = []
    for start in range(0, len(names), EXTRA_BATCH):
        chunk = names[start:start + EXTRA_BATCH]
        aliases = []
        for index, full in enumerate(chunk):
            owner, _, name = full.partition("/")
            if not owner or not name:
                sys.exit(f"extra.json: очікується 'owner/name', отримано {full!r}")
            aliases.append(
                f'  r{index}: repository(owner: "{owner}", name: "{name}") '
                f"{{ ...RepoFields }}"
            )
        data = graphql(EXTRA_QUERY % "\n".join(aliases), {}, token)
        for index, full in enumerate(chunk):
            repo = data.get(f"r{index}")
            if repo:
                found.append(repo)
            else:
                print(f"  увага: {full} недоступний — пропущено")
    return found


def as_pseudo_fork(repo: dict) -> dict:
    """Обгортка, у якій репозиторій виступає власним оригіналом.

    Так класифікатор, мітки й рендеринг працюють без жодної окремої гілки:
    різниця між форком і просто відстежуваним проєктом зводиться до `url = None`.
    """
    return {
        "name": repo["name"],
        "url": None,
        "description": repo.get("description"),
        "isArchived": repo.get("isArchived", False),
        "createdAt": None,
        "primaryLanguage": repo.get("primaryLanguage"),
        "repositoryTopics": repo.get("repositoryTopics"),
        "parent": repo,
    }


def fetch_forks(token: str) -> list[dict]:
    forks, cursor = [], None
    while True:
        page = graphql(
            GRAPHQL, {"login": USER, "cursor": cursor, "size": PAGE_SIZE}, token
        )["user"]["repositories"]
        forks.extend(page["nodes"])
        if not page["pageInfo"]["hasNextPage"]:
            return forks
        cursor = page["pageInfo"]["endCursor"]


# --------------------------------------------------------------------------- #
# Класифікація
# --------------------------------------------------------------------------- #

def normalize(text: str) -> str:
    """Текст -> ' токен токен '.

    CamelCase спершу розбивається на слова, бо назви репозиторіїв часто злиті
    (`MachineLearningRoadmap`, `SecLists`) і без цього не дають жодного збігу.
    Обрамлення пробілами дає межі слів безкоштовно: ` ai ` більше не знаходиться
    всередині `email` чи `training`.
    """
    text = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", text)
    return " " + re.sub(r"[^0-9a-z]+", " ", text.lower()).strip() + " "


def haystack(repo: dict) -> str:
    parent = repo.get("parent") or {}
    topics = [
        node["topic"]["name"]
        for source in (repo, parent)
        for node in (source.get("repositoryTopics") or {}).get("nodes", [])
    ]
    parts = [
        repo.get("name") or "",
        repo.get("description") or "",
        parent.get("nameWithOwner") or "",
        parent.get("description") or "",
        " ".join(topics),
    ]
    return normalize(" ".join(parts))


def classify(repo: dict, overrides: dict) -> str:
    forced = overrides.get(repo["name"], {}).get("category")
    if forced:
        return forced
    hay = haystack(repo)
    for category in CATEGORIES:
        for keyword in category["keywords"]:
            if f" {normalize(keyword).strip()} " in hay:
                return category["key"]
    return OTHER["key"]


def badges(repo: dict, now: datetime) -> list[str]:
    parent = repo.get("parent")
    marks = []
    hay = haystack(repo)
    if (
        normalize(repo["name"]).startswith(" awesome ")
        or " awesome list " in hay
        or " curated list " in hay
        or " a list of " in hay
        or " collection of " in hay
    ):
        marks.append("list")
    if repo.get("url") is None:
        marks.append("linkonly")
    if not parent:
        marks.append("orphan")
        return marks
    if parent.get("isArchived") or repo.get("isArchived"):
        marks.append("archived")
    pushed = parent.get("pushedAt")
    if pushed and datetime.fromisoformat(pushed) < now - timedelta(days=STALE_DAYS):
        marks.append("stale")
    return marks


def build(forks: list[dict], overrides: dict, now: datetime) -> list[dict]:
    rows = []
    for repo in forks:
        parent = repo.get("parent") or {}
        override = overrides.get(repo["name"], {})
        rows.append(
            {
                "name": repo["name"],
                "url": repo.get("url"),
                "category": classify(repo, overrides),
                "upstream": parent.get("nameWithOwner"),
                "upstream_url": parent.get("url"),
                "description": parent.get("description") or repo.get("description") or "",
                "homepage": parent.get("homepageUrl"),
                "stars": parent.get("stargazerCount", 0),
                "language": (parent.get("primaryLanguage") or repo.get("primaryLanguage") or {}).get("name"),
                "license": (parent.get("licenseInfo") or {}).get("spdxId"),
                "upstream_pushed_at": parent.get("pushedAt"),
                "forked_at": repo.get("createdAt"),
                "badges": badges(repo, now),
                "note": override.get("note"),
            }
        )
    # Стабільне сортування за назвою: інакше кожен запуск переставляє рядки
    # і git-діф перестає показувати, що насправді змінилося.
    rows.sort(key=lambda r: r["name"].lower())
    return rows


# --------------------------------------------------------------------------- #
# Рендеринг
# --------------------------------------------------------------------------- #

def thousands(value: int) -> str:
    """72481 -> '72 481': без розділювача чотиризначні зірки читаються як шум."""
    return f"{value:,}".replace(",", " ")


def cell(text: str, limit: int = DESC_LIMIT) -> str:
    text = re.sub(r"\s+", " ", (text or "").strip())
    text = text.replace("|", "\\|").replace("<", "&lt;")
    if len(text) > limit:
        cut = text[:limit].rsplit(" ", 1)[0]
        text = cut + "…"
    return text or "—"


def render(rows: list[dict], now: datetime) -> str:
    order = [*CATEGORIES, OTHER]
    grouped = {c["key"]: [] for c in order}
    for row in rows:
        grouped.setdefault(row["category"], []).append(row)

    total = len(rows)
    forked = sum(1 for r in rows if r["url"])
    stars = sum(r["stars"] or 0 for r in rows)
    out: list[str] = []
    add = out.append

    add(f"# Атлас проєктів [@{USER}](https://github.com/{USER})")
    add("")
    add(
        f"Каталог **{total}** проєктів, за якими стежу: що це, звідки і навіщо тут. "
        "Оновлюється автоматично раз на тиждень."
    )
    add("")
    add(
        f"Більшість — форки ({forked}). Решта позначена 🔗: форк видалено або його "
        "не було, але сам проєкт лишається вартим уваги. Каталог переживає видалення "
        "форку — запис нікуди не зникає."
    )
    add("")
    add(
        f"`Записів: {total}` · `З них форків: {forked}` "
        f"· `Сумарно ★: {thousands(stars)}` · `Оновлено: {now:%d.%m.%Y}`"
    )
    add("")
    add("### Позначки")
    add("")
    for icon, meaning in BADGES.values():
        add(f"- {icon} — {meaning}")
    add("")
    add(
        "> Формат не є темою: awesome-список про безпеку лежить у розділі безпеки з міткою 📋, "
        "а не в загальному списку списків. Категорія відповідає на питання «про що це», "
        "мітка — «в якому це вигляді»."
    )
    add("")
    add("## Зміст")
    add("")
    for category in order:
        items = grouped.get(category["key"]) or []
        if items:
            add(f"- [{category['title']}](#cat-{category['key']}) — {len(items)}")
    add("")
    add("---")
    add("")

    for category in order:
        items = grouped.get(category["key"]) or []
        if not items:
            continue
        add(f'<a id="cat-{category["key"]}"></a>')
        add("")
        add(f"## {category['title']}")
        add("")
        add(category["blurb"])
        add("")
        add("| Проєкт | Оригінал | ★ | Мова | Що це |")
        add("| --- | --- | --: | --- | --- |")
        for row in sorted(items, key=lambda r: (-(r["stars"] or 0), r["name"].lower())):
            icons = "".join(BADGES[b][0] for b in row["badges"])
            # Без форку посилатися нікуди — лишається текст, а джерело
            # дає сусідня колонка. Мертвих посилань у каталозі не буває.
            name = f"[{row['name']}]({row['url']})" if row["url"] else row["name"]
            if icons:
                name = f"{name} {icons}"
            if row["upstream"]:
                upstream = f"[{row['upstream']}]({row['upstream_url']})"
            else:
                upstream = "—"
            description = cell(row["description"])
            if row["note"]:
                description = f"{description} **— {cell(row['note'], 120)}**"
            add(
                f"| {name} | {upstream} | {thousands(row['stars'] or 0)} "
                f"| {row['language'] or '—'} | {description} |"
            )
        add("")

    add("---")
    add("")
    add("## Як це працює")
    add("")
    add(
        "`scripts/update.py` тягне список форків через GitHub GraphQL, додає проєкти з "
        "`scripts/extra.json` (ті, за якими стежимо без форку), розкладає все за правилами "
        "(назва + опис + теми оригіналу) і перегенеровує цей файл разом із `data/forks.json`. "
        "Правила й тексти категорій лежать у самому скрипті, ручні виправлення — "
        "у `scripts/overrides.json`."
    )
    add("")
    add("Деталі, формат винятків і як додати категорію — у [docs/how-it-works.md](docs/how-it-works.md).")
    add("")
    return "\n".join(out)


# --------------------------------------------------------------------------- #
# Самоперевірка
# --------------------------------------------------------------------------- #

def _repo(name, description="", topics=(), parent_name="up/stream", parent_desc=None):
    return {
        "name": name,
        "url": f"https://github.com/{USER}/{name}",
        "description": description,
        "isArchived": False,
        "stargazerCount": 0,
        "pushedAt": "2026-01-01T00:00:00Z",
        "createdAt": "2026-01-01T00:00:00Z",
        "primaryLanguage": None,
        "repositoryTopics": {"nodes": [{"topic": {"name": t}} for t in topics]},
        "parent": {
            "nameWithOwner": parent_name,
            "url": f"https://github.com/{parent_name}",
            "description": parent_desc if parent_desc is not None else description,
            "homepageUrl": None,
            "stargazerCount": 0,
            "forkCount": 0,
            "isArchived": False,
            "pushedAt": "2026-01-01T00:00:00Z",
            "licenseInfo": None,
            "primaryLanguage": None,
            "repositoryTopics": {"nodes": []},
        },
    }


def self_test() -> None:
    no_overrides: dict = {}

    # Межі слів: 'ai' не має знаходитись усередині інших слів.
    assert " ai " in normalize("AI agents"), normalize("AI agents")
    assert " ai " not in normalize("email training Ukraine"), normalize("email training")
    # CamelCase розбивається, інакше жодне ключове слово не спрацює.
    assert " roadmap " in normalize("MachineLearningRoadmap")
    assert " lists " in normalize("SecLists")

    cases = [
        # Вузькі категорії мають вигравати у широкого «AI».
        (_repo("strix", "Open-source AI penetration testing tool", ["agents", "cybersecurity"]), "security"),
        (_repo("explorbot", "AI Agent for Exploratory Browser Testing", ["playwright", "qa-automation"]), "qa"),
        (_repo("nuclei", "Fast customizable vulnerability scanner", ["security"]), "security"),
        (_repo("playwright-utils", "A collection of utilities for Playwright tests", ["qa-team"]), "qa"),
        # Формат «awesome» не має підміняти тему.
        (_repo("awesome-agent-skills", "A curated collection of agent skills", ["awesome-list", "agent-skills"]), "skills"),
        (_repo("awesome-uses", "A list of /uses pages detailing developer setups"), "resources"),
        # Решта опорних точок.
        (_repo("vllm", "A high-throughput and memory-efficient inference and serving engine for LLMs"), "llm-infra"),
        (_repo("honcho", "Memory library for building stateful agents", ["agent-memory"]), "memory"),
        (_repo("openclaw", "Your own personal AI assistant. Any OS.", ["openclaw"]), "agents"),
        (_repo("travelagency-AZANIR-DOP", "travelagency created by GitHub Classroom"), "archive"),
        (_repo("mystery-box", ""), "other"),
    ]
    for repo, expected in cases:
        actual = classify(repo, no_overrides)
        assert actual == expected, f"{repo['name']}: очікували {expected}, отримали {actual}"

    # overrides мають перебивати правила.
    assert classify(_repo("nuclei", "vulnerability scanner"), {"nuclei": {"category": "qa"}}) == "qa"

    # Мітка списку і мітка «сплячого» оригіналу.
    now = datetime(2026, 7, 29, tzinfo=timezone.utc)
    assert "list" in badges(_repo("awesome-bash", "A curated list of scripts"), now)
    old = _repo("dead", "x")
    old["parent"]["pushedAt"] = "2020-01-01T00:00:00Z"
    assert "stale" in badges(old, now)
    orphan = _repo("gone", "x")
    orphan["parent"] = None
    assert badges(orphan, now) == ["orphan"]

    # Проєкт без форку: класифікується як звичайний запис, але позначається 🔗
    # і не отримує посилання на неіснуючий форк.
    tracked = as_pseudo_fork({
        "name": "authelia",
        "nameWithOwner": "authelia/authelia",
        "url": "https://github.com/authelia/authelia",
        "description": "Single Sign-On Multi-Factor portal for web apps",
        "homepageUrl": None,
        "stargazerCount": 1,
        "forkCount": 0,
        "isArchived": False,
        "pushedAt": "2026-07-01T00:00:00Z",
        "licenseInfo": None,
        "primaryLanguage": {"name": "Go"},
        "repositoryTopics": {"nodes": [{"topic": {"name": "authentication"}}]},
    })
    assert tracked["url"] is None
    assert "linkonly" in badges(tracked, now)
    assert classify(tracked, no_overrides) == "security"
    built = build([tracked], no_overrides, now)[0]
    assert built["upstream"] == "authelia/authelia" and built["url"] is None

    # Екранування таблиці: символ '|' не має ламати розмітку.
    assert cell("a | b") == "a \\| b"

    # Кожна категорія має унікальний ключ і непорожній опис.
    keys = [c["key"] for c in [*CATEGORIES, OTHER]]
    assert len(keys) == len(set(keys)), "дублікати ключів категорій"
    assert all(c["blurb"].strip() for c in [*CATEGORIES, OTHER]), "категорія без опису"

    print(f"Самоперевірка пройдена: {len(cases)} кейсів класифікації, {len(keys)} категорій.")


# --------------------------------------------------------------------------- #

def main() -> None:
    if "--self-test" in sys.argv:
        self_test()
        return

    overrides = json.loads(OVERRIDES.read_text(encoding="utf-8")) if OVERRIDES.exists() else {}
    extra_names = json.loads(EXTRA.read_text(encoding="utf-8")) if EXTRA.exists() else []
    now = datetime.now(timezone.utc)

    token = get_token()
    forks = fetch_forks(token)

    # Дедуплікація за оригіналом прибирає «день переходу»: поки форк існує,
    # запис приходить із нього; щойно форк видалено — з extra.json. Обидва
    # джерела можуть перелічувати той самий проєкт, дубля не буде.
    already = {
        (f.get("parent") or {}).get("nameWithOwner")
        for f in forks
        if f.get("parent")
    }
    wanted = [name for name in extra_names if name not in already]
    tracked = [as_pseudo_fork(r) for r in fetch_extra(wanted, token)] if wanted else []

    rows = build(forks + tracked, overrides, now)

    DATA.parent.mkdir(parents=True, exist_ok=True)
    DATA.write_text(
        json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    README.write_text(render(rows, now), encoding="utf-8")

    counts: dict[str, int] = {}
    for row in rows:
        counts[row["category"]] = counts.get(row["category"], 0) + 1
    print(f"Записів: {len(rows)}  (форків: {len(forks)}, лише посилань: {len(tracked)})")
    for category in [*CATEGORIES, OTHER]:
        if counts.get(category["key"]):
            print(f"  {counts[category['key']]:>4}  {category['title']}")


if __name__ == "__main__":
    main()
