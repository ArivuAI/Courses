# Sequential Bayesian Inference - Quick Reference Guide

## 📐 Core Formulas

### Bayes' Theorem (Single Update)
```
P(H | E) = P(E | H) × P(H) / P(E)
```

**Components**:
- **P(H | E)**: Posterior probability (updated belief after evidence)
- **P(E | H)**: Likelihood (how well hypothesis explains evidence)
- **P(H)**: Prior probability (initial belief before evidence)
- **P(E)**: Evidence probability (normalizing constant)

### Sequential Bayesian Update
```
P(H | E₁, E₂, ..., Eₙ) = P(Eₙ | H) × P(H | E₁, ..., Eₙ₋₁) / P(Eₙ)
```

**Key Insight**: Posterior from step N becomes prior for step N+1!

### Expanded Form
```
Step 1: P(H | E₁) = P(E₁ | H) × P(H) / P(E₁)
Step 2: P(H | E₁, E₂) = P(E₂ | H) × P(H | E₁) / P(E₂)
Step 3: P(H | E₁, E₂, E₃) = P(E₃ | H) × P(H | E₁, E₂) / P(E₃)
...
```

### Normalization
```
P(H | E) = [P(E | H) × P(H)] / Σₕ [P(E | h) × P(h)]
```

Ensures probabilities sum to 1.

### Log-Space (for numerical stability)
```
log P(H | E) = log P(E | H) + log P(H) - log P(E)
```

Prevents underflow from multiplying many small numbers.

---

## 🔄 Implementation Steps

### Step 1: Initialize Prior
```python
def initialize_prior(hypotheses):
    """Start with uniform distribution"""
    n = len(hypotheses)
    return {h: 1.0/n for h in hypotheses}
```

### Step 2: Single Bayesian Update
```python
def bayesian_update(prior, evidence, likelihood_table):
    """Update probabilities with new evidence"""
    posterior = {}
    
    # Calculate unnormalized posterior
    for hypothesis in prior:
        likelihood = likelihood_table[hypothesis][evidence]
        posterior[hypothesis] = prior[hypothesis] * likelihood
    
    # Normalize
    total = sum(posterior.values())
    for hypothesis in posterior:
        posterior[hypothesis] /= total
    
    return posterior
```

### Step 3: Sequential Inference
```python
def sequential_inference(evidence_sequence, likelihood_table):
    """Process evidence sequentially"""
    current_probs = initialize_prior(hypotheses)
    history = [current_probs.copy()]
    
    for evidence in evidence_sequence:
        current_probs = bayesian_update(current_probs, evidence, likelihood_table)
        history.append(current_probs.copy())
    
    return history
```

### Step 4: Visualize Evolution
```python
def plot_probability_evolution(history, hypotheses):
    """Plot how probabilities change over time"""
    for hypothesis in hypotheses:
        probs = [step[hypothesis] for step in history]
        plt.plot(probs, label=hypothesis, marker='o')
    
    plt.xlabel('Step')
    plt.ylabel('Probability')
    plt.legend()
    plt.show()
```

---

## 🎯 Key Concepts

### 1. Prior Probability
**Definition**: Initial belief before observing any evidence.

**Types**:
- **Uniform Prior**: No preference, all hypotheses equally likely
- **Informative Prior**: Based on domain knowledge or previous data
- **Empirical Prior**: Estimated from historical data

**Example**:
```python
# Uniform prior
P(Flu) = P(COVID) = P(Cold) = 1/3 = 0.333

# Informative prior (based on season)
P(Flu) = 0.40  # Winter, flu season
P(COVID) = 0.35
P(Cold) = 0.25
```

### 2. Likelihood
**Definition**: Probability of observing evidence given hypothesis is true.

**Formula**: P(Evidence | Hypothesis)

**Example**:
```python
# P(Fever | Flu) = 0.85
# P(Fever | COVID) = 0.80
# P(Fever | Cold) = 0.20
```

### 3. Posterior Probability
**Definition**: Updated belief after observing evidence.

**Formula**: P(Hypothesis | Evidence)

**Example**:
```python
# After observing fever:
P(Flu | Fever) = 0.45
P(COVID | Fever) = 0.42
P(Cold | Fever) = 0.13
```

### 4. Evidence Accumulation
**Definition**: Combining multiple pieces of evidence sequentially.

**Process**:
1. Start with prior
2. Observe evidence E₁ → Calculate posterior P(H | E₁)
3. Use P(H | E₁) as new prior
4. Observe evidence E₂ → Calculate posterior P(H | E₁, E₂)
5. Repeat...

### 5. Convergence
**Definition**: Probabilities stabilize as more evidence accumulates.

**Properties**:
- More evidence → stronger conclusions
- Uncertainty decreases over time
- Eventually converges to true hypothesis (with enough evidence)

---

## 📊 Common Patterns

### Pattern 1: Confirming Evidence
Evidence that increases probability of leading hypothesis.

```
Day 1: P(Flu) = 0.40, P(COVID) = 0.35
Observe: Body Aches (strong flu indicator)
Day 2: P(Flu) = 0.65, P(COVID) = 0.25
```

### Pattern 2: Disconfirming Evidence
Evidence that decreases probability of leading hypothesis.

```
Day 1: P(Flu) = 0.65, P(COVID) = 0.25
Observe: Loss of Taste (strong COVID indicator)
Day 2: P(Flu) = 0.30, P(COVID) = 0.60
```

### Pattern 3: Ambiguous Evidence
Evidence that doesn't strongly favor any hypothesis.

```
Day 1: P(Flu) = 0.50, P(COVID) = 0.30
Observe: Fatigue (common to both)
Day 2: P(Flu) = 0.48, P(COVID) = 0.32
```

