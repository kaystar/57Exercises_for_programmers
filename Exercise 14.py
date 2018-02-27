tax = 5.5

while True:
    amount = int(input("What is the order amount?: "))
    state = input("What is the State?: ")

    if state.lower() == "wi" or state.lower() == "wisconsin":
        tax = amount * tax / 100
        total = round(amount + tax,2)
        print("The subtotal is: {}\n The tax is: {} \n The total is {}" .format(amount, tax, total))

print("The total is: {}" .format(amount))
