# Student Performance Analysis

## Overview

This project analyzes student performance based on:

* Marks
* Attendance
* Assignment scores

It generates student data, stores it in structured formats, and performs basic statistical analysis.

---

## Features

* Random student data generation
* Data stored using list, tuple, and dictionary
* Conversion to Pandas DataFrame
* Student classification (At Risk, Average, Good, Top Performer)
* Basic statistics using NumPy
* Marks normalization
* Simple pattern detection

---

## Data Format

Each student record:
(student_id, marks, attendance, assignment_score)

Example:

```id="eg1"
("S001", 75, 80, 30)
```

---

##  Steps

### 1. Data Generation

* Generates 10 students using random values
* Marks: 0–100
* Attendance: 0–100
* Assignment: 0–50

### 2. Data Storage

* Stored in list of tuples
* Converted into a DataFrame

### 3. Classification

* At Risk → marks < 40 OR attendance < 50
* Average → 40–70
* Good → 71–90
* Top Performer → marks > 90 AND attendance > 80

---

### 4. Analysis

* Mean, Median, Standard Deviation of marks
* Correlation between marks and attendance

---

### 5. Normalization

Marks are scaled using:

```id="eg2"
(x - min) / (max - min)
```

---

### 6. Pattern Detection

* Check if dataset is consistent
* Count students with low attendance
* Identify top performers

---

##  How to Run

1. Install dependencies:

```id="eg3"
pip install pandas numpy
```

2. Run the program:

```id="eg4"
python main.py
```

---

## Output

* Student DataFrame
* Categorized students
* Statistical summary
* Pattern insights

---
## Tech Used

* Python
* Pandas
* NumPy

---

##  What You Learn

* Data handling in Python
* Basic data analysis
* Use of Pandas & NumPy
* Writing functions and logic

---



Your Name
