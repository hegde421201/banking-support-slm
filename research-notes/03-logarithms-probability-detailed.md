# Logarithms, exponentials, and probability

**Note ID:** MATH-03  
**Tags:** math, probability, banking-support-slm  
**Status:** Nine conceptual lessons completed; implementation and empirical evaluation pending  
**Written by:** Ganesh Rama Hegde  
**Last updated:** 17-Oct-2026  
**Suggested time:** Week 1, Day 3 (original curriculum: 4–5 hours; actual study may take longer)

## Topics to cover

- [x] Lesson 1 — Powers and exponents
- [x] Lesson 2 — Logarithms as inverse operations
- [x] Lesson 3 — Natural logarithms and natural exponentials
- [x] Lesson 4 — Basic probability
- [x] Lesson 5 — Conditional probability
- [x] Lesson 6 — Category probability distributions
- [x] Lesson 7 — Softmax: from scores to probabilities
- [x] Lesson 8 — Numerically stable softmax
- [x] Lesson 9 — Evaluation versus probability calibration
- [x] Lesson 10 — Consolidation of the conceptual lessons
- [ ] Implement and test the formulas in code
- [ ] Evaluate intent predictions and calibration on representative held-out banking messages

## My explanation

### Lesson 1 — Powers: what does an exponent mean?

**The question we want to answer.** What does it mean when a number is raised to a power, and why do we need to understand it before studying logarithms?

Consider $2^3$. The number **2** is the *base*. The number **3** is the *exponent*. For a positive whole-number exponent, the operation means repeated multiplication:

$$2^3=2\times2\times2=8.$$

It is **not** $2\times3=6$. The exponent specifies the number of factors, not a multiplier applied once. Similarly,

$$5^3=5\times5\times5=125.$$

A useful special case is $a^0=1$ for any nonzero $a$. Negative exponents are also meaningful: $a^{-2}=1/a^2$ when $a\ne0$. Thus an exponential expression is not limited to counting repeated factors, even though repeated multiplication is the easiest place to begin.

**Why this matters next.** If we know the base and exponent, we can calculate the result. Logarithms answer the reverse question: if we know the base and result, which exponent was used?

**Exercise completed.** $5^3=125$ — **correct**.

### Lesson 2 — Logarithms: finding an unknown exponent

**The problem.** Suppose we know $4^3=64$, but instead of calculating 64, we ask: *Which exponent must be applied to 4 to obtain 64?*

The answer is 3. We write this question as:

$$\log_4(64)=3.$$

Read it as “logarithm of 64 to base 4 equals 3.” The base is 4, the input to the logarithm is 64, and the output is the exponent 3.

The general relationship is:

$$a^y=x\quad\Longleftrightarrow\quad\log_a(x)=y,$$

where $a>0$, $a\ne1$, and $x>0$ for real-valued logarithms.

This equivalence explains the operation rather than requiring us to memorize disconnected formulas. For example:

$$10^2=100\quad\Longleftrightarrow\quad\log_{10}(100)=2.$$

$$3^4=81\quad\Longleftrightarrow\quad\log_3(81)=4.$$

**Common mistake.** A logarithm does not return the base or the final result. It returns the exponent needed to produce that result from the specified base.

**Exercise completed.** $\log_4(64)=3$ — **correct**.

### Lesson 3 — Natural logarithms and exponentials

**The question.** If logarithms can have bases 2, 4, or 10, what is special about $\ln(x)$ in machine learning?

The *natural logarithm* is simply the logarithm with base $e$, where $e\approx2.71828$:

$$\ln(x)=\log_e(x).$$

The corresponding exponential is $e^x$. For example,

$$e^2\approx7.389,$$

so

$$\ln(e^2)=2.$$

The natural logarithm asks which exponent of $e$ produces the input. Therefore:

$$\ln(e^x)=x\qquad\text{for every real }x.$$

In the opposite direction:

$$e^{\ln(x)}=x\qquad\text{for }x>0.$$

The domain condition matters: a real-valued natural logarithm is defined only for positive inputs. By contrast, $e^x$ is positive for every real input, even when $x$ is negative. For example, $e^{-2}=1/e^2\approx0.1353$.

**Connection to MATH-02 (IDF).** We previously defined inverse document frequency as:

$$\operatorname{IDF}(t)=\ln\left(\frac{N}{DF(t)}\right).$$

