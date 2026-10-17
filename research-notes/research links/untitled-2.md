
Problem Discovery and Market Research
9. Give your proposed project a name

Ans: 
**Banking Support SLM: Policy-Guided Reply Assistance for Support Teams**

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

SECTION 3: SLM Thesis and Technical Approach
14. Why do you believe a specialized SLM is the right solution?

- compare with general purpose LLMs, prompting,RAG,conventional software, and existing-model
workflows.
- consider cost,latency, privacy, specialization,deployment constraints,relaiability, structured
outputs and task performance.
- if fine-tuning is not necessary, explain the right approach.

15. SLM Proposal and Research Hypothesis: What will you build, and what measurable hypothesis do you intend to test?

- specify tasks 
- capabilities
- inputs
- outputs
- operating environment
- limits
- specialization
State a falsifiable hypothesis against the strongest relevant baseline and what result would disprove it.

16. What is your proposed model-development strategy?
- outline data preparation
- supervised fine-tuning
- synthetic data
- preference optimization
- distillation
- evaluation
- and deployment where relevant
Justify selected techniques

17. Compute and Data Requirements: Which base model, compute resources, and datasets will you need? How will you access the data?
- specify model family and size
- gpu needs
- training and inference requirements
- timeline
- existing resources
- assumptions
- describe training/evaluation data sources, volume, formats,quality,access permissions
- privacy,confidentiality, licensing, PII handling 
- access risks


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