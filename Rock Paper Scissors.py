print("ROCK PAPER SCISSORS \n")

import random

# FOR ONLY ONE PLAY

"""options = ("rock" , "paper" , "scissors")
player = None
computer = random.choice(options)
playing = True
    
while player not in options:
    player = input("Enter a choice (""Rock"" , ""Paper"" , ""Scissors"") : ")

print("Player : " , player)
print("Computer : " , computer)

if player == computer:
    print("Its a tie")
                
elif player == "rock" and computer == "scissors":
    print("You win !!")
            
elif player == "paper" and computer == "rock":
    print("You win !!")
            
elif player == "scissors" and computer == "paper":
    print("You win !!")

else:
    print("You lose !!")"""

# FOR MULTIPLE PLAYS

options = ("rock" , "paper" , "scissors")
playing = True

while playing:
    player = None
    computer = random.choice(options)
    
    while player not in options:
        player = input("Enter a choice (""rock"" , ""paper"" , ""scissors"") : ")
        
    print("PLayer : " , player)
    print("Computer : " , computer)

    if player == computer:
        print("Its a tie")
                    
    elif player == "rock" and computer == "scissors":
        print("You win !!")
                
    elif player == "paper" and computer == "rock":
        print("You win !!")
                
    elif player == "scissors" and computer == "paper":
        print("You win !!")    

    else:
        print("You lose !!")

    playagain = input("Do you want to continue(y/n) : ").lower()

    if playagain == "y":
        playing

    elif playagain == "n":
        playing = False

    elif playagain != "y" or "n":
        print("invalid option")
        playagain = input("Do you want to continue(y/n) : ").lower()

        if playagain == "y":
            playing

        elif playagain == "n":
            playing = False

print("\n---------THANK YOU FOR PLAYING----------------")




























