import random
import numpy as np
import pandas as pd
import math

def generate_students(n=10):
    students = []

    for i in range(1, n + 1):
        student_id = f"S{i:03d}"
        marks = random.randint(0, 100)
        attendance = random.randint(0, 100)
        assignment = random.randint(0, 50)

        # tuple format (required)
        students.append((student_id, marks, attendance, assignment))

    return students

def classify_students(df):
    categories = {
        "At Risk": [],
        "Average": [],
        "Good": [],
        "Top Performer": []
    }

    for _, row in df.iterrows():
        marks = row["marks"]
        attendance = row["attendance_percentage"]
        sid = row["student_id"]

        if marks > 90 and attendance > 80:
            categories["Top Performer"].append(sid)
        elif marks < 40 or attendance < 50:
            categories["At Risk"].append(sid)
        elif 40 <= marks <= 70:
            categories["Average"].append(sid)
        else:
            categories["Good"].append(sid)

    return categories

def statistical_analysis(df):
    marks = df["marks"].to_numpy()
    attendance = df["attendance_percentage"].to_numpy()

    stats = {
        "mean_marks": np.mean(marks),
        "median_marks": np.median(marks),
        "std_marks": np.std(marks),
        "correlation_marks_attendance": np.corrcoef(marks, attendance)[0][1]
    }

    return stats

def normalize(series):
    return (series - series.min()) / (series.max() - series.min())

def pattern_detection(df, categories):
    patterns = {}
    
    
    if df["marks"].std() < 15:
        patterns["consistent_students"] = "Dataset is consistent"
    else:
        patterns["consistent_students"] = "Dataset is NOT consistent"
    
    low_attendance = df[df["attendance_percentage"] < 50]
    patterns["attendance_risk_count"] = len(low_attendance)
    
    patterns["high_achievers"] = categories["Top Performer"]
    patterns["high_achievement_check"] = len(categories["Top Performer"]) >= 2
    
    return patterns

student_data = generate_students(10)


df = pd.DataFrame(student_data, columns=[
    "student_id", "marks", "attendance_percentage", "assignment_score"
])


df["normalized_marks"] = normalize(df["marks"])


categories = classify_students(df)


stats = statistical_analysis(df)


patterns = pattern_detection(df, categories)



print("\n     STUDENT DATAFRAME    \n")
print(df)

print("\n     CATEGORIZED STUDENTS    \n")
print(categories)

print("\n    STATISTICAL SUMMARY   \n")
for k, v in stats.items():
    print(f"{k}: {v}")

print("\n    PATTERN DETECTION       \n")
for k, v in patterns.items():
    print(f"{k}: {v}")
