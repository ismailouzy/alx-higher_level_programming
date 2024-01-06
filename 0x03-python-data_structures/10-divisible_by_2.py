#!/usr/bin/python3
""""a function that finds all multiples of 2 in a list."""


def divisible_by_2(my_list=[]):
    res = []
    for i in my_list:
        if i % 2 == 0:
            res.append(True)
        else:
            res.append(False)
    return (res)
