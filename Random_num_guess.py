import random

secret_number = random.randint(1, 10)
attempts = 0

try:
  guess = int(input("Guess a number between 1 and 10: \n"))
  if 1<= guess <= 10:
    attempts +=1
    if guess == secret_number:
      print("You got it! 🎉")
    else:
        print(f"Oops! The correct number was {secret_number}. Try again!")
        print(f"You have used {attempts} attempts")
  else:
      print("Please enter a number from 1 to 10")
except ValueError:
    print("Invalid input!!")
