# Module 3: Quick Reference Guide

## 📐 Core Formulas

### Part 1: Ensemble Learning

#### AdaBoost (Adaptive Boosting)

**Initialize Weights**:
```
w_n^(1) = 1/N  for all n = 1, ..., N
```

**For t = 1 to T iterations**:

**1. Train weak classifier** h_t on weighted dataset

**2. Compute weighted error**:
```
ε_t = (Σ w_n^(t) · I(y_n ≠ h_t(x_n))) / (Σ w_n^(t))

where I(·) is indicator function (1 if true, 0 if false)
```

**3. Calculate classifier weight**:
```
α_t = log((1 - ε_t) / ε_t)

Properties:
- If ε_t = 0.5 (random guess) → α_t = 0 (no weight)
- If ε_t = 0.3 (good) → α_t ≈ 0.85 (positive weight)
- If ε_t = 0.1 (excellent) → α_t ≈ 2.20 (high weight)
```

**4. Update example weights**:
```
w_n^(t+1) = w_n^(t) · exp(α_t · I(y_n ≠ h_t(x_n))) / Z_t

where Z_t is normalization constant: Σ w_n^(t+1) = 1

Equivalent form:
w_n^(t+1) = w_n^(t) · exp(-α_t · y_n · h_t(x_n)) / Z_t
```

**Final Classifier**:
```
f(x) = sign(Σ(t=1 to T) α_t · h_t(x))

Weighted majority vote of all weak classifiers
```

**Training Error Bound**:
```
Training Error ≤ exp(-2 Σ(t=1 to T) γ_t²)

where γ_t = 0.5 - ε_t (edge over random guessing)
```

#### Bagging (Bootstrap Aggregating)

**Bootstrap Sampling**:
```
For b = 1 to B:
    Sample N examples with replacement from training set
    → Creates dataset D_b
    
Expected unique samples: ~63% of original data
Out-of-bag samples: ~37% of original data
```

**Training**:
```
For b = 1 to B:
    Train classifier f_b on D_b
```

**Prediction**:
```
Classification: f(x) = majority_vote(f_1(x), ..., f_B(x))
Regression: f(x) = (1/B) · Σ(b=1 to B) f_b(x)
```

**Variance Reduction** (assuming independence):
```
If individual models have variance σ²:
Averaged model has variance ≈ σ²/B

Example: 10 models → 10x variance reduction!
```

**Out-of-Bag Error Estimate**:
```
For each sample x_i:
    Predict using only models where x_i was out-of-bag
    
OOB Error ≈ Test Error (free validation!)
```

#### Random Forests

**Algorithm**:
```
For b = 1 to B:
    1. Create bootstrap sample D_b
    2. Grow tree:
       At each node:
           - Randomly select m features (out of p total)
           - Find best split among these m features
           - Split node
       Grow tree fully (no pruning)
    3. Store tree
    
Prediction: Majority vote (classification) or average (regression)
```

**Feature Selection**:
```
Classification: m = √p
Regression: m = p/3

where p = total number of features
```

**Feature Importance**:
```
For each feature j:
    Importance_j = Σ(over all trees) Σ(over all nodes using feature j) 
                   (decrease in impurity weighted by samples)
    
Normalize: Importance_j / Σ(all features) Importance
```

### Part 2: K-Means Clustering

**Objective Function** (minimize within-cluster sum of squares):
```
J = Σₖ Σᵢ∈Cₖ ||xᵢ - μₖ||²

Where:
- k = cluster index (1 to K)
- Cₖ = set of points in cluster k
- xᵢ = data point i
- μₖ = centroid of cluster k
- ||·|| = Euclidean distance
```

**Algorithm**:

**Step 1: Initialize**
```
Randomly select k data points as initial centroids {μ₁, ..., μₖ}

Better: K-Means++ initialization (spreads centroids apart)
```

**Step 2: Assignment**
```
For each data point xᵢ:
    Assign to cluster: Cₖ where k = argmin_j ||xᵢ - μⱼ||
    
(Assign each point to nearest centroid)
```

**Step 3: Update**
```
For each cluster k:
    μₖ = (1/|Cₖ|) Σᵢ∈Cₖ xᵢ
    
(Update centroid to mean of assigned points)
```

**Step 4: Convergence Check**
```
If ||μₖ^(new) - μₖ^(old)|| < ε for all k:
    STOP
Else:
    Go to Step 2
```

**Inertia (WCSS)**:
```
Inertia = Σᵢ min_k ||xᵢ - μₖ||²

Sum of squared distances to nearest centroid
```

**Silhouette Score** (cluster quality):
```
For each point i:
    a(i) = average distance to points in same cluster
    b(i) = average distance to points in nearest other cluster
    
    s(i) = (b(i) - a(i)) / max(a(i), b(i))
    
Average Silhouette Score = (1/N) Σᵢ s(i)

Interpretation:
- s(i) ≈ 1: Well clustered
- s(i) ≈ 0: On cluster boundary
- s(i) ≈ -1: Assigned to wrong cluster
```

**Competitive Learning (Online K-Means)**:
```
For each input x:
    1. Find winner: j* = argmin_j ||x - w_j||
    2. Update winner: w_j* ← w_j* + η(x - w_j*)
    3. Losers: No update (hard competition)
    
Learning rate: η(t) = η₀ / (1 + t)
```

**Normalization** (critical for K-Means!):

