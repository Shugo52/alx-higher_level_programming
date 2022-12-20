#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        c = a / b
        return c
    except ZeroDivisionError:
        c = None
        return None
    finally:
        print("Inside result: {}".format(c))


if __name__ == "__main__":
    safe_print_list()
