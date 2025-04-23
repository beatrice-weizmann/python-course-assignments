import random

# Generate a random number between 1 and 20
secret_number = random.randint(1, 20)

# Get user input
guess = int(input("Guess a number between 1 and 20: "))

# Check the guess
if guess < secret_number:
  print("Too low!")
elif guess > secret_number:
  print("Too high!")
else:
  print("Correct!")
