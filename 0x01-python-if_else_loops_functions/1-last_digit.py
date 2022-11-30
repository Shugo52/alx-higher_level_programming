#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lsd = int(str(number)[-1:])
if number < 0:
    lsd = lsd * -1
if lsd > 5:
    print("Last digit of {} is {} and is greater than 5"
          .format(number, lsd))
elif lsd == 0:
    print("Last digit of {} is {} and is 0".format(number, lsd))
elif lsd < 6 and lsd != 0:
    print("Last digit of {} is {} and is less than 6 and not 0"
          .format(number, lsd))
