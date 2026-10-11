# Implementation plan

## Purpose

This plan lists the work needed to build and test the research system.
A task is one defined piece of work.
A task is complete only when its required checks pass.

This document is the current task list.
The assistant manages implementation and reports completed checks.

## Status

The specification has been reviewed.
The project owner approved this plan on 11 October 2026.
DATA-1 is complete. All 12 tests passed.
DATA-2 is complete. All 11 data preparation tests passed.
BASE-1 is next: build and evaluate the CPU classifier, policy rules, and reply templates.
Checks for later tasks are still planned.

## Tasks in order

| Task | Work | Required output |
|---|---|---|
| DATA-1 | Check scenario records and separate human review records. | A validator and tests. The 20 initial records remain unchanged. |
| DATA-2 | Import the eight selected BANKING77 categories. | Data with source information, separate data groups, and duplicate checks. |
| BASE-1 | Build the classifier, policy rules, and reply templates. | A CPU baseline with tests for incorrect and unsafe outputs. |
| EVAL-1 | Define scenario groups, review scores, and comparison methods. | A fixed test method and evaluation program. |
| SLM-1 | Run the selected SLM on CPU. Compare its replies with templates. | Measured quality, response time, and memory use, or a documented execution problem. |
| REVIEW-1 | Build a local interface for human review. | Separate accept, edit, reject, and defer records with source links. |
| REPORT-1 | Fix the final settings. Run the final comparison. | Results, failure analysis, research limits, reproduction steps, and a local demonstration. |

Each task after DATA-1 depends on the previous task.
The plan check confirms that these tasks cover all 22 specification requirements.
It does not confirm that the software works.
Independent review remains useful for research quality.
No independent review is claimed. Its absence does not stop routine development.

## DATA-1 details

Create these files:

- `src/schema.py`: checks scenario records and review records.
- `tests/test_schema.py`: tests valid and invalid records.

Read these files without changing them:

- `examples/starter_cases.jsonl`
- `DEMO_POLICY.md`
- `SPEC.md`

Check the following items:

1. Check required fields and field types.
2. Check that record IDs are unique.
3. Check request labels, actions, policy IDs, and policy versions.
4. Check source information and development-data membership.
5. Link each review record to its original proposal.
6. Require a reviewer ID and a timestamp with a time zone.
7. Preserve the proposal when a reviewer changes a label or reply.
8. Check corrected values before the record can become eligible for training.
9. Keep unreviewed, rejected, and deferred records ineligible for training.
10. Test invalid records, duplicate IDs, broken links, and review-state changes.

This task uses the Python standard library.
It does not download data or models.
It does not train a model or build the review interface.

Run this check after implementation:

```powershell
C:/Python312/python.exe -m unittest discover -s tests -p test_schema.py -v
```

Run the command from the project folder.
The test files now exist. The DATA-1 check passed.
To check the original cases directly, run:

```powershell
C:/Python312/python.exe src/schema.py examples/starter_cases.jsonl
```

Expected result: 20 valid records and zero records eligible for training.
A record-format check cannot establish reviewer identity or label correctness.
Those items require actual review evidence.

## Proposed schedule

| Week | Main work | Evidence |
|---|---|---|
| 1 | Fix the protocol. Review the initial scenarios. Check the environment. | Agreed methods, assumptions, and actual review records. |
| 2 | Validate records and prepare public data. | Source hashes, label mapping, and separate data groups. |
| 3 | Build the baseline. | Validation scores and an error table by request type. |
| 4 | Prepare separate development and final scenario sets. | Review rules, reviewer records, and scenario-family assignments. |
| 5 | Measure SLM performance on CPU. | Model settings, memory, response times, and errors. |
| 6 | Compare replies on development cases. | Paired scores, policy errors, and fallback results. |
| 7 | Add human review and repeat failure checks. | Review records and regression test results. |
| 8 | Fix settings and run the final test. | Research report and reproducible results. |

Week 1 includes all five maths topics from [the notes schedule](research-notes/README.md).
The provisional maths budget is 24-30 hours. Later weekly capacity is not confirmed.
The project owner has 14 years of programming experience and knows Python.
Do not use final test cases to select settings.
If the SLM is unsuitable, report the measured reason and retain the baseline.

## Checks within the work

Trace one complete case from message to policy action.
Check data sources and separation before model work.
Inspect token lengths and model inputs during the SLM experiment.
Use small numerical traces when they help explain a model error.
Change one experimental factor at a time.
Keep records of failed cases and rejected alternatives.
These checks support the research method. They are not additional product features.
