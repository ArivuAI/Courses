# Experiment 7: Bayesian Networks for Medical Diagnosis

## 📚 Overview

This experiment teaches you how to build and use **Bayesian Networks** for probabilistic reasoning and medical diagnosis. You'll learn to read patient data, construct a probabilistic graphical model, and calculate the likelihood of diseases given observed symptoms.

---

## 🎯 Learning Objectives

By completing this experiment, you will:

1. ✅ Understand Bayesian Network structure (nodes, edges, DAG)
2. ✅ Learn Conditional Probability Tables (CPTs)
3. ✅ Implement Bayes' Theorem for inference
4. ✅ Calculate posterior probabilities given evidence
5. ✅ Perform diagnostic reasoning (symptoms → disease)
6. ✅ Visualize network structure and probabilities
7. ✅ Apply Bayesian Networks to real-world problems
8. ✅ Handle uncertainty in predictions

---

## 📊 Dataset

### Medical Diagnosis Dataset

**Domain**: Healthcare - Disease Diagnosis  
**File**: `data/medical_diagnosis_data.json`  
**Size**: ~300 lines  
**Format**: JSON

**Contents**:
- **500 patient records** (simulated for educational purposes)
- **4 diseases**: Flu, COVID-19, Common Cold, Allergies
- **3 risk factors**: Season, Age Group, Vaccination Status
- **5 symptoms**: Fever, Cough, Fatigue, Breathing Difficulty, Runny Nose
- **Network structure**: Nodes, edges, and relationships
- **Prior probabilities**: P(Season), P(Age), P(Vaccination)
- **Conditional probabilities**: P(Symptom | Disease)

**Network Structure**:
```
Season ────┐
           ├──→ Disease ──→ Fever
Age ───────┤           ├──→ Cough
           │           ├──→ Fatigue
Vaccination┘           ├──→ Breathing_Difficulty
                       └──→ Runny_Nose
```

---

## 🚀 Quick Start

### Prerequisites

```bash
# Required libraries
pip install numpy pandas matplotlib seaborn
```

### Running the Experiment

1. **Open Jupyter Notebook**:
   ```bash
   jupyter notebook Experiment_7_Bayesian_Networks.ipynb
   ```

2. **Run all cells** in sequence (Cell → Run All)

3. **Follow along** with explanations and visualizations

4. **Complete exercises** at the end of each section

---

## 📖 Notebook Structure

