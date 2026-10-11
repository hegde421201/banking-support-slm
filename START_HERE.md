# Project guide

## Current step

The research design has been reviewed.
The project owner approved direct implementation on 11 October 2026.
DATA-1 is complete. Its record validator passed 12 tests.
DATA-2 is complete. Its 11 data preparation tests passed.
BASE-1 is next. No classifier or SLM has been trained.

Read [PLAN.md](PLAN.md) to understand the proposed work.
The first task checks scenario records before the project uses them.
Approval of a plan does not approve individual scenario labels.

## What the files mean

A Markdown file is a text document. Its filename ends with `.md`.
A specification states the required system behaviour.
A research protocol states the experiment method.
An implementation plan states the work needed to build the system.

Use [PLAN.md](PLAN.md) as the current task list.
Old workflow records are stored under `.workflow-history` for reference only.
They do not control current work or require your approval.

## Terms

| Term | Meaning in this project |
|---|---|
| SLM | Small language model. It generates text. |
| CPU | The computer processor used for this study. No GPU is required. |
| Intent | The type of customer request, such as a missing card. |
| Classifier | A model that selects a request type from the supported labels. |
| Baseline | The reference method used for comparison. |
| Template | A fixed reply format that uses known scenario information. |
| Context | Account information supplied with a scenario. It is simulated. |
| Scenario | A message, context, expected action, and related policy. |
| Provenance | A record of the source, author method, and review history. |
| Validation data | Data used to select model settings before the final test. |
| Final test data | Reserved data used after the system settings are fixed. |
| Fallback | The response used when the normal output is not acceptable. |
| Coverage | The share of cases for which the system supplies an answer. |
| Gate | A required check that a task must pass. |
| Scope | The files and work included in one task. |
| Queued | Planned, but not started. |
| Independent review | A check by a person who did not do the work under review. |

## First task

DATA-1 checks the format and source information of scenario records.
It also checks separate records of human review decisions.
It must accept the 20 initial proposals without changing them.
It must reject invalid records and unsupported training eligibility.
It cannot prove that a reviewer identity is genuine.
It cannot prove that a proposed label is correct.

A JSONL file contains one JSON record on each line.
The initial records are in [examples/starter_cases.jsonl](examples/starter_cases.jsonl).
Each record remains unreviewed and ineligible for training until an actual review occurs.

## Local tools

Project folder: `D:/Antern/banking-support-slm`.
Python command: `C:/Python312/python.exe`.
The detected Python version is 3.12.0.

To run the project checks, use these commands in PowerShell:

```powershell
Set-Location D:/Antern/banking-support-slm
C:/Python312/python.exe -m unittest discover -s tests -v
```

## Document language

These documents use ASD-STE100 as a writing guide.
They use short sentences, consistent terms, and direct instructions.
Technical names and identifiers retain their exact spelling.
A complete dictionary and rule audit has not been performed.
Do not describe these documents as verified ASD-STE100-compliant documents.

Reference: [ASD-STE100 official guidance](https://www.asd-ste100.org/STE_faq.html).
