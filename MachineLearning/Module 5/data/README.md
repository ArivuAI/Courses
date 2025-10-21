# Module 5 Data Files

## 📊 Overview

This folder contains datasets for Module 5: Graphical Models examples and exercises.

---

## 📁 Files

### 1. `bayesian_network_exam_data.csv`
**Purpose**: Student exam performance data for Bayesian Network analysis  
**Rows**: 500 students  
**Columns**: 5
- `student_id`: Unique identifier (1-500)
- `boring_class`: Whether class was boring (True/False)
- `revised`: Whether student revised (True/False)
- `attended`: Whether student attended class (True/False)
- `scared`: Whether student was scared before exam (True/False)

**Use Cases**:
- Train Bayesian Networks from data
- Validate inference results
- Learn conditional probability tables
- Test structure learning algorithms

**Example**:
```csv
student_id,boring_class,revised,attended,scared
1,True,False,False,True
2,False,True,True,False
```

---

### 2. `hmm_student_behavior_sequences.csv`
**Purpose**: Student daily behavior observation sequences for HMM analysis  
**Rows**: 100 sequences (students)  
**Columns**: 8
- `sequence_id`: Unique identifier (1-100)
- `day_1` to `day_7`: Observations for each day (Tired/Hungover/Scared/Fine)

**Use Cases**:
- Test Forward Algorithm
- Test Viterbi Algorithm
- Train HMM with Baum-Welch
- Evaluate HMM performance

**Example**:
```csv
sequence_id,day_1,day_2,day_3,day_4,day_5,day_6,day_7
1,Tired,Tired,Fine,Scared,Fine,Hungover,Tired
2,Fine,Fine,Scared,Scared,Fine,Fine,Fine
```

---

### 3. `kalman_filter_gps_tracking.csv`
**Purpose**: GPS tracking data with noisy measurements for Kalman Filter  
**Rows**: 200 time steps  
**Columns**: 7
- `time_step`: Time index (0-199)
- `true_position`: Actual position (meters)
- `true_velocity`: Actual velocity (m/s)
- `measured_position`: Noisy GPS measurement (meters)
- `measurement_noise`: Noise level (meters)
- `process_noise`: System uncertainty
- `scenario`: Tracking scenario (constant_velocity/acceleration/turning)

**Use Cases**:
- Test Kalman Filter implementation
- Compare filtered vs. raw measurements
- Analyze noise sensitivity
- Evaluate RMSE performance

**Example**:
```csv
time_step,true_position,true_velocity,measured_position,measurement_noise,process_noise,scenario
0,0.0,10.0,2.3,5.0,0.1,constant_velocity
1,10.0,10.0,8.7,5.0,0.1,constant_velocity
```

---

### 4. `medical_diagnosis_data.csv`
**Purpose**: Medical symptoms and diagnoses for Bayesian Network (Assignment 1)  
**Rows**: 1000 patients  
**Columns**: 5
- `patient_id`: Unique identifier (1-1000)
- `fever`: Has fever (Yes/No)
- `cough`: Has cough (Yes/No)
- `loss_of_smell`: Has loss of smell (Yes/No)
- `diagnosis`: Disease (Flu/COVID/None)

**Use Cases**:
- Assignment 1: Medical diagnosis Bayesian Network
- Learn CPTs from real data
- Validate diagnostic accuracy
- Compare with expert-defined network

**Example**:
```csv
patient_id,fever,cough,loss_of_smell,diagnosis
1,Yes,Yes,Yes,COVID
2,Yes,Yes,No,Flu
3,No,No,No,None
```

---

### 5. `weather_sequences.csv`
**Purpose**: Weather observation sequences for HMM (Assignment 2)  
**Rows**: 200 sequences  
**Columns**: 11
- `sequence_id`: Unique identifier (1-200)
- `day_1` to `day_10`: Observations (Dry/Wet/Damp)

**Use Cases**:
- Assignment 2: Weather prediction HMM
- Test Forward and Viterbi algorithms
- Evaluate sequence probability
- Decode hidden weather states

**Example**:
```csv
sequence_id,day_1,day_2,day_3,day_4,day_5,day_6,day_7,day_8,day_9,day_10
1,Dry,Dry,Damp,Wet,Wet,Damp,Dry,Dry,Dry,Damp
2,Wet,Wet,Wet,Damp,Dry,Dry,Dry,Damp,Wet,Wet
```

---

