# Module 4: Quick Reference Guide

## 📐 Core Formulas

### Part 1: Unsupervised Learning

#### k-Means Clustering

**Objective Function** (minimize within-cluster variance):
```
J = Σₖ Σᵢ∈Cₖ ||xᵢ - μₖ||²

Where:
- k = cluster index (1 to K)
- Cₖ = set of points in cluster k
- xᵢ = data point i
- μₖ = center of cluster k
```

**Algorithm Steps**:
```
1. Initialize: Randomly select k centers {μ₁, ..., μₖ}

2. Assignment Step:
   Cₖ = {i : ||xᵢ - μₖ|| ≤ ||xᵢ - μⱼ|| for all j}
   (Assign each point to nearest center)

3. Update Step:
   μₖ = (1/|Cₖ|) Σᵢ∈Cₖ xᵢ
   (Update center to mean of assigned points)

4. Repeat steps 2-3 until convergence
```

**Convergence Criterion**:
```
||μₖ⁽ᵗ⁺¹⁾ - μₖ⁽ᵗ⁾|| < ε  for all k
```

**Inertia** (sum of squared distances):
```
Inertia = Σᵢ min_k ||xᵢ - μₖ||²
```

**Silhouette Score** (cluster quality):
```
s(i) = (b(i) - a(i)) / max(a(i), b(i))

Where:
- a(i) = average distance to points in same cluster
- b(i) = average distance to points in nearest other cluster
- s(i) ∈ [-1, 1]: 1 = perfect, 0 = overlapping, -1 = wrong cluster
```

#### Self-Organizing Map (SOM)

**Weight Update Rule**:
```
wⱼ⁽ᵗ⁺¹⁾ = wⱼ⁽ᵗ⁾ + η(t) × h(j, BMU, t) × (x - wⱼ⁽ᵗ⁾)

Where:
- wⱼ = weight vector of neuron j
- η(t) = learning rate at time t
- h(j, BMU, t) = neighborhood function
- x = input vector
- BMU = Best Matching Unit
```

**Learning Rate Decay**:
```
η(t) = η₀ × (1 - t/T)

Where:
- η₀ = initial learning rate (e.g., 0.5)
- t = current iteration
- T = total iterations
```

**Neighborhood Function** (Gaussian):
```
h(j, BMU, t) = exp(-||rⱼ - r_BMU||² / (2σ(t)²))

Where:
- rⱼ = grid position of neuron j
- r_BMU = grid position of BMU
- σ(t) = neighborhood radius at time t
```

**Neighborhood Radius Decay**:
```
σ(t) = σ₀ × (1 - t/T)

Where:
- σ₀ = initial radius (e.g., grid_size/2)
```

**Best Matching Unit (BMU)**:
```
BMU = argmin_j ||x - wⱼ||
```

**U-Matrix** (Unified Distance Matrix):
```
U(i,j) = (1/|N(i,j)|) Σₖ∈N(i,j) ||w(i,j) - wₖ||

Where:
- N(i,j) = neighbors of neuron (i,j)
- High values = cluster boundaries
- Low values = cluster interiors
```

### Part 2: MCMC Methods

#### Monte Carlo Integration

**Expectation Estimation**:
```
E[f(X)] ≈ (1/N) Σᵢ₌₁ᴺ f(xⁱ)

Where xⁱ ~ p(x)
```

**Law of Large Numbers**:
```
lim(N→∞) (1/N) Σᵢ₌₁ᴺ f(xⁱ) = E[f(X)]
```

**Variance of Estimate**:
```
Var[(1/N) Σᵢ f(xⁱ)] = Var[f(X)] / N
```

#### Metropolis-Hastings Algorithm

**Acceptance Probability**:
```
α(x*, x) = min(1, [p(x*) / p(x)] × [q(x|x*) / q(x*|x)])

For symmetric proposals (q(x*|x) = q(x|x*)):
α(x*, x) = min(1, p(x*) / p(x))
```

**Algorithm**:
```
1. Initialize: x⁽⁰⁾
2. For t = 1 to N:
   a) Propose: x* ~ q(x*|x⁽ᵗ⁻¹⁾)
   b) Calculate: α = min(1, p(x*)/p(x⁽ᵗ⁻¹⁾))
   c) Accept with probability α:
      if U(0,1) < α:
          x⁽ᵗ⁾ = x*
      else:
          x⁽ᵗ⁾ = x⁽ᵗ⁻¹⁾
```

**Common Proposal Distributions**:
```
Random Walk: x* = x + ε, where ε ~ N(0, σ²)
Independent: x* ~ q(x*)
```

**Detailed Balance Condition**:
```
p(x) × T(x → x') = p(x') × T(x' → x)

Where T is the transition probability
This ensures p(x) is the stationary distribution
```

