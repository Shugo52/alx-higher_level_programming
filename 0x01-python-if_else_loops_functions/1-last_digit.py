#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lsd = int(str(number)[-1:])
if number < 0:
    lsd = lsd * -1
if lsd > 5:
    print(f"Last digit of {number} is {lsd} and is greater than 5")
elif lsd == 0:
    print(f"Last digit of {number} is {lsd} and is 0")
elif lsd < 6 and lsd != 0:
    print(f"Last digit of {number} is {lsd} and is less than 6 and not 0")