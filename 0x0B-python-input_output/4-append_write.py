#!/usr/bin/python3
"""Defines append_write"""


def append_write(filename="", text=""):
    """Appends string to end of text file, returns num of chars added"""
    with open(filename, 'a') as f:
        return f.write(text)