### 6. `robot_tracking_data.csv`
**Purpose**: 2D robot position data for Kalman Filter (Assignment 3)  
**Rows**: 300 time steps  
**Columns**: 9
- `time_step`: Time index (0-299)
- `true_x`: Actual x position (meters)
- `true_y`: Actual y position (meters)
- `true_vx`: Actual x velocity (m/s)
- `true_vy`: Actual y velocity (m/s)
- `measured_x`: Noisy GPS x measurement
- `measured_y`: Noisy GPS y measurement
- `noise_level`: Measurement noise std dev
- `trajectory_type`: Path type (straight/circular/zigzag)

**Use Cases**:
- Assignment 3: Robot localization
- 2D Kalman Filter implementation
- Multi-dimensional state estimation
- Trajectory visualization

**Example**:
```csv
time_step,true_x,true_y,true_vx,true_vy,measured_x,measured_y,noise_level,trajectory_type
0,0.0,0.0,1.0,0.5,1.2,-0.8,2.0,straight
1,1.0,0.5,1.0,0.5,2.3,1.1,2.0,straight
```

---

## 🔧 Data Generation

All datasets were generated using `generate_datasets.py` with:
- **Reproducible random seed**: 42
- **Realistic probability distributions**
- **Controlled noise levels**
- **Multiple scenarios for robustness**

To regenerate datasets:
```bash
cd "Module 5/data"
python generate_datasets.py
```

---

## 📊 Dataset Statistics

| Dataset | Rows | Columns | Size (KB) | Use Case |
|---------|------|---------|-----------|----------|
| `bayesian_network_exam_data.csv` | 500 | 5 | ~15 | Bayesian Network training |
| `hmm_student_behavior_sequences.csv` | 100 | 8 | ~8 | HMM testing |
| `kalman_filter_gps_tracking.csv` | 200 | 7 | ~12 | Kalman Filter demo |
| `medical_diagnosis_data.csv` | 1000 | 5 | ~25 | Assignment 1 |
| `weather_sequences.csv` | 200 | 11 | ~15 | Assignment 2 |
| `robot_tracking_data.csv` | 300 | 9 | ~20 | Assignment 3 |

**Total**: 2,300 rows, ~95 KB

---

## 🎓 Educational Use

### For Students
1. **Load data**: Use pandas to read CSV files
2. **Explore data**: Visualize distributions and patterns
3. **Train models**: Learn parameters from data
4. **Validate results**: Compare with theoretical predictions
5. **Complete assignments**: Use assignment-specific datasets

### For Instructors
1. **Demonstrations**: Use in live coding sessions
2. **Assignments**: Provide as starter data
3. **Grading**: Consistent datasets for fair evaluation
4. **Extensions**: Students can generate their own variations

---

## 📝 Loading Data Examples

### Python (Pandas)
```python
import pandas as pd

# Load Bayesian Network data
bn_data = pd.read_csv('Module 5/data/bayesian_network_exam_data.csv')
print(bn_data.head())

# Load HMM sequences
hmm_data = pd.read_csv('Module 5/data/hmm_student_behavior_sequences.csv')
print(hmm_data.head())

# Load Kalman Filter tracking data
kf_data = pd.read_csv('Module 5/data/kalman_filter_gps_tracking.csv')
print(kf_data.head())
```

### NumPy
```python
import numpy as np

# Load as NumPy array (skip header)
data = np.genfromtxt('Module 5/data/kalman_filter_gps_tracking.csv', 
                     delimiter=',', skip_header=1)
```

---

## 🔍 Data Quality

All datasets include:
- ✅ **No missing values**: Complete data for all rows
- ✅ **Consistent formatting**: Standard CSV format
- ✅ **Realistic distributions**: Based on domain knowledge
- ✅ **Controlled noise**: Known noise parameters for validation
- ✅ **Multiple scenarios**: Diverse examples for robustness

---

## 📚 References

**Data Generation Methods**:
- Bayesian Networks: Ancestral sampling from CPTs
- HMMs: Forward sampling from transition/emission matrices
- Kalman Filter: Linear dynamics with Gaussian noise

**Validation**:
- All datasets tested with notebook examples
- Probability distributions verified
- Noise levels calibrated for educational clarity

---

## 🚀 Next Steps

After using these datasets:
1. Generate your own variations with different parameters
2. Collect real-world data for your domain
3. Apply learned techniques to personal projects
4. Share insights with the learning community

---

**Module 5 Data Files**  
*Arivu AI Machine Learning Course*  
*Last Updated: 2025-10-16*

