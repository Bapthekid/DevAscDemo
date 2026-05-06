import random
import time

print(" Welcome to DevAscDemo python script!") 
print("Welcome to the Magic Number Guessing Game!")
time.sleep(1)
print("I'm thinking of a number between 1 and 100...")
time.sleep(1)

number = random.randint(1, 100)
attempts = 0

while True:
    try:
        guess = int(input("Take a guess: "))
        attempts += 1
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts.")
            break
    except ValueError:
        print("Please enter a valid number.")