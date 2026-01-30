Overview

The program validates student registration details based on the constraints given :
The details are :
   1. STUDENT ID
   2. EMAIL ID
   3. PASSWORD
   4. REFERRAL CODE
if all conditions are staisfied the it prints : "APPROVED"
else it prints :"REJECTED"

Validation Rules:

Student ID Rules:
        Format : CSE-XXX
        ID must start with “CSE”
        There should be ‘-’ after CSE
        Last 3 characters must be digits
Email ID Rules:
     Email ID must contain ‘@’ and ‘.’ 
     It should neither start nor end with ‘@’
    It must end with “.edu”
Password Rules:
     Length of the Password must be greater than or equal to 8
     First character must be upper case
     Password must contain at least one digit
Referral Code Rules:
      Must start with “REF”
      Next two characters must be digits 
      Last character must be ‘@’


Logics used :
string slicing, indexing
count function
length checks
nested conditional statements

HOW TO RUN :
ensure any pyhton IDE is installed 
save the file
Run the program

Sample input:
ID: CSE-245
Email: student@univ.edu
Password: Aman1234
Referral: REF45@

sample output:
APPROVED
