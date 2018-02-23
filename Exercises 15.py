# !python3

#Password Safe

password_vault = {"kevin" : "peanuts",
                         "amyke" : "camera",
                         "deyna" : "lamp",
                         "dad" : "telefone"
                         }
while True:
    username = input("What is your username...: ")
    password = input("Password...:")

    if username in password_vault and password == password_vault.get(username):
        print("Welcome {}, enjoy your stay!".format(username))
        break
    else:
        print("Sorry your credentials were not recognised, please try again.")

