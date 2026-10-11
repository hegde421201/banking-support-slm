# Research notes

Use this folder for your explanations, calculations, code notes, and experiment decisions.
Write the content in your own words as you work.
The files contain prompts only. No topic is marked complete.

## Working approach

The project owner has 14 years of programming experience and knows Python.
Focus on ML mathematics, notation, assumptions, and experimental reasoning.
Use Python directly to check calculations. Skip introductory programming exercises.
Use familiar topics as a quick diagnostic, not a mandatory lesson.

## Week 1: mathematics

Cover all five maths topics in Week 1.
The provisional budget is 24-30 hours, including exercises and a final integration session.
This is an estimate, not a claim about available time or a guarantee of mastery.
Revisit difficult concepts during project experiments.

| Day | Note | Hours | Practical output |
|---|---|---:|---|
| 1 | [MATH-01: notation, functions, and algebra](01-arithmetic-algebra-functions.md) | 1-2 | Translate a model formula into Python. Review ratios only if needed. |
| 2 | [MATH-02: vectors, matrices, and TF-IDF](02-vectors-dot-products-tfidf.md) | 4-5 | Compute message features and category scores. Check array dimensions. |
| 3 | [MATH-03: logarithms and probability](03-logarithms-probability.md) | 4-5 | Convert scores to probabilities. Explain normalization. |
| 4-5 | [MATH-04: gradients, loss, and training](04-gradients-loss-training.md) | 8-9 | Calculate a gradient and check one weight update. |
| 6 | [MATH-05: evaluation and uncertainty](05-evaluation-statistics.md) | 4-5 | Calculate metrics from predictions. Explain sample-size limits. |
| 7 | Integration across the five notes | 3-4 | Trace features, scores, probabilities, loss, an update, and evaluation in one small Python example. |

## Other project notes

| Note ID | Topic | When |
|---|---|---|
| ENG-01 | [Data engineering and reproducibility](06-python-and-data.md) | During data preparation and experiment setup. |
| MODEL-01 | [Intent classifier and policy rules](07-classifier-and-policy.md) | During baseline work. |
| MODEL-02 | [SLM internals and CPU inference](08-slm-internals.md) | During the SLM experiment. |
| RES-01 | [Experiments, failures, and decisions](09-experiments-and-decisions.md) | After each experiment. |

## Status and links

Use these status values: Not started, Draft, or Ready for review.
A ready note must explain the topic and identify its supporting example or result.
Do not mark a topic ready only because you read a source.

Keep the note ID stable when you change the title.
The tags are plain text. No plugin or special software is required.
Later, use these IDs to connect the notes to the code, tests, and research report.
For example, MODEL-01 can identify a note about the classifier.
Add actual file links only when the files exist.

## Interview reference

When a note is ready, add its link to the relevant project document.
Keep draft notes separate from claims about completed research.
Use the interview section to explain a decision and the evidence behind it.
State what you implemented and what assistance you received.

## New topics

Create another Markdown file when a useful topic does not fit an existing note.
Reuse the headings from one of these templates.
Add the file to this index.
