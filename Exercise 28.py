# !python3
# Adding numbers - Exercise 28

list_of_nums = []

while True:
    try:
        number_count = int(input("Enter how man numbers you would like to input: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
    for i in range(0, number_count):
        variable = int(input("Please enter a value: \n"))
        list_of_nums.append(variable)

    print("The total of all number entered is: " + str(sum(list_of_nums)))
