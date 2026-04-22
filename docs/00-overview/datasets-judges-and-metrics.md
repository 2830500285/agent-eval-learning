# Datasets, Judges, and Metrics / 数据集、Judge 与指标设计

## English

This page answers the practical question teams usually struggle with: what exactly should go into an eval row, how should it be graded, and which metrics actually matter?

### A good eval row

For most applications, a dataset row should include:

- raw input
- reference output if one exists
- metadata such as user segment, locale, task type, and risk class
- expected tool behavior when tools are involved
- failure category labels
- reviewer notes

If you only store `input -> output`, your dataset will be too weak for debugging.

### Reference outputs are not always mandatory

You do not always need one gold answer. For open-ended tasks, store:

- rubric bullets
- unacceptable behaviors
- must-include facts
- style or policy constraints

This is often a better fit for summarization, planning, support, and agent trajectories.

### Judge types

#### 1. Deterministic checks

Best for:

- JSON validity
- schema compliance
- exact facts
- code compilation or unit tests

Use deterministic checks whenever possible because they are cheap and stable.

#### 2. Heuristic checks

Best for:

- presence of citations
- number of tool calls
- response length bounds
- refusal formatting

Heuristics are imperfect, but they catch many obvious regressions.

#### 3. LLM-as-a-judge

Best for:

- helpfulness
- completeness
- instruction following
- answer groundedness
- rubric-based qualitative scoring

Use LLM judges with clear rubrics and human calibration, not as magic truth oracles.

#### 4. Human review

Best for:

- ambiguous edge cases
- policy-sensitive outputs
- high-value customer journeys
- disagreement arbitration

Human review is expensive, so reserve it for where it buys the most clarity.

### Metrics that matter

Useful metrics differ by system.

For general assistants:

- pass rate
- major error rate
- refusal correctness
- hallucination rate

For RAG:

- retrieval hit rate
- citation grounding
- answer faithfulness
- latency and cost

For agents:

- task success
- tool misuse rate
- unnecessary step count
- session completion time
- recovery-from-error rate

### Judge validation checklist

- Compare judge decisions with human labels
- Estimate agreement by category, not only overall
- Review false positives and false negatives
- Freeze rubrics during experiments when possible
- Re-validate after major prompt or model changes

## 中文

这一页回答团队最常卡住的三个问题：一条 eval 样本到底该存什么，应该怎么评分，哪些指标才真的有价值。

### 一条好的 eval 样本应该包含什么

对大多数应用来说，一条数据最好至少包含：

- 原始输入
- 参考输出（如果有）
- 元数据：用户类型、语言、任务类型、风险等级
- 如果涉及工具，还要记录期望工具行为
- 失败类别标签
- 复核备注

如果你只保存 `input -> output`，这个数据集基本不够调试。

### 参考答案不是永远必须的

很多开放任务并不适合只给一个标准答案。可以存：

- rubric 要点
- 明确不允许出现的行为
- 必须覆盖的事实
- 风格或策略约束

这对摘要、规划、客服、Agent 轨迹类任务通常更合适。

### Judge 的四种常见类型

#### 1. 确定性检查

适合：

- JSON 是否合法
- 是否符合 schema
- 明确事实是否正确
- 代码能否编译或通过测试

只要能用确定性检查，就优先用，因为它最便宜、最稳定。

#### 2. 规则或启发式检查

适合：

- 是否包含引用
- 工具调用次数
- 回复长度约束
- 拒答格式

它不完美，但能抓住很多明显回归。

#### 3. LLM-as-a-judge

适合：

- 是否有帮助
- 是否完整
- 是否遵循指令
- 是否基于证据
- 基于 rubric 的质量评分

前提是 rubric 清晰，并且做过人工校准，不能把它当“真理机器”。

#### 4. 人工审核

适合：

- 模糊边界案例
- 策略敏感输出
- 高价值用户路径
- 作为 judge 分歧的仲裁机制

人工审核很贵，所以应当只用在最值得的位置。

### 真正有用的指标

不同系统关心的指标不同。

通用助手常看：

- 通过率
- 严重错误率
- 拒答正确率
- 幻觉率

RAG 常看：

- 检索命中率
- 引用是否真实支撑答案
- 答案忠实度
- 延迟与成本

Agent 常看：

- 任务成功率
- 工具误用率
- 冗余步骤数量
- 会话完成时间
- 出错后恢复率

### Judge 校验清单

- 用人工标签对比 judge 结果
- 按类别看一致性，不只看总分
- 重点看误报和漏报
- 实验期间尽量冻结 rubric
- 大改 prompt 或模型后重新验证 judge
