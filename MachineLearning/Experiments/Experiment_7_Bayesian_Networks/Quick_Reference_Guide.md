# Bayesian Networks - Quick Reference Guide

## 📖 Core Concepts

### What is a Bayesian Network?

A **Bayesian Network** is a probabilistic graphical model that represents:
- **Variables** as nodes
- **Dependencies** as directed edges
- **Probabilities** via Conditional Probability Tables (CPTs)

**Key Property**: Forms a Directed Acyclic Graph (DAG) - no cycles allowed!

---

## 🧮 Mathematical Formulas

### 1. Bayes' Theorem (Foundation)

```
P(A | B) = P(B | A) × P(A) / P(B)
```

**In medical diagnosis context**:
```
P(Disease | Symptoms) = P(Symptoms | Disease) × P(Disease) / P(Symptoms)
```

**Components**:
- **P(Disease | Symptoms)**: Posterior probability (what we want)
- **P(Symptoms | Disease)**: Likelihood (from CPTs)
- **P(Disease)**: Prior probability (base rate)
- **P(Symptoms)**: Evidence (normalizing constant)

### 2. Joint Probability (Chain Rule)

```
P(X₁, X₂, ..., Xₙ) = ∏ᵢ P(Xᵢ | Parents(Xᵢ))
```

**Example**:
```
P(Season, Age, Disease, Fever) = 
    P(Season) × P(Age) × P(Disease | Season, Age) × P(Fever | Disease)
```

### 3. Marginalization

```
P(X) = Σᵧ P(X, Y)
```

**Example**:
```
P(Fever=Yes) = Σ_disease P(Fever=Yes, Disease=disease)
```

### 4. Conditional Independence

```
P(A, B | C) = P(A | C) × P(B | C)
```

**Example**: Given Disease, symptoms are conditionally independent:
```
P(Fever, Cough | Disease) = P(Fever | Disease) × P(Cough | Disease)
```

---

## 🔧 Implementation Steps

### Step 1: Define Network Structure

```python
# Define nodes
nodes = ['Season', 'Age', 'Vaccination', 'Disease', 'Fever', 'Cough']

# Define edges (parent → child)
edges = [
    ('Season', 'Disease'),
    ('Age', 'Disease'),
    ('Vaccination', 'Disease'),
    ('Disease', 'Fever'),
    ('Disease', 'Cough')
]
```

### Step 2: Define Prior Probabilities

```python
# For root nodes (no parents)
P_Season = {
    'Winter': 0.25,
    'Spring': 0.25,
    'Summer': 0.25,
    'Fall': 0.25
}
```

### Step 3: Define Conditional Probability Tables

```python
# P(Fever | Disease)
P_Fever_given_Disease = {
    'Flu': {'Yes': 0.85, 'No': 0.15},
    'COVID-19': {'Yes': 0.80, 'No': 0.20},
    'Common_Cold': {'Yes': 0.20, 'No': 0.80},
    'Allergies': {'Yes': 0.05, 'No': 0.95},
    'None': {'Yes': 0.02, 'No': 0.98}
}
```

### Step 4: Implement Inference

```python
def calculate_posterior(symptoms):
    posteriors = {}
    
    for disease in diseases:
        # Prior
        prior = P_Disease[disease]
        
        # Likelihood
        likelihood = 1.0
        for symptom, value in symptoms.items():
            likelihood *= P_Symptom_given_Disease[symptom][disease][value]
        
        # Unnormalized posterior
        posteriors[disease] = likelihood * prior
    
    # Normalize
    total = sum(posteriors.values())
    for disease in diseases:
        posteriors[disease] /= total
    
    return posteriors
```

---

## 📊 Types of Inference

### 1. Predictive (Causal) Inference

**Direction**: Cause → Effect  
**Question**: "If patient has Flu, what's probability of Fever?"

```python
# Given: Disease = Flu
# Find: P(Fever = Yes | Disease = Flu)
prob = P_Fever_given_Disease['Flu']['Yes']  # 0.85
```

### 2. Diagnostic (Evidential) Inference

**Direction**: Effect → Cause  
**Question**: "If patient has Fever, what's probability of Flu?"

```python
# Given: Fever = Yes
# Find: P(Disease = Flu | Fever = Yes)
# Use Bayes' Theorem
posterior = calculate_posterior({'Fever': 'Yes'})
prob_flu = posterior['Flu']
```

### 3. Intercausal (Explaining Away) Inference

**Direction**: Cause ← Effect → Cause  
**Question**: "If Fever explained by Flu, how does it affect COVID-19 probability?"

```python
# Given: Fever = Yes
# Find: P(COVID-19 | Fever = Yes)
# Then: Given Fever = Yes AND Disease = Flu
# Find: P(COVID-19 | Fever = Yes, Disease = Flu)
# Probability of COVID-19 decreases (explaining away)
```

---

## 🎯 Common Patterns

### Pattern 1: Serial Connection (Chain)

```
A → B → C
```

**Property**: A and C are independent given B  
**Example**: Season → Disease → Fever

### Pattern 2: Diverging Connection (Common Cause)

```
    B
   ↙ ↘
  A   C
```

**Property**: A and C are independent given B  
**Example**: Disease → Fever, Disease → Cough

### Pattern 3: Converging Connection (Common Effect)

```
  A   C
   ↘ ↙
    B
```

**Property**: A and C are dependent given B (explaining away)  
**Example**: Season → Disease ← Vaccination

---

## 💻 Code Snippets

### Load Data

