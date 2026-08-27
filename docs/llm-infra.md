![LLM-інфра — 19 проєктів](../assets/readme/window-llm-infra.svg)

# LLM-інфраструктура, гейтвеї та проксі

Шар під агентами: сервери інференсу, маршрутизатори моделей, проксі для економії токенів і локальні голосові моделі. Це те, що визначає вартість і швидкість усього, що вище. Форки тут — переважно про незалежність від одного провайдера: гейтвеї на 200+ моделей, локальний STT/TTS, обхід rate limit.

| Проєкт | Оригінал | ★ | Мова | Що це |
| --- | --- | --: | --- | --- |
| [vllm-project/vllm](https://github.com/vllm-project/vllm) 🔗 | — | 90 229 | Python | A high-throughput and memory-efficient inference and serving engine for LLMs |
| [rtk-ai/rtk](https://github.com/rtk-ai/rtk) 🔗 | — | 77 604 | Rust | CLI proxy that reduces LLM token consumption by 60-90% on common dev commands. Single Rust binary, zero dependencies |
| [unslothai/unsloth](https://github.com/unslothai/unsloth) 🔗 | — | 74 971 | Python | Local UI to run and train LLMs and diffusion models, including Qwen3.8, Kimi K3, MiniMax-H3, Gemma 4, DeepSeek-V4, FLUX and more. |
| [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) 🔗 | — | 67 799 | Python | Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers.… |
| [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) 🔗 | — | 56 761 | TypeScript | Never stop coding. Free MIT AI gateway: one endpoint, 350 providers (90+ free), 1200+ models Kimi, Claude, GPT, Gemini, GLM, DeepSeek, MiniMax. Works with Claude… |
| [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) 🔗 | — | 53 248 | Python | Open-Source Frontier Voice AI |
| [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) 🔗 | — | 50 781 | Python | Use Claude Code, Codex, Pi, and OpenCode and more for free (1.3B+ free tokens) from your terminal, app, IDE, or phone like OpenClaw (voice supported + ToS friendly) |
| [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) 🔗 | — | 48 976 | Go | Wrap Antigravity, ChatGPT Codex, Claude Code, Grok Build as an OpenAI/Gemini/Claude/Codex compatible API service, allowing you to enjoy the free Gemini 3.1 Pro, GPT… |
| [lbjlaq/Antigravity-Manager](https://github.com/lbjlaq/Antigravity-Manager) 🔗 | — | 30 767 | Rust | Professional Antigravity Account Manager & Switcher. One-click seamless account switching for Antigravity Tools. Built with Tauri v2 + React (Rust).专业的 Antigravity… **— не просто перемикач акаунтів: під капотом проксі-шлюз диспетчеризації запитів до AI-провайдерів** |
| [p-e-w/heretic](https://github.com/p-e-w/heretic) 🔗 | — | 28 182 | Python | Fully automatic censorship removal for language models |
| [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) 🔗 | — | 13 735 | Swift | Lightning-Fast, On-Device, Multilingual TTS — running natively via ONNX. |
| [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice) 🔗 | — | 10 968 | Swift | Fastest and only macOS Dictation app with on-device STT and custom trained AI enhancement model. Windows pre-build available! A local Wispr Flow alternative. DM us… |
| [FreeToken](https://github.com/AZANIR/FreeToken) | [FlashML-org/FreeToken](https://github.com/FlashML-org/FreeToken) | 8 810 | Python | — |
| [FareedKhan-dev/kimi-k3-in-c](https://github.com/FareedKhan-dev/kimi-k3-in-c) 🔗 | — | 6 578 | C | A 2.78-trillion-parameter Kimi K3 running inference on a single CPU in 8.24 GB of RAM. Portable C99: no BLAS, no framework, no GPU. |
| [automazeio/vibeproxy](https://github.com/automazeio/vibeproxy) 🔗 | — | 3 308 | Swift | Native macOS menu bar app to use your Claude Code & ChatGPT subscriptions with AI coding tools - no API keys needed |
| [liaohch3/claude-tap](https://github.com/liaohch3/claude-tap) 🔗 | — | 3 127 | Python | Intercept and inspect Coding Agent API traffic from Claude Code, Codex CLI, Gemini CLI, Cursor CLI, OpenCode, Kimi/Kimi Code, Pi, and Hermes in a local trace viewer. |
| [superlinked/sie](https://github.com/superlinked/sie) 🔗 | — | 2 832 | Python | Open-source inference server and production cluster for all the models your agent needs. |
| [smixs/iva-agent](https://github.com/smixs/iva-agent) 🔗 | — | 188 | TypeScript | AI assistant in Telegram that remembers everything and helps you run your life. Self-hosted in one command. |
| [cneuralnetwork/smol-kimi-k3](https://github.com/cneuralnetwork/smol-kimi-k3) 🔗 | — | 91 | Python | A 49M-parameter Kimi K3-inspired language model trainable on one 8GB GPU **— маленька Kimi K3 для тренування на одній 8GB GPU; без тем правила нічого не бачать** |

---

**Інші теки** · [Архів](archive.md) · [Безпека](security.md) · [QA](qa.md) · [Skills](skills.md) · [Пам'ять](memory.md) · [Медіа](media.md) · [Агенти](agents.md) · [DevOps](devops.md) · [Ресурси](resources.md) · [Веб](web.md)

[← На робочий стіл](../README.md)
