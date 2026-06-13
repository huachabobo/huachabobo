<div align="center">

<img src="https://raw.githubusercontent.com/huachabobo/huachabobo/main/assets/lecia-agentos-banner.svg?v=20260614-dual-core" alt="huachabobo custom banner" />

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
  <img src="https://img.shields.io/badge/Lecia%20Progress-97%25-704f63?style=for-the-badge" alt="Lecia AgentOS Progress 97%" />
  <img src="https://img.shields.io/badge/CodeLife-CI%20green-4f8f7a?style=for-the-badge&logo=githubactions&logoColor=white" alt="CodeLife CI green" />
  <img src="https://komarev.com/ghpvc/?username=huachabobo&label=PROFILE%20VIEWS&color=ca6c97&style=for-the-badge" alt="Profile views counter" />
</p>

<p>
  <a href="https://leciabot-site.huach.top/">官方文档 / Docs</a> ·
  <span>CodeLife Lab / private research</span> ·
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
- 当前进度：`97%`，controlled-core V1 已推进到 `P6.7 hosted / adapter / companion expansion` 的 readiness 与 evidence closeout。<br />Current progress: `97%`, with controlled-core V1 now in `P6.7 hosted / adapter / companion expansion` readiness and evidence closeout.
- 当前形态：`self-hosted AgentOS control plane` · `P6.7 readiness` · `governed operator evidence`<br />Current shape: `self-hosted AgentOS control plane` · `P6.7 readiness` · `governed operator evidence`
- 默认气质：`local-first` · `self-hosted` · `governable`<br />Default posture: `local-first` · `self-hosted` · `governable`
- 默认要求：`safe` · `auditable` · `controllable`<br />Default expectations: `safe` · `auditable` · `controllable`

<div align="center">

<img src="https://raw.githubusercontent.com/huachabobo/huachabobo/main/assets/lecia-agentos-dashboard.svg?v=20260614-dual-core" alt="Lecia AgentOS mini dashboard" />

</div>

### 最新进度 / Latest Progress

- 当前主线已经推进到 `P6.7 hosted / adapter / companion expansion`：重点是 readiness surface、default-off boundary、support-bundle/operator evidence，而不是直接打开 hosted 或 companion-first 行为。<br />The active track has moved to `P6.7 hosted / adapter / companion expansion`: readiness surfaces, default-off boundaries, and support-bundle/operator evidence, not hosted-first or companion-first behavior.
- 最新远端 HEAD 是 `e3611b26`，`origin/main` 已对齐；最近一批提交把 Compose success、queue policy preflight、approval/audit route-count、lease scope 与 read-only mutation summary 显示到 Operations local artifact reader。<br />The latest remote HEAD is `e3611b26`, aligned with `origin/main`; the recent batch exposes Compose success, queue policy preflight, approval/audit route-counts, lease scope, and read-only mutation summaries in the Operations local artifact reader.
- 本地验证已通过 `docs:current-work-item:check` 和 `docs:p6-agentos-completion-roadmap:audit -- --json`，P6 roadmap 审计覆盖 `13` 个脚本与 `1812` 个证据片段。<br />Local validation passes `docs:current-work-item:check` and `docs:p6-agentos-completion-roadmap:audit -- --json`, with the P6 roadmap audit covering `13` scripts and `1812` evidence fragments.
- 远端 GitHub Actions 目前被 billing / spending-limit 门禁拦住：`ci-core` 与 `compose-up-smoke` 的 job 没有真正启动，所以它是外部门禁噪声，不是测试日志里的代码失败。<br />Remote GitHub Actions are currently blocked by a billing / spending-limit gate: `ci-core` and `compose-up-smoke` never really start, so this is external gate noise, not a code failure from test logs.

### 已经进入真实形态 / Already Real

- 官网与文档中心已经上线，产品入口和叙事骨架是完整的。<br />The public site and docs are live, and the product narrative now has a real entrypoint.
- 核心仓库已经具备真实的 `web` / `server` / `CLI` / `persistence` / `runtime` 切片。<br />The core repo already has real `web` / `server` / `CLI` / `persistence` / `runtime` slices.
- `approval`、`trust`、`snapshot`、`restore`、`observability` 这些治理能力已经不是概念，而是工程中的默认能力。<br />`approval`, `trust`, `snapshot`, `restore`, and `observability` are no longer ideas on paper, but default engineering capabilities.
- 前台对话、后台任务、Provider incident、adapter readiness、NapCat/OneBot 回执、bulk action、Compose success 与 queue preflight evidence，正在被收进同一条可追踪的运行时链路。<br />Foreground chat, background jobs, Provider incidents, adapter readiness, NapCat/OneBot receipts, bulk actions, Compose success, and queue preflight evidence are being pulled into one traceable runtime chain.

### 持续打磨中 / Still Being Polished

- 收口 P6.7：继续把 hosted / adapter / companion 相关能力保持在 readiness 与 default-off 证据层，先证明 operator 能看懂、能复盘、能拒绝。<br />Close out P6.7: keep hosted / adapter / companion work at the readiness and default-off evidence layer first, proving operators can understand, review, and reject it.
- 继续打磨 Compose / queue / policy preflight：让成功路径和失败路径都能解释 route、action、approval/audit count、lease scope 与 read-only mutation posture。<br />Keep hardening Compose / queue / policy preflight: make both success and failure paths explain route, action, approval/audit counts, lease scope, and read-only mutation posture.
- 处理 GitHub Actions billing / spending-limit 门禁后，再重新跑 `ci-core` 与 `compose-up-smoke`，不要把门禁噪声混进代码质量判断。<br />After the GitHub Actions billing / spending-limit gate is resolved, rerun `ci-core` and `compose-up-smoke` without mixing gate noise into code-quality judgment.