### Pattern 4: Rapid Convergence
Strong evidence quickly resolves uncertainty.

```
Day 1: P(Flu) = 0.33, P(COVID) = 0.33, P(Cold) = 0.33
Observe: Loss of Taste (very specific to COVID)
Day 2: P(Flu) = 0.05, P(COVID) = 0.90, P(Cold) = 0.05
```

---

## 🔧 Code Snippets

### Load Sequential Data
```python
import json

with open('data/sequential_diagnosis_data.json', 'r') as f:
    data = json.load(f)

cases = data['sequential_patient_cases']
cond_probs = data['conditional_probabilities']
```

### Process Single Patient
```python
patient = cases[0]
symptom_sequence = patient['symptom_sequence']

prob_history = sequential_inference(symptom_sequence)

for step in prob_history:
    print(f"Day {step['day']}: {step['evidence']}")
    for disease, prob in step['probabilities'].items():
        print(f"  P({disease}) = {prob:.4f}")
```

### Calculate Confidence
```python
def get_confidence(probabilities):
    """Return probability of most likely hypothesis"""
    return max(probabilities.values())

def get_prediction(probabilities):
    """Return most likely hypothesis"""
    return max(probabilities, key=probabilities.get)

# Usage
confidence = get_confidence(current_probs)
prediction = get_prediction(current_probs)
print(f"Prediction: {prediction} ({confidence:.2%} confidence)")
```

### Early Stopping
```python
def should_stop(probabilities, threshold=0.90):
    """Decide if we have enough evidence"""
    max_prob = max(probabilities.values())
    return max_prob >= threshold

# Usage
for step in prob_history:
    if should_stop(step['probabilities']):
        print(f"Confident enough at Day {step['day']}")
        break
```

### Compare Evidence Orders
```python
def compare_orderings(symptoms):
    """Test different evidence orderings"""
    import itertools
    
    results = []
    for ordering in itertools.permutations(symptoms):
        history = sequential_inference(ordering)
        final_probs = history[-1]['probabilities']
        results.append({
            'order': ordering,
            'final': final_probs
        })
    
    return results
```

---

## ⚠️ Common Pitfalls

### 1. Forgetting to Normalize
**Problem**: Probabilities don't sum to 1
```python
# WRONG
posterior = {h: prior[h] * likelihood[h] for h in hypotheses}

# CORRECT
posterior = {h: prior[h] * likelihood[h] for h in hypotheses}
total = sum(posterior.values())
posterior = {h: posterior[h]/total for h in hypotheses}
```

### 2. Numerical Underflow
**Problem**: Multiplying many small probabilities → 0
```python
# WRONG
prob = 0.1 * 0.1 * 0.1 * ... * 0.1  # Eventually becomes 0

# CORRECT (use log space)
log_prob = log(0.1) + log(0.1) + ... + log(0.1)
prob = exp(log_prob)
```

### 3. Ignoring Conditional Independence
**Problem**: Assuming evidence is independent when it's not
```python
# WRONG (if symptoms are correlated)
P(Fever, Cough | Flu) = P(Fever | Flu) × P(Cough | Flu)

# CORRECT (if symptoms are correlated)
P(Fever, Cough | Flu) = P(Fever | Flu) × P(Cough | Flu, Fever)
```

### 4. Using Wrong Prior
**Problem**: Starting with biased or incorrect prior
```python
# WRONG (if no domain knowledge)
prior = {'Flu': 0.90, 'COVID': 0.05, 'Cold': 0.05}

# CORRECT (uniform prior)
prior = {'Flu': 0.33, 'COVID': 0.33, 'Cold': 0.33}
```

---

## 🚀 Performance Tips

### 1. Use Vectorization
```python
# SLOW (loop)
for h in hypotheses:
    posterior[h] = prior[h] * likelihood[h]

# FAST (vectorized)
import numpy as np
posterior = np.array(prior) * np.array(likelihood)
```

### 2. Cache Computations
```python
# Cache likelihood tables
likelihood_cache = {}

def get_likelihood(symptom, disease):
    key = (symptom, disease)
    if key not in likelihood_cache:
        likelihood_cache[key] = compute_likelihood(symptom, disease)
    return likelihood_cache[key]
```

### 3. Early Stopping
```python
# Stop when confident enough
if max(probabilities.values()) > 0.95:
    break  # No need to process more evidence
```

### 4. Approximate Inference
```python
# For large networks, use sampling
from pgmpy.sampling import GibbsSampling

sampler = GibbsSampling(model)
samples = sampler.sample(size=1000)
```

---

## 📚 Best Practices

1. ✅ **Always normalize** probabilities after each update
2. ✅ **Use log probabilities** for numerical stability
3. ✅ **Validate CPTs** ensure they sum to 1
4. ✅ **Track history** to understand probability evolution
5. ✅ **Set decision thresholds** for early stopping
6. ✅ **Visualize results** to gain insights
7. ✅ **Test edge cases** (all evidence, no evidence, conflicting evidence)
8. ✅ **Document assumptions** (conditional independence, etc.)

---

## 🔗 Useful Links

- [Bayes' Theorem Explained](https://en.wikipedia.org/wiki/Bayes%27_theorem)
- [Sequential Bayesian Updating](https://www.probabilitycourse.com/chapter9/9_1_2_bayesian_updating.php)
- [pgmpy Documentation](https://pgmpy.org/)
- [Bayesian Networks Tutorial](https://www.cs.ubc.ca/~murphyk/Bayes/bnintro.html)

---

**Quick Reference Version 1.0**  
*Last Updated: 2024*

