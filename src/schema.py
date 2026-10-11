"""Validate development proposals and separate review events.

This module checks structure, not reviewer identity or banking correctness.
Proposals stay unreviewed. Reviews are append-only events supplied separately.
An accept event approves the original proposal; an edit event supplies a full
replacement decision. The latest event controls eligibility. Reject/defer revoke
eligibility. Timestamps must increase for each case in the supplied event order.
"""
import argparse
from copy import deepcopy
from datetime import datetime
import hashlib
import json
import math
from pathlib import Path

INTENTS = frozenset({
    "card_arrival", "activate_my_card", "card_not_working", "pending_transfer",
    "failed_transfer", "Refund_not_showing_up", "transaction_charged_twice",
    "card_payment_not_recognised", "out_of_scope", "unknown",
})
ACTIONS = frozenset({"ask_clarification", "explain_status", "guide_self_service",
                     "escalate_human", "decline_out_of_scope"})
POLICIES = frozenset({f"P-{n:02d}" for n in (*range(1, 5), *range(10, 18))})
CASE_FIELDS = frozenset({"id", "scenario_family", "split", "source_type",
    "author_method", "policy_version", "customer_message", "context", "proposal",
    "review_status", "reviewer_id", "reviewed_at", "training_eligible"})
DECISION_FIELDS = frozenset({"intent", "action", "policy_ids", "response"})
REVIEW_FIELDS = frozenset({"id", "case_id", "proposal_sha256", "decision",
                          "reviewer_id", "reviewed_at", "correction"})


class ValidationError(ValueError):
    """A record cannot be used safely under the declared schema."""


def require(condition, message):
    if not condition:
        raise ValidationError(message)


def text(value, label):
    require(isinstance(value, str) and bool(value.strip()), f"{label}: expected nonempty text")


def fields(value, expected, label):
    require(isinstance(value, dict), f"{label}: expected an object")
    require(set(value) == expected, f"{label}: missing or unexpected fields")


def json_value(value):
    if isinstance(value, dict):
        require(all(isinstance(k, str) for k in value), "context: keys must be text")
        for item in value.values():
            json_value(item)
    elif isinstance(value, list):
        for item in value:
            json_value(item)
    else:
        require(value is None or type(value) in (str, bool, int, float),
                "context: expected JSON values")
        if type(value) is float:
            require(math.isfinite(value), "context: non-finite number")


def validate_decision(value):
    fields(value, DECISION_FIELDS, "proposal/correction")
    for name in ("intent", "action", "response"):
        text(value[name], name)
    require(value["intent"] in INTENTS, "unknown intent")
    require(value["action"] in ACTIONS, "unknown action")
    refs = value["policy_ids"]
    require(isinstance(refs, list) and bool(refs), "policy_ids: expected nonempty list")
    for ref in refs:
        text(ref, "policy ID")
        require(ref in POLICIES, "unknown policy ID")
    require(len(refs) == len(set(refs)), "duplicate policy ID")


def validate_case(case):
    fields(case, CASE_FIELDS, "case")
    for name in ("id", "scenario_family", "split", "source_type", "author_method",
                 "policy_version", "customer_message"):
        text(case[name], name)
    require(case["split"] == "development", "only development proposals are supported")
    require(case["source_type"] == "synthetic_authored", "unsupported source type")
    require(case["policy_version"] == "demo-bank/v0.1", "unknown policy version")
    require(isinstance(case["context"], dict), "context: expected object")
    json_value(case["context"])
    validate_decision(case["proposal"])
    require(case["review_status"] == "unreviewed", "store review status in separate events")
    require(case["reviewer_id"] is None and case["reviewed_at"] is None,
            "store reviewer details in separate events")
    require(case["training_eligible"] is False, "proposal cannot grant training eligibility")


def proposal_hash(case):
    """Bind a review to all source fields, not just a reusable case ID."""
    validate_case(case)
    payload = json.dumps(case, sort_keys=True, separators=(",", ":"),
                         ensure_ascii=True, allow_nan=False)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def review_time(value):
    text(value, "reviewed_at")
    try:
        result = datetime.fromisoformat(value)
    except ValueError as exc:
        raise ValidationError("reviewed_at: invalid ISO timestamp") from exc
    require(result.tzinfo is not None and result.utcoffset() is not None,
            "reviewed_at: time zone required")
    return result


def validate_records(cases, reviews=()):
    """Return independent derived records; do not mutate either input.

    A review must carry id, case_id, proposal_sha256, decision, reviewer_id,
    reviewed_at and correction. Correction is a full decision for edit and null
    for other events. These checks do not authenticate claimed human reviews.
    """
    sources, results, times, event_ids = {}, {}, {}, set()
    for case in cases:
        validate_case(case)
        key = case["id"]
        require(key not in sources, "duplicate case ID")
        sources[key] = case
        results[key] = {"case_id": key, "proposal_sha256": proposal_hash(case),
                       "review_status": "unreviewed", "training_eligible": False,
                       "review": None, "effective_proposal": deepcopy(case["proposal"])}
    for event in reviews:
        fields(event, REVIEW_FIELDS, "review")
        for name in REVIEW_FIELDS - {"correction"}:
            text(event[name], name)
        require(event["id"] not in event_ids, "duplicate review ID")
        event_ids.add(event["id"])
        key = event["case_id"]
        require(key in sources, "review refers to unknown case")
        require(event["proposal_sha256"] == results[key]["proposal_sha256"],
                "review source hash does not match")
        decision = event["decision"]
        require(decision in {"accept", "edit", "reject", "defer"}, "unknown review decision")
        stamp = review_time(event["reviewed_at"])
        require(key not in times or stamp > times[key], "review times must increase per case")
        times[key] = stamp
        if decision == "edit":
            validate_decision(event["correction"])
        else:
            require(event["correction"] is None, "only edit can carry a correction")
        result = results[key]
        result["review_status"] = decision
        result["training_eligible"] = decision in {"accept", "edit"}
        result["review"] = deepcopy(event)
        result["effective_proposal"] = deepcopy(
            event["correction"] if decision == "edit" else sources[key]["proposal"])
    return list(results.values())


def unique_object(pairs):
    obj = {}
    for key, value in pairs:
        require(key not in obj, "duplicate JSON field")
        obj[key] = value
    return obj


def reject_constant(value):
    raise ValidationError(f"invalid JSON constant: {value}")


def load_jsonl(path):
    """Read strict JSONL without changing the source file."""
    records = []
    with Path(path).open(encoding="utf-8") as stream:
        for number, line in enumerate(stream, 1):
            try:
                records.append(json.loads(line, object_pairs_hook=unique_object,
                                          parse_constant=reject_constant))
            except ValueError as exc:
                raise ValidationError(f"line {number}: invalid JSON record: {exc}") from exc
    require(bool(records), "empty record file")
    return records


def main():
    parser = argparse.ArgumentParser(description="Check development proposals and review events.")
    parser.add_argument("cases", type=Path)
    parser.add_argument("--reviews", type=Path)
    args = parser.parse_args()
    try:
        results = validate_records(load_jsonl(args.cases),
                                   load_jsonl(args.reviews) if args.reviews else ())
    except (OSError, ValueError) as exc:
        parser.exit(1, f"Validation failed: {exc}\n")
    print(json.dumps({"valid_records": len(results),
                      "training_eligible": sum(r["training_eligible"] for r in results)}))


if __name__ == "__main__":
    main()
