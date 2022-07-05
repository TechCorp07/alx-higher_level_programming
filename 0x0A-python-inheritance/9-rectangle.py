#!/usr/bin/python3
"""Defines class BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle shape class"""
    def __init__(self, width, height):
        """Initializer"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns informal representation of Rectangle instance"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
