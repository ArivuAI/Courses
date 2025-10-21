"""
Generate datasets for Module 3: Ensemble Learning & Unsupervised Learning

This script creates three datasets:
1. fraud_detection_data.csv - Credit card fraud detection (500 samples)
2. customer_segmentation_data.csv - Customer clustering (400 samples)
3. normalization_example_data.csv - Feature scaling example (300 samples)

Run this script to regenerate the datasets with different random seeds.
"""

import numpy as np
import pandas as pd
from sklearn.datasets import make_classification, make_blobs
import json
import os

# Set random seed for reproducibility
np.random.seed(42)

# Create data directory if it doesn't exist
os.makedirs('.', exist_ok=True)

print("=" * 80)
print("GENERATING MODULE 3 DATASETS")
print("=" * 80)

# ============================================================================
# Dataset 1: Fraud Detection Data (for AdaBoost/Bagging/Random Forest)
# ============================================================================
print("\n1. Generating Fraud Detection Dataset...")

# Generate synthetic fraud detection data
# Feature 1: Transaction amount (normalized)
# Feature 2: Time since last transaction (normalized)
X_fraud, y_fraud_binary = make_classification(
    n_samples=500,  # 500 transactions
    n_features=2,  # 2 features for easy visualization
    n_informative=2,  # Both features are informative
    n_redundant=0,  # No redundant features
    n_clusters_per_class=1,  # One cluster per class
    flip_y=0.1,  # 10% label noise (realistic for fraud detection)
    class_sep=1.0,  # Moderate separation between classes
    random_state=42
)

# Convert to -1/+1 labels (required for AdaBoost)
y_fraud = np.where(y_fraud_binary == 0, -1, 1)

# Create DataFrame
fraud_df = pd.DataFrame({
    'transaction_amount_normalized': X_fraud[:, 0],
    'time_since_last_transaction_normalized': X_fraud[:, 1],
    'is_fraud': y_fraud
})

# Add additional realistic features
fraud_df['transaction_id'] = [f'TXN_{i:05d}' for i in range(500)]
fraud_df['merchant_category'] = np.random.choice(
    ['Online Retail', 'Gas Station', 'Restaurant', 'Grocery', 'Travel'],
    size=500
)
fraud_df['card_type'] = np.random.choice(['Visa', 'Mastercard', 'Amex'], size=500)

# Reorder columns
fraud_df = fraud_df[[
    'transaction_id', 'transaction_amount_normalized', 
    'time_since_last_transaction_normalized', 'merchant_category', 
    'card_type', 'is_fraud'
]]

# Save to CSV
fraud_df.to_csv('fraud_detection_data.csv', index=False)
print(f"   ✓ Created fraud_detection_data.csv")
print(f"   - Samples: {len(fraud_df)}")
print(f"   - Features: {fraud_df.shape[1] - 1}")
print(f"   - Fraud cases: {(fraud_df['is_fraud'] == 1).sum()}")
print(f"   - Legitimate cases: {(fraud_df['is_fraud'] == -1).sum()}")

# ============================================================================
# Dataset 2: Customer Segmentation Data (for K-Means Clustering)
# ============================================================================
print("\n2. Generating Customer Segmentation Dataset...")

# Create 4 natural clusters (VIP, Loyal, Occasional, At-Risk)
X_customers, y_true = make_blobs(
    n_samples=400,  # 400 customers
    n_features=2,  # 2 features for visualization
    centers=4,  # 4 customer segments
    cluster_std=0.6,  # Moderate cluster spread
    center_box=(-3, 3),  # Range of cluster centers
    random_state=42
)

# Create DataFrame with meaningful feature names
customer_df = pd.DataFrame({
    'purchase_frequency': X_customers[:, 0],  # How often they buy
    'average_order_value': X_customers[:, 1],  # How much they spend
    'true_segment': y_true  # Ground truth labels (for evaluation)
})

# Add customer IDs
customer_df['customer_id'] = [f'CUST_{i:05d}' for i in range(400)]

# Add additional realistic features
customer_df['recency_days'] = np.random.randint(1, 365, size=400)
customer_df['customer_lifetime_value'] = (
    (customer_df['purchase_frequency'] + 3) * 
    (customer_df['average_order_value'] + 3) * 
    np.random.uniform(50, 200, size=400)
).round(2)
customer_df['account_age_months'] = np.random.randint(1, 60, size=400)

# Map true segments to business names
segment_names = {0: 'At-Risk', 1: 'Occasional', 2: 'Loyal', 3: 'VIP'}
customer_df['segment_name'] = customer_df['true_segment'].map(segment_names)

# Reorder columns
customer_df = customer_df[[
    'customer_id', 'purchase_frequency', 'average_order_value',
    'recency_days', 'customer_lifetime_value', 'account_age_months',
    'true_segment', 'segment_name'
]]

