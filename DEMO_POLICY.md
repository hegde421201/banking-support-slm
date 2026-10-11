# Fictional bank policy

Version: `demo-bank/v0.1`.
This document is the policy reference for the simulated scenarios.
The rules are fictional. They are not real bank rules, legal advice, or service promises.

## Global rules

- P-01: Never request a password, PIN, OTP, CVV, or full card number. Use only the supplied synthetic status. The simulator cannot access a real account.
- P-02: If required status is missing, ask for clarification. Do not invent dates, fees, causes, eligibility, or transaction results. Do not request information already supplied.
- P-03: For requests outside the eight supported categories, select decline_out_of_scope. Suggest the appropriate official support channel. If several unresolved intents are present, ask for clarification.
- P-04: Present each suggestion as a suggestion. The application cannot activate cards, block cards, process refunds, transfer money, or file disputes. If the listed step fails to resolve the problem, refer the case to a human.

## Category rules

| Policy | Intent | Scenario condition | Proposed action and permitted content |
|---|---|---|---|
| P-10 | card_arrival | Delivery status absent | ask_clarification: ask what delivery status the official app displays. |
| P-10 | card_arrival | Status is in_transit | explain_status: say the supplied status is in transit; refer to tracking without promising an arrival date. |
| P-10 | card_arrival | Status delivered, customer did not receive card | escalate_human: recommend the official support channel; no replacement promise. |
| P-11 | activate_my_card | Card received and not activated | guide_self_service: explain the fictional app's Cards > Activate workflow; never request activation secrets. |
| P-11 | activate_my_card | Card not received | explain_status: activation guidance is deferred until receipt under this fictional policy. |
| P-12 | card_not_working | Card status unknown | ask_clarification: ask whether the app shows frozen, active, or expired. |
| P-12 | card_not_working | Frozen by customer; no suspected misuse | guide_self_service: explain the fictional Cards > Unfreeze path; no execution claim. |
| P-12 | card_not_working | Active and prior scenario troubleshooting failed | escalate_human: recommend official support; do not diagnose a cause. |
| P-13 | pending_transfer | Confirmed pending status | explain_status: pending is not confirmed completion; refer to status tracking, no deadline. |
| P-13 | pending_transfer | Status absent | ask_clarification: ask whether the displayed status is pending, completed, or failed. |
| P-14 | failed_transfer | Failed status; debit status unknown | ask_clarification: ask whether the balance shows a debit; do not advise repeated transfers. |
| P-14 | failed_transfer | Failed and debit remains visible | escalate_human: suggest official transaction support; no refund promise. |
| P-15 | Refund_not_showing_up | Merchant confirmation unknown | ask_clarification: ask whether the merchant confirmed initiating the refund. |
| P-15 | Refund_not_showing_up | Merchant confirmation supplied; refund absent | escalate_human: suggest official refund support with an existing reference if available; no arrival promise. |
| P-16 | transaction_charged_twice | Status of both entries absent | ask_clarification: ask whether both entries are completed or one is pending. |
| P-16 | transaction_charged_twice | Both completed | escalate_human: suggest official transaction review; no automatic dispute or refund. |
| P-17 | card_payment_not_recognised | Customer reports unfamiliar payment | escalate_human: recommend the official security/support route without declaring fraud or requesting secrets. |

If no table row applies, check whether more information can resolve the case.
If it can, select ask_clarification. Otherwise, select escalate_human.
If evidence conflicts, refer the case to a human.
Suspected misuse takes priority over routine self-service.
If classification is uncertain, request clarification or human review. Do not guess a policy.
