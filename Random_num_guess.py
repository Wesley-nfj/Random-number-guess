import random

secret_number = random.randint(1, 10)

guess = int(input("7Guess a number between 1 and 10: \n"))

if guess == secret_number:
    print("You got it! 🎉")
else:
    print(f"Oops! The correct number was {secret_number}. Try again!")
