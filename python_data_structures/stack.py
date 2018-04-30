"""Module to implement Stack in Python ."""


class Stack(object):
    """Class to create instance of Stack implementation."""

    def __init__(self):
        """Create new instance of Stack class object."""

        # One thing you may have noticed is that there is no Node class defined
        # above. That's because this implementation of the Stack has no need
        # to store data, or any pointers, in Nodes. Instead, we can take
        # advantage of Python's built-in array data type to create a fully-
        # functional implementation of a Stack. We do this below on line 16 by
        # assigning self.stack to equal an empty list.

        self.stack = []
        self.top = None
        self.is_empty = True

    def push(self, data):
        """Method to add given data to Stack class object."""

        self.stack.insert(0, data)
        self.top = self.stack[0]
        self.is_empty = False
