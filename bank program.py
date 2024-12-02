"""def showbalance(balance):
    print("*********************************")
    print(f"Your balance is {balance : .2f}")
    print("*********************************")
    
def deposit():
    print("*********************************")
    amount = float(input("Enter amount to deposit : "))
    print("*********************************")

    if amount < 0:
        print("*********************************")
        print("that is not a valid amount")
        print("*********************************")
        return 0
    else:
        return amount
    
def withdraw(balance):
    print("*********************************")
    amount = float(input("Enter amount to withdraw : "))
    print("*********************************")

    if amount > balance:
        print("Insufficient balance")
        return 0

    elif amount < 0:
        print("that is not a valid amount")
        return 0
    else:
        return amount
        print("amount deposited successfully")

def main():
    balance = 0
    isrunning = True
    
    while isrunning:
        print("*********************************")
        print("Show Balance")
        print("Deposit")
        print("Withdraw")
        print("Exit")
        print("*********************************")

        choice = float(input("Enter your number : "))


        if choice == 1:
            showbalance(balance)

        elif choice == 2:
            balance += deposit()

        elif choice == 3:
            balance -= withdraw(balance)

        elif choice == 4:
            isrunning = False

        else:
            print("Invalid input!!!")

    print("*********************************")
    print("Thank You!!!")
    print("*********************************")


if __name__ == "__main__":
    main()"""






































