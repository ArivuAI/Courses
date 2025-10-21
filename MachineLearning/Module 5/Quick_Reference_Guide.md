# Module 5: Graphical Models - Quick Reference Guide

## 🎯 Core Formulas and Algorithms

---

## Part 1: Bayesian Networks

### Joint Probability Factorization
```
P(X₁, X₂, ..., Xₙ) = ∏ᵢ₌₁ⁿ P(Xᵢ | Parents(Xᵢ))
```

**Example** (Exam Fear Network):
```
P(B, R, A, S) = P(B) × P(R|B) × P(A|B) × P(S|R,A)
```

### Conditional Probability (Bayes' Rule)
```
P(X | Y) = P(Y | X) × P(X) / P(Y)
```

### Marginalization
```
P(X) = Σᵧ P(X, Y)
```

### Conditional Independence
```
X ⊥ Y | Z  ⟺  P(X, Y | Z) = P(X | Z) × P(Y | Z)
```

**D-Separation Rules**:
1. **Chain**: X → Z → Y: X ⊥ Y | Z
2. **Fork**: X ← Z → Y: X ⊥ Y | Z
3. **Collider**: X → Z ← Y: X ⊥ Y (but NOT given Z!)

---

## Part 2: Hidden Markov Models

### Model Parameters
- **π**: Initial state probabilities, π(i) = P(S₀ = i)
- **A**: Transition probabilities, A(i,j) = P(Sₜ = j | Sₜ₋₁ = i)
- **B**: Emission probabilities, B(i,k) = P(Oₜ = k | Sₜ = i)

### Forward Algorithm (Evaluation)
**Goal**: Compute P(observations | model)

**Initialization** (t=0):
```
α(i, 0) = π(i) × B(i, o₀)
```

**Recursion** (t=1 to T-1):
```
α(j, t) = B(j, oₜ) × Σᵢ α(i, t-1) × A(i, j)
```

**Termination**:
```
P(O₁, O₂, ..., Oₜ | model) = Σᵢ α(i, T-1)
```

**Complexity**: O(N² × T)

### Viterbi Algorithm (Decoding)
**Goal**: Find most likely state sequence

**Initialization** (t=0):
```
δ(i, 0) = π(i) × B(i, o₀)
φ(i, 0) = 0
```

**Recursion** (t=1 to T-1):
```
δ(j, t) = B(j, oₜ) × maxᵢ [δ(i, t-1) × A(i, j)]
φ(j, t) = argmaxᵢ [δ(i, t-1) × A(i, j)]
```

**Termination**:
```
Best final state: q* = argmaxᵢ δ(i, T-1)
Best probability: P* = maxᵢ δ(i, T-1)
```

**Backtracking**:
```
Path: qₜ = φ(qₜ₊₁, t+1) for t = T-2 down to 0
```

**Complexity**: O(N² × T)

### Baum-Welch Algorithm (Learning)
**Goal**: Learn A, B, π from observations

**E-Step** (Expectation):
```
ξ(i, j, t) = α(i,t) × A(i,j) × B(j,oₜ₊₁) × β(j,t+1) / P(O)
γ(i, t) = Σⱼ ξ(i, j, t)
```

**M-Step** (Maximization):
```
π(i) = γ(i, 0)
A(i,j) = Σₜ ξ(i,j,t) / Σₜ γ(i,t)
B(i,k) = Σₜ:oₜ=k γ(i,t) / Σₜ γ(i,t)
```

**Complexity**: O(N² × T × iterations)

---

## Part 3: Kalman Filter

### System Model
**State Equation**:
```
x(t+1) = A × x(t) + B × u(t) + w(t)
```
- x: state vector (n × 1)
- u: control input (m × 1)
- w: process noise ~ N(0, Q)

**Measurement Equation**:
```
y(t) = H × x(t) + v(t)
```
- y: measurement vector (k × 1)
- v: measurement noise ~ N(0, R)

### Kalman Filter Algorithm

**Predict Step**:
```
x̂⁻ = A × x̂ + B × u
P⁻ = A × P × Aᵀ + Q
```

**Update Step**:
```
K = P⁻ × Hᵀ × (H × P⁻ × Hᵀ + R)⁻¹
x̂ = x̂⁻ + K × (y - H × x̂⁻)
P = (I - K × H) × P⁻
```

**Where**:
- x̂: state estimate
- P: error covariance
- K: Kalman gain
- Q: process noise covariance
- R: measurement noise covariance

**Complexity**: O(n³) per time step (matrix inversion)

---

## 🔧 Implementation Patterns

### Bayesian Network Template
```python
# Create network
bn = BayesianNetwork()

# Add root node (no parents)
bn.add_node('X', domain=[True, False], parents=None, cpt=0.5)

# Add child node
bn.add_node('Y', domain=[True, False], parents=['X'], 
            cpt={(True,): 0.8, (False,): 0.2})

# Query
prob = bn.query('Y', True, evidence={'X': True})
```

### HMM Template
```python
# Create HMM
hmm = HiddenMarkovModel(states=['S1', 'S2'], 
                        observations=['O1', 'O2'])

# Set probabilities
hmm.set_start_prob({'S1': 0.6, 'S2': 0.4})
hmm.set_trans_prob({('S1','S1'): 0.7, ('S1','S2'): 0.3, ...})
hmm.set_emit_prob({('S1','O1'): 0.9, ('S1','O2'): 0.1, ...})

# Forward Algorithm
alpha, prob = hmm.forward(['O1', 'O2', 'O1'])

# Viterbi Algorithm
path, path_prob = hmm.viterbi(['O1', 'O2', 'O1'])
```

