# !python3

# numerical calculator

bool = True
solution = 0

def add():
    solution = num_1 + num_2
    print("{} + {} = {}".format(num_1, num_2, solution))

def subtract():
    solution = num_1 - num_2
    print("{} - {} = {}".format(num_1, num_2, solution))

def multiply():
    solution = num_1 * num_2
    print("{} * {} = {}".format(num_1, num_2, solution))

def divide():
    solution = num_1 / num_2
    print("{} / {} = {}".format(num_1, num_2, solution))

while bool:
    num_1 = input("What is the first mumber: ")
    if not num_1.isnumeric():
        print("Please enter a numerical value")
        continue
    num_2 = input("What is the second mumber: ")
    if not num_2.isnumeric():
        print("Please enter a numerical value")
        continue
    else:
        add()
        subtract()
        multiply()
        divide()





