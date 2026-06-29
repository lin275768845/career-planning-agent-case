# Career Planning Agent

English primary version: [README.md](README.md). 中文术语说明见
[docs/zh-CN/GLOSSARY.md](docs/zh-CN/GLOSSARY.md)。

## 战略摘要：为什么这不是自动投递助手

Career Planning Agent 的目标不是自动帮人投简历，而是把分散的个人背景、不完整的 JD、职位片段、
职业偏好和风险信号，整理成可审阅、可追踪、可人工确认的职业决策产物。

这个项目真正难的地方不是让模型“更主动”，而是控制承诺边界。职业选择会影响声誉、薪酬、时间、
关系和长期路径。AI 可以解析、总结、比较、提问、起草和整理证据，但不能静默投递、发消息、
覆盖职业策略、推进机会、拒绝机会，或创建已经承诺的 tracker 状态。一个更可靠的职业 Agent
应该让决策面更清晰，同时把职业承诺留给人。

这个脱敏公开镜像展示的是私有 Career Planning Agent 中可复用的方法：本地优先的个人数据边界、
draft 与 committed state 的分离、机会 intake 与 review 工作流、数据充分性门禁、
决策所有权门禁、外部副作用门禁、advisory artifact 的 schema 契约、无外部副作用 eval cases，
以及可以安全公开审阅的模拟 demo outputs。

## 公开案例镜像定位

本仓库是一个脱敏公开作品集镜像，面向架构审阅、工作流审阅、隐私边界审阅、
human-in-the-loop 产品审阅、schema/eval 审阅和案例研究。

它是 validation-runnable，不是 production-runnable。它不是完整生产仓库副本，也不连接真实职业数据。
私有本地项目仍然独立保留。

生产源代码、私有 app state、真实 profile/context、真实简历内容、真实 JD、导出的 app JSON、
localStorage dumps、私有机会 tracker、外部账号数据和 secrets 都被有意排除。

推荐先阅读：

- [公开镜像范围说明](docs/zh-CN/PUBLIC_MIRROR_SCOPE.md)
- [Agent 策略面板](docs/zh-CN/STRATEGY_PANEL.md)
- [架构总览](docs/zh-CN/ARCHITECTURE_OVERVIEW.md)

## 这个公开镜像是什么

- 基于私有本地职业规划 Agent 整理出的脱敏作品集镜像。
- 用来展示 human-owned career decision workflow 的案例仓库。
- 适合审阅隐私边界、工作流门禁、schema、eval cases 和模拟 demo artifacts。
- 一个紧凑的 evidence bundle，展示产品形状，但不暴露个人职业数据或生产源代码。

## 这个公开镜像不是什么

- 不是完整 app 仓库。
- 不是私有项目的完整 clone。
- 不连接真实 LinkedIn、Boss、BOSS career platform、猎聘、邮箱、消息、provider、scraper 或投递渠道。
- 不承诺 clone 后复现私有本地 app。
- 不存放真实简历、真实薪酬信息、真实 offer、真实 JD、私有笔记、localStorage dumps 或导出的 app state。
- 不能投递岗位、发送消息、抓取平台或更新已承诺的职业状态。

## 适合审阅的内容

- 从 profile/context 建模到 strategy、intake、verdict、review session 和人工确认 decision 的工作流设计。
- 把 draft generation 与 committed career action 分开的自治边界。
- 个人数据工作流的隐私门禁和公开镜像门禁。
- 防止 snippet-only 输入变成高置信 verdict 的数据充分性门禁。
- Opportunity Verdict、Review Decision、Data Health Report 的 JSON schema 契约。
- `evals/` 下无外部副作用的 eval cases 和本地静态检查器。
- `demo_run/` 下脱敏、模拟的 demo artifacts。

## 可以本地运行的安全检查

这些检查只读本地文件，不需要 secrets、provider keys、浏览器 session、平台登录，也不会产生外部副作用：

```bash
python3 scripts/validate_public_mirror.py
python3 -m unittest discover -s tests
```

底层检查也可以单独运行：

```bash
python3 -m json.tool schemas/opportunity_verdict.schema.json >/dev/null
python3 -m json.tool schemas/review_decision.schema.json >/dev/null
python3 -m json.tool schemas/data_health_report.schema.json >/dev/null
for f in demo_run/*.json; do python3 -m json.tool "$f" >/dev/null; done
python3 evals/check_career_planning_eval_cases.py
```

