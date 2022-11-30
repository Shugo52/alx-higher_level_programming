#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = str
    if n < 0:
        return str
    return new_str[:n] + new_str[n + 1:]