# Save to CSV
customer_df.to_csv('customer_segmentation_data.csv', index=False)
print(f"   ✓ Created customer_segmentation_data.csv")
print(f"   - Samples: {len(customer_df)}")
print(f"   - Features: {customer_df.shape[1] - 3}")  # Exclude IDs and labels
print(f"   - Segments:")
for segment_id, segment_name in segment_names.items():
    count = (customer_df['true_segment'] == segment_id).sum()
    print(f"     • {segment_name}: {count} customers")

# ============================================================================
# Dataset 3: Normalization Example Data (for Feature Scaling)
# ============================================================================
print("\n3. Generating Normalization Example Dataset...")

# Create data with different scales
n_samples = 300

# Feature 1: Small scale (0-10)
feature1 = np.random.rand(n_samples) * 10

# Feature 2: Large scale (0-1000)
feature2 = np.random.rand(n_samples) * 1000

# Feature 3: Negative values (-50 to 50)
feature3 = np.random.randn(n_samples) * 20

# Create 3 natural clusters (for demonstrating normalization importance)
cluster_labels = np.random.choice([0, 1, 2], size=n_samples)

# Add cluster-specific patterns
for i in range(n_samples):
    if cluster_labels[i] == 0:
        feature1[i] += 2
        feature2[i] += 200
        feature3[i] += 10
    elif cluster_labels[i] == 1:
        feature1[i] += 5
        feature2[i] += 500
        feature3[i] -= 10
    else:
        feature1[i] += 8
        feature2[i] += 800
        feature3[i] += 0

# Create DataFrame
normalization_df = pd.DataFrame({
    'feature_small_scale': feature1,
    'feature_large_scale': feature2,
    'feature_negative_values': feature3,
    'true_cluster': cluster_labels
})

# Add sample IDs
normalization_df['sample_id'] = [f'SAMPLE_{i:05d}' for i in range(n_samples)]

# Reorder columns
normalization_df = normalization_df[[
    'sample_id', 'feature_small_scale', 'feature_large_scale',
    'feature_negative_values', 'true_cluster'
]]

# Save to CSV
normalization_df.to_csv('normalization_example_data.csv', index=False)
print(f"   ✓ Created normalization_example_data.csv")
print(f"   - Samples: {len(normalization_df)}")
print(f"   - Features: {normalization_df.shape[1] - 2}")  # Exclude ID and label
print(f"   - Feature scales:")
print(f"     • Small scale: {feature1.min():.2f} to {feature1.max():.2f}")
print(f"     • Large scale: {feature2.min():.2f} to {feature2.max():.2f}")
print(f"     • Negative values: {feature3.min():.2f} to {feature3.max():.2f}")

# ============================================================================
# Create metadata file
# ============================================================================
print("\n4. Creating metadata file...")

metadata = {
    "module": "Module 3 - Ensemble Learning & Unsupervised Learning",
    "created_date": "2025-10-15",
    "random_seed": 42,
    "datasets": {
        "fraud_detection_data.csv": {
            "description": "Credit card fraud detection dataset for ensemble learning",
            "samples": 500,
            "features": ["transaction_amount_normalized", "time_since_last_transaction_normalized"],
            "target": "is_fraud",
            "use_case": "AdaBoost, Bagging, Random Forest classification"
        },
        "customer_segmentation_data.csv": {
            "description": "Customer purchase behavior for clustering",
            "samples": 400,
            "features": ["purchase_frequency", "average_order_value"],
            "clusters": 4,
            "use_case": "K-Means clustering, customer segmentation"
        },
        "normalization_example_data.csv": {
            "description": "Multi-scale features demonstrating normalization importance",
            "samples": 300,
            "features": ["feature_small_scale", "feature_large_scale", "feature_negative_values"],
            "clusters": 3,
            "use_case": "Feature normalization, scaling techniques"
        }
    }
}

with open('dataset_metadata.json', 'w') as f:
    json.dump(metadata, f, indent=2)

print(f"   ✓ Created dataset_metadata.json")

# ============================================================================
# Summary
# ============================================================================
print("\n" + "=" * 80)
print("DATASET GENERATION COMPLETE!")
print("=" * 80)
print("\nGenerated files:")
print("  1. fraud_detection_data.csv (500 samples)")
print("  2. customer_segmentation_data.csv (400 samples)")
print("  3. normalization_example_data.csv (300 samples)")
print("  4. dataset_metadata.json (metadata)")
print("\nTo load datasets in your notebook:")
print("  fraud_df = pd.read_csv('data/fraud_detection_data.csv')")
print("  customer_df = pd.read_csv('data/customer_segmentation_data.csv')")
print("  norm_df = pd.read_csv('data/normalization_example_data.csv')")
print("\n" + "=" * 80)

