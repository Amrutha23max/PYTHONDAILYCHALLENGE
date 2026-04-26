User Profile Validation System
 Overview

This project is a Python-based User Profile Validation System developed as part of the SRM University–AP Code2Xplore Challenge (CSE205).
It validates user details such as name, age, email, and password using defined rules and ensures that only valid inputs are accepted.

A personalization rule is also included based on the last digit of the register number, which changes the validation strictness.

Features

Validates user name, age, email, and password
Checks proper format for email and password strength
Applies strict validation based on register number
Provides final output as valid or invalid profile

Logic Used
Functions are used for each validation step
Conditional statements control validation rules
String operations are used for format checking

Personalization rule:
Even last digit → Strict validation mode
Odd last digit → Normal validation mode

Input Required
Name
Age
Email
Password
Register Number

Output
Validation mode (Strict / Normal)
Field-wise validation results
Final decision: Valid or Invalid User Profile

 How to Run
python filename.py

 Learning Outcome
Learned input validation in Python
Understood use of functions and conditions
Improved logic building skills
Learned how personalization affects program behavior

