# Agent Eval Learning

A bilingual handbook for building, running, and operating agent and LLM evaluations.

`Agent Eval Learning` is not just a reading list. It is a practical handbook for builders who want to design eval datasets, choose tools, run experiments, and turn evals into a release gate.

`Agent Eval Learning` 不只是资料清单，而是一份可落地的双语手册，目标是帮助团队真正搭建评测体系：设计数据集、选择工具、运行实验、把评测变成上线门槛。

## What is inside / 仓库内容

- `docs/00-overview`: mental models and detailed system-building guidance
- `docs/01-companies`: OpenAI, Anthropic, Google, LangChain, Microsoft, and what to borrow from them
- `docs/02-practitioners`: practical methods from respected builders and researchers
- `docs/03-tooling`: detailed tool selection and setup guidance
- `docs/04-templates`: reusable templates for eval specs and operating rhythm
- `docs/05-reading-list`: curated reading list
- `docs/06-playbooks`: step-by-step playbooks for common eval problems
- `docs/07-examples`: recommended repository and example structure
- `examples`: example code and config you can adapt

## Suggested reading path / 建议阅读路径

1. Start with [docs/00-overview/eval-principles.md](docs/00-overview/eval-principles.md)
2. Then read [docs/00-overview/knowledge-map.md](docs/00-overview/knowledge-map.md)
3. Read [docs/00-overview/building-an-eval-program.md](docs/00-overview/building-an-eval-program.md)
4. Compare approaches in `docs/01-companies` and `docs/03-tooling`
5. Use [docs/06-playbooks/from-zero-to-first-eval.md](docs/06-playbooks/from-zero-to-first-eval.md)
6. Reuse [docs/04-templates/eval-spec-template.md](docs/04-templates/eval-spec-template.md)

## Naming note / 命名说明

GitHub repository names cannot contain spaces, so the repository slug is `agent-eval-learning` while the project title is `Agent Eval Learning`.

## If You Want To Build Fast / 如果你想快速落地

Start here:

1. [docs/06-playbooks/from-zero-to-first-eval.md](docs/06-playbooks/from-zero-to-first-eval.md)
2. [docs/03-tooling/promptfoo.md](docs/03-tooling/promptfoo.md)
3. [examples/promptfoo/promptfooconfig.yaml](examples/promptfoo/promptfooconfig.yaml)

If you need a more trace-centric stack:

1. [docs/03-tooling/langsmith.md](docs/03-tooling/langsmith.md)
2. [docs/03-tooling/langfuse.md](docs/03-tooling/langfuse.md)
3. [docs/06-playbooks/operating-an-eval-program.md](docs/06-playbooks/operating-an-eval-program.md)

## Editorial principles / 编辑原则

- Prefer primary sources when possible
- Summarize instead of copying source material
- Keep each major page actionable for builders
- Write in English and Chinese for every high-value page
- Separate benchmarks, applied evals, tooling, and operating processes
- Prefer workflows and decision criteria over vague opinions

## Current scope / 当前范围

This version prioritizes:

- OpenAI
- Anthropic
- Google Research / DeepMind / Vertex AI
- LangChain / LangSmith
- Microsoft Azure / Promptflow / GenAI Evals
- Practitioners such as Hamel Husain, Shreya Shankar, Eugene Yan, and Chip Huyen
- Tooling such as Promptfoo, LangSmith, Langfuse, Phoenix, and Weave

## Expansion ideas / 后续扩展

- Add papers by domain: coding, safety, factuality, browsing, healthcare
- Add benchmark cards with fields for task, judge type, cost, latency, and failure modes
- Add CI examples for GitHub Actions
- Add Chinese annotations for more papers and talks
- Add more example eval configs for coding agents, RAG, customer support, and browsing agents
