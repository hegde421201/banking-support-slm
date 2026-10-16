# Logarithms, exponentials, and probability

Note ID: MATH-03  
Tags: math, probability  
Status: Conceptual lessons complete; implementation and empirical evaluation pending  
Written by: Ganesh Rama Hegde  
Last updated: 17-Oct-2026  
Suggested time: Week 1, Day 3: logarithms, exponentials, and probability; 4–5 hours


## Topics to cover

- [x] Powers and exponents
- [x] Logarithms and inverse operations
- [x] Natural logarithms and exponentials
- [x] Basic probability
- [x] Conditional probability
- [x] Category probability distributions
- [x] Softmax normalization of classifier scores
- [x] Numerically stable softmax
- [x] Evaluation versus probability calibration (introductory)
- [ ] Empirical classifier evaluation and calibration on held-out data (future engineering work)

## My explanation

### 1. Powers and logarithms

A power such as $5^3$ means multiplying 5 by itself three times: $5^3=125$. For a positive integer exponent, the exponent counts the number of repeated factors.

A logarithm reverses exponentiation. If $4^3=64$, then $\log_4(64)=3$. In general, for $a>0$, $a\ne1$, and $x>0$:

$$a^y=x\quad\Longleftrightarrow\quad\log_a(x)=y.$$

The natural logarithm $\ln(x)$ has base $e\approx2.71828$. Exponentiation with base $e$ and the natural logarithm undo each other:

$$\ln(e^x)=x,\qquad e^{\ln(x)}=x\quad(x>0).$$

The exponential $e^x$ is positive for every real $x$, including negative inputs.

### 2. Basic probability

For a uniformly selected message from a finite dataset:

$$P(A)=\frac{\text{number of messages satisfying }A}{\text{total number of messages}}.$$

Probabilities lie between 0 and 1. This fraction estimates the frequency of an event in the specified dataset; it does not by itself give a trustworthy model probability for every new message.

### 3. Conditional probability

$P(A\mid B)$ means the probability of $A$ **given that** $B$ is true. Conditioning changes the group used as the denominator:

$$P(A\mid B)=\frac{P(A\cap B)}{P(B)},\qquad P(B)>0.$$

In a dataset, if 50 messages contain *refund* and 35 of those are verified `REFUND_REQUEST`, the conditional probability is $35/50=0.70$, not $35/200$. The denominator is 50 because the condition limits the group to messages containing *refund*.

### 4. Category probabilities

When categories are mutually exclusive and exhaustive, their probabilities sum to 1:

$$\sum_{i=1}^{K}P(C_i)=1.$$

For example, probabilities 0.40, 0.35, and 0.25 sum to 1. These can represent dataset class frequencies or a model's per-message predictions; those are **different quantities** and should not be confused.

### 5. Softmax: scores to a probability distribution

A classifier can assign a real-valued score $s_i$ to each intent. A score is not a probability. Softmax converts a vector of scores into positive numbers that sum to 1:

$$P_i=\frac{e^{s_i}}{\sum_{j=1}^{K}e^{s_j}}.$$

Exponentiation ensures positive numerators; dividing by the total ensures normalization. A higher score receives a higher softmax probability. This transformation is useful, but softmax probabilities are **not automatically calibrated**.

### 6. Numerically stable softmax

Adding or subtracting the same constant $c$ from every score leaves softmax unchanged:

$$\frac{e^{s_i-c}}{\sum_j e^{s_j-c}}=\frac{e^{s_i}}{\sum_j e^{s_j}}.$$

Choose $c=\max_j(s_j)$ to avoid unnecessarily large exponentials. For scores $(5,2)$, the shifted scores are $(0,-3)$; the probabilities remain approximately $(0.953,0.047)$.

### 7. Evaluation and calibration

**Evaluation** measures predictive performance on held-out examples, using metrics such as accuracy. **Calibration** checks whether stated confidence levels agree with observed correctness rates across groups of predictions.

For example, if 50 predictions each have approximately 80% confidence but only 30 are correct, observed accuracy for that group is $30/50=0.60$. The confidence exceeds observed accuracy by 0.20 (20 percentage points): the classifier is **overconfident in this group**. This does not establish its calibration across all confidence ranges.

## Worked example

### A. Logarithm

$$4^3=64\quad\Longrightarrow\quad\log_4(64)=3.$$

The logarithm asks for the exponent that turns base 4 into 64.

### B. Natural logarithm and IDF

In the MATH-02 illustrative dataset, $N=100$ messages and $DF(\text{loan})=20$:

$$\operatorname{IDF}(\text{loan})=\ln\left(\frac{100}{20}\right)=\ln(5)\approx1.609.$$

Equivalently, $e^{1.609}\approx5$. This is an example of how logarithms compress frequency ratios.

### C. Conditional probability

In an **invented** dataset of 200 banking messages, 50 contain *refund*, and 35 of those have verified intent `REFUND_REQUEST`:

