#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    todel = []
    for i in a_dictionary:
        if a_dictionary[i] == value:
            todel.append(i)

    for i in todel:
        del a_dictionary[i]

    return a_dictionary
