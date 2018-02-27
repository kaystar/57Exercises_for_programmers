# Paint Calculator
import math

gallon = 9
paint_buckets = 1

def calculation(leng,widt):
    global area
    area = leng * widt
    paint_buckets = math.ceil(area / gallon)
    result = "\nYou will need to purchase " + str(paint_buckets) + " liter(s) of paint to cover " + str(area) + " square meter(s)."
    print(result)

while True:
    try:
        length = int(input("What is the length of the room in feet?: "))
        width = int(input("What is the width of the room in feet?: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
    else:
        calculation(length, width)
