#!/usr/bin/python3
"""Defines is_same_class function"""


def is_same_class(obj, a_class):
    """Returns True if object is exactly an
    instance of specified class, else False"""
    return type(obj) is a_class
