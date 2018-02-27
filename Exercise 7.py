def calcuation(l, w):
    squaredfeet = l * w
    metres = squaredfeet * 0.09290304
    squaredmetres = round(metres, 2)
    print("The area is {} square feet and {} square metres" .format(squaredfeet, squaredmetres))


while True:
    try:
        length = int(input("What is the length of the room in feet?: "))
        width = int(input("What is the width of the room in feet?: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
    else:
        print("You entered dimension of {} feet by {} feet".format(length, width))
        calcuation(length, width)
