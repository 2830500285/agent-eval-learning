# From Zero to First Eval / 从零搭出第一套 Eval

## English

This playbook is for a small team that has no formal eval process today.

### Week 1: capture failure reality

1. Export 50 to 100 real user cases
2. Label the top failure categories
3. Identify one business-critical workflow
4. Decide the release decision the eval will support

Deliverable:

- a spreadsheet or JSONL with labeled examples

### Week 2: define the first dataset and judge

1. Clean the examples
2. Add metadata fields
3. Write a simple rubric
4. Choose one deterministic evaluator and one judge-based evaluator

Deliverable:

- a stable v0 eval dataset

### Week 3: connect a tool

Choose one path:

- Promptfoo if you want the fastest CI-ready config
- LangSmith if you want trace-centric experiments
- Langfuse if you want observability and eval in one system

Deliverable:

- one command that anyone on the team can run

### Week 4: create the release gate

1. Set pass thresholds by category
2. Define who reviews failures
3. Decide what blocks deploys
4. Run one real change through the process

Deliverable:

- a working release gate, even if imperfect

## 中文

这份 playbook 适合当前还没有正式 eval 流程的小团队。

### 第 1 周：先看到真实失败

1. 导出 50 到 100 条真实用户案例
2. 标出最主要的失败类别
3. 选一个业务最关键的工作流
4. 明确 eval 将支持什么发布决策

交付物：

- 一个带标签的表格或 JSONL

### 第 2 周：定义第一版 dataset 和 judge

1. 清洗样本
2. 增加元数据字段
3. 写一个简单 rubric
4. 选一个确定性 evaluator 和一个 judge 型 evaluator

交付物：

- 一个稳定的 v0 eval 数据集

### 第 3 周：接入工具

三条常见路径：

- 如果你要最快进 CI，用 Promptfoo
- 如果你要 trace 驱动实验，用 LangSmith
- 如果你要 observability 和 eval 一体化，用 Langfuse

交付物：

- 一个任何团队成员都能跑起来的命令

### 第 4 周：建立发布门槛

1. 按失败类别设阈值
2. 定义谁来复核失败
3. 明确什么情况下阻止发布
4. 拿一次真实改动走完整流程

交付物：

- 一套能工作的发布门槛，即使它还不完美
