# !python3
# Handling bad input - Exercise 29

def calculate(i):
    years = 72 / i
    print("It will take you {} years to double your initial investment" .format(years))

while True:
    try:
        rate_of_return = int(input("What is the rate of return?: \n"))
        if rate_of_return <= 0:
            print("Sorry your initial investment wasn't a positive number")
            continue
        calculate(rate_of_return)
    except ValueError:
        print("Sorry, that is not a valid number, try again...")
