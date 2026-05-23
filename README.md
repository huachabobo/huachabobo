<div align="center">

<img src="https://raw.githubusercontent.com/huachabobo/huachabobo/main/assets/lecia-agentos-banner.svg?v=20260523-p2-5-beta" alt="huachabobo custom banner" />

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
  <img src="https://img.shields.io/badge/Current%20Progress-89%25-704f63?style=for-the-badge" alt="Current Progress 89%" />
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
- 当前进度：`89%`，controlled-core V1 已进入 P2.5 Provider & Adapter beta proof 阶段。<br />Current progress: `89%`, with controlled-core V1 now in the P2.5 Provider & Adapter beta proof stage.
- 当前形态：`self-hosted AgentOS control plane` · `P2 controlled-core beta` · `provider / adapter evidence`<br />Current shape: `self-hosted AgentOS control plane` · `P2 controlled-core beta` · `provider / adapter evidence`
- 默认气质：`local-first` · `self-hosted` · `governable`<br />Default posture: `local-first` · `self-hosted` · `governable`
- 默认要求：`safe` · `auditable` · `controllable`<br />Default expectations: `safe` · `auditable` · `controllable`

<div align="center">

<img src="https://raw.githubusercontent.com/huachabobo/huachabobo/main/assets/lecia-agentos-dashboard.svg?v=20260523-p2-5-beta" alt="Lecia AgentOS mini dashboard" />

</div>

### 最新进度 / Latest Progress

- P2.1 到 P2.4 的守门审计已经全部通过：contract freeze `22/22`，persistence/migration `20/20`，governance `30 events / 21 evidence paths`，queue/worker lifecycle `16 events / 39 evidence paths`。<br />The P2.1 through P2.4 guard audits are all passing: contract freeze `22/22`, persistence/migration `20/20`, governance `30 events / 21 evidence paths`, and queue/worker lifecycle `16 events / 39 evidence paths`.
- 当前主线是 `P2.5 Provider & Adapter Beta Proof`：Provider incident summaries、budget posture、fallback attempt、request class 与 background Provider failure evidence 正在被收进 route / audit / Web / artifact reader。<br />The active track is `P2.5 Provider & Adapter Beta Proof`: Provider incident summaries, budget posture, fallback attempts, request classes, and background Provider failure evidence are being carried through routes, audit, Web, and the artifact reader.
- NapCat / OneBot / QQ 证明路径继续变硬：supported-command contract 已冻结，receipt state 能区分 accepted、rejected、missing、deferred，stale-ingress send guidance 也被 gated。<br />The NapCat / OneBot / QQ proof path is stronger: the supported-command contract is frozen, receipt states distinguish accepted, rejected, missing, and deferred, and stale-ingress send guidance is gated.
- 最新本地 HEAD 是 `26055f9`，比 `origin/main` 领先 `20` 个提交；这些提交集中在 Provider/Adapter beta proof，而不是重新打开大架构。<br />The latest local HEAD is `26055f9`, `20` commits ahead of `origin/main`; those commits focus on Provider/Adapter beta proof instead of reopening broad architecture.
- 当前边界也很清楚：本地 P2 验证为绿，但这批还需要 batch closeout / push，远端验证要等新的 pushed SHA 再重新跟进。<br />The boundary is clear too: local P2 validation is green, but this batch still needs closeout / push, and remote validation should be followed up again after the next pushed SHA.

### 已经进入真实形态 / Already Real

- 官网与文档中心已经上线，产品入口和叙事骨架是完整的。<br />The public site and docs are live, and the product narrative now has a real entrypoint.
- 核心仓库已经具备真实的 `web` / `server` / `CLI` / `persistence` / `runtime` 切片。<br />The core repo already has real `web` / `server` / `CLI` / `persistence` / `runtime` slices.
- `approval`、`trust`、`snapshot`、`restore`、`observability` 这些治理能力已经不是概念，而是工程中的默认能力。<br />`approval`, `trust`, `snapshot`, `restore`, and `observability` are no longer ideas on paper, but default engineering capabilities.
- 前台对话、后台任务、Provider incident、adapter readiness、NapCat/OneBot 回执与恢复证据，正在被收进同一条可追踪的运行时链路。<br />Foreground chat, background jobs, Provider incidents, adapter readiness, NapCat/OneBot receipts, and recovery evidence are being pulled into one traceable runtime chain.

### 持续打磨中 / Still Being Polished

- 完成 P2.5 Provider / Adapter beta proof 的 batch closeout，把本地领先的 `20` 个提交收口成可推送状态。<br />Finish the P2.5 Provider / Adapter beta proof batch closeout and turn the `20` local-ahead commits into a push-ready state.
- 继续把 Provider incident、budget / fallback posture、NapCat command contract 与 OneBot receipt recovery 做成可复盘证据，而不是口头“能跑”。<br />Keep turning Provider incidents, budget / fallback posture, NapCat command contracts, and OneBot receipt recovery into reviewable evidence instead of informal “it works” claims.
- 准备进入 P2.6 observability / internal diagnostics，把 smoke-time evidence 进一步变成日常 operator signals。<br />Prepare for P2.6 observability / internal diagnostics, turning smoke-time evidence into daily operator signals.
- 把 orchestration layer 继续做实，避免产品退化成单纯的 reply shell。<br />Keep building out orchestration so the product does not collapse into a reply shell.

> `Lecia AgentOS` 核心仓库目前还在持续私有开发中，所以我把官网与文档中心作为当前最主要的对外入口。  
> The core repo is still under private development, so the public site and docs are the main public entry today.

<details>
<summary>Roadmap / 路线图</summary>

| Horizon | 中文 | English |
| --- | --- | --- |
| `Now` | 完成 P2.5 Provider / Adapter beta proof：Provider incident、budget posture、NapCat command contract 与 OneBot receipt recovery 收口。 | Finish P2.5 Provider / Adapter beta proof: Provider incidents, budget posture, NapCat command contracts, and OneBot receipt recovery. |
| `Next` | 进入 P2.6 observability / internal diagnostics：把 smoke-time evidence 变成日常 operator signals 与诊断 bundle。 | Move into P2.6 observability / internal diagnostics: turn smoke-time evidence into daily operator signals and diagnostic bundles. |
| `Later` | 进入 P3 external trial readiness：安装、首跑、恢复、更新、支持包与 trial checklist。 | Move into P3 external trial readiness: install, first run, restore, update, support bundles, and the trial checklist. |

</details>

## Now Building / 当前在做

<div align="center">

<img src="https://raw.githubusercontent.com/huachabobo/huachabobo/main/assets/lecia-agentos-now-building.svg?v=20260523-p2-5-beta" alt="Now building terminal status bar" />

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
