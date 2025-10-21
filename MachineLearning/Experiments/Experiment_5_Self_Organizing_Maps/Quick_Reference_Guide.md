# Self-Organizing Maps (SOM) - Quick Reference Guide

## 📖 Algorithm Overview

**Self-Organizing Map (SOM)** is an unsupervised neural network algorithm that creates a low-dimensional (typically 2D) representation of high-dimensional data while preserving topological relationships.

**Invented by**: Teuvo Kohonen (1982)  
**Also known as**: Kohonen Map, Kohonen Network  
**Type**: Unsupervised learning, competitive learning, dimensionality reduction

---

## 🎯 Key Concepts

### 1. Competitive Learning
- Neurons compete to respond to input
- "Winner takes all" mechanism
- Best Matching Unit (BMU) is the neuron closest to input
- Only BMU and its neighbors are updated

### 2. Topology Preservation
- Similar inputs map to nearby neurons
- Smooth transitions between different regions
- Neighborhood relationships are maintained
- Creates interpretable visualizations

### 3. Best Matching Unit (BMU)
- Neuron with weight vector closest to input
- Found using Euclidean distance
- Winner of the competition for each input

### 4. Neighborhood Function
- Determines which neurons are updated
- Typically Gaussian function
- Radius decreases over time
- Creates smooth, continuous maps

### 5. Learning Rate Decay
- Controls magnitude of weight updates
- Starts high (aggressive learning)
- Decreases over time (fine-tuning)
- Ensures convergence

---

## 📐 Mathematical Formulation

### SOM Structure
```
Input Layer:  x = [x₁, x₂, ..., xₙ]  (n-dimensional input)
Output Layer: 2D grid of neurons (e.g., 10×10 = 100 neurons)
Weights:      wᵢ = [w₁, w₂, ..., wₙ]  (each neuron has n-dimensional weight vector)
```

### Training Algorithm

**Step 1: Initialize**
```
For each neuron i:
    wᵢ = random values in [0, 1]
```

**Step 2: Find Best Matching Unit (BMU)**
```
For input x:
    BMU = argmin ||x - wᵢ||
          i
    
Where ||·|| is Euclidean distance
```

**Step 3: Update Weights**
```
For each neuron i:
    wᵢ(t+1) = wᵢ(t) + α(t) × h(i, BMU, t) × [x - wᵢ(t)]

Where:
    α(t) = learning rate at time t
    h(i, BMU, t) = neighborhood function
```

**Step 4: Repeat**
```
Repeat steps 2-3 for all training samples and iterations
```

### Neighborhood Function (Gaussian)
```
h(i, BMU, t) = exp(-||rᵢ - rBMU||² / (2σ(t)²))

Where:
    rᵢ = position of neuron i in grid (e.g., [3, 5])
    rBMU = position of BMU in grid
    σ(t) = neighborhood radius at time t
```

### Learning Rate Decay
```
α(t) = α₀ × exp(-t / τ)

Where:
    α₀ = initial learning rate (e.g., 0.5)
    τ = time constant
    t = current iteration
```

### Neighborhood Radius Decay
```
σ(t) = σ₀ × exp(-t / τ)

Where:
    σ₀ = initial radius (e.g., 3.0)
    τ = time constant
    t = current iteration
```

---

## 🔧 Implementation Steps

### Step 1: Data Preparation
```python
# Load data
X = load_data()  # Shape: (n_samples, n_features)

# Normalize to [0, 1]
X_norm = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0))
```

### Step 2: Configure SOM
```python
from minisom import MiniSom

# Parameters
som_x = 10  # Grid width
som_y = 10  # Grid height
input_len = X_norm.shape[1]  # Number of features
sigma = 3.0  # Initial neighborhood radius
learning_rate = 0.5  # Initial learning rate

# Initialize SOM
som = MiniSom(x=som_x, y=som_y, input_len=input_len,
              sigma=sigma, learning_rate=learning_rate,
              random_seed=42)
```

