print("RANDOM NUMBER GENERATOR \n")

import random

low = 1
high = 100
guesses = 0
number = random.randint(low , high)

while True:
    guess = int(input("Guess a number between 1 to 100 : "))

    guesses = guesses + 1

    if guess < number:
        print(guess , "is too low")

    elif guess > number:
        print(guess , "is too high")
        
    else:
        print(guess , "is correct")
        break
 
print("You took " ,guesses, "guesses")
