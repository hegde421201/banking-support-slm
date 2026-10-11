# Arithmetic, algebra, and functions
```
Note ID: MATH-01
Tags: math, foundations
Status: Completed - mathematical foundations
Written by: Ganesh Rama Hegde
Last updated: 11-Oct-2026
Suggested time: Week 1, Day 1: notation, functions, and essential algebra; 1-2 hours
```

## Topics to cover

Model notation, variables, functions, summation notation, and algebraic rearrangement.
Use ratios, percentages, and averages as a quick check only if needed.

## Explanation

### 1. Variables

A variable represents a value.

Example:

```math
x=1
```

In a banking classifier, $x$ can represent whether a word occurs in a customer message.

### 2. Functions

A function takes an input and calculates an output.

```math
y=f(x)
```

Example:

```math
f(x)=3x+2
```

If $x=1$:

```math
f(1)=3(1)+2=5
```

### 3. Weights and bias

A classifier can use more than one input feature.

```math
s=w_1x_1+w_2x_2+b
```

Where:

- $s$ is the calculated score.
- $x_1,x_2$ are input features.
- $w_1,w_2$ are weights.
- $b$ is the bias.

A weight controls the size and direction of a feature's contribution to the score. A positive weight increases the score when the feature is positive. A negative weight decreases it.

A bias adds a constant value.

### 4. Summation notation

Summation notation gives us a short way to write repeated multiplication and addition.

```math
\sum_{i=1}^{3}a_i=a_1+a_2+a_3
```

For example:

```math
\sum_{i=1}^{3}a_i=2+4+1=7
```

A classifier with many features can use:

```math
s=\sum_{i=1}^{n}w_ix_i+b
```

- $i$ identifies the current feature.
- $i=1$ means start with the first feature.
- $n$ is the total number of input features.
- $\sum$ means add the terms.

### 5. Algebraic rearrangement

Algebraic rearrangement lets us isolate an unknown value.

Example:

```math
s=wx+b
```

Subtract $b$ from both sides:

```math
s-b=wx
```

If $x\neq0$, divide both sides by $x$:

```math
w=\frac{s-b}{x}
```

This equation calculates the weight when the other values are known.

These are basic mathematical tools. We will use them to understand classification and model training.

## Worked example

### Problem

Calculate a Card Delivery intent score for two banking support messages.

We use three binary input features:

| Feature | Meaning |
|---|---|
| $x_1$ | Message contains "card" |
| $x_2$ | Message contains "arrived" |
| $x_3$ | Message contains "activate" |

Each feature has a value of 1 if the word is present. Otherwise, its value is 0.

### Scoring function

```math
s=\sum_{i=1}^{3}w_ix_i+b
```

For this example, we assign:

```math
w_1=2,\quad w_2=4,\quad w_3=-1,\quad b=1
```

These are manually selected teaching values. They are not trained model parameters.

### Case A — Card delivery request

Customer message:

"My debit card has not arrived."

Feature values:

```math
x_1=1,\quad x_2=1,\quad x_3=0
```

Expand the summation:

```math
s=w_1x_1+w_2x_2+w_3x_3+b
```

Substitute the values:

```math
s=2(1)+4(1)+(-1)(0)+1
```

```math
s=2+4+0+1=7
```

The Card Delivery score is **7**.

### Case B — Card activation request

Customer message:

"Activate my debit card."

Feature values:

```math
x_1=1,\quad x_2=0,\quad x_3=1
```

Substitute the values:

```math
s=2(1)+4(0)+(-1)(1)+1
```

```math
s=2+0-1+1=2
```

The Card Delivery score is **2**.

### Interpretation

The first message receives a higher Card Delivery score than the second message.

The scoring function uses the same weights and bias for both messages.

The score is not a probability. It is not sufficient to determine the predicted intent because we have not calculated scores for the other intent categories.

The word-presence features also do not fully represent sentence meaning or negation.

### What I learned

1. A scoring function can use multiple input features.
2. Summation notation represents repeated multiplication and addition.
3. We can use the same scoring function for different messages.
4. Different feature values can produce different scores.
5. A classification score is not the same as a probability.

## Connection to this project

The Banking Support SLM project processes customer messages to identify their intent and prepare an appropriate response.

