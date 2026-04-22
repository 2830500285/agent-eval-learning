# LangChain and LangSmith / LangChain 与 LangSmith

## English

LangChain is relevant to evals not because it invented evaluation, but because LangSmith turned traces, datasets, experiments, prompts, and evaluators into a coherent workflow.

### What LangSmith is strong at

- dataset-centric experiments
- trace-first debugging
- prompt iteration in a UI
- offline experiments plus online observability
- custom evaluators and prebuilt evaluators

### What to borrow even if you do not use the product

- treat datasets as versioned assets
- evaluate target functions, not just models
- preserve full traces for debugging
- compare experiments rather than staring at one score

### Practical setup path

1. Create a LangSmith account and API key
2. Turn on tracing in the application
3. Capture a week of representative traces
4. Convert interesting failures into a dataset
5. Write one deterministic evaluator and one rubric-based evaluator
6. Run experiments against prompt or model variants
7. Promote the best-performing configuration into staging

### When LangSmith is a good fit

- you already use LangChain or LangGraph
- you need detailed traces for agent debugging
- you want prompt playground, datasets, and experiments in one place
- your team is comfortable with cloud tooling

### When it is a weaker fit

- you need a completely local-first stack
- you mostly want YAML-based CI regression checks with minimal infrastructure
- you do not need trace-level debugging

### Recommended source links

- Evaluation quickstart: https://docs.langchain.com/langsmith/evaluation-quickstart
- Evaluation concepts: https://docs.langchain.com/langsmith/evaluation-concepts
- Observability quickstart: https://docs.langchain.com/langsmith/observability-quickstart
- How to evaluate an agent: https://docs.langchain.com/langsmith/evaluate-agent

## 中文

LangChain 在 eval 领域真正重要的地方，不是它“发明了评测”，而是 LangSmith 把 trace、dataset、experiment、prompt 和 evaluator 串成了一整套工作流。

### LangSmith 最强的地方

- 以数据集为中心的实验管理
- 以 trace 为中心的问题定位
- 在 UI 中快速改 prompt
- 离线实验和线上观测打通
- 支持自定义 evaluator 和预置 evaluator

### 即使你不用 LangSmith，也值得借鉴的做法

- 把 dataset 当成需要版本化的资产
- 评估 target function，而不是只评模型
- 保留完整 trace 方便调试
- 比较实验结果，而不是只盯单一分数

### 实操落地路径

1. 创建 LangSmith 账号和 API key
2. 给应用接入 tracing
3. 先采集一周左右的真实 traces
4. 把有代表性的失败整理成 dataset
5. 至少写一个确定性 evaluator 和一个 rubric 型 evaluator
6. 针对 prompt 或模型变体跑实验
7. 把表现最好的配置推进到 staging

### 哪些团队适合 LangSmith

- 已经在用 LangChain 或 LangGraph
- Agent 调试非常依赖细粒度 trace
- 希望把 prompt playground、dataset 和 experiment 放在一个平台里
- 团队能接受云端工作流

### 哪些场景不一定合适

- 你需要完全本地化优先
- 你更想要最轻量的 YAML + CI 回归测试
- 你不太需要 trace 级调试

### 参考资料

- Evaluation quickstart: https://docs.langchain.com/langsmith/evaluation-quickstart
- Evaluation concepts: https://docs.langchain.com/langsmith/evaluation-concepts
- Observability quickstart: https://docs.langchain.com/langsmith/observability-quickstart
- How to evaluate an agent: https://docs.langchain.com/langsmith/evaluate-agent
