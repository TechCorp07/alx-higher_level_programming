#!/usr/bin/python3
"""Defines function inherits_from"""


def inherits_from(obj, a_class):
    """Returns True if object is an instance of a sublass
    of the specified class"""
    if type(obj) != a_class and issubclass(type(obj), a_class):
        return True
    return False
