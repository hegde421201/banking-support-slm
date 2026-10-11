# DATA-2 review

Status: data preparation is complete. All 11 automated checks passed.
No independent human review has been performed.

## Results

| Data group | Questions |
|---|---:|
| excluded | 17 |
| test | 320 |
| train | 933 |
| validation | 264 |

All eight categories appear in training, validation, and test data.
The source contains 1,214 training questions and 320 test questions for these eight categories.
The preparation step excluded 17 source-training questions because their duplicate groups overlap the official test set.
No official test question was moved or removed.

The lexical check found 39 matching pairs in 28 groups.
It checks exact text, normalized text, and token overlap.
It can miss semantic paraphrases. It can also flag distinct questions.
The test does not establish that all remaining questions are semantically independent.

## Files to review

- [Preparation code](../src/prepare_data.py)
- [Eleven automated tests](../tests/test_prepare_data.py)
- [Source and output manifest](../reports/data_manifest.json)
- [Duplicate report](processed/banking77_v1/duplicate_report.json)
- [Data instructions](README.md)
- [Attribution](processed/banking77_v1/ATTRIBUTION.json)

## Automated checks

The checks verify source hashes, selected labels, original text, and official test membership.
They check that data groups have no shared IDs or detected duplicate groups.
They compare saved files with freshly prepared results.
They check license retention and reject changed source files.
They exercise malformed CSV, quoted multiline text, and transitive duplicate groups.
They verify stable assignments and a byte-identical offline repeat run.

Run from the project folder:

```powershell
C:/Python312/python.exe -m unittest discover -s tests -p test_prepare_data.py -v
```

## Optional independent assessment

These checks can support a later independent assessment. They do not block the next development task.

Check that the selected labels match SPEC.md.
Check that only official training records enter training and validation.
Check the duplicate rule and the exclusion policy.
Check that the manifest records the source revision and checksums.
Record an actual reviewer identity and decision after reviewing the code and evidence.
A passed automated check is not an independent human review.

No classifier or SLM has been trained in this task.
