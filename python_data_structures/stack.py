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

        # As a side note, a Stack can also be fully implemented using the
        # Singly Linked List ADT.

        self.stack = []
        self.top = None
        self.is_empty = True

    def push(self, data):
        """Method to add given data to Stack class object."""

        # OVERVIEW
        # Since our stack is simply a Python list, we can take advantage of
        # Python built-in methods to add the given data to our Stack, making
        # this operation straightforward and simple. We also need to be sure
        # that we're properly reassinging the Stack's top attribute each time
        # this method is called.

        # Before we add the given data to our Stack, we'll first check to see
        # if the Stack is empty. If it is, we'll preemptively assign the
        # Stack's is_empty attribute to equal False. In this way we can be sure
        # is_empty is only reassigned if our Stack is empty. This check is
        # performed below on line 41 and the reassignment of the is_empty
        # attribute is performed on line 43.

        if self.is_empty:

            self.is_empty = False

        # The next step we take is to place the given data into our Stack.
        # Since our Stack is a Python list, we can use the built-in Python
        # method append() to add the data. This will place our newly added data
        # at the "end" of our list. We do this below on line 60.

        # As a side note, one could also use the Python built-in method
        # insert() to add the given data to the "beginning" (index zero) of our
        # list. This may make more intuitive sense. If the newly added data is
        # to become our Stack's new top, shouldn't it be placed at the "front"
        # or "beginning" of our list? This is a great point. The reason we're
        # using append() instead of insert() has to do with the runtimes of
        # both methods. Using append() to place the given data at the end of
        # our list is much faster than using insert() to place the given data
        # at the beginning of our list.

        self.stack.append(data)

        # Now that we've added the given data to our Stack, the only step left
        # is to reassign the top to equal the newest addition to our Stack.
        # Since we used the append() method to add the given data to the "end"
        # of our list, we can be sure top will get correctly reassigned if we
        # set it equal to the last element in our list. We do this below on
        # line 70 by setting it equal to self.stack[-1], which will always
        # point to the last element in our list.

        self.top = self.stack[-1]

    def pop(self):
        """Method to remove and return top of Stack class object."""

        # OVERVIEW
        # The goal of this method is to remove and return our Stack's top.
        # Since our Stack is essentially a Python list, we can (and will) use a
        # built-in method to accomplish this task, being careful to perform a
        # few checks and reassign the Stack's top along the way.

        # Below, on line...

        if not self.is_empty:

            old_top = self.stack.pop()

            if len(self.stack) == 0:

                self.is_empty = True
                self.top = None

            else:

                self.top = self.stack[-1]

            return old_top

        raise IndexError("""Cannot pop from an empty Stack.""")
