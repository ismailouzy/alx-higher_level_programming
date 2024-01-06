#!/usr/bin/python3
"""" a function that replaces an element in a list
at a specific position without modifying the original list."""


def new_in_list(my_list, idx, element):
    if idx < 0:
        return (my_list.copy())
    elif idx > len(my_list) - 1:
        return (my_list.copy())
    else:
        lista = my_list.copy()
        lista[idx] = element
        return lista