$$P(\text{REFUND\_REQUEST}\mid\text{contains refund})=\frac{35}{50}=0.70.$$

The remaining 150 messages are excluded from the denominator because they do not satisfy the condition.

### D. Softmax

Assume **illustrative** scores $(3,1,0)$ for `CARD_BLOCKED`, `REFUND_REQUEST`, and `LOAN_PAYMENT_FAILURE`:

$$e^3\approx20.086,\quad e^1\approx2.718,\quad e^0=1.$$

The total is approximately $23.804$. Softmax gives:

| Intent | Score | Approximate softmax output |
|---|---:|---:|
| `CARD_BLOCKED` | 3 | 0.844 |
| `REFUND_REQUEST` | 1 | 0.114 |
| `LOAN_PAYMENT_FAILURE` | 0 | 0.042 |

The outputs sum to approximately 1 (subject to rounding). They are mathematical outputs for invented scores, not validated model probabilities.

### E. Calibration

Suppose 50 held-out predictions have confidence near 0.80 and 30 are correct:

$$\text{Observed accuracy}=\frac{30}{50}=0.60.$$

$$\text{Confidence gap}=0.80-0.60=0.20.$$

This group is overconfident. A single group does not characterize the entire classifier.

## Connection to this project

In the Banking Support SLM system, intent classification is separate from policy decisions and response generation. A classifier may compute intent scores and use softmax to obtain a distribution across supported intents. The policy engine may consider a confidence threshold when deciding whether to provide an approved response, request clarification, or escalate.

That workflow creates a risk: if confidence is poorly calibrated, a high numerical value may cause the policy engine to trust an incorrect intent. Therefore, classifier accuracy and calibration must be evaluated on representative held-out messages before using confidence thresholds in production. A generated response must still obey the policy engine and must not gain authority merely because a classifier reports high confidence.

This mathematical study does **not** establish that a particular model, threshold, or banking response workflow is safe or accurate. Those claims require experimental evidence.

## Code and evidence links

- Code: Not linked yet; mathematical study preceded implementation.
- Test or result: No repository experiment or benchmark result is claimed here.
- Related requirement or research question: Confirm the applicable ID in the repository before adding a link.

## Checks I completed

The following are **interactive lesson exercises**, not automated tests or benchmark results:

| Lesson | Exercise | Answer supplied | Review |
|---|---|---|---|
| 1 | $5^3$ | 125 | Correct |
| 2 | $\log_4(64)$ | 3 | Correct |
| 3 | $\ln(e^4)$ | 4 | Correct |
| 4 | 50 of 200 messages | 0.40 | Corrected to 0.25 |
| 4 correction | 40 of 200 messages | 0.20 | Correct |
| 5 | 35 `REFUND_REQUEST` among 50 messages containing *refund* | 0.70 | Correct |
| 6 | 70 of 200 messages | 0.35 | Correct |
| 7 | Softmax of scores $(0,0)$, first class | 0.50 | Correct |
| 8 | Subtract 5 from $(5,2)$ | $(0,-3)$ | Correct |
| 9 | 30 correct of 50 predictions at ~0.80 confidence | Overconfident | Correct |

No Python execution, trained-model evaluation, or calibration experiment was performed as part of these checks.

## Questions and corrections

1. **Why does the denominator change in conditional probability?** The condition restricts the eligible group. In the *refund* example, only the 50 messages containing the word are considered.
2. **Why can category probabilities sum to 1?** Only if the categories are mutually exclusive and exhaustive over the specified outcome space.
3. **Why are classifier scores not probabilities?** Scores can be negative or greater than 1 and need not sum to 1. Softmax produces a normalized distribution.
4. **Why subtract the largest score before softmax?** A common shift cancels algebraically, while smaller exponent inputs reduce numerical overflow risk.
5. **Why is a 0.95 softmax output not proof of correctness?** Calibration is an empirical property established across representative held-out predictions, not guaranteed by the softmax formula.
6. **Correction from Lesson 4:** $50/200=0.25$, not 0.40. The follow-up $40/200=0.20$ was answered correctly.

## Interview explanation

**How do scores become probabilities?** A classifier can use softmax to exponentiate each category score and divide it by the sum of all exponentials. This creates nonnegative values that sum to 1. Subtracting the maximum score first preserves the output while improving numerical stability.

**Why is a prediction probability not proof of correctness?** A softmax output is a model-produced number, not a guarantee. Evaluation checks how often predictions are correct; calibration checks whether confidence values agree with observed correctness frequencies on representative held-out data.

## Sources and assistance

- Primary structure: the author's `03-logarithms-probability.md` template (MATH-03).
- Prior learning: MATH-01 classifier scores and MATH-02 TF-IDF/IDF examples discussed in the learning sessions.
- ChatGPT assistance: mathematical explanations, illustrative banking examples, exercise reviews, and consolidation of this draft.
- Author's contributions: exercise answers listed in **Checks I completed**, including the corrected probability exercise.
- External sources and empirical evidence: none added or claimed in this consolidation.
