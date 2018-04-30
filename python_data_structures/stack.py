"""Module to implement Stack in Python ."""


class Stack(object):
    """Class to create instance of Stack implementation."""

    def __init__(self):
        """Create new instance of Stack class object."""

        self.stack = []
        self.top = None
        self.is_empty = True

    def push(self, data):
        """Method to add given data to Stack class object."""

        self.stack.insert(0, data)
        self.top = self.stack[0]
