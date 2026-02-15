roll_number = input("ENTER THE ROLL NUMBER:")
last_two_digits = ""
count =0
index = len(roll_number)-1
while count < 2 and index >= 0:
    value = roll_number[index]
    last_two_digits = value+last_two_digits
    count += 1          
    index -= 1 
last_two_digits = int(last_two_digits)
no_of_students = int(input("ENTER NUMBER OF STUDENTS"))
valid_count =0
fail_count =0
student_marks = []
new_student_marks =[]
for i in range (no_of_students):
   marks = int(input("ENTER THE MARKS:"))
   student_marks = student_marks+[marks]
   new_student_marks = new_student_marks+[marks]
    

print("STUDENT PERFORMANCE:")
for i in range(no_of_students):
   
    if student_marks[i]>0 and student_marks[i]<100 :
       if student_marks[i]%last_two_digits ==0 :
            
            new_marks = student_marks[i]+5
            if new_marks>100:
                new_marks =100
            new_student_marks[i] = new_marks 
            print(" 5 marks were added to", student_marks[i],"new marks",new_marks)
       else:
             print(student_marks[i],"got no hike")


            
for i in range(no_of_students): 
    if student_marks[i]<0 or student_marks[i]>100 :
        print(student_marks[i] ,"->Invalid")
    else: 
        valid_count += 1
        if new_student_marks[i] >=90:
          print(new_student_marks[i],"->EXCELLENT")
        elif new_student_marks[i] >=75:
          print(new_student_marks[i],"->VERY GOOD")
        elif new_student_marks[i] >=60:
          print(new_student_marks[i],"->GOOD")
        elif new_student_marks[i] >=40:
          print(new_student_marks[i],"->AVERAGE")
        else :
          print(new_student_marks[i],"->FAIL")
          fail_count +=1
print("FINAL SUMMARY :")
print("Total Valid Students: ",valid_count)
print("Total Failed Students: ",fail_count)