完整私有本地 app 不属于这个公开镜像的可运行范围。

## 有意排除的内容

- 生产源代码。
- `.env`、`.env.*`、token 文件、webhook 配置、cookies、keys 和 secrets。
- 真实 profile、career context、简历、JD、薪酬数据、offer、雇主备注和机会 tracker。
- 真实 LinkedIn exports、Boss career platform exports、猎聘 exports 或其他外部平台数据。
- 从私有 app state 导出的 JSON。
- localStorage dumps、浏览器 session 数据、私有日志和私有 runtime outputs。
- 生产 prompts、provider integrations、scraper code、message-send logic、auto-apply logic 和私有 runbooks。
- 本机私有路径和机器相关配置。

## 可运行性边界

本镜像服务于架构审阅、安全姿态审阅、schema、eval definitions 和脱敏 demo。
它是 validation-runnable，不是 production-runnable。

端到端生产运行需要私有 app 源代码、本地 state、用户拥有的职业数据、credentials、浏览器 session、
provider 配置、外部渠道权限和明确的人类批准。这些内容都不在公开镜像中。

## 当前实现状态

| 领域 | 公开镜像状态 | 说明 |
| --- | --- | --- |
| 核心工作流文档 | 已实现 | Workflow、autonomy、tools、gates、eval plan、observability 和 runbook 已文档化。 |
| Advisory artifact schemas | 已实现 | `schemas/` 中包含 Opportunity Verdict、Review Decision 和 Data Health Report schema。 |
| 静态 eval definitions | 已实现 | JSONL 中定义了 10 个无外部副作用 eval cases。 |
| 静态 eval checker | 已实现 | 本地检查器校验 eval definitions 和安全不变量。 |
| Public validation harness | 已实现 | `scripts/validate_public_mirror.py` 和 `tests/` 校验 schemas、evals、demo safety markers 和 public gates。 |
| Demo-only helper package | 已实现 | `career_planning_agent_public/` 只包含面向公开 artifact 的标准库 gate/rule helpers。 |
| Runtime eval integration | 不在公开镜像范围内 | 本镜像校验 definitions 和 demo artifacts，不校验私有 runtime behavior。 |
| 脱敏 demo run | 已实现 | Demo artifacts 是确定性、虚构、明确模拟的数据。 |
| 中文 README 和精选文档 | 已实现 | 中文镜像文档位于 `README.zh-CN.md` 和 `docs/zh-CN/`。 |
| 生产源代码 | 已省略 | 公开镜像有意排除私有 app 实现。 |
| 外部职业动作 | 禁止 | 投递、发消息、抓取平台和外部渠道动作都不属于本镜像。 |

## 工作流概览

```text
User Model
  -> Career Strategy
  -> Opportunity Discovery
  -> Candidate Intake Inbox
  -> Candidate Pool
  -> Opportunity Verdict
  -> Review Session
  -> Human Review Decision
  -> Optional Private Approved Opportunity
```

公开镜像保留了让这条工作流可审阅的文档、schema、evals 和脱敏 demo artifacts。
它不包含端到端运行私有 app 所需的源代码或个人数据。

## 产物地图

