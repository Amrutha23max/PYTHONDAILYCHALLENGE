Academic Data Drift & Copy Behavior Analyzer
 Overview

This project analyzes student academic data and demonstrates the difference between shallow copy and deep copy in Python. It also detects data drift using statistical methods.

⚙️ Features
Generates random student data
Stores data using list of dictionaries
Converts data into Pandas DataFrame
Applies shallow copy and deep copy
Performs data mutation on copied data
Uses NumPy for statistical analysis
Detects data drift and classifies results
 Data Format

Each student record contains:

id
marks
attendance
scores (list of internal values)
 Process Flow
Generate random dataset
Create shallow and deep copies
Apply mutation rule on copied data only
Modify marks using square root transformation
Change nested score values
Compute mean, median, and standard deviation
Calculate drift between original and modified data
Classify result based on drift
 Personalization Rule
Last digit of register number = 4
Modify only records where:
index % 3 == 1
 Output
Original DataFrame
Shallow copy result
Deep copy result
Drift value
Tuple output (mean, drift, std deviation)
Final classification (Stable / Minor Drift / Critical Drift / Copy Failure)
 Key Learning
Difference between shallow and deep copy
Effect of mutations on nested data
Basic statistical analysis using NumPy
Concept of data drift in real datasets
