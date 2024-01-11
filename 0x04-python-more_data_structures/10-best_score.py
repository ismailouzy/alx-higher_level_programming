#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    maxim = 0
    for i in a_dictionary:
        if a_dictionary[i] > maxim:
            maxim = a_dictionary[i]
    return maxim
