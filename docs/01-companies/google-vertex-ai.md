# Google Cloud Vertex AI / Google Cloud Vertex AI

## English

Google has two eval stories worth separating:

- Google Research / DeepMind: strong experimental and benchmark thinking
- Vertex AI: practical enterprise workflows for running GenAI evaluations

This page focuses on Vertex AI because it is the more operational piece.

### What Vertex AI is strong at

- managed evaluation workflows
- prompt and model comparison
- pointwise and pairwise evaluation patterns
- integration with enterprise Google Cloud environments
- support for both custom metrics and model-based evaluation

### Practical adoption path

1. Define a dataset in BigQuery, JSONL, or managed storage
2. Decide whether you need pointwise scoring or pairwise comparison
3. Separate quality metrics from operational metrics
4. Run baseline evaluation on the current system
5. Compare new prompt, model, or grounding strategy against baseline
6. Review disagreements manually before promoting changes

### What to borrow from Google even if you do not use Vertex

- evaluate agent systems experimentally, not only anecdotally
- compare architectures under controlled conditions
- combine user-study evidence with automated scoring for high-stakes domains

### When Vertex AI is a good fit

- your stack is already on Google Cloud
- you need centralized governance and IAM controls
- you want managed evaluation instead of stitching together many tools

### Recommended source links

- Evaluation overview: https://cloud.google.com/vertex-ai/generative-ai/docs/models/evaluation-overview
- Run an evaluation: https://cloud.google.com/vertex-ai/generative-ai/docs/models/run-evaluation
- Evaluate prompts: https://cloud.google.com/vertex-ai/generative-ai/docs/models/prompt-management/evaluate-prompts
- Research blog on scaling agent systems: https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/

## 中文

Google 相关的 eval 内容其实分两条线：

- Google Research / DeepMind：更偏研究、benchmark、实验设计
- Vertex AI：更偏企业可运营的评测工作流

这一页重点讲 Vertex AI，因为它更接近“如何实际搭建”。

### Vertex AI 擅长的地方

- 托管式评测流程
- Prompt 和模型对比
- pointwise 与 pairwise 两类评测模式
- 与 Google Cloud 企业环境整合
- 支持自定义指标和模型型 judge

### 实操落地路径

1. 在 BigQuery、JSONL 或托管存储里准备数据集
2. 先判断你要的是 pointwise 打分还是 pairwise 对比
3. 把质量指标和运营指标分开
4. 先对当前系统跑 baseline
5. 再拿新 prompt、模型或 grounding 策略和 baseline 对比
6. 在正式上线前，人工检查分歧样本

### 即使不用 Vertex，也值得学 Google 的地方

- Agent system 要靠受控实验来评，而不是靠个别案例
- 架构比较必须在可控条件下进行
- 高风险领域里，用户研究与自动评分要结合

### 哪些团队适合 Vertex AI

- 你的栈本来就在 Google Cloud 上
- 你需要统一治理和 IAM 权限控制
- 你希望用托管服务而不是自己拼很多工具

### 参考资料

- Evaluation overview: https://cloud.google.com/vertex-ai/generative-ai/docs/models/evaluation-overview
- Run an evaluation: https://cloud.google.com/vertex-ai/generative-ai/docs/models/run-evaluation
- Evaluate prompts: https://cloud.google.com/vertex-ai/generative-ai/docs/models/prompt-management/evaluate-prompts
- Research blog on scaling agent systems: https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/
