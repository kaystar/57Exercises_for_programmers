# !python3

# Password Strength Indicator
#ToDo This doesn't work so complete it

recommendlength = 8

def password_strength(pwd):
    if pwd.isnumeric() and len(pwd) < recommendlength:
        print("Your password {}, is a very weak password." .format(pwd))
    elif pwd.isalnum() and len(pwd) < recommendlength:
        print("Your password {}, is a weak password." .format(pwd))
    elif any(char.isdigit() for char in pwd) and len(pwd) >= recommendlength:
        print("Your password {}, is a strong password." .format(pwd))
    elif pwd == ('/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$%^&]).*$/') and len(pwd) >= recommendlength:
        print("Your password {}, is a very strong password." .format(pwd))
    else:
        print("I'm not too sure.")

while True:
    password = input("Please input a password: \n")
    password_strength(password)
