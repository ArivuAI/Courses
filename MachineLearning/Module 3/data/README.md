# Module 3 - Data Files

This folder contains datasets for **Module 3: Ensemble Learning & Unsupervised Learning**.

## 📁 Files

### 1. `fraud_detection_data.csv` (500 samples)
**Purpose**: Credit card fraud detection for ensemble learning

**Features**:
- `transaction_id`: Unique identifier (TXN_00000 to TXN_00499)
- `transaction_amount_normalized`: Normalized transaction amount
- `time_since_last_transaction_normalized`: Normalized time since last transaction
- `merchant_category`: Type of merchant (5 categories)
- `card_type`: Credit card type (Visa, Mastercard, Amex)
- `is_fraud`: **Target** (1 = fraud, -1 = legitimate)

**Use Cases**:
- AdaBoost classification
- Bagging with decision trees
- Random Forest classification
- Ensemble method comparison

**Loading**:
```python
import pandas as pd
fraud_df = pd.read_csv('data/fraud_detection_data.csv')
X = fraud_df[['transaction_amount_normalized', 'time_since_last_transaction_normalized']].values
y = fraud_df['is_fraud'].values
```

---

### 2. `customer_segmentation_data.csv` (400 samples)
**Purpose**: Customer clustering and segmentation

**Features**:
- `customer_id`: Unique identifier (CUST_00000 to CUST_00399)
- `purchase_frequency`: How often customer purchases (normalized)
- `average_order_value`: Average spending per order (normalized)
- `recency_days`: Days since last purchase (1-365)
- `customer_lifetime_value`: Total customer value ($100-$5000)
- `account_age_months`: Account age (1-60 months)
- `true_segment`: **Ground truth** cluster (0-3)
- `segment_name`: Business segment (At-Risk, Occasional, Loyal, VIP)

**Segments**:
- **0 - At-Risk**: Low frequency, low value
- **1 - Occasional**: Medium frequency, medium value
- **2 - Loyal**: High frequency, medium-high value
- **3 - VIP**: Very high frequency, very high value

**Use Cases**:
- K-Means clustering
- Optimal k selection (elbow method, silhouette score)
- Customer segmentation
- Cluster profiling

**Loading**:
```python
import pandas as pd
customer_df = pd.read_csv('data/customer_segmentation_data.csv')
X = customer_df[['purchase_frequency', 'average_order_value']].values
y_true = customer_df['true_segment'].values  # For evaluation
```

---

### 3. `normalization_example_data.csv` (300 samples)
**Purpose**: Demonstrate importance of feature normalization

**Features**:
- `sample_id`: Unique identifier (SAMPLE_00000 to SAMPLE_00299)
- `feature_small_scale`: Small range (0-10)
- `feature_large_scale`: Large range (0-1000) - **dominates distance!**
- `feature_negative_values`: Negative values (-50 to 50)
- `true_cluster`: **Ground truth** cluster (0-2)

**Use Cases**:
- Show why normalization is critical for K-Means
- Compare K-Means with/without normalization
- Demonstrate Min-Max, Z-Score, Robust scaling

**Loading**:
```python
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

norm_df = pd.read_csv('data/normalization_example_data.csv')
X = norm_df[['feature_small_scale', 'feature_large_scale', 'feature_negative_values']].values

# Without normalization (BAD!)
kmeans_bad = KMeans(n_clusters=3)
labels_bad = kmeans_bad.fit_predict(X)

# With normalization (GOOD!)
scaler = StandardScaler()
X_normalized = scaler.fit_transform(X)
kmeans_good = KMeans(n_clusters=3)
labels_good = kmeans_good.fit_predict(X_normalized)
```

---

## 🔧 Normalization Methods

### Min-Max Scaling (0 to 1)
```python
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_normalized = scaler.fit_transform(X)
```
**Formula**: `x_normalized = (x - x_min) / (x_max - x_min)`

### Z-Score Normalization (mean=0, std=1)
```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_normalized = scaler.fit_transform(X)
```
**Formula**: `x_normalized = (x - mean) / std`

