# Vectors, dot products, and TF-IDF
Note ID: MATH-02
Tags: math, text-features
Status: Completed — manual mathematical exercises; implementation pending
Written by: Ganesh Rama Hegde
Last updated: 16-Oct-2026
Suggested time: Week 1, Day 2: vectors, dot products, and TF-IDF; 4-5 hours

## Topics to cover

Vectors, matching dimensions, dot products, word counts, term frequency, inverse document frequency, and TF-IDF. Matrix operations are outside the scope of this note.

## Explanation

Objective: Explain how a banking support message becomes numerical input for a classifier.

### 1. Vectors and binary features

A vector is an ordered collection of numbers.

In the Banking Support SLM project, a vector can represent features extracted from a customer message.

Consider the vocabulary:

```text
V = [card, arrived, activate]
```

Customer message:

"My debit card has not arrived."

The feature vector is:

```math
\mathbf{x}=[1,1,0]
```

The vector has three dimensions because it contains three elements.

The first element represents "card". The second represents "arrived". The third represents "activate".

#### Limitation

Binary word-presence vectors do not fully represent sentence meaning.

For example:

"My card has arrived."

"My card has not arrived."

Both messages produce the same vector when the vocabulary contains only "card", "arrived", and "activate".

The vector does not capture the negation in the second message.

This is one reason to investigate more informative text representations.

### 2. Dot product

A dot product combines two vectors of the same length.

It multiplies the elements at corresponding positions and adds the products.

For two three-dimensional vectors:

```math
\mathbf{x}=[x_1,x_2,x_3]
```

```math
\mathbf{w}=[w_1,w_2,w_3]
```

The dot product is:

```math
\mathbf{w}\cdot\mathbf{x}=w_1x_1+w_2x_2+w_3x_3
```

The result is a scalar, which is one number.

#### Worked dot-product example

Customer message:

"Activate my debit card."

Vocabulary:

`[card, arrived, activate]`

Input vector:

```math
\mathbf{x}=[1,0,1]
```

Manually selected weight vector:

```math
\mathbf{w}=[2,4,-1]
```

Calculate the dot product:

```math
\mathbf{w}\cdot\mathbf{x}=2(1)+4(0)+(-1)(1)
```

```math
\mathbf{w}\cdot\mathbf{x}=1
```

The dot product is 1.

If the classifier uses a bias of 1, the score becomes:

```math
s=\mathbf{w}\cdot\mathbf{x}+b=1+1=2
```

The dot product combines feature values and weights. The bias is added separately.

### 3. Term Frequency (TF)

Term Frequency measures how often a term occurs in a document.
In this project, one customer message can be treated as one document.

There are different definitions of Term Frequency. For this lesson, we use raw term frequency.

```math
\operatorname{TF}(t,d)=\operatorname{count}(t,d)
```

Where:

- $t$ is the term.
- $d$ is the document.
- $\operatorname{count}(t,d)$ is the number of occurrences of the term in the document.

#### Banking support example

Customer message:

"My card is missing. I cannot find my card."

After converting the text to lowercase and removing punctuation, we split it into words:

- "card" occurs twice.
- "missing" occurs once.
- "activate" does not occur.

Therefore:

```math
\operatorname{TF}(\text{card},d)=2
```

```math
\operatorname{TF}(\text{missing},d)=1
```

```math
\operatorname{TF}(\text{activate},d)=0
```

For the vocabulary `[card, missing, activate]`, the raw term-frequency vector is:

```math
\mathbf{x}=[2,1,0]
```

A binary vector records word presence. A raw term-frequency vector records word counts.

Raw term frequency does not measure whether a term is common or rare across the full dataset.

That limitation motivates Inverse Document Frequency (IDF), which we will study next.

### 4. Inverse Document Frequency (IDF)

Inverse Document Frequency measures how uncommon a term is across a collection of documents.

In the Banking Support SLM project, each customer message can be treated as a document.

For this lesson, we use the unsmoothed IDF formula:

```math
\operatorname{IDF}(t)=\ln\left(\frac{N}{\operatorname{DF}(t)}\right)
```

Where:

-  $t$ is a term.
-  $N$ is the total number of documents.
- $\operatorname{DF}(t)$ is the number of documents containing the term at least once.
- $\ln$ is the natural logarithm.

The formula requires a positive document frequency.

#### Banking support example

Assume a hypothetical dataset contains 10 customer messages.

The word "card" appears in 8 documents.
The word "fraud" appears in 2 documents.

For "card":

```math
\operatorname{IDF}(\text{card})=\ln(10/8)\approx0.223
```

For "fraud":

```math
\operatorname{IDF}(\text{fraud})=\ln(10/2)\approx1.609
```

