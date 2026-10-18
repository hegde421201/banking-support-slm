Form: [Specialized SLM Research and Development Program](https://tally.so/r/Y5ELX5).

## 9. Give your proposed project a name

**Banking Support SLM: Policy-Guided Reply Assistance for Customer-Support Staff**

## 10. Problem and Target Users: What specific problem are you solving, who experiences it, and how frequently?

Banking customer-support staff must read customer requests, check the available information, and follow the correct bank policy. They must then prepare a reply. This work can require several checks.

We want to build a Small Language Model (SLM) that helps the banking support staff prepare clear and consistent replies. The SLM must not invent facts or promise a date that the bank has not confirmed.

Our primary users will be customer-support staff at Indian retail banks and fintech payment companies. Supervisors and quality reviewers will be secondary users.

We plan to study common support problems. These include pending or failed transfers, delayed refunds, duplicate charges, and card-related problems. Each bank or fintech company can have different policies, work steps, and rules for sending a case to another team.

Our first prototype will support written requests in English. We will study eight types of banking requests. These cover cards, transfers, refunds, duplicate charges, and card payments that customers do not recognise.

Some card-related request types may not apply to every fintech company. We will use test account information and fictional bank policies. A support staff member must review each draft reply before it can be sent to a customer. UPI-specific requests are not part of the first prototype. We will need more data and a new project scope before we can add them.

We want to study five steps in the support process. These are reading the customer message, classifying the request, checking the policy, selecting the next action, and preparing the reply.

We think that repeated policy checks and changes to draft replies can increase the work for support staff. An incorrect reply can also confuse a customer or cause another support request. We have not measured these effects yet.

The RBI Annual Report 2024–25 states that its Ombudsman offices received 2.96 lakh complaints during the year. Most complaints concerned loans or advances and digital banking products.

These figures show the number of complaints received by the Ombudsman offices. They do not show the number of daily customer-support requests. They also do not tell us how often our eight request types occur or how many banks would buy our product.

Source: RBI Annual Report 2024–25, paragraph VI.98
https://www.rbi.org.in/scripts/AnnualReportPublications.aspx?Id=1436

We have not interviewed banking support staff or tested competing products. We need interviews or direct study of support work to measure how often these problems occur, how much time each request takes, and how often staff must correct a reply.

We do not yet have measured support costs or request volumes from any bank or fintech company.

## 11. Market Research and Competition: What evidence validates this problem, and what competing solutions have you researched? Include links.
Our research is based on published reports, public documents, and an initial review of competing solutions. We have also reviewed the interface.ai website.

We plan to use public datasets and create additional examples that people will review before training. We have not interviewed users or tested competing products ourselves.

We want to study banking customer-support problems in Indian retail banks,corporate banks and fintech payment companies. We do not claim that our proposed SLM will perform better than existing products. We will test this during our research.

Our four-person research team includes a BFSI domain programmer (Sarfaraj Ejaj).
This collaborator has reported that some customer queries can take four to five days to complete. We have not yet measured the average handling or resolution time.
The collaborator will help us study banking workflows and review fictional support scenarios. We will use this input to identify which tasks may benefit from automated action selection and draft reply preparation.

Evidence of the problem:

1. RBI Annual Report 2024–25

The RBI reports that its Ombudsman offices received 2.96 lakh complaints in 2024–25. The report also describes plans to add AI features to complaint management in stages.

This shows that complaint handling is an important area of work. It does not prove that banks need our specific product.

Source: RBI Annual Report 2024–25, paragraphs VI.93 and VI.98
https://www.rbi.org.in/scripts/AnnualReportPublications.aspx?Id=1436

2. McKinsey banking customer-care case study

McKinsey describes a credit union project that reduced average handling time by 15% within 100 days. It also reports a 10% cost reduction within six months.

The project included changes to work processes and several AI applications. We cannot say that an SLM alone caused these results. We also cannot use these figures as expected results for our project.

Source: McKinsey case study
https://www.mckinsey.com/industries/financial-services/our-insights/the-ai-powered-bank-rewiring-for-excellence-in-customer-care

3. CFPB Consumer Complaint Database

The CFPB provides public consumer complaint data. We can use this information to find examples of banking problems that may be useful for our research.

The CFPB warns that its complaint data does not represent all consumer experiences. We also cannot treat complaint descriptions as correct policy decisions or approved customer replies.

Source: CFPB Consumer Complaint Database
https://www.consumerfinance.gov/data-research/consumer-complaints/

Competing solutions and alternatives:

1. Manual policy checks and fixed reply templates

Support staff can check bank policies and select approved replies from a set of templates.

This method gives predictable replies. However, fixed templates may not fit every customer situation.

We need to test whether an SLM can prepare more useful replies without adding too many errors or too much cost.

2. interface.ai

We reviewed the interface.ai website. The company describes AI tools that help banking employees find information and handle customer-support work.

Its products cover more work processes and system connections than our first prototype.

We have not used the product, obtained its pricing, or measured its performance. We cannot compare its results with our proposed system yet.

Source: interface.ai Employee AI
https://interface.ai/solutions/employee-ai/

3. TF-IDF, Logistic Regression, policy rules, and reply templates

We plan to build a traditional Machine Learning (ML) baseline.

TF-IDF will convert customer messages into numerical features. Logistic Regression will use these features to classify requests into known banking categories.

A separate set of policy rules will select the next action. Approved templates will provide the reply.

This method is simple and uses fewer computing resources than a language model. However, intent classification alone cannot prepare a reply that uses all the details of a customer case.

We will measure its classification accuracy, policy correctness, and reply quality before we compare it with an SLM.

Our proposed research:

We want to make a repeatable comparison between a traditional ML system and a specialized SLM on a small set of banking-support tasks.

We will first build the traditional ML baseline.

Next, we plan to test a Qwen base model. We will then fine-tune Qwen with LoRA on Tinker. We will compare the fine-tuned model with the base model and a frontier model, such as GPT or Claude.

We will use the same test cases and scoring rules for each model where the tasks are the same.

We will measure whether the models select the correct action and prepare useful replies that follow the supplied policy. We will also record errors and computing costs.

For reply-quality tests, we will keep the selected action and policy the same when we compare templates with SLM-generated replies. We will measure action-selection accuracy separately.

We do not claim that banking AI assistants are new. Our goal is to test whether a smaller model can perform this specific task well enough to be useful.

We still need to test the alternatives, and measure costs and performance.

The published international case studies and vendor examples do not prove that Indian banks or fintech companies need our proposed product.

## 12. Why is this problem worth solving now?


We believe this is a good time to study the use of Small Language Models (SLMs) in banking customer support.

Two or three years ago, it was more difficult for a small team to train and test language models. Today, smaller pretrained models such as Qwen are available. Tools such as LoRA also make model training less costly. LoRA lets us train a small set of new weights without changing all the weights of the original model.

Traditional Machine Learning (ML) methods, such as TF-IDF with Logistic Regression, can classify banking requests into known categories. These methods are fast and need fewer computing resources. However, they cannot write customer replies by themselves. We must add policy rules and reply templates to complete the task.

An SLM can take a customer message, the available account details, and a banking policy as input. It can then suggest the next action and write a draft reply. This may help support staff handle requests that need different replies based on the case details.

We do not yet know whether an SLM will perform better than the traditional ML system. An SLM can also make mistakes, select the wrong action, or write information that the policy does not support.

There is also growing interest in the use of AI for banking support. The RBI Annual Report 2024–25 describes plans to add AI features to its complaint management system. This shows that AI-assisted complaint handling is being explored, but it does not prove that banks need our proposed product.

RBI Annual Report 2024–25:
https://www.rbi.org.in/scripts/AnnualReportPublications.aspx?Id=1436

Qwen3 model announcement:
https://qwen.ai/blog?id=qwen3

LoRA reference:
https://huggingface.co/docs/transformers/peft

Our first step is to build a baseline using TF-IDF, Logistic Regression, policy rules, and reply templates. We will then test a Qwen model and fine-tune it with LoRA on Tinker.

We want to find out whether the SLM can select the correct action and prepare better replies without adding too many errors or too much cost.

We have not yet tested these models. These activities are part of our research plan.


## 13. What value would solving this problem create, and what specific use case will you tackle first?


We want to help banking customer-support staff prepare correct and consistent replies with less manual work.

The primary beneficiaries will be customer-support staff at Indian retail banks and fintech payment companies. Supervisors and quality reviewers may also benefit because they need to check whether replies follow the correct policy.

Potential buyers could be banks, fintech payment companies, or teams that manage customer-support operations. We have not spoken to these buyers or confirmed their interest.

Business value:

We expect that an SLM could reduce the time needed to check policies and prepare draft replies. It could also reduce the number of replies that staff must correct.

A correct reply may help customers understand the next step in their support request. It may also reduce the need for another customer contact.

These are possible benefits. We have not measured them yet.

Initial use case:

We propose to start with delayed refund requests.

A customer sends a written message because an expected refund has not arrived.

The system receives the customer message, simulated account information, and a fictional bank policy.

It must select one of the permitted support actions and prepare a draft reply that follows the policy.

For example, if the refund status is not available, the system must not invent a refund date. It must select the correct next action based on the supplied policy.

A human support staff member will review the draft before any customer use.

We will start with English written requests. We will not connect the prototype to real bank accounts or payment systems.

How we will measure value:

We will compare our traditional ML and template-based system with the SLM on the same test cases.

We will measure the time needed to prepare and review each reply. We will also measure how often a draft needs correction.

We will check whether the system selects the correct action and follows the supplied policy. We will record incorrect replies, unsupported statements, and cases that need human review.

We will measure computing costs and response time.

We will use these results to estimate whether the SLM could save staff time or reduce support costs. We will not claim actual business savings until we have measured results from a real support workflow.

Our first goal is to show that the system can handle one type of request correctly and consistently. We will consider more request types only after we evaluate the initial results.

## 14. Why do you believe a specialized SLM is the right solution?

We believe a specialized Small Language Model (SLM) is worth testing for banking customer support. We do not yet know whether it is the best solution.

Our task is to read a customer message, use the available case details, follow a supplied bank policy, select the next action, and prepare a draft reply.

We will compare several approaches before we decide whether a specialized SLM is necessary.

Conventional software:

We will first build a system that uses TF-IDF and Logistic Regression to classify customer requests. A separate set of rules will select the next action. Approved templates will prepare the reply.

This system should be fast and need few computing resources. It can also give predictable results when the rules are clear.

However, it may need many rules and templates to handle different customer situations. We will test whether this is a real limitation.

General-purpose Large Language Models (LLMs):

A general-purpose LLM can read a customer message and prepare a reply. It may not need additional training.

However, we must test whether it follows our supplied policies and selects the correct action. We must also measure its response time and cost.

Prompting:

We can give a pretrained model clear instructions, examples, and policy information in its prompt.

This may be sufficient for our task. We will test prompting before we fine-tune a model.

Retrieval-Augmented Generation (RAG):

RAG can find relevant policy information and give it to a language model.

This can help when policies are stored in many documents or change frequently.

Our first prototype will use a small set of fictional policies. We will supply the relevant policy as part of the input. We do not plan to build a RAG system in the first experiment.

Existing model workflows:

We will also test a Qwen base model without fine-tuning. This will help us measure whether additional training improves its results.

Specialized SLM:

We plan to fine-tune a small Qwen model with LoRA on Tinker. We want to test whether the model can learn to select permitted actions and prepare replies that follow our fictional bank policies.

A smaller model may need fewer computing resources than a larger model. It may also have lower operating costs. We must measure these differences before making a claim.

A small model does not automatically protect private information. Our first prototype will use simulated account data and fictional policies. We will not use real customer records.

We will test the model's ability to return a fixed output format. The output will contain the selected action and a draft reply. We will also check whether the output follows the supplied policy.

We do not yet have a target bank environment or confirmed deployment requirements. We will measure response time, computing needs, errors, and model size during our experiments.

Fine-tuning is not our starting assumption. If prompting with a base model, or using rules and templates, gives sufficient results at lower cost, we will prefer that approach.

Our goal is to find the simplest system that can perform the task correctly and consistently.

## Q15. SLM Proposal and Research Hypothesis: What will you build, and what measurable hypothesis do you intend to test?

We propose to build a Banking Support SLM that helps customer-support staff select the next action and prepare a draft reply.

The system will support written requests in English. It will use simulated account information and fictional bank policies.

Our first use case will be delayed refund requests. We will test this use case before we expand to the other banking request types in our research scope.

System inputs:

The system will receive a customer message, the available case details, and the applicable bank policy.

The case details may include the refund status and other information needed to select the next action.

System outputs:

The system will return a selected action from a fixed set of permitted actions and a draft customer reply.

The reply must follow the supplied policy. It must not invent transaction facts or promise a refund date that has not been confirmed.

A human support staff member must review the draft before it can be sent to a customer.

Operating environment:

We will develop and test the system in a research environment. We will not connect it to real bank accounts, payment systems, or customer databases.

We will use a traditional ML baseline with TF-IDF, Logistic Regression, policy rules, and approved reply templates.

We will also test a Qwen base model with prompting and a general-purpose frontier model.

We plan to fine-tune Qwen with LoRA on Tinker. We will use reviewed training examples. We will keep the test examples separate from the training data.

Research hypothesis:

We hypothesize that the fine-tuned Qwen model will improve correct action selection by at least 5 percentage points compared with the strongest relevant baseline on unseen test cases.

We also expect the fine-tuned model to prepare replies that follow the supplied policy and contain fewer unsupported statements.

We will measure action accuracy, policy compliance, reply quality, response time, and computing cost.

We will use the same test cases and scoring rules for the models that perform the same task.

A result that would disprove our hypothesis:

Our hypothesis will not be supported if the fine-tuned Qwen model fails to improve action accuracy by at least 5 percentage points over the strongest baseline.

We will also reject the model as a useful choice if it improves action accuracy but produces more policy violations or unsupported statements.

If a prompted model or the traditional ML system gives similar results with lower cost, we will not claim that fine-tuning is necessary.

The goal is to measure whether specialization provides enough value to justify the additional training and operating costs.

## 16. What is your proposed model-development strategy?

We plan to develop the Banking Support SLM in stages. We will start with a simple baseline before we fine-tune a language model.

Our first use case will be delayed refund requests. We will use written English messages, simulated account information, and fictional bank policies.

Data preparation:

We will use public banking datasets, including BANKING77, for our initial intent-classification work.

BANKING77 is a dataset, not a language model or a banking application.
It does not provide account status, bank policies, approved replies, or context-dependent next actions.

Source: https://github.com/PolyAI-LDN/task-specific-datasets

We will also create a separate dataset for policy-guided action selection and reply preparation. Each example will contain a customer message, case details, the applicable policy, the correct next action, and a draft reply.

We will use synthetic data to create different customer situations. These examples will not contain real customer information.

Our team will review the examples before training. We will write review rules so that different reviewers can apply the same standards.

We will check for missing information, incorrect labels, and cases that have the same input but different expected actions.

We will divide the reviewed data into training, validation, and test sets. We will keep the test set separate until the final evaluation.

Baseline:

We will first build a traditional Machine Learning (ML) baseline using TF-IDF and Logistic Regression for intent classification.

We will use deterministic policy rules to select the next action. Approved templates will prepare the reply.

We will also test a Qwen base model with prompting and a general-purpose frontier model. These models will help us measure whether fine-tuning provides additional value.

Supervised fine-tuning:

We plan to fine-tune a small Qwen model using Low-Rank Adaptation (LoRA) on Tinker.

LoRA lets us train a small set of additional weights instead of changing all the weights of the base model.

We will train the model with reviewed examples of customer messages, case details, policies, correct actions, and draft replies.

We selected supervised fine-tuning because our task has defined inputs and expected outputs.

Synthetic data:

We will use synthetic examples to cover different refund situations, missing information, and cases that need human review.

We will check these examples against the fictional policies before we use them for training.

Synthetic data will help us test more situations. However, it will not prove that the model works correctly with real banking customers.

Preference optimization:

We do not plan to use preference optimization in the first experiment.

This method needs reliable information about which of two model replies is better. We do not yet have a reviewed dataset of such comparisons.

We will consider it only if our first results show that supervised fine-tuning is not sufficient and we can prepare reliable comparison data.

Knowledge distillation:

We do not plan to use knowledge distillation in the first experiment.

Distillation can train a smaller model using outputs from a larger model. However, we must first establish whether our selected Qwen model can perform the task well.

We will consider distillation later if a larger model performs better and we need a smaller model for deployment.

Evaluation:

We will use the same held-out test cases and scoring rules for models that perform the same task.

We will measure correct action selection, policy compliance, reply quality, and unsupported statements.

We will also measure response time and computing costs.

We will compare the fine-tuned Qwen model with the strongest relevant baseline. We will use the research hypothesis and success criteria defined in Q15.

We will record failed cases and study why the model made incorrect decisions.

Deployment:

Our first system will be a research prototype. It will not connect to real bank accounts or payment systems.

A human support staff member must review each draft reply before any customer use.

We will not deploy the model in a real banking environment during the first experiment.

If the results support further development, we will study deployment cost, data protection, system integration, and operational controls.

Our goal is to find out whether supervised fine-tuning improves this specific banking-support task. If the simpler baseline performs equally well at lower cost, we will not claim that fine-tuning is necessary.

## 17. Compute and Data Requirements

Our proposed base model is Qwen3.5-4B, which has approximately four billion parameters.

We selected this model because it is listed among the models supported for training on Tinker.
We want to test policy-guided action selection and reply preparation for delayed refund requests. We do not plan to train a language model from the beginning.

We plan to use LoRA for supervised fine-tuning. We will first test the pretrained model with prompting. We will then compare it with the fine-tuned model.

We will confirm account access, training quotas, costs, and the model license before we start.

If the model is not available to our account, we will select another supported Qwen model and document the reason for the change.

Compute requirements:

We plan to use Tinker for supervised fine-tuning with LoRA.

LoRA trains a small set of additional weights. It usually needs fewer training resources than updating all model weights.

We expect to use GPU resources provided through Tinker for training. We do not plan to purchase a dedicated training GPU for the first experiment.

We will confirm Tinker model support, GPU availability, access limits, and training costs before we begin.

For inference, we will first use a hosted environment that supports the selected model. We will measure response time, memory use, and cost.

We have not yet measured the hardware requirements of the selected model.

Existing resources:

Our team has four members. We have a GitLab repository for source code, research notes, and experiment records.

We plan to use Python for data preparation, baseline development, training experiments, and evaluation.

We have access to personal development computers. We will not assume that these computers are sufficient for model fine-tuning.

Training and evaluation data:

We plan to use BANKING77, a public banking intent-classification dataset published by PolyAI.

The dataset contains 13,083 customer queries across 77 intent categories. It has 10,003 training examples and 3,080 test examples.

Our initial project uses eight selected banking request types. We have prepared a smaller subset for our first intent-classification experiments.

BANKING77 contains customer messages and intent labels. It does not contain bank policies, account status, correct support actions, or approved replies.

We will create a separate dataset with at least 100 human-reviewed examples for supervised fine-tuning.

We will use fictional policies and simulated account information. We will not use confidential customer records.

The PolyAI repository identifies the dataset license as CC BY 4.0. We will retain the required attribution and cite the original research paper.

We will use JSON or JSONL files for the structured examples. We will keep the training, validation, and test sets separate.

Dataset source:
https://github.com/PolyAI-LDN/task-specific-datasets

Research paper:
https://arxiv.org/abs/2003.04807


Data access:

We will obtain public datasets from their official distribution sources.

We will check the dataset license and usage conditions before training or publishing derived data.

Our team will create the additional policy examples and review them.

We do not have access to confidential bank records or real customer-support conversations. We do not plan to request these records for the first experiment.

Privacy and confidentiality:

We will use fictional policies and simulated account information.

We will not use real customer names, account numbers, card numbers, phone numbers, or other personally identifiable information (PII).

We will check public and generated examples for personal information before including them in the dataset.

We will not upload confidential banking information to external training or inference services.

We will record dataset sources and licenses. We will not publish data that we do not have permission to share.

Timeline:

We plan to complete the initial research within ten weeks.

During the early weeks, we will prepare the datasets, define the evaluation rules, and build the traditional ML baseline.

We will then test the Qwen base model and fine-tune it with LoRA on Tinker.

The later weeks will focus on evaluation, error analysis, documentation, and improvements. We have reserved time for unexpected technical problems.

Access risks and assumptions:

Our main risks are Tinker access, model support, GPU availability, training cost, and dataset quality.

A small reviewed dataset may not contain enough examples for the model to learn reliable policy decisions.

Synthetic examples may also fail to represent real customer-support work.

We will measure these limitations and report them.

If Tinker does not support our first model choice, we will select another small Qwen model that meets the training requirements.

We will not claim production readiness or business savings from this initial experiment.

## 18. What makes this model difficult to replicate?

- discuss specialised data
- evaluation,domain representations
- workflow integration
- cost performance
- training advantages

Fine tuning is not a defensible advantage.

### Answer

We do not claim that fine-tuning a Qwen model is difficult to replicate. Other teams can use the same pretrained models and training methods.

Our potential advantage will come from the quality of our banking-support data, policy representations, evaluation methods, and workflow design.

Specialized data:

We plan to create a dataset of banking-support cases that contain more information than an intent label.

Each example will include a customer message, simulated account details, a fictional banking policy, the correct permitted action, and a reference reply.

We will include cases with missing information, different refund statuses, and requests that need human review.

Our four-person team includes a programmer with experience in the Banking, Financial Services, and Insurance (BFSI) sector. This experience can help us design realistic technical scenarios.

However, we will still need to confirm that our scenarios represent real banking work.

Evaluation:

We will develop tests that check whether a model follows a supplied policy and selects the correct action.

We will also test whether a reply contains unsupported statements, invents a refund date, or fails to request missing information.

We plan to include difficult cases where a small change in account status or policy changes the correct action.

These tests may become a useful research asset because they measure banking decisions rather than general language quality.

Domain representations:

We will represent each case using a defined set of fields, permitted actions, and policy conditions.

We will keep the policy version with each test case.

This will help us test whether the model uses the supplied facts and follows the correct policy.

Workflow integration:

Our proposed workflow will support message classification, policy checking, action selection, draft reply preparation, and human review.

The first prototype will not connect to real banking systems.

Future integration with authorized bank systems may provide additional value. However, we do not claim that these integrations already exist.

Cost and performance:

We will measure action accuracy, policy compliance, reply quality, response time, and inference cost.

We want to find out whether a small specialized model can meet the task requirements at a lower cost than a larger general-purpose model.

We have not yet demonstrated this advantage.

Training advantages:

We plan to maintain reviewed examples, policy versions, error records, and repeatable evaluation tests.

These resources may help us improve the system when new request types or policies are added.

Our potential advantage is not the LoRA training method. It is the combination of reliable domain data, policy tests, and a repeatable improvement process.

Current limitations:

We do not have exclusive banking data, proprietary model weights, customer contracts, or production integrations.

Our first dataset will be small and will use fictional policies.

We therefore do not claim that the first prototype has a defensible competitive advantage.

Our research goal is to determine whether the domain data, evaluation methods, and workflow design can become useful assets that are difficult to reproduce at the same quality and cost.


SECTION 4: Evaluation and Research Quality

## 19. Evaluation Strategy: Which baselines and metrics will you use to demonstrate that your SLM performs better?

- define primary metrics
- target improvement
- test conditions
- commercial/open-source/non LLm/human baselines
- and fair comparisons using comparable prompts
- test data, settings and costs
- include accuracy, factuality,latency,inference cost,task completion or human ratings as appropriate

### Answer
We will evaluate whether our fine-tuned Banking Support SLM can select the correct support action and prepare a useful reply that follows the supplied banking policy.

Our first evaluation will focus on delayed refund requests.

1. Baselines

We will compare four systems.

Baseline A: Traditional Machine Learning (ML).

This system will use TF-IDF and Logistic Regression for intent classification. Deterministic policy rules will select the next action. Approved templates will prepare the reply.

Baseline B: Prompted Qwen.

We will test the selected Qwen base model without fine-tuning. It will receive the customer message, simulated account details, policy, and output instructions.

Baseline C: General-purpose frontier model.

We will test a capable general-purpose language model using the same case information and task instructions.

Baseline D: Fine-tuned Qwen.

We will fine-tune a small Qwen model with LoRA on Tinker. We will evaluate it on the same held-out cases.

We also plan to ask human reviewers to complete a sample of cases. This will provide a reference for task time, action correctness, and reply quality.

We will not claim to have evaluated a commercial banking product unless we can obtain access and run comparable tests.

2. Primary metric

Our primary metric will be action-selection accuracy.
For each test case, we will compare the selected action with the human-reviewed reference action.
Action-selection accuracy is the number of correct actions divided by the total number of evaluated cases.

Our earlier Q15 hypothesis is that the fine-tuned Qwen model will improve action-selection accuracy by at least five percentage points over the strongest relevant baseline.

We will compare the models using the same held-out test cases.

3. Policy compliance and factuality

We will check whether each selected action and draft reply follow the supplied policy.
We will record policy violations separately from action-selection errors.
We will also count unsupported statements. These include invented transaction facts, incorrect refund status, and refund dates that the input does not confirm.
We will report the number and rate of these errors.
An improvement in action accuracy will not be sufficient if the fine-tuned model produces more policy violations or unsupported statements.

4. Reply quality

Human reviewers will assess draft replies using a defined scoring guide.
They will check whether each reply is correct, clear, complete, and consistent with the supplied policy.
We will record whether the reviewer accepts the reply, edits it, or rejects it.
We will also measure the time needed to review and correct a reply.

5. Latency and inference cost

We will measure response time for each system.
We will record token usage and the cost of model inference where this information is available.
For hosted models, we will use the applicable service prices.
For the traditional ML baseline, we will record the computing resources and processing time.
We will report the test environment and cost assumptions. We will not claim a cost advantage without measurements.

6. Fair test conditions

We will use the same customer messages, simulated account details, fictional policies, and permitted actions for systems that perform the same task.

We will use comparable task instructions and output formats for language models.
We will record the model version, prompt version, generation settings, and test conditions.
We will use a fixed test set that is separate from training and model selection.
We will check for duplicate and closely related examples across the data splits.
We will not compare BANKING77 intent-classification accuracy directly with policy-action accuracy.

7. Test cases

We will create at least 100 human-reviewed examples for the supervised fine-tuning work.
We will divide the examples into training, validation, and test sets.
We will seek additional independent test cases to evaluate the five-percentage-point hypothesis.
Our test cases will include different refund statuses, missing information, policy changes, and cases that need human review.
We will also test cases where a small change in the input changes the correct action.

8. Research decision

We will report the results for every baseline, including cases where the fine-tuned model performs worse.
We will report the number of test cases and the uncertainty in the measured differences.

Our hypothesis will not be supported if fine-tuned Qwen fails to improve action-selection accuracy by at least five percentage points over the strongest baseline.

We will not recommend the fine-tuned model if it causes more policy violations or unsupported statements.

If a prompted model or the traditional ML system performs equally well at lower cost, we will prefer the simpler system.

Our goal is to identify the most suitable approach for the task, not to prove that fine-tuning is always necessary.

## 20. How will you construct a reliable evaluation dataset?

- explain representative examples
- ground truth
- ambiguous cases
- leakage prevention
- training/validation/test splits
- and human or expert annotation

### Answer

We will create a separate evaluation dataset for our Banking Support SLM. The dataset will test whether the system selects the correct support action and prepares a reply that follows the supplied banking policy.

1. Representative examples

Our first use case will be delayed refund requests.
We will create examples with different refund statuses, transaction details, missing information, and policy conditions.
We will include simple cases, difficult cases, and cases that require human review.
We will also include cases where a small change in the refund status or policy changes the correct action.

We will use fictional banking policies and simulated account information.
Our four-person team includes a programmer with experience in the BFSI sector. This collaborator can help us review the technical details of the scenarios.

We will seek additional feedback to check whether the scenarios represent real support work.

2. Ground truth

Each example will contain a customer message, simulated case details, an applicable policy, a correct permitted action, and a reference reply.

We will determine the correct action from the supplied policy and case details.
The reference reply must use only the available information. It must not invent a transaction status, refund date, or other unsupported fact.
We will record the policy version and the reason for the expected action.

3. Ambiguous cases

Some requests may not contain enough information to select an action.

We will mark these cases separately.

The expected action may be to request missing information or send the case for human review, according to the policy.

If the reviewers cannot agree on the correct action, we will examine the policy and the case details.

We will not force an uncertain case into an incorrect label.

4. Human review

Our team will use written annotation rules.
At least two team members will review each evaluation example independently.
They will check the action label, policy compliance, and reference reply.
We will record disagreements and resolve them before finalizing the dataset.

For cases that need banking operations knowledge, we will seek qualified domain review. We will not treat software engineering experience as a substitute for banking policy authority.

5. Data splits and leakage prevention

We will create separate training, validation, and test sets.

Training examples will be used for fine-tuning. Validation examples will be used for model selection and development. Test examples will be reserved for final evaluation.

We will keep related examples together in one split when they share the same underlying scenario.
We will check for duplicate messages, repeated templates, and cases with nearly identical facts across different splits.

We will not use final test cases to select prompts, change training settings, or improve the model.

6. Dataset size and quality

Our initial target is at least 100 human-reviewed examples for the supervised fine-tuning work.
We will seek additional independent evaluation cases because 100 examples may not be sufficient to measure a small difference in accuracy.

We will record the number of examples in each split and report results separately for important case types.
We will use JSONL files with unique case identifiers, policy versions, review status, and expected outputs.
We will check each record for missing fields, conflicting labels, unsupported facts, and personal information.

7. Evaluation reliability

We will use the same held-out cases to compare the traditional ML baseline, prompted Qwen, the frontier model, and fine-tuned Qwen.

We will define the scoring rules before final testing.
We will measure action-selection accuracy, policy compliance, unsupported statements, and human-rated reply quality.
We will report the test-set size and uncertainty in the measured differences.
We will also publish our evaluation rules and permitted synthetic examples where licensing and permissions allow.

Our goal is to create a repeatable evaluation process that can show both the strengths and the failures of the proposed SLM.


## 21. Risks and Failure Criteria: What are your three biggest risks, and what results would make you reconsider the approach?

- For each risk,explain importance,early testing, and fallback.
- State evidence or experiments that would invalidate your hypothesis and cause 
abandonment or substantial change

### Answer

Our Banking Support SLM project has three main risks. We will test these risks early and use the results to decide whether to continue, change, or stop the proposed approach.

1. Risk: The training and evaluation data may not represent real banking work.

Our first dataset will use fictional policies and simulated account information.

These examples can help us test model behaviour. However, they may not represent the problems that banking support staff handle every day.

Our four-person team includes a programmer with BFSI experience. This collaborator can help us review technical scenarios. We will also seek feedback from banking support or operations staff.

Early test:

We will create a small set of delayed refund scenarios before fine-tuning.

We will check whether the policies are clear, whether the expected actions are correct, and whether reviewers agree on the labels.

We will record disagreements and cases that do not have a clear answer.

Fallback:

If the examples are not reliable, we will improve the policy definitions and annotation rules before training.

If we cannot establish reliable ground truth, we will stop the fine-tuning experiment for this use case.

We will not claim that synthetic data proves performance in a real bank.

2. Risk: The fine-tuned SLM may select incorrect actions or generate replies that violate policy.

A model may select an action that is not permitted by the supplied policy.

It may also invent a refund status, promise an unsupported refund date, or fail to request missing information.

These errors are important because banking support staff need correct information before they can advise customers.

Early test:

We will evaluate the prompted Qwen model before fine-tuning.

We will test cases with known refund status, missing information, conflicting details, and different policy conditions.

We will measure action-selection accuracy, policy violations, and unsupported statements.

After fine-tuning, we will repeat the evaluation on held-out cases.

Fallback:

If the SLM makes unacceptable policy errors, we will keep action selection under deterministic policy rules and use the model only for draft reply preparation.

The selected action and policy will remain fixed inputs to the reply generator.

A human support staff member must review each draft before customer use.

If the model continues to produce unsafe or unreliable replies, we will stop using it for reply generation.

3. Risk: Fine-tuning may not provide enough value compared with simpler systems.

Our traditional ML baseline uses TF-IDF, Logistic Regression, deterministic policy rules, and approved reply templates.

We will also test a prompted Qwen model and a general-purpose frontier model.

These alternatives may perform as well as the fine-tuned SLM.

Early test:

We will compare the systems on the same held-out cases.

Our primary metric is action-selection accuracy.

Our Q15 hypothesis requires the fine-tuned Qwen model to improve action-selection accuracy by at least five percentage points over the strongest relevant baseline.

We will also measure policy compliance, reply quality, response time, and inference cost.

Fallback:

If the fine-tuned model does not achieve the five-percentage-point improvement, our primary hypothesis will not be supported.

If it improves accuracy but increases policy violations or unsupported statements, we will not recommend it for the proposed task.

If a simpler system achieves similar quality with lower cost, we will select the simpler approach.

We may then narrow the SLM task to reply preparation or investigate another banking-support use case.

Research failure criteria:

We will substantially change or stop the proposed approach if we cannot establish reliable ground truth, if the model continues to produce unacceptable policy errors, or if fine-tuning provides no useful advantage over the strongest baseline.

We will report negative results as part of our research.

Our goal is not to prove that an SLM is always the correct solution. Our goal is to identify which banking-support tasks benefit from specialization and which tasks are better handled by conventional software.

SECTION 5: Execution Plan and Team Leadership
22. Provide a proposed 8–12 week execution plan

- break into milestones,validation,baselines,dataset,training,evaluation,iteration,final 
deliverable.
- identify owner and expected outcome for each

### Answer
We propose a ten-week research and development plan for our Banking Support SLM.

Our four-person team will work on three technical deliverables from the Antern course brief.

Member 1 (Project Lead): Ganesh Hegde
Member 2: Rishik Kumar Balanagu
Member 3: Shriyansh Sinha
Member 4: Sarfaraj Ejaj

Part A: A research paper comparing Qwen, Llama, and Mistral.
Part B: A visual explanation of Low-Rank Adaptation (LoRA), with a video, source code, and report.
Part C: A Banking Support SLM trained with LoRA on Tinker, with a reviewed dataset and evaluation report.

We will work on these parts in parallel.

Proposed responsibilities:

Member 1, Project Lead: System design, research coordination, baseline development, evaluation, and final integration.

Member 2, Training and Visualization Contributor: Python training support, Tinker experiments, Manim animations, and experiment records.

Member 3, Data and Research Contributor: Dataset preparation, annotation records, architecture research, and documentation.

Member 4: BFSI Programmer: Banking scenario design, fictional policy rules, data review, and domain-related validation.


The team will review these assignments before work begins.

Weeks 1 and 2: Research design and data preparation

We will define the first model behaviour: select a permitted action and prepare a policy-compliant reply for a delayed refund request.

We will confirm the Qwen mode
We will start the Qwen, Llama, and Mistral architecture comparison.
We will prepare the data schema, fictional policies, permitted actions, and review Standard Operating Procedure (SOP).

We will define the evaluation metrics before training.

Owners: Members 1, 2, and 4, with Member 3 checking model access.

Expected outcome: Research scope, initial architecture notes, data schema, review SOP, evaluation plan, and confirmed training requirements.

Weeks 3 and 4: Dataset, baselines, and LoRA explanation

We will create at least 100 human-reviewed examples. We will check label balance, contradictions, and duplicate cases.

We will create separate training, validation, and test sets.
We will build the traditional ML baseline using TF-IDF, Logistic Regression, policy rules, and approved reply templates.
We will evaluate the prompted Qwen base model and one frontier model.

We will record decision accuracy and draft reply quality.

We will also develop the LoRA explanation. The video will show the frozen weights, matrices A and B, rank, alpha, training, and merging.

Owners: Members 1 and 4 for the baseline and policy checks. Member 3 for dataset review and architecture research. Member 2 for LoRA animation.

Expected outcome: Reviewed dataset, baseline results, initial scorecard, and LoRA video draft.

Weeks 5 and 6: Fine-tuning and research deliverables

We will complete the architecture comparison paper.

The paper will compare Qwen, Llama, and Mistral using the same model blocks. It will explain important design decisions, costs, and trade-offs.

We will prepare a 10–15-page LaTeX paper with a comparison table, at least four original figures, and a reading log.

We will complete the 10–20-minute LoRA video and the 4–6-page LaTeX report.

For the SLM, we will record the base model, LoRA rank, alpha, target layers, learning rate, epochs, and estimated training cost.

We will run a dry test before training.

We will then fine-tune the selected Qwen model on Tinker and save the adapter weights.

Owners: Members 1 and 4 for the architecture paper. Member 2 for the LoRA video and training implementation. Member 3 for policy and data checks.

Expected outcome: Architecture paper, LoRA video and report, and at least one completed LoRA training run with recorded settings and losses.

Weeks 7 and 8: Evaluation and error analysis

We will evaluate the fine-tuned Qwen model on the held-out test set.

We will compare it with the prompted Qwen base model and the frontier model using the same scoring method.

We will also compare the traditional ML baseline on the tasks that it supports.

We will measure action-selection accuracy, policy compliance, reply quality, and unsupported statements.

We will report results for each permitted action, not only the total score.

We will examine at least five failed examples and explain the possible causes.

We will record response time and resource costs where measurement is available.

Owners: Member 1 for evaluation. Member 4 for policy review. Member 2 for error analysis and reporting. Member 3 for model runs and experiment logs.

Expected outcome: Comparative scorecard, error analysis, and a decision on whether fine-tuning supports our research hypothesis.

Weeks 9 and 10: Improvements and final submission

We will use the evaluation results to identify data or model problems.

If time and resources permit, we will correct the data and run another controlled experiment.

We will prepare a public GitLab/GitHub repository with a clear README, step-by-step commit history, dataset or permitted sample, review SOP, training configuration, and scorecard.

We will include two Mermaid diagrams. One will show how a data example moves through the project files. The other will show the training process.

We will check that the repository does not contain API keys or confidential data.

We will complete the research report and prepare a demonstration of the delayed refund workflow.

Owners: Member 1 for final integration. Member 4 for domain checks. Member 3 for research documentation. Member 2 for training artifacts and demonstration support.

Expected outcome: Reproducible project repository, final evaluation report, research paper, LoRA explanation materials, and working research demonstration.

Public research communication:

Each member may publish their own learning notes, figures, experiment results, and corrections on LinkedIn or X.

The Antern brief sets a target of 150–200 pieces of content for Part D, with no fixed deadline.

We will keep a record of published work. We will not make completion of all these posts a condition for the ten-week technical project.

Project controls:

We will review progress each week.

We will keep experiment configurations, dataset versions, evaluation results, and decisions in GitLab.

We will record blockers related to Tinker access, computing costs, dataset quality, and model performance.

If fine-tuning does not improve the strongest baseline, we will report the negative result and explain what we learned.

Our final goal is a reproducible research project with measured results, not an untested claim of production readiness.

23. Team Responsibilities and Commitment: Who will do what, and how many hours per week can each member commit?
- assign research,data,training,evaluation,validation,and documentation responsibilities
- include realistic hours per member and other commitments that affect delivery


Our research team has four members. We plan to divide the work according to technical experience and learning goals.

We propose a ten-week schedule. Each member will have a primary responsibility and will support the other members during reviews.

The responsibilities and weekly hours below are proposed. We will confirm them with all team members before the project begins.

Member 1: Project Lead and System Design

Proposed commitment: 10 hours per week.

I will coordinate the project and maintain the technical plan.

My responsibilities will include system design, the traditional Machine Learning (ML) baseline, evaluation design, integration, and final research reporting.

I have more than 15 years of experience in software engineering. I will apply my experience in software architecture, testing, code review, and team coordination.

I will also contribute to the Qwen, Llama, and Mistral architecture paper.

Member 2: Model Training and Visualization

Proposed commitment: 8 hours per week.

This member will help develop Python scripts, prepare Tinker training configurations, and record experiment results.

They will contribute to the LoRA explanation video using Manim and help prepare the accompanying report.

They will work with Member 1 on model evaluation and the final demonstration.

Member 3: Data Engineering and Research

Proposed commitment: 8 hours per week.

This member will help prepare the dataset, maintain annotation records, check data quality, and document the training, validation, and test splits.

They will also contribute to the architecture research paper, reading log, references, and original figures.

This member will work with Member 4 to identify contradictory labels, duplicate examples, and missing information.

Member 4: BFSI Domain and Policy Development

Proposed commitment: 8 hours per week.

This collaborator has software development experience in the Banking, Financial Services, and Insurance (BFSI) sector.

Their proposed responsibilities include defining fictional banking workflows, preparing policy rules, reviewing simulated cases, and testing action-selection logic.

He will help us identify technical assumptions that need confirmation from banking support or operations staff.

We will not treat BFSI programming experience as proof of authority over banking operations or customer-support policies.

Shared responsibilities:

All four members will participate in dataset review, technical discussions, code reviews, and weekly progress checks.

We will use GitLab/GitHub issues, branches, merge requests, and experiment records to track work.

We will assign one owner to each major deliverable. Other members will provide reviews and support.

The project lead will check progress against the ten-week schedule.

Research and evaluation:

Members 1, 3 and 4 will coordinate the research paper.

Members 2 and 3 will prepare the LoRA explanation materials.

Members 2, 3 and 4 will coordinate dataset preparation and review.

Members 1 and 3 will coordinate the baseline and fine-tuning experiments.

All members will review the final evaluation report. We will record each person's contribution.

Other commitments and delivery risks:

We expect team members to complete this project alongside their existing professional or personal commitments.

We will confirm individual availability before the project begins.

We will reserve weeks 9 and 10 for corrections, additional experiments, documentation, and unexpected technical problems.

If a member cannot complete an assigned task, we will review the schedule and reassign the work.

Our proposed weekly commitment is 34 team-hours.

Over ten weeks, this represents approximately 340 team-hours, subject to actual availability.

We will record actual contributions and report any significant changes to the project plan.

We do not claim that all team members have equal experience in Machine Learning or model fine-tuning. We will use peer review, documentation, and small technical tasks to support members who are learning these skills.

## 24. What will you deliver if the project is approved?
- specify model
- reproducible pipeline
- evaluation report, benchmark dataset, paper repository
- demo or pilot available after the initial project.

### Answer

If our project is approved, we plan to deliver a reproducible Banking Support SLM research prototype within ten weeks.

Our first use case will be delayed refund requests in retail banking. The system will receive a customer message, simulated case details, and a fictional banking policy. It will select a permitted support action and prepare a draft reply for human review.

We propose the following deliverables.

1. Fine-tuned Small Language Model

We will fine-tune a small Qwen model using Low-Rank Adaptation (LoRA) on Tinker.

We will select the exact Qwen version after confirming model availability, training support, and cost.

We will deliver the trained adapter weights or an accessible model checkpoint, subject to platform and licensing conditions.

We will document the base model, training settings, model limitations, and intended use.

2. Reproducible Training and Evaluation Pipeline

We will provide Python scripts for data preparation, validation, training, and evaluation.

The repository will include configuration files, dependency instructions, and steps to reproduce the experiments.

We will record the LoRA rank, alpha, target layers, learning rate, training epochs, and training costs.

We will also include two Mermaid diagrams. One will show how a dataset example moves through the project. The other will explain the training process.

3. Reviewed Benchmark Dataset

We will create at least 100 human-reviewed examples for the supervised fine-tuning work.

Each example will contain a customer request, simulated case details, a fictional policy, the expected permitted action, and a reference reply.

We will provide an annotation Standard Operating Procedure (SOP), review records, and documented training, validation, and test splits.

We will also prepare additional independent evaluation cases where resources permit.

We will release synthetic examples and benchmark materials that we are permitted to share.

4. Evaluation and Research Report

We will compare the fine-tuned Qwen model with the prompted Qwen base model and a general-purpose frontier model.

We will also evaluate a traditional Machine Learning baseline using TF-IDF, Logistic Regression, policy rules, and reply templates.

The report will include action-selection accuracy, policy compliance, unsupported statements, human-reviewed reply quality, and available cost measurements.

We will provide a comparative scorecard, results for each permitted action, and an analysis of at least five model failures.

We will state whether the fine-tuned model supports our hypothesis of improving action-selection accuracy by at least five percentage points over the strongest relevant baseline without increasing policy violations.

Negative results will also be reported.

5. Architecture Research Paper

We will prepare a 10–15-page LaTeX paper comparing Qwen, Llama, and Mistral.

The paper will explain the main architecture blocks, design choices, trade-offs, and limitations.

It will include a comparison table, at least four original figures, references, and a reading log.

6. LoRA Explanation Materials

We will prepare a 10–20-minute visual explanation of LoRA using Manim, or the permitted visual presentation alternative if necessary.

We will also deliver the animation source code and a 4–6-page LaTeX report.

The explanation will cover frozen weights, matrices A and B, rank, alpha, training, and merging.

7. Public Research Repository

We will maintain the project in GitLab.

The repository will include the README, research documentation, source code, training configurations, permitted dataset files, evaluation scorecard, and reproducibility instructions.

We will maintain a step-by-step commit history.

We will not publish API keys, real customer records, or confidential banking information.

8. Working Demonstration

We plan to deliver a research demonstration that accepts a simulated delayed refund request and displays the selected action and draft reply.

The demonstration will show the supplied policy and allow a reviewer to examine the output.

We will not connect the initial prototype to live banking systems or send automated replies to customers.

After the initial project, we may seek a supervised pilot with an interested banking or fintech organization.

Such a pilot would require access to authorized workflows, qualified domain reviewers, appropriate data protection measures, and separate approval.

Final outcome:

Our main deliverable will be a reproducible research system with a documented dataset, trained model, baseline comparisons, evaluation results, and a working demonstration.

We will report whether fine-tuning provides a measurable advantage.

We will not claim production readiness or commercial performance without further validation.

## 25. How will you keep the project moving and report progress?
- describe weekly milestones
- internal reviews
- experiment tracking
- documentation,
- communication blockers
- accountability

### Answer

We will manage the Banking Support SLM project through weekly milestones, GitLab collaboration, experiment tracking, and documented technical reviews.

Our proposed project duration is ten weeks. We will assign one primary owner to each deliverable and record the expected result before work begins.

1. Weekly milestones and progress reviews

We will maintain a ten-week milestone plan in GitLab.

Each milestone will have defined tasks, an owner, a target completion date, and an expected deliverable.

We will hold one weekly team review to check completed work, review technical results, and identify blockers.

Our planned milestones are:

Weeks 1–2: Research scope, architecture study, dataset schema, review SOP, and evaluation design.

Weeks 3–4: Reviewed dataset, traditional ML baseline, prompted model baselines, and initial LoRA explanation.

Weeks 5–6: Architecture paper, LoRA video and report, and the first Tinker fine-tuning experiment.

Weeks 7–8: Held-out evaluation, comparative scorecard, policy-error analysis, and model failure review.

Weeks 9–10: Corrections, final experiments where feasible, reproducibility checks, documentation, and final submission.

2. GitLab collaboration and accountability

We will use our existing GitLab repository to manage source code, research documents, and experiment configurations.

We will create issues for major tasks and assign an owner to each issue.

Team members will work on separate branches and submit merge requests for review.

We will maintain a step-by-step commit history so that reviewers can examine how the project developed.

The project lead will track unfinished tasks and coordinate reassignment when necessary.

3. Experiment tracking

We will record each model experiment using a unique experiment identifier.

The record will include the dataset version, model version, training configuration, random seed where applicable, evaluation results, and cost.

For LoRA experiments, we will record rank, alpha, target layers, learning rate, epochs, and training and validation losses.

We will retain failed experiment records and explain what we learned.

We will not change the final test dataset to improve reported results.

4. Internal technical reviews

We will review the dataset before training.

The review will check missing fields, contradictory labels, duplicate examples, and agreement between reviewers.

We will review the baseline results before starting fine-tuning.

After training, we will inspect the comparative scorecard and at least five failed model examples.

We will check whether the results support our original research hypothesis.

We will also review the architecture paper, LoRA video, and repository documentation before submission.

5. Blocker management

Team members will report blockers through GitLab issues and team communication.

Important blockers may include Tinker access, compute costs, unclear banking policies, inconsistent data labels, and model evaluation failures.

We will record the blocker, its owner, its effect on the schedule, and the proposed next action.

We will raise critical blockers during the weekly review or earlier if they prevent planned work.

If a blocker cannot be resolved, we will reduce the experiment scope or use a documented fallback rather than hide the delay.

6. Progress reporting to SBL

We propose to provide SBL with a short weekly progress report.

Each report will include:

Work completed during the week.

Links to relevant GitLab commits, documents, or experiment records.

Measured results, where available.

Open problems and risks.

Work planned for the following week.

Support required from SBL, if any.

We will distinguish completed work from planned work and preliminary findings from validated results.

7. Final accountability

At the end of ten weeks, we will submit the repository, research paper, LoRA explanation materials, dataset documentation, training artifacts, and evaluation report.

We will document each team member's contribution.

We will report negative results and limitations.

Our measure of progress will be completed and reviewable technical evidence, not the number of meetings, commits, or claims about model performance.

SECTION 6: Support Requirements and Funding
26. Resource Requirements and Budget: What support do you need from SBL, and what is your estimated project budget?

- Itemize compute,APIs,subscriptions,datasets,annotation,feedback,mentorship and publication 
support
- explain each resource's purpose,cost estimate,assumptions and resources you can contribute

27. What level of financial support are you seeking?
(Pick one choice)

Funding and compensation are not guaranteed. Any arrangement will depend on project approval, scope, progress, available resources, and mutually agreed terms.
- Primarily tech resources and mentorship
- Tech resources plus a potential paid arrangement based on milestones
- A funded R & D engagement
- I am open to discussing the structure based on project scope and demonstrated progress.

SECTION 7: Final Proposal and Commitment
29. Final Research Pitch: Summarize your proposal, its strongest evidence, and why your team deserves selection
-in 250-400 words,cover problem,users,demand,SLM,hypothesis,differentiation
-evaluation,impact,and evidence of team strengths
- avoid generic claims

30. Share supporting links
- Include repositories
- papers,blogs,prototypes,demos,benchmarks,market research and a brief explanation of relevance