### Robust Scaling (median and IQR)
```python
from sklearn.preprocessing import RobustScaler
scaler = RobustScaler()
X_normalized = scaler.fit_transform(X)
```
**Formula**: `x_normalized = (x - median) / IQR`

---

## 📊 Dataset Statistics

| Dataset | Samples | Features | Target | Use Case |
|---------|---------|----------|--------|----------|
| **Fraud Detection** | 500 | 2 (+ 3 metadata) | Binary (-1/+1) | Ensemble Learning |
| **Customer Segmentation** | 400 | 2 (+ 4 metadata) | 4 clusters | K-Means Clustering |
| **Normalization Example** | 300 | 3 | 3 clusters | Feature Scaling |

---

## 🎯 Quick Start Examples

### Example 1: AdaBoost on Fraud Detection
```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# Load data
fraud_df = pd.read_csv('data/fraud_detection_data.csv')
X = fraud_df[['transaction_amount_normalized', 'time_since_last_transaction_normalized']].values
y = fraud_df['is_fraud'].values

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train AdaBoost (use your implementation from notebook)
adaboost = AdaBoost(n_estimators=50)
adaboost.fit(X_train, y_train)

# Evaluate
predictions = adaboost.predict(X_test)
accuracy = np.mean(predictions == y_test)
print(f"AdaBoost Accuracy: {accuracy:.4f}")
```

### Example 2: K-Means on Customer Segmentation
```python
import pandas as pd
import numpy as np
from sklearn.metrics import silhouette_score

# Load data
customer_df = pd.read_csv('data/customer_segmentation_data.csv')
X = customer_df[['purchase_frequency', 'average_order_value']].values
y_true = customer_df['true_segment'].values

# Find optimal k using elbow method
inertias = []
for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)
    inertias.append(kmeans.inertia)

# Cluster with optimal k
kmeans = KMeans(n_clusters=4, random_state=42)
labels = kmeans.fit(X)

# Evaluate
silhouette = silhouette_score(X, labels)
print(f"Silhouette Score: {silhouette:.4f}")

# Analyze clusters
for k in range(4):
    cluster_data = customer_df[labels == k]
    print(f"\nCluster {k}: {len(cluster_data)} customers")
    print(f"  Avg Purchase Frequency: {cluster_data['purchase_frequency'].mean():.2f}")
    print(f"  Avg Order Value: {cluster_data['average_order_value'].mean():.2f}")
```

### Example 3: Normalization Comparison
```python
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load data
norm_df = pd.read_csv('data/normalization_example_data.csv')
X = norm_df[['feature_small_scale', 'feature_large_scale', 'feature_negative_values']].values

# K-Means WITHOUT normalization
kmeans_bad = KMeans(n_clusters=3, random_state=42)
labels_bad = kmeans_bad.fit(X)
print(f"Without normalization - Inertia: {kmeans_bad.inertia:.2f}")

# K-Means WITH normalization
scaler = StandardScaler()
X_normalized = scaler.fit_transform(X)
kmeans_good = KMeans(n_clusters=3, random_state=42)
labels_good = kmeans_good.fit(X_normalized)
print(f"With normalization - Inertia: {kmeans_good.inertia:.2f}")

# Compare with ground truth
from sklearn.metrics import adjusted_rand_score
y_true = norm_df['true_cluster'].values
print(f"\nAdjusted Rand Score (without norm): {adjusted_rand_score(y_true, labels_bad):.4f}")
print(f"Adjusted Rand Score (with norm): {adjusted_rand_score(y_true, labels_good):.4f}")
```

---

## 🔄 Regenerating Datasets

To regenerate datasets with different random seeds:

```bash
cd "Module 3/data"
python generate_datasets.py
```

This will create fresh datasets with the same structure but different random values.

---

## 📝 Notes

- All datasets use `random_seed=42` for reproducibility
- Datasets are synthetic but realistic
- Ground truth labels provided for evaluation
- Features are pre-normalized where appropriate
- Additional metadata columns included for business context

---

## 📚 Additional Information

For more details, see:
- `dataset_metadata.json` - Complete metadata for all datasets
- `generate_datasets.py` - Script to regenerate datasets
- Main notebook - Examples using these datasets

---

**Module 3 - Ensemble Learning & Unsupervised Learning**