#### Gibbs Sampling

**Algorithm** (for 2 variables):
```
1. Initialize: x⁽⁰⁾, y⁽⁰⁾
2. For t = 1 to N:
   a) Sample: x⁽ᵗ⁾ ~ p(x | y⁽ᵗ⁻¹⁾)
   b) Sample: y⁽ᵗ⁾ ~ p(y | x⁽ᵗ⁾)
```

**Bivariate Normal Conditionals**:
```
Given (X, Y) ~ N(μ, Σ) where:
μ = [μₓ, μᵧ]ᵀ
Σ = [[σₓ², ρσₓσᵧ],
     [ρσₓσᵧ, σᵧ²]]

Conditionals:
X | Y=y ~ N(μₓ + ρ(σₓ/σᵧ)(y - μᵧ), σₓ²(1 - ρ²))
Y | X=x ~ N(μᵧ + ρ(σᵧ/σₓ)(x - μₓ), σᵧ²(1 - ρ²))
```

#### MCMC Diagnostics

**Autocorrelation**:
```
ρₖ = Cov(Xₜ, Xₜ₊ₖ) / Var(Xₜ)

Where k = lag
```

**Effective Sample Size**:
```
ESS = N / (1 + 2 Σₖ₌₁^∞ ρₖ)

Where:
- N = total samples
- ρₖ = autocorrelation at lag k
```

**Gelman-Rubin Statistic** (R̂):
```
R̂ = √(Var⁺ / W)

Where:
- Var⁺ = weighted average of within and between chain variance
- W = within-chain variance
- Convergence: R̂ < 1.1
```

## 🔧 Implementation Patterns

### k-Means Implementation

```python
class KMeans:
    def __init__(self, n_clusters=3, max_iterations=100):
        self.n_clusters = n_clusters
        self.max_iterations = max_iterations
        self.centers = None
        self.labels = None
    
    def fit(self, X):
        # 1. Initialize centers
        self.centers = self._initialize_centers(X)
        
        # 2. Iterate until convergence
        for iteration in range(self.max_iterations):
            # Assignment step
            labels = self._assign_clusters(X)
            
            # Update step
            new_centers = self._update_centers(X, labels)
            
            # Check convergence
            if np.allclose(self.centers, new_centers):
                break
            
            self.centers = new_centers
        
        self.labels = labels
        return self
    
    def _assign_clusters(self, X):
        # Calculate distances to all centers
        distances = np.sqrt(((X[:, np.newaxis] - self.centers) ** 2).sum(axis=2))
        # Return index of nearest center
        return np.argmin(distances, axis=1)
    
    def _update_centers(self, X, labels):
        # Calculate mean of points in each cluster
        new_centers = np.array([X[labels == k].mean(axis=0) 
                               for k in range(self.n_clusters)])
        return new_centers
```

### SOM Implementation

```python
class SelfOrganizingMap:
    def __init__(self, grid_height, grid_width, input_dim, 
                 learning_rate=0.5, sigma=None):
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.input_dim = input_dim
        self.learning_rate_init = learning_rate
        self.sigma_init = sigma or max(grid_height, grid_width) / 2
        
        # Initialize weights randomly
        self.weights = np.random.rand(grid_height, grid_width, input_dim)
    
    def train(self, data, n_iterations=1000):
        n_samples = data.shape[0]
        
        for iteration in range(n_iterations):
            # Decay parameters
            progress = iteration / n_iterations
            learning_rate = self.learning_rate_init * (1 - progress)
            sigma = self.sigma_init * (1 - progress)
            
            # Random sample
            idx = np.random.randint(0, n_samples)
            input_vector = data[idx]
            
            # Find BMU
            bmu = self._find_bmu(input_vector)
            
            # Update weights
            self._update_weights(input_vector, bmu, learning_rate, sigma)
    
    def _find_bmu(self, input_vector):
        # Calculate distances to all neurons
        distances = np.linalg.norm(self.weights - input_vector, axis=2)
        # Return coordinates of minimum
        return np.unravel_index(np.argmin(distances), distances.shape)
    
    def _update_weights(self, input_vector, bmu, learning_rate, sigma):
        # Calculate neighborhood influence
        neighborhood = self._calculate_neighborhood(bmu, sigma)
        
        # Update all neurons
        for i in range(self.grid_height):
            for j in range(self.grid_width):
                influence = learning_rate * neighborhood[i, j]
                self.weights[i, j] += influence * (input_vector - self.weights[i, j])
```

### Metropolis-Hastings Implementation

