#!/usr/bin/python3
def roman_to_int(r_str=None) -> int:
    if r_str is None or type(r_str) is not str:
        return 0

    r_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    # Create and reverse a list of the roman strings
    r_list = list(r_str)[::-1]

    result = r_dict[r_list[0]]

    # Subtract value from result if previous value is less than value
    # else add value to result
    for i in range(1, len(r_list)):
        if r_dict[r_list[i]] < r_dict[r_list[i - 1]]:
            result -= r_dict[r_list[i]]
        else:
            result += r_dict[r_list[i]]

    return result
