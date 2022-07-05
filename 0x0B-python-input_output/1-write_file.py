#!/usr/bin/python3
"""Defines number_of_lines"""


def number_of_lines(filename=""):
    """Returns number of lines in text file"""
    with open(filename) as f:
        lines = 0
        for line in f:
            lines += 1
        return lines
