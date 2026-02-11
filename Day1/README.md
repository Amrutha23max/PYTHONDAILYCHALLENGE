Overview:
This programs validates basic profile details entered by the user entered via terminal of the IDE.
It checks whether the data like NAME, EMAIL, PHONE NUMBER, AGE are matching with the required constraints.

If all the conditions are satisfied, the ouput is:
           User Profile is VALID
If the conditions were not satisfied, the output is:
          User Profile is INVALID

Inputs Taken:
The program asks the user to enter:
Full Name
Email
Mobile Number
Age



Validation Rules:
1. Full Name Validation
   Must contain at least two words
   Must not start or end with a space
2. Email ID Validation
   Must contain ‘@’ and ‘.’
  ‘@’ must not be the first character
3. Mobile Number Validation
  Must be exactly 10 characters
  Must contain only digits
  Must not start with 0
4. Age Validation
  Age must be between 18 and 60 (inclusive)

Logics used in the program:

String indexing and built-in functions like len(), isdigit(),count()
used nested if conditions for validating conditions one by one

How to Run:
ensure any python IDE is installed
save the file
run the program
enter the details and check for the validation


Sample input:

NAME : YASIR AFAQ
EMAIL:yasir@gmail.com
Mobile:9787665454
Age : 29

sample output:
User Profile is VALID

