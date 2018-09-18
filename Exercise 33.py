# !python3

# Exercise 33 - Magic 8 Ball

import random
import time

messages = ['yes',
            'no',
            'Maybe',
            'Ask again later']

question = input("What is your question?: ")
for i in range(0, 3):
    print('.')
    time.sleep(1)
    i += 1
answer = random.choice(messages)
print(answer)
