#!/usr/bin/python3
""" Gives a rebel integer
"""


class MyInt(int):
    """ is a rebel. MyInt has == and != operators inverted.
    """
    def __eq__(self, value):
        """ Do the opposite of ==
        """
        return super().__ne__(value)

    def __ne__(self, value):
        """ override !=
        """
        return super().__eq__(value)
