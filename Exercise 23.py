# !python3
#
# Car diagnostic program

import time

print("*******Welcome to the car diagnostic tool********")
time.sleep(2)
question_1 = input(r"Is the car silent when you turn the key? 'Y' or 'N: ")
if question_1.lower() == 'y':
    question_2_positive = input(r"Are the battery terminals corroded? 'Y' or 'N: ")
    if question_2_positive == 'y':
        print("Clean terminals and try again...")
    else:
        print("Replace cables and try again.")
elif question_1.lower() == 'n':
    question_2_negative = input(r"Does the car make a clicking noise? 'Y' or 'N': ")
    if question_2_negative.lower() == 'y':
        print("Replace the battery")
        time.sleep(1)
    elif question_2_negative.lower() == 'n':
        question_3 = input(r"Does the car crank up but fail to start? 'Y'or 'N': ")
        if question_3.lower() == 'y':
            print("Check the spark plug connections")
            time.sleep(1)
        elif question_3.lower() == 'n':
            question_4 = input(r"Does the engine start-up and then die? 'Y' or 'N': ")
            if question_4.lower() == 'y':
                question_5 = input(r"Does your car have fuel injection? 'Y' or 'N': ")
                if question_5.lower() == 'y':
                    print("Get it in for service.")
                elif question_5.lower() == 'n':
                    print("Check to ensure the choke is opening and closing.")
                else:
                    print("Did not understand input, returning to start.")
else:
    print("Did not understand input, returning to start.")




