# OpenAI / OpenAI

## English

OpenAI's eval story is notable because it spans both classic model benchmarks and practical product guidance.

### Key resources

1. Evaluation best practices
   - Link: https://developers.openai.com/api/docs/guides/evaluation-best-practices
   - Why it matters: A practical guide for designing evals in product settings, including dataset construction, iteration, and judge design.

2. Introducing SimpleQA
   - Link: https://openai.com/index/introducing-simpleqa/
   - Why it matters: A focused factuality benchmark for short, verifiable questions. Useful for understanding calibration and hallucination measurement.

3. BrowseComp: a benchmark for browsing agents
   - Link: https://openai.com/index/browsecomp/
   - Why it matters: Shows how OpenAI evaluates browsing-heavy agents on questions requiring real web navigation and evidence gathering.

4. Simple Evals repository
   - Link: https://github.com/openai/simple-evals
   - Why it matters: A lightweight open-source reference implementation that shows how OpenAI packages benchmark runs for public transparency.

5. TruthfulQA
   - Link: https://openai.com/index/truthfulqa/
   - Why it matters: An early but still influential benchmark on truthfulness and model tendency to repeat common misconceptions.

### OpenAI pattern

OpenAI tends to publish both:

- benchmark-oriented artifacts for comparability
- product-oriented guidance for iteration and deployment

That combination is useful: benchmarks help communicate progress, while applied eval guides help teams ship.

### How to use OpenAI material in your own stack

1. Use OpenAI's benchmark work to understand what capability is being measured.
2. Use OpenAI's evaluation best-practice guidance to design task-specific product evals.
3. For application work, borrow the evaluation flywheel:
   - build a small dataset
   - create graders
   - compare variants
   - inspect failures
   - update the dataset
4. Separate research benchmarks from release decisions.

## 中文

OpenAI 的 eval 体系有一个很明显的特点：同时覆盖传统 benchmark 和偏产品实践的评测方法。

### 关键资料

1. Evaluation best practices
   - 链接：https://developers.openai.com/api/docs/guides/evaluation-best-practices
   - 价值：面向产品团队的实操指南，涉及数据集构建、迭代方式以及 judge 设计。

2. Introducing SimpleQA
   - 链接：https://openai.com/index/introducing-simpleqa/
   - 价值：面向短事实问答的 benchmark，适合理解事实性、校准和幻觉测量。

3. BrowseComp
   - 链接：https://openai.com/index/browsecomp/
   - 价值：展示了浏览型 Agent 如何评测，尤其是依赖真实网页导航和证据收集的任务。

4. simple-evals 仓库
   - 链接：https://github.com/openai/simple-evals
   - 价值：一个轻量级开源参考实现，可以看到 OpenAI 如何把公开 benchmark 包装成可运行代码。

5. TruthfulQA
   - 链接：https://openai.com/index/truthfulqa/
   - 价值：较早但影响深远的真实性 benchmark，用来衡量模型是否会复述常见误解。

### OpenAI 的风格

OpenAI 经常同时发布：

- 面向可比性的 benchmark 产物
- 面向迭代落地的产品评测指南

这两类内容结合起来很有价值：前者帮助你理解能力边界，后者帮助你真正上线系统。

### 如何把 OpenAI 的思路用到自己的系统里

1. 先用 OpenAI 的 benchmark 材料理解“它到底测了什么能力”。
2. 再用 OpenAI 的评测实践指南设计你自己的任务型 eval。
3. 在应用层面，最值得借鉴的是 evaluation flywheel：
   - 先做小数据集
   - 再设计 grader
   - 比较不同方案
   - 复盘失败
   - 把新失败写回数据集
4. 研究 benchmark 和产品发布门槛要明确分开。
