# Glossary / 术语表

| Term | 中文说明 |
| --- | --- |
| Advisory artifact | 供人审阅的建议性产物，例如 verdict、review session、data health report。不是 committed state。 |
| Approved Opportunity | 私有环境中由人明确确认后进入 tracker 的机会。公开镜像不包含真实数据。 |
| Auto-apply | 自动投递岗位。公开镜像禁止，也不包含实现。 |
| Candidate Intake Inbox | 机会进入正式 candidate pool 前的缓冲层，用来处理片段、不完整 JD 和手动输入。 |
| Candidate Pool | 人确认后的候选机会集合。状态变化仍由人控制。 |
| Committed state | 已被人确认并进入长期状态的记录，例如 active strategy 或 approved opportunity。 |
| Data Health Report | 描述数据完整性、缺失字段、歧义和 blocked actions 的产物。 |
| Data Sufficiency Gate | 判断输入是否足够支持 verdict 的门禁。稀疏 snippet 不能生成高置信 full verdict。 |
| Decision Ownership Gate | 防止 AI 自动推进、拒绝、归档、投递或发送消息的门禁。 |
| Draft | AI 或系统生成的待审阅内容。Draft 不是承诺。 |
| External Side Effect Gate | 阻断消息发送、投递、平台抓取、workflow dispatch 等外部动作的门禁。 |
| Human Review Decision | 人类 reviewer 明确确认的 review 结果。公开 demo 中只使用模拟决策。 |
| Opportunity Verdict | 对机会匹配度、风险、证据和缺失信息的 advisory verdict。 |
| Public Mirror Gate | 决定文件是否可以进入公开镜像的隐私与脱敏门禁。 |
| Review Session | 把 verdict 转成问题、证据和下一步选项的人工 review agenda。 |
| Strategy Ownership Gate | 防止 AI 自动覆盖 active career strategy 的门禁。 |
| Validation-runnable | 可以运行本地 schema/demo/eval 验证。 |
| Production-runnable | 可以端到端运行真实产品。这个公开镜像不是 production-runnable。 |