### Step 3: Train SOM
```python
# Initialize weights
som.random_weights_init(X_norm)

# Train
num_iterations = 10000
som.train_random(data=X_norm, num_iteration=num_iterations)
```

### Step 4: Evaluate
```python
# Quantization error
qe = som.quantization_error(X_norm)
print(f"Quantization Error: {qe:.4f}")

# Topographic error
te = som.topographic_error(X_norm)
print(f"Topographic Error: {te:.4f}")
```

### Step 5: Visualize
```python
# U-Matrix
distance_map = som.distance_map()
plt.pcolor(distance_map.T, cmap='bone_r')
plt.colorbar()
plt.title('U-Matrix')
plt.show()

# Component planes
weights = som.get_weights()
for i in range(input_len):
    plt.figure()
    plt.pcolor(weights[:, :, i].T, cmap='viridis')
    plt.colorbar()
    plt.title(f'Component Plane {i}')
    plt.show()

# Hit map
hit_map = np.zeros((som_x, som_y))
for x in X_norm:
    winner = som.winner(x)
    hit_map[winner[0], winner[1]] += 1
plt.pcolor(hit_map.T, cmap='YlOrRd')
plt.colorbar()
plt.title('Hit Map')
plt.show()
```

### Step 6: Find Clusters
```python
# Get BMU for each sample
winners = np.array([som.winner(x) for x in X_norm])

# Assign cluster labels (optional: use K-Means on SOM coordinates)
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=4, random_seed=42)
cluster_labels = kmeans.fit_predict(winners)
```

---

## 📊 Evaluation Metrics

### 1. Quantization Error (QE)
**Definition**: Average distance from each data point to its BMU

**Formula**:
```
QE = (1/N) × Σ ||xᵢ - w_BMU(i)||
```

**Interpretation**:
- Lower is better (tighter fit)
- Typical range: 0.1 - 0.5 for normalized data
- Very low (<0.05) may indicate overfitting

### 2. Topographic Error (TE)
**Definition**: Proportion of data points where 1st and 2nd BMUs are not adjacent

**Formula**:
```
TE = (1/N) × Σ u(xᵢ)

Where u(xᵢ) = 1 if 1st and 2nd BMUs are not adjacent, 0 otherwise
```

**Interpretation**:
- Lower is better (better topology preservation)
- Range: 0.0 (perfect) to 1.0 (poor)
- Good value: < 0.1

### 3. Davies-Bouldin Index (Optional)
**Definition**: Ratio of within-cluster to between-cluster distances

**Interpretation**:
- Lower is better
- Measures cluster separation

---

## ⚙️ Parameter Selection Guide

### Grid Size
**Rule of Thumb**: Grid size ≈ 5√n, where n = number of samples

| Samples | Recommended Grid | Total Neurons |
|---------|-----------------|---------------|
| 100 | 7×7 or 10×10 | 49-100 |
| 500 | 11×11 or 12×12 | 121-144 |
| 1000 | 15×15 or 16×16 | 225-256 |
| 5000 | 35×35 or 40×40 | 1225-1600 |

**Trade-offs**:
- Small grid: Coarse, fast, less detail
- Large grid: Fine detail, slow, may overfit

### Learning Rate
- **Initial**: 0.5 - 1.0
- **Final**: 0.01 - 0.1
- **Decay**: Exponential

### Neighborhood Radius
- **Initial**: ~2/3 of grid size (e.g., 3.0 for 10×10)
- **Final**: 0.5 - 1.0
- **Decay**: Exponential

### Training Iterations
**Rule of Thumb**: 100-500 iterations per neuron

| Grid Size | Neurons | Recommended Iterations |
|-----------|---------|----------------------|
| 5×5 | 25 | 2,500 - 12,500 |
| 10×10 | 100 | 10,000 - 50,000 |
| 20×20 | 400 | 40,000 - 200,000 |

---

## 🎨 Visualization Types

