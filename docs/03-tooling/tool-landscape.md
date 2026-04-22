# Tooling Landscape / 工具版图

## English

The tooling question is not "which tool is best?" It is "which workflow shape fits our team?"

### Fastest path to regression testing

- Promptfoo
- Best for: prompt, model, RAG, and lightweight agent regression checks
- Why choose it: config-first, easy CI, low setup cost

### Best path for trace-centric experiments

- LangSmith
- Best for: agent debugging, prompt experiments, dataset-based evaluation, trace review
- Why choose it: strong trace model plus experiments and datasets

### Best path for observability plus evaluation

- Langfuse
- Best for: teams that want traces, scores, datasets, and review in one product
- Why choose it: observability and evaluation live together

### Best path for open-source leaning observability

- Phoenix
- Best for: teams that want more open and self-managed workflows
- Why choose it: good observability foundation with evaluation workflows

### Best path for experiment-heavy research teams

- Weave
- Best for: artifact-oriented experimentation and reproducibility
- Why choose it: strong fit when the team already works in a W&B-style experimental culture

### Best path for benchmark reference implementations

- OpenAI simple-evals
- Best for: understanding benchmark packaging and reference benchmark execution
- Why choose it: simple, transparent benchmark code

## Tool selection heuristics

- Choose Promptfoo if you need a quick CI gate this week
- Choose LangSmith if you need trace-level debugging and experiments
- Choose Langfuse if you need production observability and evaluation together
- Choose Phoenix if you want a more open observability-first stack
- Choose Weave if your team already thinks in terms of experiment artifacts
- Use benchmark runners when the goal is comparability, not product shipping

## 中文

工具选型真正该问的，不是“哪个工具最好”，而是“哪种工作流形态最适合我们团队”。

### 最快做出回归测试的路径

- Promptfoo
- 适合：Prompt、模型、RAG、轻量 Agent 的回归检查
- 选择原因：配置驱动、CI 友好、接入成本低

### 最适合 trace 驱动实验的路径

- LangSmith
- 适合：Agent 调试、Prompt 实验、数据集评测、trace 复盘
- 选择原因：trace、experiment、dataset 串得很完整

### 最适合 observability + eval 一体化的路径

- Langfuse
- 适合：想把 trace、score、dataset、人工复核放进一个系统
- 选择原因：可观测性与评测天然打通

### 最适合偏开源观测栈的路径

- Phoenix
- 适合：想要更开放、更自管理的工作流
- 选择原因：观测基础不错，评测能力也能逐步叠加

### 最适合实验型研究团队的路径

- Weave
- 适合：强调实验产物、可复现、run 对比的团队
- 选择原因：非常契合 W&B 风格的研发文化

### 最适合理解 benchmark 参考实现的路径

- OpenAI simple-evals
- 适合：理解 benchmark 代码如何组织、如何跑参考实验
- 选择原因：实现简单、透明

## 选型启发

- 这周就要做出 CI 门槛，用 Promptfoo
- 需要 trace 级调试和实验对比，用 LangSmith
- 需要生产观测和评测打通，用 Langfuse
- 想走更开放的 observability-first 路线，用 Phoenix
- 团队本来就用实验产物思维做研发，用 Weave
- 如果目标是“可比性”，而不是“上线”，benchmark runner 更合适
