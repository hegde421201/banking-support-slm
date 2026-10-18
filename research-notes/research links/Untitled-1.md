
Problem Discovery and Market Research
9. Give your proposed project a name

10. Problem and Target Users: What specific problem are you solving, who experiences it, and how frequently?

- Define the problem before u define the model.
- Identify target users, workflows,frequency, pain,costs,and consequences.
- be specific about persona or business segment.

11. Market Research and Competition: What evidence validates this problem, and what competing solutions have you researched? Include links.

- Include interviews,reports,discussions,reviews or surveys or observations
- Separate verified evidence from assumptions. 
- compare products,open-source models, commercial AI, and manual workflows with concrete limitations.

12. Why is this problem worth solving now?
- Explain changes in market,technology,data availability,or customer behaviour that makes it timely compared with 2-3 years ago

13. Business Value and Initial Scope: What value would solving this problem create, and what specific use case will you tackle first?
- identify beneficiaries,time or cost savings, business outcomes,potential buyers, and assumptions.Define narrowest useful 
initial use cases with measurable value.


Links

```
https://www.mckinsey.com/industries/financial-services/our-insights/the-ai-powered-bank-rewiring-for-excellence-in-customer-care?utm_source=chatgpt.com


McKinsey describes banking customer operations as a major AI opportunity. Its case study reports a 15% reduction in average handling time within 100 days and a 10% cost reduction within six months for a credit union transformation. 

Project implication: Build a support-agent copilot that reduces time spent classifying complaints, finding policies, and drafting responses.

```


```
https://www.rbi.org.in/scripts/AnnualReportPublications.aspx?Id=1436&utm_source=chatgpt.com

2. RBI Annual Report 2024–25
Reserve Bank of India · Official reportRBI reports approximately 2.96 lakh complaints received by its Ombudsman offices in FY 2024–25. It also describes work to integrate AI into complaint management. 

Project implication: Complaint classification, evidence collection, and safe escalation address documented operational needs.


```

```

https://www.npci.org.in/product/upi/product-statistics?_bhlid=5ad8a6b9294dbc6e5346af7062d0ebd2193cafe7&utm_source=chatgpt.com

3. NPCI UPI Product Statistics
NPCI · September 202624.07 billion
UPI transactions in September 2026
The scale of digital payments creates a substantial potential support workload, although transaction volume does not tell us the complaint rate. 

Project implication: Include India-specific payment scenarios rather than relying exclusively on BANKING77.

```

```
https://cfpb.website/data-research/consumer-complaints/?utm_source=chatgpt.com

U.S. Consumer Financial Protection BureauProvides downloadable consumer complaint data, including selected public narratives and information about company responses. The agency cautions that complaints are not representative of all consumers. 

Project implication: Use complaint narratives to discover realistic scenarios, then create independently reviewed labels for actions and replies.

```

```
https://www.rbi.org.in/commonman/Upload/English/Notification/PDFs/CIRCULAR677EC931A7A65E4D99AA957D8E85BC0A2A.PDF?utm_source=chatgpt.com

RBI · Payment systems circularDescribes different reversal and compensation rules for failed ATM, card, IMPS, and UPI transactions. These rules depend on transaction type. 

Project implication: Add a policy-driven decision engine. The SLM must not invent deadlines or compensation eligibility.

```
---

## Draft form answers

Prepared on 17 October 2026. These answers describe proposed research, not completed model results.

### 9. Give your proposed project a name

**Banking Support SLM: Policy-Guided Reply Assistance for Support Teams**

### 10. Problem and target users

Banking support agents must interpret customer messages, check the available account context, and apply the correct policy before replying. Similar requests can require different actions. A pending transfer, a failed transfer, and an unrecognised payment must not receive the same response. Missing information can require clarification. Other cases need human escalation. The problem is to make these decisions and reply drafts consistent, without inventing facts, deadlines, or completed banking actions.

Our intended primary users are frontline banking support agents. Support supervisors and quality reviewers are secondary users. Customers would benefit indirectly through the replies that agents review and send. Our initial research covers eight English request types involving cards, transfers, refunds, and disputed payments. We will use public intent data, simulated account context, and fictional bank policies.

