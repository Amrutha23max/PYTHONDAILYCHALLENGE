def validate_name(name):
    return name.isalpha()


def validate_age(age):
    return age >= 18


def validate_email(email):
    # strict check: must contain @, ., and no spaces
    return "@" in email and "." in email and " " not in email


def validate_password(password, strict_mode):
    if strict_mode:
        # STRICT MODE (roll last digit = 4)
        return len(password) >= 10 and any(ch.isdigit() for ch in password)
    else:
        # normal mode
        return len(password) >= 6


def main():
    print("\n--- USER PROFILE VALIDATION SYSTEM ---")

    name = input("Enter name: ")
    age = int(input("Enter age: "))
    email = input("Enter email: ")
    password = input("Enter password: ")
    reg_no = input("Enter register number: ")

    # personalization rule
    last_digit = int(reg_no[-1])
    strict_mode = (last_digit % 2 == 0)  # even → strict mode

    print("\n--- VALIDATION MODE ---")
    if strict_mode:
        print("STRICT MODE ENABLED (Even Roll Number Rule Applied)")
    else:
        print("NORMAL MODE ENABLED")

    # validations
    name_check = validate_name(name)
    age_check = validate_age(age)
    email_check = validate_email(email)
    password_check = validate_password(password, strict_mode)

    print("\n--- VALIDATION RESULTS ---")
    print("Name Valid:", name_check)
    print("Age Valid:", age_check)
    print("Email Valid:", email_check)
    print("Password Valid:", password_check)

    # final decision
    if name_check and age_check and email_check and password_check:
        print("\n RESULT: Valid User Profile")
    else:
        print("\n  RESULT: Invalid User Profile")


# run program
main()