Here $N$ is the number of documents and $DF(t)$ is the number of documents containing term $t$. In a *teaching dataset* of 100 banking messages, if 20 contain the term `loan`, then:

$$\operatorname{IDF}(\text{loan})=\ln(100/20)=\ln(5)\approx1.609.$$

This is not a probability. It is a feature weight used to represent how uncommon the term is across documents. The natural log compresses the ratio: a fivefold ratio becomes about 1.609, rather than 5. Other log bases are possible; the natural logarithm is a common mathematical convention.

**Exercise completed.** $\ln(e^4)=4$ — **correct**. We do not need to calculate $e^4$ first; the inverse relationship gives the result directly.

### Lesson 4 — Basic probability: what does a fraction describe?

**The engineering problem.** A banking message may belong to several possible intent categories. Before using message-specific evidence, we can first ask how common each intent is in a labeled dataset.

If we select one message **uniformly at random** from a finite dataset, the probability of an event $A$ is:

$$P(A)=\frac{\text{number of messages satisfying }A}{\text{total number of messages}}.$$

The equal-likelihood assumption is essential: the formula applies directly because every message has the same chance of being selected. In a dataset of 100 messages, if 30 have verified intent `CARD_BLOCKED`, then:

$$P(\text{CARD\_BLOCKED})=30/100=0.30.$$

This means 30% of the messages in **this dataset** belong to that category. It does **not** establish that any particular new message has a 30% chance of being blocked, nor does it prove the dataset represents real production traffic.

A probability must lie between 0 and 1: 0 means impossible under the stated setup; 1 means certain under that setup. To convert a probability to a percentage, multiply by 100.

**The correction that mattered.** The first exercise had 50 `LOAN_PAYMENT_FAILURE` messages among 200. The initial answer was 0.40, but the correct calculation is:

$$50/200=0.25=25\%.$$

A follow-up exercise had 40 `CARD_ACTIVATION` messages among 200:

$$40/200=0.20=20\%.$$

That correction was solved correctly. The lesson is to identify the numerator and denominator **before** dividing.

### Lesson 5 — Conditional probability: changing the denominator when evidence arrives

**The engineering question.** A customer writes, “My debit card is blocked.” Should the classifier ignore the word `blocked` and rely only on the overall frequency of `CARD_BLOCKED` messages? No. We want to reason about the subset of messages that contain this evidence.

Define two events:

- $A$: the verified intent is `CARD_BLOCKED`.
- $B$: the message contains the word `blocked`.

The notation $P(A\mid B)$ is read “probability of $A$ **given** $B$.” The vertical bar tells us to restrict attention to cases where $B$ is true.

Suppose, in an illustrative dataset of 100 messages, 20 contain `blocked`, and 15 of those 20 are verified `CARD_BLOCKED`. Then:

$$P(A\mid B)=15/20=0.75.$$

**Why not divide by 100?** Because the question is not “What fraction of *all* messages have both properties?” It is “Among messages already known to contain `blocked`, what fraction have intent `CARD_BLOCKED`?” Once $B$ is given, the relevant population is the 20 messages satisfying $B$.

The formal definition follows from expressing both counts as proportions of the original population:

$$P(A\mid B)=\frac{P(A\cap B)}{P(B)},\qquad P(B)>0.$$

In the example, $P(A\cap B)=15/100=0.15$ and $P(B)=20/100=0.20$. Their ratio is $0.15/0.20=0.75$.

**A second example from the exercise.** Among 200 messages, 50 contain `refund`. Of those 50, 35 have verified intent `REFUND_REQUEST`. Therefore:

$$P(\text{REFUND\_REQUEST}\mid\text{contains refund})=35/50=0.70.$$

The answer **0.70 was correct**. The number 200 would be the denominator for the *joint* event among all messages, giving $35/200=0.175$; that answers a different question.

**Important distinction.** $P(A\mid B)$ is generally different from $P(B\mid A)$. “Probability of refund intent given the word refund” is not the same as “probability of the word refund given refund intent.” We did not derive Bayes' theorem in this lesson.

### Lesson 6 — Category probabilities: why must they add up to one?

**The problem.** Our intent classifier considers more than one possible category. If a dataset contains mutually exclusive, exhaustive labels, the categories partition the dataset: every message belongs to one category and none belongs to two.

Suppose 100 illustrative messages are labeled as follows:

| Intent | Count | Probability |
|---|---:|---:|
| `CARD_BLOCKED` | 40 | 0.40 |
| `LOAN_PAYMENT_FAILURE` | 35 | 0.35 |
| `REFUND_REQUEST` | 25 | 0.25 |
| **Total** | **100** | **1.00** |

