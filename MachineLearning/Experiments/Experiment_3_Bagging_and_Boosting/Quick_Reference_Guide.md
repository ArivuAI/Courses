# Quick Reference Guide: Bagging and Boosting for Classification

## 🎯 Algorithm Quick Reference

### Bagging (Bootstrap Aggregating)

**Purpose**: Reduce variance by training multiple models on different data subsets

**Input**: Training dataset D with n examples

**Output**: Ensemble of T models with majority voting

**Algorithm Steps**:
```
1. For t = 1 to T:
   a. Create bootstrap sample Dₜ by sampling n examples from D with replacement
   b. Train model hₜ on Dₜ
   c. Add hₜ to ensemble

2. For prediction on new example x:
   a. Get predictions from all models: {h₁(x), h₂(x), ..., hₜ(x)}
   b. Return majority vote (mode) for classification
```

**Time Complexity**: O(T × C) where T = number of models, C = cost of training one model

**Space Complexity**: O(T × M) where M = model size

**Key Properties**:
- Parallel training (can use multiple CPUs)
- Reduces variance, not bias
- Works best with high-variance models (deep trees)
- More models = better (diminishing returns)

---

### Boosting (AdaBoost)

**Purpose**: Reduce bias by sequentially focusing on hard examples

**Input**: Training dataset D with n examples

**Output**: Ensemble of T weighted models

**Algorithm Steps**:
```
1. Initialize sample weights: wᵢ = 1/n for all i

2. For t = 1 to T:
   a. Train weak learner hₜ on D with weights w
   b. Calculate weighted error: εₜ = Σᵢ wᵢ × I(hₜ(xᵢ) ≠ yᵢ)
   c. Calculate model weight: αₜ = 0.5 × log((1 - εₜ) / εₜ)
   d. Update sample weights:
      - wᵢ = wᵢ × exp(-αₜ × yᵢ × hₜ(xᵢ))  for all i
      - Normalize: wᵢ = wᵢ / Σⱼ wⱼ

3. For prediction on new example x:
   a. Get weighted predictions: Σₜ αₜ × hₜ(x)
   b. Return sign of weighted sum
```

**Time Complexity**: O(T × C) - sequential, cannot parallelize

**Space Complexity**: O(T × M + n) - stores weights for each example

**Key Properties**:
- Sequential training (models depend on previous)
- Reduces bias, can reduce variance
- Works best with low-variance models (shallow trees/stumps)
- Can overfit if T is too large

---

## 📊 Key Concepts

### Bootstrap Sampling

**What**: Sampling n examples with replacement from dataset of size n

**Properties**:
- Each bootstrap sample contains ~63.2% unique examples
- Remaining ~36.8% are "out-of-bag" (OOB) samples
- Creates diversity among models

**Example**:
```
Original: [1, 2, 3, 4, 5]
Bootstrap 1: [1, 1, 3, 4, 5]  # 2 is missing, 1 appears twice
Bootstrap 2: [1, 2, 2, 3, 5]  # 4 is missing, 2 appears twice
Bootstrap 3: [2, 3, 3, 4, 5]  # 1 is missing, 3 appears twice
```

### Weak Learners

**Definition**: Model slightly better than random guessing (>50% accuracy for binary classification)

**Examples**:
- Decision stumps (trees with max_depth=1)
- Shallow decision trees (max_depth=2-3)
- Simple linear models

**Why Use Weak Learners in Boosting**:
- Prevent overfitting
- Allow gradual learning
- Ensemble of many weak learners = strong learner

### Bias-Variance Tradeoff

**Bias**: Error from wrong assumptions (underfitting)
**Variance**: Error from sensitivity to training data (overfitting)

**How Ensembles Help**:
- **Bagging**: Reduces variance by averaging predictions
- **Boosting**: Reduces bias by focusing on mistakes

---

## 💻 Code Snippets

### Bagging Implementation

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.utils import resample
import numpy as np

class SimpleBagging:
    def __init__(self, n_estimators=10):
        self.n_estimators = n_estimators
        self.models = []
    
    def fit(self, X, y):
        for i in range(self.n_estimators):
            # Bootstrap sample
            X_sample, y_sample = resample(X, y, n_samples=len(X))
            
            # Train model
            model = DecisionTreeClassifier()
            model.fit(X_sample, y_sample)
            self.models.append(model)
    
    def predict(self, X):
        # Get predictions from all models
        predictions = np.array([model.predict(X) for model in self.models])
        
        # Majority vote
        return np.apply_along_axis(
            lambda x: np.bincount(x).argmax(), 
            axis=0, 
            arr=predictions
        )
