# Microsoft / Microsoft

## English

Microsoft contributes to the eval landscape through Azure AI evaluation workflows, Promptflow, and open projects such as `genai-evals`.

### What Microsoft is strong at

- enterprise evaluation workflows
- CI-friendly evaluation runs
- prompt-flow style pipeline testing
- integration with the Azure stack

### Practical adoption path

1. Define a flow or application boundary
2. Store evaluation data separately from live production logs
3. Run baseline evaluations in Azure or CI
4. Add a GitHub Action or pipeline gate
5. Use humans for high-risk disagreement review

### Why Microsoft matters even if you do not run Azure

- it treats eval as part of application lifecycle management
- it pushes toward CI-compatible evaluation
- it is useful for teams that want governance and enterprise rollout discipline

### Recommended source links

- Azure AI evaluation concepts: https://learn.microsoft.com/azure/ai-foundry/concepts/evaluation-evaluators
- Promptflow evaluation: https://microsoft.github.io/promptflow/how-to-guides/develop-a-dag-flow/run-and-evaluate-a-flow/index.html
- Microsoft GenAI Evals: https://github.com/microsoft/genai-evals

## 中文

Microsoft 在 eval 领域的重要性主要来自三部分：Azure AI 的评测工作流、Promptflow，以及像 `genai-evals` 这样的开源项目。

### Microsoft 擅长的地方

- 企业级评测流程
- 易于接入 CI 的评测运行方式
- 类 prompt-flow 的流程化测试
- 和 Azure 生态的深度整合

### 实操落地路径

1. 先定义 flow 或应用边界
2. 把评测数据和生产日志分开存储
3. 在 Azure 或 CI 里先跑 baseline
4. 给 GitHub Action 或流水线加门槛
5. 对高风险分歧样本保留人工审核

### 即使不用 Azure，也值得借鉴的点

- 它把 eval 当成应用生命周期的一部分
- 它强调 CI 可兼容的评测方式
- 很适合需要治理与企业发布纪律的团队参考

### 参考资料

- Azure AI evaluation concepts: https://learn.microsoft.com/azure/ai-foundry/concepts/evaluation-evaluators
- Promptflow evaluation: https://microsoft.github.io/promptflow/how-to-guides/develop-a-dag-flow/run-and-evaluate-a-flow/index.html
- Microsoft GenAI Evals: https://github.com/microsoft/genai-evals