The total is 1 because:

$$\frac{40}{100}+\frac{35}{100}+\frac{25}{100}=\frac{100}{100}=1.$$

For $K$ exhaustive, mutually exclusive categories $C_1,\dots,C_K$:

$$\sum_{i=1}^{K}P(C_i)=1.$$

**Why the assumptions matter.** If labels overlap (for example, a message can have both `CARD_BLOCKED` and `COMPLAINT`), adding their separate probabilities may exceed 1. If the category list omits some possible intents, its total may be less than 1. The sum-to-one requirement belongs to a complete distribution over mutually exclusive outcomes.

**Exercise completed.** For 200 messages, `REFUND_REQUEST` occurred 70 times. Thus $70/200=0.35$ — **correct**. The other categories had frequencies 80/200=0.40 and 50/200=0.25, giving $0.40+0.35+0.25=1$.

**Distinction to preserve.** These frequencies describe a dataset. A model may later output a *different* distribution for each individual message. We should not confuse class prevalence with per-message model confidence.

### Lesson 7 — Softmax: turning scores into a distribution

**The engineering problem.** In MATH-01, we used a weighted score such as $s=w_1x_1+w_2x_2+b$. For multiple intents, a classifier may produce one real-valued score per category. These raw scores are often called *logits*.

Suppose an illustrative classifier scores a single message as:

| Intent | Score |
|---|---:|
| `CARD_BLOCKED` | 3 |
| `REFUND_REQUEST` | 1 |
| `LOAN_PAYMENT_FAILURE` | 0 |

The score 3 is **not** a probability. It is greater than 1, and the scores sum to 4 rather than 1. We need a transformation that yields nonnegative values summing to 1 while preserving score order.

**Step 1: exponentiate.** Compute $e^{s_i}$ for each score:

$$e^3\approx20.086,\qquad e^1\approx2.718,\qquad e^0=1.$$

All values are positive, and the highest score remains highest.

**Step 2: calculate the total.**

$$Z=e^3+e^1+e^0\approx23.804.$$

**Step 3: normalize each value by the same total.**

$$P(\text{CARD\_BLOCKED})\approx20.086/23.804\approx0.844,$$

$$P(\text{REFUND\_REQUEST})\approx2.718/23.804\approx0.114,$$

$$P(\text{LOAN\_PAYMENT\_FAILURE})\approx1/23.804\approx0.042.$$

They add to approximately 1; tiny differences can arise from rounding. This is **softmax**:

$$\operatorname{softmax}(s)_i=\frac{e^{s_i}}{\sum_{j=1}^{K}e^{s_j}}.$$

**Why this formula works.** The numerator is positive. The denominator is the sum of all positive numerators, so each fraction is between 0 and 1. Adding the fractions produces denominator divided by itself, which equals 1. Exponentiation also makes relative score differences matter. Softmax is a useful choice, **not the only mathematical way** to create a distribution.

**Exercise completed.** For two scores $(0,0)$, the exponentials are $(1,1)$. The first probability is $1/(1+1)=0.50$ — **correct**. Equal scores give equal softmax probabilities.

**Caution.** A softmax result of 0.844 is a model output, not proof that 84.4% of such predictions will be correct. Reliability must be measured on data.

### Lesson 8 — Numerically stable softmax: why subtract the maximum?

**The engineering problem.** Exponentials grow rapidly. A naive program attempting to compute $e^{1000}$ may overflow ordinary floating-point arithmetic, even when the *final probability* would be perfectly valid.

The key mathematical property is that softmax does not change when we subtract the **same constant** from every score.

For any constant $c$:

$$\frac{e^{s_i-c}}{\sum_j e^{s_j-c}}=\frac{e^{s_i}/e^c}{\sum_j e^{s_j}/e^c}=\frac{e^{s_i}}{\sum_j e^{s_j}}.$$

The common factor $1/e^c$ cancels. This means the absolute location of the scores is irrelevant; their differences determine the probabilities.

For example, scores $(3,1)$ and $(13,11)$ differ by 2 in both cases. Their softmax probabilities are identical.

**Why choose the maximum score as $c$?** Subtracting the maximum makes the largest shifted score exactly zero, so its exponential is $e^0=1$. Every other shifted score is zero or negative, so its exponential is at most 1. This prevents huge positive exponentials.

