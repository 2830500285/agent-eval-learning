# Hamel Husain / Hamel Husain

## English

Hamel Husain is one of the clearest practitioners writing about applied evals for real product teams.

### Recommended resources

1. LLM Evals: Everything You Need to Know
   - Link: https://hamel.dev/blog/posts/evals-faq/
   - Why it matters: Excellent practical FAQ on failure analysis, judge validation, synthetic data generation, and multi-step evaluation.

2. Using LLM-as-a-Judge for Evaluation: A Complete Guide
   - Link: https://hamel.dev/blog/posts/llm-judge/
   - Why it matters: Good starting point for understanding how to use model-based judges without fooling yourself.

3. Evals Skills for Coding Agents
   - Link: https://hamel.dev/blog/posts/evals-skills/
   - Why it matters: Connects eval design to modern coding-agent workflows and applied harness design.

### Core lessons

- Error analysis comes before metrics
- Domain experts matter more than generic labelers
- Agent evals should capture traces, not only final outputs
- Synthetic data is useful, but only after you understand real failure patterns

### How to apply Hamel's advice

1. Start every eval project with a manual failure review.
2. Make your taxonomy of failures before you make a dashboard.
3. Use domain reviewers on a small, high-signal sample.
4. Let synthetic data expand coverage only after the real categories are stable.

## 中文

Hamel Husain 是目前写“应用型 eval”最清楚的一批实践者之一，尤其适合产品和工程团队。

### 推荐内容

1. LLM Evals: Everything You Need to Know
   - 链接：https://hamel.dev/blog/posts/evals-faq/
   - 价值：从失败分析、judge 校准、合成数据、到多步骤评测，覆盖非常完整。

2. Using LLM-as-a-Judge for Evaluation
   - 链接：https://hamel.dev/blog/posts/llm-judge/
   - 价值：适合入门理解如何用模型来做 judge，同时避免自欺式评测。

3. Evals Skills for Coding Agents
   - 链接：https://hamel.dev/blog/posts/evals-skills/
   - 价值：把 eval 设计和 coding agent 的实际工作流连接起来。

### 核心观点

- 失败分析先于指标建设
- 领域专家往往比通用标注者更重要
- Agent Eval 要看 trace，而不是只看 final answer
- 合成数据有用，但前提是你先看懂真实失败模式

### 如何把 Hamel 的建议落地

1. 每个 eval 项目都先做人工失败复盘。
2. 先定义失败分类，再做 dashboard。
3. 用少量高价值样本引入领域专家复核。
4. 只有在真实失败类别稳定后，再用合成数据扩展覆盖面。
