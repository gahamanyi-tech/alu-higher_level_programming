#!/usr/bin/python3
"""Module that formats text with double newlines after '.', '?', and ':'."""


def text_indentation(text):
    """Prints a text with 2 new lines after each of: '.', '?' and ':'."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    length = len(text)
    while i < length:
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            i += 1
            while i < length and text[i] == ' ':
                i += 1
            continue
        i += 1