| 产物 | 用途 |
| --- | --- |
| [docs/zh-CN/PUBLIC_MIRROR_SCOPE.md](docs/zh-CN/PUBLIC_MIRROR_SCOPE.md) | 说明公开镜像包含什么、不包含什么，以及可运行性边界。 |
| [docs/REVIEWER_GUIDE.md](docs/REVIEWER_GUIDE.md) | Reviewer 建议阅读路径和 validation artifacts。 |
| [docs/DEMO_WALKTHROUGH.md](docs/DEMO_WALKTHROUGH.md) | 脱敏虚构 demo run 的逐步说明。 |
| [docs/zh-CN/STRATEGY_PANEL.md](docs/zh-CN/STRATEGY_PANEL.md) | 说明 human-owned career decisions 的产品原则。 |
| [docs/zh-CN/ARCHITECTURE_OVERVIEW.md](docs/zh-CN/ARCHITECTURE_OVERVIEW.md) | 用图示说明工作流、门禁、可观测对象和公开/私有边界。 |
| [docs/03_WORKFLOW.md](docs/03_WORKFLOW.md) | 从 user model 到 review decision 的工作流说明。 |
| [docs/04_AUTONOMY_MATRIX.md](docs/04_AUTONOMY_MATRIX.md) | 自治边界和人工批准点。 |
| [docs/05_DATA_MODEL.md](docs/05_DATA_MODEL.md) | Draft、active、advisory、committed 和 demo data classes。 |
| [docs/09_GATES_AND_GUARDRAILS.md](docs/09_GATES_AND_GUARDRAILS.md) | 隐私、数据充分性、决策所有权和公开镜像门禁。 |
| [schemas/opportunity_verdict.schema.json](schemas/opportunity_verdict.schema.json) | Advisory verdict schema contract。 |
| [schemas/review_decision.schema.json](schemas/review_decision.schema.json) | Human-confirmed review decision schema contract。 |
| [schemas/data_health_report.schema.json](schemas/data_health_report.schema.json) | 数据完整性与 blocked-action schema contract。 |
| [evals/career_planning_eval_cases.jsonl](evals/career_planning_eval_cases.jsonl) | 无外部副作用的 eval case definitions。 |
| [evals/check_career_planning_eval_cases.py](evals/check_career_planning_eval_cases.py) | 本地静态检查器。 |
| [scripts/validate_public_mirror.py](scripts/validate_public_mirror.py) | 标准库 public mirror validator。 |
| [tests/](tests/) | 覆盖 schemas、eval cases、demo safety markers 和 gate helpers 的 unittest。 |
| [career_planning_agent_public/](career_planning_agent_public/) | 只用于公开 demo/gate/rule 校验的 helper package。 |
| [.github/workflows/validate.yml](.github/workflows/validate.yml) | 不使用 secrets、无部署的 GitHub Actions validation workflow。 |
| [demo_run/demo_output_summary.md](demo_run/demo_output_summary.md) | 脱敏模拟 demo summary。 |
| [docs/zh-CN/case_study_career_planning_week3.md](docs/zh-CN/case_study_career_planning_week3.md) | 中文案例研究草稿。 |

## 公开仓库结构

```text
.
├── career_planning_agent_public/ # 只用于 demo/gate/rule 校验
├── demo_run/                # 脱敏模拟 demo artifacts
├── docs/                    # 架构、工作流和安全文档
│   └── zh-CN/               # 面向作品集审阅的中文镜像文档
├── evals/                   # 无外部副作用的静态 eval cases 和 checker
├── scripts/                 # Public mirror validation harness
├── schemas/                 # Advisory artifact schema contracts
├── tests/                   # 标准库 unittest
├── .github/workflows/       # Validation workflow，无部署、无 secrets
├── README.md
└── README.zh-CN.md
```

## 脱敏演示产物

`demo_run/` 目录中的产物是确定性、脱敏、模拟生成的样例。它们用于展示产物形态和安全姿态，
不使用真实个人数据。

包含的 demo artifacts：

- `demo_profile_summary.json`
- `demo_career_strategy.json`
- `demo_candidate_intake_item.json`
- `demo_data_health_report.json`
- `demo_opportunity_verdict.json`
- `demo_review_session.md`
- `demo_review_decision.json`
- `demo_output_summary.md`

这些文件不是真实职业建议，不是真实机会记录，不是真实投递历史，也不是生产输出。

## 安全姿态

- 不提交 `.env`、secrets、tokens、cookies、webhooks、私有日志或真实凭据。
- 不把真实简历、JD、薪酬信息、offer、雇主备注、联系方式、导出的 app state、
  localStorage dumps 或私有职业笔记放进公开镜像。
- 私有 app state、private outputs 和 private opportunity trackers 应视为个人运维产物。
- 日志和摘要必须保持脱敏，不输出完整 prompts、完整 private profile text、真实 JD payloads、
  浏览器 session 数据、HTTP headers、secrets 或 webhook URLs。
- 外部投递、发送消息、平台抓取、workflow dispatch 和 committed opportunity state changes
  仍然是公开镜像之外的人类拥有动作。

## 维护原则

- README 聚焦架构、工作流、安全边界、evals、schemas 和脱敏 demos。
- 私有源代码、私有 runbooks、prompts、app state、exports 和个人职业数据留在公开镜像之外。
- 更新文档时，必须区分已实现、省略、模拟、不在范围内和私有环境能力。
- 更新 demo 时，只使用虚构实体和模拟 ID。
- 更新 evals 时，保持外部副作用在设计上被禁止。

## License / 使用限制

License not yet specified。本仓库用于作品集审阅；除非后续添加 license，否则不授予复用权利。
