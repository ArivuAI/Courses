"""
Generate datasets for Module 5: Graphical Models

This script generates 6 CSV datasets for examples and assignments:
1. bayesian_network_exam_data.csv - Student exam data
2. hmm_student_behavior_sequences.csv - Student behavior sequences
3. kalman_filter_gps_tracking.csv - GPS tracking data
4. medical_diagnosis_data.csv - Medical diagnosis data
5. weather_sequences.csv - Weather observation sequences
6. robot_tracking_data.csv - 2D robot tracking data

Author: Arivu AI Machine Learning Course
Date: 2025-10-16
"""

import numpy as np
import pandas as pd
from typing import List, Tuple

# Set random seed for reproducibility
np.random.seed(42)

print("="*80)
print("Module 5: Graphical Models - Dataset Generation")
print("="*80)


# ============================================================================
# Dataset 1: Bayesian Network Exam Data
# ============================================================================

def generate_bayesian_network_data(n_samples: int = 500) -> pd.DataFrame:
    """
    Generate student exam data following Bayesian Network structure:
    Boring → Revised, Boring → Attended, (Revised, Attended) → Scared
    """
    print("\n1. Generating Bayesian Network Exam Data...")
    
    data = []
    
    for i in range(n_samples):
        # Root node: Boring (prior probability)
        boring = np.random.random() < 0.7  # P(Boring=True) = 0.7
        
        # Revised depends on Boring
        if boring:
            revised = np.random.random() < 0.2  # P(Revised=True | Boring=True) = 0.2
        else:
            revised = np.random.random() < 0.8  # P(Revised=True | Boring=False) = 0.8
        
        # Attended depends on Boring
        if boring:
            attended = np.random.random() < 0.4  # P(Attended=True | Boring=True) = 0.4
        else:
            attended = np.random.random() < 0.9  # P(Attended=True | Boring=False) = 0.9
        
        # Scared depends on both Revised and Attended
        if revised and attended:
            scared = np.random.random() < 0.1  # Well prepared
        elif revised and not attended:
            scared = np.random.random() < 0.3  # Revised but didn't attend
        elif not revised and attended:
            scared = np.random.random() < 0.5  # Attended but didn't revise
        else:
            scared = np.random.random() < 0.9  # Neither revised nor attended
        
        data.append({
            'student_id': i + 1,
            'boring_class': boring,
            'revised': revised,
            'attended': attended,
            'scared': scared
        })
    
    df = pd.DataFrame(data)
    print(f"   Generated {len(df)} student records")
    return df


# ============================================================================
# Dataset 2: HMM Student Behavior Sequences
# ============================================================================

def generate_hmm_sequences(n_sequences: int = 100, seq_length: int = 7) -> pd.DataFrame:
    """
    Generate student behavior observation sequences.
    Hidden states: TV, Party, Pub, Study
    Observations: Tired, Hungover, Scared, Fine
    """
    print("\n2. Generating HMM Student Behavior Sequences...")
    
    states = ['TV', 'Party', 'Pub', 'Study']
    observations = ['Tired', 'Hungover', 'Scared', 'Fine']
    
    # Transition matrix (from slides)
    trans_matrix = np.array([
        [0.3, 0.3, 0.2, 0.2],  # From TV
        [0.2, 0.4, 0.3, 0.1],  # From Party
        [0.1, 0.3, 0.4, 0.2],  # From Pub
        [0.2, 0.1, 0.1, 0.6]   # From Study
    ])
    
    # Emission matrix
    emit_matrix = np.array([
        [0.5, 0.1, 0.1, 0.3],  # TV → observations
        [0.3, 0.4, 0.1, 0.2],  # Party → observations
        [0.2, 0.5, 0.1, 0.2],  # Pub → observations
        [0.1, 0.0, 0.5, 0.4]   # Study → observations
    ])
    
    # Initial state probabilities
    start_prob = np.array([0.25, 0.25, 0.25, 0.25])
    
    data = []
    
    for seq_id in range(n_sequences):
        # Generate hidden state sequence
        state_seq = []
        obs_seq = []
        
        # Initial state
        state = np.random.choice(len(states), p=start_prob)
        state_seq.append(state)
        
        # Generate observation
        obs = np.random.choice(len(observations), p=emit_matrix[state])
        obs_seq.append(observations[obs])
        
        # Generate rest of sequence
        for _ in range(seq_length - 1):
            # Transition to next state
            state = np.random.choice(len(states), p=trans_matrix[state])
            state_seq.append(state)
            
            # Generate observation
            obs = np.random.choice(len(observations), p=emit_matrix[state])
            obs_seq.append(observations[obs])
        
        # Create row
        row = {'sequence_id': seq_id + 1}
        for day in range(seq_length):
            row[f'day_{day + 1}'] = obs_seq[day]
        
        data.append(row)
    
    df = pd.DataFrame(data)
    print(f"   Generated {len(df)} sequences of length {seq_length}")
    return df


