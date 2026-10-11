# System specification

Status: the project owner reviewed the research design on 11 October 2026.
This revision simplifies the language. It retains the requirement IDs and intended behaviour.
The assistant manages work under the agreed plan.

## Problem

Build a reproducible system for simulated banking support.
The system identifies a request type, selects a permitted action, and writes a reply draft.
Compare SLM replies with template replies under the same policy conditions.
Use public data, synthetic scenarios, and CPU execution without paid model services.

## Users

The project author runs the study. Reviewers inspect the method and evidence.
A simulated operator reviews proposed replies. No real customer receives a reply from this application.
See [RESEARCH_PROTOCOL.md](RESEARCH_PROTOCOL.md) for the experiment method.

## What BANKING77 means

BANKING77 is a public dataset of English online banking questions, released by PolyAI.
A dataset is a collection of examples used to train or test a model.
Each BANKING77 example contains a customer question and an intent label.
An intent label identifies the request type. The number 77 refers to the 77 request types in the dataset.

The full dataset contains 10,003 training examples and 3,080 test examples.
These counts describe the full dataset, not our eight-category subset.

For example, an authored illustration is: "My card has not arrived" -> `card_arrival`.
The label means that the request concerns card delivery.
This illustration is not presented as a quoted dataset record.

### How this project uses BANKING77

Use eight selected categories to train and test the intent classifier.
The classifier answers: "What type of request is this?"
Keep the original training and test groups separate.
Use part of the training group for validation, which helps select model settings.
Report results for the selected categories only.

### What BANKING77 does not provide

BANKING77 is a dataset, not a language model or a banking application.
It does not provide account status, bank policies, approved replies, or context-dependent next actions.
Create those items separately through the fictional policy and reviewed synthetic scenarios.
The 20 initial project scenarios are separate from BANKING77.
BANKING77 alone cannot establish whether a proposed banking reply is correct.

