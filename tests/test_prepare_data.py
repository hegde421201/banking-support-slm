"""Offline checks for source integrity, partition isolation and saved artifacts."""
import copy
import json
from pathlib import Path
import tempfile
import unittest

from src.prepare_data import (LABELS, REVISION, SOURCES, build, normalize,
                              partition, prepare, read_rows, sha, verified_sources)

ROOT = Path(__file__).resolve().parents[1]
FOLDER = ROOT / "data/processed/banking77_v1"


class DataTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.raw = verified_sources(ROOT)
        cls.outputs, cls.audit = build(cls.raw)
        cls.manifest = json.loads((ROOT / "reports/data_manifest.json").read_text(encoding="utf-8"))

    def test_sources_match_pinned_checksums(self):
        self.assertEqual(len(self.raw), 5)
        for name, content in self.raw.items():
            self.assertEqual(sha(content), SOURCES[name][1])
            self.assertIn(REVISION, self.manifest["source_files"][name]["url"])
        self.assertEqual(len(json.loads(self.raw["categories.json"])), 77)

    def test_selected_rows_preserve_text_labels_and_official_test(self):
        categories = json.loads(self.raw["categories.json"])
        original = [r for split in ("train", "test")
                    for r in read_rows(self.raw[f"{split}.csv"], split, categories)
                    if r["intent"] in LABELS]
        source_by_id = {row["id"]: row for row in original}
        actual = [r for rows in self.outputs.values() for r in rows]
        self.assertEqual(len(actual), len({r["id"] for r in actual}))
        self.assertEqual({r["id"] for r in actual}, set(source_by_id))
        for row in actual:
            for key, value in source_by_id[row["id"]].items():
                self.assertEqual(row[key], value)
        self.assertEqual({r["id"] for r in self.outputs["test"]},
                         {r["id"] for r in original if r["original_split"] == "test"})
        for split in ("train", "validation", "excluded"):
            self.assertTrue(all(r["original_split"] == "train" for r in self.outputs[split]))

    def test_all_eight_labels_and_no_id_or_group_leakage(self):
        splits = ("train", "validation", "test")
        for i, left in enumerate(splits):
            self.assertEqual({r["intent"] for r in self.outputs[left]}, set(LABELS))
            for right in splits[i+1:]:
                for field in ("id", "duplicate_group"):
                    self.assertFalse({r[field] for r in self.outputs[left]} &
                                     {r[field] for r in self.outputs[right]})
        for row in self.outputs["excluded"]:
            self.assertEqual(row["exclusion_reason"], "official_test_overlap")
            self.assertIn(row["duplicate_group"], {r["duplicate_group"] for r in self.outputs["test"]})

    def test_saved_artifacts_match_recomputed_data(self):
        for split, expected in self.outputs.items():
            actual = [json.loads(line) for line in (FOLDER / f"{split}.jsonl").read_text(encoding="utf-8").splitlines()]
            self.assertEqual(actual, expected)
            self.assertEqual(self.manifest["counts"][split], len(actual))
        self.assertEqual(json.loads((FOLDER / "duplicate_report.json").read_text()), self.audit)
        for name, expected in self.manifest["artifacts"].items():
            self.assertEqual(sha((ROOT / name).read_bytes()), expected)
        self.assertEqual(self.manifest["code"]["prepare_data_sha256"],
                         sha((ROOT / "src/prepare_data.py").read_bytes()))
        self.assertEqual(json.loads((FOLDER / "label_mapping.json").read_text()),
                         {label: i for i, label in enumerate(LABELS)})

    def test_license_and_attribution_are_present(self):
        self.assertEqual((FOLDER / "LICENSE").read_bytes(), self.raw["LICENSE"])
        credit = json.loads((FOLDER / "ATTRIBUTION.json").read_text())
        self.assertEqual(credit["license"], "CC BY 4.0")
        self.assertEqual(credit["revision"], REVISION)
        self.assertIn("Casanueva", credit["citation"])
        self.assertIn("Selected eight", credit["changes"])

    def test_corrupt_or_missing_source_fails_closed(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            with self.assertRaisesRegex(ValueError, "Missing source"):
                verified_sources(root)
            raw = root / "data/raw" / REVISION
            raw.mkdir(parents=True)
            (raw / "train.csv").write_bytes(self.raw["train.csv"] + b"corrupt")
            with self.assertRaisesRegex(ValueError, "checksum mismatch"):
                verified_sources(root)
            self.assertFalse((root / "data/processed").exists())

    def test_bad_csv_and_missing_label_are_rejected(self):
        for value in (b"wrong,category\nx,card_arrival\n", b"text,category\n,card_arrival\n",
                      b"text,category\nx,made_up\n", b"text,category\nx,card_arrival,extra\n"):
            with self.subTest(value=value):
                with self.assertRaises(ValueError): read_rows(value, "train", LABELS)
        bad = dict(self.raw)
        categories = json.loads(bad["categories.json"])
        categories[categories.index(LABELS[0])] = "missing_selected_label"
        bad["categories.json"] = json.dumps(categories).encode()
        with self.assertRaisesRegex(ValueError, "selected label"):
            build(bad)

    def test_csv_quoted_multiline_text_is_preserved(self):
        content = b'text,category\n"First line, here\nsecond line",card_arrival\n'
        row = read_rows(content, "train", LABELS)[0]
        self.assertEqual(row["text"], "First line, here\nsecond line")
        self.assertEqual(row["source_row"], 1)

    @staticmethod
    def row(id, text, split="train", label="card_arrival"):
        return {"id": id, "text": text, "original_split": split, "intent": label}

    def test_exact_normalized_and_transitive_near_matches(self):
        words = "one two three four five six seven eight nine ten"
        rows = [self.row("a", words), self.row("b", words + " eleven"),
                self.row("c", words + " eleven twelve", "test"),
                self.row("d", "CARD, please!"), self.row("e", "card please"),
                self.row("f", "CARD, please!")]
        before = copy.deepcopy(rows)
        result, audit = partition(rows)
        self.assertEqual(rows, before)
        self.assertEqual({r["id"] for r in result["excluded"]}, {"a", "b"})
        self.assertEqual({r["id"] for r in result["test"]}, {"c"})
        self.assertEqual({e["kind"] for e in audit["edges"]}, {"exact", "normalized", "near"})
        group_splits = {r["split"] for values in result.values() for r in values if r["id"] in {"d", "e", "f"}}
        self.assertEqual(len(group_splits), 1)
        self.assertEqual(normalize("ＣＡＲＤ, Please!"), "card please")

    def test_assignments_do_not_depend_on_input_order(self):
        rows = [self.row(str(i), f"unique question {i}") for i in range(30)]
        left, _ = partition(rows)
        right, _ = partition(list(reversed(rows)))
        self.assertEqual(left, right)

    def test_offline_rerun_is_byte_identical(self):
        before = (ROOT / "reports/data_manifest.json").read_bytes()
        prepare(ROOT)
        self.assertEqual((ROOT / "reports/data_manifest.json").read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
