#!/usr/bin/python3
"""Defines class_to_json"""


def class_to_json(obj):
    """Returns dictionary description with simple data
    structure for JSON serialization of object"""
    return obj.__dict__
