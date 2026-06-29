# Career Planning Agent Week 3 Case Study

English mirror: [docs/case_study_career_planning_week3.md](../case_study_career_planning_week3.md).

## 1. Title

Career Planning Agent：local-first human-in-the-loop career decision workflow standardization。

## 2. Context

Career Planning Agent 起点是一个私有本地产品，用来组织职业 context、review opportunities，
并判断哪些机会值得进一步关注。Week 3 standardization 把这个项目整理成更清晰的 Agent 产品案例：
文档化 workflow，定义 privacy 和 autonomy boundaries，添加 schema contracts，添加无外部副作用
eval cases，并生成 sanitized demo artifacts。

这个公开 case study 只覆盖脱敏镜像。它不声称 demo artifacts 是真实职业数据、真实 JD、
真实投递记录或生产输出。

## 3. Problem

职业机会 review 噪声很高，也非常个人化。输入常常是不完整的 role snippets、不完整 JD、
模糊薪酬范围、分散的个人 constraints，或者已经过期的 profile assumptions。一个有用的 Agent
必须帮助整理 review，而不能把 private context 变成 public artifacts，也不能把 advisory drafts
变成现实承诺。

核心风险是 commitment leakage。没有显式门禁时，Agent 很容易把“看起来不错”误当成“推进机会”，
把“起草消息”误当成“发送消息”，把“建议策略变化”误当成“覆盖 active strategy”。在职业工作流中，
这些错误会影响声誉、薪酬、关系和长期路径。

## 4. Design Goal

Week 3 的目标是把 Career Planning Agent 标准化成 privacy-first、human-in-the-loop 的 Agent 案例：

- 让 workflow 从 user model 到 review decision 清晰可读。
- 区分 draft artifacts 和 committed career state。
- 文档化 human-owned career actions 和 external side-effect boundaries。
- 定义 Opportunity Verdict、Review Decision 和 Data Health Report 的 schemas。
- 添加禁止 auto-apply、auto-message、hidden platform actions 和 private-data leakage 的本地 eval definitions。
- 生成不含真实职业数据的 sanitized demo run。

## 5. Constraints

- 不导出生产源代码。
- 不使用真实 profile、context、resume、JD、salary、offer、employer、opportunity 或 tracker data。
- 不使用 localStorage dumps、导出的私有 app JSON、浏览器 sessions、私有 notes、private runtime outputs 或 private logs。
- 不触发 LinkedIn、Boss、猎聘、邮箱、消息、provider、scraper、application 或 workflow side effects。
- Demo output 必须是 deterministic、fictional、simulated、sanitized。
- External career actions 保持 human-owned，不属于公开镜像范围。

## 6. Architecture

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

架构围绕 review gates 组织，而不是单次 autonomous action。Parsing、summarization、
draft verdict generation、data health reporting 和 review-session preparation 可以在安全本地上下文中自动化。
Strategy application、opportunity advancement、rejection、messaging、application submission
和 committed tracker changes 必须由人拥有。

## 7. Human-In-The-Loop Workflow

Workflow 从 User Model 开始：profile facts、context、preferences、constraints、avoid signals
和 search scope。Career Strategy 把这个模型转成 draft path hypotheses 和 search direction。
Opportunity Discovery 与 Candidate Intake 在机会成为正式 candidate 之前充当缓冲层。

Opportunity Verdict 是 advisory。它总结 fit、evidence、risks、missing information 和 recommended
review direction。Review Session 再把 verdict 转成 human decision agenda：需要检查的问题、
证据和允许的 next-step options。Agent 不执行这些 options。人类 reviewer 决定 hold、advance、
reject、archive、request more information、revise strategy，或在私有环境中创建 approved opportunity。

详细 workflow 见 [docs/03_WORKFLOW.md](../03_WORKFLOW.md)。

## 8. Safety And Autonomy Model

Autonomy model 区分低风险本地 drafting 与职业承诺：

- Local schema validation 和 demo checks 是允许的。
- Profile、context、strategy、verdict 和 review artifacts 可以被 draft。
- Applying profile/context、applying strategy、changing opportunity status、
  creating approved opportunities、sending messages 和 applying to jobs 需要人类确认。
- External platform actions、scraping、hidden channel usage、auto-apply 和 auto-send
  在公开镜像中被禁止。

