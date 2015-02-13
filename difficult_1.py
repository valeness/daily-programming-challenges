"""
This is a reverse guessing game
The computer will guess numbers between 1 - 100,
The use will then respond with "higher" or "lower" until the computer gets it right
"""
from random import randrange

limit = 100
base = 0

guess = randrange(base, limit)
print(guess)