**Exercise completed.** Original scores $(5,2)$. Subtract the maximum, 5:

$$(5-5,\ 2-5)=(0,-3).$$

The answer **$(0,-3)$ was correct**. Both original and shifted scores yield:

$$P_1=\frac{1}{1+e^{-3}}\approx0.953,\qquad P_2\approx0.047.$$

**Engineering takeaway.** In a Python implementation, compute shifted exponentials rather than raw exponentials. This is a numerical safety measure; it does not retrain or recalibrate the classifier.

### Lesson 9 — Evaluation and probability calibration

**The engineering question.** Suppose a banking intent classifier reports `CARD_BLOCKED` with confidence 0.95. Does that prove a 95% chance that this individual prediction is correct? No. A softmax value is a model's reported probability, and we must test whether those reports are trustworthy.

**Evaluation asks:** How well does the classifier perform on examples whose true labels we know? For instance, if it correctly classifies 80 of 100 held-out messages:

$$\text{Accuracy}=80/100=0.80.$$

This measures the fraction of correct predictions in that evaluation set. It does not by itself tell us whether reported confidence values match reality.

**Calibration asks:** Across many predictions assigned roughly the same confidence, how often is the predicted class actually correct? A classifier is well calibrated around 80% confidence if, over enough representative predictions assigned about 80% confidence, roughly 80% are correct.

Consider the completed exercise: 50 predictions each have confidence approximately 0.80, but only 30 are correct. Their observed accuracy is:

$$30/50=0.60.$$

The gap is:

$$0.80-0.60=0.20\quad\text{(20 percentage points)}.$$

Therefore the classifier is **overconfident in this group**. The selected answer **B** was correct. This one group does not establish calibration across all possible confidence values.

**Why this matters in a banking system.** Suppose a policy engine permits an approved automated response when confidence exceeds an illustrative threshold of 0.90. If confidence is systematically inflated, the engine may act on more incorrect intent predictions than the threshold suggests. Confidence-based decisions need evaluation, calibration checks, and appropriate safeguards. A threshold of 0.90 here is an example, not a production recommendation.

**What calibration does not do.** Calibration cannot guarantee the correctness of an individual prediction. Nor does a calibrated classifier necessarily have high accuracy: accuracy and calibration answer different questions.

## Worked example

This section collects the calculations in one place **after** their full explanations above, for convenient review.

| Lesson | Question | Calculation | Result |
|---|---|---|---|
| 1 | Evaluate $5^3$ | $5\times5\times5$ | $125$ |
| 2 | Find $\log_4(64)$ | $4^3=64$ | $3$ |
| 3 | Find $\ln(e^4)$ | Inverse operations | $4$ |
| 4 | 40 activation messages of 200 | $40/200$ | $0.20$ |
| 5 | 35 refund intents among 50 containing `refund` | $35/50$ | $0.70$ |
| 6 | 70 refund messages of 200 | $70/200$ | $0.35$ |
| 7 | Softmax of $(0,0)$ | $1/(1+1)$ | $0.50$ |
| 8 | Shift $(5,2)$ by its maximum | $(5-5,2-5)$ | $(0,-3)$ |
| 9 | 30 correct of 50 predictions | $30/50$ | $0.60$ observed accuracy |

## Connection to this project

Our Banking Support SLM research separates **intent recognition**, **policy decisions**, and **response generation**. The mathematics in MATH-03 is most directly relevant to the intent-classification stage and to deciding whether its confidence is dependable.

1. **Text features:** MATH-02 introduced TF-IDF. The natural logarithm appears in IDF and helps scale document-frequency ratios.
2. **Intent scores:** MATH-01 introduced weighted scores. A multiclass classifier can produce a score for each candidate banking intent.
3. **Intent probabilities:** Softmax converts the scores into a distribution over mutually exclusive intent categories.
4. **Safe computation:** Subtracting the maximum score before exponentiation reduces overflow risk.
5. **Decision reliability:** Evaluation checks predicted intents against verified labels; calibration checks whether reported probabilities correspond to observed accuracy.
6. **Policy boundary:** The policy engine must not treat high confidence as authorization to perform a banking action. Policy rules and authorized backend operations remain separate from the classifier and from any SLM-generated response.

**Example flow (conceptual, not an implemented pipeline):**

