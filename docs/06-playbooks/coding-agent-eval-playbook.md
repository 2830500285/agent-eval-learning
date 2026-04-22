# Coding Agent Eval Playbook / Coding Agent 评测实操手册

## English

Coding agents should not be evaluated like chatbots.

### The unit of evaluation is usually the whole task

A coding agent run includes:

- problem understanding
- planning
- code edits
- test execution
- recovery from errors

If you score only the final message, you will miss the real reasons the run failed.

### What to capture

- task prompt
- repository state
- file diffs
- terminal output
- tests that passed or failed
- tool calls
- time to completion
- whether human intervention was required

### High-value metrics

- task completion rate
- test pass rate
- destructive action rate
- unnecessary edit rate
- recovery rate after failing tests
- cost and latency

### Recommended harness design

1. freeze a benchmark task set
2. run each task in isolated workspaces
3. record full traces and diffs
4. run the same test suite on every run
5. use human review on a sample of "passed" runs

### Typical traps

- letting the agent see hidden test answers
- mixing environment problems with agent quality
- judging only by whether a patch exists
- ignoring partial success and recovery behavior

## 中文

Coding Agent 不能按聊天机器人那套方式来评。

### 评测单位通常应该是“完整任务”

一次 coding agent 运行包含：

- 理解问题
- 规划方案
- 修改代码
- 跑测试
- 出错后的恢复

如果你只给最终回复打分，你会错过真正导致失败的原因。

### 应该记录什么

- 任务提示
- 仓库初始状态
- 文件 diff
- 终端输出
- 测试通过或失败情况
- 工具调用
- 完成耗时
- 是否需要人工介入

### 高价值指标

- 任务完成率
- 测试通过率
- 危险操作率
- 无效编辑率
- 测试失败后的恢复率
- 成本与延迟

### 推荐的 harness 设计

1. 固定一套 benchmark 任务集
2. 每个任务在隔离工作区里运行
3. 记录完整 trace 和 diff
4. 每次运行都跑同一套测试
5. 对一部分“看起来通过”的结果做人工复核

### 常见陷阱

- 让 agent 提前看到隐藏测试答案
- 把环境问题和 agent 质量混在一起
- 只看是否产生 patch
- 忽略部分成功和失败恢复能力
