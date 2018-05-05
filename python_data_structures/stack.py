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

        # Below, on line 87, we check to see if our Stack isn't empty by
        # checking it's is_empty attribute (as the value for is_empty is always
        # a boolean, either True or False). If is_empty is set to False, we'll
        # perform the pop method as planned. If is_empty is set to True an
        # error is promptly raised as we can't pop from an empty Stack.

        if not self.is_empty:

            # If the Stack isn't empty, we'll land here. The first thing we'll
            # do is create a variable with which to return the Stack's top. On
            # line 99 below, this is accomplished by assigning a variable
            # old_top to the value of calling a Python built-in method pop() on
            # our Stack's stack attribute (which is a Python list). Since we
            # designed our Stack such that it's top refers to the element at
            # the "end" of our Stack list, we can call Python's built-in pop()
            # method on that list without any given parameters to remove and
            # return our Stack's top.

            old_top = self.stack.pop()

            # With the Stack's top removed we're already halfway done! Now all
            # we have to do is reassign the Stack's top and maybe the Stack's
            # is_empty attribute. But the reassignment of these attributes will
            # depend on if the Stack, after performing Python's built-in pop()
            # method, is currently empty or not. We check for this below on
            # line 108 by seeing if the length of our Stack list is equal to 0.

            if len(self.stack) == 0:

                # If the length of our Stack list is equal to 0, we know our
                # Stack is empty. Thus, the Stack's is_empty attribute must be
                # set to True. Without any elements to reference our Stack's
                # top also must be set to None. These two steps are performed
                # below.

                self.is_empty = True
                self.top = None

            else:

                # If the length of our Stack list isn't equal to zero, we know
                # our Stack isn't empty. Now the only action we need to take is
                # ensuring the Stack's top is reassigned to the next
                # appropriate element in the Stack list, which will be whatever
                # element is now contained at index negative one of the list.
                # This reassignment happens below.

                self.top = self.stack[-1]

            return old_top

        raise IndexError("""Cannot pop from an empty Stack.""")
