# !python3

# Exercise 33 - Magic 8 Ball

import random

messages = ['yes',
            'no',
            'Maybe',
            'Ask again later']

question = input("What is your question?: ")
answer = random.choice(messages)
print(answer)