```python
def metropolis_hastings(target_pdf, proposal_std, initial_value, 
                       n_samples, burn_in=1000):
    samples = np.zeros(n_samples + burn_in)
    samples[0] = initial_value
    n_accepted = 0
    
    for i in range(1, n_samples + burn_in):
        current = samples[i-1]
        
        # Propose new state
        proposal = current + np.random.normal(0, proposal_std)
        
        # Calculate acceptance probability
        acceptance_prob = min(1.0, target_pdf(proposal) / target_pdf(current))
        
        # Accept or reject
        if np.random.rand() < acceptance_prob:
            samples[i] = proposal
            n_accepted += 1
        else:
            samples[i] = current
    
    acceptance_rate = n_accepted / (n_samples + burn_in)
    return samples[burn_in:], acceptance_rate
```

### Gibbs Sampling Implementation

```python
def gibbs_sampling_bivariate_normal(mu_x, mu_y, sigma_x, sigma_y, rho,
                                   n_samples, burn_in=1000):
    total_samples = n_samples + burn_in
    samples_x = np.zeros(total_samples)
    samples_y = np.zeros(total_samples)
    
    # Initialize
    samples_x[0] = mu_x
    samples_y[0] = mu_y
    
    # Conditional parameters
    sigma_x_cond = sigma_x * np.sqrt(1 - rho**2)
    sigma_y_cond = sigma_y * np.sqrt(1 - rho**2)
    
    for i in range(1, total_samples):
        # Sample X given Y
        mu_x_cond = mu_x + rho * (sigma_x / sigma_y) * (samples_y[i-1] - mu_y)
        samples_x[i] = np.random.normal(mu_x_cond, sigma_x_cond)
        
        # Sample Y given X
        mu_y_cond = mu_y + rho * (sigma_y / sigma_x) * (samples_x[i] - mu_x)
        samples_y[i] = np.random.normal(mu_y_cond, sigma_y_cond)
    
    return samples_x[burn_in:], samples_y[burn_in:]
```

## 📊 Common Workflows

### Workflow 1: Customer Segmentation with k-Means

```python
# 1. Load and prepare data
data = pd.read_json('customer_data.json')
features = ['purchase_frequency', 'avg_order_value', 'recency']
X = data[features].values

# 2. Normalize features
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_normalized = scaler.fit_transform(X)

# 3. Find optimal k
inertias = []
silhouette_scores = []
for k in range(2, 11):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(X_normalized)
    inertias.append(kmeans.inertia)
    silhouette_scores.append(silhouette_score(X_normalized, kmeans.labels))

# 4. Apply k-Means with optimal k
optimal_k = 3  # Based on elbow/silhouette
kmeans = KMeans(n_clusters=optimal_k)
kmeans.fit(X_normalized)

# 5. Analyze clusters
data['cluster'] = kmeans.labels
cluster_profiles = data.groupby('cluster')[features].mean()
```

### Workflow 2: Bayesian A/B Testing with MCMC

```python
# 1. Define data
n_A, successes_A = 10000, 520
n_B, successes_B = 10000, 580

# 2. Define posterior (Beta distribution)
def posterior_A(p):
    return stats.beta.pdf(p, 1 + successes_A, 1 + n_A - successes_A)

def posterior_B(p):
    return stats.beta.pdf(p, 1 + successes_B, 1 + n_B - successes_B)

# 3. Sample from posteriors
samples_A, _ = metropolis_hastings(posterior_A, 0.01, 0.05, 50000, 5000)
samples_B, _ = metropolis_hastings(posterior_B, 0.01, 0.06, 50000, 5000)

# 4. Calculate probability B > A
prob_B_better = np.mean(samples_B > samples_A)

# 5. Calculate expected lift
expected_lift = np.mean(samples_B - samples_A)
lift_ci = np.percentile(samples_B - samples_A, [2.5, 97.5])
```

## 🎯 Decision Framework

### When to Use k-Means vs SOM

| Criterion | k-Means | SOM |
|-----------|---------|-----|
| **Speed** | Fast (O(nkd)) | Slow (O(nmd²)) |
| **Scalability** | Millions of points | Thousands of points |
| **Visualization** | Limited | Excellent |
| **Topology** | No preservation | Preserves topology |
| **Interpretability** | High | Medium |
| **Use Case** | Customer segmentation | Gene expression, fraud detection |

### When to Use Metropolis-Hastings vs Gibbs

| Criterion | Metropolis-Hastings | Gibbs Sampling |
|-----------|---------------------|----------------|
| **Generality** | Any distribution | Need conditionals |
| **Acceptance Rate** | 15-50% | 100% |
| **Tuning** | Requires tuning | No tuning |
| **Efficiency** | Medium | High (when applicable) |
| **Use Case** | General Bayesian inference | Conjugate priors |

---

**Quick Reference Guide - Module 4**

