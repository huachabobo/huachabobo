<div align="center">

<img src="https://raw.githubusercontent.com/huachabobo/huachabobo/main/assets/lecia-agentos-banner.svg" alt="huachabobo custom banner" />

<br />
<br />

<a href="https://github.com/DenverCoder1/readme-typing-svg">
  <img src="https://readme-typing-svg.demolab.com/?font=Fira+Code&size=24&pause=1400&color=CA6C97&center=true&vCenter=true&width=760&lines=Lecia+AgentOS+builder;做可爱、认真、可治理的+AI+系统;self-hosted+agent+systems%2C+operator-first;soft+edges+%C2%B7+serious+systems" alt="Typing SVG" />
</a>

# 花茶 / huachabobo

<p>
  <strong>做可爱、认真、可治理的 AI 系统。</strong><br />
  Building trustworthy, governable, and self-hosted agent systems.
</p>

<p><sub>soft edges, serious systems.</sub></p>

<p>
  <a href="https://leciabot-site.huach.top/">
    <img src="https://img.shields.io/badge/Lecia%20AgentOS-Official%20Site-ca6c97?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Lecia AgentOS Official Site" />
  </a>
  <img src="https://img.shields.io/badge/Current%20Progress-70%25-704f63?style=for-the-badge" alt="Current Progress 70%" />
  <img src="https://komarev.com/ghpvc/?username=huachabobo&label=PROFILE%20VIEWS&color=ca6c97&style=for-the-badge" alt="Profile views counter" />
</p>

<p>
  <a href="https://leciabot-site.huach.top/">官方文档 / Docs</a> ·
  <a href="https://github.com/huachabobo/vc-daily-brief-agent">VC Daily Brief Agent</a> ·
  <a href="https://github.com/huachabobo/astrbot_plugin_mimo_tts_decorator">MiMo TTS Plugin</a>
</p>

</div>

## Lecia AgentOS / Core Project

`Lecia AgentOS` 是我目前最核心、也最想被认真介绍的项目。

`Lecia AgentOS` is the project I care about most, and the one I most want people to understand clearly.

它不是一个“会聊天”的 bot 包装层，而是一套面向自托管团队的 AgentOS control plane。

It is not just a chat wrapper for bots, but a self-hosted AgentOS control plane for teams.

我想把入口、runtime、governance、docs、operator workflow 与后续 orchestration，收进同一套清晰、长期可维护的系统设计里。

I want product entrypoints, runtime, governance, docs, operator workflows, and orchestration to feel like one coherent, maintainable system.

官网负责建立第一理解，文档负责继续展开运行时、治理与控制面的细节。

The public site gives the first mental model, while the docs expand the runtime, governance, and control-plane details.

