#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    list1 = []
    temp = []
    dup = []
    for i in set_1, set_2:
        for j in i:
            if j not in list1:
                list1.append(j)
            else:
                dup.append(j)

    for q in list1:
        if q not in dup:
            temp.append(q)
    return temp
