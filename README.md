# Banking Support SLM Research

## Purpose

This project compares two methods that write replies to banking support requests.
The first method uses fixed reply templates.
The second method uses a small language model (SLM).
Both methods receive the same action, account context, and fictional bank policy.

The main question is simple:
Does the SLM improve reply quality enough to justify its memory use, response time, and errors?

## Current status

The project owner reviewed the research design on 11 October 2026.
The project owner approved direct implementation on 11 October 2026.
DATA-1 is complete: record validation and its 12 tests passed.
DATA-2 is complete: public data preparation passed 11 tests.
The classifier and model experiments are next.
All 20 initial scenario records still require individual review.

## System design

1. Receive a customer message and simulated account context.
2. Use a classifier to identify the request type.
3. Use policy rules to select the next action.
4. Use a template or an SLM to write a draft reply.
5. Check the reply before an operator reviews it.

The classifier is a conventional machine learning model. It is not an SLM.
The SLM experiment will use an existing pretrained model on a CPU.
The study does not require a new model or model fine-tuning.

## Project documents

| File | Purpose |
|---|---|
| [START_HERE.md](START_HERE.md) | Explains the terms and the current step. |
| [PLAN.md](PLAN.md) | Lists the work in order. Explains what each task must produce. |
| [SPEC.md](SPEC.md) | States what the system must do and how to check it. |
| [RESEARCH_PROTOCOL.md](RESEARCH_PROTOCOL.md) | States how to conduct the comparison and report results. |
| [DEMO_POLICY.md](DEMO_POLICY.md) | Contains the fictional rules used in the scenarios. |
| [Scenario records](examples/starter_cases.jsonl) | Contains 20 initial proposals. These are not final test data. |
| [Research notes](research-notes/README.md) | Working explanations, calculations, and evidence links. Notes start as empty templates. |

## Expected outputs

- A classifier for eight banking request types.
- Scenario records with source and review information.
- A comparison of template replies and SLM replies.
- Measurements of errors, reply quality, response time, and memory use.
- A research report with failure analysis and reproduction instructions.
- A recorded local demonstration.

These outputs are planned. They are not completed research contributions.
A result that shows no SLM benefit is still a valid research result.

## Study limits

The project uses English public data and synthetic scenarios.
It runs on a local CPU without paid model services.
Account states and bank policies are fictional.
The application cannot access accounts, move money, or contact customers.
Results do not establish suitability for a real bank.
The study does not claim a new model architecture or a full BANKING77 benchmark.

## Data and tools

- [BANKING77](https://github.com/PolyAI-LDN/task-specific-datasets) provides questions and request labels. It does not provide policies or approved replies.
- [SmolLM2-360M-Instruct](https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct) is the initial model candidate. Its local performance is not known.

Before downloads, verify source versions and licenses. Preserve BANKING77 attribution under CC BY 4.0.
See the [research protocol](RESEARCH_PROTOCOL.md#references) for background sources.
