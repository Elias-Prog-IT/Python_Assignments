# a guessing game where the user gets 3 guesses to get the right number between an approximate range of two integer numbers.
import random

number = random.randint(1, 10)

for i in range(3):
    guess  = int(input("Guess: "))
    if guess > number:
        print("Guess is too large!")
    elif guess < number:
        print("Guess is too small!")
    else:
        print("Correct!")
        break

