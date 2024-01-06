#!/usr/bin/python3
""""a function that deletes the item at a specific position in a list."""


def delete_at(my_list=[], idx=0):
    res = my_list
    if idx < 0 or idx > len(my_list):
        return (my_list)
    else:
        res.remove(my_list[idx])
        return res
