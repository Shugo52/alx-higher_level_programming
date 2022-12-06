#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = list(tuple_a[:2])
    b = list(tuple_b[:2])

    while len(a) < 2 or len(b) < 2:
        a.append(0)
        b.append(0)

    return tuple([a[i] + b[i] for i in range(2)])