```

### Boosting Implementation (Simplified AdaBoost)

```python
class SimpleAdaBoost:
    def __init__(self, n_estimators=10):
        self.n_estimators = n_estimators
        self.models = []
        self.alphas = []
    
    def fit(self, X, y):
        n_samples = len(X)
        weights = np.ones(n_samples) / n_samples
        
        for i in range(self.n_estimators):
            # Train weak learner
            model = DecisionTreeClassifier(max_depth=1)
            model.fit(X, y, sample_weight=weights)
            
            # Calculate error
            predictions = model.predict(X)
            incorrect = predictions != y
            error = np.sum(weights * incorrect) / np.sum(weights)
            
            # Calculate model weight
            alpha = 0.5 * np.log((1 - error) / (error + 1e-10))
            
            # Update sample weights
            weights *= np.exp(-alpha * y * predictions)
            weights /= np.sum(weights)
            
            self.models.append(model)
            self.alphas.append(alpha)
    
    def predict(self, X):
        # Weighted vote
        predictions = np.array([
            alpha * model.predict(X) 
            for alpha, model in zip(self.alphas, self.models)
        ])
        return np.sign(np.sum(predictions, axis=0))
```

### Using Scikit-Learn

```python
from sklearn.ensemble import BaggingClassifier, AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier

# Bagging
bagging = BaggingClassifier(
    base_estimator=DecisionTreeClassifier(),
    n_estimators=100,
    random_state=42
)
bagging.fit(X_train, y_train)
y_pred_bagging = bagging.predict(X_test)

# Boosting
boosting = AdaBoostClassifier(
    base_estimator=DecisionTreeClassifier(max_depth=1),
    n_estimators=100,
    learning_rate=1.0,
    random_state=42
)
boosting.fit(X_train, y_train)
y_pred_boosting = boosting.predict(X_test)
```

---

## 📈 When to Use Each Method

### Use Bagging When:
- ✅ Data is noisy or has outliers
- ✅ Base model has high variance (overfits)
- ✅ Need stable, robust predictions
- ✅ Can train models in parallel (have multiple CPUs)
- ✅ Want to reduce overfitting

### Use Boosting When:
- ✅ Need maximum accuracy
- ✅ Base model has high bias (underfits)
- ✅ Data is clean and well-labeled
- ✅ Willing to tune hyperparameters carefully
- ✅ Sequential training is acceptable

### Comparison Table

| Aspect | Bagging | Boosting |
|--------|---------|----------|
| **Training** | Parallel | Sequential |
| **Focus** | Reduce variance | Reduce bias |
| **Base Learner** | Complex (deep trees) | Simple (stumps) |
| **Weighting** | Equal vote | Weighted vote |
| **Overfitting** | Resistant | Can overfit |
| **Speed** | Fast (parallel) | Slower (sequential) |
| **Interpretability** | Low | Low |
| **Example** | Random Forest | AdaBoost, XGBoost |

---

## 🔍 Hyperparameter Tuning

### Bagging Parameters

**n_estimators** (number of models):
- Start: 50-100
- Typical: 100-500
- More is usually better (diminishing returns)

**max_samples** (bootstrap sample size):
- Default: 1.0 (same as training set)
- Can reduce for faster training

**max_features** (features per model):
- Default: All features
- Random Forest uses sqrt(n_features) for classification

### Boosting Parameters

**n_estimators** (number of iterations):
- Start: 50-100
- Typical: 50-200
- Too many can overfit!

**learning_rate** (shrinkage):
- Range: 0.01 to 2.0
- Lower = more robust, needs more estimators
- Higher = faster learning, risk of overfitting

**max_depth** (tree depth):
- AdaBoost: 1-3 (weak learners)
- Gradient Boosting: 3-8

---

## 🎯 Performance Metrics

### Classification Metrics

**Accuracy**: (TP + TN) / (TP + TN + FP + FN)
- Overall correctness
- Can be misleading with imbalanced data

**Precision**: TP / (TP + FP)
- Of predicted positives, how many are correct?
- Important when false positives are costly

**Recall (Sensitivity)**: TP / (TP + FN)
- Of actual positives, how many did we catch?
- Important in medical diagnosis (don't miss diseases!)

**F1-Score**: 2 × (Precision × Recall) / (Precision + Recall)
- Harmonic mean of precision and recall
- Good for imbalanced datasets

**AUC-ROC**: Area Under ROC Curve
- Measures model's ability to distinguish classes
- 0.5 = random, 1.0 = perfect

---

## 🚀 Quick Troubleshooting

| Problem | Possible Cause | Solution |
|---------|---------------|----------|
| Bagging not improving | Base models too simple | Use deeper trees |
| Boosting overfitting | Too many estimators | Reduce n_estimators, lower learning_rate |
| Training too slow | Too many estimators | Reduce n_estimators, use parallel Bagging |
| Poor performance | Wrong base learner | Try different max_depth, min_samples_split |
| Imbalanced classes | Dataset skewed | Use class_weight='balanced' |

---

**Quick Reference Version 1.0** | **Arivu AI ML Course** | **Experiment 3**

