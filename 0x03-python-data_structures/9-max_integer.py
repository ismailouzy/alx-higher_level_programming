#!/usr/bin/python3
""""a function that finds the biggest integer of a list."""


def max_integer(my_list=[]):
    if not my_list:
        return (None)
    else:
        res = 0
        for i in my_list:
            if (i+1) > res:
                res = i
    return (res)
