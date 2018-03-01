# !python3

# Exercise 35 - Picking a winner
import random
import time
contestants = []

def pick_winner():
    winner = random.choice(contestants)
    print("The winner is.......")
    time.sleep(2)
    print(winner)
    contestants.remove(winner)
    again = input("Pick another winner? [Y or N] : ")
    if again.lower() == 'y':
        pick_winner()
    elif again.lower() == 'n':
        main()

def main():
    while True:
        entry = input("Enter a name [blank to stop entry] : ")
        if entry == '':
            pick_winner()
            break
        contestants.append(entry)

if __name__ == "__main__":
    main()

