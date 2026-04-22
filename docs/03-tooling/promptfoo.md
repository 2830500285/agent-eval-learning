# Promptfoo Setup Guide / Promptfoo 搭建指南

## English

Promptfoo is one of the fastest ways to get from zero to a repeatable regression suite.

### Why teams choose Promptfoo

- config-first workflow
- easy CI integration
- model, prompt, and RAG comparison
- good for quick regression testing
- useful red-teaming support

### Fast start

1. Install with `npm` or use `npx`
2. Create `promptfooconfig.yaml`
3. Define providers
4. Define test cases and assertions
5. Run `promptfoo eval`
6. Inspect failed cases
7. Add the command to CI

### Minimal install

```bash
npm install -g promptfoo
promptfoo init
promptfoo eval
```

### What belongs in the config

- prompt or target prompt files
- providers to compare
- test cases
- assertions
- optional red-team scenarios

### Good use cases

- prompt regression tests
- comparing two or three models quickly
- gating a pull request
- testing RAG answers against rubric assertions

### Weak fit

- teams that need rich trace trees and deep runtime debugging
- teams that want one hosted platform for observability plus evals

### Sources

- https://www.promptfoo.dev/docs/intro/
- https://www.promptfoo.dev/docs/configuration/guide/
- https://www.promptfoo.dev/docs/integrations/ci-cd/

## 中文

如果你想最快从零做出一套“能重复跑的回归测试”，Promptfoo 是非常强的起点。

### 团队为什么选 Promptfoo

- 配置驱动
- 非常容易接入 CI
- 适合比较模型、Prompt、RAG 策略
- 很适合快速做回归测试
- 红队化支持也比较实用

### 最快上手方式

1. 用 `npm` 安装，或者直接 `npx`
2. 新建 `promptfooconfig.yaml`
3. 定义 providers
4. 定义测试样本和 assertions
5. 运行 `promptfoo eval`
6. 查看失败样本
7. 把命令接进 CI

### 最小安装

```bash
npm install -g promptfoo
promptfoo init
promptfoo eval
```

### 配置里应该放什么

- Prompt 或 prompt 文件
- 要比较的 providers
- 测试样本
- 断言规则
- 可选的红队场景

### 适合的场景

- Prompt 回归测试
- 快速比较两三个模型
- 给 PR 设置门槛
- 用 rubric 断言测试 RAG 答案

### 不太适合的场景

- 需要非常丰富 trace 树和深度运行时调试的团队
- 想把可观测性和 eval 放在一个托管平台里的团队

### 资料来源

- https://www.promptfoo.dev/docs/intro/
- https://www.promptfoo.dev/docs/configuration/guide/
- https://www.promptfoo.dev/docs/integrations/ci-cd/
