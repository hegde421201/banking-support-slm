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

We want to study banking customer-support problems in Indian retail banks and fintech payment companies. We do not claim that our proposed SLM will perform better than existing products. We will test this during our research.

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

