#!/usr/bin/python3
"""Defines save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """Writes Object to text file using JSON representation"""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
