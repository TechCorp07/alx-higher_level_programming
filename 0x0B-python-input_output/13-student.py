#!/usr/bin/python3
"""Defines class Student"""


class Student:
    """Student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves dictionary rep of Student instance"""
        if attrs is None:
            return self.__dict__
        my_dict = {}
        for _ in attrs:
            for k, v in self.__dict__.items():
                if k == _:
                    my_dict.update({k: v})
        return my_dict

    def reload_from_json(self, json):
        """Replaces all attributes of Student instance"""
        for k, v in json.items():
            setattr(self, k, v)
