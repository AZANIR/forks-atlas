![LLM-інфра — 17 проєктів](../assets/readme/window-llm-infra.svg)

# LLM-інфраструктура, гейтвеї та проксі

Шар під агентами: сервери інференсу, маршрутизатори моделей, проксі для економії токенів і локальні голосові моделі. Це те, що визначає вартість і швидкість усього, що вище. Форки тут — переважно про незалежність від одного провайдера: гейтвеї на 200+ моделей, локальний STT/TTS, обхід rate limit.

| Проєкт | ★ | Мова | Що це |
| --- | --: | --- | --- |
| [vllm-project/vllm](https://github.com/vllm-project/vllm) | 88 431 | Python | A high-throughput and memory-efficient inference and serving engine for LLMs |
| [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | 75 142 | Rust | CLI proxy that reduces LLM token consumption by 60-90% on common dev commands. Single Rust binary, zero dependencies |
| [unslothai/unsloth](https://github.com/unslothai/unsloth) | 69 679 | Python | Unsloth is a local UI for training and running Kimi K3, Gemma 4, Qwen3.6, DeepSeek-V4, GLM and other models. |
| [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | 65 340 | Python | Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers.… |
| [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | 52 132 | Python | Open-Source Frontier Voice AI |
| [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | 46 460 | Go | Wrap Antigravity, ChatGPT Codex, Claude Code, Grok Build as an OpenAI/Gemini/Claude/Codex compatible API service, allowing you to enjoy the free Gemini 3.1 Pro, GPT… |
| [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | 44 706 | Python | Use Claude Code, Codex and Pi for free from your terminal, app, IDE, or phone like OpenClaw (voice supported) |
| [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | 42 172 | TypeScript | Never stop coding. Free MIT AI gateway: one endpoint, 290+ providers (90+ free), 500+ models — Kimi, Claude, GPT, OpenAI, Gemini, GLM, DeepSeek, MiniMax. Works with… |
| [lbjlaq/Antigravity-Manager](https://github.com/lbjlaq/Antigravity-Manager) | 30 324 | Rust | Professional Antigravity Account Manager & Switcher. One-click seamless account switching for Antigravity Tools. Built with Tauri v2 + React (Rust).专业的 Antigravity… **— не просто перемикач акаунтів: під капотом проксі-шлюз диспетчеризації запитів до AI-провайдерів** |
| [p-e-w/heretic](https://github.com/p-e-w/heretic) | 27 179 | Python | Fully automatic censorship removal for language models |
| [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | 13 624 | Swift | Lightning-Fast, On-Device, Multilingual TTS — running natively via ONNX. |
| [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice) | 9 407 | Swift | Fastest and only macOS Dictation app with on-device STT and custom trained AI enhancement model. A local Wispr Flow alternative. ⭐ helps a ton :) Windows & iOS… |
| [automazeio/vibeproxy](https://github.com/automazeio/vibeproxy) | 3 260 | Swift | Native macOS menu bar app to use your Claude Code & ChatGPT subscriptions with AI coding tools - no API keys needed |
| [FareedKhan-dev/kimi-k3-in-c](https://github.com/FareedKhan-dev/kimi-k3-in-c) | 3 038 | C | A 2.78-trillion-parameter Kimi K3 running inference on a single CPU in 8.24 GB of RAM. Portable C99: no BLAS, no framework, no GPU. |
| [liaohch3/claude-tap](https://github.com/liaohch3/claude-tap) | 2 982 | Python | Intercept and inspect Coding Agent API traffic from Claude Code, Codex CLI, Gemini CLI, Cursor CLI, OpenCode, Kimi/Kimi Code, Pi, and Hermes in a local trace viewer. |
| [superlinked/sie](https://github.com/superlinked/sie) | 2 647 | Python | Open-source inference server and production cluster for all the models your agent needs. |
| [cneuralnetwork/smol-kimi-k3](https://github.com/cneuralnetwork/smol-kimi-k3) | 86 | Python | A 49M-parameter Kimi K3-inspired language model trainable on one 8GB GPU **— маленька Kimi K3 для тренування на одній 8GB GPU; без тем правила нічого не бачать** |

---

**Інші теки** · [Архів](archive.md) · [Безпека](security.md) · [QA](qa.md) · [Skills](skills.md) · [Пам'ять](memory.md) · [Медіа](media.md) · [Агенти](agents.md) · [DevOps](devops.md) · [Ресурси](resources.md) · [Веб](web.md)

[← На робочий стіл](../README.md)
