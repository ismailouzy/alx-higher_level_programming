#!/usr/bin/python3
""""a function that returns a tuple with the length
of a string and its first character."""


def multiple_returns(sentence):
    if sentence == "":
        sentence[0] = "None"
    else:
        result = (len(sentence), sentence[0])
        return (result)
