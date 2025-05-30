#!/usr/bin/python3
def print_last_digit(number):
    """
    A function that prints the last digit of a number
    """
    if number < 0:
        mod = (number * -1) % 10
    else:
        mod = number % 10
    print("{}".format(mod), end="")
    return mod