# ============================================================================
# Dataset 3: Kalman Filter GPS Tracking
# ============================================================================

def generate_kalman_tracking_data(n_steps: int = 200) -> pd.DataFrame:
    """
    Generate GPS tracking data with constant velocity motion.
    """
    print("\n3. Generating Kalman Filter GPS Tracking Data...")
    
    # True initial state
    true_position = 0.0
    true_velocity = 10.0  # m/s
    
    # Noise parameters
    process_noise_std = 0.1  # Small process noise
    measurement_noise_std = 5.0  # GPS noise
    
    data = []
    
    for t in range(n_steps):
        # True dynamics (constant velocity with small noise)
        true_position += true_velocity + np.random.normal(0, process_noise_std)
        
        # Noisy measurement
        measured_position = true_position + np.random.normal(0, measurement_noise_std)
        
        data.append({
            'time_step': t,
            'true_position': round(true_position, 2),
            'true_velocity': round(true_velocity, 2),
            'measured_position': round(measured_position, 2),
            'measurement_noise': measurement_noise_std,
            'process_noise': process_noise_std,
            'scenario': 'constant_velocity'
        })
    
    df = pd.DataFrame(data)
    print(f"   Generated {len(df)} time steps")
    return df


# ============================================================================
# Dataset 4: Medical Diagnosis Data (Assignment 1)
# ============================================================================

def generate_medical_diagnosis_data(n_patients: int = 1000) -> pd.DataFrame:
    """
    Generate medical diagnosis data for Flu vs. COVID-19.
    """
    print("\n4. Generating Medical Diagnosis Data...")
    
    data = []
    
    # Disease prior probabilities
    disease_probs = {'Flu': 0.15, 'COVID': 0.10, 'None': 0.75}
    
    for patient_id in range(n_patients):
        # Sample disease
        disease = np.random.choice(list(disease_probs.keys()), p=list(disease_probs.values()))
        
        # Generate symptoms based on disease
        if disease == 'Flu':
            fever = np.random.random() < 0.8
            cough = np.random.random() < 0.7
            loss_of_smell = np.random.random() < 0.1
        elif disease == 'COVID':
            fever = np.random.random() < 0.9
            cough = np.random.random() < 0.8
            loss_of_smell = np.random.random() < 0.7
        else:  # None
            fever = np.random.random() < 0.1
            cough = np.random.random() < 0.2
            loss_of_smell = np.random.random() < 0.05
        
        data.append({
            'patient_id': patient_id + 1,
            'fever': 'Yes' if fever else 'No',
            'cough': 'Yes' if cough else 'No',
            'loss_of_smell': 'Yes' if loss_of_smell else 'No',
            'diagnosis': disease
        })
    
    df = pd.DataFrame(data)
    print(f"   Generated {len(df)} patient records")
    return df


# ============================================================================
# Dataset 5: Weather Sequences (Assignment 2)
# ============================================================================

