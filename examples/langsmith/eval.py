from langsmith import Client, wrappers
from openai import OpenAI
from openevals.llm import create_llm_as_judge
from openevals.prompts import CORRECTNESS_PROMPT

openai_client = wrappers.wrap_openai(OpenAI())


def build_dataset() -> None:
    client = Client()
    dataset = client.create_dataset(
        dataset_name="Agent Eval Learning Sample",
        description="A starter dataset for learning LangSmith evaluations.",
    )
    examples = [
        {
            "inputs": {"question": "Which country is Mount Kilimanjaro located in?"},
            "outputs": {"answer": "Mount Kilimanjaro is located in Tanzania."},
        },
        {
            "inputs": {"question": "What is Earth's lowest point?"},
            "outputs": {"answer": "Earth's lowest point is the Dead Sea."},
        },
    ]
    client.create_examples(dataset_id=dataset.id, examples=examples)


def target(inputs: dict) -> dict:
    response = openai_client.chat.completions.create(
        model="gpt-5-mini",
        messages=[
            {"role": "system", "content": "Answer the following question accurately."},
            {"role": "user", "content": inputs["question"]},
        ],
    )
    return {"answer": response.choices[0].message.content.strip()}


def correctness_evaluator(inputs: dict, outputs: dict, reference_outputs: dict):
    evaluator = create_llm_as_judge(
        prompt=CORRECTNESS_PROMPT,
        model="openai:o3-mini",
        feedback_key="correctness",
    )
    return evaluator(
        inputs=inputs,
        outputs=outputs,
        reference_outputs=reference_outputs,
    )


def main() -> None:
    client = Client()
    client.evaluate(
        target,
        data="Agent Eval Learning Sample",
        evaluators=[correctness_evaluator],
        experiment_prefix="agent-eval-learning",
        max_concurrency=2,
    )


if __name__ == "__main__":
    # Run build_dataset() once before main() if the dataset does not exist yet.
    main()
