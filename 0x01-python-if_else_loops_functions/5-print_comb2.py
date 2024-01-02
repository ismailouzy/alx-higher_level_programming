#!/usr/bin/python3
for delta in range(0, 100):
    i = delta // 10
    j = delta % 10
    if delta != 99:
        print("{}{}".format(i, j), end=", ")
    else:
        print("{}{}".format(i, j))
