# BANKING77 data

Run `C:/Python312/python.exe src/prepare_data.py --download` from the project folder.
Later runs work offline without `--download`. No external Python package is required.
Raw files stay unchanged in `data/raw/` at the recorded source revision.
The processed folder contains train, validation, test, and excluded JSONL files.
Validation comes only from official training data. The official test membership stays unchanged.
The fixed group-hash rule targets 20% validation. It does not force an exact class ratio.
Related lexical matches stay together. Training records that overlap test records are excluded.
The duplicate report lists exact, normalized, and possible near-duplicate matches by ID.
This heuristic does not detect all semantic paraphrases.
Use the final test only after model settings are fixed. Do not use excluded records for development.
Public intent records use a separate schema from authored scenario records.
No human review or approved reply is implied by a public intent label.
See `../reports/data_manifest.json` for counts, source links, checksums, and execution details.
See `processed/banking77_v1/ATTRIBUTION.json` and `LICENSE` for credit and license terms.
Existing files are checked before writes. Different outputs require a separate output root.
