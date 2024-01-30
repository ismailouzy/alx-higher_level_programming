#!/usr/bin/python3
def magic_string():
    magic_string.hsseb = getattr(magic_string, 'hsseb', 0) + 1
    return ("BestSchool" + (", BestSchool" * (magic_string.hsseb - 1)))
