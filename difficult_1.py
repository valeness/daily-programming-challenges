"""
This is a reverse guessing game
The computer will guess numbers between 1 - 100,
The use will then respond with "higher" or "lower" until the computer gets it right
"""
from random import randrange

running = True

directions = """
Think of a number from 1 - 100. I will try to guess it!
Tell me if it is too high or too low by typing 
an 'H/h' for high, and a 'L/l' for low
"""

print(directions)

base = 0
limit = 100

def get_guess():
	guess = randrange(base, limit)
	print("Guess: {0}".format(guess))
	return guess

def too_low():
	base = guess
	return base

def too_high():
	limit = guess
	return limit

# Get the Initial Guess
guess = get_guess()

while running:
	command = raw_input('>>').lower()

	if 'h' in command:
		limit = too_high()
		guess = get_guess()
	elif 'l' in command:
		base = too_low()
		guess = get_guess()
	elif 'y' in command:
		print("Yay! I guessed right!")