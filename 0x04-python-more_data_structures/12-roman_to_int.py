#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }
    tot = 0
    prev_val = 0

    for i in reversed(roman_string):
        curr_val = roman[i]
        if curr_val < prev_val:
            tot -= curr_val
        else:
            tot += curr_val
        prev_val = curr_val

    return tot