### Kalman Filter Template
```python
# Define matrices
A = np.array([[1, dt], [0, 1]])  # State transition
H = np.array([[1, 0]])            # Observation
Q = np.eye(2) * 0.1               # Process noise
R = np.array([[5.0]])             # Measurement noise

# Initialize
x0 = np.array([[0], [0]])
P0 = np.eye(2) * 100

# Create filter
kf = KalmanFilter(A, B, H, Q, R, x0, P0)

# Run filter
estimates = kf.filter(measurements)
```

---

## 📊 Decision Framework

### When to Use Each Model

| Problem Type | Model | Reason |
|--------------|-------|--------|
| **Static causal relationships** | Bayesian Network | Directed edges represent causation |
| **Spatial/symmetric relationships** | Markov Random Field | Undirected edges for correlation |
| **Sequential data, hidden states** | HMM | Temporal evolution with observations |
| **Linear tracking, Gaussian noise** | Kalman Filter | Optimal for linear systems |
| **Non-linear tracking** | Extended Kalman Filter | Linearization around estimate |
| **Non-Gaussian, multi-modal** | Particle Filter | Represents arbitrary distributions |

### Bayesian Network vs. HMM

**Use Bayesian Network when**:
- Relationships are static (no time component)
- You have expert knowledge of causal structure
- Variables have clear parent-child relationships
- Example: Medical diagnosis, spam filtering

**Use HMM when**:
- Data is sequential/temporal
- Hidden states evolve over time
- Observations depend on current hidden state
- Example: Speech recognition, activity tracking

### Kalman Filter vs. Particle Filter

**Use Kalman Filter when**:
- System dynamics are linear
- Noise is Gaussian
- Computational efficiency is critical
- Example: GPS tracking, simple robot localization

**Use Particle Filter when**:
- System is highly non-linear
- Noise is non-Gaussian or multi-modal
- Multiple hypotheses need to be tracked
- Example: Robot localization in complex environments

---

## 🎯 Common Workflows

### Workflow 1: Bayesian Network Inference
```
1. Define network structure (nodes and edges)
2. Set conditional probability tables (CPTs)
3. Collect evidence (observations)
4. Query for unknown variables
5. Interpret results (probabilities)
```

### Workflow 2: HMM Sequence Analysis
```
1. Define states and observations
2. Set transition and emission probabilities
3. Collect observation sequence
4. Run Forward (evaluate) or Viterbi (decode)
5. Interpret state sequence or probability
```

### Workflow 3: Kalman Filter Tracking
```
1. Define state and measurement models (A, H)
2. Estimate noise covariances (Q, R)
3. Initialize state estimate (x₀, P₀)
4. For each time step:
   a. Predict next state
   b. Receive measurement
   c. Update estimate
5. Extract filtered trajectory
```

---

## 💡 Optimization Tips

### Bayesian Networks
- **Use variable elimination** instead of enumeration for large networks
- **Order matters**: Eliminate variables in optimal order
- **Approximate inference**: Use sampling (MCMC, Gibbs) for very large networks

### HMMs
- **Use log probabilities** to avoid underflow:
  ```python
  log_alpha = np.log(alpha)
  ```
- **Vectorize operations** with NumPy for speed
- **Scaling**: Normalize α and δ at each time step

### Kalman Filter
- **Pre-compute constant matrices** (A, H, Q, R)
- **Use Cholesky decomposition** for matrix inversion
- **Joseph form** for numerical stability:
  ```python
  P = (I - K@H) @ P @ (I - K@H).T + K @ R @ K.T
  ```

---

## 🐛 Debugging Checklist

### Bayesian Networks
- [ ] CPTs sum to 1.0 for each parent configuration
- [ ] No cycles in the graph (DAG property)
- [ ] All nodes have defined CPTs
- [ ] Evidence variables are in the network

### HMMs
- [ ] Transition matrix rows sum to 1.0
- [ ] Emission matrix rows sum to 1.0
- [ ] Initial probabilities sum to 1.0
- [ ] Observations are in the defined set
- [ ] Using log probabilities for long sequences

### Kalman Filter
- [ ] Matrix dimensions match (A: n×n, H: k×n, etc.)
- [ ] Q and R are positive definite
- [ ] P remains positive definite (check eigenvalues)
- [ ] Kalman gain K is in valid range [0, 1]
- [ ] Innovation (y - H@x) is reasonable

---

## 📈 Performance Metrics

### Bayesian Networks
- **Accuracy**: % of correct predictions
- **Log-likelihood**: Σ log P(data | model)
- **AUC-ROC**: For binary classification tasks

### HMMs
- **Accuracy**: % of correctly decoded states (if ground truth known)
- **Log-likelihood**: log P(observations | model)
- **Perplexity**: exp(-log P / T) - lower is better

### Kalman Filter
- **RMSE**: √(Σ(x_true - x_est)² / T)
- **Innovation**: Should be zero-mean Gaussian
- **Consistency**: Innovation covariance matches theoretical value

---

## 🔑 Key Insights

1. **Graphical models exploit structure** to make inference tractable
2. **Conditional independence** is the key to efficiency
3. **HMMs are Bayesian Networks** with temporal structure
4. **Kalman Filter is optimal** for linear Gaussian systems
5. **Trade-off**: Exact inference (slow) vs. approximate (fast)
6. **Interpretability**: Graphical models are more explainable than black-box models

---

**Module 5: Graphical Models - Quick Reference**  
*Arivu AI Machine Learning Course*

