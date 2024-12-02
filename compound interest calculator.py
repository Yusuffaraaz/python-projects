print("COMPOUND INTEREST CALCULATOR \n")

principle = 0
rate = 0
time = 0

while principle<=0:
    principle = float(input("Enter the principle amount : "))
    if principle <=0:
        print("principle cant be less than or equal to zero")
   
rate = float(input("Enter the interest rate : "))
if rate <=0:
    print("principle cant be less than or equal to zero")

time = float(input("Enter the time in years : "))
if time <=0:
    print("time cant be less than or equal to zero")
    
print(principle)
print(rate)
print(time)

total = principle *pow((1 + rate / 100) , time)

print(f"Balance after {time}year/s : Rs {total : .2f}")
