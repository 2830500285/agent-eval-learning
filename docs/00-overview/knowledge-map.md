# Knowledge Map / 知识地图

## English

This repository organizes agent evaluation knowledge into four major buckets:

### 1. Research and benchmarks

Use this layer to understand what a benchmark measures, what it ignores, and whether it transfers to your use case.

Examples:

- SimpleQA for factuality
- BrowseComp for browsing agents
- TruthfulQA for truthfulness

### 2. Applied product evals

This is the layer most teams actually need. It includes:

- golden datasets
- regression suites
- human review queues
- LLM judges
- online experiments

### 3. Safety and robustness evals

These focus on rare failures, sabotage, bias, prompt injection, policy evasion, and unknown unknowns.

### 4. Tooling and workflow

This covers the mechanics of running evals repeatedly:

- experiment tracking
- trace collection
- dataset versioning
- CI integration
- score dashboards

## 中文

本仓库把 Agent Eval Learning 的核心知识分成四个层次：

### 1. 研究与基准

这一层帮助你理解 benchmark 到底在测什么、忽略了什么，以及它是否真的能迁移到你的业务场景。

例如：

- SimpleQA：事实性
- BrowseComp：浏览型 Agent
- TruthfulQA：真实性

### 2. 应用型产品评测

这是大多数团队最需要的层：

- golden dataset
- 回归测试集
- 人工审核队列
- LLM judge
- 在线实验

### 3. 安全与鲁棒性评测

重点关注罕见失败、破坏行为、偏见、提示注入、策略绕过，以及“未知未知”。

### 4. 工具与流程

这一层解决的是“如何持续跑 eval”：

- 实验追踪
- trace 采集
- 数据集版本管理
- CI 集成
- 评分看板

## Cross-cutting questions / 横切问题

- What is the unit of evaluation: answer, step, trace, or session?
- Who is the judge: code, heuristics, humans, or another model?
- How expensive is the eval to run repeatedly?
- Can the eval catch regressions before users do?
- Does it reflect the actual product risk?
