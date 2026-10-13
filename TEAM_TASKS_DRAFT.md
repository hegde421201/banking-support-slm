# Team task list: eight weeks

Date: 14 October 2026.
Status: Draft.

This document uses ASD-STE100 writing principles.
A full dictionary compliance review is not complete.
PLAN.md remains the current implementation task list.

## 1. Responsibilities

| Person | Responsibility |
|---|---|
| Project lead (you) | Mathematics, code, data preparation, experiments, and technical checks. |
| Collaborator 1 | Video scene plan, figures, and animation. |
| Collaborator 2 | Video script, voice recording, captions, editing, and report. |

The two collaborators are the video team.
The video team can change its task allocation.
The project lead checks the mathematics in the video.
Each person must understand their contribution.
Each person keeps a separate public-post log.

## 2. Technical terms

| Term | Meaning in this document |
|---|---|
| Baseline | A method used as a reference for comparison. |
| LoRA | A training method that changes a model through small additional matrices. |
| Adapter | The additional model weights produced by LoRA training. |
| Rank | The size of the intermediate dimension in the LoRA matrices. |
| Alpha | A value that controls the size of the LoRA update. |
| Epoch | One pass through the training data. |
| SOP | Standard operating procedure: written instructions for data reviewers. |
| Development data | Examples used to select prompts and model settings. |
| Validation data | Examples used to check training and select settings. |
| Final test data | Reserved examples used after settings are fixed. |
| Scenario family | A group of related examples that must stay in one data group. |
| Frontier model | A comparison model, such as a selected GPT or Claude model. |
| Scorecard | A table of model results measured with the same scoring rules. |
| Dry run | A check of the data format and estimated cost before training. |

## 3. Project scope

The current project compares template replies with SLM replies on a CPU.
The current scope does not require model training or paid APIs.

Part C requires a Qwen model trained with LoRA on Tinker.
Part C also requires a comparison with a frontier model.
These requirements change the current project scope.

- [ ] Confirm the scope change with the project owner.
- [ ] Confirm access to Tinker.
- [ ] Confirm access to the frontier model.
- [ ] Set a maximum cost before a paid run.

For the proposed course extension, use this behavior:

> Select a permitted action from the message, simulated context, and fictional policy. Produce a reply draft for human review.

The model must produce the action and the reply draft.
The existing classifier, policy rules, and templates remain a separate baseline.
The experiments must establish whether LoRA improves the behavior.

## 4. Week 1: define the work

### Project lead

- [ ] Confirm each person's available hours.
- [ ] Define the model input.
- [ ] Define the model output.
- [ ] Define the permitted actions.
- [ ] Record success criteria before training.
- [ ] Study the five mathematics topics in research-notes/README.md.
- [ ] Check matrix dimensions with Python.
- [ ] Calculate one loss value.
- [ ] Calculate one gradient.
- [ ] Check one weight update.
- [ ] Prepare the architecture paper outline.
- [ ] Select one version each of Qwen, Llama, and Mistral.

### Video team

- [ ] Read Part B of the course brief.
- [ ] Make a list of the video requirements.
- [ ] Assign one owner to each video task.
- [ ] Prepare the ten-scene plan.
- [ ] Prepare the script outline.
- [ ] Make one short Manim animation.
- [ ] Use visual Beamer slides if Manim is unsuitable.
- [ ] Record the reason for a Beamer substitution.

Required output: Responsibilities, scope decision, paper outline, and video scene plan.

## 5. Week 2: build the baseline

### Project lead

- [ ] Complete BASE-1 in PLAN.md.
- [ ] Run the required baseline checks.
- [ ] Prepare the review SOP.
- [ ] Arrange human review of the 20 existing proposals.
- [ ] Keep the original proposals unchanged.
- [ ] Plan at least 100 reviewed examples for Part C.
- [ ] Record the planned example count for each data group.
- [ ] Check the calculations in the video.

### Video team

