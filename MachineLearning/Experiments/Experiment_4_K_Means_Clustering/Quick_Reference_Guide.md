# K-Means Clustering - Quick Reference Guide

## 📚 Table of Contents
1. [Algorithm Overview](#algorithm-overview)
2. [Key Concepts](#key-concepts)
3. [Implementation Steps](#implementation-steps)
4. [Code Snippets](#code-snippets)
5. [Evaluation Metrics](#evaluation-metrics)
6. [Common Pitfalls](#common-pitfalls)
7. [Troubleshooting](#troubleshooting)

---

## 🎯 Algorithm Overview

### What is K-Means?

**K-Means** is a partitioning clustering algorithm that divides data into K distinct, non-overlapping clusters.

**Goal**: Minimize within-cluster variance (make points in same cluster as similar as possible)

**Type**: Unsupervised learning (no labels needed)

### How It Works

```
1. Initialize: Randomly select K points as initial centroids
2. Assignment: Assign each point to nearest centroid
3. Update: Recalculate centroids as mean of assigned points
4. Repeat: Steps 2-3 until convergence (centroids stop moving)
```

### Mathematical Formulation

**Objective Function**:
```
Minimize: J = Σᵢ₌₁ᴷ Σₓ∈Cᵢ ||x - μᵢ||²

Where:
- K = number of clusters
- Cᵢ = cluster i
- x = data point
- μᵢ = centroid of cluster i
- ||x - μᵢ||² = squared Euclidean distance
```

**Euclidean Distance**:
```
d(x, y) = √(Σⱼ₌₁ⁿ (xⱼ - yⱼ)²)
```

---

## 🔑 Key Concepts

### 1. Centroids
- **Definition**: Center point of a cluster
- **Calculation**: Mean of all points in the cluster
- **Role**: Represents the "typical" member of the cluster

### 2. Within-Cluster Sum of Squares (WCSS)
- **Also called**: Inertia
- **Definition**: Sum of squared distances from each point to its cluster centroid
- **Goal**: Minimize WCSS
- **Formula**: `WCSS = Σᵢ₌₁ᴷ Σₓ∈Cᵢ ||x - μᵢ||²`

### 3. Silhouette Score
- **Range**: -1 to 1 (higher is better)
- **Meaning**: How similar a point is to its own cluster vs other clusters
- **Interpretation**:
  - 0.7-1.0: Strong clustering
  - 0.5-0.7: Reasonable clustering
  - 0.25-0.5: Weak clustering
  - <0.25: No substantial structure

### 4. k-means++ Initialization
- **Purpose**: Smart centroid initialization
- **Benefit**: Faster convergence, better results
- **Method**: Spread out initial centroids based on distance

---

## 📋 Implementation Steps

### Step 1: Load and Explore Data
```python
import pandas as pd
import json

# Load data
with open('data/customer_data.json', 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data['data'])
print(df.head())
print(df.describe())
```

### Step 2: Select and Scale Features
```python
from sklearn.preprocessing import StandardScaler

# Select features (exclude identifiers)
features = ['Age', 'Income', 'SpendingScore']
X = df[features].values

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

### Step 3: Determine Optimal K

**Method A: Elbow Method**
```python
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

wcss = []
k_range = range(2, 11)

for k in k_range:
    kmeans = KMeans(n_clusters=k, init='k-means++', random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

# Plot elbow curve
plt.plot(k_range, wcss, marker='o')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('WCSS')
plt.title('Elbow Method')
plt.show()
```

**Method B: Silhouette Analysis**
```python
from sklearn.metrics import silhouette_score

silhouette_scores = []

for k in k_range:
    kmeans = KMeans(n_clusters=k, init='k-means++', random_state=42)
    labels = kmeans.fit_predict(X_scaled)
    score = silhouette_score(X_scaled, labels)
    silhouette_scores.append(score)
    print(f"K={k}: Silhouette Score = {score:.4f}")
```

### Step 4: Train Final Model
```python
# Choose optimal K (e.g., K=4)
optimal_k = 4

# Train final model
kmeans_final = KMeans(
    n_clusters=optimal_k,
    init='k-means++',
    n_init=10,
    max_iter=300,
    random_state=42
)

# Fit and predict
cluster_labels = kmeans_final.fit_predict(X_scaled)

# Add labels to DataFrame
df['Cluster'] = cluster_labels
```

### Step 5: Analyze Clusters
```python
# Get centroids (in original scale)
centroids_scaled = kmeans_final.cluster_centers_
centroids_original = scaler.inverse_transform(centroids_scaled)

# Cluster statistics
for i in range(optimal_k):
    cluster_data = df[df['Cluster'] == i]
    print(f"\nCluster {i}:")
    print(f"  Size: {len(cluster_data)}")
    print(f"  Mean Age: {cluster_data['Age'].mean():.1f}")
    print(f"  Mean Income: {cluster_data['Income'].mean():.1f}")
```

### Step 6: Visualize Results
```python
import matplotlib.pyplot as plt

# 2D scatter plot
plt.figure(figsize=(12, 8))

for i in range(optimal_k):
    cluster_data = df[df['Cluster'] == i]
    plt.scatter(cluster_data['Income'], 
                cluster_data['SpendingScore'],
                label=f'Cluster {i}',
                s=100, alpha=0.6)

# Plot centroids
plt.scatter(centroids_original[:, 1],  # Income
            centroids_original[:, 2],  # SpendingScore
            c='yellow', marker='X', s=500,
            edgecolors='black', linewidth=2,
            label='Centroids')

plt.xlabel('Income')
plt.ylabel('Spending Score')
plt.title('Customer Segments')
plt.legend()
plt.show()
```

---

## 💻 Code Snippets

### Complete Pipeline (Minimal Code)
```python
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

# 1. Load data
df = pd.read_csv('customers.csv')

# 2. Prepare features
X = df[['Age', 'Income', 'SpendingScore']].values
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. Find optimal K
silhouette_scores = []
for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, init='k-means++', random_state=42)
    labels = kmeans.fit_predict(X_scaled)
    silhouette_scores.append(silhouette_score(X_scaled, labels))

optimal_k = silhouette_scores.index(max(silhouette_scores)) + 2

# 4. Train final model
kmeans = KMeans(n_clusters=optimal_k, init='k-means++', random_state=42)
df['Cluster'] = kmeans.fit_predict(X_scaled)

# 5. Analyze
print(df.groupby('Cluster').mean())
```

### Custom K-Means Implementation
```python
import numpy as np

def kmeans_custom(X, K, max_iters=100):
    """Simple K-Means implementation"""
    # Random initialization
    centroids = X[np.random.choice(X.shape[0], K, replace=False)]
    
    for _ in range(max_iters):
        # Assignment step
        distances = np.sqrt(((X - centroids[:, np.newaxis])**2).sum(axis=2))
        labels = np.argmin(distances, axis=0)
        
        # Update step
        new_centroids = np.array([X[labels == k].mean(axis=0) for k in range(K)])
        
        # Check convergence
        if np.all(centroids == new_centroids):
            break
            
        centroids = new_centroids
    
    return labels, centroids

# Usage
labels, centroids = kmeans_custom(X_scaled, K=4)
```

---

## 📊 Evaluation Metrics

### 1. Silhouette Score
```python
from sklearn.metrics import silhouette_score, silhouette_samples

# Overall score
score = silhouette_score(X_scaled, labels)
print(f"Silhouette Score: {score:.4f}")

# Per-sample scores
sample_scores = silhouette_samples(X_scaled, labels)

# Per-cluster scores
for k in range(optimal_k):
    cluster_score = sample_scores[labels == k].mean()
    print(f"Cluster {k}: {cluster_score:.4f}")
```

### 2. Davies-Bouldin Index
```python
from sklearn.metrics import davies_bouldin_score

# Lower is better
db_score = davies_bouldin_score(X_scaled, labels)
print(f"Davies-Bouldin Index: {db_score:.4f}")
```

### 3. Calinski-Harabasz Index
```python
from sklearn.metrics import calinski_harabasz_score

# Higher is better
ch_score = calinski_harabasz_score(X_scaled, labels)
print(f"Calinski-Harabasz Index: {ch_score:.2f}")
```

---

## ⚠️ Common Pitfalls

### 1. Forgetting to Scale Features
**Problem**: Features with larger ranges dominate distance calculations

**Solution**: Always use StandardScaler or MinMaxScaler
```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

### 2. Not Setting Random Seed
**Problem**: Results change every time you run

**Solution**: Set random_state parameter
```python
kmeans = KMeans(n_clusters=4, random_state=42)
```

### 3. Using Too Many Features
**Problem**: Curse of dimensionality, poor clustering

**Solution**: Use PCA for dimensionality reduction
```python
from sklearn.decomposition import PCA
pca = PCA(n_components=3)
X_reduced = pca.fit_transform(X_scaled)
```

### 4. Ignoring Outliers
**Problem**: Outliers distort centroids

**Solution**: Remove outliers or use robust clustering (DBSCAN)
```python
from sklearn.ensemble import IsolationForest
iso = IsolationForest(contamination=0.1)
outliers = iso.fit_predict(X)
X_clean = X[outliers == 1]
```

### 5. Choosing K Arbitrarily
**Problem**: Wrong number of clusters

**Solution**: Use Elbow Method + Silhouette Analysis + Business needs

---

## 🔧 Troubleshooting

| Problem | Possible Cause | Solution |
|---------|---------------|----------|
| **Poor silhouette scores** | Wrong K, overlapping clusters | Try different K, check if data is clusterable |
| **Clusters change every run** | No random seed | Set `random_state=42` |
| **One large cluster, rest small** | Outliers, imbalanced data | Remove outliers, try different K |
| **Slow convergence** | Poor initialization | Use `init='k-means++'` |
| **Memory error** | Dataset too large | Use MiniBatchKMeans for large datasets |
| **Clusters don't make sense** | Wrong features, need scaling | Check feature selection, apply scaling |

### MiniBatchKMeans for Large Datasets
```python
from sklearn.cluster import MiniBatchKMeans

# For datasets with >100K samples
kmeans = MiniBatchKMeans(
    n_clusters=4,
    batch_size=1000,
    random_state=42
)
labels = kmeans.fit_predict(X_scaled)
```

---

## 🎯 Best Practices

1. **Always scale features** before K-Means
2. **Use k-means++ initialization** (default in scikit-learn)
3. **Run multiple times** with different initializations (`n_init=10`)
4. **Validate with multiple metrics** (Elbow + Silhouette + Business logic)
5. **Visualize results** to ensure clusters make sense
6. **Document assumptions** and business interpretations
7. **Monitor cluster stability** over time
8. **Consider alternatives** (DBSCAN for irregular shapes, Hierarchical for unknown K)

---

## 📖 Quick Formula Reference

| Metric | Formula | Interpretation |
|--------|---------|----------------|
| **Euclidean Distance** | `d = √(Σ(xᵢ-yᵢ)²)` | Distance between two points |
| **WCSS** | `Σᵢ Σₓ∈Cᵢ ||x-μᵢ||²` | Within-cluster variance (lower is better) |
| **Silhouette** | `s = (b-a)/max(a,b)` | Cluster quality (-1 to 1, higher is better) |
| **Centroid** | `μ = (1/n)Σₓ∈C x` | Mean of all points in cluster |

Where:
- `a` = average distance to points in same cluster
- `b` = average distance to points in nearest other cluster

---

## 🚀 Advanced Topics

### 1. Elbow Detection (Automated)
```python
from kneed import KneeLocator

kl = KneeLocator(k_range, wcss, curve='convex', direction='decreasing')
optimal_k = kl.elbow
print(f"Optimal K: {optimal_k}")
```

### 2. Hierarchical Clustering for Comparison
```python
from scipy.cluster.hierarchy import dendrogram, linkage

linkage_matrix = linkage(X_scaled, method='ward')
dendrogram(linkage_matrix)
plt.show()
```

### 3. DBSCAN for Irregular Shapes
```python
from sklearn.cluster import DBSCAN

dbscan = DBSCAN(eps=0.5, min_samples=5)
labels = dbscan.fit_predict(X_scaled)
```

---

**End of Quick Reference Guide**

For detailed explanations and examples, refer to the main Jupyter notebook!

