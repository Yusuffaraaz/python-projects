print("COUNTDOWN TIMER PROGRAM \n")

import time

mytime = int(input("Enter your time in seconds : "))

for x in range(mytime , 0 , -1):
    seconds = x%60
    minutes = int(x/60)%60
    hours = int(x/3600)
    print(f"{hours}:{minutes:02}:{seconds:03}")
    time.sleep(1)

print("TIMES'S UP")