- [ ] Show the frozen matrix W.
- [ ] Show the additional update to W.
- [ ] Show A with dimensions 4 x 64.
- [ ] Show B with dimensions 32 x 4.
- [ ] Show W with dimensions 32 x 64.
- [ ] Show how B multiplied by A has the same dimensions as W.
- [ ] Compare 384 LoRA weights with 2,048 full-update weights.
- [ ] Show the 4,096 x 4,096 example with rank 8.
- [ ] Prepare the report outline.
- [ ] Start the source log.

Required output: Working baseline, SOP draft, and checked animation example.

## 6. Week 3: prepare evaluation

### Project lead

- [ ] Complete EVAL-1 in PLAN.md.
- [ ] Check the data for contradictory labels.
- [ ] Check the number of examples for each label.
- [ ] Check duplicate examples.
- [ ] Check source attribution.
- [ ] Keep each scenario family in one data group.
- [ ] Reserve the final test data before model selection.
- [ ] Read 20 randomly selected training or development examples.
- [ ] Compare prompted Qwen with the frontier model on development data, if access and scope are confirmed.

### Video team

- [ ] Explain the low-rank update.
- [ ] Explain the initial values of A and B.
- [ ] Explain why B starts at zero.
- [ ] Show rank values of 1, 4, and 8.
- [ ] Show the weight count for each rank.
- [ ] Explain alpha/r scaling.
- [ ] Complete the first script.
- [ ] Ask the project lead to check the script.

Required output: Reviewed data, data-group record, scoring program, and complete video script.

## 7. Week 4: prepare the model runs

### Project lead

- [ ] Start SLM-1 after the EVAL-1 checks pass.
- [ ] Select a supported Qwen model for the confirmed course extension.
- [ ] Record the model revision.
- [ ] Record the rank and alpha.
- [ ] Record the target layers.
- [ ] Record the learning rate and epoch count.
- [ ] Record the random seed.
- [ ] Estimate the training cost.
- [ ] Set the maximum training cost.
- [ ] Complete the dry run before training.
- [ ] Prepare the architecture comparison table.
- [ ] Draw at least four original figures for Part A.
- [ ] Explain at least five architecture design changes.

### Video team

- [ ] Show which weights change during training.
- [ ] Show how the trained update is added to W.
- [ ] Explain the target-layer choices.
- [ ] Prepare the first complete video draft.
- [ ] Prepare the first report draft.
- [ ] Mark unconfirmed project settings as pending.

Required output: Dry-run results, recorded settings, paper draft, and video draft.

## 8. Week 5: train the model

### Project lead

Start Tinker training only after scope and access are confirmed.

- [ ] Run LoRA training on Tinker.
- [ ] Save the adapter weights.
- [ ] Record the training loss for each epoch.
- [ ] Record the validation loss for each epoch.
- [ ] Record the actual cost.
- [ ] Record errors and failed runs.
- [ ] Evaluate the model on development and validation data.
- [ ] Give the actual settings to the video team.
- [ ] Explain the reason for each setting.

### Video team

- [ ] Add the actual settings to the project scene.
- [ ] Add the actual settings to the report.
- [ ] Record the voice-over yourselves.
- [ ] Add captions.
- [ ] Complete the animation.
- [ ] Complete the video editing.
- [ ] Check each question in Part B.5 against the video.

Required output: Saved adapter, run records, development results, and complete video draft.

## 9. Week 6: check the work

### Project lead

- [ ] Examine development failures.
- [ ] Select changes only from development and validation results.
- [ ] Complete REVIEW-1 after its required earlier tasks pass.
- [ ] Fix the final prompt.
- [ ] Fix the final model and adapter.
- [ ] Fix the policy version.
- [ ] Fix the scoring rules.
- [ ] Check the technical content of the architecture paper.
- [ ] Check the technical content of the video.
- [ ] Check the technical content of the LoRA report.

### Video team

- [ ] Correct technical errors.
- [ ] Correct unclear scenes.
- [ ] Check that the video duration is 10-20 minutes.
- [ ] Check that the figures are readable.
- [ ] Check the captions against the recording.
- [ ] Check that the LaTeX report has 4-6 pages.
- [ ] Include references in the report.
- [ ] Include video figures in the report.
- [ ] Prepare the animation source for publication.
- [ ] Record each person's contribution.

