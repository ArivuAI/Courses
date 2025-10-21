# Module 4: Unsupervised Learning & MCMC Methods

## 📚 Overview

This module covers two fundamental topics in machine learning:

**Part 1: Unsupervised Learning**
- k-Means Clustering
- Vector Quantisation
- Self-Organizing Maps (SOM)
- Cluster validation and optimization

**Part 2: Markov Chain Monte Carlo (MCMC) Methods**
- Monte Carlo sampling
- Metropolis-Hastings algorithm
- Gibbs Sampling
- Bayesian inference applications

## 🎯 Learning Objectives

By the end of this module, you will be able to:

### Unsupervised Learning
- ✅ Implement k-Means clustering from scratch
- ✅ Apply k-Means to customer segmentation problems
- ✅ Choose optimal number of clusters using Elbow Method and Silhouette Score
- ✅ Understand vector quantisation for data compression
- ✅ Implement Self-Organizing Maps (SOM)
- ✅ Visualize high-dimensional data using SOM
- ✅ Interpret U-Matrix and component planes
- ✅ Compare k-Means vs SOM for different applications

### MCMC Methods
- ✅ Understand Monte Carlo principles and Law of Large Numbers
- ✅ Implement Metropolis-Hastings algorithm
- ✅ Implement Gibbs Sampling
- ✅ Sample from complex, multimodal distributions
- ✅ Diagnose MCMC convergence (trace plots, autocorrelation, Gelman-Rubin)
- ✅ Apply MCMC to Bayesian inference problems
- ✅ Solve real-world A/B testing problems with Bayesian methods

## 📂 Files in This Module

```
Module 4/
├── Module_4_Unsupervised_Learning_and_MCMC.ipynb  # Main notebook (~2,850 lines)
├── README.md                                       # This file
├── Quick_Reference_Guide.md                        # Formulas and concepts
├── COMPLETION_SUMMARY.md                           # Project statistics
├── ml_module4_slides.md                           # Lecture slides
└── data/
    └── customer_segmentation_data.json            # Customer dataset (50 samples)
```

## 🚀 Quick Start

### Prerequisites

**Python Libraries**:
```bash
pip install numpy pandas matplotlib seaborn scipy scikit-learn
```

**Knowledge Prerequisites**:
- Basic Python programming
- NumPy arrays and operations
- Probability and statistics fundamentals
- Linear algebra basics (vectors, matrices, distances)

### Running the Notebook

1. **Open Jupyter**:
   ```bash
   jupyter notebook Module_4_Unsupervised_Learning_and_MCMC.ipynb
   ```

2. **Run all cells** (Kernel → Restart & Run All)

3. **Expected runtime**: ~2-3 minutes (depending on MCMC iterations)

## 📊 Datasets

### 1. Customer Segmentation Dataset
- **File**: `data/customer_segmentation_data.json`
- **Size**: 50 customers
- **Features**:
  - `purchase_frequency`: Number of purchases (0-100)
  - `avg_order_value`: Average spending per order ($0-$1000)
  - `days_since_last_purchase`: Recency (0-365 days)
  - `customer_lifetime_value`: Total spending ($0-$10,000)
- **Use**: k-Means clustering example

### 2. Synthetic Datasets
- **RGB Colors**: 1,000 random colors for SOM visualization
- **Mixture Gaussians**: Bimodal distribution for Metropolis-Hastings
- **Bivariate Normal**: Correlated 2D distribution for Gibbs Sampling

## 🧠 Key Concepts

### Part 1: Unsupervised Learning

#### k-Means Clustering
**Algorithm**:
1. Initialize k cluster centers randomly
2. Assign each point to nearest center
3. Update centers to mean of assigned points
4. Repeat until convergence

**Key Parameters**:
- `n_clusters`: Number of clusters (k)
- `max_iterations`: Maximum iterations (default: 100)
- `random_state`: Random seed for reproducibility

**Choosing k**:
- **Elbow Method**: Plot inertia vs k, find "elbow"
- **Silhouette Score**: Measure cluster quality (-1 to +1)
- **Domain knowledge**: Business context often suggests k

#### Self-Organizing Maps (SOM)
**Algorithm**:
1. Initialize grid of neurons with random weights
2. For each input:
   - Find Best Matching Unit (BMU)
   - Update BMU and neighbors towards input
3. Decay learning rate and neighborhood radius
4. Repeat until convergence

**Key Parameters**:
- `grid_height`, `grid_width`: Grid dimensions
- `learning_rate`: Initial learning rate (η₀)
- `sigma`: Initial neighborhood radius
- `n_iterations`: Training iterations

**Visualizations**:
- **U-Matrix**: Shows cluster boundaries
- **Component Planes**: Feature distributions
- **Hit Map**: Data distribution across grid

### Part 2: MCMC Methods

#### Metropolis-Hastings
**Algorithm**:
1. Start at x₀
2. Propose x* from q(x*|xₜ)
3. Calculate acceptance probability: α = min(1, p(x*)/p(xₜ))
4. Accept with probability α, else stay at xₜ
5. Repeat

**Key Parameters**:
- `proposal_std`: Proposal distribution width
- `n_samples`: Number of samples to generate
- `burn_in`: Initial samples to discard

**Tuning**:
- Optimal acceptance rate: 23-50% (1D), 15-30% (high-D)

