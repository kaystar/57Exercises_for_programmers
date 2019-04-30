import time

points = {
    "1st" : 15,
    "2nd" : 12,
    "3rd" : 10,
    "4th" : 8,
    "5th" : 7,
    "6th" : 6,
    "7th" : 5,
    "8th" : 4,
    "9th" : 3,
    "10th": 2,
    "11th": 1,
    "12th": 0
}

player_1_scores = []
player_2_scores = []

def main():
    print("Mario Kart Calculator ")
    time.sleep(1)
    player_1 = input("Enter a name for player 1:\n")
    player_2 = input("Enter a name for player 2:\n")

    for i in range(1,8):
        entry = int(input("Enter position for {} [0 to stop entry] : ".format(player_1)))


    while True:
        entry = int(input("Enter a number [0 to stop entry] : "))
        if entry == 0:
            calculate()
            break
        numbers.append(entry)

if __name__ == "__main__":
    main()


