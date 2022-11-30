#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lsb = number % 10 if number > -1 else number % -10
print(f"Last digit of {number:d} is {lsb:d} and is", end=" ")
print(f"{lsb:d}" if lsb == 0 else "less than 6 and not 0" if lsb < 6
      else "greater than 5")
