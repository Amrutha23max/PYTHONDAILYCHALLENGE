Student_ID =  input("ID:")
Email_ID = input("EMAIL:")
Password = input("Password:")
Referral_Code = input("Referral:")
REGISTRATION_NUMBER =input("Enter registration number:")
reg_len = len(REGISTRATION_NUMBER)

if REGISTRATION_NUMBER[reg_len-1] >='0' and REGISTRATION_NUMBER[reg_len-1]<='5':
    if len(Password) >= 8 and Password[0] >= 'A' and Password[0] <= 'Z' and (
            Password.count('0') + Password.count('1') + Password.count('2') + Password.count('3') + Password.count(
        '4') + Password.count('5') + Password.count('6') + Password.count('7') + Password.count('8') + Password.count(
        '9')) >= 1:

        if len(Student_ID)==7 and Student_ID[0:3]=="CSE" and Student_ID[3]=='-'and Student_ID[4].isdigit() and Student_ID[5].isdigit() and Student_ID[6].isdigit():
            if len(Email_ID)>=4 and Email_ID.count("@")>0 and Email_ID.count(".")>0 and Email_ID[0]!='@' and Email_ID[len(Email_ID)-1]!='@'and Email_ID[len(Email_ID)-4 : len(Email_ID)]==".edu":

              if len(Referral_Code) == 6 and Referral_Code[0:3] =="REF" and Referral_Code[3].isdigit()and Referral_Code[4].isdigit() and Referral_Code[len(Referral_Code)-1]=='@':
                print("APPROVED")
              else:
                print("REJECTED")

            else:
              print("REJECTED")

        else:
           print("REJECTED")
    else:
         print("REJECTED")

else:
    if len(Student_ID) == 7 and Student_ID[0:3] == "CSE" and Student_ID[3] == '-' and Student_ID[4].isdigit() and \
            Student_ID[5].isdigit() and Student_ID[6].isdigit():
        if len(Email_ID) >= 4 and Email_ID.count("@") > 0 and Email_ID.count(".") > 0 and Email_ID[0] != '@' and \
                Email_ID[len(Email_ID) - 1] != '@' and Email_ID[len(Email_ID) - 4: len(Email_ID)] == ".edu":
            if len(Password) >= 8 and Password[0] >= 'A' and Password[0] <= 'Z' and (
                    Password.count('0') + Password.count('1') + Password.count('2') + Password.count(
                '3') + Password.count('4') + Password.count('5') + Password.count('6') + Password.count(
                '7') + Password.count('8') + Password.count('9')) >= 1:
                if len(Referral_Code) == 6 and Referral_Code[0:3] == "REF" and Referral_Code[3].isdigit() and \
                        Referral_Code[4].isdigit() and Referral_Code[len(Referral_Code) - 1] == '@':
                    print("APPROVED")
                else:
                    print("REJECTED")

            else:
                print("REJECTED")

        else:
            print("REJECTED")
    else:
        print("REJECTED")
