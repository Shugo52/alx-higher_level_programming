#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as error:
        print("Exception: {}".format(error), file=stderr)
        return None


if __name__ == "__main__":
    safe_print_list()
