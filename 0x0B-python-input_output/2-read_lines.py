#!/usr/bin/python3
"""Defines read_lines"""


def read_lines(filename="", nb_lines=0):
    """Reads n lines of text file and prints to stdout"""
    with open(filename) as f:
        if nb_lines <= 0:
            print(f.read(), end='')
        else:
            for line in range(nb_lines):
                print(f.readline(), end='')
