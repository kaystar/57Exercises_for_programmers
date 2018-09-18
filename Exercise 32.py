# !python3

# Exercise 32 - Guess the number game
#ToDo Finish winning statement function
import random
import time

def guessingGame():
    global guesses
    while True:
        user_choice = int(input("I have my number, whats your guess?: \n"))
        if user_choice in past_guesses:
            print("Oops, you've already guessed {} please choose a different number" . format(user_choice))
            continue

        if (user_choice == cpu_guess):
            print("Well done, you've guessed correctly in {} guesses" .format(guesses))
            time.sleep(2)
            print("Your past guesses were {}" .format(past_guesses))
            time.sleep(2)
            answer = input("Would you like to play again? [Yes/No]")
            if answer.lower() in ['y', 'yes']:
                main()
            elif answer.lower() in ['y', 'yes']:
                break

        elif (user_choice < cpu_guess):
            print("Sorry, your guess {} is too low, please guess again.".format(user_choice))
            guesses += 1
            past_guesses.append(user_choice)
            continue

        elif (user_choice > cpu_guess):
            print("Sorry, your guess {} is too high, please guess again.".format(user_choice))
            guesses += 1
            past_guesses.append(user_choice)
            continue
        return

def winning_statement(i):
    if i == 1:
        print("You're a mind reader!")
    elif i >= 2 and i <= 4:
        print("Most Impressive")
    elif i > 4 and i <= 6:
        print("You can do better than that")
    elif i >= 7:
        print("Better luck next time")


def main():
    global guesses
    global max_no
    global cpu_guess
    global past_guesses
    past_guesses = []

    #max_no = 1
    guesses = 1
    print("Let's plat Guess the Number.")
    try:
        difficulty = int(input("Pick a difficulty level (1, 2, or 3): "))
    except ValueError:
        print("Please enter a numerical value between 1 and 3")
        main()

    if difficulty == 1:
        max_no = 10
        cpu_guess = random.randint(1, max_no)
        guessingGame()
    elif difficulty == 2:
        max_no = 100
        cpu_guess = random.randint(1, max_no)
        guessingGame()
    elif difficulty == 3:
        max_no = 1000
        cpu_guess = random.randint(1, max_no)
        guessingGame()
    else:
        print("I'm not too sure what you selected")

if __name__ == "__main__":
    main()