#### Gibbs Sampling
**Algorithm**:
1. Initialize x⁽⁰⁾, y⁽⁰⁾
2. Sample x⁽ᵗ⁾ ~ p(x | y⁽ᵗ⁻¹⁾)
3. Sample y⁽ᵗ⁾ ~ p(y | x⁽ᵗ⁾)
4. Repeat

**Advantages**:
- 100% acceptance rate
- No tuning required
- Efficient for conjugate priors

## 🏢 Real-World Applications

### Unsupervised Learning
1. **Customer Segmentation** (Banking, E-commerce)
   - Identify VIP, loyal, occasional, at-risk customers
   - Personalized marketing campaigns
   - Impact: 15-20% increase in conversion rates

2. **Fraud Detection** (Finance, Insurance)
   - Detect anomalous transaction patterns
   - Real-time monitoring with SOM
   - Impact: $11B+ fraud prevented annually

3. **Image Compression** (Media, Telecommunications)
   - Vector quantisation for color reduction
   - JPEG-like compression
   - Impact: 10-100x compression ratios

4. **Gene Expression Analysis** (Genomics)
   - Cluster genes with similar expression patterns
   - Disease subtype discovery
   - Impact: Personalized medicine

### MCMC Methods
1. **Bayesian A/B Testing** (Tech, E-commerce)
   - Probability statements: P(B > A)
   - Uncertainty quantification
   - Impact: Better decisions, faster experiments

2. **Clinical Trials** (Healthcare)
   - Adaptive trial designs
   - Early stopping rules
   - Impact: Faster drug approval, patient safety

3. **Risk Modeling** (Finance)
   - Portfolio optimization under uncertainty
   - Value-at-Risk (VaR) estimation
   - Impact: Better risk management

4. **Bayesian Neural Networks** (AI Research)
   - Uncertainty in deep learning
   - Robust predictions
   - Impact: Safer AI systems

## 📝 Assignments

### Assignment 1: Customer Segmentation (30 points)
- Apply k-Means to real customer data
- Choose optimal k
- Provide business recommendations

### Assignment 2: SOM Visualization (30 points)
- Implement SOM for MNIST digits
- Create U-Matrix and component planes
- Analyze topology preservation

### Assignment 3: Bayesian A/B Testing (40 points)
- Use MCMC for A/B test analysis
- Implement Metropolis-Hastings or Gibbs
- Make business decision with uncertainty

## 🎓 Additional Resources

### Books
- **Pattern Recognition and Machine Learning** by Christopher Bishop
  - Chapter 9: Mixture Models and EM
  - Chapter 11: Sampling Methods
- **Bayesian Data Analysis** by Gelman et al.
  - Comprehensive MCMC coverage
- **The Elements of Statistical Learning** by Hastie et al.
  - Chapter 14: Unsupervised Learning

### Online Courses
- **Andrew Ng's Machine Learning** (Coursera) - k-Means
- **Probabilistic Programming & Bayesian Methods for Hackers** (free online)
- **Fast.ai** - Practical Deep Learning (includes clustering)

### Software Libraries
- **Scikit-learn**: k-Means, DBSCAN, GMM
- **MiniSom**: Self-Organizing Maps
- **PyMC3**: Probabilistic programming with MCMC
- **Stan**: High-performance Bayesian inference
- **ArviZ**: MCMC diagnostics and visualization

### Research Papers
- Kohonen (1990): "The Self-Organizing Map"
- Metropolis et al. (1953): "Equation of State Calculations"
- Arthur & Vassilvitskii (2007): "k-means++: The Advantages of Careful Seeding"

## 💡 Tips for Success

### Unsupervised Learning
1. **Always normalize features** before k-Means
2. **Try multiple random initializations** (k-means++)
3. **Validate clusters** with domain knowledge
4. **Use multiple metrics** (Elbow + Silhouette)
5. **Visualize results** (scatter plots, heatmaps)

### MCMC
1. **Always check convergence** (trace plots, R̂)
2. **Use multiple chains** from different starting points
3. **Discard burn-in samples** (10-50% of total)
4. **Monitor acceptance rate** (tune proposal distribution)
5. **Calculate effective sample size** (account for autocorrelation)

## 🐛 Common Pitfalls

### k-Means
- ❌ Forgetting to normalize features
- ❌ Using k-Means for non-spherical clusters
- ❌ Not checking multiple values of k
- ❌ Ignoring cluster interpretability

### SOM
- ❌ Grid too small (underfitting) or too large (overfitting)
- ❌ Too few training iterations
- ❌ Not decaying learning rate and neighborhood

### MCMC
- ❌ Not discarding burn-in samples
- ❌ Assuming convergence without diagnostics
- ❌ Ignoring autocorrelation
- ❌ Proposal distribution too narrow or too wide

## 📞 Support

For questions or issues:
1. Review the FAQs in the notebook
2. Check the Quick Reference Guide
3. Consult the textbook (Module 4 - TextBook 2 - C14-15)
4. Ask in discussion forums

## 🎉 Next Steps

After completing this module:
1. ✅ Complete all 3 assignments
2. ✅ Participate in discussion questions
3. ✅ Apply to your own datasets
4. ✅ Explore advanced topics:
   - Hierarchical clustering
   - DBSCAN (density-based clustering)
   - Gaussian Mixture Models (GMM)
   - Hamiltonian Monte Carlo (HMC)
   - Variational Inference

---

**Happy Learning! 🚀**

*Module 4 - Unsupervised Learning & MCMC Methods*