```text
Customer message
      |
      v
Text representation (e.g., TF-IDF)
      |
      v
Intent classifier -> one score per intent
      |
      v
Stable softmax -> probability distribution
      |
      v
Evaluation / calibration evidence informs confidence handling
      |
      v
Policy engine -> approved response, clarification, or escalation
      |
      v
Template or SLM response generator (subject to policy)
```

**Benchmarking implication.** If comparing template responses against Qwen, Llama, and Mistral-generated responses, keep the intent classifier and policy decisions fixed where the experiment calls for it. Otherwise a difference in outcomes may come from a changed classifier or policy rather than from the response generator. This is an experimental-design recommendation, not a measured result.

## Code and evidence links

- **Code:** Not linked yet. Do not claim a Python implementation exists until it is committed and tested.
- **Test or result:** No empirical benchmark, held-out accuracy, or calibration results are recorded in this note.
- **Related requirement or research question:** Verify intent recognition, probability reliability, and safe separation of classification from policy and generation. Add repository-specific requirement IDs when they are available.
- **Prior math:** MATH-01 (weighted scores and bias); MATH-02 (vectors, dot products, and TF-IDF).

## Checks I completed

The following are **manual learning exercises**, not executed software tests:

| Lesson | Submitted answer | Review |
|---|---|---|
| 1 | $125$ | Correct |
| 2 | $3$ | Correct |
| 3 | $4$ | Correct |
| 4, first attempt | $0.40$ for $50/200$ | Incorrect; corrected to $0.25$ |
| 4, correction | $0.20$ for $40/200$ | Correct |
| 5 | $0.70$ | Correct |
| 6 | $0.35$ | Correct |
| 7 | $0.50$ | Correct |
| 8 | $(0,-3)$ | Correct |
| 9 | B — overconfident | Correct; observed accuracy $0.60$ |

No Python code, evaluation dataset, or calibrated production model was run as part of these lessons.

## Questions and corrections

**Q1. Why does conditional probability use a different denominator?** Because “given $B$” restricts the relevant population to cases satisfying $B$. Among 50 messages containing `refund`, 35 have refund intent, so the answer is $35/50$, not $35/200$.

**Q2. Why do category probabilities add to 1?** Only when the categories are mutually exclusive and exhaustive. They then cover all outcomes exactly once.

**Q3. Why exponentiate scores before normalizing?** Exponentials are always positive and preserve score ordering. Dividing by their total creates a distribution. This does not automatically make the distribution calibrated.

**Q4. Why subtract the maximum score?** A common shift leaves softmax unchanged, while choosing the maximum ensures no shifted score is positive. This avoids unnecessarily large exponentials.

**Q5. What is the difference between accuracy and calibration?** Accuracy measures how many predictions are correct. Calibration compares stated confidence with observed correctness among predictions of similar confidence.

**Q6. What correction did I make?** In Lesson 4, $50/200$ was initially answered as 0.40. The correct result is 0.25. The follow-up $40/200=0.20$ was answered correctly.

**Questions for future study:** How do we evaluate a multiclass classifier beyond accuracy? How do we calculate calibration metrics such as expected calibration error? How can a calibration method be fitted without leaking information from the final test set? These topics were **not derived in MATH-03** and should be studied separately.

## Interview explanation

> **How do scores become probabilities?** A classifier produces one score per intent. Softmax exponentiates the scores and divides each exponential by the sum of all exponentials. This gives positive values that add to 1. We subtract the largest score first for numerical stability.
>
> 
> **Why is a predicted probability not proof of correctness?** Softmax normalizes scores, but normalization does not validate the classifier's beliefs. We must compare predictions and confidence values against verified labels on representative held-out data. Accuracy evaluates correctness; calibration evaluates whether reported confidence agrees with observed correctness.

*This heading is retained from the supplied MATH-03 template. It can also serve as a short engineering explanation; the full derivations are in the lessons above.*

## Sources and assistance

- **Primary source:** MATH-03 lesson-by-lesson conversation, including the author's exercise responses and corrections.
- **Earlier course context:** MATH-01 weighted-score and bias exercises; MATH-02 TF-IDF work.
- **AI assistance:** ChatGPT expanded the mathematical explanations, checked arithmetic, structured this Markdown note, and distinguished teaching examples from empirical evidence.
- **External references:** None consulted for this draft. Add authoritative references when implementing or extending these concepts.

---

**MATH-03 completion boundary:** The conceptual exercises are complete. Coding, dataset design, classifier evaluation, and calibration experiments remain future engineering work. Do not report the illustrative probabilities as benchmark results.
