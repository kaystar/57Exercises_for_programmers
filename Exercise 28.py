# !python3
# Adding numbers - Exercise 28

list_of_nums = []
number_count = 5

for i in range(0, number_count):
    variable = int(input("Please enter a value: \n"))
    list_of_nums.append(variable)

print("The total of all number entered is: " + str(sum(list_of_nums)))
