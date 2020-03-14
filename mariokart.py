import time

points = {
    1 : 15,
    2 : 12,
    2 : 10,
    4 : 8,
    5 : 7,
    6 : 6,
    7 : 5,
    8 : 4,
    9 : 3,
    10: 2,
    11: 1,
    12: 0
}

player_1_scores = []
player_2_scores = []

def main():
    print("Mario Kart Calculator ")
    time.sleep(1)
    player_1 = input("Enter a name for player 1:\n")
    player_2 = input("Enter a name for player 2:\n")

    for i in range(1,9):
        entry = int(input("Enter positions for {} [0 to stop entry] : ".format(player_1)))
        player_1_scores.append(entry)
    
    for i in range(1,9):
        entry_2 = int(input("Enter positions for {} [0 to stop entry] : ".format(player_2)))
        player_2_scores.append(entry_2)
    
    calculate(player_1_scores, player_2_scores, player_1, player_2)

def calculate(first_player_scores, second_player_scores, p1, p2):
    player_1_total = 0
    player_2_total = 0
    
    for i in first_player_scores:
        if i in points:
            player_1_total += points[i]

    for i in second_player_scores:
        if i in points:
            player_2_total += points[i]
    print(player_2_total)
    
    print("The total scores are:\n {}: {}\n{}: {}".format(p1, player_1_total, p2, player_2_total))

# def winner(player_1, player)

if __name__ == "__main__":
    main()