### Part 1: Introduction & Theory
- Simple explanation (Doctor's diagnosis analogy)
- Real-world impact and applications
- Background theory (Bayes' Theorem, DAG, CPTs)
- Mathematical foundation

### Part 2: Data Exploration
- Load medical diagnosis dataset
- Explore patient records
- Visualize data distributions
- Understand variable relationships

### Part 3: Network Construction
- Understand Bayesian Network structure
- Define nodes and edges
- Create Conditional Probability Tables (CPTs)
- Validate probability constraints

### Part 4: Bayesian Inference
- Implement Bayes' Theorem
- Calculate posterior probabilities
- Perform diagnostic reasoning
- Test on multiple patient cases

### Part 5: Visualization & Analysis
- Visualize network structure
- Plot probability distributions
- Compare predicted vs actual diagnoses
- Sensitivity analysis

### Part 6: Advanced Topics
- Handling missing data
- Learning CPTs from data
- Network structure learning
- Real-world applications

---

## 🎓 Key Concepts

### Bayesian Network
A probabilistic graphical model representing variables and their conditional dependencies via a Directed Acyclic Graph (DAG).

### Components

**1. Nodes (Variables)**
- Represent random variables
- Can be discrete or continuous
- Examples: Disease, Fever, Age

**2. Edges (Dependencies)**
- Directed arrows showing influence
- Parent → Child relationship
- Example: Disease → Fever

**3. Conditional Probability Tables (CPTs)**
- P(Child | Parents)
- Quantifies relationship strength
- Example: P(Fever=Yes | Disease=Flu) = 0.85

### Bayes' Theorem

```
P(Disease | Symptoms) = P(Symptoms | Disease) × P(Disease) / P(Symptoms)
```

Where:
- **P(Disease | Symptoms)**: Posterior (what we want)
- **P(Symptoms | Disease)**: Likelihood (from CPTs)
- **P(Disease)**: Prior (base rate)
- **P(Symptoms)**: Evidence (normalizing constant)

---

## 💡 Real-World Applications

### 1. Healthcare
- **Medical Diagnosis**: IBM Watson for cancer diagnosis
- **Disease Outbreak Prediction**: CDC epidemic forecasting
- **Treatment Planning**: Personalized medicine
- **Drug Discovery**: Predict interactions

### 2. Spam Filtering
- **Gmail**: 99.9% spam detection accuracy
- **Adaptive Learning**: Learns from user behavior

### 3. Autonomous Vehicles
- **Tesla Autopilot**: Pedestrian behavior prediction
- **Sensor Fusion**: Combine camera, radar, lidar
- **Decision Making**: Brake, turn, accelerate

### 4. Finance
- **Credit Scoring**: Loan default prediction
- **Fraud Detection**: PayPal transaction analysis
- **Risk Assessment**: Portfolio management

### 5. Cybersecurity
- **Intrusion Detection**: Network attack identification
- **Malware Classification**: Virus variant detection

---

## 📊 Example Usage

### Simple Diagnosis

```python
# Define patient symptoms
symptoms = {
    'Fever': 'Yes',
    'Cough': 'Yes',
    'Fatigue': 'Yes',
    'Breathing_Difficulty': 'No',
    'Runny_Nose': 'No'
}

# Calculate disease probabilities
disease_probs = calculate_disease_probability(symptoms)

# Display results
for disease, prob in sorted(disease_probs.items(), key=lambda x: x[1], reverse=True):
    print(f"{disease}: {prob:.2%}")

# Output:
# Flu: 65.32%
# COVID-19: 23.45%
# Common_Cold: 8.12%
# Allergies: 2.11%
# None: 1.00%
```

---

## 🎯 Assignments

### Assignment 1: Basic Inference (2-3 hours)
- Implement Bayesian inference for 5 new patient cases
- Calculate posterior probabilities
- Compare with actual diagnoses
- Analyze errors

### Assignment 2: Network Modification (3-4 hours)
- Add new symptom node (Headache)
- Define CPTs for new symptom
- Test modified network
- Compare performance

### Assignment 3: Real-World Application (4-5 hours)
- Choose a domain (spam filtering, credit scoring, etc.)
- Design Bayesian Network structure
- Define CPTs
- Implement and test
- Write report

---

## 📚 Further Reading

### Books
- "Probabilistic Graphical Models" by Daphne Koller
- "Bayesian Reasoning and Machine Learning" by David Barber
- "Artificial Intelligence: A Modern Approach" by Russell & Norvig

### Online Resources
- [Bayesian Networks Tutorial](https://www.bayesserver.com/docs/introduction/bayesian-networks)
- [pgmpy Documentation](https://pgmpy.org/)
- [Coursera: Probabilistic Graphical Models](https://www.coursera.org/specializations/probabilistic-graphical-models)

### Research Papers
- Pearl, J. (1988). "Probabilistic Reasoning in Intelligent Systems"
- Heckerman, D. (1995). "A Tutorial on Learning with Bayesian Networks"

---

## 🔧 Troubleshooting

### Common Issues

**Issue 1: Probabilities don't sum to 1**
- **Solution**: Check CPT definitions, ensure all states covered

**Issue 2: Zero probability results**
- **Solution**: Add small smoothing constant (Laplace smoothing)

**Issue 3: Slow inference**
- **Solution**: Use approximate inference (sampling methods)

**Issue 4: Poor accuracy**
- **Solution**: Review CPTs, collect more data, refine network structure

---

## 🤝 Contributing

Found an issue or have suggestions? Please:
1. Check existing issues
2. Create detailed bug report
3. Suggest improvements
4. Share your results!

---

## 📝 License

This experiment is part of the Arivu AI Machine Learning Course.  
For educational purposes only.

---

## 👥 Authors

**Arivu AI Team**  
Course: Machine Learning  
Module: Probabilistic Reasoning  
Experiment: 7 - Bayesian Networks

---

## 📞 Support

Need help? Contact:
- **Email**: support@arivuai.com
- **Forum**: [Arivu AI Community](https://community.arivuai.com)
- **Office Hours**: Monday-Friday, 9 AM - 5 PM IST

---

## 🎉 Acknowledgments

- Medical knowledge from WHO and CDC guidelines
- Bayesian Network theory from Judea Pearl's work
- Dataset inspired by real-world medical diagnosis systems
- Visualization techniques from data science community

---

**Happy Learning! 🚀**

*Master Bayesian Networks and unlock the power of probabilistic reasoning!*

