#!/usr/bin/python3
""""a function that removes all characters c and C from a string."""


def no_c(my_string):
    charact = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            charact = charact + i
    return charact
