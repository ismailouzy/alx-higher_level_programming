#!/usr/bin/python3
"""a function that prints a text with 2
new lines after each of these characters: ., ? and :"""


def text_indentation(text):
    """a function that prints a text
        Args:
            text: the text to work on"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    special_characters = {'.', '?', ':'}
    modified_text = ""
    newline_count = 0
    for char in text.strip():
        if char in " " and "\n\n\
        " in modified_text and newline_count == 2 and char in "  ":
            continue
        modified_text += char
        if char in special_characters:
            modified_text += "\n\n"
            newline_count = 2
        elif char == '\n':
            newline_count = 0
        elif newline_count > 0:
            newline_count -= 1
    print(modified_text, end="")
