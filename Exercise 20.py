# !python3

# Multi-state sales tax

order_amount = int(input("Please enter the bill amount\n"))
state = input("Please input your state\n")

if state.lower() == 'wi' or 'wisconsin':
    county = input("Input your county\n")
    if county.lower() == 'eau claire' or 'eu':
        total = (order_amount * 5.5 / 100) / 0.005 * 100
        print("Your total is {}".format(total))
    elif county.lower() == 'dunn' or 'd':
        total = (order_amount * 5.5 / 100) / 0.004 * 100
        print("Your total is {}".format(total))
    else:
        print("I didnt understand that")
elif state.lower() == 'illinois' or 'il':
    total = (order_amount * 8 / 100)
else:
    total = order_amount * 5.5 / 100
    print(total)