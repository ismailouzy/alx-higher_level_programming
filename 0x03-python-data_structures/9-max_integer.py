#!/usr/bin/python3
""""a function that finds the biggest integer of a list."""


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return "None"
    else:
        res = my_list[0]
        for i in my_list:
            if i > res:
                res = i
    return (res)
