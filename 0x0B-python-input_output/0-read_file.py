#!/usr/bin/python3
"""Defines read_file"""


def read_file(filename=""):
    """Prints a file"""
    with open(filename) as f:
        print(f.read(), end='')
