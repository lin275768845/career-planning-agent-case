# 公开镜像范围

## 为什么存在这个镜像

这个镜像让 reviewer 可以检查产品架构、human-review workflow、隐私边界、eval suite、
schema contracts 和脱敏 demo，而不需要访问私有本地数据或生产 runtime state。

它是 validation-runnable，不是 production-runnable。目标是展示 Agent 产品设计的形状、
门禁和审阅证据，不是发布一个可部署的私有 app 副本。

## 包含内容

- `README.md`
- `README.zh-CN.md`
- 精选 workflow 和 architecture docs
- `docs/PUBLIC_MIRROR_SCOPE.md`
- `docs/ARCHITECTURE_OVERVIEW.md`
- `docs/STRATEGY_PANEL.md`
- `docs/zh-CN/` 下的精选中文镜像文档
- JSON schemas
- simulated eval suite
- sanitized demo run

## 排除内容

- 生产源代码
- 生产 prompts 和 provider integrations
- 真实 app state
- 真实个人职业数据
- 真实简历
- 真实 JD exports
- 真实薪酬、offer、雇主、联系人或投递数据
- 私有笔记
- 从本地 app 导出的 JSON
- `.env*`、tokens、secrets、keys、webhooks、cookies
- 外部账号数据
- 私有 runtime outputs
- 本机私有路径
- 浏览器 sessions 和 localStorage dumps
- scraping、auto-apply 和 message-send implementation

## 隐私边界

所有示例都是虚构的。镜像使用 Fictional Candidate A、ExampleCo Labs 和 `DEMO-OPP-001`
这样的模拟 ID。这里不代表任何真实的人、雇主、机会、薪酬、offer、消息或投递。

## 不是生产 clone

这个仓库不是私有 app 的可部署副本。它是面向作品集审阅的 evidence bundle。
它不连接真实招聘平台、邮箱、消息工具、provider accounts、浏览器 session 或私有本地 state。

## 没有外部副作用

这个镜像不会投递岗位、发送消息、抓取网站、访问外部渠道、更新已承诺机会状态，
也不会发布私有职业数据。

## 公开资格规则

一个文件只有满足以下条件，才适合进入公开镜像：

- 虚构或完全脱敏
- 不含 secrets 和本机私有路径
- 不含真实个人职业数据
- 如果看起来像 runtime output，必须明确标记为 simulated
- 对架构、workflow、gate、schema、eval 或作品集审阅有用

任何来自真实 profile、context、resume、JD、salary、offer、employer、opportunity、
browser session、localStorage、private note 或 exported app state 的内容，默认都是私有的。
