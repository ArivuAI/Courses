# Module 1 Quick Reference Guide

A concise reference for key concepts, algorithms, and formulas from Module 1.

---

## 🎯 Well-Posed Learning Problem

**Definition:** A computer program learns from experience **E** with respect to task **T** and performance measure **P**, if its performance at **T** (measured by **P**) improves with experience **E**.

### The Three Components

| Component | Description | Example (Spam Filter) |
|-----------|-------------|----------------------|
| **Task (T)** | What we're trying to do | Classify emails as spam/not spam |
| **Performance (P)** | How we measure success | Accuracy % (correctly classified) |
| **Experience (E)** | What data we learn from | Database of labeled emails |

---

## 🏗️ Four Design Choices for Learning Systems

1. **Choose the Training Experience**
   - Direct vs indirect feedback
   - Teacher vs self-play
   - Representative of distribution

2. **Choose the Target Function**
   - What to learn (e.g., V(b) for checkers)
   - Input/output specification

3. **Choose Representation**
   - Linear function: V(b) = w₀ + w₁x₁ + ... + wₙxₙ
   - Decision tree, neural network, etc.

4. **Choose Learning Algorithm**
   - How to fit the representation
   - LMS, gradient descent, etc.

---

## 📝 Hypothesis Representation

### Constraint Types

| Symbol | Meaning | Example |
|--------|---------|---------|
| **?** | Any value acceptable | Sky can be anything |
| **Specific Value** | Must match exactly | Sky = "Sunny" |
| **∅** | No value (empty set) | Impossible to satisfy |

### Example Hypotheses

```
Most General:    ⟨?, ?, ?, ?, ?, ?⟩
Specific:        ⟨Sunny, Warm, ?, Strong, ?, ?⟩
More Specific:   ⟨Sunny, Warm, Normal, Strong, Warm, Same⟩
Most Specific:   ⟨∅, ∅, ∅, ∅, ∅, ∅⟩
```

### General-to-Specific Ordering

- h₁ ≥ h₂ (h₁ is more general than h₂) if:
  - h₁ classifies all instances that h₂ classifies as positive
  - Every instance satisfying h₂ also satisfies h₁

---

## 🔍 Find-S Algorithm

### Algorithm Steps

```
1. Initialize h to the most specific hypothesis ⟨∅, ∅, ..., ∅⟩

2. For each positive training example x:
   For each attribute constraint aᵢ in h:
       If constraint aᵢ is satisfied by x:
           Do nothing
       Else:
           Replace aᵢ in h by the next more general constraint
           that is satisfied by x

3. Output hypothesis h
```

### Key Properties

✅ **Advantages:**
- Simple and fast
- Guaranteed to find maximally specific hypothesis
- Easy to implement

❌ **Limitations:**
- Ignores negative examples
- Cannot detect inconsistent data
- Only finds one hypothesis
- No way to know if converged to correct concept

### Example Trace

| Step | Example | Hypothesis | Action |
|------|---------|------------|--------|
| 0 | Initial | ⟨∅, ∅, ∅, ∅, ∅, ∅⟩ | Initialize |
| 1 | ⟨Sunny, Warm, Normal, Strong, Warm, Same⟩ (+) | ⟨Sunny, Warm, Normal, Strong, Warm, Same⟩ | Replace ∅ with values |
| 2 | ⟨Sunny, Warm, High, Strong, Warm, Same⟩ (+) | ⟨Sunny, Warm, ?, Strong, Warm, Same⟩ | Generalize Humidity |

---

## 🎯 Candidate-Elimination Algorithm

### Version Space Definition

**VS(H,D)** = {h ∈ H | Consistent(h, D)}

The set of all hypotheses from H consistent with training data D.

### S and G Boundaries

- **S (Specific Boundary):** Most specific hypotheses in version space
- **G (General Boundary):** Most general hypotheses in version space

**Key Insight:** Version space is completely characterized by S and G!

### Algorithm Steps

```
1. Initialize:
   G ← {⟨?, ?, ..., ?⟩}  (most general)
   S ← {⟨∅, ∅, ..., ∅⟩}  (most specific)

2. For each training example d:
   
   If d is POSITIVE:
       • Remove from G any hypothesis inconsistent with d
       • For each hypothesis s in S not consistent with d:
           - Remove s from S
           - Add to S all minimal generalizations h of s such that:
               * h is consistent with d
               * Some member of G is more general than h
       • Remove from S any hypothesis more general than another in S
   
   If d is NEGATIVE:
       • Remove from S any hypothesis inconsistent with d
       • For each hypothesis g in G consistent with d:
           - Remove g from G
           - Add to G all minimal specializations h of g such that:
               * h is inconsistent with d
               * Some member of S is more specific than h
       • Remove from G any hypothesis less general than another in G

3. Output: Version space characterized by S and G
```

