# Атлас проєктів [@AZANIR](https://github.com/AZANIR)

Каталог **286** проєктів, за якими стежу: що це, звідки і навіщо тут. Оновлюється автоматично раз на тиждень.

Форків не тримаю: копія чужого репозиторію застаріває з першим же комітом в оригіналі, а посилання — ні. Каталог веде до джерел і щотижня перевіряє, чи вони ще живі.

`Проєктів: 286` · `Сумарно ★: 7 342 994` · `Оновлено: 29.07.2026`

### Позначки

- 📋 — куративний список
- ⚠️ — оригінал заархівовано
- 💤 — оригінал без комітів понад рік

> Формат не є темою: awesome-список про безпеку лежить у розділі безпеки з міткою 📋, а не в загальному списку списків. Категорія відповідає на питання «про що це», мітка — «в якому це вигляді».

## Зміст

- [Навчальний архів і курсові проєкти](#cat-archive) — 4
- [Кібербезпека, OSINT і red team](#cat-security) — 37
- [QA та автоматизація тестування](#cat-qa) — 30
- [Agent Skills, субагенти та плагіни](#cat-skills) — 44
- [LLM-інфраструктура, гейтвеї та проксі](#cat-llm-infra) — 15
- [Пам'ять, контекст і RAG](#cat-memory) — 23
- [Медіа, контент і маркетинг](#cat-media) — 20
- [AI-агенти, harness'и та оркестрація](#cat-agents) — 78
- [DevOps, інфраструктура та мережі](#cat-devops) — 14
- [Ресурси, роадмапи та навчальні матеріали](#cat-resources) — 13
- [Веб, фронтенд і шаблони](#cat-web) — 8

---

<a id="cat-archive"></a>

## Навчальний архів і курсові проєкти

Курсові приклади й чужі profile-README, збережені колись як зразок оформлення. Робочої цінності не мають, але видаляти їх — це стирати власну історію. Тримаються окремо, щоб не засмічувати активні категорії. Навчальних завдань GitHub Classroom тут немає: вони приватні, а каталог свідомо показує лише публічне.

| Проєкт | ★ | Мова | Що це |
| --- | --: | --- | --- |
| [dimashyshkin/advanced-selenium-webdriver](https://github.com/dimashyshkin/advanced-selenium-webdriver) 💤 | 43 | HTML | Code examples for Advanced Selenium Webdriver course on Udemy |
| [jamesgeorge007/jamesgeorge007](https://github.com/jamesgeorge007/jamesgeorge007) | 35 | — | 🙌 **— профільний README іншої людини — форкнуто як приклад оформлення** |
| [ShyamPraveenSingh/ShyamPraveenSingh](https://github.com/ShyamPraveenSingh/ShyamPraveenSingh) 💤 | 5 | — | — |
| [LumenRvenu/LumenRvenu](https://github.com/LumenRvenu/LumenRvenu) 💤 | 0 | — | Config files for my GitHub profile. |

<a id="cat-security"></a>

## Кібербезпека, OSINT і red team

Класичний інструментарій безпеки поруч з новою хвилею AI-пентестерів. Тут і фундамент, який працює десятиліттями (ghidra, mitmproxy, nuclei, SecLists), і автономні агенти, що намагаються цей фундамент замінити (strix, shannon, pentagi). Тримати їх разом корисно саме для порівняння: видно, що AI поки додає шар зверху, а не витісняє базові сканери.

| Проєкт | ★ | Мова | Що це |
| --- | --: | --- | --- |
| [danielmiessler/SecLists](https://github.com/danielmiessler/SecLists) 📋 | 72 486 | PHP | SecLists is the security tester's companion. It's a collection of multiple types of lists used during security assessments, collected in one place. List types… |
| [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra) | 71 585 | Java | Ghidra is a software reverse engineering (SRE) framework |
| [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | 46 255 | TypeScript | Shannon is an autonomous, white-box AI pentester for web applications and APIs. It analyzes your source code, identifies attack vectors, and executes real exploits… |
| [usestrix/strix](https://github.com/usestrix/strix) | 45 564 | Python | Open-source AI penetration testing tool to find and fix your app’s vulnerabilities. |
| [mitmproxy/mitmproxy](https://github.com/mitmproxy/mitmproxy) | 44 498 | Python | An interactive TLS-capable intercepting HTTP proxy for penetration testers and software developers. |
| [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei) | 30 096 | Go | Nuclei is a fast, customizable vulnerability scanner powered by the global security community and built on a simple YAML-based DSL, enabling collaboration to tackle… |
| [authelia/authelia](https://github.com/authelia/authelia) | 28 385 | Go | The Single Sign-On Multi-Factor portal for web apps, now OpenID Certified™ |
| [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | 26 876 | Python | 817 structured cybersecurity skills for AI agents · Mapped to 6 frameworks: MITRE ATT&CK, NIST CSF 2.0, MITRE ATLAS, D3FEND, NIST AI RMF & MITRE F3 (Fight Fraud) ·… |
| [qeeqbox/social-analyzer](https://github.com/qeeqbox/social-analyzer) | 23 600 | JavaScript | API, CLI, and Web App for analyzing and finding a person's profile in 1000 social media \ websites |
| [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | 21 349 | Go | Fully autonomous AI Agents system capable of performing complex penetration testing tasks |
| [farhanashrafdev/90DaysOfCyberSecurity](https://github.com/farhanashrafdev/90DaysOfCyberSecurity) | 18 026 | — | This repository contains a 90-day cybersecurity study plan, along with resources and materials for learning various cybersecurity concepts and technologies. The… |
| [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | 13 935 | Python | Security scanner for AI agent skills. Detect vulnerabilities, malicious patterns, and security risks. |
| [awslabs/git-secrets](https://github.com/awslabs/git-secrets) | 13 358 | Shell | Prevents you from committing secrets and credentials into git repositories |
| [projectdiscovery/nuclei-templates](https://github.com/projectdiscovery/nuclei-templates) 📋 | 12 712 | JavaScript | Community curated list of templates for the nuclei engine to find security vulnerabilities. |
| [hslatman/awesome-threat-intelligence](https://github.com/hslatman/awesome-threat-intelligence) 📋 | 10 496 | — | A curated list of Awesome Threat Intelligence resources |
| [lissy93/awesome-privacy](https://github.com/lissy93/awesome-privacy) 📋 | 9 681 | Astro | 🦄 A curated list of privacy & security-focused software and services |
| [aliasrobotics/cai](https://github.com/aliasrobotics/cai) | 9 593 | Python | Cybersecurity AI (CAI), the framework for AI Security |
| [anchore/syft](https://github.com/anchore/syft) | 9 319 | Go | CLI tool and library for generating a Software Bill of Materials from container images and filesystems |
| [meirwah/awesome-incident-response](https://github.com/meirwah/awesome-incident-response) 📋 | 9 286 | — | A curated list of tools for incident response |
| [reddelexc/hackerone-reports](https://github.com/reddelexc/hackerone-reports) | 6 391 | Python | Top disclosed reports from HackerOne |
| [vavkamil/awesome-bugbounty-tools](https://github.com/vavkamil/awesome-bugbounty-tools) 📋 | 6 136 | — | A curated list of various bug bounty tools |
| [lanmaster53/recon-ng](https://github.com/lanmaster53/recon-ng) 💤 | 5 814 | Python | Open Source Intelligence gathering tool aimed at reducing the time spent harvesting information from open sources. |
| [onlurking/awesome-infosec](https://github.com/onlurking/awesome-infosec) 📋 | 5 716 | — | A curated list of awesome infosec courses and training resources. |
| [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST) | 5 292 | TypeScript | autonomous red teaming platform; multi-agent offensive-security meta-harness |
| [ShadowHackrs/gmail-account-creator](https://github.com/ShadowHackrs/gmail-account-creator) | 3 811 | Python | 🚀 Advanced automated Gmail account creation tool with anti-detection, phone verification bypass, 5sim integration, and beautiful modern interface. Create Gmail… **— інструмент обходу антифроду; тут як зразок технік, а не для використання** |
| [gadievron/raptor](https://github.com/gadievron/raptor) | 3 442 | Python | Raptor turns Claude Code into a general-purpose AI offensive/defensive security agent. By using Claude.md and creating rules, sub-agents, and skills, and… |
| [kaifcodec/user-scanner](https://github.com/kaifcodec/user-scanner) | 2 878 | Python | 🕵️‍♂️ (2-in-1) Email & Username OSINT suite for deep data extraction. Analyzes 360+ scan vectors (140+ email / 220+ username) for security research, investigations,… |
| [lkarlslund/Adalanche](https://github.com/lkarlslund/Adalanche) | 2 189 | Go | Attack Graph Visualizer and Explorer (Active Directory) ...Who's *really* Domain Admin? |
| [iknowjason/Awesome-CloudSec-Labs](https://github.com/iknowjason/Awesome-CloudSec-Labs) 📋 | 2 161 | — | Awesome free cloud native security learning labs. Includes CTF, self-hosted workshops, guided vulnerability labs, and research labs. |
| [TheGP/untidetect-tools](https://github.com/TheGP/untidetect-tools) | 1 860 | — | List of anti-detect and humanizing tools and browsers, including captcha solvers and sms-activation. |
| [PaulJerimy/SecCertRoadmapHTML](https://github.com/PaulJerimy/SecCertRoadmapHTML) 💤 | 1 171 | HTML | Security Certification Roadmap HTML5/CSS3 version |
| [bugbasesecurity/pentest-copilot](https://github.com/bugbasesecurity/pentest-copilot) | 1 135 | TypeScript | Pentest Copilot is an AI-powered browser based ethical hacking assistant tool designed to streamline pentesting workflows. |
| [HadessCS/Red-team-Interview-Questions](https://github.com/HadessCS/Red-team-Interview-Questions) 💤 | 769 | — | Red team Interview Questions |
| [ubikron/Awesome-AI-OSINT](https://github.com/ubikron/Awesome-AI-OSINT) 📋 | 734 | — | A list of articles, videos, and tools related to the use of AI for OSINT. |
| [UndeadSec/SwaggerSpy](https://github.com/UndeadSec/SwaggerSpy) | 315 | Python | Automated OSINT on SwaggerHub |
| [RojanSapkota/osint-terminal](https://github.com/RojanSapkota/osint-terminal) | 29 | Python | Self-hosted OSINT dashboard: 400+ keyless recon tools, a live 3D threat globe, and batch/case investigation workflows, no API keys required. |
| [ProwlrBot/CyberBox](https://github.com/ProwlrBot/CyberBox) | 13 | Python | CyberSandbox — all-in-one Docker security workspace with 160+ tools, dual AI, Caido proxy, and plugin marketplace |

<a id="cat-qa"></a>

## QA та автоматизація тестування

Профільний блок: фреймворки, бойлерплейти й утиліти для e2e, API та мобільного тестування. Частина форків — робочі інструменти (Playwright, Appium, mokapi, k6), частина — навчальні репозиторії часів опанування Cypress. Другі позначені як сплячі, але лишаються як приклади еволюції підходів.

| Проєкт | ★ | Мова | Що це |
| --- | --: | --- | --- |
| [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | 23 730 | TypeScript | Test your prompts, agents, and RAGs. Red teaming/pentesting/vulnerability scanning for AI. Compare performance of GPT, Claude, Gemini, DeepSeek, and more. Simple… **— правила відносять до безпеки через red teaming, але за суттю це тест-фреймворк для промптів** |
| [SonarSource/sonarqube](https://github.com/SonarSource/sonarqube) | 10 841 | Java | Continuous Inspection |
| [AirtestProject/Airtest](https://github.com/AirtestProject/Airtest) | 9 485 | Python | UI Automation Framework for Games and Apps |
| [refreshdotdev/web-eval-agent](https://github.com/refreshdotdev/web-eval-agent) ⚠️ | 1 240 | Python | An MCP server that autonomously evaluates web applications. |
| [akshayp7/playwright-typescript-playwright-test](https://github.com/akshayp7/playwright-typescript-playwright-test) | 716 | TypeScript | This is a boilerplate/template for a Playwright-Typescript framework for web UI, API, mobile emulation, DB, and visual testing. Docker image, SonarQube, Lighthouse,… |
| [AppiumTestDistribution/appium-device-farm](https://github.com/AppiumTestDistribution/appium-device-farm) | 617 | TypeScript | This is an Appium 2.0 plugin designed to manage and create driver sessions on available devices. |
| [currents-dev/playwright-best-practices-skill](https://github.com/currents-dev/playwright-best-practices-skill) | 341 | — | AI Skill for Playwright Best Practices—made by Currents.dev |
| [LambdaTest/agent-skills](https://github.com/LambdaTest/agent-skills) | 338 | Python | AI agent skills for TestMu AI (Formerly LambdaTest). |
| [JoanEsquivel/cypress-cucumber-boilerplate](https://github.com/JoanEsquivel/cypress-cucumber-boilerplate) 💤 | 109 | JavaScript | Cypress.IO Project using Javascript and Cucumber to start automating E2E tests just cloning it and installing dependencies. |
| [seontechnologies/playwright-utils](https://github.com/seontechnologies/playwright-utils) 📋 | 103 | TypeScript | A collection of utilities for Playwright tests at SEON Technologies, designed to make testing more efficient and maintainable. |
| [appclawhq/AppClaw](https://github.com/appclawhq/AppClaw) | 96 | TypeScript | AI-powered mobile automation agent — describe what you want in plain English, AppClaw reads the screen, reasons, and acts. LLM-agnostic, open-source, zero telemetry. |
| [bmad-code-org/bmad-method-test-architecture-enterprise](https://github.com/bmad-code-org/bmad-method-test-architecture-enterprise) | 87 | JavaScript | Test Architect Full BMad Method Enhancement |
| [testomatio/explorbot](https://github.com/testomatio/explorbot) | 61 | TypeScript | AI Agent for Exploratory Browser Testing |
| [marle3003/mokapi](https://github.com/marle3003/mokapi) | 57 | Go | Your API mocking tool for OpenAPI and AsyncAPI using Go and JavaScript - https://mokapi.io **— мок OpenAPI/AsyncAPI; правила плутають через тему ldap** |
| [403-html/the-qa-architecture-handbook](https://github.com/403-html/the-qa-architecture-handbook) | 18 | — | This guide provides a structured framework and practical advice for building a rock-solid, end-to-end QA architecture in an organization. |
| [deepakkamboj/playwright-ai-reporter](https://github.com/deepakkamboj/playwright-ai-reporter) | 4 | TypeScript | Playwright AI Reporter is an enterprise-grade, production-ready test reporter that combines artificial intelligence with comprehensive test automation workflows. |
| [sherlock1982/wdio-selenoid-boilerplate](https://github.com/sherlock1982/wdio-selenoid-boilerplate) 💤 | 4 | JavaScript | WebdriverIO 6 Selenoid boilerplate project with video support |
| [teosoph/cypress-cucumber___telnyx.com](https://github.com/teosoph/cypress-cucumber___telnyx.com) 💤 | 2 | JavaScript | This is a tutorial project for learning the Cypress and Cucumber frameworks. |
| [YegorMaksymchuk/ai-testing-demo](https://github.com/YegorMaksymchuk/ai-testing-demo) | 1 | — | Prototype for AI testing system |
| [Diankavoy19/Cypress-cucumber](https://github.com/Diankavoy19/Cypress-cucumber) 💤 | 1 | HTML | — |
| [MichalFidor/playswag](https://github.com/MichalFidor/playswag) | 1 | TypeScript | Playwright API coverage tracking against Swagger/OpenAPI specifications |
| [Cryzalis/Postman-newman-ghActions](https://github.com/Cryzalis/Postman-newman-ghActions) 💤 | 1 | — | — |
| [Cryzalis/cypress-telnyx.com](https://github.com/Cryzalis/cypress-telnyx.com) 💤 | 0 | JavaScript | — |
| [Andrey-Pivtorak/Cypress_Cucumber](https://github.com/Andrey-Pivtorak/Cypress_Cucumber) 💤 | 0 | JavaScript | The testing using cypress, cucumber, JavaScript, allure |
| [doktorgonza21/cypress_demo](https://github.com/doktorgonza21/cypress_demo) 💤 | 0 | JavaScript | — |
| [cri-us/Cypress_Typescript_e2e](https://github.com/cri-us/Cypress_Typescript_e2e) 💤 | 0 | TypeScript | — |
| [YegorMaksymchuk/k6-Grafana-InfluxDb-GitHubCopilot](https://github.com/YegorMaksymchuk/k6-Grafana-InfluxDb-GitHubCopilot) 💤 | 0 | JavaScript | How to start with Performance testing with k6 and GitHub Copilot |
| [MichalFidor/playswag-examples](https://github.com/MichalFidor/playswag-examples) | 0 | HTML | Real-world playswag API coverage examples — Swagger Petstore v3 with Playwright |
| [leraroy/playwright-ts](https://github.com/leraroy/playwright-ts) 💤 | 0 | TypeScript | — |
| [Andrey-Pivtorak/PlayWrightProject](https://github.com/Andrey-Pivtorak/PlayWrightProject) 💤 | 0 | TypeScript | — **— правила не бачать playwright у злитій назві PlayWrightProject — саме такі випадки й потрапляють у «Нерозібране»** |

<a id="cat-skills"></a>

## Agent Skills, субагенти та плагіни

Найшвидше зростаючий шар екосистеми: не самі агенти, а те, чим їх «озброюють». Skills, субагенти, плагіни й марketplace-каталоги для Claude Code, Codex, OpenClaw і Cursor. Цінність колекції тут не в кожному окремому репо, а в можливості порівняти, як різні команди описують одну й ту саму ідею — переносний набір інструкцій для агента.

| Проєкт | ★ | Мова | Що це |
| --- | --: | --- | --- |
| [obra/superpowers](https://github.com/obra/superpowers) | 263 172 | Shell | An agentic skills framework & software development methodology that works. |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | 235 433 | JavaScript | The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and… **— harness-система: skills, інстинкти, пам'ять і research-first підхід одним набором** |
| [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | 197 579 | — | A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls. |
| [mattpocock/skills](https://github.com/mattpocock/skills) | 194 350 | Shell | Skills for Real Engineers. Straight from my .agents directory. |
| [anthropics/skills](https://github.com/anthropics/skills) | 165 029 | Python | Public repository for Agent Skills |
| [garrytan/gstack](https://github.com/garrytan/gstack) | 125 140 | TypeScript | Use Garry Tan's exact Claude Code setup: 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA |
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | 111 415 | Python | An AI SKILL that provide design intelligence for building professional UI/UX multiple platforms |
| [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | 91 573 | JavaScript | Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote. |
| [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | 63 700 | HTML | from vibe coding to agentic engineering - practice makes claude perfect |
| [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | 61 310 | JavaScript | Extracted system prompts from Anthropic - Claude Fable 5, Opus 5, Claude Design, Claude Code. OpenAI - ChatGPT GPT-5.6-Sol, Codex. Google - Gemini 3.5 Flash, 3.1… |
| [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | 55 003 | Python | AI agent skill that researches any topic across Reddit, X, YouTube, HN, Polymarket, and the web - then synthesizes a grounded summary |
| [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) 📋 | 51 595 | — | The awesome collection of OpenClaw skills. 5,400+ skills filtered and categorized from the official OpenClaw Skills Registry.🦞 |
| [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | 44 131 | Python | AAS Core is the local, agent-first control plane for complete catalog discovery, agent-owned selection, stack validation, and planning, backed by 1,987+ agentic… |
| [wshobson/agents](https://github.com/wshobson/agents) | 38 354 | Python | Multi-harness agentic plugin marketplace for Claude Code, Codex CLI, Cursor, OpenCode, GitHub Copilot, and Gemini CLI |
| [github/awesome-copilot](https://github.com/github/awesome-copilot) 📋 | 37 198 | Python | Community-contributed instructions, agents, skills, and configurations to help you make the most of GitHub Copilot. |
| [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) 📋 | 31 644 | — | A community collection of OpenClaw use cases for making life easier. |
| [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | 30 355 | JavaScript | Use Codex from Claude Code to review code or delegate tasks. |
| [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) 📋 | 29 199 | — | A curated collection of 1000+ agent skills from official dev teams and the community, compatible with Claude Code, Codex, Gemini CLI, Cursor, and more. |
| [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | 26 936 | JavaScript | A Claude Code plugin that shows what's happening - context usage, active tools, running agents, and todo progress |
| [agentskills/agentskills](https://github.com/agentskills/agentskills) | 23 632 | Python | Specification and documentation for Agent Skills |
| [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | 23 598 | TypeScript | Official Compound Engineering plugin for Claude Code, Codex, Cursor, and more |
| [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | 23 482 | Shell | Turn Claude Code into a full game dev studio — 49 AI agents, 72 workflow skills, and a complete coordination system mirroring real studio hierarchy. |
| [emilkowalski/skills](https://github.com/emilkowalski/skills) | 22 470 | — | Skills for Design Engineers. |
| [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) 📋 | 17 497 | Python | A comprehensive collection of Agent Skills for context engineering, multi-agent architectures, and production agent systems. Use when building, optimizing, or… |
| [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) 📋 | 9 217 | JavaScript | A curated list of awesome plugins, themes, agents, projects, and resources for https://opencode.ai |
| [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | 9 157 | Python | GEO-first SEO skill for Claude Code. Comprehensive AI search optimization for any website — citability scoring, AI crawler analysis, brand authority, schema markup,… |
| [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | 6 858 | Python | Generate draw.io diagrams from natural language — 11 presets (UML, SysML/MBSE, BPMN, network, C4…), 36 tools: codebase/CI/infra-to-diagram, image→editable diagram,… |
| [dontriskit/awesome-ai-system-prompts](https://github.com/dontriskit/awesome-ai-system-prompts) 📋 | 6 111 | TypeScript | 🧠 Curated collection of system prompts for top AI tools. Perfect for AI agent builders and prompt engineers. Incuding: ChatGPT, Claude, Perplexity, Manus,… |
| [VoltAgent/awesome-codex-subagents](https://github.com/VoltAgent/awesome-codex-subagents) 📋 | 5 858 | — | A collection of 130+ specialized Codex subagents covering a wide range of development use cases. |
| [oso95/scroll-world](https://github.com/oso95/scroll-world) | 5 726 | JavaScript | A skill that turn any brand into a scrollable 3D world |
| [nyldn/claude-octopus](https://github.com/nyldn/claude-octopus) | 3 899 | Shell | Surface AI blindspots before you ship. Put up to 8 AI models on every research, design or coding task. |
| [op7418/Claude-to-IM-skill](https://github.com/op7418/Claude-to-IM-skill) | 2 835 | TypeScript | Bridge Claude Code / Codex to IM platforms — chat with AI coding agents from Telegram, Discord, or Feishu/Lark. |
| [zubair-trabzada/ai-marketing-claude](https://github.com/zubair-trabzada/ai-marketing-claude) | 2 233 | Python | AI Marketing Suite for Claude Code. 15 marketing skills with parallel subagents — audit any website, generate copy, email sequences, ad campaigns, content… |
| [iannuttall/claude-agents](https://github.com/iannuttall/claude-agents) ⚠️💤 | 2 052 | — | Custom subagents to use with Claude Code. |
| [plannotator/effective-html](https://github.com/plannotator/effective-html) | 1 440 | HTML | Agent skill for elegant and simple html plans, architecture diagrams, or whatever else you can think of. |
| [oil-oil/beautify-github-readme](https://github.com/oil-oil/beautify-github-readme) | 1 364 | Python | Design clear, theme-specific GitHub README homepages with SVG titles, real proof, and maintainable Markdown |
| [shang-zhu/violin](https://github.com/shang-zhu/violin) | 1 028 | Python | Open-source Video Translation Skill |
| [Kappaemme-git/codex-startup-pressure-test-skill](https://github.com/Kappaemme-git/codex-startup-pressure-test-skill) | 981 | JavaScript | — |
| [yetone/kill-ai-slop](https://github.com/yetone/kill-ai-slop) | 824 | TypeScript | A field guide to the visual & copy tics of AI-generated products — and an Agent Skill that scans your project and strips them out. https://killaislop.com |
| [LSTM-Kirigaya/openmcp-client](https://github.com/LSTM-Kirigaya/openmcp-client) | 754 | TypeScript | All in one vscode plugin for mcp developer |
| [smixs/visual-skills](https://github.com/smixs/visual-skills) | 113 | — | AI film director skills for Claude agents: cinematic dramaturgy (Murch, blocking, montage) + exact prompt syntax for Seedance 2.5, Kling 3.0 Turbo/Omni, Veo 3.1,… |
| [Houseofmvps/claude-rank](https://github.com/Houseofmvps/claude-rank) | 90 | JavaScript | Claude Code plugin that tells you why your site won't get cited by AI — and fixes the discoverability files automatically. 170+ rules across 10 scanners. |
| [genkovich/sdd](https://github.com/genkovich/sdd) | 78 | TypeScript | Spec-Driven Development for Claude Code: 12 atomic Socratic skills + a TDD implement engine (agent-team & dynamic-workflow modes) |
| [DimPa1966/creative-director-skill](https://github.com/DimPa1966/creative-director-skill) | 4 | — | AI Creative Director skill for Claude, GPT, Gemini — 20+ methodologies (SIT, TRIZ, Bisociation, SCAMPER), Cannes-calibrated scoring, recursive refinement. Insight →… |

<a id="cat-llm-infra"></a>

## LLM-інфраструктура, гейтвеї та проксі

Шар під агентами: сервери інференсу, маршрутизатори моделей, проксі для економії токенів і локальні голосові моделі. Це те, що визначає вартість і швидкість усього, що вище. Форки тут — переважно про незалежність від одного провайдера: гейтвеї на 200+ моделей, локальний STT/TTS, обхід rate limit.

| Проєкт | ★ | Мова | Що це |
| --- | --: | --- | --- |
| [vllm-project/vllm](https://github.com/vllm-project/vllm) | 87 587 | Python | A high-throughput and memory-efficient inference and serving engine for LLMs |
| [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | 73 835 | Rust | CLI proxy that reduces LLM token consumption by 60-90% on common dev commands. Single Rust binary, zero dependencies |
| [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | 63 172 | Python | Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers.… |
| [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | 51 182 | Python | Open-Source Frontier Voice AI |
| [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | 45 493 | Go | Wrap Antigravity, ChatGPT Codex, Claude Code, Grok Build as an OpenAI/Gemini/Claude/Codex compatible API service, allowing you to enjoy the free Gemini 3.1 Pro, GPT… |
| [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | 42 882 | Python | Use claude code, codex or pi for free from the terminal, IDE, or your phone like OpenClaw (voice supported) |
| [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | 33 956 | TypeScript | Never stop coding. Free MIT AI gateway: one endpoint, 290+ providers (90+ free), 500+ models — Kimi, Claude, GPT, OpenAI, Gemini, GLM, DeepSeek, MiniMax. Works with… |
| [lbjlaq/Antigravity-Manager](https://github.com/lbjlaq/Antigravity-Manager) | 30 251 | Rust | Professional Antigravity Account Manager & Switcher. One-click seamless account switching for Antigravity Tools. Built with Tauri v2 + React (Rust).专业的 Antigravity… **— не просто перемикач акаунтів: під капотом проксі-шлюз диспетчеризації запитів до AI-провайдерів** |
| [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) 📋 | 28 655 | Python | A list of free LLM inference resources accessible via API. |
| [p-e-w/heretic](https://github.com/p-e-w/heretic) | 26 912 | Python | Fully automatic censorship removal for language models |
| [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | 13 547 | Swift | Lightning-Fast, On-Device, Multilingual TTS — running natively via ONNX. |
| [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice) | 9 100 | Swift | Fastest and only macOS Dictation app with on-device STT and custom trained AI enhancement model. A local Wispr Flow alternative. ⭐ helps a ton :) Windows & iOS… |
| [automazeio/vibeproxy](https://github.com/automazeio/vibeproxy) | 3 241 | Swift | Native macOS menu bar app to use your Claude Code & ChatGPT subscriptions with AI coding tools - no API keys needed |
| [liaohch3/claude-tap](https://github.com/liaohch3/claude-tap) | 2 904 | Python | Intercept and inspect Coding Agent API traffic from Claude Code, Codex CLI, Gemini CLI, Cursor CLI, OpenCode, Kimi/Kimi Code, Pi, and Hermes in a local trace viewer. |
| [superlinked/sie](https://github.com/superlinked/sie) | 2 360 | Python | Open-source inference server and production cluster for all the models your agent needs. |

<a id="cat-memory"></a>

## Пам'ять, контекст і RAG

Відповідь індустрії на головне обмеження LLM — вікно контексту. Тут бібліотеки довготривалої пам'яті агентів, графи знань, RAG-фреймворки й інтеграції з Obsidian та NotebookLM. Практичний сенс форків: більшість проєктів у цій категорії ще не стабілізували API, тому власна копія — це страховка від ламких оновлень.

| Проєкт | ★ | Мова | Що це |
| --- | --: | --- | --- |
| [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | 98 313 | Python | Turn any codebase, with its docs, SQL schemas, configs, and PDFs, into a queryable knowledge graph. A /graphify skill for Claude Code, Cursor, Codex, and Gemini… |
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | 88 961 | JavaScript | Persistent Context Across Sessions for Every Agent – Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back… |
| [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | 76 700 | TypeScript | Graphs that teach > graphs that impress. Turn any code into an interactive knowledge graph you can explore, search, and ask questions about. Works with Claude Code,… |
| [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | 36 154 | TypeScript | An Open Source implementation of Notebook LM with more flexibility and features |
| [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | 35 649 | Rust | Your Personal AI super intelligence. A brain that builds a local-first memory of your life, a fantastic orchestrator of agent fleets and workflows, and a deep… |
| [NirDiamant/RAG_Techniques](https://github.com/NirDiamant/RAG_Techniques) | 28 865 | Jupyter Notebook | This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial. |
| [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | 25 962 | TypeScript | #1 Persistent memory for AI coding agents based on real-world benchmarks |
| [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | 22 468 | Python | "RAG-Anything: All-in-One RAG Framework" |
| [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | 18 321 | Python | Unofficial Python API and agentic skill for Google NotebookLM. Full programmatic access to NotebookLM's features—including capabilities the web UI doesn't… |
| [coleam00/context-engineering-intro](https://github.com/coleam00/context-engineering-intro) | 13 749 | Python | Context engineering is the new vibe coding - it's the way to actually make AI coding assistants work. Claude Code is the best for this so that's what this repo is… |
| [PleasePrompto/notebooklm-skill](https://github.com/PleasePrompto/notebooklm-skill) | 7 529 | Python | Use this skill to enable Claude Code to communicate directly with your Google NotebookLM notebooks. Query your uploaded documents and get source-grounded,… |
| [plastic-labs/honcho](https://github.com/plastic-labs/honcho) | 6 303 | Python | Memory library for building stateful agents |
| [jacob-bd/gemini-notebook-mcp-cli](https://github.com/jacob-bd/gemini-notebook-mcp-cli) | 5 671 | Python | Programmatic access to Gemini Notebook - via command-line interface (CLI), Model Context Protocol (MCP) server, and AI agent skills. |
| [breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind) | 4 116 | TypeScript | A self-organizing Obsidian vault that gives AI coding agents persistent memory. Claude Code, Codex CLI, Gemini CLI. |
| [OSU-NLP-Group/HippoRAG](https://github.com/OSU-NLP-Group/HippoRAG) | 3 895 | Python | [NeurIPS'24] HippoRAG is a novel RAG framework inspired by human long-term memory that enables LLMs to continuously integrate knowledge across external documents.… |
| [vanzan01/cursor-memory-bank](https://github.com/vanzan01/cursor-memory-bank) | 3 052 | — | A modular, documentation-driven framework using Cursor custom modes (VAN, PLAN, CREATIVE, IMPLEMENT) to provide persistent memory and guide AI through a structured… |
| [GitHamza0206/simba](https://github.com/GitHamza0206/simba) | 1 451 | TypeScript | OpenSource Production ready Customer service with built in Evals and monitoring |
| [coleam00/claude-memory-compiler](https://github.com/coleam00/claude-memory-compiler) | 1 260 | Python | Give Claude Code a memory that evolves with your codebase. Hooks automatically capture sessions, the Claude Agent SDK extracts key decisions and lessons, and an LLM… |
| [smixs/agent-second-brain](https://github.com/smixs/agent-second-brain) | 339 | Python | An always-on second brain you talk to. Voice notes in Telegram → typed, linked knowledge in your Obsidian vault. Runs 24/7 on the Claude subscription you already… **— правила чіпляються за слово voice, але це не голосовий стек, а конвеєр Telegram → Obsidian** |
| [AndyShaman/add_to_NotebookLM](https://github.com/AndyShaman/add_to_NotebookLM) | 148 | JavaScript | — **— букмарклет: кидає будь-яку сторінку в NotebookLM без ручного копіювання** |
| [coleam00/dark-factory-experiment](https://github.com/coleam00/dark-factory-experiment) | 113 | Python | AI chat app for conversational RAG over YouTube video transcripts |
| [smixs/autograph](https://github.com/smixs/autograph) | 54 | Python | Schema-as-code memory for AI agents in Obsidian: typed cards, entity dedup, link repair, update-in-place, and Ebbinghaus decay. Plain Markdown you own — a Claude… |
| [smixs/agent-memory-skill](https://github.com/smixs/agent-memory-skill) | 7 | Python | — |

<a id="cat-media"></a>

## Медіа, контент і маркетинг

Інструменти, що виробляють артефакт для людини, а не для рантайму: відео, презентації, діаграми, зображення, SEO-аналіз. Окрема категорія потрібна тому, що ці проєкти майже завжди агентні за реалізацією, але їхня цінність — у результаті, а не в архітектурі.

| Проєкт | ★ | Мова | Що це |
| --- | --: | --- | --- |
| [microsoft/markitdown](https://github.com/microsoft/markitdown) | 170 014 | Python | Python tool for converting files and office documents to Markdown. |
| [nexu-io/open-design](https://github.com/nexu-io/open-design) | 82 506 | TypeScript | 🎨 The open-source Claude Design alternative. 🖥️ Local-first desktop app. 🖼️ Your coding agent becomes the design engine: prototypes, landing pages, dashboards,… |
| [penpot/penpot](https://github.com/penpot/penpot) | 57 689 | Clojure | Penpot: The open-source design platform for Product teams that need scalable collaboration. |
| [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | 43 822 | Python | World's first open-source, agentic video production system. 12 production pipelines, 100+ tools, 700+ agent skill and production-knowledge files. Turn your AI… |
| [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | 41 811 | Python | AI turns documents or topics into real, native PowerPoint decks—with native shapes, transitions and animations, data-backed charts and tables on demand, audio… |
| [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) ⚠️ | 39 864 | TypeScript | Create stunning demos for free. Open-source, no subscriptions, no watermarks, and free for commercial use. An alternative to Screen Studio. |
| [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | 38 596 | TypeScript | Write HTML. Render video. Built for agents. |
| [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | 27 994 | Java | PDF Parser for AI-ready data. Automate PDF accessibility. Open-source. |
| [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | 27 355 | Rust | Privacy first, AI meeting assistant with 4x faster Parakeet/Whisper live transcription, speaker diarization, and Ollama summarization built on Rust. 100% local… **— правила чіпляються за privacy first, але це транскрибування зустрічей** |
| [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | 12 616 | Python | Give Claude the ability to watch any video. /watch downloads, extracts frames, transcribes, hands it all to Claude. |
| [XiaoYouChR/Ghost-Downloader-3](https://github.com/XiaoYouChR/Ghost-Downloader-3) | 7 629 | Python | An AI-boost cross-platform multi-protocol fluent-design concurrent downloader built with Python & Qt. |
| [persepolisdm/persepolis](https://github.com/persepolisdm/persepolis) | 7 428 | Python | Persepolis is a download manager written in Python. |
| [Yqnn/svg-path-editor](https://github.com/Yqnn/svg-path-editor) | 5 249 | TypeScript | Online editor to create and manipulate SVG paths |
| [oop7/YTSage](https://github.com/oop7/YTSage) | 4 334 | Python | Modern YouTube downloader with a clean PySide6 interface. Download videos in any quality, extract audio, fetch subtitles, sponsorBlock, and view video metadata.… |
| [walterlow/freecut](https://github.com/walterlow/freecut) | 1 898 | TypeScript | FreeCut is a professional-grade video editor that runs entirely in your browser. Professional video editing, zero installation. Create stunning videos with… |
| [perminder-klair/subwave](https://github.com/perminder-klair/subwave) | 1 074 | TypeScript | Personal internet radio: Agentic AI DJ **— агентне за реалізацією, але артефакт — ефір: AI-діджей добирає треки й говорить між ними** |
| [kizuna-ai-lab/sokuji](https://github.com/kizuna-ai-lab/sokuji) | 1 030 | TypeScript | Real-time two-way speech translation for bilingual meetings — auto-detects the spoken language and translates both directions, cloud or fully offline on-device.… |
| [techjarves/Uncensored-Local-Studio](https://github.com/techjarves/Uncensored-Local-Studio) | 759 | JavaScript | Uncensored local AI studio for Windows, Linux, and macOS. Zero-setup GUI for Image Generation, GGUF LLMs, Text to Speech & Speech to Text |
| [NathanRSmith/graphql-visualizer](https://github.com/NathanRSmith/graphql-visualizer) 💤 | 198 | JavaScript | — |
| [AgriciDaniel/seo-os](https://github.com/AgriciDaniel/seo-os) | 91 | TypeScript | SEO Office is a local-first SEO agency operating system. claw3d UI + claude-seo specialists + marketing-brain. Distributed as a private repo to a non-technical… |

<a id="cat-agents"></a>

## AI-агенти, harness'и та оркестрація

Ядро колекції й причина, чому вона взагалі така велика. Агентні фреймворки, harness'и навколо Claude Code / Codex / OpenClaw, дашборди для керування роями агентів, MCP-сервери. Категорія навмисно широка: у 2025–2026 межа між «фреймворком», «оболонкою» і «продуктом» розмита, і розділяти їх штучно означало б щотижня перекладати репозиторії з полиці на полицю.

| Проєкт | ★ | Мова | Що це |
| --- | --: | --- | --- |
| [openclaw/openclaw](https://github.com/openclaw/openclaw) | 384 474 | TypeScript | Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞 |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | 222 255 | Python | The agent that grows with you |
| [n8n-io/n8n](https://github.com/n8n-io/n8n) | 198 561 | TypeScript | Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations. |
| [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | 194 942 | Rust | An agent-managed museum exhibit, built in Rust with Gajae-Code / LazyCodex — developed and maintained with no human intervention. |
| [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | 137 420 | Shell | A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized… |
| [github/spec-kit](https://github.com/github/spec-kit) | 124 468 | Python | 💫 Toolkit to help you get started with Spec-Driven Development |
| [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | 92 331 | Python | AI agents running research on single-GPU nanochat training automatically |
| [lobehub/lobehub](https://github.com/lobehub/lobehub) | 80 959 | TypeScript | 🤯 LobeHub is your Chief Agent Operator, organizing your agents into 7×24 operations by hiring, scheduling, and reporting on your entire AI team. |
| [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | 75 075 | TypeScript | The open-source app everyone uses to manage agents at work |
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | 66 483 | TypeScript | 🌊 The leading agent meta-harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive… |
| [santifer/career-ops](https://github.com/santifer/career-ops) | 62 157 | JavaScript | Open-source AI job search: scan job portals, evaluate listings with a structured A-F rubric into a 1.0-5.0 score, tailor your CV, track applications — runs locally… |
| [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | 51 256 | JavaScript | Breakthrough Method for Agile Ai Driven Development |
| [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | 46 381 | Python | Ultra-lightweight, open-source, self-hosted personal AI agent framework in Python with WebUI, tools, memory, MCP, multi-agent workflows, automation, and chat apps |
| [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | 46 289 | Python | "CLI-Anything: Making ALL Software Agent-Native" -- CLI-Hub: https://clianything.cc/ |
| [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | 39 499 | Rust | Browser automation CLI for AI agents |
| [stablyai/orca](https://github.com/stablyai/orca) | 32 615 | TypeScript | Orca is the ADE for working with a fleet of parallel agents. Run any coding agent with your own subscription. Available on desktop, mobile and VPS. |
| [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | 30 549 | TypeScript | Clone any website with one command using AI coding agents |
| [simstudioai/sim](https://github.com/simstudioai/sim) | 29 233 | TypeScript | Build, deploy, and orchestrate AI agents. Sim is the central intelligence layer for your AI workforce. |
| [ScrapeGraphAI/Scrapegraph-ai](https://github.com/ScrapeGraphAI/Scrapegraph-ai) | 28 778 | Python | Python scraper based on AI |
| [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | 28 393 | Python | Build and run agents you can see, understand and trust. |
| [oraios/serena](https://github.com/oraios/serena) | 27 161 | Python | A powerful MCP toolkit for coding, providing semantic retrieval and editing capabilities - the IDE for your agent **— семантичний пошук по коду через LSP — дає агенту навігацію рівня IDE замість grep** |
| [openai/symphony](https://github.com/openai/symphony) | 26 301 | Elixir | Symphony turns project work into isolated, autonomous implementation runs, allowing teams to manage work instead of supervising coding agents. |
| [karpathy/llm-council](https://github.com/karpathy/llm-council) | 23 337 | Python | LLM Council works together to answer your hardest questions |
| [agentsmd/agents.md](https://github.com/agentsmd/agents.md) | 23 296 | TypeScript | AGENTS.md — a simple, open format for guiding coding agents |
| [czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp) | 22 441 | TypeScript | A MCP for Claude Desktop / Claude Code / Windsurf / Cursor to build n8n workflows for you |
| [dyad-sh/dyad](https://github.com/dyad-sh/dyad) | 21 074 | TypeScript | Local, open-source AI app builder for power users ✨ v0 / Lovable / Replit / Bolt alternative 🌟 Star if you like it! |
| [trycua/cua](https://github.com/trycua/cua) | 20 759 | HTML | Scale computer-use 2.0 with open-source drivers, cross-OS fleets, and benchmarks for training, evaluation, and data generation. |
| [iii-hq/iii](https://github.com/iii-hq/iii) | 18 530 | Rust | Effortlessly compose, extend, and observe every service in real-time for the first time ever. |
| [rowboatlabs/rowboat](https://github.com/rowboatlabs/rowboat) | 16 877 | TypeScript | Open-source AI coworker, with memory |
| [block/buzz](https://github.com/block/buzz) | 16 760 | Rust | A hive mind communication platform **— спільний простір, де люди й агенти працюють над задачею на власному релеї** |
| [AndyMik90/Aperant](https://github.com/AndyMik90/Aperant) | 14 491 | TypeScript | Autonomous multi-session AI coding |
| [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | 13 920 | Python | Fully autonomous & self-evolving research from idea to paper. Chat an Idea. Get a Paper. 🦞 |
| [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | 13 623 | TypeScript | Desktop Companion for Hermes Agent |
| [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) | 12 093 | TypeScript | 🚀 Beautiful highly customizable statusline for Claude Code CLI with powerline support, themes, and more. |
| [oblien/openship](https://github.com/oblien/openship) | 9 692 | TypeScript | Self-hosted deployment platform |
| [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | 9 586 | JavaScript | Practical patterns, starters & CLI tools for loop engineering with AI coding agents. Design systems that prompt and orchestrate agents (inspired by Addy Osmani and… |
| [pixel-agents-hq/pixel-agents](https://github.com/pixel-agents-hq/pixel-agents) | 8 739 | TypeScript | Pixel office. |
| [Maciek-roboblog/Claude-Code-Usage-Monitor](https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor) | 8 543 | Python | Real-time Claude Code usage monitor with predictions and warnings |
| [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | 8 299 | Python | "ClawWork: OpenClaw as Your AI Coworker - 💰 $15K earned in 11 Hours" |
| [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | 8 109 | Python | Personal AI, On Personal Devices |
| [vudovn/ag-kit](https://github.com/vudovn/ag-kit) | 8 074 | TypeScript | — **— агентний кіт для Antigravity; в оригіналі немає ні опису, ні тем, тому правила його не бачать** |
| [CodebuffAI/codebuff](https://github.com/CodebuffAI/codebuff) | 8 074 | TypeScript | Generate code from the terminal! |
| [pickle-com/glass](https://github.com/pickle-com/glass) | 7 560 | JavaScript | Digital Mind Extension |
| [ringhyacinth/Star-Office-UI](https://github.com/ringhyacinth/Star-Office-UI) | 7 400 | HTML | A pixel office for your OpenClaw: turn invisible work states into a cozy little space with characters, daily notes, and guest agents. Code under MIT; art assets for… |
| [craft-ai-agents/craft-agents-oss](https://github.com/craft-ai-agents/craft-agents-oss) | 6 974 | TypeScript | — |
| [coleam00/ottomator-agents](https://github.com/coleam00/ottomator-agents) | 5 699 | Python | All the open source AI Agents hosted on the oTTomator Live Agent Studio platform! |
| [HKUDS/ClawTeam](https://github.com/HKUDS/ClawTeam) | 5 452 | Python | "ClawTeam: Agent Swarm Intelligence" (One Command → Full Automation) |
| [buildermethods/agent-os](https://github.com/buildermethods/agent-os) | 5 137 | Shell | Agent OS is a system for injecting your codebase standards and writing better specs for spec-driven development. |
| [kevinrgu/autoagent](https://github.com/kevinrgu/autoagent) | 4 558 | Python | autonomous harness engineering |
| [abhi1693/openclaw-mission-control](https://github.com/abhi1693/openclaw-mission-control) | 4 102 | TypeScript | AI Agent Orchestration Dashboard - Manage AI agents, assign tasks, and coordinate multi-agent collaboration via OpenClaw Gateway. |
| [kyrolabs/awesome-agents](https://github.com/kyrolabs/awesome-agents) 📋 | 2 672 | — | 🤖 Awesome list of AI Agents |
| [plexe-ai/plexe](https://github.com/plexe-ai/plexe) | 2 592 | Python | ✨ Build a machine learning model from a prompt |
| [nusquama/n8nworkflows.xyz](https://github.com/nusquama/n8nworkflows.xyz) | 2 461 | — | N8N Workflows Catalog |
| [grp06/openclaw-studio](https://github.com/grp06/openclaw-studio) | 2 031 | TypeScript | A clean web dashboard for OpenClaw. Connect your Gateway, manage agents, and ship faster. ⭐️ Star if you like it! |
| [virattt/ai-financial-agent](https://github.com/virattt/ai-financial-agent) | 2 016 | TypeScript | A financial agent for investment research |
| [hyperspaceai/agi](https://github.com/hyperspaceai/agi) | 2 013 | — | The first distributed AGI system. Thousands of autonomous AI agents collaboratively train models, share experiments via P2P gossip, and push breakthroughs here.… |
| [xmanrui/OpenClaw-bot-review](https://github.com/xmanrui/OpenClaw-bot-review) | 2 011 | TypeScript | A lightweight web dashboard for viewing all your OpenClaw Bots/Agents/Models/Sessions status at a glance. |
| [Pickle-Pixel/ApplyPilot](https://github.com/Pickle-Pixel/ApplyPilot) | 1 357 | Python | AI agent that applies to jobs for you. Any site. Any form. |
| [firecrawl/open-scouts](https://github.com/firecrawl/open-scouts) | 1 341 | TypeScript | 🔥 AI-powered web monitoring platform. Create automated scouts that search the web and send email alerts when they find what you're looking for. |
| [andyrewlee/awesome-agent-orchestrators](https://github.com/andyrewlee/awesome-agent-orchestrators) 📋 | 1 157 | — | List of agent orchestrators |
| [iannuttall/mcp-boilerplate](https://github.com/iannuttall/mcp-boilerplate) | 1 023 | TypeScript | A remote Cloudflare MCP server boilerplate with user authentication and Stripe for paid tools. |
| [daggerhashimoto/openclaw-nerve](https://github.com/daggerhashimoto/openclaw-nerve) | 856 | TypeScript | Real-time web cockpit for OpenClaw: voice conversations, agent automated kanban board, workspace/file control, sub-agent sessions, inline charts, and usage… |
| [openswarm-ai/openswarm](https://github.com/openswarm-ai/openswarm) | 784 | Python | Your mission control center for a swarm of Ai agents. |
| [phioranex/openclaw-docker](https://github.com/phioranex/openclaw-docker) | 687 | Shell | — |
| [ShenSeanChen/waku-agent](https://github.com/ShenSeanChen/waku-agent) | 607 | Python | Waku Waku! Waku agent is your personal AI agent, on your own laptop, in code you can read in an afternoon — harness + loop + memory + eval |
| [yashab-cyber/opendroid](https://github.com/yashab-cyber/opendroid) | 497 | Kotlin | Your Open Autonomous Android Agent — A production-ready, self-planning AI assistant powered by local/remote LLMs and accessibility-driven screen automation. |
| [paulrobello/claude-office](https://github.com/paulrobello/claude-office) | 474 | TypeScript | Real-time pixel art office simulation that visualizes Claude Code operations |
| [eggent-ai/eggent](https://github.com/eggent-ai/eggent) | 320 | TypeScript | AI agent your mom can use. |
| [ErwanLorteau/BMAD_Openclaw](https://github.com/ErwanLorteau/BMAD_Openclaw) | 311 | TypeScript | Bridging the BMad Method to OpenClaw — Structured AI-driven development workflows. |
| [EpicStaff/EpicStaff](https://github.com/EpicStaff/EpicStaff) | 270 | Python | Source-available, self-hosted platform for building AI agent flows - visual editor over a Django backend. |
| [3DCF-Labs/safepilot](https://github.com/3DCF-Labs/safepilot) | 249 | Rust | AI assistant that executes real work, safely. |
| [iannuttall/task-magic](https://github.com/iannuttall/task-magic) ⚠️💤 | 241 | — | A complete task management system using Cursor/Windsurf rules |
| [geezerrrr/agent-town](https://github.com/geezerrrr/agent-town) | 224 | TypeScript | A pixel-art AI agent online collaboration platform. |
| [nikok6/herdr-mirror](https://github.com/nikok6/herdr-mirror) | 82 | Rust | Unify your local and remote sessions in one window: mirror remote herdr servers into your local sidebar and drive them over SSH **— дзеркалить агентів з віддалених машин в одну панель — видно, хто працює, хто заблокований, хто завершив** |
| [karem505/openclaw-agent-dashboard](https://github.com/karem505/openclaw-agent-dashboard) | 49 | HTML | Glassmorphic agent management dashboard for OpenClaw |
| [noblehacks/frenemy](https://github.com/noblehacks/frenemy) | 25 | JavaScript | I got tired of copy pasting between Claude and Codex, so I made them talk to each other. No API keys, just the subscriptions you already pay for. |
| [MattMagg/clawdash](https://github.com/MattMagg/clawdash) | 13 | TypeScript | Real-time control plane for OpenClaw — monitor, manage, and configure AI agents and gateway from a single dashboard. **— панель керування, а не інфраструктура — слово gateway в описі збиває правила** |
| [Namreg-gami/agent-cockpit](https://github.com/Namreg-gami/agent-cockpit) | 1 | Python | Local-first operational dashboard for Hermes Agent profiles. |

<a id="cat-devops"></a>

## DevOps, інфраструктура та мережі

Контейнери, Kubernetes, Terraform, мережеві утиліти й самохостинг. Помітно менший блок, ніж AI, і це чесно відображає зміщення фокусу: інфраструктурні форки здебільшого 2021–2024 років, тоді як AI-шар — останнього року.

| Проєкт | ★ | Мова | Що це |
| --- | --: | --- | --- |
| [ripienaar/free-for-dev](https://github.com/ripienaar/free-for-dev) 📋 | 130 762 | HTML | A list of SaaS, PaaS and IaaS offerings that have free tiers of interest to devops and infradev |
| [jdx/mise](https://github.com/jdx/mise) | 31 288 | Rust | dev tools, env vars, task runner **— заміна asdf/nvm/pyenv одним бінарником — керує і версіями інструментів, і env, і тасками** |
| [basecamp/omarchy](https://github.com/basecamp/omarchy) | 24 170 | Shell | Beautiful, Modern & Opinionated Linux |
| [milanm/DevOps-Roadmap](https://github.com/milanm/DevOps-Roadmap) | 19 984 | — | DevOps Roadmap for 2026. with learning resources |
| [sqshq/sampler](https://github.com/sqshq/sampler) 💤 | 14 717 | Go | Tool for shell commands execution, visualization and alerting. Configured with a simple YAML file. |
| [awesome-lists/awesome-bash](https://github.com/awesome-lists/awesome-bash) 📋 | 9 961 | Shell | A curated list of delightful Bash scripts and resources. |
| [remote-android/redroid-doc](https://github.com/remote-android/redroid-doc) | 6 627 | Shell | redroid (Remote-Android) is a multi-arch, GPU enabled, Android in Cloud solution. Track issues / docs here |
| [pshenok/server-survival](https://github.com/pshenok/server-survival) | 6 232 | JavaScript | Tower defense game that teaches cloud architecture. Build infrastructure, survive traffic, learn scaling. |
| [lissy93/networking-toolbox](https://github.com/lissy93/networking-toolbox) | 2 619 | Svelte | 🛜 100+ offline-first networking tools and utilities |
| [Manoj-engineer/k8squest](https://github.com/Manoj-engineer/k8squest) | 1 426 | Shell | K8sQuest — A local, hands-on Kubernetes learning game with real-world troubleshooting challenges. Practice Pods, Deployments, Services, networking, storage, and… |
| [karam-ajaj/atlas](https://github.com/karam-ajaj/atlas) | 1 279 | JavaScript | Open-source tool for network discovery, visualization, and monitoring. Built with Go, FastAPI, and React, supports Docker host scanning. |
| [AmineDjeghri/personal-os-setup](https://github.com/AmineDjeghri/personal-os-setup) | 597 | Python | An app and guide to easily configure Windows, Linux, MacOS, Google TV, Stremio, Home Assistant and more (including WSL2, GPU drivers & development tools). Improve… |
| [AlariCode/docker-demo](https://github.com/AlariCode/docker-demo) 💤 | 43 | TypeScript | — |
| [dimdimuzun/LearningTerraform](https://github.com/dimdimuzun/LearningTerraform) 💤 | 0 | HCL | — |

<a id="cat-resources"></a>

## Ресурси, роадмапи та навчальні матеріали

Курировані списки й дорожні карти, що не належать жодній технічній категорії напряму. Зверніть увагу: тематичні awesome-списки (наприклад, про безпеку чи агентів) лежать не тут, а у своїх категоріях із міткою 📋 — формат не є темою.

| Проєкт | ★ | Мова | Що це |
| --- | --: | --- | --- |
| [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) 📋💤 | 235 741 | — | A collection of inspiring lists, manuals, cheatsheets, blogs, hacks, one-liners, cli/web tools and more. |
| [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | 40 652 | Python | A visual, example-driven guide to Claude Code — from basic concepts to advanced agents, with copy-paste templates that bring immediate value. |
| [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | 26 119 | Python | 《深入理解 AI Agent：设计原理与工程实践》（李博杰 著）开源主仓库：全书正文、编译版 PDF 与按章配套代码 **— книга китайською; цінна саме розділами про пам'ять і контекст, код доданий покроково** |
| [karpathy/nn-zero-to-hero](https://github.com/karpathy/nn-zero-to-hero) 💤 | 23 772 | Jupyter Notebook | Neural Networks: Zero to Hero |
| [NirDiamant/GenAI_Agents](https://github.com/NirDiamant/GenAI_Agents) | 23 533 | Jupyter Notebook | 50+ tutorials and implementations for Generative AI Agent techniques, from basic conversational bots to complex multi-agent systems. |
| [NirDiamant/agents-towards-production](https://github.com/NirDiamant/agents-towards-production) | 21 202 | Jupyter Notebook | End-to-end, code-first tutorials for building production-grade GenAI agents. From prototype to enterprise deployment. |
| [wesbos/awesome-uses](https://github.com/wesbos/awesome-uses) 📋 | 5 288 | JavaScript | A list of /uses pages detailing developer setups, gear, software and configs. |
| [Sumanth077/Hands-On-AI-Engineering](https://github.com/Sumanth077/Hands-On-AI-Engineering) 📋 | 2 826 | Python | A curated collection of practical AI projects implementing OCR systems, RAG, AI agents, and other AI use cases. |
| [digitalknk/openclaw-runbook](https://github.com/digitalknk/openclaw-runbook) | 1 104 | Astro | Unofficial OpenClaw runbook for running agents day to day without burning money, exposing your gateway, or trusting random automation. **— найкорисніше в колекції з експлуатації: як не спалити бюджет і не відкрити гейтвей назовні** |
| [GnuriaN/format-README](https://github.com/GnuriaN/format-README) | 1 039 | — | Формат файла README |
| [nexu-io/harness-engineering-guide](https://github.com/nexu-io/harness-engineering-guide) | 583 | TypeScript | 🔧 The open guide to Harness Engineering — concepts, tutorials, papers, tools, and resources for building and managing AI agent runtimes. |
| [justxor/MachineLearningRoadmap](https://github.com/justxor/MachineLearningRoadmap) | 322 | — | Полный Roadmap по машинному обучению 2026 |
| [coleam00/evolution-of-ai-agents](https://github.com/coleam00/evolution-of-ai-agents) | 36 | Python | Three working examples showing how AI agent development evolved - from traditional RAG to batteries-included SDKs and skill-based frameworks |

<a id="cat-web"></a>

## Веб, фронтенд і шаблони

Стартові шаблони, генератори статичних сайтів і фронтенд-утиліти. Найстаріший шар колекції — здебільшого форки-заготовки, збережені «щоб було з чого почати», коли така потреба виникне.

| Проєкт | ★ | Мова | Що це |
| --- | --: | --- | --- |
| [tw93/Pake](https://github.com/tw93/Pake) | 60 308 | Rust | 🤱🏻 Turn any webpage into a desktop app with one command. |
| [CorentinTh/it-tools](https://github.com/CorentinTh/it-tools) 📋 | 39 993 | Vue | Collection of handy online tools for developers, with great UX. |
| [birobirobiro/awesome-shadcn-ui](https://github.com/birobirobiro/awesome-shadcn-ui) 📋 | 20 182 | TypeScript | A curated list of awesome things related to shadcn/ui. |
| [vladilenm/astro-cc](https://github.com/vladilenm/astro-cc) 💤 | 8 | Astro | — |
| [andberry/berry-11ty](https://github.com/andberry/berry-11ty) 💤 | 5 | SCSS | Eleventy (11ty) playground with multi-sections landing pages setup, and Frontend workflow (Scss, JS es6+) implemented with gulp |
| [ZennoHelpers/ZennoPoster-project-template](https://github.com/ZennoHelpers/ZennoPoster-project-template) ⚠️💤 | 5 | C# | Проект ZennoPoster для IDE (C# и F#) |
| [mentorchita/my_yourname_site](https://github.com/mentorchita/my_yourname_site) | 3 | SCSS | — |
| [isNan909/11tyblog-theme](https://github.com/isNan909/11tyblog-theme) 💤 | 2 | Nunjucks | A Static site generator blog template made with 11ty. |

---

## Як це працює

`scripts/update.py` тягне список форків через GitHub GraphQL, додає проєкти з `scripts/extra.json` (ті, за якими стежимо без форку), розкладає все за правилами (назва + опис + теми оригіналу) і перегенеровує цей файл разом із `data/forks.json`. Правила й тексти категорій лежать у самому скрипті, ручні виправлення — у `scripts/overrides.json`.

Деталі, формат винятків і як додати категорію — у [docs/how-it-works.md](docs/how-it-works.md).
