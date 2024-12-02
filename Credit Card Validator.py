print("CREDIT CARD VALIDATOR \n")

#1. Remove any " " or "-"
#2. Add all digits in odd places from left to right (sum of odd)
#3. double every second digit from right to left
# (If result is two digit add the two digits to get single digit (sum of even)
#5. sum the (sum of odd) and (sum of even) 
#6. If the sum is divisible by 10 then the card is valid
# 378282246310005

sumodddigits = 0
sumevendigits = 0
total = 0

# STEP 1
cardnumber = input("Enter your Credit Card number : ")
cardnumberorg = cardnumber
cardnumber = cardnumber.replace("-" , "")
cardnumber = cardnumber.replace(" " , "")
cardnumber = cardnumber[::-1]

# STEP 2
for x in cardnumber[::2]:
    sumodddigits = sumodddigits + int(x)

# STEP 3
for x in cardnumber[1::2]:
    x = int(x*2)

    if x >= 10:
        sumevendigits = sumevendigits + (1 + (x%10))
    else:
        sumevendigits = sumevendigits + x
                                         
# STEP 4
total = sumodddigits + sumevendigits

# STEP 5

if total % 10 == 0:
    print("Card Number :" , cardnumberorg , "IS VALID")
else:
    print("Card Number :" , cardnumberorg , "IS INVALID")
