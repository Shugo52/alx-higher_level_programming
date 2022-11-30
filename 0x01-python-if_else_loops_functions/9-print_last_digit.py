#!/usr/bin/python3
def print_last_digit(number):
    print("{}".format((int(number) * -1) % 10 if int(number) < 0
          else int(number) % 10), end=(""))
    return ((int(number) * -1) % 10 if int(number) < 0 else int(number) % 10)
