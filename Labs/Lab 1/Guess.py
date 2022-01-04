# Guess The Number game
# program generates random number which player tries to guess

# imports library
import random

# generates a random number between 1-10
random_number = random.choice(range(1,11))

# print instructions and prompt for guess
print("I am thinking of a number between 1 and 10.")
player_guess = input("What is the number? ")

# print generated and guessed number
print("The number was " + str(random_number) + ".")
print("You guessed " + player_guess + ".")