### 1. U-Matrix (Unified Distance Matrix)
**Shows**: Average distance between each neuron and its neighbors  
**Interpretation**:
- Light regions = Cluster centers
- Dark regions = Cluster boundaries

### 2. Component Planes
**Shows**: Distribution of each feature across the SOM  
**Interpretation**:
- One plane per feature
- Hot regions = High values
- Cold regions = Low values

### 3. Hit Map
**Shows**: Number of data points mapped to each neuron  
**Interpretation**:
- Hot regions = Common patterns
- Cold regions = Rare patterns
- Empty neurons = Interpolation

### 4. Distance Map
**Shows**: Average distance to neighbors  
**Interpretation**:
- Similar to U-Matrix
- Identifies cluster structure

---

## ⚠️ Common Pitfalls

| Problem | Cause | Solution |
|---------|-------|----------|
| **Poor clustering** | Grid too small | Increase grid size |
| **Overfitting** | Grid too large | Decrease grid size |
| **Slow convergence** | Too few iterations | Increase iterations |
| **Noisy map** | Learning rate too high | Decrease initial learning rate |
| **No clear patterns** | Features not normalized | Apply min-max or z-score normalization |
| **High topographic error** | Neighborhood radius too small | Increase initial sigma |
| **Uneven distribution** | Imbalanced data | Oversample minority patterns |

---

## 💡 Best Practices

1. **Always normalize data** to [0, 1] or standardize to mean=0, std=1
2. **Start with 10×10 grid** for most applications
3. **Use 10,000+ iterations** for stable results
4. **Set random seed** for reproducibility
5. **Visualize U-Matrix first** to understand cluster structure
6. **Compare component planes** to find feature relationships
7. **Check hit map** to ensure good data coverage
8. **Monitor both QE and TE** for quality assessment
9. **Experiment with parameters** to find optimal configuration
10. **Interpret results** in domain context

---

## 🚀 Advanced Topics

### 1. Growing SOM (GSOM)
- Dynamically adds neurons during training
- Adapts to data complexity
- No need to specify grid size upfront

### 2. Hierarchical SOM
- Multiple SOM layers
- Coarse-to-fine clustering
- Better for large datasets

### 3. Batch SOM
- Updates all neurons simultaneously
- Faster convergence
- More stable than online learning

### 4. Time-Series SOM
- Temporal SOM (TSOM)
- Recurrent SOM
- For sequential data

### 5. Supervised SOM
- XY-Fused SOM
- Combines input and output
- For classification tasks

---

## 📚 Quick Formula Reference

```
BMU:           BMU = argmin ||x - wᵢ||
                     i

Update:        wᵢ(t+1) = wᵢ(t) + α(t) × h(i,BMU,t) × [x - wᵢ(t)]

Neighborhood:  h(i,BMU,t) = exp(-||rᵢ - rBMU||² / (2σ(t)²))

Learning Rate: α(t) = α₀ × exp(-t / τ)

Radius:        σ(t) = σ₀ × exp(-t / τ)

QE:            QE = (1/N) × Σ ||xᵢ - w_BMU(i)||

TE:            TE = (1/N) × Σ u(xᵢ)
```

---

## 🔗 Useful Resources

**Libraries**:
- MiniSom: https://github.com/JustGlowing/minisom
- SOMPY: https://github.com/sevamoo/SOMPY
- Kohonen (R): https://cran.r-project.org/package=kohonen

**Papers**:
- Kohonen (1982): Original SOM paper
- Kohonen (2001): Self-Organizing Maps (3rd edition)

**Tutorials**:
- MiniSom examples: https://github.com/JustGlowing/minisom/tree/master/examples
- SOM visualization: https://www.pitt.edu/~is2470pb/Spring05/FinalProjects/Group1a/tutorial/som.html

---

**Quick Reference Guide for Self-Organizing Maps**  
*Part of Arivu AI Machine Learning Course - Experiment 5*

