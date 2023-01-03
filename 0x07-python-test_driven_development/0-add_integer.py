#!/usr/bin/python3

def add_integer(a=None, b=98):
    '''Adds two integers

        Args:
            a: first integer
            b: second integer

        Returns: sum of integers
    '''
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    
    try:
        a, b = int(a), int(b)
    except Exception as e:
        raise e

    return a + b


if __name__ == "__main__":
    add_integer()