- 官网与文档中心：[leciabot-site.huach.top](https://leciabot-site.huach.top/)<br />Public site and docs: [leciabot-site.huach.top](https://leciabot-site.huach.top/)
- 当前进度：`70%`<br />Current progress: `70%`
- 当前形态：`self-hosted AgentOS control plane`<br />Current shape: `self-hosted AgentOS control plane`
- 默认气质：`local-first` · `self-hosted` · `governable`<br />Default posture: `local-first` · `self-hosted` · `governable`
- 默认要求：`safe` · `auditable` · `controllable`<br />Default expectations: `safe` · `auditable` · `controllable`

<div align="center">

<img src="https://raw.githubusercontent.com/huachabobo/huachabobo/main/assets/lecia-agentos-dashboard.svg" alt="Lecia AgentOS mini dashboard" />

</div>

### 已经进入真实形态 / Already Real

- 官网与文档中心已经上线，产品入口和叙事骨架是完整的。<br />The public site and docs are live, and the product narrative now has a real entrypoint.
- 核心仓库已经具备真实的 `web` / `server` / `CLI` / `persistence` / `runtime` 切片。<br />The core repo already has real `web` / `server` / `CLI` / `persistence` / `runtime` slices.
- `approval`、`trust`、`snapshot`、`restore`、`observability` 这些治理能力已经不是概念，而是工程中的默认能力。<br />`approval`, `trust`, `snapshot`, `restore`, and `observability` are no longer ideas on paper, but default engineering capabilities.
- 前台对话、后台任务、provider 路由与执行证据，正在被收进同一条可追踪的运行时链路。<br />Foreground chat, background jobs, provider routing, and execution evidence are being pulled into one traceable runtime chain.

### 持续打磨中 / Still Being Polished

- 把 controlled core 做得更稳，让它更适合真实部署，而不只是漂亮 demo。<br />Make the controlled core steadier and more deployment-ready, not just demo-friendly.
- 继续打磨 provider / adapter runtime，让它能长期运行，而不是短期可演示。<br />Keep hardening the provider / adapter runtime so it can run for the long term, not just for short demos.
- 强化 operator 视角下的 approval、auditability 与 recovery 体验。<br />Strengthen approval, auditability, and recovery from the operator point of view.
- 把 orchestration layer 继续做实，避免产品退化成单纯的 reply shell。<br />Keep building out orchestration so the product does not collapse into a reply shell.

> `Lecia AgentOS` 核心仓库目前还在持续私有开发中，所以我把官网与文档中心作为当前最主要的对外入口。  
> The core repo is still under private development, so the public site and docs are the main public entry today.

<details>
<summary>Roadmap / 路线图</summary>

| Horizon | 中文 | English |
| --- | --- | --- |
| `Now` | 把 controlled core 做稳，把 provider runtime 做硬，把 operator-facing approval flow 做顺。 | Make the controlled core steadier, harden provider runtime, and smooth out the operator-facing approval flow. |
| `Next` | 把 orchestration 语义做得更强，把执行证据做得更清楚，把恢复路径做得更可靠。 | Strengthen orchestration semantics, clarify execution evidence, and improve recovery paths. |
| `Later` | 让 runtime、governance、docs 与 orchestration 在同一套 self-hosted AgentOS 体验里自然闭环。 | Make runtime, governance, docs, and orchestration feel like one closed-loop self-hosted AgentOS experience. |

</details>

## Now Building / 当前在做

<div align="center">

<img src="https://raw.githubusercontent.com/huachabobo/huachabobo/main/assets/lecia-agentos-now-building.svg" alt="Now building terminal status bar" />

<sub>当前焦点，但用一条微型 control-plane terminal 来表达。 / Current focus, rendered like a tiny control-plane terminal.</sub>

</div>

## Heartbeat / 心跳

<div align="center">

<img src="https://raw.githubusercontent.com/huachabobo/huachabobo/main/assets/lecia-agentos-heartbeat.svg" alt="Heartbeat status card" />

<sub>系统在线，节奏稳定。 / System alive, operator calm.</sub>

</div>

## Selected Work / 精选项目

| Project | 中文 | English |
| --- | --- | --- |
| [vc-daily-brief-agent](https://github.com/huachabobo/vc-daily-brief-agent) | 把 YouTube 与 RSS 信号整理成移动优先、可解释的飞书 VC 简报。 | Turns YouTube and RSS signals into mobile-first, explainable Feishu VC briefings. |
| [astrbot_plugin_mimo_tts_decorator](https://github.com/huachabobo/astrbot_plugin_mimo_tts_decorator) | 一个给 AstrBot 使用的 MiMo TTS 装饰器，支持自动打标、清洗与调试开关。 | A MiMo TTS decorator for AstrBot with auto-tagging, cleanup, and debugging switches. |
| [MaiBot](https://github.com/huachabobo/MaiBot) | 一个更关注长期理解与真实交互质感的 LLM 数字生命实验。 | An LLM digital-life experiment focused on long-horizon understanding and more human interaction texture. |

## Focus / 关注方向

`AgentOS` `LLM Runtime` `Self-hosted AI` `Governance` `Operator UX` `Automation` `Docs as Product` `TypeScript` `Python`

<div align="center">

<img src="https://skillicons.dev/icons?i=ts,py,nodejs,docker,githubactions,postgres,redis,linux,vite&theme=light&perline=9" alt="Skill icons" />

</div>

<details>
<summary>How I think about systems / 我如何看系统</summary>

我喜欢把看起来柔软的体验，建立在足够坚实的系统之上。

I like building soft-looking experiences on top of systems that are actually solid underneath.

我会反复追问这些问题：

These are the questions I keep asking:

- 产品有没有清晰的控制面。<br />Does the product have a clear control plane?
- 运行时是不是诚实、稳定、可解释。<br />Is the runtime honest, stable, and explainable?
- 文档是不是产品的一部分，而不是最后补上的说明。<br />Are the docs part of the product, instead of an afterthought?
- 默认能力里有没有治理、审计、恢复与安全边界。<br />Do the defaults include governance, auditability, recovery, and safety boundaries?
- 项目能不能被部署、维护、继续演化。<br />Can the project actually be deployed, maintained, and evolved?

</details>

## Tiny Arcade / 小彩蛋

<div align="center">

<img src="https://raw.githubusercontent.com/huachabobo/huachabobo/main/assets/lecia-agentos-pacman.svg" alt="Pac-Man style Lecia AgentOS arcade component" />

<sub>待办列表也值得一点街机能量。<br />Even the backlog deserves a little arcade energy.</sub>

</div>

## Contribution Flow / 贡献流

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/huachabobo/huachabobo/output/github-contribution-grid-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/huachabobo/huachabobo/output/github-contribution-grid-snake.svg" />
  <img alt="github contribution snake" src="https://raw.githubusercontent.com/huachabobo/huachabobo/output/github-contribution-grid-snake.svg" />
</picture>

<sub>表面可爱，底层认真。 / Cute on the surface. Serious underneath.</sub>

</div>
