name =      input("FULL NAME:")
email =     input("EMAIL:")
mobile_no = input("MOBILE NUMBER:")
age =       int(input("AGE:"))

if name[0]!=" " and name[len(name)-1]!=" " and name.count(" ")>=1:
    if email[0]!='@' and email.count('@')>=1 and email.count('.')>=1:
        if len(mobile_no) ==10 and mobile_no.isdigit() and mobile_no[0]!='0':
            if age >=18 and age<=60:
                print("User Profile is VALID")
            else:
                print("User Profile is INVALID")
        else:
            print("User Profile is INVALID")
    else:
        print("User Profile is INVALID")
else:
    print("User Profile is INVALID")