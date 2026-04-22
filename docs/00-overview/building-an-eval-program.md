# Building an Eval Program / 搭建一套可运营的 Eval 体系

## English

The fastest way to waste time on evals is to start with tooling. Strong teams start with decisions, not dashboards.

### 1. Define the product decision

Ask what decision the eval is supposed to support:

- Should we ship this prompt change?
- Should we switch models?
- Is the agent reliable enough for beta users?
- Which failure modes still require human review?

If the eval cannot change a real decision, it will become reporting theater.

### 2. Choose the unit of evaluation

Different products need different evaluation units:

- final answer: useful for simple question answering
- full trace: necessary for agents and multi-step systems
- retrieval result set: necessary for RAG
- multi-turn session: necessary for support, tutoring, browsing, and coding agents

Many teams fail because they evaluate only the final answer while the real problem lives in the intermediate steps.

### 3. Build a small gold dataset first

Start with 30 to 100 examples that cover:

- common flows
- important edge cases
- costly failures
- policy-sensitive cases

For each row, store:

- input
- reference output when available
- failure category
- difficulty
- notes from human reviewers

This first dataset should be manually curated. Synthetic expansion comes later.

### 4. Separate evaluators by role

Use more than one evaluator when possible:

- exact or code-based checks for deterministic facts
- heuristic rules for format or tool behavior
- LLM judges for qualitative dimensions
- human review for ambiguous or high-risk cases

Do not let a single judge score everything. This creates blind spots and false confidence.

### 5. Validate the judge

Before trusting an LLM judge:

- sample 50 to 100 examples
- compare model judgments with human labels
- inspect disagreement cases
- rewrite the rubric until disagreement is understandable

Judge quality should be treated as its own evaluation problem.

### 6. Run experiments like a release process

A usable eval loop looks like this:

1. change prompt, model, tool, or workflow
2. run eval suite
3. inspect per-category failures
4. decide ship, fix, or rollback
5. log the new failure cases into the dataset

This is an evaluation flywheel, not a one-time benchmark.

### 7. Track operational metrics

For production systems, quality metrics are not enough. Also track:

- latency
- token cost
- tool calls per run
- retries
- escalation rate
- human override rate

Many "better" systems are only better because the cost was hidden.

### 8. Add online monitoring

Offline evals catch known failures. Online monitoring catches drift:

- prompt edits
- model updates
- traffic shifts
- new user intents

Use traces, annotations, and sampled review queues to keep the system honest after launch.

### 9. Establish release gates

Examples:

- no regression in top 3 business-critical categories
- no increase in safety policy failures
- p95 latency below threshold
- manual review passed for all high-risk samples

This is where evals stop being "research" and become engineering control systems.

## 中文

最容易把 eval 做废的方式，就是一上来先装工具。成熟团队先定义“它要服务什么决策”，而不是先做 dashboard。

### 1. 先定义评测要支持什么决策

先问清楚：

- 这个 prompt 改动能不能发？
- 要不要切换模型？
- 这个 agent 能不能开放给 beta 用户？
- 哪些失败模式仍然必须人工兜底？

如果一个 eval 不能影响真实决策，它很快就会沦为“展示型报表”。

### 2. 选对评测单位

不同系统，需要不同评测单位：

- 最终答案：适合简单问答
- 完整 trace：适合 Agent、多步骤系统
- 检索结果集：适合 RAG
- 多轮会话：适合客服、教学、浏览、代码 Agent

很多团队的根本问题是：只评 final answer，但真正的失败发生在中间步骤。

### 3. 先做一小批 gold dataset

先从 30 到 100 条开始，覆盖：

- 高频主流程
- 关键边界案例
- 高成本失败
- 策略敏感场景

每条样本最好至少存这些字段：

- 输入
- 参考答案（如果有）
- 失败类别
- 难度
- 人工复核备注

第一版数据集应该以人工整理为主，合成扩充放到后面。

### 4. 把 evaluator 分角色

尽量不要只靠一个 judge：

- 确定性事实用 exact match 或代码检查
- 格式与工具行为用规则或 heuristic
- 质量维度用 LLM judge
- 模糊或高风险场景用人工审核

如果一个 judge 什么都评，盲区会非常大。

### 5. 先验证 judge，再使用 judge

在正式信任 LLM judge 之前：

- 抽 50 到 100 条样本
- 用人工标签对比 judge 结果
- 重点看分歧案例
- 不断重写 rubric，直到分歧变得可解释

Judge 本身也应该被视为一个需要评测的系统。

### 6. 把实验流程做成发布流程

一套可用的 eval 闭环通常是：

1. 改 prompt、模型、工具或工作流
2. 跑 eval 套件
3. 看分类型失败
4. 决定上线、修复或回滚
5. 把新失败写回数据集

这才是 evaluation flywheel，而不是一次性的 benchmark。

### 7. 质量之外，还要看运营指标

生产系统不能只看质量，还要同时看：

- 延迟
- Token 成本
- 单次运行工具调用数
- 重试次数
- 升级到人工的比例
- 人工覆盖率

很多“质量更好”的方案，只是把成本藏起来了。

### 8. 加入线上监控

离线 eval 只能抓住已知失败，线上监控负责抓漂移：

- prompt 被修改
- 模型版本变化
- 流量结构变化
- 新型用户意图出现

上线之后，要靠 traces、annotations 和抽样复盘队列继续维持系统真实可靠。

### 9. 给发布设置门槛

例如：

- 业务最关键的 3 类样本不能回退
- 安全策略失败不能升高
- p95 延迟必须低于阈值
- 所有高风险样本必须通过人工复核

到了这一步，eval 才从“研究动作”变成真正的工程控制系统。
