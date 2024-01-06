#!/usr/bin/python3
""""a function that retrieves an element from a list."""


def element_at(my_list, idx):
    if idx < 0:
        return (0)
    elif idx > len(my_list) - 1:
        return ("None")
    else:
        return (my_list[idx])
