#!/usr/bin/python3
"""Adds all arguments to a python list and saves to file"""
import json
from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


try:
    my_list = load_from_json_file('add_item.json')
except:
    my_list = []
save_to_json_file(my_list + argv[1:], 'add_item.json')