Required output: Fixed experiment settings and checked Part B files.

## 10. Week 7: run the final evaluation

### Project lead

- [ ] Run the final evaluation with the fixed settings.
- [ ] Score base Qwen on the final test data.
- [ ] Score the frontier model on the same final test data.
- [ ] Score trained Qwen on the same final test data.
- [ ] Use the same prompt for base Qwen and the frontier model.
- [ ] Apply the same scoring rules to all three models.
- [ ] Report action accuracy for each action type.
- [ ] Report reply scores.
- [ ] Record at least five trained-model failures, if five failures occur.
- [ ] Report the actual failure count if fewer than five failures occur.
- [ ] Keep all final failure records.
- [ ] Do not change settings from final test results.

A later model revision needs new final test data.

### Video team

- [ ] Review model outputs with the fixed SOP, if time permits.
- [ ] Record the reviewer for each review.
- [ ] Record disagreements between reviewers.
- [ ] Hide the model identity during review where possible.
- [ ] Follow the README instructions as a new user.
- [ ] Record problems in the demonstration.

Required output: Three-model scorecard, failure analysis, and reproduction checks.

## 11. Week 8: prepare the submission

### Project lead

- [ ] Complete REPORT-1 in PLAN.md.
- [ ] Record the research limits.
- [ ] Include the commands needed to repeat the experiment.
- [ ] Prepare the local demonstration.
- [ ] Complete the 10-15-page architecture paper in LaTeX.
- [ ] Complete the reading log.
- [ ] Include the dataset or a dataset sample.
- [ ] Include the review SOP.
- [ ] Include the configuration file.
- [ ] Include the results and scorecard.
- [ ] Draw one Mermaid diagram that follows an example through the files.
- [ ] Draw one Mermaid diagram that shows the training steps.
- [ ] Check the submission for API keys.
- [ ] Check the submission for personal data.
- [ ] Check source attribution.
- [ ] Check each result claim against recorded evidence.
- [ ] Keep the actual commit history.

### Video team

- [ ] Check the final video.
- [ ] Check the final captions.
- [ ] Check the final report.
- [ ] Check the animation source.
- [ ] Prepare the video publication details.
- [ ] Prepare the submission links.
- [ ] Complete the contribution record.

Required output: Parts A, B, and C ready for submission, plus individual Part D logs.

## 12. Tasks for every week

- [ ] Assign an owner to each task.
- [ ] Record the required output for each task.
- [ ] Check problems at the middle of the week.
- [ ] Show completed work at the end of the week.
- [ ] Commit each completed code change.
- [ ] Record experiment decisions.
- [ ] Record failed experiments.
- [ ] Prepare 3-5 public posts per person each week, if time permits.
- [ ] Record each post's date, platform, link, part, and topic.

Part D requires 150-200 posts from each person.
Part D has no deadline.
The suggested rate gives 24-40 posts per person in eight weeks.
Continue Part D after Week 8.
The same idea on X and LinkedIn counts once.

## 13. Schedule limits

The schedule depends on available hours and model access.
The Week 1 mathematics estimate is 24-30 hours.
Coding requires additional time.

BANKING77 supplies intent labels.
It does not supply reviewed policy decisions or approved replies.
Team review does not establish independent banking expertise.
Local CPU experiments do not satisfy the Tinker training requirement.

- [ ] Record access problems if a model run cannot start.
- [ ] Continue local work and Parts A/B while access is unavailable.
- [ ] Keep original proposals separate from actual review records.
- [ ] Keep final test data separate from model selection.
- [ ] Report measured results, including results that show no improvement.

## 14. Sources

- Course brief: C:/Users/hegde10122/antern/antern-brief-v4.pdf, Parts A-D.
- Implementation tasks: [PLAN.md](PLAN.md).
- Project scope: [SPEC.md](SPEC.md).
- Research method: [RESEARCH_PROTOCOL.md](RESEARCH_PROTOCOL.md).
- Mathematics schedule: [research-notes/README.md](research-notes/README.md).
- Writing reference: [ASD-STE100 Issue 9](https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf).
