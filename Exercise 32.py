# !python3

# Exercise 32 - Guess the number game
import random

cpu_guess_easy = random.randint(1, 10)
cpu_guess_normal = random.randint(1, 100)
cpu_guess_hard = random.randint(1, 1000)
#guesses = 1

def easy():
    while True:
        global guesses
        user_choice = int(input("I have my number, whats your guess?: \n"))
        if (user_choice == cpu_guess_easy):
            print("Well done, you've guessed correctly in {} guesses " .format(guesses))
            answer = input("Would you like to play again? [Yes/No]")
            if answer.lower() in ['y', 'yes']:
                main()
            elif answer.lower() in ['y', 'yes']:
                break

        elif (user_choice < cpu_guess_easy):
            print("Sorry, your guess is too low, please guess again.")
            guesses += 1
            continue

        elif (user_choice > cpu_guess_easy):
            print("Sorry, your guess is too high, please guess again.")
            guesses += 1
            continue
        return

def normal():
    while True:
        global guesses
        user_choice = int(input("I have my number, whats your guess?: \n"))
        if (user_choice == cpu_guess_normal):
            print("Well done, you've guessed correctly in {} guesses" .format(guesses))
            answer = input("Would you like to play again? [Yes/No]")
            if answer.lower() in ['y', 'yes']:
                main()
            elif answer.lower() in ['y', 'yes']:
                break

        elif (user_choice < cpu_guess_normal):
            print("Sorry, your guess is too low, please guess again.")
            guesses += 1
            continue

        elif (user_choice > cpu_guess_normal):
            print("Sorry, your guess is too high, please guess again.")
            guesses += 1
            continue
        return

def hard():
    global guesses
    while True:
        user_choice = int(input("I have my number, whats your guess?: \n"))
        if (user_choice == cpu_guess_hard):
            print("Well done, you've guessed correctly in {} guesses" .format(guesses))
            answer = input("Would you like to play again? [Yes/No]")
            if answer.lower() in ['y', 'yes']:
                main()
            elif answer.lower() in ['y', 'yes']:
                break

        elif (user_choice < cpu_guess_hard):
            print("Sorry, your guess is too low, please guess again.")
            guesses += 1
            continue

        elif (user_choice > cpu_guess_hard):
            print("Sorry, your guess is too high, please guess again.")
            guesses += 1
            continue
        return

def main():
    global guesses
    guesses = 1
    print("Let's plat Guess the Number.")
    try:
        difficulty = int(input("Pick a difficulty level (1, 2, or 3): "))
    except ValueError:
        print("Please enter a numerical value between 1 and 3")
        main()
    if difficulty == 1:
        easy()
    elif difficulty == 2:
        normal()
    elif difficulty == 3:
        hard()
    else:
        print("I'm not too sure what you selected")

def winning_statement(i):
    if i == 1:
        print("You're a mind reader!")
    elif i >= 2 and i <= 4:
        print("Most Impressive")
    elif i > 4 and i <= 6:
        print("You can do better than that")
    elif i >= 7:
        print("Better luck next time")


if __name__ == "__main__":
    main()
