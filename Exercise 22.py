#!python3

#Comparing Numbers

#Author: Kevin Rose

def calculate(a,b,c):
    if a > b:
        if a > c:
            largest_number = a
        else:
            largest_number = c
    elif b > c:
        if b > a:
            largest_number = b
        else:
            largest_number = a
    elif c > a:
        if c > b:
            largest_number = c
        else:
            largest_number = b
    result = "\nThe largest number is " + str(largest_number) + "."
    print(result)


first_input = int(input("Enter the first number: "))
second_input = int(input("Enter the second number: "))
third_input = int(input("Enter the third number: "))

if first_input == second_input or second_input == third_input:
    print("Enter unique values\n")

calculate(first_input,second_input,third_input)
