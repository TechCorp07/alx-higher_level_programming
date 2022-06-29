#!/usr/bin/python3
"""Contains class LockedClass"""


class LockedClass:
    """LockedClass prevents the user form dynamically creating
    new instance attributes, except if the new instance attribute
    is called first_name
    """

    __slots__ = "first_name"

    def __init__(self):
        """initialize instances"""
        self.first_name = any
