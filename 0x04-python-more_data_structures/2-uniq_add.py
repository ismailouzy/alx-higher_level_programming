#!/usr/bin/python3
def uniq_add(my_list=[]):
    ordr = set(my_list)
    sum = 0
    for i in ordr:
        sum += i
    return sum
