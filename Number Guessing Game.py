import random

low = 1
high = 100
guesses = 0
number = random.randint(low , high)

while True:
    guess = input(f"Enter a number between {low} and {high} : ")

    if guess.isdigit():
        guess = int(guess)
        guesses+=1

        if guess > high or guess < low:
            print("Number is out of range")
            print("Please enter a number between 1 to 100 : ")
            
        elif guess < number:
            print(guess , "is too low")

            
        elif guess > number:
            print(guess , "is too high")

        else:
            print(guess , "is right")
            print("it took you" , guesses , "guesses")
            break
    else:
        print("INVALID INPUT")
        print("Please enter a number between 1 to 100 : ")


