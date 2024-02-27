# Pseudo random

import random                 # import the random lib

x = random.randint(1, 6)      # assign x and random.random integer from (1 to 6)
y = random.random()           # assign y and random.random float
print(x)
print(y)


# rock paper scissor

mylist = ['rock', 'paper', 'scissor']
z = random.choice(mylist)                        # this select some random choice
print(z)


# shuffle
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K']
random.shuffle(cards)                                  # shuffle method
print(cards)