The word "fraud" has a higher IDF because it occurs in fewer documents.

#### Interpretation

A common term has a lower IDF.
A rare term has a higher IDF.
IDF does not directly measure the semantic importance of a word.

For the research project, document-frequency statistics must be calculated from training data only. The example values above are hypothetical and are not experimental results.

### 5. TF-IDF

TF-IDF combines Term Frequency and Inverse Document Frequency.
Term Frequency measures how often a term occurs in one document.
Inverse Document Frequency measures how uncommon that term is across a document collection.

For this lesson, we use raw TF and unsmoothed IDF:

```math
\operatorname{TFIDF}(t,d)=\operatorname{TF}(t,d)\times\operatorname{IDF}(t)
```

#### Banking support example

Customer message:

"My card was charged twice. My card was charged again."

Assume a hypothetical training collection of 100 messages.

| Term | TF | DF | IDF | TF-IDF |
|---|---:|---:|---:|---:|
| card | 2 | 80 | 0.223 | 0.446 |
| charged | 2 | 20 | 1.609 | 3.219 |
| twice | 1 | 10 | 2.303 | 2.303 |

The displayed IDF values are rounded; TF-IDF results below use the full-precision logarithm before rounding.

For "charged":

```math
\operatorname{TFIDF}(\text{charged},d)
=2\times\ln(100/20)
```

```math
=2\times1.609438\approx3.219
```

For the vocabulary `[card, charged, twice]`, the TF-IDF vector is approximately:

```math
\mathbf{x}=[0.446,3.219,2.303]
```

#### Connection to the classifier

A TF-IDF vector can be used as input to a linear classifier.

```math
s=\mathbf{w}\cdot\mathbf{x}+b
```

The vector $\mathbf{x}$ contains TF-IDF feature values.

The vector $\mathbf{w}$ contains classifier model weights.

The classifier weights are separate from the TF-IDF values.

#### Limitations

- TF-IDF does not directly represent sentence meaning.
- A high TF-IDF value does not guarantee that a term identifies the correct banking intent.
- IDF statistics must be learned from the training collection to avoid test-data leakage.
- This lesson uses raw TF and unsmoothed IDF. Production libraries can use different defaults, including smoothing and vector normalization.

The document frequencies in this example are hypothetical. They are not experimental results.


## Worked example

Customer message: "My loan payment failed. My loan payment is overdue."

Vocabulary: `[loan, payment, overdue]`.

The raw term-frequency vector is:

```math
\mathbf{x}_{\mathrm{TF}}=[2,2,1]
```

Assume the following *illustrative*, already-rounded IDF values from a hypothetical training collection:

| Term | Raw TF | Given IDF | TF × IDF |
|---|---:|---:|---:|
| loan | 2 | 1.609 | 3.218 |
| payment | 2 | 0.693 | 1.386 |
| overdue | 1 | 2.303 | 2.303 |

Using the supplied three-decimal IDF values, the TF-IDF vector is:

```math
\mathbf{x}_{\mathrm{TFIDF}}=[3.218,1.386,2.303]
```

These are manual teaching calculations, not measured dataset results. In an actual pipeline, IDF would be fitted on training documents and the precise calculation would depend on the vectorizer configuration.

## Connection to this project

The Banking Support SLM system first identifies a customer's intent, then applies a policy, and finally prepares a reply using either a template or an SLM. Vectors and TF-IDF provide one possible numerical representation for a **traditional intent-classification baseline**.

A linear classifier can use the TF-IDF vector in the score:

```math
s=\mathbf{w}\cdot\mathbf{x}+b
```

The feature values in `x` are distinct from the classifier's learned model weights in `w`. Each intent category can have its own weights and bias. Scores are not automatically probabilities, and neither scores nor generated text authorize banking actions.

This project can compare template-based and SLM-based replies while keeping the classifier and policy fixed. TF-IDF is not itself the SLM's tokenization or embedding method; it is a useful classical baseline representation.

IDF must be fitted using **training data only**. Validation and test messages must be transformed with the already-fitted vocabulary and IDF statistics to avoid data leakage.

## Code and evidence links

- Code: No code was implemented as part of this mathematics note; add a verified relative repository path when an implementation exists.
- Test or result: Five manual exercises were checked in the learning session. No automated MATH-02 test was executed or verified here.
- Related requirement or research question: Intent-classification baseline and the comparison of template-based versus SLM-based replies. Add the exact project requirement ID after verifying it in the repository.

## Questions, answers, and corrections

### How does a customer message become a vector?

Define a vocabulary with a fixed word order. Apply a feature rule, such as binary word presence, raw word counts, or TF-IDF, to produce one number for each vocabulary term.

