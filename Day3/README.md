This program analyzes student performance based on their marks and a special rule derived from the user's roll number.

The last two digits of the roll number are extracted and used to determine whether a student is eligible for a 5-mark bonus.

After applying the bonus (if eligible), the program classifies student performance into different categories and displays a final summary.

How It Works
The special Rule:
   Roll number is taken as the input at the beginning, Ihave given my roll number (AP24110011514).
   After extracting the last two digits of the Roll number, the marks entered by the user which are valid(i.e >0 and <100), if    is multiple of the last two digits, will be given a grace marks of 5.
        If the score crosses 100 after the grace mark addition, then the score will be made 100 ensuring the integrity of the          data

Input Student Marks
The user enters the total number of students.
Marks are collected for each student.
Marks must be between 0 and 100 (inclusive).

Performance Classification

After applying the bonus (if applicable), students are categorized as:

Marks Range	Grade
90 – 100	EXCELLENT
75 – 89	VERY GOOD
60 – 74	GOOD
40 – 59	AVERAGE
Below 40	FAIL

Invalid marks (<0 or >100) are flagged as Invalid.

Output Includes:
Bonus mark notifications (if applicable)
Individual performance classification
Total valid students
Total failed students
Final summary report

How to run:
python challengeday3.py
