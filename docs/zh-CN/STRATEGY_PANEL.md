# Agent 策略面板

## 产品定位

Career Planning Agent 是一个 local-first 的职业机会 review 决策支持系统。
它组织个人 context、career strategy、opportunity evidence、verdicts 和 review decisions，
同时把职业承诺保持为 human-owned。

这个产品不是 auto-apply workflow。更强的 agentic behavior 应该意味着更好的 context handling、
更好的 evidence organization、更好的 uncertainty surfacing 和更好的 review sessions，
而不是静默外部动作。

## Stakeholder View

- User：希望职业决策更清晰，但不失去控制权。
- Reviewer：希望看到 evidence、gates 和 evals，证明 Agent 是安全可审阅的。
- Builder：希望沉淀一个 personal-data agent workflow 的可复用模式。
- Future maintainer：希望公开 artifact 可以审阅，但不会暴露私有源代码或私有职业数据。

## 为什么 Human-In-The-Loop 重要

职业动作会影响声誉、薪酬、关系和长期路径。因此产品必须把 draft intelligence 与 committed action
分开。

## 为什么 More Agent 不等于 Auto Apply

更多 Agent 能力应该表现为更稳的上下文处理、更清晰的证据、更强的 gate checks 和更有用的 review
sessions，而不是静默投递、发消息、覆盖策略或改变状态。

## Operating Doctrine

- Draft before commit.
- Context before verdict.
- Missing information before confidence.
- Human ownership before career action.
- Privacy gate before public artifact.
- Validation before portfolio publication.

## 核心产品判断

| 判断 | 产品含义 |
| --- | --- |
| 职业数据是个人运营数据 | 真实 profile、context、resume、JD 和 tracker state 默认私有。 |
| 机会输入经常不完整 | full verdict 前必须有 Data Sufficiency Gate。 |
| Verdict 是建议，不是行动 | advance、reject、archive、apply、message 前必须有人类 review。 |
| Strategy change 是承诺 | strategy application 是 human-owned state transition。 |
| 公开镜像需要独立安全门禁 | 只有虚构、模拟、脱敏 artifact 可以进入本仓库。 |

## Portfolio Talking Points

- workflow-first agent design
- schema-first contracts for verdict and review decisions
- privacy-first public mirror design
- simulated eval cases for human-review boundaries
- clear external side-effect gate
- local-first pattern for personal-data agents
- decision traceability without telemetry by default

## 风险与缓解

| 风险 | 缓解 |
| --- | --- |
| AI 夸大岗位匹配度 | Data Sufficiency Gate 和 human review |
| 私有数据进入公开 artifact | Public Mirror Gate 和 demo sanitation |
| Agent 提交职业动作 | Decision Ownership Gate 和 Approval Gate |
| 外部副作用静默发生 | External Side Effect Gate |
| Active strategy 被覆盖 | Strategy Ownership Gate |
| 稀疏职位片段变成过度自信 verdict | Data Sufficiency Gate |
| Public demo 被误认为生产输出 | 显式 simulated / sanitized markers |

## Roadmap

- broaden eval cases for ambiguous roles
- add browser-level review-session QA
- strengthen stale context detection
- keep public mirror generated from sanitized artifacts only
- consider read-only mock screenshots from simulated data only
