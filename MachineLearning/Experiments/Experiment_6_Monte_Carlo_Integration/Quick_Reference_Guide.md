# Monte Carlo Integration - Quick Reference Guide

## 📐 Core Formula

### Basic Monte Carlo Estimator

```
For integral I = ∫ₐᵇ f(x) dx:

Î = (b - a) × (1/N) × Σᵢ₌₁ᴺ f(xᵢ)

where xᵢ ~ Uniform[a, b]
```

**In words**: 
1. Generate N random points in [a, b]
2. Evaluate f(x) at each point
3. Take average of f(x) values
4. Multiply by interval width (b-a)

---

## 🔢 Mathematical Foundation

### Expected Value Interpretation

```
If x ~ Uniform[a, b], then:

E[f(x)] = ∫ₐᵇ f(x) × (1/(b-a)) dx
        = (1/(b-a)) × ∫ₐᵇ f(x) dx
        = I / (b-a)

Therefore: I = (b-a) × E[f(x)]

Monte Carlo estimates E[f(x)] using sample mean:
E[f(x)] ≈ (1/N) × Σf(xᵢ)
```

### Law of Large Numbers

```
As N → ∞:
(1/N) × Σf(xᵢ) → E[f(x)]

Guarantees convergence to true value
```

### Central Limit Theorem

```
Sample mean is approximately normal:
ȳ ~ N(μ, σ²/N)

where:
- μ = E[f(x)] (true mean)
- σ² = Var[f(x)] (variance)
- N = sample size
```

---

## 📊 Error Analysis

### Standard Error

```
SE = (b - a) × σ̂/√N

where:
- σ̂ = sample standard deviation of f(xᵢ)
- N = number of samples
```

### Convergence Rate

```
Error ∝ 1/√N

To reduce error by factor k:
Need k² times more samples

Examples:
- 10× error reduction → 100× more samples
- 100× error reduction → 10,000× more samples
```

### Confidence Intervals

```
95% Confidence Interval:
CI = Î ± 1.96 × SE
   = Î ± 1.96 × (b-a) × σ̂/√N

99% Confidence Interval:
CI = Î ± 2.576 × SE
```

---

## 💻 Python Implementation

### Basic Implementation

```python
import numpy as np

def monte_carlo_integrate(func, a, b, n_samples, seed=None):
    """
    Estimate integral using Monte Carlo method
    
    Parameters:
    -----------
    func : callable
        Function to integrate
    a, b : float
        Integration bounds
    n_samples : int
        Number of random samples
    seed : int, optional
        Random seed for reproducibility
    
    Returns:
    --------
    dict with keys:
        - estimate: integral estimate
        - std_error: standard error
        - samples: random samples used
        - function_values: f(x) for each sample
    """
    if seed is not None:
        np.random.seed(seed)
    
    # Generate random samples
    samples = np.random.uniform(a, b, n_samples)
    
    # Evaluate function
    function_values = func(samples)
    
    # Calculate estimate
    mean_value = np.mean(function_values)
    estimate = (b - a) * mean_value
    
    # Calculate standard error
    std_dev = np.std(function_values, ddof=1)
    std_error = (b - a) * std_dev / np.sqrt(n_samples)
    
    return {
        'estimate': estimate,
        'std_error': std_error,
        'samples': samples,
        'function_values': function_values
    }
```

### Usage Example

```python
# Define function
def f(x):
    return x**2

# Estimate integral
result = monte_carlo_integrate(f, 0, 1, 10000, seed=42)

print(f"Estimate: {result['estimate']:.6f}")
print(f"Std Error: {result['std_error']:.6f}")
print(f"95% CI: [{result['estimate'] - 1.96*result['std_error']:.6f}, "
      f"{result['estimate'] + 1.96*result['std_error']:.6f}]")
```

---

## 🎯 Sample Size Selection

### Rule of Thumb

```
For relative error ε:
N ≈ (1.96 × CV / ε)²

where CV = coefficient of variation = σ/μ
```

### Common Targets

| Desired Accuracy | Approximate N |
|-----------------|---------------|
| 10% error | 100 - 1,000 |
| 1% error | 10,000 - 100,000 |
| 0.1% error | 1,000,000 - 10,000,000 |
| 0.01% error | 100,000,000+ |

---

## 🔄 Variance Reduction Techniques

### 1. Stratified Sampling

```python
def stratified_monte_carlo(func, a, b, n_samples, n_strata):
    """Divide [a,b] into strata, sample from each"""
    samples_per_stratum = n_samples // n_strata
    estimates = []
    
    for i in range(n_strata):
        # Stratum bounds
        a_i = a + i * (b - a) / n_strata
        b_i = a + (i + 1) * (b - a) / n_strata
        
        # Sample from stratum
        samples = np.random.uniform(a_i, b_i, samples_per_stratum)
        values = func(samples)
        estimates.append(np.mean(values))
    
    # Combine estimates
    return (b - a) * np.mean(estimates)
```

**Variance Reduction**: 2-10× typical

### 2. Antithetic Variates

