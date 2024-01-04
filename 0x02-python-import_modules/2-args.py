#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    lent = len(argv) - 1
    if lent == 0:
        print(f"{lent} arguments.")
    elif lent == 1:
        print(f"{lent} argument:")
    else:
        print(f"{lent} arguments:")
    for i in range(1, lent + 1):
        print(f"{i}: {argv[i]}")
