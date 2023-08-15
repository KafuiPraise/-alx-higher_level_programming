#!/usr/bin/python3
"""Writes a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """For  a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """
            Instantiate a new Rectangle object
        Args:
            width (int): width of the new Rectangle obj.
            height (int): height of the new Rectangle obj.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
