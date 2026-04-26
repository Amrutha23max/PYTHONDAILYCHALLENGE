 import random
import math
import pandas as pd
import numpy as np
import copy

def generate_students(n=12):
    students = []
    for i in range(n):
        students.append({
            "id": i + 1,
            "marks": random.randint(40, 100),
            "attendance": random.randint(60, 100),
            "scores": [
                random.randint(10, 50),
                random.randint(10, 50)
            ]
        })
    return students


def to_dataframe(data):
    return pd.DataFrame(data)



def mutate_data(data, roll_digit):
    rule = roll_digit % 3  # personalization rule

    for i, student in enumerate(data):
        if i % 3 == rule:
            student["marks"] += math.sqrt(student["marks"])
            student["attendance"] += 2
            student["scores"][0] += 5

    return data


def analyze(original_df, modified_df):
    orig_mean = np.mean(original_df["marks"])
    mod_mean = np.mean(modified_df["marks"])

    drift = abs(orig_mean - mod_mean)

    median = np.median(modified_df["marks"])
    std_dev = np.std(modified_df["marks"])

    manual_mean = sum(modified_df["marks"]) / len(modified_df["marks"])

    return orig_mean, mod_mean, drift, median, std_dev, manual_mean



def classify_drift(drift, threshold):
    if drift == 0:
        return "Copy Failure Detected"
    elif drift > threshold:
        return "Critical Drift"
    elif drift > 2:
        return "Minor Drift"
    else:
        return "Stable Data"


roll_digit = 4  # last digit of register number

# Generate data
original_data = generate_students(12)

# Create copies
shallow_copy = copy.copy(original_data)
deep_copy = copy.deepcopy(original_data)

 #Mutate only copies
shallow_copy = mutate_data(shallow_copy, roll_digit)
deep_copy = mutate_data(deep_copy, roll_digit)

# Convert to DataFrames
df_original = to_dataframe(original_data)
df_shallow = to_dataframe(shallow_copy)
df_deep = to_dataframe(deep_copy)

# Analysis
orig_mean, mod_mean, drift, median, std_dev, manual_mean = analyze(df_original, df_shallow)

# Threshold (custom)
threshold = 5

# Classification
status = classify_drift(drift, threshold)

print("\n--- ORIGINAL DATA ---")
print(df_original)

print("\n--- SHALLOW COPY DATA ---")
print(df_shallow)

print("\n--- DEEP COPY DATA ---")
print(df_deep)

print("\nDrift Value:", drift)
print("Tuple Output:", (manual_mean, drift, std_dev))
print("Final Classification:", status)
