# Operating an Eval Program / 持续运营一套 Eval 体系

## English

An eval program breaks when nobody owns the boring parts.

### Weekly operating rhythm

1. Review top new failures from production traces
2. Add or refresh dataset rows
3. Re-run baseline and candidate experiments
4. Triage disagreement cases
5. Update release gates if product risk changed

### Roles that usually matter

- product owner: defines which failures matter
- engineer: maintains instrumentation and execution
- domain reviewer: judges ambiguous quality questions
- team lead: decides release gates

### Minimum artifacts

- versioned dataset
- evaluator definitions
- experiment logs
- release decision record
- failure taxonomy

### Signs the program is healthy

- new failures are added back into the dataset
- release decisions cite eval results
- humans regularly inspect samples
- metrics are tracked by category, not only overall

## 中文

一套 eval 体系真正失效，往往不是技术不够，而是没有人持续负责那些“无聊但关键”的部分。

### 每周运营节奏

1. 复盘生产 trace 中最新的高价值失败
2. 往 dataset 里补新样本或更新旧样本
3. 重新跑 baseline 和候选方案实验
4. 处理 judge 分歧样本
5. 如果产品风险变化，调整发布门槛

### 常见角色分工

- 产品负责人：定义哪些失败最重要
- 工程师：维护埋点、数据和执行流程
- 领域评审：判断模糊质量问题
- 团队负责人：决定发布门槛

### 最低限度要保留的资产

- 版本化 dataset
- evaluator 定义
- 实验记录
- 发布决策记录
- 失败分类体系

### 一个健康的 eval 项目会有什么表现

- 新失败会不断回写到数据集
- 发布决策会引用 eval 结果
- 人工会定期抽样复核
- 指标会按类别拆开，而不是只看总分
