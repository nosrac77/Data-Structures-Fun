"""Module to implement Singly Linked List in Python."""


class Node(object):
    """Class to create instance of Node."""

    def __init__(self, data=None, next_node=None):
        """Create new intance of a Node class object."""

        self.data = data
        self.next_node = next_node


class SinglyLinkedList(object):
    """Class to create instance of Singly Linked List."""

    def __init__(self):
        """Create new instance of a Singly Linked List class object."""

        self.head = Node()
        self.next_node = None

    def add_node(self, data):
        """Method to add new Node to Singly Linked List."""

        # When we want to add a new Node to our Singly Linked List, all we have
        # to do is 1) create a variable that contains the current list's head
        # Node and 2) reassign the list's head Node to become a new instance
        # of our Node class.

        new_next_node = self.head

        # 1) On line 31 we create a new variable called new_next_node
        # and assign it's value to the list's current self.head. We'll then use
        # this variable below on step 2.

        self.head = Node(data, new_next_node)

        # 2) On line 37 we reassign the list's head Node to become the newly
        # added Node. It's data will be the data passed in as the
        # argument for our method and it's next_node will become what the old
        # head Node used to be.