> `Lecia AgentOS` 核心仓库目前还在持续私有开发中，所以我把官网与文档中心作为当前最主要的对外入口。  
> The core repo is still under private development, so the public site and docs are the main public entry today.

<details>
<summary>Roadmap / 路线图</summary>

| Horizon | 中文 | English |
| --- | --- | --- |
| `Now` | P6.7：hosted / adapter / companion readiness，默认关闭，证据先行。 | P6.7: hosted / adapter / companion readiness, default-off, evidence first. |
| `Next` | 重新跑 Actions 门禁，继续把 Compose / queue preflight 变成日常 operator evidence。 | Rerun the Actions gates, then keep turning Compose / queue preflight into daily operator evidence. |
| `Later` | 只有在受治理证据闭合后，才进入真正的 hosted、broad adapter、companion-rich 或 desktop shell 扩展。 | Only after governed evidence closes should the system expand into real hosted, broad adapter, companion-rich, or desktop-shell behavior. |

</details>

## CodeLife Lab / Digital Life Research

`CodeLife Lab` 是我的另一个长期研究项目：在纯计算基质里做非 LLM 的数字生命实验。

`CodeLife Lab` is another long-running research project: a non-LLM digital-life experiment inside a computational substrate.

它研究的“生命体”不是 prompt、agent 或 Python 脚本，而是运行在 LifeVM 中的 CIL genome：有 energy、sensor inputs、action ports、reproduction、mutation operators 和 lineage history。

The "organisms" are not prompts, agents, or Python scripts, but CIL genomes running in LifeVM with energy, sensor inputs, action ports, reproduction, mutation operators, and lineage history.

- 当前状态：私有研究仓库，最新远端 HEAD 为 `1b8bb180`，GitHub Actions `ci` 绿，Python `3.11` / `3.12` 下 Ruff、Pytest、v0 smoke run 均通过。<br />Current status: private research repo, latest remote HEAD `1b8bb180`, GitHub Actions `ci` green, with Ruff, Pytest, and v0 smoke passing on Python `3.11` / `3.12`.
- 最新进度：进入 Milestone `357`，把 post-support sampling gap 从“看不见原因”推进到可解释的 public lineage diagnostics。<br />Latest progress: Milestone `357`, moving the post-support sampling gap from an opaque blocker into explainable public lineage diagnostics.
- 关键突破：support-order / dispatch-window audits 已能解释 support 完成后的 reproduction、birth、death、mutation rejection，并把下一步 focus 收敛到 `dispatch_probability` 与 rejection/death timing。<br />Key improvement: support-order / dispatch-window audits now explain post-support reproduction, birth, death, and mutation rejection, narrowing the next focus to `dispatch_probability` and rejection/death timing.
- 清晰边界：这些都是 host-side public evidence，不改变 CIL / LifeVM 行为，不开放 hidden tests，不把 LLM 或 Codex 变成生命体大脑。<br />Clear boundary: this is host-side public evidence only; it does not change CIL / LifeVM behavior, expose hidden tests, or turn LLMs / Codex into the organism's brain.

<div align="center">

<img src="https://raw.githubusercontent.com/huachabobo/huachabobo/main/assets/codelife-lab-card.svg?v=20260614-dual-core" alt="CodeLife Lab digital life research card" />

</div>

## Now Building / 当前在做

<div align="center">

<img src="https://raw.githubusercontent.com/huachabobo/huachabobo/main/assets/lecia-agentos-now-building.svg?v=20260614-dual-core" alt="Now building terminal status bar" />

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
| `CodeLife Lab` | 非 LLM 数字生命实验平台，当前重点是 public lineage diagnostics、mutation/operator evidence 与 CI 绿的研究闭环。 | A non-LLM digital-life lab focused on public lineage diagnostics, mutation/operator evidence, and CI-backed research loops. |
| [vc-daily-brief-agent](https://github.com/huachabobo/vc-daily-brief-agent) | 把 YouTube 与 RSS 信号整理成移动优先、可解释的飞书 VC 简报。 | Turns YouTube and RSS signals into mobile-first, explainable Feishu VC briefings. |
| [astrbot_plugin_mimo_tts_decorator](https://github.com/huachabobo/astrbot_plugin_mimo_tts_decorator) | 一个给 AstrBot 使用的 MiMo TTS 装饰器，支持自动打标、清洗与调试开关。 | A MiMo TTS decorator for AstrBot with auto-tagging, cleanup, and debugging switches. |
| [MaiBot](https://github.com/huachabobo/MaiBot) | 一个更关注长期理解与真实交互质感的 LLM 数字生命实验。 | An LLM digital-life experiment focused on long-horizon understanding and more human interaction texture. |

## Focus / 关注方向

`AgentOS` `LLM Runtime` `Digital Life` `Evidence Systems` `Self-hosted AI` `Governance` `Operator UX` `Automation` `Docs as Product` `TypeScript` `Python`

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
