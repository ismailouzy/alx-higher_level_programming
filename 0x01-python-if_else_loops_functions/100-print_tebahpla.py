#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 == 0:
        temp = chr(i)
    else:
        temp = chr(i - 32)
    print("".join(f"{temp}"), end="")
