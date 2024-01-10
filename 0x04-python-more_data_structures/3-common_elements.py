#!/usr/bin/python3
def common_elements(set_1, set_2):
    list1 = []
    dup = []
    for i in set_1, set_2:
        for j in i:
            if j not in list1:
                list1.append(j)
            else:
                dup.append(j)
    return dup
