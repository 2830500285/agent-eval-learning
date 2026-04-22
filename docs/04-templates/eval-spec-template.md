# Eval Spec Template / Eval 方案模板

Use this template when designing a new evaluation.

设计新评测时，可直接复用这个模板。

## 1. Objective / 目标

- What product or model behavior are we evaluating?
- 我们要评估的是哪种产品行为或模型能力？

## 2. Unit of evaluation / 评测单位

- single answer
- full trace
- multi-turn session
- tool-use episode

## 3. Failure modes / 失败模式

- What specific failures matter?
- 哪些具体失败最值得关注？

## 4. Dataset / 数据集

- source of examples
- labeling process
- sampling strategy
- versioning rule

## 5. Judge / 评分方式

- code or exact match
- heuristic rules
- human review
- LLM-as-a-judge

## 6. Validation / 验证

- How will judge quality be checked against human labels?
- judge 的质量如何与人工标注对齐验证？

## 7. Metrics / 指标

- pass rate
- error rate by category
- cost per run
- latency
- escalation rate

## 8. Release gate / 发布门槛

- What threshold blocks deployment?
- 什么阈值会阻止上线？

## 9. Review cadence / 复盘频率

- weekly
- per model change
- per prompt change
- before major launch
