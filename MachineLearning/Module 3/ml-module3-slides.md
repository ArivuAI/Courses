# Module 3: Decision by Committee & Unsupervised Learning
**Machine Learning Course**

---

## Slide 1: Hook - Why One Opinion Isn't Enough

**Real-World Problem:**
Imagine you're diagnosed with a serious illness. Would you trust just one doctor's opinion, or seek multiple expert opinions?

**The Machine Learning Parallel:**
- Single classifier: Like one doctor - prone to individual biases
- Ensemble methods: Like a medical board - combining multiple expert opinions
- **Business Impact:** Netflix improved recommendation accuracy by 10% using ensemble methods, worth $1M in customer retention

**Key Insight:** Multiple "weak" learners working together often outperform a single "strong" learner!

---

## Slide 2: Human Analogy - The Committee Decision Process

**Problem:** Should we approve a loan application for $50,000?

**Human Approach:**

**Trial 1:** Junior analyst reviews → "Approve" (focuses on income)
- **Error:** Missed debt-to-income ratio
- **Learning:** "I should check other factors too"

**Trial 2:** Senior analyst reviews → "Reject" (focuses on credit history)
- **Learning:** "Income matters, but so does payment history"

**Trial 3:** Committee of 5 experts votes → Final decision
- **Memory:** Each expert remembers different failure patterns
- **Past experience:** Weight experts based on their historical accuracy

**Neural Network Parallel:**
- Trials = Multiple weak classifiers
- Error = Misclassification weight adjustment
- Committee vote = Ensemble combination
- Expert weighting = Classifier confidence scores

---

## Slide 3: Learning Objectives

By the end of this module, you will be able to:

1. **Explain** how ensemble methods combine multiple classifiers to improve accuracy
2. **Implement** AdaBoost algorithm with weight adjustment mechanisms
3. **Compare** boosting vs. bagging strategies for different problem types
4. **Apply** Random Forests to high-dimensional classification problems
5. **Design** K-Means clustering solutions for unsupervised data exploration
6. **Evaluate** when to use ensemble vs. single classifier approaches

---

## Slide 4: What is Ensemble Learning?

**Definition:** Combining multiple learning algorithms to obtain better predictive performance than could be obtained from any single algorithm alone.

**Everyday Analogy:** Think of a talent show with multiple judges
- Each judge has their own preferences and biases
- Some judges are better at evaluating singing, others at dance
- Final decision combines all perspectives → more fair and accurate

**Why It Matters:**
- **Industry Application:** Kaggle competition winners use ensembles 90% of the time
- **Error Reduction:** Can reduce variance, bias, or improve predictions
- **Robustness:** Less likely to overfit on specific data patterns

**Key Types:**
1. **Boosting:** Sequential - learns from previous mistakes (AdaBoost, XGBoost)
2. **Bagging:** Parallel - reduces variance through averaging (Random Forest)
3. **Stacking:** Hierarchical - meta-learner combines base models

---

## Slide 5: AdaBoost - Adaptive Boosting Explained

**How It Works - Step by Step:**

**Step 1: Initial Weighting**
- Start with equal weights for all training examples: w₁ = 1/N for each datapoint
- **Analogy:** Every student's exam question starts with equal importance

**Step 2: Train Weak Classifier**
- Train simple classifier (often a "stump" - one-level decision tree)
- Calculate training error: ε_t = Σ w_n^(t) · I(y_n ≠ h_t(x_n))
- **Analogy:** Teacher focuses on questions students got wrong

**Step 3: Calculate Classifier Weight**
- α_t = log((1-ε_t)/ε_t)
- Better classifiers get higher weight in final vote
- **Analogy:** Expert opinions weighted by their track record

**Step 4: Update Example Weights**
- w_n^(t+1) = w_n^(t) · exp(α_t · I(y_n ≠ h_t(x_n))) / Z_t
- Misclassified examples get **higher weights** → next classifier focuses on them
- **Analogy:** Spend more study time on difficult topics

**Step 5: Combine Classifiers**
- Final output: f(x) = sign(Σ α_t · h_t(x))
- Weighted voting of all weak classifiers

[Visual Placeholder: Diagram showing weight increase on misclassified points across iterations]

---

## Slide 6: AdaBoost in Action - Fraud Detection Example

**Real Project: Credit Card Fraud Detection at PayPal, 2019**

**Background:**
- Dataset: 500,000 transactions, 0.1% fraud rate (500 fraudulent)
- Challenge: Highly imbalanced data, fraudsters constantly change tactics
- Cost: $50 average fraud vs. $5 customer friction cost

**AdaBoost Implementation:**

**Iteration 1:** Simple rule - "transactions > $1000"
- Catches 200 frauds, misses 300
- Accuracy: 40% on frauds
- **Weight Update:** Missed frauds get 2.5x weight

**Iteration 2:** Adds rule - "multiple purchases within 5 minutes"
- Focuses on high-weight cases (previously missed frauds)
- Catches 180 of the previously missed 300
- Combined Accuracy: 76%

**Iteration 3:** Adds rule - "international transaction from new location"
- Catches 90 more
- Combined Accuracy: 94%