The problem occurs across recurring support requests. However, we have not measured its daily frequency at a target bank. Published evidence establishes a broader complaint workload. The RBI Annual Report 2024-25 states that its Ombudsman offices received 2.96 lakh complaints during that year. Most concerned loans or advances and digital banking products. These are escalated complaints across regulated entities, not a count of all bank support contacts or our eight request types. [Source: RBI, paragraph VI.98](https://www.rbi.org.in/scripts/AnnualReportPublications.aspx?Id=1436).

There is also evidence that changes to banking support operations can improve efficiency. McKinsey reports a credit union transformation that reduced average handling time by 15% within 100 days. The programme also reduced costs by 10% within six months. It combined workflow changes with several AI use cases. These figures cannot be attributed to an SLM alone or presented as expected results for our project. [Source: McKinsey case study](https://www.mckinsey.com/industries/financial-services/our-insights/the-ai-powered-bank-rewiring-for-excellence-in-customer-care).

We propose to study whether a specialized SLM can help agents prepare consistent, policy-guided reply drafts. The comparison will measure reply usefulness and policy errors against fixed templates under the same action and policy conditions. Response time and memory use will also be measured. Human review remains part of the proposed workflow. The prototype will not access real accounts, move money, or send customer messages.

This is currently a research hypothesis. We have not established customer demand through agent interviews, measured handling-time savings, or demonstrated model improvement. Interviews and workflow observations are proposed next steps. They would help establish which request types cause the most rework and how frequently agents encounter them.

## Source checks and research limits

These checks supplement the original notes above. The original links and summaries remain unchanged.

1. **RBI annual report:** The 2.96 lakh figure is supported by paragraph VI.98. Paragraph VI.93 describes phased AI integration into complaint management. This supports problem discovery, not a claim that our system is validated.
2. **McKinsey:** The handling-time and cost figures are supported by the linked case study. They describe a wider transformation. They are not results from our project.
3. **NPCI:** The linked statistics page did not expose the monthly figures during this check. The September 2026 figure of 24.07 billion remains unverified here. It is excluded from the draft answer. Transaction volume alone would not establish a support-contact rate.
4. **CFPB:** The original link uses cfpb.website. Use the official [Consumer Complaint Database](https://www.consumerfinance.gov/data-research/consumer-complaints/) for attribution. The CFPB warns that these complaints are not a representative sample of all consumer experiences. Narratives can inform problem discovery, but they do not supply verified action labels or approved replies.
5. **RBI payment circular:** The linked document is dated 20 September 2019. It describes failed-transaction resolution and compensation rules for different payment types. It supports the need to distinguish transaction contexts. We have not established that this document alone contains all currently applicable requirements. Our prototype continues to use fictional policies. [Source: RBI circular](https://www.rbi.org.in/commonman/Upload/English/Notification/PDFs/CIRCULAR677EC931A7A65E4D99AA957D8E85BC0A2A.PDF).

### Items to establish through user research

- Interview support agents and supervisors, if access can be arranged.
- Record the number of interviews and each participant's role.
- Identify frequent request types and difficult policy decisions.
- Ask how often agents correct templates or rewrite drafts.
- Measure handling time and editing effort only with an agreed method and suitable access.
- Separate interview findings from assumptions and published case studies.

### Scope and team notes for later answers

- The team has four people: the project lead and three collaborators.
- The project lead owns mathematics and coding.
- Two collaborators have an established LoRA-video role. The third collaborator's responsibilities are not yet recorded here.
- Qwen fine-tuning on Tinker is a proposed course extension. It is not a completed experiment or part of the currently approved CPU comparison.
- India-specific UPI scenarios and real regulatory policies would expand the current study. They are possible future work, not existing deliverables.
- Drafting assistance: Codex,ChatGPT. Research links and initial source summaries were provided by the project lead.


---

Rishik Kumar Balanagu
-------------------

Repos:
Memory-Ops: https://github.com/rishibalanagu0108/Memory-OPS
Invoice Risk Check: https://github.com/rishibalanagu0108/Invoice_Risk_Check_Agent

Opensource contributions:
https://github.com/supermemoryai/supermemory/pull/1816
https://github.com/supermemoryai/supermemory/pull/1815
https://github.com/neatlogs/neatlogs/pull/219

Rishik has previous working experience on building the Full-stack Systems (Javascript, Python) of 2 years, and right now he is building many AI Systems and also trying to understand the finetuning concepts by understanding and making them work at production level.

------

Sarfaraj Ejaj

He is a full stack Java/Angular developer with 10 years of experience.
In the BFSI (Banking,Financial Service,Insurance) domain, he has 7+ years experience in banking.
He has also developed GenAI applications, specifically chatbot and worked on apps using OpenAI, RAG,Langchain,langraph etc.

git - https://github.com/sarfaraj-ejaj

---

Shriyansh Sinha 

He is a IIT Patna B.Tech 2025 graduate. 
He has around 2 years of experience working as a software engineer in a product based company - Juspay where he has experience taking lead and innovating solutions for the ever changing and frontier tech ask of a startup culture. 

These are some of the projects he has recently done - 

1. Data Quality pipeline triage classifier - https://github.com/Shriyansh-20/AI-Native-Learning/tree/main/week1/deliverables/student-project
2. Ask-My-Doc a RAG based product that'll help anyone with their documents -  https://github.com/Shriyansh-20/Domain-Specific-Ask-my-DOC-System
3. Autodeploy - A deployment web-app for deploying your local projects to cloud for public usage - https://github.com/Shriyansh-20/AutoDeploy


Research Paper - HyDeML: Hybrid Mode Decomposition-based Machine Learning Framework for Bus Arrival PredictionHe has also published a research paper on Travel Time Predictions and benchmarking various Mode Decomposition techniques for this scenario. His paper was accepted in the 2026 TRB research conference, Washington D.C.

https://drive.google.com/file/d/13xrBczK6WbtdzdyFoecn3Fs5-uguLXc9/view?usp=sharing

---