Source: [PolyAI dataset description](https://github.com/PolyAI-LDN/task-specific-datasets#banking).
The source requests citation of *Efficient Intent Detection with Dual Sentence Encoders* (Casanueva et al., 2020).
Preserve dataset attribution under CC BY 4.0 when importing the data.

## Functional requirements

- FR-1: Import only the eight BANKING77 labels listed below. Preserve exact labels and original training/test membership. Derive validation data only from training data. Record source position or hash in each source ID. Preserve license attribution.
- FR-2: Store each authored case with its ID, scenario family, policy version, message, and simulated context. Include proposed intent, action, reply, source type, author method, review status, and training eligibility. Store actual reviewer identity and review time separately. Do not overwrite the proposal.
- FR-3: Train a CPU classifier with text features and a linear model. Report intent results separately from policy selection. Do not call this classifier an SLM.
- FR-4: Apply DEMO_POLICY.md to the intent and available context. Use only the five actions listed below. Use clarification or human review for uncertain cases. Select thresholds with validation data. Do not treat a threshold score as a correctness probability.
- FR-5: Return the intent, action, policy IDs, policy version, and reply draft. State whether human review is recommended. Never claim that the application completed a bank operation.
- FR-6: Provide local accept, edit, reject, and defer controls. Preserve original proposals and separate corrections. Keep each initial case ineligible until an actual review occurs.
- FR-7: Compare templates with an existing SLM that runs on CPU. Supply the same selected action and policy to both methods. Measure memory and response time first. Retain templates if the SLM is unsuitable. Do not require a paid model or API.
- FR-8: Measure intent, action correctness, reply-policy consistency, fallback, coverage, and critical failures separately. Keep related scenarios and paraphrases in one data group. Reserve unseen final scenarios before settings are selected.

### Exact BANKING77 labels

- `card_arrival`
- `activate_my_card`
- `card_not_working`
- `pending_transfer`
- `failed_transfer`
- `Refund_not_showing_up`
- `transaction_charged_twice`
- `card_payment_not_recognised`

### Exact action names

- `ask_clarification`
- `explain_status`
- `guide_self_service`
- `escalate_human`
- `decline_out_of_scope`

## Non-functional requirements

- NFR-1: Run data preparation, training, evaluation, and the demonstration locally on CPU. Do not require paid APIs. Record Python and package versions, random seed, source hashes, data-group assignments, and code revision.
- NFR-2: Keep source datasets and proposals unchanged. Preserve source links in derived records. Do not accept private customer material or credentials.
- NFR-3: Never request passwords, PINs, OTPs, CVVs, or full card numbers. Never claim that the application transferred funds, refunded money, blocked a card, or filed a real dispute.
- NFR-4: Measure response time and memory use on the available computer. Do not claim a performance guarantee before measurement. Setup detected approximately 12 GB RAM.
- NFR-5: Reject invalid input, missing policy versions, malformed model output, and unknown actions. Show a clear operator error or use an approved fallback. Do not continue with an unchecked result.

## Constraints

Use Windows and PowerShell in `D:/Antern/banking-support-slm`.
No GPU or paid-compute budget is available.
Initial public downloads require internet access. They do not require a cloud account or credit card.
The prototype supports English only. All account states and workflow policies are simulated.
Policy version `demo-bank/v0.1` is the scenario reference.
Each initial record still requires an annotation review.
Authored cases do not establish real banking correctness.
Follow PLAN.md for implementation order.
Ask the project owner about material changes to the agreed scope.

## Non-goals

- Real account access, money movement, or production banking deployment.
- Credit scoring, lending decisions, investment advice, or fraud determination.
- SLM pretraining or mandatory generative-model fine-tuning.
- A hosted website, vector database, paid model judge, or multiple-agent system.
- Claims about all 77 BANKING77 categories or the complete benchmark.

## Acceptance criteria

These criteria describe future checks. They do not report completed tests.

- AC-1: Verify selected labels, source checksums, attribution, separate data groups, and preserved official test membership. Save a duplicate and near-duplicate report. Identify duplicate groups that cross development/test boundaries.
- AC-2: Reject missing IDs, unknown actions, unknown policies, and training eligibility without review evidence. Accept all 20 initial cases as unreviewed and ineligible.
- AC-3: Train and run the baseline on CPU without API credentials. Produce repeatable data-group assignments and metrics. Record the configuration.
- AC-4: Use a separate authored final set. Report acceptable-action accuracy, valid policy references, critical violations, fallback rate, and answer coverage. Do not use this set to select prompts, thresholds, or models.
- AC-5: Test secret requests, false operation claims, invented deadlines, unsupported requests, and policy-override instructions. Every critical test case must pass before the local demonstration is ready.
- AC-6: Preserve proposals when a reviewer makes a decision. Record identity, time, and corrections. Exclude deferred and rejected cases from training exports.
- AC-7: Record the model revision, generation settings, CPU, RAM, runtime, and errors for at least 20 development cases. If execution is blocked, document the cause without claiming a successful SLM test. When execution succeeds, retain paired template and SLM outputs. Use the same cases, actions, and policies. Record policy violations, fallback, coverage, response time, and memory.
- AC-8: Record provisional targets before final evaluation: intent macro-F1 >= 0.85 and acceptable-action accuracy >= 0.90. Report actual scores, denominators, per-class results, and coverage if targets fail. Do not change targets after inspecting final results to claim success. These targets are not published benchmark standards or proof of a research contribution.
- AC-9: Follow RESEARCH_PROTOCOL.md for the final comparison. Fix case counts, scoring rules, and configurations before final testing. Report paired outcomes, uncertainty across scenario families, reviewer sources, coverage, and violations before and after fallback. Separate reference-action tests from complete-system tests. Report negative findings and research limits. Do not claim unsupported superiority.

## Risks

Public intent labels do not specify context-dependent actions. Separate reviewed scenarios are required.
A small SLM can invent facts or run slowly. Preserve failures and compare outputs with templates.
Related synthetic cases can cross data groups. Group cases by source and scenario family before assignment.
Human review must have actual source records. Automated checks do not establish substantive correctness.
No domain expert or second reviewer is confirmed. A solo review is not independent domain validation.
Report the absence of independent review as a research limitation.
Routine implementation can continue without an independent reviewer.

## Open questions

Confirm the reproducible environment before installing dependencies.
Confirm capacity for the remaining project work. All five foundational maths topics are scheduled for Week 1.
The project owner has 14 years of programming experience and knows Python.
Identify a suitable reviewer if independent assessment becomes available.
