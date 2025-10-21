# Module 5: Graphical Models

## 📚 Bayesian Networks, Markov Random Fields, Hidden Markov Models, and Tracking Methods

Welcome to Module 5 of the Arivu AI Machine Learning Course! This module covers **probabilistic graphical models** - powerful frameworks for representing and reasoning about complex probability distributions.

---

## 🎯 Module Overview

### Part 1: Bayesian Networks
Learn to build and query directed graphical models for causal reasoning:
- Building Bayesian Networks from expert knowledge
- Conditional probability tables (CPTs)
- Exact inference via enumeration
- Variable elimination for efficiency
- Applications: Medical diagnosis, spam filtering, risk assessment

### Part 2: Hidden Markov Models (HMMs)
Master sequential models with hidden states:
- HMM fundamentals and the Markov property
- **Forward Algorithm** - Evaluate observation probability
- **Viterbi Algorithm** - Decode most likely state sequence
- **Baum-Welch Algorithm** - Learn model parameters
- Applications: Speech recognition, gene prediction, activity tracking

### Part 3: Tracking Methods
Implement state estimation algorithms:
- **Kalman Filter** - Optimal tracking for linear Gaussian systems
- Predict-Update cycle
- Handling noisy sensor measurements
- Applications: GPS navigation, robotics, aerospace, finance

---

## 📦 File Structure

```
Module 5/
├── Module_5_Graphical_Models.ipynb          # Main notebook (~1,796 lines)
├── README.md                                 # This file
├── Quick_Reference_Guide.md                  # Formulas and patterns
├── COMPLETION_SUMMARY.md                     # Project statistics
├── ml_module5_slides.txt                    # Lecture slides (644 lines)
├── data/                                     # Data files (to be created)
└── Reference Materials/
    ├── Module 5 - TextBook 2 - C16 - P321-359.pdf
    └── Module 5 - TextBook 2 - C16 - P321-359.txt
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- NumPy, Pandas, Matplotlib, Seaborn, SciPy
- Basic probability and linear algebra

### Installation
```bash
# Install required packages
pip install numpy pandas matplotlib seaborn scipy jupyter

# Navigate to Module 5
cd "Module 5"

