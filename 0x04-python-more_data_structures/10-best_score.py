#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        tmp = sorted(list(a_dictionary.values()))
        return (list(a_dictionary.keys())
                [list(a_dictionary.values()).index(tmp[-1])])
    else:
        return None
