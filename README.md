<div align="center">

<img src="https://raw.githubusercontent.com/huachabobo/huachabobo/main/assets/lecia-agentos-banner.svg?v=20260601-p6-agentos" alt="huachabobo custom banner" />

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
  <img src="https://img.shields.io/badge/Current%20Progress-95%25-704f63?style=for-the-badge" alt="Current Progress 95%" />
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
- 当前进度：`95%`，controlled-core V1 已进入 `P6 AgentOS completion roadmap`，正在把 P4/P5 的未来保留范围收束成有顺序的完成路线。<br />Current progress: `95%`, with controlled-core V1 now in the `P6 AgentOS completion roadmap`, turning P4/P5 future-reserved scope into an ordered completion path.
- 当前形态：`self-hosted AgentOS control plane` · `P6 completion roadmap` · `runtime execution spine`<br />Current shape: `self-hosted AgentOS control plane` · `P6 completion roadmap` · `runtime execution spine`
- 默认气质：`local-first` · `self-hosted` · `governable`<br />Default posture: `local-first` · `self-hosted` · `governable`
- 默认要求：`safe` · `auditable` · `controllable`<br />Default expectations: `safe` · `auditable` · `controllable`

<div align="center">

<img src="https://raw.githubusercontent.com/huachabobo/huachabobo/main/assets/lecia-agentos-dashboard.svg?v=20260601-p6-agentos" alt="Lecia AgentOS mini dashboard" />

</div>

### 最新进度 / Latest Progress

- 当前主线已经切到 `P6 AgentOS Completion Roadmap`：P6.0 做 remote closeout stabilization，P6.1 做 runtime execution spine。<br />The active track has moved to `P6 AgentOS Completion Roadmap`: P6.0 for remote closeout stabilization, and P6.1 for the runtime execution spine.
- P4/P5 的未展开范围不再是含糊的“以后再说”，而是被放进 P6.0-P6.7 的有序路线：module activation、Bot-first ServerOps、governed ecosystem、Studio、multi-agent/self-tuning、hosted/adapters/companion expansion。<br />The unimplemented P4/P5 scope is no longer vague “later” work; it is now ordered into P6.0-P6.7 lanes: module activation, Bot-first ServerOps, governed ecosystem, Studio, multi-agent/self-tuning, and hosted/adapters/companion expansion.
- 最新远端 HEAD 是 `7f161af7`，`origin/main` 已对齐；最近一批提交正在贯通后台执行、queued/retry/cancel/digest、bulk actions、run evidence 与 Web/operator 可见证据。<br />The latest remote HEAD is `7f161af7`, aligned with `origin/main`; the recent batch connects background execution, queued/retry/cancel/digest behavior, bulk actions, run evidence, and Web/operator-visible proof.
- 本地验证已通过 `docs:current-work-item:check`、`docs:p6-agentos-completion-roadmap:audit`，以及 protocol / kernel / server / Web 的焦点测试。<br />Local validation passes `docs:current-work-item:check`, `docs:p6-agentos-completion-roadmap:audit`, plus focused protocol / kernel / server / Web tests.
- 当前边界也很清楚：`compose-up-smoke` 已经绿了，`ci-core` 正在 P6.0 closeout triage 中，失败点集中在 automation retry-lineage 路径；P5 recorded-SHA / predecessor artifact alignment 被作为证据边界单独跟进。<br />The boundary is clear too: `compose-up-smoke` is green, while `ci-core` is in P6.0 closeout triage around the automation retry-lineage path; P5 recorded-SHA / predecessor artifact alignment is tracked separately as an evidence boundary.

### 已经进入真实形态 / Already Real

- 官网与文档中心已经上线，产品入口和叙事骨架是完整的。<br />The public site and docs are live, and the product narrative now has a real entrypoint.
- 核心仓库已经具备真实的 `web` / `server` / `CLI` / `persistence` / `runtime` 切片。<br />The core repo already has real `web` / `server` / `CLI` / `persistence` / `runtime` slices.
- `approval`、`trust`、`snapshot`、`restore`、`observability` 这些治理能力已经不是概念，而是工程中的默认能力。<br />`approval`, `trust`, `snapshot`, `restore`, and `observability` are no longer ideas on paper, but default engineering capabilities.
- 前台对话、后台任务、Provider incident、adapter readiness、NapCat/OneBot 回执、bulk action 与恢复证据，正在被收进同一条可追踪的运行时链路。<br />Foreground chat, background jobs, Provider incidents, adapter readiness, NapCat/OneBot receipts, bulk actions, and recovery evidence are being pulled into one traceable runtime chain.

### 持续打磨中 / Still Being Polished

- 收口 P6.0：继续跟进最新 pushed SHA 的 `ci-core`，并把远端 CI / recorded-SHA / artifact alignment 和真实代码问题分开处理。<br />Close out P6.0: keep following the latest pushed SHA's `ci-core`, and separate remote CI / recorded-SHA / artifact alignment from real code issues.
- 推进 P6.1：让 queue lease、resume、retry、cancel、digest、run_id 与 governance audit evidence 形成更真实的 runtime execution spine。<br />Advance P6.1: make queue lease, resume, retry, cancel, digest, run_id, and governance audit evidence form a more real runtime execution spine.
- 后续进入 P6.2/P6.3：把 ThemePack / ExperienceProfile activation 与 OpsPack local operation execution 从 handoff evidence 推到受治理的真实动作。<br />Next, move into P6.2/P6.3: turn ThemePack / ExperienceProfile activation and OpsPack local operation execution from handoff evidence into governed real actions.
- 再往后才扩展 ecosystem distribution、full Studio、multi-agent/self-tuning、hosted/adapters/companion shape。<br />Only after that should the system expand into ecosystem distribution, full Studio, multi-agent/self-tuning, and hosted/adapters/companion shape.

> `Lecia AgentOS` 核心仓库目前还在持续私有开发中，所以我把官网与文档中心作为当前最主要的对外入口。  
> The core repo is still under private development, so the public site and docs are the main public entry today.

<details>
<summary>Roadmap / 路线图</summary>

| Horizon | 中文 | English |
| --- | --- | --- |
| `Now` | P6.0/P6.1：远端 closeout 稳定化，继续把后台执行与 bulk runtime evidence 串成 runtime spine。 | P6.0/P6.1: stabilize remote closeout and keep connecting background execution plus bulk runtime evidence into the runtime spine. |
| `Next` | P6.2/P6.3：模块激活真实化，以及 Bot-first ServerOps 的本地受治理执行。 | P6.2/P6.3: make module activation real, then add governed local Bot-first ServerOps execution. |
| `Later` | P6.4-P6.7：外部分发、完整 Studio、多智能体/自调优、hosted/adapter/companion 扩展。 | P6.4-P6.7: external distribution, full Studio, multi-agent/self-tuning, and hosted/adapter/companion expansion. |

</details>

## Now Building / 当前在做

<div align="center">

<img src="https://raw.githubusercontent.com/huachabobo/huachabobo/main/assets/lecia-agentos-now-building.svg?v=20260601-p6-agentos" alt="Now building terminal status bar" />

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
