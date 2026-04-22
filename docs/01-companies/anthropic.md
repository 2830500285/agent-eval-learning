# Anthropic / Anthropic

## English

Anthropic is especially strong on behavioral, safety, and "unknown unknown" style evaluation.

### Key resources

1. Discovering Language Model Behaviors with Model-Written Evaluations
   - Link: https://www.anthropic.com/research/discovering-language-model-behaviors-with-model-written-evaluations
   - Why it matters: A foundational reference for using models themselves to generate eval datasets and surface new behaviors.

2. A "diff" tool for AI: Finding behavioral differences in new models
   - Link: https://www.anthropic.com/research/diff-tool
   - Why it matters: Moves beyond fixed benchmarks toward change detection between model versions.

3. Forecasting rare language model behaviors
   - Link: https://www.anthropic.com/research/forecasting-rare-behaviors
   - Why it matters: Highlights a core eval problem: rare but dangerous failures may not show up in normal sample sizes.

4. Sabotage evaluations for frontier models
   - Link: https://www.anthropic.com/research/sabotage-evaluations
   - Why it matters: Illustrates eval design for adversarial and deceptive behavior rather than only helpfulness or accuracy.

5. A new initiative for developing third-party model evaluations
   - Link: https://www.anthropic.com/news/a-new-initiative-for-developing-third-party-model-evaluations
   - Why it matters: Offers practical guidance on designing external evals for serious capability and safety questions.

### Anthropic pattern

Anthropic often treats evaluation as a discovery process, not just a scoreboard. That mindset is useful when your biggest risks are emergent behaviors and not simple accuracy regressions.

### How to use Anthropic material in your own stack

1. Use Anthropic's work when you care about rare failures, sabotage, deception, or hidden behavior changes.
2. Treat evaluation as a search process for unknown failure modes, not only a pass/fail report.
3. Add adversarial datasets and long-tail cases into your program early.
4. Keep a separate safety eval suite from your normal product-quality suite.

## 中文

Anthropic 在行为型、安全型、以及“未知未知”类评测上尤其值得研究。

### 关键资料

1. Model-Written Evaluations
   - 链接：https://www.anthropic.com/research/discovering-language-model-behaviors-with-model-written-evaluations
   - 价值：用模型自己生成评测数据集，去发现新行为，是这个方向的代表性工作。

2. Diff tool for AI
   - 链接：https://www.anthropic.com/research/diff-tool
   - 价值：不再只看静态 benchmark，而是比较模型版本之间的行为差异。

3. Forecasting rare behaviors
   - 链接：https://www.anthropic.com/research/forecasting-rare-behaviors
   - 价值：强调一个现实问题，危险但低频的失败，常常在普通采样下根本测不出来。

4. Sabotage evaluations
   - 链接：https://www.anthropic.com/research/sabotage-evaluations
   - 价值：展示如何设计针对破坏、欺骗和规避监督的评测，而不是只看准确率。

5. Third-party model evaluations initiative
   - 链接：https://www.anthropic.com/news/a-new-initiative-for-developing-third-party-model-evaluations
   - 价值：给出设计外部 eval 的建议，尤其适合高风险能力和安全问题。

### Anthropic 的风格

Anthropic 经常把评测视为“发现问题的过程”，而不是“打分板”。如果你的系统面临的是涌现行为、策略规避、低频高风险错误，这种思路很重要。

### 如何把 Anthropic 的思路用到自己的系统里

1. 如果你关心低频失败、破坏行为、欺骗行为、隐藏行为变化，就要重点看 Anthropic 的做法。
2. 把评测当成“搜索未知失败模式”的过程，而不只是 pass/fail 报告。
3. 尽早把对抗样本和长尾案例纳入你的数据集。
4. 安全 eval 最好和普通产品质量 eval 分开维护。
