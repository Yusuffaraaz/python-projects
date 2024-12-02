import random

def spinrow():
    symbols = ["⭐" , "✨" , "✔" , " ⚽" ,  "⚾"]
    results=[]

    for symbol in range(3):
        results.append(random.choice(symbols))
    return results

    #return[random.choice(symbols) for _ in range(3)]

def printrow(row):
    print("*************")
    print(" | ".join(row))
    print("*************")

def getpayout(row , bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "⭐":
            return bet*2
        
        if row[0] == "✨":
            return bet*3
        
        if row[0] == "✔":
            return bet*5
        
        if row[0] == "⚽":
            return bet*10
        
        if row[0] == "⚾":
            return bet*20
    return 0

def main():
    balance = 100

    print("******************************")
    print("WELCOME TO PYTHON SLOT MACHINE")
    print("SYMBOLS :⭐ ✨ ✔ ⚽ ⚾")
    print("******************************")

    while balance > 0:
        print(f"Current balance : Rs{balance} \n")
        
        bet = input("Place your bet amount : ")

        if not bet.isdigit():
            print("Invalid Input Enter Number")
            continue
        
        bet = int(bet)

        if bet > balance:
            print("Insufficient Balance")
            continue

        if bet <= 0:
            print("Bet must be greater than 0")
            continue

        balance = balance - bet

        row = spinrow()
        print("Spinning......//\n")
        printrow(row)

        payout = getpayout(row , bet)

        if payout > 0:
            print(f"You won : Rs {payout}")
        else:
            print("Sorry you lost this round \n")

        balance = balance + payout

        playagain = input("Do ou want to spin again (y/n) : ").lower()

        if not playagain == "y":
            break
        
    print("\n*************************************************")    
    print(f"Game Over , Your total balance is : Rs {balance}")
    print("*************************************************")    
    
if __name__ == "__main__":
    main()
