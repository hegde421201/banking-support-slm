# Research protocol

The project owner reviewed the research design on 11 October 2026.
This document describes planned experiments. It contains no measured results.
See [START_HERE.md](START_HERE.md) for term definitions and [SPEC.md](SPEC.md) for system requirements.

## Research questions

- RQ1: How accurately does the classifier identify the eight request types? Which types does it confuse?
- RQ2: With the action and policy fixed, how do SLM replies compare with template replies?
- RQ3: How do uncertainty checks and output checks affect policy violations and answer coverage?
- RQ4: What response time and memory use accompany any improvement in reply quality?

RQ2 is the main comparison.
The study does not assume that the SLM is better.
A result with no benefit, or a worse result, remains useful evidence.

## Methods to compare

The baseline uses a linear classifier, explicit policy rules, and fixed reply templates.
The candidate uses the same classifier and policy rules. Only its reply writer changes to an SLM.
Both methods receive the same message, simulated context, selected action, and policy version.
Neither method performs a real banking operation.

Use two separate tests:

1. Supply reviewed reference actions to both reply methods. This test isolates reply-generation errors.
2. Run the complete system with predicted intents and rule-selected actions. This test includes errors from earlier stages.

Report the two tests separately.
Do not attribute a classifier error to the reply generator.

## Experimental controls

Keep cases, action inputs, policy inputs, and scoring rules fixed across each paired comparison.
A paired comparison tests both methods on the same case.
Record prompt versions, template versions, model revision, generation settings, seeds, software versions, and code revision.
Use development data to select prompts and thresholds.
Fix the selected configuration before the final test.
Do not use final results to improve the tested system.

An optional development test can remove policy context from the SLM prompt.
This test measures the effect of that context. It is called an ablation.
Change only that factor. Keep other settings fixed.
Run this test offline only if CPU resources permit.
Do not add it as an application mode.

## Public data

BANKING77 supplies messages and intent labels.
Preserve its original training and test groups.
Derive validation data only from the training group.
Report the eight-intent subset clearly. Do not claim a complete BANKING77 result.

## Authored scenarios

Use DEMO_POLICY.md as the reference for context-dependent actions and replies.
Keep original records unchanged.
Record the source, author method, policy version, scenario family, proposed labels, and review history.
Store reviewer identity, time, and corrections separately.
Keep related cases and paraphrases in the same data group.

The 20 initial cases are development proposals.
They are not final test data or independent annotations.
A model-generated label is not a verified reference label.
Exclude unreviewed, rejected, and deferred cases from training exports.

Before final evaluation, fix these items:

- Case count and coverage for each intent and action.
- Scenario-family assignments to development and final groups.
- Ambiguous cases, conflicting cases, and adversarial cases.
- The reason that the sample is suitable for the intended comparison.

Twenty execution-test cases do not establish adequate statistical power.
If independent review is unavailable, identify the labels as author-reviewed.
State this limitation. Do not claim independent domain validation.

## Scores and measurements

| Item | Report |
|---|---|
| Intent | Macro-F1, precision, recall, F1 by class, confusion matrix, and case counts. |
| Action | Accuracy against reviewed acceptable actions. Separate clarification, escalation, and unsupported-request results. |
| Policy | Valid references, unsupported facts, invented deadlines, secret requests, and false operation claims. |
| Reply usefulness | Relevance, clarity, and a suitable next step. Score each item from 0 to 2. |
| Reliability | Invalid-output rate, critical violations, fallback rate, and answer coverage. Show every denominator. |
| Resources | CPU, RAM, model version, software version, load time, response times, peak process memory, token counts, and run counts. |

Precision measures how often predictions for a class are correct.
Recall measures how many reference cases of a class the system finds.
F1 combines precision and recall. Macro-F1 gives each class equal weight.
A confusion matrix shows the counts for each reference label and predicted label.
A denominator is the number of cases used to calculate a rate.

## Human review scores

Use these anchors for each usefulness item:

- 0: The item is absent or materially wrong.
- 1: The item is partly satisfactory.
- 2: The item is fully satisfactory under the supplied scenario and policy.

Add example scores before final review. Fix the scoring rules before final review starts.
A fluent reply with a critical violation remains a policy failure.
Do not hide critical failures inside an average usefulness score.

Randomize reply order where feasible.
Hide the reply method from reviewers where feasible.
Record reviewer identities, instructions, edits, and disagreements.
If two reviewers are available, report their agreement and the method used to resolve differences.
If one reviewer is available, report the bias risk.
Human review does not automatically establish banking expertise.

## Comparison and uncertainty

Report score differences for each paired case. Report wins, ties, and losses.
Report uncertainty intervals with the method used to calculate them.
An uncertainty interval describes uncertainty in an estimate under the stated method.
It does not guarantee real-bank performance.

