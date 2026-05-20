<div align="center">

<img src="https://raw.githubusercontent.com/huachabobo/huachabobo/main/assets/lecia-agentos-banner.svg?v=20260521-p1-audit" alt="huachabobo custom banner" />

<br />
<br />

<img src="https://raw.githubusercontent.com/huachabobo/huachabobo/main/assets/lecia-agentos-typing.svg?v=20260424-type-backspace" alt="Lecia AgentOS animated typing line" />

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
  <img src="https://img.shields.io/badge/Current%20Progress-84%25-704f63?style=for-the-badge" alt="Current Progress 84%" />
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
- 当前进度：`84%`，controlled-core V1 已进入 P1 evidence-ready / freeze audit 阶段。<br />Current progress: `84%`, with controlled-core V1 now in the P1 evidence-ready / freeze audit stage.
- 当前形态：`self-hosted AgentOS control plane` · `operator recovery loop` · `P1 audit-ready`<br />Current shape: `self-hosted AgentOS control plane` · `operator recovery loop` · `P1 audit-ready`
- 默认气质：`local-first` · `self-hosted` · `governable`<br />Default posture: `local-first` · `self-hosted` · `governable`
- 默认要求：`safe` · `auditable` · `controllable`<br />Default expectations: `safe` · `auditable` · `controllable`

<div align="center">

<img src="https://raw.githubusercontent.com/huachabobo/huachabobo/main/assets/lecia-agentos-dashboard.svg?v=20260521-p1-audit" alt="Lecia AgentOS mini dashboard" />

</div>

### 最新进度 / Latest Progress

- P1 completion audit 的 required evidence 已经 `4/4` 通过：Provider bootstrap、clean first useful run、restore/update recovery drill、Compose deploy/recover smoke 都有可复盘产物。<br />The P1 completion audit now has `4/4` required evidence passing: Provider bootstrap, clean first useful run, restore/update recovery drill, and Compose deploy/recover smoke all have reviewable artifacts.
- `compose-up smoke` 已经把 first-useful-run、restore、update-apply、secret-leak proof 与 runtime shutdown audit 收进结构化结果。<br />`compose-up smoke` now captures first-useful-run, restore, update-apply, secret-leak proof, and runtime shutdown audit in structured results.
- Provider / adapter 真实路径继续变硬：OpenAI-compatible dialect 证据、Postgres first-wave phase status、OneBot/SnowLuma 预检与授权 QQ/NapCat Provider reply 都进入证据链。<br />Provider / adapter reality is getting stronger: OpenAI-compatible dialect evidence, Postgres first-wave phase status, OneBot/SnowLuma preflight, and authorized QQ/NapCat Provider reply are now part of the evidence chain.
- 运维侧新增 runtime shutdown reason、server close audit、auto-ports、local-admin takeover password-file 与 artifact locator 收口。<br />Operations now include runtime shutdown reasons, server close audit, auto-ports, local-admin takeover password-file support, and tighter artifact locator handoff.
- 当前剩余 follow-up 很明确：current data-dir local-admin security live check，以及 recorded-SHA deferred CI 跟进。<br />The remaining follow-ups are explicit: current data-dir local-admin security live check and recorded-SHA deferred CI follow-up.

### 已经进入真实形态 / Already Real

- 官网与文档中心已经上线，产品入口和叙事骨架是完整的。<br />The public site and docs are live, and the product narrative now has a real entrypoint.
- 核心仓库已经具备真实的 `web` / `server` / `CLI` / `persistence` / `runtime` 切片。<br />The core repo already has real `web` / `server` / `CLI` / `persistence` / `runtime` slices.
- `approval`、`trust`、`snapshot`、`restore`、`observability` 这些治理能力已经不是概念，而是工程中的默认能力。<br />`approval`, `trust`, `snapshot`, `restore`, and `observability` are no longer ideas on paper, but default engineering capabilities.
- 前台对话、后台任务、provider 路由、isolated execution、NapCat/OneBot 回执与恢复证据，正在被收进同一条可追踪的运行时链路。<br />Foreground chat, background jobs, provider routing, isolated execution, NapCat/OneBot receipts, and recovery evidence are being pulled into one traceable runtime chain.

### 持续打磨中 / Still Being Polished

- 做 P1 freeze audit 前的最后收口：确认 current data-dir security、recorded-SHA deferred CI 与外部阻塞都被显式记录。<br />Close the last pre-freeze audit loop: make current data-dir security, recorded-SHA deferred CI, and external blockers explicit.
- 继续把 Provider / adapter runtime、Postgres first-wave 与 NapCat/QQ 证明做成可复盘证据，而不是口头“能跑”。<br />Keep turning Provider / adapter runtime, Postgres first-wave, and NapCat/QQ proof into reviewable evidence instead of informal “it works” claims.
- 强化 operator 视角下的 approval、auditability、artifact handoff、shutdown audit 与 recovery deep links。<br />Strengthen approval, auditability, artifact handoff, shutdown audit, and recovery deep links from the operator point of view.
- 把 orchestration layer 继续做实，避免产品退化成单纯的 reply shell。<br />Keep building out orchestration so the product does not collapse into a reply shell.

> `Lecia AgentOS` 核心仓库目前还在持续私有开发中，所以我把官网与文档中心作为当前最主要的对外入口。  
> The core repo is still under private development, so the public site and docs are the main public entry today.

<details>
<summary>Roadmap / 路线图</summary>

| Horizon | 中文 | English |
| --- | --- | --- |
| `Now` | 完成 P1 evidence-ready 后的 freeze audit：证据、关闭审计、外部 CI 跟进与本地安全检查收口。 | Finish the post evidence-ready P1 freeze audit: evidence, shutdown audit, external CI follow-up, and local security checks. |
| `Next` | 进入 P2.1 contract freeze：把已使用的 routes、artifacts、handoff payloads 与 Provider/adapter 证据固化为共享契约。 | Move into P2.1 contract freeze: stabilize routes, artifacts, handoff payloads, and Provider/adapter evidence into shared contracts. |
| `Later` | 让 runtime、governance、docs 与 orchestration 在同一套 self-hosted AgentOS 体验里自然闭环。 | Make runtime, governance, docs, and orchestration feel like one closed-loop self-hosted AgentOS experience. |

</details>

## Now Building / 当前在做

<div align="center">

<img src="https://raw.githubusercontent.com/huachabobo/huachabobo/main/assets/lecia-agentos-now-building.svg?v=20260521-p1-audit" alt="Now building terminal status bar" />

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
