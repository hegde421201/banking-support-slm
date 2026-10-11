"""Prepare an attributed BANKING77 subset with a fixed source and split rule.

Run: python src/prepare_data.py --download
Later runs work offline without --download. Existing source/output files are
never silently replaced. A changed preparation rule requires a new output root.
Near-duplicate detection is a lexical heuristic, not semantic paraphrase proof.
"""
import argparse
from collections import Counter, defaultdict
import csv
import hashlib
import io
import json
from pathlib import Path
import platform
import re
import subprocess
import unicodedata
from urllib.request import urlopen

REVISION = "57ec275d8078af65b7731c2a98be812d844a6d6b"
REPOSITORY = "https://github.com/PolyAI-LDN/task-specific-datasets"
SEED = "20261011"
VALIDATION_FRACTION = 0.2
NEAR_THRESHOLD = 0.9
LABELS = (
    "card_arrival", "activate_my_card", "card_not_working", "pending_transfer",
    "failed_transfer", "Refund_not_showing_up", "transaction_charged_twice",
    "card_payment_not_recognised",
)
SOURCES = {
    "train.csv": ("banking_data/train.csv", "b06e26ac675513959a63135f11b94ea7786ed02da65db93a5650d8838cbc664b"),
    "test.csv": ("banking_data/test.csv", "d12d6e3bc4c3103966ae786dc435913c0c563dfa328f5a3646d0e62cfeeb474d"),
    "categories.json": ("banking_data/categories.json", "53261da888122daf2d120d925458631d9619e15d82e56052e7a42e535ce32b63"),
    "LICENSE": ("LICENSE", "7e7170e3cebf88a9f60c7b8421418323c09304da1af4d5e90f4da1dc1c8a2661"),
    "README.md": ("README.md", "7b9ce9069931cc2de89dce8c7ffb53d07806cf413601ccf133b9af5227b3a373"),
}
ATTRIBUTION = {
    "dataset": "BANKING77", "publisher": "PolyAI", "license": "CC BY 4.0",
    "repository": REPOSITORY, "revision": REVISION,
    "citation": "Casanueva, Temcinas, Gerz, Henderson and Vulic (2020). Efficient Intent Detection with Dual Sentence Encoders.",
    "paper": "https://arxiv.org/abs/2003.04807",
    "changes": "Selected eight categories; derived validation groups from official train; excluded train/test overlaps from development use. Original text and labels retained.",
}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def encoded(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")


def source_url(name):
    return f"https://raw.githubusercontent.com/PolyAI-LDN/task-specific-datasets/{REVISION}/{SOURCES[name][0]}"


def verified_sources(root, download=False):
    folder = root / "data/raw" / REVISION
    result = {}
    for name, (_, expected) in SOURCES.items():
        path = folder / name
        if not path.exists():
            if not download:
                raise ValueError(f"Missing source {name}; run with --download")
            content = urlopen(source_url(name), timeout=45).read()
            if sha(content) != expected:
                raise ValueError(f"Source checksum mismatch: {name}")
            folder.mkdir(parents=True, exist_ok=True)
            with path.open("xb") as stream:
                stream.write(content)
        content = path.read_bytes()
        if sha(content) != expected:
            raise ValueError(f"Source checksum mismatch: {name}")
        result[name] = content
    return result


def read_rows(content, original_split, categories):
    reader = csv.DictReader(io.StringIO(content.decode("utf-8"), newline=""))
    if reader.fieldnames != ["text", "category"]:
        raise ValueError("Unexpected CSV columns")
    result = []
    for position, row in enumerate(reader, 1):
        if set(row) != {"text", "category"} or not row["text"] or not row["text"].strip():
            raise ValueError(f"Invalid CSV row {position}")
        if row["category"] not in categories:
            raise ValueError(f"Unknown source category at row {position}")
        text_hash = sha(row["text"].encode("utf-8"))
        result.append({"id": f"banking77:{REVISION}:{original_split}:{position}:{text_hash[:12]}",
                       "text": row["text"], "intent": row["category"],
                       "original_split": original_split, "source_row": position,
                       "text_sha256": text_hash, "source_revision": REVISION})
    return result


def normalize(text):
    return " ".join(re.findall(r"\w+", unicodedata.normalize("NFKC", text).casefold()))


def partition(rows):
    """Group lexical duplicates before splitting; never move official test rows."""
    parents = list(range(len(rows)))

    def find(i):
        while parents[i] != i:
            parents[i] = parents[parents[i]]
            i = parents[i]
        return i

    normalized = [normalize(row["text"]) for row in rows]
    tokens = [set(text.split()) for text in normalized]
    edges = []
    for i in range(len(rows)):
        for j in range(i):
            exact = rows[i]["text"] == rows[j]["text"]
            same = normalized[i] == normalized[j]
            union = tokens[i] | tokens[j]
            score = len(tokens[i] & tokens[j]) / len(union) if union else 0.0
            if not (same or score >= NEAR_THRESHOLD):
                continue
            parents[find(i)] = find(j)
            edges.append({"left": rows[j]["id"], "right": rows[i]["id"],
                          "kind": "exact" if exact else "normalized" if same else "near",
                          "token_jaccard": round(score, 6)})
    groups = defaultdict(list)
    for i, row in enumerate(rows):
        groups[find(i)].append(row)
    outputs = {name: [] for name in ("train", "validation", "test", "excluded")}
    clusters = []
    for members in groups.values():
        group_id = sha("\n".join(sorted(row["id"] for row in members)).encode("utf-8"))
        has_test = any(row["original_split"] == "test" for row in members)
        # A fixed hash assigns whole groups. It targets 20%, not an exact count.
        ratio = int(sha(f"{SEED}:{group_id}".encode()), 16) / (2 ** 256)
        target = "validation" if ratio < VALIDATION_FRACTION else "train"
        for row in members:
            split = "test" if row["original_split"] == "test" else "excluded" if has_test else target
            outputs[split].append({**row, "split": split, "duplicate_group": group_id,
                                   "exclusion_reason": "official_test_overlap" if split == "excluded" else None})
        if len(members) > 1:
            clusters.append({"group": group_id, "ids": sorted(row["id"] for row in members),
                             "source_splits": sorted({row["original_split"] for row in members}),
                             "labels": sorted({row["intent"] for row in members})})
    for records in outputs.values():
        records.sort(key=lambda row: row["id"])
    by_id = {row["id"]: row["split"] for records in outputs.values() for row in records}
    for edge in edges:
        edge["output_splits"] = [by_id[edge["left"]], by_id[edge["right"]]]
    audit = {"method": "NFKC + casefold + word tokens; exact/normalized matches or token-set Jaccard >= 0.9; connected components",
             "limitation": "Lexical screening can miss paraphrases and flag distinct questions. No semantic-duplicate claim. Threshold fixed before inspection; no label-based threshold tuning.",
             "policy": "Preserve official test records; exclude overlapping official-train groups; assign remaining groups together.",
             "threshold": NEAR_THRESHOLD, "edges": edges,
             "clusters": sorted(clusters, key=lambda group: group["group"]),
             "excluded_train_count": len(outputs["excluded"])}
    return outputs, audit


def build(raw):
    categories = json.loads(raw["categories.json"])
    if not isinstance(categories, list) or len(categories) != 77 or len(set(categories)) != 77:
        raise ValueError("Expected 77 unique source categories")
    if not set(LABELS) <= set(categories):
        raise ValueError("A selected label is absent from the source")
    all_rows = {split: read_rows(raw[f"{split}.csv"], split, categories) for split in ("train", "test")}
    if {key: len(value) for key, value in all_rows.items()} != {"train": 10003, "test": 3080}:
        raise ValueError("Unexpected official source counts")
    selected = [row for rows in all_rows.values() for row in rows if row["intent"] in LABELS]
    outputs, audit = partition(selected)
    for split in ("train", "validation", "test"):
        if {r["intent"] for r in outputs[split]} != set(LABELS):
            raise ValueError(f"Missing selected category in {split}")
    return outputs, audit


def prepare(root, download=False):
    raw = verified_sources(root, download)
    outputs, audit = build(raw)
    folder = "data/processed/banking77_v1"
    artifacts = {f"{folder}/{split}.jsonl": b"".join(
        (json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n").encode("utf-8") for row in rows)
        for split, rows in outputs.items()}
    artifacts[f"{folder}/duplicate_report.json"] = encoded(audit)
    artifacts[f"{folder}/label_mapping.json"] = encoded({label: i for i, label in enumerate(LABELS)})
    artifacts[f"{folder}/ATTRIBUTION.json"] = encoded(ATTRIBUTION)
    artifacts[f"{folder}/LICENSE"] = raw["LICENSE"]
    artifacts["data/README.md"] = ("# BANKING77 data\n\n"
        "Run `C:/Python312/python.exe src/prepare_data.py --download` from the project folder.\n"
        "Later runs work offline without `--download`. No external Python package is required.\n"
        "Raw files stay unchanged in `data/raw/` at the recorded source revision.\n"
        "The processed folder contains train, validation, test, and excluded JSONL files.\n"
        "Validation comes only from official training data. The official test membership stays unchanged.\n"
        "The fixed group-hash rule targets 20% validation. It does not force an exact class ratio.\n"
        "Related lexical matches stay together. Training records that overlap test records are excluded.\n"
        "The duplicate report lists exact, normalized, and possible near-duplicate matches by ID.\n"
        "This heuristic does not detect all semantic paraphrases.\n"
        "Use the final test only after model settings are fixed. Do not use excluded records for development.\n"
        "Public intent records use a separate schema from authored scenario records.\n"
        "No human review or approved reply is implied by a public intent label.\n"
        "See `../reports/data_manifest.json` for counts, source links, checksums, and execution details.\n"
        "See `processed/banking77_v1/ATTRIBUTION.json` and `LICENSE` for credit and license terms.\n"
        "Existing files are checked before writes. Different outputs require a separate output root.\n").encode()
    run = subprocess.run(["git", "-C", str(root), "rev-parse", "HEAD"], capture_output=True, text=True)
    manifest = {"attribution": ATTRIBUTION, "selected_labels": list(LABELS),
        "official_counts": {"train": 10003, "test": 3080},
        "counts": {split: len(rows) for split, rows in outputs.items()},
        "per_label": {split: dict(sorted(Counter(r["intent"] for r in rows).items())) for split, rows in outputs.items()},
        "split_rule": {"seed": SEED, "validation_fraction_target": VALIDATION_FRACTION,
                       "algorithm": "SHA256(seed:component-ID) / 2^256 < 0.2; group IDs hash sorted source IDs"},
        "source_files": {name: {"url": source_url(name), "sha256": sha(content)} for name, content in raw.items()},
        "artifacts": {name: sha(content) for name, content in artifacts.items()},
        "environment": {"python": platform.python_version(), "platform": platform.platform(), "dependencies": "Python standard library only"},
        "code": {"git_revision": run.stdout.strip() if run.returncode == 0 else None,
                 "prepare_data_sha256": sha(Path(__file__).read_bytes()),
                 "note": "No commit exists yet; script checksum records the implementation used." if run.returncode else "Script checksum also identifies working-file changes."},
        "duplicate_summary": {"pairs": len(audit["edges"]), "clusters": len(audit["clusters"]),
                              "excluded_train_count": audit["excluded_train_count"]}}
    artifacts["reports/data_manifest.json"] = encoded(manifest)
    # Preflight all paths before changing any existing artifact.
    for name, content in artifacts.items():
        path = root / name
        if path.exists() and path.read_bytes() != content:
            raise ValueError(f"Refusing to replace changed artifact: {name}; use a new output root")
    for name, content in artifacts.items():
        path = root / name
        if not path.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open("xb") as stream:
                stream.write(content)
    return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--download", action="store_true")
    args = parser.parse_args()
    try:
        manifest = prepare(args.root.resolve(), args.download)
    except (OSError, ValueError) as exc:
        parser.exit(1, f"Data preparation failed: {exc}\n")
    print(json.dumps({"counts": manifest["counts"], "duplicates": manifest["duplicate_summary"]}))


if __name__ == "__main__":
    main()