```python
import json
import pandas as pd

# Load JSON dataset
with open('data/medical_diagnosis_data.json', 'r') as f:
    data = json.load(f)

# Extract components
network_structure = data['network_structure']
prior_probs = data['prior_probabilities']
cond_probs = data['conditional_probabilities']
```

### Calculate Single Probability

```python
# P(Fever = Yes | Disease = Flu)
prob = cond_probs['Fever_given_Disease']['Flu']['Yes']
print(f"P(Fever=Yes | Flu) = {prob}")  # 0.85
```

### Diagnose Patient

```python
# Patient symptoms
symptoms = {
    'Fever': 'Yes',
    'Cough': 'Yes',
    'Fatigue': 'No',
    'Breathing_Difficulty': 'No',
    'Runny_Nose': 'No'
}

# Calculate disease probabilities
disease_probs = calculate_disease_probability(symptoms)

# Get most likely disease
most_likely = max(disease_probs, key=disease_probs.get)
confidence = disease_probs[most_likely]

print(f"Diagnosis: {most_likely} ({confidence:.2%} confidence)")
```

### Visualize Probabilities

```python
import matplotlib.pyplot as plt

# Sort diseases by probability
sorted_diseases = sorted(disease_probs.items(), 
                         key=lambda x: x[1], reverse=True)

# Create bar chart
diseases = [d[0] for d in sorted_diseases]
probs = [d[1] for d in sorted_diseases]

plt.figure(figsize=(10, 6))
plt.bar(diseases, probs, color='steelblue', edgecolor='black')
plt.xlabel('Disease')
plt.ylabel('Probability')
plt.title('Disease Probability Distribution')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3, axis='y')
plt.show()
```

---

## ⚠️ Common Pitfalls

### 1. Probabilities Don't Sum to 1

**Problem**: CPT probabilities don't sum to 1  
**Solution**: Always verify `sum(P(X=x | Parents)) = 1` for all parent configurations

```python
# Verify CPT
for disease in diseases:
    total = sum(P_Fever_given_Disease[disease].values())
    assert abs(total - 1.0) < 0.01, f"Invalid CPT for {disease}"
```

### 2. Cycles in Network

**Problem**: Network has cycles (not a DAG)  
**Solution**: Remove cycles, ensure directed acyclic structure

```python
# Check for cycles (simple approach)
def has_cycle(edges):
    # Use topological sort or DFS
    # Return True if cycle detected
    pass
```

### 3. Zero Probabilities

**Problem**: P(Evidence) = 0 causes division by zero  
**Solution**: Use Laplace smoothing

```python
# Add small constant to avoid zeros
epsilon = 1e-10
likelihood = max(likelihood, epsilon)
```

### 4. Conditional Independence Assumption

**Problem**: Assuming independence when variables are dependent  
**Solution**: Add edges to capture dependencies

---

## 📈 Performance Tips

### 1. Use Log Probabilities

**Why**: Avoid numerical underflow with many multiplications

```python
import numpy as np

# Instead of: likelihood = p1 * p2 * p3 * ...
# Use: log_likelihood = log(p1) + log(p2) + log(p3) + ...
log_likelihood = sum(np.log(prob) for prob in probs)
likelihood = np.exp(log_likelihood)
```

### 2. Cache Intermediate Results

**Why**: Avoid redundant calculations

```python
# Cache CPT lookups
cpt_cache = {}

def get_cpt(symptom, disease, value):
    key = (symptom, disease, value)
    if key not in cpt_cache:
        cpt_cache[key] = cond_probs[f'{symptom}_given_Disease'][disease][value]
    return cpt_cache[key]
```

### 3. Approximate Inference for Large Networks

**Why**: Exact inference is NP-hard for complex networks

```python
# Use sampling methods
# - Monte Carlo sampling
# - Gibbs sampling
# - Importance sampling
```

---

## 🎓 Best Practices

### 1. Domain Knowledge

✅ **DO**: Consult domain experts for network structure  
❌ **DON'T**: Rely solely on data-driven structure learning

### 2. Data Quality

✅ **DO**: Use sufficient data for CPT estimation  
❌ **DON'T**: Use CPTs from small sample sizes

### 3. Model Validation

✅ **DO**: Test on held-out data  
❌ **DON'T**: Evaluate only on training data

### 4. Interpretability

✅ **DO**: Keep network simple and explainable  
❌ **DON'T**: Create overly complex networks

---

## 📚 Quick Reference Table

| Concept | Formula | Example |
|---------|---------|---------|
| **Bayes' Theorem** | P(A\|B) = P(B\|A)P(A)/P(B) | P(Flu\|Fever) = P(Fever\|Flu)P(Flu)/P(Fever) |
| **Joint Probability** | P(A,B) = P(A)P(B\|A) | P(Disease,Fever) = P(Disease)P(Fever\|Disease) |
| **Marginalization** | P(A) = Σ_B P(A,B) | P(Fever) = Σ_disease P(Fever,Disease) |
| **Conditional Independence** | P(A,B\|C) = P(A\|C)P(B\|C) | P(Fever,Cough\|Disease) = P(Fever\|Disease)P(Cough\|Disease) |

---

## 🔗 Useful Links

- [pgmpy Library](https://pgmpy.org/) - Python library for Bayesian Networks
- [BayesPy](http://bayespy.org/) - Bayesian inference in Python
- [Pomegranate](https://pomegranate.readthedocs.io/) - Probabilistic modeling
- [bnlearn](https://erdogant.github.io/bnlearn/) - Bayesian Network learning

---

**Keep this guide handy while working with Bayesian Networks!** 📖

