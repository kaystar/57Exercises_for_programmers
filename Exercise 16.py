# !python3

# Legal age calculator

legal_age = 16

def yes():
    print("Yes. You're of legal age to drive")

def no():
    print("Sorry you're not of legal age to drive")

while True:
    try:
        age = int(input("What is your age?: "))
        if age >= 16:
            yes()
        elif age < 0:
            print("Please input a positive number")
            continue
        else:
            no()
    except ValueError:
        print("Please input an integer")
        continue



#yes if age >

