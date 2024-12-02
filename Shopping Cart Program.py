print("SHOPPING CART PROGRAM \n")

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit) : ")
    
    if food.lower() == "q" :
        break
    
    else:
        price = float(input(f"Enter price of the {food} : Rs "))
        foods.append(food)
        prices.append(price)
        
print("\n-----YOUR CART-----")

print("Your total food items are :")
for food in foods:
    print(food , end = " ")
print()

for price in prices:
    total = total + price

print(f"Your total price is : Rs{total}")
