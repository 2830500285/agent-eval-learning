# Eugene Yan / Eugene Yan

## English

Eugene Yan writes particularly well about task-specific evaluation and production realism.

### Recommended resource

1. Task-Specific LLM Evals that Do and Don't Work
   - Link: https://eugeneyan.com/writing/evals/
   - Why it matters: A strong practical discussion of why generic metrics often fail and how task-specific evaluation should be designed.

### Core lessons

- Generic automatic metrics are often weak proxies
- You need evaluation tied to the exact failure modes that matter in your product
- Ranking prompts or models without a clear target metric can create false confidence

### How to apply Eugene's advice

1. Write down which failure would actually hurt your users or business.
2. Turn those failures into dataset slices.
3. Reject metrics that look elegant but do not change decisions.
4. Compare variants per slice instead of only looking at a global average.

## 中文

Eugene Yan 的价值在于，他非常擅长把“生产场景中的真实问题”翻译成“可操作的 eval 设计”。

### 推荐内容

1. Task-Specific LLM Evals that Do and Don't Work
   - 链接：https://eugeneyan.com/writing/evals/
   - 价值：很好地解释了为什么很多通用自动指标并不可靠，以及为什么必须围绕具体任务失败模式来设计评测。

### 核心观点

- 通用自动指标往往只是弱代理变量
- 评测必须绑定你的业务失败模式
- 如果目标指标不清晰，模型或 prompt 排名会制造虚假的确定感

### 如何把 Eugene 的建议落地

1. 先写清楚哪些失败真的会伤害用户或业务。
2. 把这些失败转成数据集切片。
3. 拒绝那些看起来优雅、但不会改变决策的指标。
4. 比较方案时优先按切片看，而不是只看全局平均分。