### Key Properties

✅ **Advantages:**
- Uses both positive AND negative examples
- Maintains all consistent hypotheses (via S and G)
- Can detect when more data needed
- Can detect inconsistent data
- Provides confidence in predictions

❌ **Limitations:**
- Assumes target concept is in hypothesis space
- Cannot handle noisy data well
- Computational complexity for large hypothesis spaces
- Requires conjunctive representation

---

## 🧬 Inductive Bias

### Definition

The set of assumptions a learner uses to predict outputs for inputs it has not encountered.

### Candidate-Elimination Inductive Bias

**"The target concept c can be represented as a conjunction of attribute constraints."**

### Key Principles

1. **No Bias = No Generalization**
   - An unbiased learner cannot make inductive leaps
   - Bias is NECESSARY for learning

2. **Bias-Generalization Trade-off**
   - Stronger bias → Better generalization (if assumptions correct)
   - Weaker bias → More expressive but needs more data

3. **No Free Lunch Theorem**
   - No single algorithm is best for all problems
   - Choose bias based on domain knowledge

### Bias Comparison

| Algorithm | Bias | Strength | Generalization |
|-----------|------|----------|----------------|
| Candidate-Elimination | Conjunctive concepts | Strong | Good (if conjunctive) |
| Decision Trees | Prefer shorter trees | Medium | Good |
| Neural Networks | Smooth boundaries | Weak | Needs more data |
| Unbiased Learner | None | None | Impossible |

---

## 📊 LMS Algorithm (Least Mean Squares)

### Weight Update Rule

For each training example (x, V_train(x)):

```
V(x) = w₀ + w₁x₁ + w₂x₂ + ... + wₙxₙ

For each weight wᵢ:
    wᵢ ← wᵢ + η × (V_train(x) - V(x)) × xᵢ
```

Where:
- **η** = learning rate (e.g., 0.1)
- **V_train(x)** = target value
- **V(x)** = predicted value
- **xᵢ** = feature value

### Properties

- Converges to global minimum for linear functions
- Gradient descent on squared error
- Learning rate controls step size

---

## 🔑 Key Formulas

### Hypothesis Consistency

```
Consistent(h, D) ⟺ ∀⟨x, c(x)⟩ ∈ D : h(x) = c(x)
```

### Version Space Size

```
|VS(H,D)| = Number of hypotheses between S and G
```

### Mean Squared Error

```
MSE = (1/n) Σᵢ₌₁ⁿ (V_train(xᵢ) - V(xᵢ))²
```

### Accuracy

```
Accuracy = (Correct Predictions / Total Predictions) × 100%
```

---

## 💡 Quick Tips

### When to Use Find-S
- Simple problems with only positive examples
- Quick prototyping
- Educational purposes

### When to Use Candidate-Elimination
- Both positive and negative examples available
- Need to maintain all consistent hypotheses
- Want to detect when more data is needed
- Target concept is conjunctive

### Common Pitfalls

❌ **Don't:**
- Use Find-S when you have negative examples
- Assume Candidate-Elimination works for all concept types
- Forget that bias is necessary for learning
- Ignore the importance of well-defined T, P, E

✅ **Do:**
- Clearly define your learning problem (T, P, E)
- Choose appropriate inductive bias for your domain
- Test on unseen data
- Visualize hypothesis evolution
- Consider noise and inconsistencies in real data

---

## 📚 Important Definitions

**Concept Learning:** Inferring a boolean-valued function from training examples.

**Hypothesis Space (H):** Set of all possible hypotheses the learner can represent.

**Target Concept (c):** The true function we're trying to learn.

**Training Data (D):** Set of examples ⟨x, c(x)⟩ used for learning.

**Generalization:** Ability to correctly classify unseen examples.

**Overfitting:** Learning training data too well, poor generalization.

**Underfitting:** Model too simple to capture the pattern.

---

## 🎓 Study Checklist

Before moving to Module 2, ensure you can:

- [ ] Define a well-posed learning problem with T, P, E
- [ ] Explain the four design choices for learning systems
- [ ] Represent hypotheses using constraint notation
- [ ] Trace Find-S algorithm step-by-step
- [ ] Trace Candidate-Elimination algorithm step-by-step
- [ ] Explain S and G boundaries
- [ ] Describe why inductive bias is necessary
- [ ] Compare Find-S vs Candidate-Elimination
- [ ] Implement both algorithms in Python
- [ ] Apply concepts to new domains

---

**Keep this guide handy for quick reference!** 📖

*Arivu AI Machine Learning Course - Module 1*

