# Recommended Repo Layout / 推荐的仓库结构

## English

If you want evals to survive beyond one experiment, keep the repository structure explicit:

```text
evals/
  datasets/
  prompts/
  rubrics/
  configs/
  reports/
examples/
  promptfoo/
  langsmith/
src/
tests/
```

Why this matters:

- datasets need versioning
- prompts and rubrics should change independently
- reports should be archived by run or release

## 中文

如果你希望 eval 不只是一次性实验，仓库结构就应该从一开始分清楚：

```text
evals/
  datasets/
  prompts/
  rubrics/
  configs/
  reports/
examples/
  promptfoo/
  langsmith/
src/
tests/
```

这样做的价值在于：

- dataset 需要版本管理
- prompt 和 rubric 应该独立演进
- 报告最好按运行或发布版本归档
