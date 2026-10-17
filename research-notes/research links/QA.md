Form: [Specialized SLM Research and Development Program](https://tally.so/r/Y5ELX5).

## 9. Give your proposed project a name

**Banking Support SLM: Policy-Guided Reply Assistance for Customer-Support Staff**

## 10. Problem and Target Users: What specific problem are you solving, who experiences it, and how frequently?

The banking customer-support staff must interpret a banking request, analyse it using the 
available context and reply according to the correct policy.
The SLM must help to prepare consistent replies without inventing facts or imposing deadlines.

The proposed primary users of this SLM product will be customer-support staff at Indian retail banks and fintech payment companies. The supervisors and quality reviewers are secondary users.
We intend to study common payment-support problems, such as pending or failed transfers, delayed refunds, and duplicate charges. The workflows, policies and escalation routes will remain organisation-specific.

The initial prototype supports English written requests. The proposed research problem covers eight request types involving cards, transfers, refunds, duplicate charges, and unrecognised card payments. Some card-specific types may not apply to every fintech payment company. The prototype uses simulated account context and fictional policies. A staff member reviews each draft before any potential customer use. UPI-specific scenarios would require additional data and a defined scope change.

The current workflow to examine is message review, request classification, policy checking, action selection, and reply preparation. Our working hypothesis is that repeated policy checks and draft corrections add effort. Incorrect replies could also cause confusion or unnecessary follow-up contacts. These costs and consequences will be measured in the target workflow as a part of the research outcome.

Published evidence shows a substantial complaint workload. The RBI reports 2.96 lakh complaints received by its Ombudsman offices during 2024-25. Most concerned loans or advances and digital banking products. This is an annual count of escalated complaints across regulated entities. It does not measure daily frontline contacts, the frequency of our eight request types, or the number of potential buyers. [RBI Annual Report 2024-25, paragraph VI.98](https://www.rbi.org.in/scripts/AnnualReportPublications.aspx?Id=1436).

We have not conducted user interviews or tested competing tools. Interviews or workflow observations are needed to establish frequency, time per request, correction rates, and difficult decisions in both target segments. No organization-specific contact rate or cost estimate is claimed in this proposal.

## 11. Market Research and Competition: What evidence validates this problem, and what competing solutions have you researched? Include links.

Our research currently consists of published reports, public documentation, and an initial review of competing solutions. We intend to use public datasets and create additional human-reviewed examples for our experiments. We have not conducted user interviews or independently tested competing products.

We want to investigate banking customer-support problems in Indian retail banks and fintech payment companies. We are not claiming that our proposed system will outperform existing solutions. This is something we intend to evaluate through experiments.

**Evidence of the problem**

- The RBI records 2.96 lakh Ombudsman-office complaints in 2024–25. It also describes phased AI integration into complaint management. This supports the relevance of complaint handling, but does not establish demand for our specific prototype. [RBI Annual Report 2024–25, paragraphs VI.93 and VI.98](https://www.rbi.org.in/scripts/AnnualReportPublications.aspx?Id=1436).

- McKinsey describes a credit union transformation that achieved a 15% reduction in average handling time within 100 days and a 10% cost reduction within six months. The programme combined workflow changes and several AI use cases. These are published case-study results, not SLM-only effects or performance targets for our project. [McKinsey case study](https://www.mckinsey.com/industries/financial-services/our-insights/the-ai-powered-bank-rewiring-for-excellence-in-customer-care).

- The CFPB provides public consumer complaint data that may help us identify relevant support scenarios. It also warns that these complaints do not represent all consumer experiences. Complaint narratives cannot be treated as verified policy decisions or approved response labels. [CFPB Consumer Complaint Database](https://www.consumerfinance.gov/data-research/consumer-complaints/).

**Competing solutions and alternatives**

| Alternative | Relevant capability | Limitation or question for our research |
|---|---|---|
| Manual policy checking and fixed reply templates | Support staff apply explicit policies and use approved wording when responding to customer requests. | Templates provide predictable responses but may be less adaptable to different customer situations. We need to establish whether an SLM provides enough additional value to justify its errors and resource requirements. |
| [interface.ai](https://interface.ai/solutions/employee-ai/) | We reviewed the vendor's website. It describes AI assistance for banking employees, including access to institutional knowledge and support for customer-service workflows. | Its scope includes broader banking workflows and system integrations. We have not used the product, obtained pricing, or independently verified its performance for our proposed use cases. |
| TF-IDF + Logistic Regression, deterministic policy rules, and approved reply templates | A traditional ML approach can classify customer requests into predefined banking intents. Deterministic rules can then select an action and an approved response template. | Intent classification does not generate a contextual reply. We need to measure classification accuracy, policy correctness, and whether the complete baseline is sufficient without an SLM. |

**Proposed research contribution**

Our proposed contribution is a reproducible comparison on a narrow, reviewed banking-support task. We are not claiming that banking AI assistants do not already exist.

We intend to start with a traditional ML baseline using TF-IDF and Logistic Regression for intent classification, followed by deterministic policy rules and approved reply templates.

In the next stage, we plan to experiment with a Qwen base model and fine-tune it using LoRA on Tinker, following our training roadmap. We will compare the fine-tuned model against the prompted base model and a frontier model on the same held-out evaluation dataset.

Where applicable, we will compare template-based and SLM-generated replies using the same case context, selected action, and policy. This will help us examine reply quality separately from action-selection accuracy.

We still need to conduct user interviews, test the alternatives, and measure performance and resource costs before drawing conclusions. The international case studies and vendor examples do not establish demand or product suitability in India.

## 12. Why is this problem worth solving now?

The customer-support problem is not new. The timely research opportunity is to test compact language models against a strong, conventional baseline using clear policy conditions.

Compared with 2023-24, we now have additional compact-model options for this experiment. The SmolLM2 documentation provides a 360-million-parameter instruction model and CPU usage examples. Its model card also states limitations. This makes a local experiment possible without assuming that a large hosted model is required. It does not guarantee acceptable accuracy, speed, or cost. [SmolLM2 model card](https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct).

Recent operational evidence also makes the question relevant. The RBI's 2024-25 report describes planned AI integration into complaint management. McKinsey's April 2026 banking article emphasizes workflow redesign and reports results from a wider customer-care transformation. These sources support studying where assistance fits into real work. They do not prove that an SLM is the best solution. [RBI, paragraph VI.93](https://www.rbi.org.in/scripts/AnnualReportPublications.aspx?Id=1436), [McKinsey](https://www.mckinsey.com/industries/financial-services/our-insights/the-ai-powered-bank-rewiring-for-excellence-in-customer-care).

Public resources make a reproducible initial study practical. BANKING77 supplies customer questions and intent labels. It is an existing resource, not a newly available dataset. We must create and review the context, policy actions, and reply references separately. [BANKING77 source](https://github.com/PolyAI-LDN/task-specific-datasets).

Our reason to act now is therefore to measure the trade-off rather than assume a benefit. If the SLM does not improve reply usefulness enough to justify its errors and resource requirements, retaining templates is a valid result. We do not currently claim a measured change in customer behavior or new access to private banking data.

## Details to confirm before submission

These notes are for preparation. They are not part of the form answers.

- Select the first shared payment-support workflow to test across Indian retail banks and fintech payment companies.
- Arrange user interviews in both target segments.
- Record future interviews and product trials separately from desk research.
- Confirm which commercial model and competing products the team can actually test.
- Measure local request frequency and costs before adding numerical business claims.
- Keep customer-support staff distinct from AI agents in all later answers.

## Research and drafting record

- The project lead supplied the initial research links in Untitled-1.md.
- Codex checked additional public product documentation for this draft.
- Product descriptions are vendor statements, not independent benchmark results.
- The original research notes remain unchanged.
- The team consists of the project lead and three collaborators.
- The project lead confirmed Indian retail banks and fintech payment companies as the intended target segments.
- The project lead confirmed that no user interviews or personal tool tests have been conducted.
- Source review and drafting assistance do not establish completed user interviews or model experiments.
