# RAG Eval Playbook / RAG 评测实操手册

## English

RAG systems fail in at least two different places:

- retrieval
- answer generation

Do not collapse them into one score.

### What to evaluate for retrieval

- whether the right chunk was retrieved
- rank position of the relevant chunk
- whether retrieved evidence is sufficient
- whether stale or conflicting documents are selected

### What to evaluate for answer generation

- groundedness to retrieved evidence
- citation quality
- completeness
- hallucination rate
- policy compliance

### Suggested row schema

- question
- retrieved contexts
- expected facts
- allowed sources
- reference answer or rubric
- metadata such as topic, language, freshness, and risk

### Practical workflow

1. freeze a dataset of real user questions
2. store retrieved chunks alongside outputs
3. add a groundedness evaluator
4. add a citation-presence check
5. inspect failure cases by retrieval failure vs generation failure

## 中文

RAG 系统至少会在两个位置失败：

- 检索阶段
- 生成阶段

这两类问题绝对不能压成一个总分。

### 检索层该评什么

- 正确 chunk 是否被取回
- 相关 chunk 的排序位置
- 取回证据是否足够
- 是否取到了过时或冲突文档

### 生成层该评什么

- 回答是否真正基于取回证据
- 引用质量
- 是否完整
- 幻觉率
- 策略合规性

### 建议的数据行结构

- 问题
- 检索到的上下文
- 预期应覆盖的事实
- 允许引用的来源
- 参考答案或 rubric
- 元数据：主题、语言、时效性、风险等级

### 实操流程

1. 固定一批真实用户问题作为 dataset
2. 把 retrieved chunks 和最终回答一起存下来
3. 增加 groundedness evaluator
4. 增加 citation presence 检查
5. 复盘失败时，区分是 retrieval failure 还是 generation failure