**Min-Max Scaling** (0 to 1):
```
x_normalized = (x - x_min) / (x_max - x_min)
```

**Z-Score Normalization** (mean=0, std=1):
```
x_normalized = (x - μ) / σ
```

**Robust Scaling** (median and IQR):
```
x_normalized = (x - median) / IQR
```

## 🔧 Implementation Patterns

### AdaBoost Implementation

```python
class AdaBoost:
    def __init__(self, n_estimators=50):
        self.n_estimators = n_estimators
        self.stumps = []
        self.stump_weights = []
    
    def fit(self, X, y):
        n_samples = X.shape[0]
        sample_weights = np.ones(n_samples) / n_samples
        
        for t in range(self.n_estimators):
            # Train weak classifier
            stump = DecisionStump()
            error = stump.fit(X, y, sample_weights)
            
            # Calculate classifier weight
            alpha = 0.5 * np.log((1 - error) / error)
            
            # Update sample weights
            predictions = stump.predict(X)
            sample_weights *= np.exp(-alpha * y * predictions)
            sample_weights /= np.sum(sample_weights)
            
            self.stumps.append(stump)
            self.stump_weights.append(alpha)
    
    def predict(self, X):
        stump_predictions = np.array([s.predict(X) for s in self.stumps])
        weighted_sum = np.dot(self.stump_weights, stump_predictions)
        return np.sign(weighted_sum)
```

### K-Means Implementation

```python
class KMeans:
    def __init__(self, n_clusters=3, max_iterations=100):
        self.n_clusters = n_clusters
        self.max_iterations = max_iterations
        self.centroids = None
    
    def fit(self, X):
        # Initialize centroids
        indices = np.random.choice(X.shape[0], self.n_clusters, replace=False)
        self.centroids = X[indices].copy()
        
        for iteration in range(self.max_iterations):
            # Assignment step
            distances = np.sqrt(((X[:, np.newaxis] - self.centroids) ** 2).sum(axis=2))
            labels = np.argmin(distances, axis=1)
            
            # Update step
            new_centroids = np.array([X[labels == k].mean(axis=0) 
                                     for k in range(self.n_clusters)])
            
            # Check convergence
            if np.allclose(self.centroids, new_centroids):
                break
            
            self.centroids = new_centroids
        
        return labels
```

## 📊 Decision Framework

### When to Use Which Ensemble Method?

| Criterion | AdaBoost | Bagging | Random Forest |
|-----------|----------|---------|---------------|
| **Problem Type** | High bias | High variance | General purpose |
| **Data Size** | Small-Medium | Medium-Large | Any size |
| **Noise Sensitivity** | High (avoid) | Low | Low |
| **Interpretability** | High (stumps) | Low | Medium (feature importance) |
| **Training Speed** | Slow (sequential) | Fast (parallel) | Fast (parallel) |
| **Overfitting Risk** | Can overfit | Rarely overfits | Rarely overfits |
| **Hyperparameter Tuning** | Moderate | Easy | Easy |
| **Best For** | Fraud detection, medical diagnosis | Image classification | Most problems! |

### When to Use K-Means vs Other Clustering?

| Criterion | K-Means | DBSCAN | GMM | Hierarchical |
|-----------|---------|--------|-----|--------------|
| **Cluster Shape** | Spherical | Arbitrary | Elliptical | Any |
| **Cluster Size** | Similar | Any | Any | Any |
| **Number of Clusters** | Must specify k | Automatic | Must specify | Automatic |
| **Outlier Handling** | Poor | Excellent | Good | Poor |
| **Scalability** | Excellent | Good | Poor | Poor |
| **Speed** | Very fast | Fast | Slow | Very slow |
| **Best For** | Customer segmentation | Anomaly detection | Soft clustering | Taxonomy |

## 🎯 Common Workflows

### Workflow 1: Ensemble Classification

```python
# 1. Load and prepare data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# 2. Train AdaBoost
adaboost = AdaBoost(n_estimators=50)
adaboost.fit(X_train, y_train)
ada_acc = accuracy_score(y_test, adaboost.predict(X_test))

# 3. Train Random Forest
rf = RandomForestClassifier(n_estimators=100, max_features='sqrt')
rf.fit(X_train, y_train)
rf_acc = accuracy_score(y_test, rf.predict(X_test))

# 4. Compare and choose best
print(f"AdaBoost: {ada_acc:.4f}")
print(f"Random Forest: {rf_acc:.4f}")
```

### Workflow 2: Customer Segmentation

```python
# 1. Load and normalize data
scaler = StandardScaler()
X_normalized = scaler.fit_transform(X)

# 2. Find optimal k
inertias = []
silhouette_scores = []
for k in range(2, 11):
    kmeans = KMeans(n_clusters=k)
    labels = kmeans.fit(X_normalized)
    inertias.append(kmeans.inertia)
    silhouette_scores.append(silhouette_score(X_normalized, labels))

# 3. Choose k and cluster
optimal_k = 4  # Based on elbow/silhouette
kmeans = KMeans(n_clusters=optimal_k)
labels = kmeans.fit(X_normalized)

# 4. Analyze clusters
for k in range(optimal_k):
    cluster_data = X[labels == k]
    print(f"Cluster {k}: {len(cluster_data)} customers")
    print(f"  Mean: {cluster_data.mean(axis=0)}")
```

---

**Quick Reference Guide - Module 3**

