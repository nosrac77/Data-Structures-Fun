"""Module to implement Stack in Python ."""


class Stack(object):
    """Class to create instance of Stack implementation."""

    def __init__(self):
        """Create new instance of Stack class object."""

        self.stack = []
        self.top = None
        self.is_empty = True