### How does a dot product produce a classification score?

Multiply each input feature by its corresponding classifier weight, add the products, and then add the bias. The result is a score, not necessarily a probability.

### Why is document frequency different from term frequency?

TF counts occurrences within one document. DF counts how many documents contain the term at least once, even if the term repeats within one document.

### Does a high TF-IDF value mean a word is important to the customer's intent?

Not necessarily. It indicates a combination of within-message frequency and rarity across the training collection. It does not establish semantic relevance or policy correctness.

### What are the limitations of this representation?

Simple bag-of-words features lose word order and may fail to capture negation. TF-IDF is useful as a classical baseline, but it does not provide full language understanding.

### What must be checked when using a real TF-IDF library?

The library's TF definition, IDF smoothing, text preprocessing, vocabulary, and vector normalization. Its numerical output may differ from the unsmoothed teaching examples.

### Why do we need a bias?

Recall our linear classifier:
```math
\boxed{s=w_1x_1+w_2x_2+b}
```

The bias $b$ is a constant that the classifier adds to the weighted sum.

Its main purpose is to let the classifier adjust its score even when the input features stay the same.

Banking example: Card Activation

Suppose we want to calculate a score for the intent CARD_ACTIVATION.

We define two features:
- $x_1=1$ if the message contains activate.
- $x_2=1$ if the message contains card.

Assume these illustrative weights:

```math
w_1=3,\quad w_2=1
```

Our scoring function without bias is:
```math
s=3x_1+x_2
```

Now consider three messages.

| Customer message | Features | Score without bias |
|----------|----------|----------|
| "Hello"  | [0,0]    | 0        |
| "My card arrived"   | [0,1]    | 1 |
| "Activate my card"  | [1,1]  | 4     |

Suppose our illustrative decision rule is:
```math
s>0\Rightarrow\text{Predict CARD\_ACTIVATION}
```

That rule incorrectly predicts Card Activation for "My card arrived."
We could change the threshold. 
But we can also use a bias.

Let:
```math
b=-2
```

Our scoring function becomes:
```math
\boxed{s=3x_1+x_2-2}
```

| Customer message | Score with bias | Prediction using $s>0$ |
|----------|----------|----------|
| "Hello"  | -2    | Not activation    |
| "My card arrived"   | -1   | Not activation |
| "Activate my card"  | 2  | Activation     |

Now the example behaves as intended.

What did the bias actually do?

It shifted every score downward by 2.

The evidence provided by the word activate must now be strong enough to overcome that negative starting score.

One mathematical insight: for a linear classifier with a fixed zero threshold, adding a bias is equivalent to shifting the effective threshold.

**Remember**: Weights control how features influence the score. Bias controls the score's starting offset.

### What is a baseline, and why do we need one?

A baseline is a reference system against which we compare a more advanced system.

It answers a basic engineering question:
"Did our new approach actually improve the result?"

Example: Banking intent classification
Suppose we have 1,000 held-out banking messages.
The following numbers are hypothetical.

| Model | Correct predictions | Accuracy |
|----------|----------|----------|
| Majority-class baseline | 180    | 18%    |
| TF-IDF + Logistic Regression   | 820   | 82% |
| TF-IDF + Linear SVM  | 850  | 85%     |

The majority-class baseline always predicts the most common intent. It provides a basic reference.
A classifier achieving 85% accuracy looks promising compared with 18%, but we would still need to examine per-intent performance, class imbalance, and errors.

A baseline is essential because complexity alone is not evidence of improvement.

### Why do we use the natural logarithm in IDF?
Recall:
```math
\operatorname{IDF}(t)=\ln\left(\frac{N}{\operatorname{DF}(t)}\right)
```

There are two separate questions here.

Why use a logarithm at all?
Suppose we have 100 documents.

| Term | Documents containing term | Ratio $N / DF$ | Natural log of ratio |
|----------|----------|----------|----------|
|card|	100|	1	|0|
|account	|50	|2	|0.693|
|loan |	20	|5|	1.609|
|fraud|	1	|100	|4.605|

Without a logarithm, the rare term fraud receives a value of 100, compared with 2 for account.
With a logarithm, those values become 4.605 and 0.693.
The logarithm compresses large ratios. Rare terms still receive larger values, but the difference is less extreme.

## Sources and assistance

- Initial research-note structure: Codex template.
- Mathematical explanations and illustrative banking examples: developed with ChatGPT GPT-6.
- Manual exercise answers: calculated by the learner and checked with ChatGPT.
- Code execution, dataset statistics, and automated experimental evidence: not claimed in this note.

All example corpus sizes, document frequencies, and weights are hypothetical unless explicitly identified as results from an actual experiment.