For authored cases, resample whole scenario families when estimating uncertainty.
Related cases must remain together during resampling.
Record the random seed, number of families, and method limits.
For small samples, emphasize observed results and uncertainty. Do not make unsupported significance claims.

Before final results, define the minimum improvement that would justify the extra resources.
If no margin is defined, report the tradeoff without declaring a winner.

## Fallback and failure analysis

Report violations in the original generated replies.
Report violations after output checks and fallback separately.
Include all cases, not only successful generations.
A system that rejects every reply must not appear successful because it shows no violations.
Report answer coverage with the violation rate.

For each important development failure, record these items:

- Case ID and expected behaviour.
- Actual behaviour and the stage that failed.
- Possible cause and evidence for that cause.
- Correction and repeat-test result.

Keep a possible cause separate from a demonstrated cause.
Retain final-test failures. Do not tune the system on them.
Record important choices, their reasons, their tradeoffs, and rejected alternatives.

## Resource measurements

Measure model load time separately from reply time.
Measure cold runs and repeated warm runs under recorded conditions.
A cold run includes initial setup effects. A warm run uses the loaded model.
Record response-time distributions and run counts.
Do not claim stable slowest-case statistics from a small sample.
Do not claim performance guarantees before measurement.

## Technical checks

Inspect token lengths and context limits. Check for truncated inputs and invalid data formats.
When useful for diagnosis, trace tensor shapes through embeddings, attention, causal masking, and feed-forward layers.
A tensor is an array of model values. Its shape gives the size of each dimension.

Keep these values distinct: attention weights, next-token probabilities, classifier scores, and measured task correctness.
Logits are model scores before conversion to probabilities.
Cross-entropy measures loss against target tokens. Lower training loss does not prove better replies on unseen cases.

Assess low-rank adapters only if future model adaptation is justified.
An adapter changes selected model computations while the base weights remain fixed.
The current study does not require adapter training or a transformer implementation.

## Deferred components

| Component | Reason to defer | Condition for reconsideration |
|---|---|---|
| LoRA or QLoRA | No demonstrated need for adaptation or reviewed training corpus. | Persistent measured errors, sufficient reviewed data, and suitable resources. |
| RAG or a vector database | The small policy set permits direct selection. | Policy lookup fails as the document set grows. |
| Autonomous or multiple agents | The current sequence is fixed and limited. | A required task needs several tool-use steps. |
| GPU kernels or distributed training | These do not answer the CPU inference question. | A separate systems research objective. |
| RLHF, DPO, GRPO, diffusion, or GANs | These do not answer the current questions. | A separate research protocol. |
| Kafka, Redis, hosted services, or paid judges | The present workload does not require them. | A measured scale, deployment, or evaluation need. |

RAG means retrieval-augmented generation. It supplies retrieved documents to a model.
LoRA and QLoRA are methods for model adaptation.
The other deferred names identify tools or research methods. They are not required project skills or deliverables.

## Limits of the study

- Synthetic context and fictional policies limit transfer to real banks.
- Eight English intent types do not establish multilingual or all-category performance.
- Author-created cases and solo review can introduce bias.
- Templates directly encode policy. This is an intentional practical baseline, not an equal-capacity model comparison.
- One model and one computer limit conclusions about other models and hardware.
- Model pretraining data may be unknown. Public benchmark scores do not prove that the model never saw similar examples.
- Small samples and related cases limit estimate precision.

Report unresolved failures and these limits with the results.

## Final report

Include the question, related work, data sources, method, configuration, results, failure analysis, limits, and reproduction steps.
Review primary research sources before claiming novelty.
The background PDFs alone do not establish novelty.
Provide executable evaluation commands and versioned result files.
Add a short local demonstration.
Match every published claim to completed evidence.
Describe the project as in progress until experiments are complete.

## References

- Ayush Singh / Antern, *LLM Internals: From Tokens to Predictions and Learning*, 152 pages.
  Local source: `C:/Users/hegde10122/antern/llm internals.pdf`.
  Topics: tokens and embeddings, pp. 2-16; attention, pp. 51-95; feed-forward layers, pp. 97-115.
  Further topics: predictions and loss, pp. 117-128; LoRA, pp. 129-151.
  The decoder is an untrained example. Page 140 limits conclusions from reduced training loss.
  This project has not reproduced those experiment records.
- Antern, *AI-Native Engineering Sprint, Cohort 3 / August 2026*, 41 pages.
  Local source: `C:/Users/hegde10122/antern/AI-Native-Engineering-Sprint-Curriculum.pdf`.
  Topics: evaluation, pp. 6-7 and 26-27; data, pp. 18-20; context, pp. 20-22.
  Further topics: security, pp. 27-29; decision and failure analysis, p. 7 and pp. 38-39.

These sources explain background methods. They do not set project requirements.
Local PDF paths are not experiment dependencies.
Do not present source results as results from this project.
