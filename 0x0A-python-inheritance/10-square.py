#!/usr/bin/python3
"""Define class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square"""
    def __init__(self, size):
        """Initializer"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Returns area of Square instance"""
        return self.__size ** 2