# Launch Jupyter Notebook
jupyter notebook Module_5_Graphical_Models.ipynb
```

### Running the Notebook
1. Open `Module_5_Graphical_Models.ipynb`
2. Run cells sequentially (Shift + Enter)
3. Complete the exercises and assignments
4. Experiment with parameters and visualizations

---

## 📊 Key Concepts

### Bayesian Networks
- **Directed Acyclic Graph (DAG)**: Nodes = variables, edges = causal relationships
- **Conditional Independence**: Efficient probability factorization
- **Inference**: Computing P(Query | Evidence) via enumeration
- **Example**: Exam fear network (Boring → Revised/Attended → Scared)

### Hidden Markov Models
- **Hidden States**: Unobservable states that evolve over time
- **Observations**: What we actually see
- **Transition Probabilities**: P(S_t | S_{t-1})
- **Emission Probabilities**: P(O_t | S_t)
- **Example**: Student behavior (hidden: TV/Party/Pub/Study, observed: Tired/Hungover/Scared/Fine)

### Kalman Filter
- **State Estimation**: Optimal tracking from noisy measurements
- **Predict Step**: Forecast next state using dynamics model
- **Update Step**: Correct prediction using measurement
- **Kalman Gain**: Optimal balance between model and measurement
- **Example**: Tracking car position and velocity from noisy GPS

---

## 🎓 Learning Objectives

By the end of this module, you will be able to:

✅ Build Bayesian Networks for probabilistic reasoning  
✅ Perform inference to answer queries under uncertainty  
✅ Implement HMM algorithms (Forward, Viterbi)  
✅ Apply Kalman Filters to tracking problems  
✅ Choose the right graphical model for your application  
✅ Handle missing data and noisy measurements  
✅ Explain model decisions (interpretability)  

---

## 💼 Real-World Applications

### 1. Healthcare - Disease Diagnosis ($50B market)
- **Problem**: Symptoms can have multiple causes
- **Solution**: Bayesian Networks model symptom-disease relationships
- **Impact**: 23% accuracy improvement, 31% reduction in unnecessary tests
- **Example**: Mayo Clinic cardiovascular risk assessment

### 2. Finance - Fraud Detection
- **Problem**: Complex patterns of fraudulent behavior
- **Solution**: HMMs model transaction sequences
- **Impact**: 87% fraud detection rate, 40% reduction in false positives
- **Business Value**: Banks lose $28B annually to fraud

### 3. Autonomous Vehicles - Object Tracking
- **Problem**: Track multiple moving objects from noisy sensors
- **Solution**: Kalman Filter tracks position and velocity
- **Impact**: Real-time processing of 100 objects/second
- **Market**: $75B GPS navigation market

### 4. Speech Recognition - Voice Assistants
- **Problem**: Convert audio to text with 97%+ accuracy
- **Solution**: HMMs model phoneme sequences
- **Impact**: Powers Siri, Alexa, Google Assistant ($10B+ market)

---

## 📝 Assignments

### Assignment 1: Medical Diagnosis Bayesian Network (30 points)
Build a Bayesian Network to diagnose Flu vs. COVID-19 from symptoms.
- Define network structure
- Set conditional probability tables
- Perform diagnostic inference
- Write analysis report

### Assignment 2: Weather Prediction with HMM (35 points)
Implement HMM for weather state prediction.
- Define states and observations
- Implement Forward and Viterbi algorithms
- Generate synthetic data and evaluate accuracy
- Analyze performance

### Assignment 3: Robot Localization with Kalman Filter (35 points)
Track robot position from noisy GPS measurements.
- Simulate 2D robot motion
- Implement Kalman Filter
- Compare with raw measurements
- Analyze noise sensitivity

---

## 🔑 Key Formulas

### Bayesian Network Joint Probability
```
P(X₁, X₂, ..., Xₙ) = ∏ᵢ P(Xᵢ | Parents(Xᵢ))
```

### HMM Forward Algorithm
```
α(i,t) = P(oₜ | i) × Σⱼ α(j,t-1) × P(j→i)
P(observations) = Σᵢ α(i,T)
```

### HMM Viterbi Algorithm
```
δ(i,t) = P(oₜ | i) × maxⱼ [δ(j,t-1) × P(j→i)]
Best path: backtrack from argmax δ(i,T)
```

### Kalman Filter Predict
```
x_pred = A @ x + B @ u
P_pred = A @ P @ A.T + Q
```

### Kalman Filter Update
```
K = P @ H.T @ inv(H @ P @ H.T + R)
x = x_pred + K @ (y - H @ x_pred)
P = (I - K @ H) @ P_pred
```

---

## 🛠️ Implementation Highlights

### Classes Implemented
1. **BayesianNetwork** (~150 lines)
   - Add nodes with parents and CPTs
   - Exact inference via enumeration
   - Query method for probabilistic reasoning

2. **HiddenMarkovModel** (~120 lines)
   - Forward Algorithm (evaluation)
   - Viterbi Algorithm (decoding)
   - Support for arbitrary states and observations

3. **KalmanFilter** (~100 lines)
   - Predict step (state propagation)
   - Update step (measurement correction)
   - History tracking for visualization

### Examples Included
- **Exam Fear Network**: Student anxiety prediction
- **Student Behavior HMM**: Activity tracking from observations
- **Car Tracking**: Position and velocity estimation from noisy GPS

---

## 📚 Additional Resources

### Books
- "Probabilistic Graphical Models" by Koller & Friedman
- "Pattern Recognition and Machine Learning" by Bishop (Chapters 8, 13)
- "Artificial Intelligence: A Modern Approach" by Russell & Norvig (Chapters 14, 15)

### Online Courses
- Stanford CS228: Probabilistic Graphical Models
- Coursera: Probabilistic Graphical Models Specialization
- MIT 6.438: Algorithms for Inference

### Software Libraries
- **pgmpy**: Python library for Bayesian Networks
- **hmmlearn**: HMM implementation in Python
- **filterpy**: Kalman Filter library
- **PyMC3**: Probabilistic programming

### Papers
- Kalman, R.E. (1960). "A New Approach to Linear Filtering and Prediction Problems"
- Rabiner, L.R. (1989). "A Tutorial on Hidden Markov Models"
- Pearl, J. (1988). "Probabilistic Reasoning in Intelligent Systems"

---

## 💡 Tips for Success

### Understanding the Concepts
1. **Draw the graphs**: Visualize Bayesian Networks and HMMs
2. **Work through examples by hand**: Compute probabilities manually first
3. **Understand the algorithms**: Don't just memorize formulas
4. **Connect to real applications**: Think about where you'd use each model

### Debugging Common Issues
- **Bayesian Network**: Check that CPTs sum to 1.0
- **HMM**: Use log probabilities to avoid underflow
- **Kalman Filter**: Verify matrix dimensions match
- **All models**: Start with small examples, then scale up

### Performance Optimization
- **Bayesian Networks**: Use variable elimination instead of enumeration
- **HMMs**: Vectorize operations with NumPy
- **Kalman Filter**: Pre-compute constant matrices

---

## 🤔 Common Pitfalls

1. **Confusing causation and correlation** in Bayesian Networks
2. **Forgetting the Markov assumption** in HMMs
3. **Using Kalman Filter on non-linear systems** (use EKF instead)
4. **Not normalizing probabilities** (always check they sum to 1)
5. **Numerical underflow** in long HMM sequences (use log probabilities)

---

## 🎯 Next Steps

After completing this module:
1. ✅ Implement Baum-Welch algorithm for HMM learning
2. ✅ Study Extended Kalman Filter (EKF) for non-linear systems
3. ✅ Explore Particle Filters for non-Gaussian distributions
4. ✅ Learn about Conditional Random Fields (CRFs)
5. ✅ Study connections to deep learning (VAEs, Attention)

---

## 📞 Support

For questions or issues:
- Review the FAQs section in the notebook
- Check the Quick Reference Guide
- Consult the textbook (Chapter 16)
- Discuss with peers in study groups

---

## 🏆 Module Completion

To successfully complete this module:
- [ ] Run all notebook cells without errors
- [ ] Complete all 3 assignments
- [ ] Answer discussion questions
- [ ] Understand key concepts and formulas
- [ ] Apply models to a real-world problem

---

**Module 5: Graphical Models**  
*Arivu AI Machine Learning Course*  
*Empowering the next generation of AI practitioners*