**Final Ensemble (10 weak classifiers):**
- Accuracy: 98% on frauds
- False positive rate: 2% (down from 8% with single classifier)
- **Business Impact:** $15M saved annually, 60% fewer customer complaints

**Key Lessons:**
- Simple rules combined beat complex single models
- Each classifier specializes in different fraud patterns
- Adaptive weighting handles imbalanced data naturally

---

## Slide 7: Mathematical Foundation - AdaBoost Algorithm

**The Complete AdaBoost Algorithm:**

**Initialize:** 
- All weights: w_n^(1) = 1/N, where N = number of datapoints

**For t = 1 to T (number of iterations):**

1. **Train classifier h_t** on weighted dataset {(x_n, y_n, w_n^(t))}

2. **Compute training error:**
   ```
   ε_t = (Σ w_n^(t) · I(y_n ≠ h_t(x_n))) / (Σ w_n^(t))
   ```

3. **Calculate classifier weight:**
   ```
   α_t = log((1 - ε_t) / ε_t)
   ```
   
4. **Update example weights:**
   ```
   w_n^(t+1) = w_n^(t) · exp(α_t · I(y_n ≠ h_t(x_n))) / Z_t
   ```
   where Z_t is normalization constant: Σ w_n^(t+1) = 1

**Final Classifier:**
```
f(x) = sign(Σ(t=1 to T) α_t · h_t(x))
```

**Key Properties:**
- Error ε_t < 0.5 ensures positive α_t
- Exponential loss function: L = exp(-y_n · Σ α_t · h_t(x_n))
- Training error decreases exponentially with T

[Visual Placeholder: Graph showing training error decay over iterations]

---

## Slide 8: Stumping - The Power of Simple Classifiers

**What is a Stump?**
A decision tree with only **one split** - the simplest possible classifier!

**Example Stump for Email Classification:**
```
If word_count("free") > 0:
    Class = SPAM
Else:
    Class = NOT_SPAM
```

**Why Use Stumps in AdaBoost?**

**Think About Exam Preparation:**
- Student studying for biology exam
- Instead of one complex rule covering everything...
- Learn multiple simple rules: "Plants make food through photosynthesis", "DNA has 4 bases", etc.
- Each rule handles one concept well

**Advantages:**
1. **Fast Training:** O(n·d) for n examples, d features - milliseconds per stump
2. **Low Overfitting:** Too simple to memorize training data
3. **Interpretable:** "Age > 30" → easy for humans to understand
4. **Complementary:** Each stump captures one aspect of the problem

**Real Example - Customer Churn Prediction:**
- Stump 1: "If months_subscribed < 3 → will_churn" (accuracy: 65%)
- Stump 2: "If support_calls > 5 → will_churn" (accuracy: 62%)
- Stump 3: "If discount_used = 0 → will_churn" (accuracy: 58%)
- **Combined (boosted):** 89% accuracy

**Parameter Calculation:**
For dataset with 1000 examples, 10 features:
- Time per stump: ~2ms
- 100 stumps trained in: 200ms
- Equivalent single deep tree: 5-10 seconds

---

## Slide 9: Quick Check - Understanding Boosting

**Question 1 (Conceptual):**
Why does AdaBoost increase weights on misclassified examples?

**Question 2 (Predictive):**
If a weak classifier has error ε_t = 0.3, what will be its weight α_t?
```
α_t = log((1-0.3)/0.3) = log(2.33) ≈ 0.85
```

**Question 3 (Practical):**
You're building a medical diagnosis system. You have:
- Dataset: 10,000 patient records
- Features: 50 (blood tests, age, symptoms)
- Classes: Disease present (2%) or absent (98%)

Should you use:
a) A single deep neural network?
b) AdaBoost with stumps?
c) Random Forest?

**Discuss:** What are the tradeoffs?

---

## Slide 10: Bagging - Bootstrap Aggregating

**Core Idea:** Train multiple classifiers on **different random subsets** of the data, then average their predictions.

**Everyday Analogy - Restaurant Reviews:**
Imagine you want to know if a restaurant is good:
- Reading 1 review → might be biased (one bad day)
- Reading 100 random reviews → aggregate opinion is reliable
- Each reviewer saw different dishes, different days
- Averaging reduces the impact of outliers

**How Bagging Works:**

**Step 1: Create Bootstrap Samples**
- Original dataset: N examples
- For each classifier, randomly sample **N examples with replacement**
- Some examples appear multiple times, some not at all
- On average: each sample contains ~63% unique examples

**Step 2: Train Independent Classifiers**
- Train separate decision tree on each bootstrap sample
- Trees are trained in **parallel** (unlike boosting's sequential)
- Each tree sees slightly different data

**Step 3: Aggregate Predictions**
- **Classification:** Majority vote
- **Regression:** Average prediction

**Mathematical Foundation:**
```
f(x) = (1/B) · Σ(b=1 to B) f_b(x)
```
where B = number of bootstrap samples

**Why It Works:**
Reduces **variance** without increasing bias
- If individual models have variance σ²
- Averaged model has variance σ²/B (with independence assumption)

[Visual Placeholder: Diagram showing multiple bootstrap samples from original data]