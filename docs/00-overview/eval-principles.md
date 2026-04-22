# Evaluation Principles / 评测原则

## English

Agent evaluation is not one thing. It usually mixes at least five layers:

1. Offline benchmark performance
2. Task success on realistic workflows
3. Safety and policy behavior
4. Reliability under distribution shift and edge cases
5. Operational health in production

Strong teams separate these layers instead of collapsing them into a single score.

Practical principles:

- Start with failure analysis before building dashboards.
- Prefer task-specific evals over generic vanity metrics.
- Keep a small manually reviewed dataset early on.
- Validate any LLM-as-a-judge prompt against human labels before trusting it.
- Track both quality and cost: latency, token usage, tool calls, retries, and human escalation rates.
- For agents, evaluate the full trace, not only the final answer.
- Use benchmarks to compare research progress, but use application-specific evals to ship product decisions.

Common failure modes:

- Good benchmark scores but poor tool use
- Strong final answers with brittle intermediate reasoning
- Judge drift after prompt changes
- Hidden regressions in multi-turn or long-horizon tasks
- Safety issues that only appear at scale or in rare cases

## 中文

Agent 评测不是单一动作，通常至少包含五层：

1. 离线基准表现
2. 真实任务工作流中的任务成功率
3. 安全与策略行为
4. 在分布偏移与边界案例下的稳定性
5. 生产环境中的运行健康度

成熟团队通常会把这些层分开看，而不是压缩成一个总分。

实用原则：

- 先做失败分析，再做仪表盘。
- 优先做任务定制型 eval，而不是追求泛化但空洞的指标。
- 早期一定要保留一小批人工复核样本。
- 任何 LLM-as-a-judge 在正式使用前，都应先和人工标注对齐验证。
- 质量和成本要一起看：延迟、Token 消耗、工具调用次数、重试次数、人工接管率。
- 对 Agent 来说，不能只评最终答案，还要评完整 trace。
- Benchmark 适合比较研究进展，产品上线决策更依赖应用特定 eval。

常见失败模式：

- Benchmark 很高，但工具调用很差
- 最终答案看起来不错，但中间步骤极不稳定
- Judge prompt 一改，评测标准就漂移
- 多轮或长任务中出现隐藏回归
- 一些安全问题只有在大规模或极少数场景下才暴露
