# !python3
#
# Allergy score
#ToDO finish this

import time
import pprint

allergens = {
            'eggs': 1,
            'peanuts': 2,
            'shellfish': 3,
            'strawberries': 4,
            'tomatoes': 16,
            'chocolate': 32,
            'pollen': 64,
            'cats': 128
}

allergyList = []

def calculate():
    sum = 0
    for i in allergyList:
        if i in allergens:
            total = sum(allergens.values())
    print(total)


def main():
    print("Printing allergies in database")
    pprint.pprint(allergens)
    time.sleep(1)

    while True:
        allergy = input("Please input your allergies (type 'done' to stop): ")
        if allergy.lower() == "done":
            calculate()
            break
        allergyList.append(allergy)


if __name__ == "__main__":
    main()