The planned system has four main stages:

1. **Input processing:** Convert a customer message into numerical features.
2. **Intent classification:** Calculate scores for possible banking intents and select a predicted intent.
3. **Policy selection:** Select an allowed action based on the predicted intent and available context.
4. **Reply generation:** Produce a response using a template or a small language model.

The mathematical function studied in MATH-01 belongs to the intent classification stage.

A simple classifier can calculate an intent score using:

```math
s=\sum_{i=1}^{n}w_ix_i+b
```

The input features represent information extracted from the message.

The weights and bias determine the calculated score.

In this lesson, the weights and bias were selected manually. A trained classifier must learn suitable parameters from training data.

The classifier score is not itself a probability or a verified banking fact.

The policy engine must apply banking rules before the reply generator prepares a response.

### Why this matters

The project can compare a template-based reply generator with an SLM-based reply generator while keeping classification and policy decisions constant.

This separation helps identify whether a change in response quality comes from the reply generator or an earlier component.

MATH-01 provides the algebra needed to understand the classifier. It does not yet explain how the classifier learns its weights or how the SLM generates text.

## Code and evidence links

- Code: Not implemented as part of this mathematics lesson.
- Test or result: Manual calculations completed during the learning session. No automated test was executed for MATH-01.
- Related requirement or research question: Banking intent classification and the comparison of template-based and SLM-based reply generation. Add the exact requirement ID after verifying it in the project documentation.

## Checks I completed

### Check 1 — Function evaluation

Given:

```math
f(x)=3x+2
```

For $x=1$:

```math
f(1)=3(1)+2=5
```

My answer was 5. The calculation was reviewed and confirmed.

### Check 2 — Weighted score with bias

Given:

```math
s=3x_1+5x_2-2
```

For $x_1=1$ and $x_2=0$:

```math
s=3(1)+5(0)-2=1
```

My answer was 1. The calculation was reviewed and confirmed.

### Check 3 — Three-feature classification score

Given:

```math
s=2x_1+4x_2-x_3+1
```

For $x_1=1$, $x_2=0$, and $x_3=1$:

```math
s=2(1)+4(0)-1+1=2
```

My answer was 2. The calculation was reviewed and confirmed.

### Check 4 — Architecture understanding

Question: Can a classifier confirm that a customer's card has been blocked?

My answer: No.

The classifier identifies the intent. The policy engine determines the permitted action. An authorized banking system executes the operation and confirms the result.

The reply generator must not claim that an operation succeeded without confirmation.

## Questions, answers, and corrections

### 1. Is a classification score a probability?

No. The scoring function calculates a numerical value. We cannot interpret that value directly as a probability.

### 2. Are the weights in these examples learned?

No. The weights and bias were selected manually for the exercises.

A trained classifier learns its parameters from training data.

### 3. Can a classifier perform banking operations?

No. Classification and execution are separate responsibilities.

### 4. What are the limitations of the examples?

The examples use binary word-presence features.

They do not fully represent word order, negation, or sentence meaning.

### 5. What are the inputs and outputs of a function?

A function receives one or more inputs and calculates an output according to a defined rule.

In a banking classifier, the inputs can be numerical features extracted from a customer message.

The output can be a classification score.

For example:

```math
s=\sum_{i=1}^{n}w_ix_i+b
```

The function multiplies each feature by its weight, adds the products, and adds the bias.

### 6. How do you calculate a success rate?

A success rate measures the proportion of successful outcomes.

```math
\text{Success Rate}=\frac{\text{Successful Outcomes}}{\text{Total Outcomes}}\times100
```

For example, if a system correctly handles 80 out of 100 requests:

```math
\text{Success Rate}=\frac{80}{100}\times100=80\%
```

The definition of a successful outcome must be specified before evaluation.

This is a worked illustration, not a measured result from the Banking Support SLM project.

## Sources and assistance

- Original MATH-01 learning template: Codex.
- Mathematical explanations and banking examples: GPT-6.
- Manual exercise answers: Calculated by the learner and reviewed with ChatGPT.
- Automated implementation and experimental results: Not produced during this lesson.

The learning notes are educational material. They are not evidence that a trained classifier or SLM has achieved the stated example results.