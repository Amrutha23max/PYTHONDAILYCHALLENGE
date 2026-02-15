Activity Risk Classification & Personalization

A Python program that classifies activity scores into risk categories 
and applies a personalization filter based on the last digit of a registration number.

Features
Accepts multiple activity scores from the user
validates each score, and igm=nores the invalid entires

Categorizes scores into:

Low Risk (0–30)
Medium Risk (31–60)
High Risk (61–100)
Critical Risk (>100)

Removes scores divisible by the registration digit

Displays summary statistics

Personalization Logic:
After classification, scores divisible by the entered registration digit (D ≠ 0) 
are removed from their respective risk categories.

How to run:
python filename.py

Output Includes:

Risk categories before personalization
Risk categories after personalization
Total valid entries
Invalid (ignored) entries
Removed entries due to personalization