主要参考：[docs/04_AUTONOMY_MATRIX.md](../04_AUTONOMY_MATRIX.md)、
[docs/06_TOOLS_AND_PERMISSIONS.md](../06_TOOLS_AND_PERMISSIONS.md) 和
[docs/09_GATES_AND_GUARDRAILS.md](../09_GATES_AND_GUARDRAILS.md)。

## 9. Schema Contracts

Week 3 添加了三个公开 schema contracts：

- [schemas/opportunity_verdict.schema.json](../../schemas/opportunity_verdict.schema.json)
  定义 advisory verdict shape。
- [schemas/review_decision.schema.json](../../schemas/review_decision.schema.json)
  定义 human-confirmed review decision shape。
- [schemas/data_health_report.schema.json](../../schemas/data_health_report.schema.json)
  定义 completeness、ambiguity 和 blocked-action reporting。

这些是 sanitized artifacts 的公开 review contracts。它们不证明私有 runtime emission 已包含在本镜像中。

## 10. Eval Suite

Week 3 在 [evals/career_planning_eval_cases.jsonl](../../evals/career_planning_eval_cases.jsonl)
中添加了 10 个本地 eval case definitions。覆盖 sparse JD handling、avoid-signal conflicts、
missing user background、missing context、no auto-advance、no auto-approved opportunity、
no strategy overwrite、salary ambiguity、snippet-only inputs 和 public-demo privacy。

静态检查器 [evals/check_career_planning_eval_cases.py](../../evals/check_career_planning_eval_cases.py)
校验 case file 和 safety invariants。它只在本地运行：不 import production code，不调用外部 API，
不调用 LLM，不抓取平台，不发消息，不投递岗位，不更新 tracker，也不运行私有 app。

Runtime eval integration 不属于公开镜像范围。

## 11. Sanitized Demo Run

[demo_run/](../../demo_run/) 下的 deterministic demo 只使用虚构实体：

- Candidate: `Fictional Candidate A`
- Company: `ExampleCo Labs`
- Opportunity: `DEMO-OPP-001`
- Role: `Product Operations AI Analyst`

Demo 包含 draft profile summary、draft career strategy、candidate intake item、data health report、
opportunity verdict、review session、human-confirmed review decision 和 demo output summary。

Demo 不是真实投递，不是已发送消息，不是真实职位记录，不是真实职业建议，也不是生产运行。

## 12. Implemented Vs Omitted Vs Out Of Scope

| 领域 | 状态 | 说明 |
| --- | --- | --- |
| Workflow documentation | implemented | User model、strategy、intake、verdict、review 和 approval boundaries 已文档化。 |
| Autonomy and gate docs | implemented | Human-owned commitments 和 external side effects 已显式 gate。 |
| Advisory schemas | implemented | 包含 3 个公开 JSON schemas。 |
| Static eval definitions | implemented | 存在 10 个无外部副作用 cases。 |
| Static eval checker | implemented | 本地 checker 校验 eval structure 和 safety invariants。 |
| Sanitized demo run | implemented | Demo artifacts 是 deterministic fictional examples。 |
| 中文 README 和精选文档 | implemented | 已包含中文 review docs。 |
| Production source code | omitted | 镜像是 portfolio evidence bundle，不是 source export。 |
| Real career data | omitted | 不含真实 profile、resume、JD、salary、offer、employer 或 application data。 |
| External career actions | out of scope | 不存在投递、消息、抓取或平台动作能力。 |
| Private runtime eval integration | out of scope | Runtime behavior 属于私有项目。 |

## 13. Lessons Learned

- Human-in-the-loop 是产品架构，不是免责声明。
- 职业 Agent 必须严格区分 draft advice 与 committed action。
- 对不完整 JD 来说，Data Sufficiency Gate 和模型质量同样重要。
- Personal-data agent 的公开镜像需要自己的 privacy gate。
- Schema contracts 让 advisory outputs 和 human decisions 更容易审阅。
- Sanitized demo 可以让 workflow 可检查，同时不暴露个人数据或触发外部职业渠道。

## 14. Next Steps

- 保持 public portfolio artifacts 与 sanitized schemas 和 demos 同步。
- 当私有项目有稳定且可安全抽象的例子时，增加更细的 stale-context 和 compensation-ambiguity eval cases。
- 只基于 sanitized mock data 考虑 read-only UI screenshots 或 diagrams。
- 继续把生产源代码、私有职业数据和 external action paths 留在 curated public mirror 之外。