def generate_weather_sequences(n_sequences: int = 200, seq_length: int = 10) -> pd.DataFrame:
    """
    Generate weather observation sequences.
    Hidden states: Sunny, Rainy, Cloudy
    Observations: Dry, Wet, Damp
    """
    print("\n5. Generating Weather Sequences...")
    
    states = ['Sunny', 'Rainy', 'Cloudy']
    observations = ['Dry', 'Wet', 'Damp']
    
    # Transition matrix
    trans_matrix = np.array([
        [0.7, 0.1, 0.2],  # From Sunny
        [0.2, 0.6, 0.2],  # From Rainy
        [0.3, 0.3, 0.4]   # From Cloudy
    ])
    
    # Emission matrix
    emit_matrix = np.array([
        [0.8, 0.05, 0.15],  # Sunny → observations
        [0.1, 0.8, 0.1],    # Rainy → observations
        [0.3, 0.3, 0.4]     # Cloudy → observations
    ])
    
    # Initial state probabilities
    start_prob = np.array([0.5, 0.2, 0.3])
    
    data = []
    
    for seq_id in range(n_sequences):
        obs_seq = []
        
        # Initial state
        state = np.random.choice(len(states), p=start_prob)
        obs = np.random.choice(len(observations), p=emit_matrix[state])
        obs_seq.append(observations[obs])
        
        # Generate rest of sequence
        for _ in range(seq_length - 1):
            state = np.random.choice(len(states), p=trans_matrix[state])
            obs = np.random.choice(len(observations), p=emit_matrix[state])
            obs_seq.append(observations[obs])
        
        # Create row
        row = {'sequence_id': seq_id + 1}
        for day in range(seq_length):
            row[f'day_{day + 1}'] = obs_seq[day]
        
        data.append(row)
    
    df = pd.DataFrame(data)
    print(f"   Generated {len(df)} sequences of length {seq_length}")
    return df


# ============================================================================
# Dataset 6: Robot Tracking Data (Assignment 3)
# ============================================================================

def generate_robot_tracking_data(n_steps: int = 300) -> pd.DataFrame:
    """
    Generate 2D robot tracking data with noisy GPS measurements.
    """
    print("\n6. Generating Robot Tracking Data...")
    
    # Initial state
    true_x, true_y = 0.0, 0.0
    true_vx, true_vy = 1.0, 0.5
    
    # Noise parameters
    process_noise_std = 0.05
    measurement_noise_std = 2.0
    
    data = []
    
    for t in range(n_steps):
        # Update position (constant velocity with noise)
        true_x += true_vx + np.random.normal(0, process_noise_std)
        true_y += true_vy + np.random.normal(0, process_noise_std)
        
        # Noisy measurements
        measured_x = true_x + np.random.normal(0, measurement_noise_std)
        measured_y = true_y + np.random.normal(0, measurement_noise_std)
        
        data.append({
            'time_step': t,
            'true_x': round(true_x, 2),
            'true_y': round(true_y, 2),
            'true_vx': round(true_vx, 2),
            'true_vy': round(true_vy, 2),
            'measured_x': round(measured_x, 2),
            'measured_y': round(measured_y, 2),
            'noise_level': measurement_noise_std,
            'trajectory_type': 'straight'
        })
    
    df = pd.DataFrame(data)
    print(f"   Generated {len(df)} time steps")
    return df


# ============================================================================
# Main Execution
# ============================================================================

if __name__ == "__main__":
    # Generate all datasets
    bn_data = generate_bayesian_network_data(500)
    hmm_data = generate_hmm_sequences(100, 7)
    kf_data = generate_kalman_tracking_data(200)
    medical_data = generate_medical_diagnosis_data(1000)
    weather_data = generate_weather_sequences(200, 10)
    robot_data = generate_robot_tracking_data(300)
    
    # Save to CSV files
    print("\n" + "="*80)
    print("Saving datasets to CSV files...")
    print("="*80)
    
    bn_data.to_csv('bayesian_network_exam_data.csv', index=False)
    print("✓ Saved: bayesian_network_exam_data.csv")
    
    hmm_data.to_csv('hmm_student_behavior_sequences.csv', index=False)
    print("✓ Saved: hmm_student_behavior_sequences.csv")
    
    kf_data.to_csv('kalman_filter_gps_tracking.csv', index=False)
    print("✓ Saved: kalman_filter_gps_tracking.csv")
    
    medical_data.to_csv('medical_diagnosis_data.csv', index=False)
    print("✓ Saved: medical_diagnosis_data.csv")
    
    weather_data.to_csv('weather_sequences.csv', index=False)
    print("✓ Saved: weather_sequences.csv")
    
    robot_data.to_csv('robot_tracking_data.csv', index=False)
    print("✓ Saved: robot_tracking_data.csv")
    
    print("\n" + "="*80)
    print("Dataset generation complete!")
    print("="*80)
    print(f"\nTotal datasets: 6")
    print(f"Total rows: {len(bn_data) + len(hmm_data) + len(kf_data) + len(medical_data) + len(weather_data) + len(robot_data)}")
    print("\nAll datasets are ready for use in Module 5 notebook and assignments.")

