# Langfuse Setup Guide / Langfuse 搭建指南

## English

Langfuse is a strong option when you want observability and evaluation in the same system.

### Why teams choose Langfuse

- trace collection plus evaluation
- datasets and experiments
- live scores and annotations
- cloud or self-hosting options

### Practical setup path

1. Choose cloud or self-hosted deployment
2. Instrument the application to send traces
3. Define datasets from production traffic or curated samples
4. Run experiments on a stable baseline
5. Add live evaluators for production monitoring
6. Add human annotations for disputed or valuable sessions

### What Langfuse is best for

- teams that need product observability and evals together
- teams that want to connect user sessions, traces, scores, and review
- organizations that may need self-hosting

### Risks to watch

- trying to score everything with one generic metric
- not tagging traces with business metadata
- using online evaluators without sampling human review

### Sources

- https://langfuse.com/docs/evaluation/overview
- https://langfuse.com/docs/evaluation/core-concepts
- https://langfuse.com/docs/evaluation/experiments/datasets
- https://langfuse.com/docs/self-hosting

## 中文

如果你希望把“可观测性”和“评测”放进同一套系统里，Langfuse 是很强的选项。

### 团队为什么会选 Langfuse

- trace 采集和 evaluation 一体化
- 支持 dataset 和 experiment
- 支持线上 score 与人工标注
- 既能云托管，也能自托管

### 实操接入路径

1. 先决定用云版还是自托管
2. 给应用接 trace
3. 从生产流量或人工样本里整理 dataset
4. 先对稳定 baseline 跑 experiment
5. 给线上系统加 live evaluator
6. 对争议大或价值高的 session 加人工标注

### 最适合的场景

- 想把产品可观测性和评测放一起
- 想把用户 session、trace、score 和 review 串起来
- 有自托管诉求的组织

### 需要注意的风险

- 试图用一个泛化指标给所有内容打分
- trace 没有业务元数据标签
- 线上 evaluator 上线了，却没有抽样人工复核

### 资料来源

- https://langfuse.com/docs/evaluation/overview
- https://langfuse.com/docs/evaluation/core-concepts
- https://langfuse.com/docs/evaluation/experiments/datasets
- https://langfuse.com/docs/self-hosting
