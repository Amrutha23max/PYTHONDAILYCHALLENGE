Emergency Resource Dispatch Analyzer

Overview:

This Python program analyzes emergency resource requests during a disaster drill. It classifies each request into categories and 
applies a personalized filtering rule based on the length of the user’s name.
The program also displays the difference before and after applying the personalized logic.

Features:

Accepts user input for:
Full name
Number of requests
Resource request values

Classifies requests into:

Invalid (< 0)
No Demand (0)
Low Demand (1–20)
Moderate Demand (21–50)
High Demand (> 50)

Applies personalized filtering:

PLI = L % 3
Where L is the length of the name (excluding spaces)

Displays:

Lists before filtering
Lists after filtering
Total valid requests
Number of removed requests

Personalization Rule:

PLI = 0 → Remove Low Demand requests
PLI = 1 → Remove High Demand requests
PLI = 2 → Keep only Moderate Demand requests

How to Run:
Run the program:   python day4.py

Learning Outcome
This project helped me practice loops, conditional statements, list handling, and applying personalized logic in Python.