```python
def antithetic_monte_carlo(func, a, b, n_samples):
    """For each sample x, also use (a+b-x)"""
    samples = np.random.uniform(a, b, n_samples // 2)
    antithetic_samples = a + b - samples
    
    values1 = func(samples)
    values2 = func(antithetic_samples)
    
    # Average of paired samples
    paired_means = (values1 + values2) / 2
    return (b - a) * np.mean(paired_means)
```

**Variance Reduction**: 2-5× for symmetric functions

### 3. Control Variates

```python
def control_variate_monte_carlo(func, control_func, control_integral, 
                                a, b, n_samples):
    """Use correlated function with known integral"""
    samples = np.random.uniform(a, b, n_samples)
    
    # Evaluate both functions
    f_values = func(samples)
    c_values = control_func(samples)
    
    # Optimal coefficient
    cov = np.cov(f_values, c_values)[0, 1]
    var_c = np.var(c_values, ddof=1)
    beta = cov / var_c
    
    # Adjusted estimate
    f_mean = np.mean(f_values)
    c_mean = np.mean(c_values)
    c_true = control_integral / (b - a)
    
    adjusted_mean = f_mean - beta * (c_mean - c_true)
    return (b - a) * adjusted_mean
```

**Variance Reduction**: 5-100× if good control variate

---

## 📈 Convergence Diagnostics

### Visual Checks

```python
# Plot running estimate
running_means = np.cumsum(function_values) / np.arange(1, len(function_values) + 1)
plt.plot(running_means)
plt.axhline(true_value, color='red', linestyle='--')
plt.xlabel('Number of Samples')
plt.ylabel('Estimate')
plt.title('Convergence Plot')
```

### Statistical Tests

```python
# Geweke diagnostic (split chain)
n = len(function_values)
first_10 = function_values[:n//10]
last_50 = function_values[n//2:]

z_score = (np.mean(first_10) - np.mean(last_50)) / \
          np.sqrt(np.var(first_10)/len(first_10) + np.var(last_50)/len(last_50))

# |z_score| < 2 suggests convergence
```

---

## ⚠️ Common Pitfalls

### 1. Too Few Samples
```python
# ❌ BAD: Only 10 samples
result = monte_carlo_integrate(f, 0, 1, 10)

# ✅ GOOD: At least 1000 samples
result = monte_carlo_integrate(f, 0, 1, 10000)
```

### 2. Not Setting Random Seed
```python
# ❌ BAD: Non-reproducible
result = monte_carlo_integrate(f, 0, 1, 1000)

# ✅ GOOD: Reproducible
result = monte_carlo_integrate(f, 0, 1, 1000, seed=42)
```

### 3. Ignoring Variance
```python
# ❌ BAD: Only report estimate
print(f"Integral: {result['estimate']}")

# ✅ GOOD: Report with uncertainty
print(f"Integral: {result['estimate']:.4f} ± {1.96*result['std_error']:.4f}")
```

### 4. Wrong Interval Scaling
```python
# ❌ BAD: Forgot to multiply by (b-a)
estimate = np.mean(function_values)

# ✅ GOOD: Correct scaling
estimate = (b - a) * np.mean(function_values)
```

---

## 🎓 Best Practices

### 1. Always Set Random Seed
```python
np.random.seed(42)  # For reproducibility
```

### 2. Report Confidence Intervals
```python
print(f"Estimate: {est:.4f} ± {1.96*se:.4f} (95% CI)")
```

### 3. Check Convergence
```python
# Plot running estimate
# Check if it stabilizes
```

### 4. Use Variance Reduction
```python
# For expensive functions, use stratified sampling
# or other variance reduction techniques
```

### 5. Parallelize for Large N
```python
from multiprocessing import Pool

def parallel_monte_carlo(func, a, b, n_samples, n_processes=4):
    with Pool(n_processes) as pool:
        results = pool.starmap(
            monte_carlo_integrate,
            [(func, a, b, n_samples // n_processes)] * n_processes
        )
    return np.mean([r['estimate'] for r in results])
```

---

## 📚 Quick Formulas

| Quantity | Formula |
|----------|---------|
| **Estimate** | Î = (b-a) × (1/N) × Σf(xᵢ) |
| **Standard Error** | SE = (b-a) × σ̂/√N |
| **95% CI** | Î ± 1.96 × SE |
| **99% CI** | Î ± 2.576 × SE |
| **Relative Error** | \|Î - I\| / \|I\| |
| **Sample Size** | N ≈ (1.96 × σ / ε)² |

---

## 🔍 Troubleshooting

| Problem | Solution |
|---------|----------|
| High variance | Use variance reduction techniques |
| Slow convergence | Increase sample size or use stratified sampling |
| Biased results | Check random number generator quality |
| Non-reproducible | Set random seed |
| Confidence interval too wide | Increase N or reduce variance |

---

## 📖 Further Reading

- **Theory**: Robert & Casella, "Monte Carlo Statistical Methods"
- **Finance**: Glasserman, "Monte Carlo Methods in Financial Engineering"
- **Algorithms**: Rubinstein & Kroese, "Simulation and the Monte Carlo Method"

---

*This quick reference covers the essentials of Monte Carlo integration. For detailed explanations, see the main notebook.*

