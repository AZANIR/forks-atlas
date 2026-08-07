![Атлас проєктів @AZANIR — 301 проєкт](assets/readme/hero.svg)

Каталог проєктів, за якими стежу. Форків не тримаю: копія чужого репозиторію застаріває з першим же комітом в оригіналі, а посилання — ні. Розкладено по теках, оновлюється автоматично раз на тиждень.

<table>
  <tr>
    <td align="center" width="25%"><a href="docs/archive.md"><img src="assets/readme/folder-archive.svg" width="164" alt="Тека «Архів»"></a></td>
    <td align="center" width="25%"><a href="docs/security.md"><img src="assets/readme/folder-security.svg" width="164" alt="Тека «Безпека»"></a></td>
    <td align="center" width="25%"><a href="docs/qa.md"><img src="assets/readme/folder-qa.svg" width="164" alt="Тека «QA»"></a></td>
    <td align="center" width="25%"><a href="docs/skills.md"><img src="assets/readme/folder-skills.svg" width="164" alt="Тека «Skills»"></a></td>
  </tr>
  <tr>
    <td align="center" width="25%"><a href="docs/llm-infra.md"><img src="assets/readme/folder-llm-infra.svg" width="164" alt="Тека «LLM-інфра»"></a></td>
    <td align="center" width="25%"><a href="docs/memory.md"><img src="assets/readme/folder-memory.svg" width="164" alt="Тека «Пам'ять»"></a></td>
    <td align="center" width="25%"><a href="docs/media.md"><img src="assets/readme/folder-media.svg" width="164" alt="Тека «Медіа»"></a></td>
    <td align="center" width="25%"><a href="docs/agents.md"><img src="assets/readme/folder-agents.svg" width="164" alt="Тека «Агенти»"></a></td>
  </tr>
  <tr>
    <td align="center" width="25%"><a href="docs/devops.md"><img src="assets/readme/folder-devops.svg" width="164" alt="Тека «DevOps»"></a></td>
    <td align="center" width="25%"><a href="docs/resources.md"><img src="assets/readme/folder-resources.svg" width="164" alt="Тека «Ресурси»"></a></td>
    <td align="center" width="25%"><a href="docs/web.md"><img src="assets/readme/folder-web.svg" width="164" alt="Тека «Веб»"></a></td>
  </tr>
</table>

**Швидкий перехід** · [Архів](docs/archive.md) 4 · [Безпека](docs/security.md) 38 · [QA](docs/qa.md) 30 · [Skills](docs/skills.md) 47 · [LLM-інфра](docs/llm-infra.md) 17 · [Пам'ять](docs/memory.md) 24 · [Медіа](docs/media.md) 20 · [Агенти](docs/agents.md) 86 · [DevOps](docs/devops.md) 14 · [Ресурси](docs/resources.md) 13 · [Веб](docs/web.md) 8

### Позначки

- 📋 — куративний список
- ⚠️ — оригінал заархівовано
- 💤 — оригінал без комітів понад рік

> Формат не є темою: awesome-список про безпеку лежить у теці безпеки з міткою 📋, а не в окремому списку списків. Тека відповідає на питання «про що це», мітка — «в якому це вигляді».

---

## Як це працює

`scripts/update.py` тягне список форків через GitHub GraphQL, додає проєкти з `scripts/extra.json` (ті, за якими стежимо без форку), розкладає все за правилами і перегенеровує цю сторінку, теки в `docs/` та `data/forks.json`. Правила й тексти категорій лежать у самому скрипті, ручні виправлення — у `scripts/overrides.json`.

`301 проєкт` · `7 703 521 ★ сумарно` · `11 тек` · `оновлено 07.08.2026`

Деталі, формат винятків і як додати категорію — у [docs/how-it-works.md](docs/how-it-works.md).
