#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    toscore = 0
    toweight = 0

    for i, j in my_list:
        toscore += i * j
        toweight += j

    avg = toscore / toweight
    return avg
