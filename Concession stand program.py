print("CONCESSION STAND \n")

menu = {
        "pizza" : 100,
        "nachos" : 200,
        "popcorn" : 200,
        "fries" : 200,
        "chips" : 100,
        "soda" : 100,
        "lemonade" : 100
        }
cart = []
total = 0

print("------------MENU---------------")
for key , value in menu.items():
    print(f"{key:10} : Rs{value:.2f}")
print("-------------------------------")

while True:
    food = input("Select an intem from above (q to quit)")

    if food.lower() == "q":
        break

    elif menu.get(food) is not None:
        cart.append(food)

print("----------YOUR ORDER------------")
for food in cart:
    total = total + menu.get(food)
    print(food , end =" ")
print()

print(f"Your total is : Rs{total}")    
