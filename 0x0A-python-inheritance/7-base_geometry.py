#!/usr/bin/python3
"""
    BaseGeometry module
"""


class BaseGeometry():
    """
        Object Class
    """
    def area(self):
        """
            public instance
            Raise:
                Exception: Area not_ implemented

        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            Public instance  validates value
            Args:
                name (string): name
                value(int): Value
            Raises:
                TypeError: if value not int
                ValueError: if value less or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
