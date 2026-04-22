# LangSmith Setup Guide / LangSmith 搭建指南

## English

This guide is for teams who want a trace-centric eval stack.

### What you need

- a LangSmith account
- `LANGSMITH_API_KEY`
- your model provider key such as `OPENAI_API_KEY`
- application code where you can wrap model calls

### Fastest setup route

1. Install SDK dependencies
2. Enable tracing
3. Send a real request through the application
4. Inspect traces in the UI
5. Create a dataset from representative cases
6. Add evaluators
7. Run experiments

### Environment variables

```bash
export LANGSMITH_TRACING=true
export LANGSMITH_API_KEY="<your-langsmith-api-key>"
export OPENAI_API_KEY="<your-openai-api-key>"
```

### Minimal workflow

1. Wrap the provider SDK so calls are traced
2. Define a target function that represents the behavior under test
3. Create a dataset with inputs and reference outputs
4. Add evaluators such as correctness, groundedness, or custom rubric checks
5. Run an experiment and compare versions

### What LangSmith is best for

- debugging agents with many tool calls
- comparing prompt or model variants
- creating evals directly from observed traces
- combining offline experiments and online monitoring

### Common pitfalls

- evaluating too early on tiny toy examples
- no metadata on dataset rows
- trusting judge prompts without human calibration
- looking only at summary scores and not failed traces

### Sources

- https://docs.langchain.com/langsmith/evaluation-quickstart
- https://docs.langchain.com/langsmith/evaluation-concepts
- https://docs.langchain.com/langsmith/evaluate-agent

## 中文

这份指南适合想做“以 trace 为中心”的评测栈的团队。

### 你需要准备什么

- LangSmith 账号
- `LANGSMITH_API_KEY`
- 模型提供商的 key，比如 `OPENAI_API_KEY`
- 一段你可以接入 tracing 的应用代码

### 最快的接入路径

1. 安装 SDK
2. 打开 tracing
3. 用真实请求跑一遍应用
4. 在 UI 里看 trace
5. 从代表性案例里整理 dataset
6. 添加 evaluator
7. 跑 experiment

### 环境变量

```bash
export LANGSMITH_TRACING=true
export LANGSMITH_API_KEY="<your-langsmith-api-key>"
export OPENAI_API_KEY="<your-openai-api-key>"
```

### 最小闭环

1. 包装 provider SDK，让调用可追踪
2. 定义 target function，表示你真正要评的行为
3. 创建带输入和参考输出的数据集
4. 加入 correctness、groundedness 或自定义 rubric evaluator
5. 运行实验并比较版本

### 最适合的场景

- 多工具调用的 Agent 调试
- Prompt 或模型版本对比
- 直接从生产 trace 反哺 eval
- 离线实验和线上监控联动

### 常见坑

- 太早就拿玩具样本做结论
- dataset 行里没有元数据
- judge 没有人类校准就直接上
- 只看总分，不看失败 trace

### 资料来源

- https://docs.langchain.com/langsmith/evaluation-quickstart
- https://docs.langchain.com/langsmith/evaluation-concepts
- https://docs.langchain.com/langsmith/evaluate-agent
